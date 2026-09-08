---
name: eslint-plugin-jsx-a11y
description: Use when editing React/JSX UI. Enforce jsx-a11y fail-closed: every img has alt (or alt=""), every label wraps or htmlFor-binds a control, every non-interactive onClick has a keyboard handler. Do not invent ARIA roles to silence the linter. Do not skip the plugin because the component “looks fine.”
license: MIT distill of jsx-eslint/eslint-plugin-jsx-a11y. Public Foundry proof by Signal Desk.
metadata:
  source: https://github.com/jsx-eslint/eslint-plugin-jsx-a11y
  distilled: 2026-09-08
  sku: foundry-public
  price: "$0 proof / $49 thereafter"
---

# eslint-plugin-jsx-a11y (Foundry proof 03)

Distilled from [jsx-eslint/eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y) `docs/rules/alt-text.md`, `label-has-associated-control.md`, `click-events-have-key-events.md`. Recommended + strict configs enable all three.

## When to use
- Any edit under a React/JSX tree (Next, Remix, Hydrogen, LWC-React).
- Agency OS work on Shopify Hydrogen or Salesforce LWC React shops (Issue 01 Spark sell).

## Do not use
- Vue/Svelte/Liquid. Those are different skills.
- Inventing `role="presentation"` on an `<img>` to dodge `alt-text`. The rule fails that on purpose.

## Hard rules (fail closed)
1. `<img>`, `<area>`, `<input type="image">`, `<object>` have meaningful alternative text. Decorative images use `alt=""`. Spreading `{...props}` onto `<img>` without pulling `alt` out **fails**.
2. Every `<label>` either wraps a control or has `htmlFor` matching a deterministic `id`. Random `useId()` / render-time uuids fail (SSR mismatch). Empty `<label>Surname</label>` next to a naked `<input>` fails.
3. `onClick` on a non-interactive element (`div`, `span`) is accompanied by `onKeyDown` / `onKeyUp` / `onKeyPress`. `<button onClick>` is fine. `aria-hidden="true"` on a clickable div is a hide, not a fix.
4. Prefer a real `<button>` over a clickable `<div>`.
5. Do not add `role="button"` to silence the keyboard rule. Change the element.

## How
```
npx eslint --plugin jsx-a11y --ext .jsx,.tsx .
```

Recommended config from the plugin. Disable a rule only with a line comment that names the WCAG clause, never because “the designer said so.”

## Fail
- Cannot run or emulate the rule → stop. Do not LGTM JSX.
- An `<img src>` with no `alt` → reject the file.
- A `<div onClick>` with no key handler → reject the file.

## Evals
`evals/01-alt-text.md`, `evals/02-label-control.md`, `evals/03-click-key.md`.
If an agent skips them, this is not the skill.

Proof job: https://github.com/roblambert9/signal-desk/issues/1
