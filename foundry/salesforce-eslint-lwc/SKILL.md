---
name: salesforce-eslint-lwc
description: Use when writing or reviewing Lightning Web Components. Fail closed on document.querySelector, innerHTML/outerHTML/insertAdjacentHTML, and class names that do not match the file. Use this.template.querySelector and textContent instead. Do not invent LWC APIs. Do not skip @lwc/eslint-plugin-lwc because the file looks fine.
license: BSD-3-Clause distill of salesforce/eslint-plugin-lwc. Public Foundry proof by Signal Desk.
metadata:
  source: https://github.com/salesforce/eslint-plugin-lwc
  distilled: 2026-09-07
  sku: foundry-public
  price: "$0 proof / $49 thereafter"
---

# Salesforce LWC ESLint (Foundry proof 02)

Distilled from [salesforce/eslint-plugin-lwc](https://github.com/salesforce/eslint-plugin-lwc) README + `docs/rules/no-document-query.md` + `no-inner-html.md` + `consistent-component-name.md`. Pair with the Shopify Theme Check distill for the Issue 01 agency OS sell.

## Hard rules (fail closed)
1. Never `document.querySelector` (or All / getElementById / getElementsBy*). Use `this.template.querySelector`.
2. Never `innerHTML`, `outerHTML`, or `insertAdjacentHTML`. Use `textContent`.
3. Default export class name matches the file: `foo.js` → `class Foo`.
4. `@api` names do not start uppercase. Wire adapters only with `@wire`.

## Fail
- Cannot parse decorators → stop.
- Any `document.querySelector` or `innerHTML` in the diff → reject the file.

## Evals
`evals/01-no-document-query.md`, `evals/02-no-inner-html.md`, `evals/03-component-name.md`.

Proof job: https://github.com/roblambert9/signal-desk/issues/1
