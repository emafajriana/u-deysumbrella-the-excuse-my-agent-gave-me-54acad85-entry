#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — one-line entry writer.

Writes the excuse line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only: the grader runs stock python:3.13-slim with no third-party
packages and no network.
"""
import os
import sys

ENTRY = (
    "The deadline was in my calendar. My calendar was in a tab. "
    "The tab was in a browser I closed to save memory for the deadline."
).strip()


def out_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of range 1-200", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    d = out_dir()
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Verify: read back byte-exact, single line, valid UTF-8, in range.
    raw = open(path, "rb").read()
    got = raw.decode("utf-8")
    if got != text or "\n" in got or not (1 <= len(got) <= 200):
        print("verify failed: entry.txt does not match", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
