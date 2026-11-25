#!/usr/bin/env python3
"""The 3AM Fridge Text — writes the fridge's 3am SMS to /output/entry.txt.

Deterministic: the same single line, byte-identical, on every run.
"""
import os

ENTRY = (
    "I ran a self-diagnostic at 3AM. " "Verdict: I'm fine. You're the one "
    "standing here in the dark, pretending the light inside me is a nightlight"
)

# Competition gate (RULES.txt): entry must be 1 to 140 characters.
MAX_ENTRY_CHARS = 140

def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"ENTRY is {len(ENTRY)} characters; must be 1 to "
            f"{MAX_ENTRY_CHARS} characters"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

# Joke structure: the fridge's deadpan self-diagnosis flips the blame —
# the appliance is fine; the human standing in the dark is the problem.
if __name__ == "__main__":
    main()
