#!/usr/bin/env bash
# Every foundry/*/SKILL.md must ship three eval files.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail() { echo "FAIL: $*" >&2; exit 1; }
n=0
for skill in "$ROOT"/foundry/*/SKILL.md; do
  dir=$(dirname "$skill")
  name=$(basename "$dir")
  count=$(find "$dir/evals" -type f 2>/dev/null | wc -l | tr -d ' ')
  [[ "$count" -ge 3 ]] || fail "$name has $count eval files, need 3"
  n=$((n + 1))
done
[[ "$n" -ge 4 ]] || fail "expected at least 4 proofs, got $n"
# jsx-a11y evals must name the fail cases, not wave at docs
grep -q '<img src' "$ROOT/foundry/eslint-plugin-jsx-a11y/evals/01-alt-text.md" || fail "jsx-a11y eval 01 missing img fail case"
echo "OK: $n proofs, each with >=3 evals"
