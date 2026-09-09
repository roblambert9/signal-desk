#!/usr/bin/env python3
"""Max bid from comps. Human submits. Exit 2 = pass."""
from __future__ import annotations

import argparse
import json
import math
import sys


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--comp", type=float, required=True)
    p.add_argument("--fees-bps", type=int, default=1250)
    p.add_argument("--max-loss", type=float, default=0)
    args = p.parse_args()
    max_bid = math.floor((args.comp * (1 - args.fees_bps / 10_000) - args.max_loss) * 100) / 100
    verdict = "bid" if max_bid > 0 else "pass"
    out = {
        "comp": args.comp,
        "fees_bps": args.fees_bps,
        "max_loss": args.max_loss,
        "max_bid": max_bid,
        "verdict": verdict,
        "note": "Human submits this number. Do not snipe-bot.",
    }
    print(json.dumps(out, indent=2))
    return 0 if verdict == "bid" else 2


if __name__ == "__main__":
    sys.exit(main())
