# Issue JSON

Cut writes `issues/staging.json` only.
Schema promotes to `issues/NN.json` + `issues/latest.json` or blocks.

Root: `{ meta, items, layers }`.

## Fail closed

- `items` length 5–8
- `meta.id`, `title`, `coverLine`, `dek`, `thesis`, `window`
- `thesis` must not equal Issue 01 if `id != 01`
- `item.frame` ∈ Gate | Margin | Snapshot | Geometry | Distill | Appliance | Residency | Registry
- `item.sell.price` **byte-identical** to a Notion Price card `Price`:
  - `$4k–$18k/mo`
  - `$199–$799/mo`
  - `$8k–$25k`
  - `$1.5k/unit · $8k/set`
  - `$15k + $3k/mo`
  - `$6k + $400/mo`
  - `€8k–€40k`
  - `$29 / $499 + 20% take`
- `sell.product`, `sell.why`, ≥1 stat
- no `rumor|allegedly|sources say|leak|unconfirmed|procurement`

Local check: `node scripts/validate-issue.mjs issues/staging.json`

Schema does not rewrite copy to make it pass.
