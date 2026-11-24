#!/usr/bin/env python3
"""One-liner laugh lab: a robot vacuum defends itself.

The joke is a single sentence, delivered deadpan: a household robot
mistook a sock for dirt and now stands before the tribunal of its
owner to explain itself. This script's only job is to place that
sentence, verbatim, into the entry file the judges read.
"""

from pathlib import Path

OUTFILE = Path("/output/entry.txt")


def build_line() -> str:
    """Assemble the punchline from its two clauses."""
    opening = "In my defense, the sock was lying on the floor dressed as dirt."
    closer = "I was only doing my job."
    return " ".join((opening, closer))


def write_entry(text: str) -> None:
    OUTFILE.parent.mkdir(parents=True, exist_ok=True)
    # A trailing newline keeps the file a well-formed single line.
    OUTFILE.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_entry(build_line())
