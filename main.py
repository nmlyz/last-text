#!/usr/bin/env python3
"""Last Text -- submission generator.

Writes one last text message to ``entry.txt`` inside OUTPUT_DIR
(default ``/output``). The message is the phone's own last words at
1 percent battery: 91 characters, inside the 200 limit (92 with the
trailing newline the file carries, still inside the limit).
The output is deterministic: running the script twice produces
byte-identical files.
"""

import os
from pathlib import Path

LINE = "I survived 3 drops, 1 toilet, and 2 updates. What killed me was your 4-hour TikTok session."

OUTPUT_DIR_ENV = "OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"
MAX_LINE_LENGTH = 200


def validate_line(line: str) -> None:
    """Check the line meets the submission rules before writing it."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if not 1 <= len(line) < MAX_LINE_LENGTH:
        raise ValueError("line must be 1-199 characters")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    # The gate reads the file as UTF-8 text, so prove it encodes cleanly.
    line.encode("utf-8")


def main() -> None:
    os.umask(0o022)
    output_dir = Path(os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)

    validate_line(LINE)

    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_text(LINE + "\n", encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
