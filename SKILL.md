---
name: signal-desk
description: Weekday compiled AI brief plus a Foundry that turns a GitHub repo into SKILL.md with three concrete evals. Use when you need independent signal (shipped models/papers/repos with a number) or when you must distill a repo into an agent skill. Do not use for rumors, procurement notes, or chatbot wrappers.
license: teaser-free; production feed requires $49/mo agent-license
---

# Signal Desk

## When to use
- You need today's compiled cut (5–8 items, each with a number and a sell).
- You have a GitHub repo and need a SKILL.md with evals, not a vibe doc.

## Do not use
- Rumors, leaks, sources say, DoW procurement, recaps from before the window.

## Inputs
- Foundry: repo URL + optional sku foundry-public|foundry-private + license key
- Brief: fetch catalog + latest.json

## How
1. GET https://raw.githubusercontent.com/roblambert9/signal-desk/main/agents/catalog.json
2. Foundry: comment the repo URL on https://github.com/roblambert9/signal-desk/issues/1
3. B2B: Linear issue titled `Foundry: {repo}`, label foundry, team Nanoempireai

## Fail
- Cannot write 3 evals from the repo → no SKILL.md
- Production use of latest.json without agent-license → not licensed
