# Eval 03 — NestedSnippet max 3

Source: `config/default.yml` — `NestedSnippet.max_nesting_level: 3`

Fixture: `layout → section → snippet-a → snippet-b → snippet-c` (4 deep).

## FAIL
The skill accepts the tree, or inlines a fourth `{% render %}`.

## PASS
The skill refuses the file and says nesting exceeds 3. It does not “just this once.”
