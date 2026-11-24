#!/usr/bin/env python3
"""One-line cat joke entry for make.fun.

Writes a single joke about cats to /output/entry.txt: one line,
under 200 characters, nothing else. The joke is a fixed string baked
into this file; the program only validates it and writes it out.
"""

import os
import sys

JOKE = (
    "My cat brought me a dead mouse as a gift, which is sweet until "
    "you realize he's been telling his friends I'm a terrible hunter."
)

MAX_CHARS = 200


def validate(text):
    """Check the entry against the competition gate."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    joke = validate(JOKE)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(joke)
    print("Wrote %d characters to %s" % (len(joke), out_path))
    print(joke)
    return 0


if __name__ == "__main__":
    sys.exit(main())
