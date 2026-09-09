# Signal Desk

Weekday compiled cut of shipped models, papers, and repos. Foundry turns a GitHub repo into `SKILL.md` with three fail-closed evals. Deal desk quotes a floor. Empty windows ship nothing.

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/roblambert9/signal-desk/main/install.sh | sh
```

Teaser is free. Production agent use needs `SIGNAL_DESK_LICENSE` ($49/mo).

## Buy

| SKU | Price | Cart |
|---|---|---|
| Episode 01 PDF | $19 | invoice `roblambert9@gmail.com` until Gumroad permalink exists |
| Weekday cut | $29/mo | same |
| Agent license | $49/mo | comment the key on [issue #1](https://github.com/roblambert9/signal-desk/issues/1) |
| Foundry public | $49 | comment a repo URL on issue #1 |
| Foundry private | $199 | Linear `Foundry: {repo}` |

Do not invent a price. The book is [`skills/deal-desk/references/floors.json`](skills/deal-desk/references/floors.json). `quote.py` is the till.

## Foundry

Comment one repo on [issue #1](https://github.com/roblambert9/signal-desk/issues/1).

```
repo: https://github.com/org/name
sku: foundry-public
license: invoice
```

Proofs (free):
- [Shopify Theme Check](foundry/shopify-theme-check/SKILL.md)
- [Salesforce LWC ESLint](foundry/salesforce-eslint-lwc/SKILL.md)
- [jsx-a11y](foundry/eslint-plugin-jsx-a11y/SKILL.md)

No three evals = no file.

## Deal desk

[`skills/deal-desk/SKILL.md`](skills/deal-desk/SKILL.md) — one owner, one SKU, one message. CI runs `eval.sh` on every desk change. $9 on Episode 01 must refuse.

## Agents

- Catalog: [`agents/catalog.json`](agents/catalog.json)
- Card: [`.well-known/agent-card.json`](.well-known/agent-card.json)
- Skill: [`SKILL.md`](SKILL.md)
- Latest cut: [`issues/latest.json`](issues/latest.json)

## Clock (America/Toronto)

Watch 06:00–08:00 · Score 08:40 · Cut 08:55 · Schema 08:57 · Ship paused.
