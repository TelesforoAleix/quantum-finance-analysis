#!/usr/bin/env python3
"""Full pipeline orchestrator — runs all 6 extraction steps on a single paper.

Usage:
    python scripts/extract_paper.py --pdf papers/raw_pdfs/paper.pdf --name 2024_Author_Title.md
    python scripts/extract_paper.py --pdf papers/raw_pdfs/paper.pdf --name 2024_Author_Title.md --from-step 3
"""

import argparse
import os
import shutil
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.extract_pdf_text import extract_text
from scripts.utils.logger import get_logger
from scripts.utils.step_runner import run_step

logger = get_logger("extract_paper")


def _find_project_root() -> str:
    """Walk up from this file to find the directory containing CLAUDE.md."""
    current = os.path.dirname(os.path.abspath(__file__))
    for _ in range(10):
        if os.path.isfile(os.path.join(current, "CLAUDE.md")):
            return current
        current = os.path.dirname(current)
    return os.getcwd()


PROJECT_ROOT = _find_project_root()
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "papers", "processed")
RAW_PDFS_DIR = os.path.join(PROJECT_ROOT, "papers", "raw_pdfs")
TEMPLATE_PATH = os.path.join(PROJECT_ROOT, "templates", "paper_base.md")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run full extraction pipeline on a single paper.",
    )
    parser.add_argument("--pdf", required=True, help="Path to the PDF file")
    parser.add_argument(
        "--name",
        required=True,
        help="Output filename (e.g. 2024_Author_Title.md)",
    )
    parser.add_argument(
        "--from-step",
        type=int,
        default=1,
        choices=range(1, 7),
        dest="from_step",
        help="Start from this step (default: 1)",
    )
    args = parser.parse_args()

    # Validate PDF
    if not os.path.isfile(args.pdf):
        logger.error("PDF not found: %s", args.pdf)
        sys.exit(1)

    paper_name = args.name
    if not paper_name.endswith(".md"):
        paper_name += ".md"

    paper_path = os.path.join(PROCESSED_DIR, paper_name)

    # Create paper file from template if needed
    if not os.path.isfile(paper_path):
        os.makedirs(PROCESSED_DIR, exist_ok=True)
        shutil.copy2(TEMPLATE_PATH, paper_path)
        logger.info("Created paper file from template: %s", paper_name)

    # Extract PDF text (or load from cache)
    cache_path = os.path.join(RAW_PDFS_DIR, paper_name.replace(".md", ".txt"))
    if os.path.isfile(cache_path):
        logger.info("Loading cached PDF text from %s", cache_path)
        with open(cache_path, "r", encoding="utf-8") as f:
            pdf_text = f.read()
    else:
        pdf_text, is_valid = extract_text(args.pdf)
        if not is_valid:
            logger.warning(
                "PDF has very little extractable text (likely scanned): %s",
                args.pdf,
            )
        os.makedirs(RAW_PDFS_DIR, exist_ok=True)
        with open(cache_path, "w", encoding="utf-8") as f:
            f.write(pdf_text)
        logger.info("Cached PDF text to %s", cache_path)

    # Run steps
    steps = list(range(args.from_step, 7))
    succeeded: list[int] = []
    failed: list[int] = []

    for step_num in steps:
        try:
            run_step(
                paper_path,
                step_num,
                pdf_text=pdf_text if step_num <= 5 else None,
            )
            succeeded.append(step_num)
            logger.info("Step %d completed successfully", step_num)
        except Exception as exc:
            logger.error("Step %d failed: %s", step_num, exc)
            failed.append(step_num)
            break  # Stop on first failure

    # Summary
    print(f"\n{'=' * 50}")
    print(f"Paper: {paper_name}")
    print(f"Steps completed: {succeeded}")
    if failed:
        print(f"Steps failed: {failed}")
        skipped = [s for s in steps if s not in succeeded and s not in failed]
        if skipped:
            print(f"Steps skipped: {skipped}")
    print(f"Output: {paper_path}")
    print(f"{'=' * 50}")

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
