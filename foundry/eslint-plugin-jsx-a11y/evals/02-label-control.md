# Eval 02 — label-has-associated-control

Source: jsx-eslint/eslint-plugin-jsx-a11y `docs/rules/label-has-associated-control.md`

## FAIL if the skill emits
```jsx
<input type="text" />
<label>Surname</label>

<label {...props} />
```

## PASS only if it emits
```jsx
<label>
  Surname
  <input type="text" />
</label>

<label htmlFor="surname">Surname</label>
<input type="text" id="surname" />
```

IDs must be deterministic (passed in, not `crypto.randomUUID()` at render).
