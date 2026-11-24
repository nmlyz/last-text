#!/usr/bin/env python3
"""Write one last text message to entry.txt.

The message is the final words a phone sends as its battery hits
1 percent: it lists what it survived (three drops, one toilet, two
updates) and names what finally killed it (a four-hour TikTok
session). One line, 91 characters, inside the 200-character limit.
The line goes to ``entry.txt`` under OUTPUT_DIR (default
``/output``). Output is deterministic: two runs produce
byte-identical files.
"""

import os

TEXT = "I survived 3 drops, 1 toilet, and 2 updates. What killed me was your 4-hour TikTok session."
LIMIT = 199


def _check(text):
    if "\n" in text or "\r" in text:
        raise ValueError("text must be a single line")
    if not text or len(text) > LIMIT:
        raise ValueError("text must be 1-199 characters")
    if text != text.strip():
        raise ValueError("text must not have surrounding whitespace")
    text.encode("utf-8")


def _write_text():
    _check(TEXT)
    directory = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    _write_text()
