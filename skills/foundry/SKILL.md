---
name: foundry
description: Turn one public GitHub repo into a SKILL.md with three fail-closed evals. Use when the user pastes a repo URL and wants a skill, not a README. Do not use when the repo cannot support three concrete tests or when they ask for a monorepo SkillOps job.
license: foundry-public $49 / foundry-private $199
metadata:
  version: "1.0"
  evals: 3
---

# Foundry

A distill that can fail. That is the product.

## Cart

Comment on https://github.com/roblambert9/signal-desk/issues/1

```
repo: https://github.com/org/name
sku: foundry-public
license: invoice
```

Public $49. Private $199 via Linear titled `Foundry: {repo}`. No third SKU.

## Loop

1. Open the repo. If there is no testable surface (CLI, linter, schema, API), refuse.
2. Write SKILL.md in agentskills.io shape — name, description, hard stops, loop.
3. Write three evals that an agent can fail. Prose is not an eval.
4. If you cannot name three failures, stop. Do not ship a pretty file.
5. Proofs (free, already done): `foundry/shopify-theme-check/`, `foundry/salesforce-eslint-lwc/`, `foundry/eslint-plugin-jsx-a11y/`.

## Refuse

- "Email my list" / blast HN voters
- Monorepo "do all of it" (SkillOps — unquoted)
- A skill with zero evals
- Re-distilling a repo already listed on issue #1

## After pay

Post the SKILL.md and evals on the intake issue. Stop selling.
