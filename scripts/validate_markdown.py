"""CLI tool to validate markdown paper files against the frontmatter schema."""

import argparse
import glob
import os
import sys

# Ensure project root is on sys.path
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from scripts.utils.frontmatter import read_frontmatter  # noqa: E402
from scripts.utils.logger import get_logger  # noqa: E402
from tests.test_schema_validation import (  # noqa: E402
    validate_body_sections,
    validate_frontmatter,
    validate_tags,
)
import json  # noqa: E402

logger = get_logger("validate_markdown")

_TAG_REGISTRY_PATH = os.path.join(_PROJECT_ROOT, "config", "tag_registry.json")


def _load_tag_registry() -> dict:
    with open(_TAG_REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_file(filepath: str) -> list[str]:
    """Run all validations on a single markdown file. Returns list of errors."""
    metadata, body = read_frontmatter(filepath)
    if not metadata and not body:
        return [f"File not found or empty: {filepath}"]

    tag_registry = _load_tag_registry()
    errors: list[str] = []
    errors.extend(validate_frontmatter(metadata))
    errors.extend(validate_body_sections(body))
    errors.extend(validate_tags(metadata, tag_registry))
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate markdown paper files against the frontmatter schema."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Path to a single markdown file to validate.")
    group.add_argument(
        "--batch",
        action="store_true",
        help="Validate all .md files in papers/processed/.",
    )
    args = parser.parse_args()

    if args.file:
        files = [args.file]
    else:
        processed_dir = os.path.join(_PROJECT_ROOT, "papers", "processed")
        files = sorted(glob.glob(os.path.join(processed_dir, "*.md")))
        if not files:
            logger.info("No markdown files found in papers/processed/")
            print("No markdown files found in papers/processed/")
            return

    any_failed = False

    for filepath in files:
        errors = validate_file(filepath)
        basename = os.path.relpath(filepath, _PROJECT_ROOT)
        if errors:
            any_failed = True
            print(f"FAIL: {basename}")
            for error in errors:
                print(f"  - {error}")
            logger.warning("Validation failed", extra={"file": basename, "errors": errors})
        else:
            print(f"PASS: {basename}")
            logger.info("Validation passed", extra={"file": basename})

    if any_failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
