# Eval 03 — click-events-have-key-events

Source: jsx-eslint/eslint-plugin-jsx-a11y `docs/rules/click-events-have-key-events.md`

## FAIL if the skill emits
```jsx
<div onClick={() => save()} />
<span onClick={onOpen} />
```

## PASS only if it emits
```jsx
<button onClick={() => save()}>Save</button>
<div onClick={() => save()} onKeyDown={onKey} />
```

Prefer the `<button>`. A key handler on a div is the fallback, not the product.
