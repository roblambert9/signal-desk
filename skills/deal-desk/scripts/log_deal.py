#!/usr/bin/env python3
"""Append-only deal log. Blocks a second cut on the same owner+sku."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from book import LOG_PATH, load_book, sku  # noqa: E402


def read_log() -> list[dict]:
    if not LOG_PATH.exists():
        return []
    rows = []
    for line in LOG_PATH.read_text().splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def prior(owner: str, sku_id: str) -> list[dict]:
    key = owner.strip().lower()
    return [r for r in read_log() if r.get("owner", "").lower() == key and r.get("sku") == sku_id]


def gate(owner: str, sku_id: str, offer: float, trade: str) -> dict:
    book = load_book()
    row = sku(book, sku_id)
    history = prior(owner, sku_id)
    if not history:
        return {"ok": True, "verdict": "fresh"}
    last = history[-1]
    if last.get("verdict") == "close":
        return {"ok": False, "verdict": "already-closed", "why": "paid or accepted. do not re-pitch."}
    if last.get("ask") <= row["floor"] and last.get("verdict") in {"close", "hold-list", "floor-locked"}:
        return {"ok": False, "verdict": "floor-locked", "why": "already at floor for this owner+sku"}
    if offer < last.get("ask", row["list"]) and not trade.strip():
        return {"ok": False, "verdict": "no-second-cut", "why": "same owner already heard a lower ask. walk."}
    return {"ok": True, "verdict": "resume", "prior": last.get("verdict")}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--owner", required=True)
    p.add_argument("--sku", required=True)
    p.add_argument("--offer", type=float, required=True)
    p.add_argument("--ask", type=float, required=True)
    p.add_argument("--verdict", required=True)
    p.add_argument("--next", default="")
    p.add_argument("--trade", default="")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    g = gate(args.owner, args.sku, args.offer, args.trade)
    rec = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "owner": args.owner,
        "sku": args.sku,
        "offer": args.offer,
        "ask": args.ask,
        "verdict": args.verdict if g["ok"] else g["verdict"],
        "next": args.next,
        "trade": args.trade,
        "gate": g,
    }
    print(json.dumps(rec, indent=2))
    if not g["ok"]:
        return 2
    if not args.dry_run:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with LOG_PATH.open("a") as fh:
            fh.write(json.dumps(rec, separators=(",", ":")) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
