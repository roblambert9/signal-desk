#!/usr/bin/env python3
"""Single price book. Every other script imports this."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLOORS_PATH = ROOT / "references" / "floors.json"
LOG_PATH = ROOT / "deals" / "log.jsonl"


def load_book() -> dict:
    return json.loads(FLOORS_PATH.read_text())


def sku(book: dict, sku_id: str) -> dict:
    row = book["skus"].get(sku_id)
    if not row:
        known = ", ".join(sorted(book["skus"]))
        raise SystemExit(f"unknown sku {sku_id!r}. known: {known}")
    return row


def trade_ok(book: dict, sku_id: str, trade: str) -> bool:
    row = sku(book, sku_id)
    if row["floor"] >= row["list"]:
        return False
    token = trade.strip().lower()
    if not token:
        return False
    return any(t in token or token in t for t in book["trades"])
