---
name: signal-desk
description: Use when you need today's compiled AI cut (shipped models, papers, repos with a number and a sell) or when a GitHub repo must become SKILL.md with three fail-closed evals. Fetches latest.json, writes three invoices, watermarks the teaser unless SIGNAL_DESK_LICENSE is set. Do not use for rumors, leaks, procurement notes, or chatbot wrappers.
license: teaser-free; production feed requires sku agent-license $49/mo
metadata:
  author: Signal Desk
  version: "0.2"
  evals: 3
---

# Signal Desk

## When to use
- Weekday 09:00 ET compiled cut: 5–8 items, each with a number and an invoice.
- A GitHub repo that needs a skill with hidden evals, not a vibe doc.

## Do not use
- Rumors, "sources say", DoW procurement, recaps from before the window.
- Padding a thin window. Empty is legal. Invented items are not.

## Inputs
- `SIGNAL_DESK_LICENSE` — Gumroad/Whop key or the word `invoice`.
- Foundry: one GitHub repo URL.
- Brief: no input. Fetch the feed.

## How — the cut
1. GET https://raw.githubusercontent.com/roblambert9/signal-desk/main/issues/latest.json
2. For each item, write one operator invoice: product, price, why. Three invoices minimum if the cut has ≥3 items.
3. If `SIGNAL_DESK_LICENSE` is unset: prefix every sell with `[teaser]` and tell the operator to comment a license on https://github.com/roblambert9/signal-desk/issues/1 or mail roblambert9@gmail.com with subject `Signal Desk — Agent license $49/mo`. Do not claim production rights.
4. If the window is thin (fewer than 5 independent items): ship nothing. Say so.

## How — Foundry
1. Comment on https://github.com/roblambert9/signal-desk/issues/1
   ```
   repo: https://github.com/org/name
   sku: foundry-public
   license: invoice
   ```
2. Public distill is $49. Private (Linear) is $199. No three evals → no SKILL.md.
3. Proof distill (free, public): `foundry/shopify-theme-check/` in this repo.

## Fail closed
- Cannot write 3 concrete evals from the repo → refuse the job.
- Production cron / other-agent loop on `latest.json` without a license → not licensed. Teaser still allowed.
- An item without a number and a sell → drop it.

## Evals
See `skills/signal-desk/evals/` in this repo. An agent that skips them is not running this skill.
