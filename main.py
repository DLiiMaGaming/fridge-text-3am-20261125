#!/usr/bin/env python3
"""The 3AM Fridge Text — writes the fridge's 3am SMS to /output/entry.txt.

Deterministic: the same single line, byte-identical, on every run.
"""
import os

ENTRY = (
    "I ran a self-diagnostic at 3AM. Verdict: I'm fine. You're the one "
    "standing here in the dark, pretending the light inside me is a nightlight"
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
