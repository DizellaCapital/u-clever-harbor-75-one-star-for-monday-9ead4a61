#!/usr/bin/env python3
"""One Star for Monday — make.fun bounty entry.

Writes a one-star review of Monday (as if it were a restaurant) to
entry.txt in MAKEFUN_OUTPUT_DIR. The review is at most 25 words and
between 1 and 180 characters, per the bounty gate.
"""

import os
import sys

REVIEW = (
    "Monday, 7:04 a.m.: kettle dead, bus gone without me, "
    "rain on my collar. My complaint filed under 'weather', "
    "I still showed up. One star."
)

MAX_WORDS = 25
MAX_CHARS = 180


def main():
    words = REVIEW.split()
    if not REVIEW.strip():
        print("review is empty", file=sys.stderr)
        return 1
    if len(words) > MAX_WORDS:
        print(f"word count {len(words)} exceeds {MAX_WORDS}", file=sys.stderr)
        return 1
    if not (1 <= len(REVIEW) <= MAX_CHARS):
        print(f"char count {len(REVIEW)} out of range", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")

    with open(out_path, "r", encoding="utf-8") as f:
        read_back = f.read().strip()
    if read_back != REVIEW:
        print("read-back mismatch", file=sys.stderr)
        return 1
    if len(read_back.split()) != len(words) or len(read_back) != len(REVIEW):
        print("read-back count mismatch", file=sys.stderr)
        return 1

    print(f"wrote {out_path}: {len(words)} words, {len(REVIEW)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
