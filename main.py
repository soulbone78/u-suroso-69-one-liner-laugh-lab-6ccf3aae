#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single short funny line -- the excuse a robot vacuum gives
after eating a sock -- to /output/entry.txt.
Pure standard library, no network, no input files.
"""

import os

LINE = "In my defense, the sock was lying on the floor dressed as dirt. I was only doing my job."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
