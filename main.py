#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes a single original one-line dad joke (at most 140 characters) to
``entry.txt`` inside the output directory the grader passes as the first
command-line argument (or ``$MAKEFUN_OUTPUT_DIR``, or ``/output``).

The program is fully deterministic: it always writes the same joke, and it
never writes anywhere except the output directory it was given. In
particular it never writes into the repository directory, which is
read-only while grading.
"""

import os
import sys

JOKE = "My calendar says its days are numbered \u2014 it just can't commit to anything past December."

MAX_CHARS = 140


def main(argv):
    if len(argv) > 1:
        out_dir = argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    joke = JOKE.strip()
    if not joke:
        raise SystemExit("refusing to write an empty entry")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")
    if len(joke) > MAX_CHARS:
        raise SystemExit(
            "joke is %d characters, over the %d limit" % (len(joke), MAX_CHARS)
        )

    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
