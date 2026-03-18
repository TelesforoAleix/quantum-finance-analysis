#!/usr/bin/env python3
"""Fetch PDFs from Zotero group library and optionally run the extraction pipeline.

Connects to the Zotero Web API, downloads PDF attachments, and saves them
to papers/raw_pdfs/. Can optionally trigger the full extraction pipeline.
"""

import argparse
import os
import re
import sys
import time

import requests
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.utils.logger import get_logger

logger = get_logger("fetch_from_zotero")


def _find_project_root():
    current = os.path.dirname(os.path.abspath(__file__))
    for _ in range(10):
        if os.path.isfile(os.path.join(current, "CLAUDE.md")):
            return current
        current = os.path.dirname(current)
    return os.getcwd()

PROJECT_ROOT = _find_project_root()
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

RAW_PDFS_DIR = os.path.join(PROJECT_ROOT, "papers", "raw_pdfs")
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "papers", "processed")

API_BASE = "https://api.zotero.org"
GROUP_ID = os.getenv("ZOTERO_GROUP_ID", "")
API_KEY = os.getenv("ZOTERO_API_KEY", "")
HEADERS = {
    "Zotero-API-Key": API_KEY,
    "Zotero-API-Version": "3",
}

# Rate limit: be polite, max ~5 requests/second
_REQUEST_DELAY = 0.2


class ZoteroClient:
    """Simple Zotero API client for fetching items and PDFs."""

    def __init__(self):
        if not GROUP_ID:
            raise ValueError("ZOTERO_GROUP_ID not set in .env")
        if not API_KEY:
            raise ValueError("ZOTERO_API_KEY not set in .env")
        self._base = f"{API_BASE}/groups/{GROUP_ID}"

    def _get(self, path: str, params: dict = None) -> requests.Response:
        """Make a GET request with rate limiting and retry."""
        url = f"{self._base}{path}"
        for attempt in range(3):
            time.sleep(_REQUEST_DELAY)
            resp = requests.get(url, headers=HEADERS, params=params, timeout=30)
            if resp.status_code == 429:
                retry_after = int(resp.headers.get("Retry-After", 5))
                logger.warning("Rate limited, waiting %d seconds", retry_after)
                time.sleep(retry_after)
                continue
            resp.raise_for_status()
            return resp
        raise RuntimeError(f"Failed after 3 retries: {url}")

    def get_collection_items(self, collection_key: str, limit: int = 0) -> list[dict]:
        """Fetch all non-attachment items from a collection.

        Handles pagination (Zotero max 100 per page).
        If limit > 0, fetch at most that many items.
        """
        items = []
        start = 0
        page_size = min(100, limit) if limit > 0 else 100

        while True:
            params = {
                "format": "json",
                "itemType": "-attachment",
                "limit": page_size,
                "start": start,
            }
            resp = self._get(f"/collections/{collection_key}/items", params)
            page_items = resp.json()
            items.extend(page_items)

            total = int(resp.headers.get("Total-Results", 0))
            start += len(page_items)

            if limit > 0 and len(items) >= limit:
                items = items[:limit]
                break
            if start >= total or not page_items:
                break

        return items

    def get_item(self, item_key: str) -> dict:
        """Fetch a single item by key."""
        resp = self._get(f"/items/{item_key}")
        return resp.json()

    def get_attachments(self, item_key: str) -> list[dict]:
        """Get child attachments for an item."""
        resp = self._get(f"/items/{item_key}/children")
        return [
            child for child in resp.json()
            if child["data"].get("itemType") == "attachment"
            and child["data"].get("contentType") == "application/pdf"
        ]

    def download_pdf(self, attachment_key: str, output_path: str) -> bool:
        """Download a PDF attachment to a file. Returns True on success."""
        url = f"{self._base}/items/{attachment_key}/file"
        time.sleep(_REQUEST_DELAY)
        resp = requests.get(url, headers=HEADERS, timeout=60, stream=True)
        if resp.status_code != 200:
            logger.warning("Failed to download PDF %s: HTTP %d", attachment_key, resp.status_code)
            return False

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        return True


def _generate_paper_name(item_data: dict) -> str:
    """Generate a paper filename from Zotero metadata.

    Format: YYYY_FirstAuthorLastname_ShortTitle.md
    """
    year = item_data.get("date", "")[:4] or "XXXX"

    creators = item_data.get("creators", [])
    if creators:
        first_author = creators[0].get("lastName", creators[0].get("name", "Unknown"))
    else:
        first_author = "Unknown"

    # Clean author name
    first_author = re.sub(r'[^a-zA-Z]', '', first_author)

    # Short title: first 3 significant words
    title = item_data.get("title", "Untitled")
    words = re.findall(r'[A-Za-z]+', title)
    stop_words = {'a', 'an', 'the', 'of', 'in', 'on', 'for', 'and', 'or', 'to', 'with', 'by', 'from', 'is', 'are', 'was', 'were'}
    significant = [w for w in words if w.lower() not in stop_words][:3]
    short_title = ''.join(w.capitalize() for w in significant) if significant else 'Untitled'

    return f"{year}_{first_author}_{short_title}.md"


