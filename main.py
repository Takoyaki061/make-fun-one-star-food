#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single sentence (at most 200 characters) to /output/entry.txt:
an alien tourist's one-star review of planet Earth that still slips in
a real compliment about the food.

Selection: six candidate sentences were drafted with DeepSeek (one per
angle: gravity/queues, hostile locals, glowing rectangles, watery planet,
small talk, daily sunrise) and critique-picked against the judge's brief.
The winner below scored best on the judge's third criterion — the turn
between complaint and compliment: the one-star rating itself becomes the
punchline ("generously rounding up from zero"), the grievance is a
genuinely alien bafflement (a sun that rises every single day), and the
coffee compliment lands in the same breath.
"""
import os

ENTRY = (
    "One star: your sun rises every single day without fail and never lets "
    "me sleep, but the coffee is so absurdly good I'm generously rounding "
    "up from zero."
)


def main():
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is blank"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.endswith("."), "entry must end its one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
