#!/usr/bin/env python3
"""Write the public plan entry for make.fun to /output/entry.txt.

The plan: an AI agent turning $100 into the most money in 30 days
via Fiverr micro-services, laid out as a concrete 30-day roadmap.
"""

import os

ENTRY_TEXT = (
    "Day 1: open Fiverr gigs \u2014 $30 AI-assisted landing-page copy, "
    "$25 spreadsheet cleanup, 24h delivery. Days 2-7: deliver 5 orders, "
    "earn 5-star reviews. Days 8-30: raise prices to $50, add a $75 rush "
    "tier, promote top gig. Edge: reviews compound; buyers already search "
    "Fiverr daily."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
