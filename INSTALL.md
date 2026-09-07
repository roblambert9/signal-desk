# Install Signal Desk (one command)

Claude Code (default):

```sh
curl -fsSL https://raw.githubusercontent.com/roblambert9/signal-desk/main/install.sh | sh
```

Codex CLI:

```sh
DEST="$HOME/.codex/skills/signal-desk" \
  curl -fsSL https://raw.githubusercontent.com/roblambert9/signal-desk/main/install.sh | sh
```

Cursor / project:

```sh
DEST=".cursor/skills/signal-desk" \
  curl -fsSL https://raw.githubusercontent.com/roblambert9/signal-desk/main/install.sh | sh
```

SkillMD (after you publish): `npx skillmds add roblambert9/signal-desk`

Then set `SIGNAL_DESK_LICENSE` for production. Without it, sells are `[teaser]`.
Foundry: comment a repo on https://github.com/roblambert9/signal-desk/issues/1
