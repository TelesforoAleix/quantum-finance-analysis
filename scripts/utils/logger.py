"""Structured JSON-lines logging for all pipeline steps."""

import json
import logging
import os
import sys
from datetime import datetime, timezone


class _JsonFormatter(logging.Formatter):
    """Format log records as JSON-lines."""

    def format(self, record: logging.LogRecord) -> str:
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
        }
        # Include any extra fields passed via the `extra` kwarg
        for key in record.__dict__:
            if key not in logging.LogRecord(
                "", 0, "", 0, "", (), None
            ).__dict__ and key not in ("message", "msg"):
                entry[key] = record.__dict__[key]
        return json.dumps(entry)


class _ConsoleFormatter(logging.Formatter):
    """Human-readable console format: LEVEL: message."""

    def format(self, record: logging.LogRecord) -> str:
        return f"{record.levelname}: {record.getMessage()}"


def get_logger(name: str) -> logging.Logger:
    """Return a logger that writes JSON-lines to logs/ and outputs to stderr.

    File handler: logs/{YYYY-MM-DD}_{name}.jsonl at DEBUG level.
    Console handler: stderr at INFO level in human-readable format.
    Avoids adding duplicate handlers on repeated calls.
    """
    logger = logging.getLogger(f"qfin.{name}")

    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # Ensure logs/ directory exists (project root)
    project_root = _find_project_root()
    logs_dir = os.path.join(project_root, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # File handler — JSON-lines
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(logs_dir, f"{date_str}_{name}.jsonl")
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(_JsonFormatter())
    logger.addHandler(file_handler)

    # Console handler — human-readable on stderr
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(_ConsoleFormatter())
    logger.addHandler(console_handler)

    return logger


def _find_project_root() -> str:
    """Walk up from this file to find the directory containing CLAUDE.md."""
    current = os.path.dirname(os.path.abspath(__file__))
    for _ in range(10):
        if os.path.isfile(os.path.join(current, "CLAUDE.md")):
            return current
        current = os.path.dirname(current)
    # Fallback to cwd
    return os.getcwd()
