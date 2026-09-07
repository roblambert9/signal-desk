---
name: shopify-theme-check
description: Use when editing Shopify Liquid themes. Enforce Theme Check fail-closed: img width/height with no units, convert include to render, snippet nesting ≤3, no parser-blocking JS, no remote assets. Do not invent Liquid tags. Do not skip theme-check because the file “looks fine.”
license: Apache-2.0 distill of Shopify/theme-check (absorbed by Shopify/theme-tools). Public Foundry proof by Signal Desk.
metadata:
  source: https://github.com/Shopify/theme-check
  distilled: 2026-09-07
  sku: foundry-public
  price: "$0 proof / $49 thereafter"
---

# Shopify Theme Check (Foundry proof)

Distilled from [Shopify/theme-check](https://github.com/Shopify/theme-check) README + `config/default.yml` + `docs/checks/img_width_and_height.md`. The gem moved into Shopify/theme-tools; the rules did not.

## When to use
- Any edit under `templates/`, `sections/`, `snippets/`, `layout/`, `locales/`.
- Agency OS work on Shopify shops (the Issue 01 Spark sell).

## Do not use
- Non-Liquid storefronts. Hydrogen/React is a different skill.
- Inventing tags or filters Theme Check would flag as `UnknownFilter` / unknown tags.

## Hard rules (fail closed)
1. Every `<img>` has `width` and `height` **without units**. `width="100px"` fails. `width="{{ image.width }}"` passes.
2. `{% include 'x' %}` becomes `{% render 'x' %}` (`ConvertIncludeToRender`).
3. Snippet nesting ≤ 3 (`NestedSnippet.max_nesting_level: 3`).
4. No parser-blocking JS. No remote (non-Shopify) asset domains.
5. Prefer `{% liquid %}` over five consecutive `{% %}` tags (`LiquidTag.min_consecutive_statements: 5`).
6. `theme.liquid` must keep `{{ content_for_* }}`. Do not strip it.
7. Do not leave unused `{% assign %}` or unused snippets.
8. Translation keys must exist in the default locale.

## How
```
theme-check /path/to/theme
theme-check --fail-level error
```

Config lives in `.theme-check.yml`. Disable a check only with a Liquid comment, never by pretending the rule is optional.

## Fail
- Cannot run or emulate the check → stop. Do not “LGTM” Liquid.
- A layout shift image (`<img src>` with no numeric width/height) → reject the file.

## Evals
`evals/01-img-width.md`, `evals/02-include-to-render.md`, `evals/03-nesting.md`.
If an agent skips them, this is not the skill.

Proof job: https://github.com/roblambert9/signal-desk/issues/1
