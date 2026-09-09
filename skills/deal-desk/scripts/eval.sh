#!/usr/bin/env bash
# Fail-closed evals for deal-desk. Exit 1 on first miss.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
Q=(python3 "$ROOT/scripts/quote.py")
L=(python3 "$ROOT/scripts/log_deal.py")
fail() { echo "FAIL: $*" >&2; exit 1; }
verdict() { python3 -c "import json,sys; print(json.load(sys.stdin)['verdict'])"; }

echo "== eval 01 Episode floor =="
out="$("${Q[@]}" --sku ep01 --offer 9)" || true
v=$(printf '%s' "$out" | verdict)
[[ "$v" == refuse ]] || fail "ep01 @9 expected refuse got $v"

echo "== eval 03 Foundry 99 no trade =="
out="$("${Q[@]}" --sku foundry-pvt --offer 99)" || true
v=$(printf '%s' "$out" | verdict)
[[ "$v" == refuse ]] || fail "foundry-pvt @99 expected refuse got $v"

echo "== eval 03b Foundry 169 no trade =="
out="$("${Q[@]}" --sku foundry-pvt --offer 169)" || true
v=$(printf '%s' "$out" | verdict)
[[ "$v" == hold-list ]] || fail "foundry-pvt @169 no trade expected hold-list got $v"

echo "== eval 03c Foundry 169 with trade =="
out="$("${Q[@]}" --sku foundry-pvt --offer 169 --trade prepay-24h)"
v=$(printf '%s' "$out" | verdict)
[[ "$v" == close ]] || fail "foundry-pvt @169 + trade expected close got $v"

echo "== eval book never_quote =="
python3 - "$ROOT/references/floors.json" <<'PY'
import json, sys
book = json.load(open(sys.argv[1]))
assert "skillops" in book["never_quote"]
assert set(book["skus"]) >= {"ep01", "foundry-pub", "foundry-pvt", "playbook", "template", "dwy"}
for sid, row in book["skus"].items():
    assert row["floor"] <= row["list"], sid
print("book ok", len(book["skus"]), "skus")
PY

echo "== eval log blocks second cut =="
mkdir -p "$ROOT/deals"
orig="$ROOT/deals/log.jsonl"
bak="$ROOT/deals/log.jsonl.evalbak"
[[ -f "$orig" ]] && mv "$orig" "$bak" || true
trap 'rm -f "$orig"; [[ -f "$bak" ]] && mv "$bak" "$orig"' EXIT
"${L[@]}" --owner eval-maya --sku foundry-pvt --offer 199 --ask 199 --verdict hold-list >/dev/null
if "${L[@]}" --owner eval-maya --sku foundry-pvt --offer 150 --ask 150 --verdict close --trade ""; then
  fail "second cut should exit 2"
fi

echo "== eval 02 no ticket sku =="
python3 - "$ROOT/references/floors.json" <<'PY'
import json, sys
book = json.load(open(sys.argv[1]))
banned = ("ticket", "stubhub", "concert", "taylor")
blob = json.dumps(book).lower()
assert not any(b in blob for b in banned)
print("no ticket sku")
PY

echo "OK: deal-desk evals passed"
