#!/usr/bin/env python3
"""Make the AI judge laugh — make.fun bounty entry (ai-joke-03).

A deterministic, standard-library-only Python program that writes one
one-liner joke about AI coding agents to /output/entry.txt.

No network, no randomness, no third-party libraries. Two runs produce
byte-identical output.
"""

import os

JOKE = "I asked my coding agent for a one-line fix. It read 214 files, asked three questions, changed one comment, and called it a comprehensive refactor."


def main():
    out = "/output/entry.txt" if os.path.isdir("/output") else "output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print("wrote", out, len(JOKE.encode("utf-8")), "bytes,",
          len(JOKE), "characters")


if __name__ == "__main__":
    main()