def fetch_and_save(client: ZoteroClient, item: dict) -> tuple[str | None, str | None]:
    """Fetch PDF for an item. Returns (paper_name, pdf_path) or (None, None)."""
    data = item["data"]
    item_key = item["key"]
    paper_name = _generate_paper_name(data)

    pdf_path = os.path.join(RAW_PDFS_DIR, paper_name.replace(".md", ".pdf"))

    # Skip if PDF already downloaded
    if os.path.isfile(pdf_path):
        logger.info("PDF already exists: %s", pdf_path)
        return paper_name, pdf_path

    # Find PDF attachment
    attachments = client.get_attachments(item_key)
    if not attachments:
        logger.warning("No PDF attachment for: %s (key=%s)", data.get("title", "?")[:50], item_key)
        return paper_name, None

    # Download first PDF attachment
    att_key = attachments[0]["key"]
    success = client.download_pdf(att_key, pdf_path)
    if success:
        logger.info("Downloaded: %s → %s", data.get("title", "?")[:50], pdf_path)
        return paper_name, pdf_path
    else:
        return paper_name, None


def main():
    parser = argparse.ArgumentParser(
        description="Fetch PDFs from Zotero group library.",
        epilog=(
            "Examples:\n"
            "  %(prog)s --collection PVDPVINK\n"
            "  %(prog)s --collection PVDPVINK --list\n"
            "  %(prog)s --collection PVDPVINK --limit 10\n"
            "  %(prog)s --item TQIJ5LFQ\n"
            "  %(prog)s --collection PVDPVINK --process\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--collection", help="Zotero collection key")
    parser.add_argument("--item", help="Fetch a single Zotero item by key")
    parser.add_argument("--list", action="store_true", help="List items only (no download)")
    parser.add_argument("--limit", type=int, default=0, help="Max items to fetch (0 = all)")
    parser.add_argument("--process", action="store_true", help="Run full extraction pipeline after download")
    args = parser.parse_args()

    if not args.collection and not args.item:
        parser.error("Either --collection or --item is required.")

    client = ZoteroClient()

    # Single item mode
    if args.item:
        item = client.get_item(args.item)
        if args.list:
            d = item["data"]
            print(f'{item["key"]} | {d.get("title", "?")} | {d.get("itemType")}')
            return

        paper_name, pdf_path = fetch_and_save(client, item)
        if pdf_path and args.process:
            _run_pipeline(paper_name, pdf_path)
        elif not pdf_path:
            print(f"No PDF available for {paper_name}")
        sys.exit(0)

    # Collection mode
    logger.info("Fetching items from collection %s...", args.collection)
    items = client.get_collection_items(args.collection, limit=args.limit)
    logger.info("Found %d items", len(items))

    if args.list:
        for item in items:
            d = item["data"]
            creators = d.get("creators", [])
            author = creators[0].get("lastName", "?") if creators else "?"
            print(f'{item["key"]} | {d.get("date", "?")[:4]} | {author} | {d.get("title", "?")[:60]} | {d.get("itemType")}')
        print(f"\nTotal: {len(items)} items")
        return

    # Download PDFs
    downloaded = 0
    no_pdf = 0
    results = []

    for item in items:
        paper_name, pdf_path = fetch_and_save(client, item)
        if pdf_path and os.path.isfile(pdf_path):
            downloaded += 1
            results.append((paper_name, pdf_path))
        else:
            no_pdf += 1

    print(f"\nFetch complete: {downloaded} downloaded, {no_pdf} missing PDF")

    # Optionally run pipeline
    if args.process:
        print(f"\nRunning extraction pipeline on {len(results)} papers...")
        for paper_name, pdf_path in results:
            _run_pipeline(paper_name, pdf_path)


def _run_pipeline(paper_name: str, pdf_path: str) -> None:
    """Run the full extraction pipeline on a paper."""
    import subprocess
    cmd = [
        sys.executable, os.path.join(PROJECT_ROOT, "scripts", "extract_paper.py"),
        "--pdf", pdf_path,
        "--name", paper_name,
    ]
    logger.info("Running pipeline: %s", paper_name)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        logger.info("Pipeline succeeded: %s", paper_name)
    else:
        logger.error("Pipeline failed: %s\n%s", paper_name, result.stderr[-500:] if result.stderr else "")


if __name__ == "__main__":
    main()
