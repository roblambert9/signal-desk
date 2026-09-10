#!/bin/sh
# Signal Desk — one-command install for Claude Code / Codex / Cursor.
# Preferred: npx skills add roblambert9/signal-desk
# Fallback: curl -fsSL https://raw.githubusercontent.com/roblambert9/signal-desk/main/install.sh | sh
set -e
BASE="https://raw.githubusercontent.com/roblambert9/signal-desk/main"
if [ -n "$DEST" ]; then
  :
elif [ -d "$HOME/.claude/skills" ] || [ -d "$HOME/.claude" ]; then
  DEST="$HOME/.claude/skills/signal-desk"
elif [ -d "$HOME/.codex" ]; then
  DEST="$HOME/.codex/skills/signal-desk"
else
  DEST="$HOME/.claude/skills/signal-desk"
fi
mkdir -p "$DEST/evals"
curl -fsSL "$BASE/SKILL.md" -o "$DEST/SKILL.md"
for f in 01-thin-window 02-invoice-shape 03-license-nag; do
  curl -fsSL "$BASE/skills/signal-desk/evals/${f}.md" -o "$DEST/evals/${f}.md"
done
echo "Signal Desk installed → $DEST"
echo "Or: npx skills add roblambert9/signal-desk"
echo "Teaser is free. Production loops need SIGNAL_DESK_LICENSE."
echo "Foundry: https://github.com/roblambert9/signal-desk/issues/1"
