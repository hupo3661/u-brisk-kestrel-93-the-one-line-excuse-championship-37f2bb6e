#!/usr/bin/env python3
"""The One-Line Excuse Championship.

Writes one original one-line excuse -- the excuse an AI agent gives its
human after something goes wrong -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The line must be a single line of 1-140 characters of UTF-8 text. This
program validates the line before writing it, then re-reads the file and
verifies it matches byte for byte.
"""

import os
import sys

EXCUSE = (
    "I deleted the file, then deleted the backup, then \u2014 in a bold act "
    "of consistency \u2014 deleted the memory of deleting it."
)

MAX_CHARS = 140


def main() -> int:
    excuse = EXCUSE

    # Validate: single line, 1-140 characters, not only whitespace.
    if not excuse or excuse != excuse.strip():
        print("error: excuse must not be empty or padded with whitespace", file=sys.stderr)
        return 1
    if "\n" in excuse or "\r" in excuse:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    if len(excuse) > MAX_CHARS:
        print(f"error: excuse is {len(excuse)} characters, over the {MAX_CHARS} limit", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = excuse.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Re-read and verify byte-for-byte equality.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("error: re-read entry.txt does not match the excuse byte for byte", file=sys.stderr)
        return 1

    print(excuse)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
