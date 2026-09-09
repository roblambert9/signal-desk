#!/usr/bin/env python3
"""Quote against references/floors.json. Exit 2 = refuse."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from book import load_book, sku, trade_ok  # noqa: E402


def quote(sku_id: str, offer: float | None, trade: str) -> dict:
    book = load_book()
    row = sku(book, sku_id)
    list_p = float(row["list"])
    floor = float(row["floor"])
    offer_p = float(offer) if offer is not None else list_p
    unlocked = trade_ok(book, sku_id, trade)
    if offer_p < floor:
        verdict, ask = "refuse", (floor if unlocked else list_p)
    elif offer_p < list_p and not unlocked:
        verdict, ask = "hold-list", list_p
    else:
        verdict, ask = "close", offer_p
    return {
        "sku": sku_id,
        "name": row["name"],
        "list": list_p,
        "floor": floor,
        "offer": offer_p,
        "trade": trade,
        "trade_ok": unlocked,
        "ask": ask,
        "verdict": verdict,
        "cart": row["cart"],
        "deliver": row["deliver"],
        "period": row["period"],
    }


def main() -> int:
    book = load_book()
    p = argparse.ArgumentParser()
    p.add_argument("--sku", required=True, choices=sorted(book["skus"]))
    p.add_argument("--offer", type=float)
    p.add_argument("--trade", default="")
    args = p.parse_args()
    out = quote(args.sku, args.offer, args.trade)
    print(json.dumps(out, indent=2))
    return 0 if out["verdict"] != "refuse" else 2


if __name__ == "__main__":
    sys.exit(main())
