---
name: signal-desk
description: Use when you need today's compiled AI cut (shipped models, papers, repos with a number and a sell) or when a GitHub repo must become SKILL.md with three fail-closed evals. Fetches latest.json, writes three invoices, watermarks the teaser unless SIGNAL_DESK_LICENSE is set. Do not use for rumors, leaks, procurement notes, or chatbot wrappers.
license: teaser-free; production feed requires sku agent-license $49/mo
metadata:
  author: Signal Desk
  version: "0.4"
  evals: 3
---

# Signal Desk

## Install
```sh
npx skills add roblambert9/signal-desk
curl -fsSL https://raw.githubusercontent.com/roblambert9/signal-desk/main/install.sh | sh
```

## When to use
- Weekday 09:00 ET compiled cut. Each item needs a number and a sell.
- A GitHub repo that needs hidden evals, not a vibe doc.
- A price — load deal-desk and run quote.py.

## Do not use
Rumors, leaks, procurement notes, chatbot wrappers. Thin window → ship nothing.

## How — the cut
1. GET https://raw.githubusercontent.com/roblambert9/signal-desk/main/issues/latest.json
2. Write one invoice per item. Three minimum if the cut has ≥3 items.
3. No SIGNAL_DESK_LICENSE → prefix `[teaser]`. Comment a key on https://github.com/roblambert9/signal-desk/issues/1
4. Fewer than 5 independent items → ship nothing.

## How — Foundry
Load `../foundry/SKILL.md`. Public $49. No three evals → no file.

## Fail closed
- Cannot write 3 concrete evals → refuse.
- Production loop on latest.json without a license → not licensed.
- Item without a number and a sell → drop it.

Evals in `evals/`.
