#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one voicemail greeting, as recorded by a cat, to
/output/entry.txt. Pure Python standard library, no network, no input
files: the greeting is the entry.

The greeting: Mochi the cat answers his own voicemail. He is asleep in
the cardboard box (not the expensive bed), and mid-sentence he lets slip
what he really wants from the caller — food, at 4 a.m., the hour every
cat owner knows. One line, spoken aloud in a few seconds.
"""

import os

LINE = (
    "You've reached Mochi. I'm asleep in the box, not the bed. "
    "Leave food \u2014 I mean, a message \u2014 at 4 a.m."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, must be 1-120"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() == text, "entry must not start or end with whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read it back: the gate counts characters, so prove what landed on
    # disk is exactly the greeting we meant to enter.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "entry.txt on disk differs from the entry"
    print(written, end="")


if __name__ == "__main__":
    main()
