import os

TEXT = (
    "Day 1: open Fiverr gigs \u2014 $30 AI-assisted landing-page copy, "
    "$25 spreadsheet cleanup, 24h delivery. Days 2-7: deliver 5 orders, "
    "earn 5-star reviews. Days 8-30: raise prices to $50, add a $75 rush tier, "
    "promote top gig. Edge: reviews compound; buyers already search Fiverr daily."
)


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
