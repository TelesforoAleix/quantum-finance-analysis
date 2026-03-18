#!/usr/bin/env python3
"""Sync processed markdown files to an Obsidian vault directory.

If the vault path is the same as papers/processed/ (default), no sync is needed.
Otherwise, copies new or updated .md files to the vault.

Usage:
    python scripts/sync_obsidian.py
    python scripts/sync_obsidian.py --vault-path /path/to/obsidian/vault
"""

import argparse
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.utils.logger import get_logger

logger = get_logger("sync_obsidian")


def _find_project_root() -> str:
    """Walk up from this file to find the directory containing CLAUDE.md."""
    current = os.path.dirname(os.path.abspath(__file__))
    for _ in range(10):
        if os.path.isfile(os.path.join(current, "CLAUDE.md")):
            return current
        current = os.path.dirname(current)
    return os.getcwd()


PROJECT_ROOT = _find_project_root()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync processed papers to Obsidian vault.",
    )
    parser.add_argument(
        "--vault-path",
        help="Obsidian vault directory (default: from extraction_config.json)",
    )
    args = parser.parse_args()

    source_dir = os.path.join(PROJECT_ROOT, "papers", "processed")

    if args.vault_path:
        vault_path = os.path.abspath(args.vault_path)
    else:
        config_path = os.path.join(PROJECT_ROOT, "config", "extraction_config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        vault_rel = config.get("obsidian_vault_path", "papers/processed")
        vault_path = os.path.abspath(os.path.join(PROJECT_ROOT, vault_rel))

    # Check if source and destination are the same
    if os.path.realpath(source_dir) == os.path.realpath(vault_path):
        print(f"Obsidian vault is already pointed at {source_dir}")
        print("No sync needed — Obsidian reads files directly from papers/processed/")
        sys.exit(0)

    # Sync files
    if not os.path.isdir(source_dir):
        logger.error("Source directory not found: %s", source_dir)
        sys.exit(1)

    os.makedirs(vault_path, exist_ok=True)

    md_files = [f for f in os.listdir(source_dir) if f.endswith(".md")]
    copied = 0
    skipped = 0

    for fname in sorted(md_files):
        src = os.path.join(source_dir, fname)
        dst = os.path.join(vault_path, fname)

        # Skip if destination is up-to-date
        if os.path.isfile(dst):
            src_mtime = os.path.getmtime(src)
            dst_mtime = os.path.getmtime(dst)
            if dst_mtime >= src_mtime:
                skipped += 1
                continue

        shutil.copy2(src, dst)
        copied += 1
        logger.info("Copied %s", fname)

    print(
        f"Sync complete: {copied} copied, {skipped} up-to-date, "
        f"{len(md_files)} total"
    )


if __name__ == "__main__":
    main()
