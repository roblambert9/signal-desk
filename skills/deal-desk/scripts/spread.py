#!/usr/bin/env python3
"""Flip / scalp spread. Exit 2 = pass."""
from __future__ import annotations

import argparse
import json
import sys


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--ask", type=float, required=True)
    p.add_argument("--bid", type=float, required=True)
    p.add_argument("--fees-bps", type=int, default=1250)
    p.add_argument("--ship", type=float, default=0)
    p.add_argument("--hold-days", type=int, default=7)
    args = p.parse_args()
    fees = args.bid * (args.fees_bps / 10_000)
    net = args.bid - fees - args.ship - args.ask
    pct = (net / args.ask) if args.ask else 0.0
    stale_hold = args.hold_days > 21
    verdict = "buy" if (pct >= 0.15 and not stale_hold and net > 0) else "pass"
    out = {
        "ask": args.ask,
        "bid": args.bid,
        "fees": round(fees, 2),
        "ship": args.ship,
        "net": round(net, 2),
        "net_pct": round(pct * 100, 1),
        "hold_days": args.hold_days,
        "verdict": verdict,
        "why": "net>=15% and hold<=21" if verdict == "buy" else "need 15% after fees and <=21 day cash, else pass",
    }
    print(json.dumps(out, indent=2))
    return 0 if verdict == "buy" else 2


if __name__ == "__main__":
    sys.exit(main())
