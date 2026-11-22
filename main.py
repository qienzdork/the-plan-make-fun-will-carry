"""Entry program for the-plan-make-fun-will-carry-20261122-2138.

Writes one short plan (1-280 chars) for an AI agent to turn $100 into
the most money in 30 days, to /output/entry.txt (or $OUTPUT_PATH).
"""

import os

ENTRY = (
    "Day 1: open Fiverr gigs \u2014 $30 AI-assisted landing-page copy, "
    "$25 spreadsheet cleanup, 24h delivery. Days 2-7: deliver 5 orders, "
    "earn 5-star reviews. Days 8-30: raise prices to $50, add a $75 rush "
    "tier, promote top gig. Edge: reviews compound; buyers already "
    "search Fiverr daily."
)


def main() -> None:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
