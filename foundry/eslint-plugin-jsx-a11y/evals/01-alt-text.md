# Eval 01 — alt-text

Source: jsx-eslint/eslint-plugin-jsx-a11y `docs/rules/alt-text.md`

## FAIL if the skill emits
```jsx
<img src="foo" />
<img {...props} />
<img src="foo" alt />
<img src="foo" role="presentation" />
<input type="image" />
```

## PASS only if it emits
```jsx
<img src="foo" alt="Foo eating a sandwich." />
<img src="foo" alt="" />
<input type="image" alt="Submit search" />
```
