"""Token-aware text truncation and chunking."""

import re


# Approximate ratio: 1 token ≈ 4 characters
_CHARS_PER_TOKEN = 4


def truncate_tokens(text: str, max_tokens: int) -> str:
    """Truncate text to approximately max_tokens.

    Uses a simple heuristic: 1 token ≈ 4 characters.
    If max_tokens is 0, return the full text (no truncation).
    """
    if max_tokens <= 0:
        return text

    max_chars = max_tokens * _CHARS_PER_TOKEN
    if len(text) <= max_chars:
        return text

    return text[:max_chars]


def chunk_by_sections(text: str, max_tokens: int) -> list[str]:
    """Split text into chunks at section boundaries.

    Splits on markdown headings (lines starting with #) and double newlines.
    Each chunk should be under max_tokens.
    Returns a list of text chunks.
    """
    if max_tokens <= 0:
        return [text]

    max_chars = max_tokens * _CHARS_PER_TOKEN

    if len(text) <= max_chars:
        return [text]

    # Split on heading lines or double newlines
    parts = re.split(r"(?=^#{1,3}\s)", text, flags=re.MULTILINE)

    # If heading-based splitting didn't help, split on double newlines
    if len(parts) <= 1:
        parts = re.split(r"\n\n+", text)

    chunks: list[str] = []
    current = ""

    for part in parts:
        if not part:
            continue

        # If adding this part would exceed the limit, flush the current chunk
        if current and len(current) + len(part) > max_chars:
            chunks.append(current.strip())
            current = ""

        # If a single part is longer than max_chars, split it by characters
        if len(part) > max_chars:
            if current:
                chunks.append(current.strip())
                current = ""
            for i in range(0, len(part), max_chars):
                chunks.append(part[i : i + max_chars].strip())
        else:
            current += part

    if current.strip():
        chunks.append(current.strip())

    return chunks if chunks else [text]
