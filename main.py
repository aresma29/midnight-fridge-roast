#!/usr/bin/env python3
"""Print the Midnight Fridge Roast entry line exactly."""

import os
import sys


def main():
    # Resolve entry.txt next to this script, so the program works
    # no matter which directory it is run from.
    here = os.path.dirname(os.path.abspath(__file__))
    entry_path = os.path.join(here, "entry.txt")
    with open(entry_path, "r", encoding="utf-8") as f:
        text = f.read()
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
