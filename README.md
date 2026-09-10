# Signal Desk

Weekday compiled cut of shipped models, papers, and repos. Foundry turns a GitHub repo into `SKILL.md` with three fail-closed evals. Deal desk quotes a floor. Empty windows ship nothing.

## Install

```sh
npx skills add roblambert9/signal-desk
```

or

```sh
curl -fsSL https://raw.githubusercontent.com/roblambert9/signal-desk/main/install.sh | sh
```

Teaser is free. Production agent use needs `SIGNAL_DESK_LICENSE` ($49/mo).

## Buy

| SKU | Price | Cart |
|---|---|---|
| Episode 01 PDF | $19 | [invoice](products/invoice-ep01.md) · `roblambert9@gmail.com` |
| Weekday cut | $29/mo | same inbox |
| Agent license | $49/mo | comment the key on [issue #1](https://github.com/roblambert9/signal-desk/issues/1) |
| Foundry public | $49 | [invoice](products/invoice-foundry-pub.md) · comment a repo on issue #1 |
| Foundry private | $199 | Linear `Foundry: {repo}` |

Do not invent a price. Book: [`skills/deal-desk/references/floors.json`](skills/deal-desk/references/floors.json).

## Foundry

```
repo: https://github.com/org/name
sku: foundry-public
license: invoice
```

Proofs (free):
- [Shopify Theme Check](foundry/shopify-theme-check/SKILL.md)
- [Salesforce LWC ESLint](foundry/salesforce-eslint-lwc/SKILL.md)
- [jsx-a11y](foundry/eslint-plugin-jsx-a11y/SKILL.md)
- [tink](foundry/tink/SKILL.md)

No three evals = no file. `scripts/check-proofs.sh` fails CI if a proof is missing evals.

## Deal desk

[`skills/deal-desk/SKILL.md`](skills/deal-desk/SKILL.md). One owner, one SKU. $9 on Episode 01 must refuse.

## Agents

- `npx skills add roblambert9/signal-desk`
- Catalog: [`agents/catalog.json`](agents/catalog.json)
- Card: [`.well-known/agent-card.json`](.well-known/agent-card.json)
- Latest cut: [`issues/latest.json`](issues/latest.json)
