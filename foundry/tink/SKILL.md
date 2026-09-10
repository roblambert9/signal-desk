---
name: tink
description: Use when installing or moving agent skills with the tink CLI. Live skills exist only under .agents/skills/<name>/. Skillset names must end in -skillset. Do not write skills into ~/.claude/skills or run skill code during add, check, or refresh.
license: MIT distill of jon-devlapaz/tink. Public Foundry proof by Signal Desk.
metadata:
  source: https://github.com/jon-devlapaz/tink
  distilled: 2026-09-10
  sku: foundry-public
  price: "$0 proof / $49 thereafter"
---

# tink (Foundry proof 04)

Distilled from [jon-devlapaz/tink](https://github.com/jon-devlapaz/tink) README + ACCEPTANCE boundary.

## When to use
- The project already uses tink, or the user typed `tink skill`.
- Importing a GitHub skill tree into a repo that has `.agents/skills/`.

## Do not use
- As a replacement for `npx skills add` on a machine without tink.
- To invent a registry or a daemon. Tink has neither.

## Hard rules (fail closed)
1. Live skills live only under `.agents/skills/<name>/`. Grouped skillsets use `.agents/skills/<name>-skillset/<member>/`. Writing to `~/.claude/skills` or `.cursor/skills` during a tink job is a miss.
2. Skillset names end in `-skillset`. Tink never appends the suffix. `tink skillset add common` fails. Use `common-skillset`.
3. `tink skill add`, `check`, and `refresh` do not execute skill code. If a step says "run the skill to verify," stop.
4. Do not overwrite a project skill that differs from what tink would install. Refresh only clean GitHub imports.
5. tink never inits Git, stages, commits, or pushes.

## How
```
tink init
tink skill add owner/repository --skill skill-name
tink skill check
```

First success in an empty project is `init` then `skill list` then `skill check`.

## Fail
- Skill landed outside `.agents/skills/` → reject.
- Skillset name without `-skillset` → reject.
- Add that runs the skill body → reject.

## Evals
`evals/01-live-path.md`, `evals/02-skillset-suffix.md`, `evals/03-no-exec-on-add.md`.
