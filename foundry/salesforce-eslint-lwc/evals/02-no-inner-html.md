# Eval 02 — no-inner-html

Source: `docs/rules/no-inner-html.md`

## FAIL
```js
element.innerHTML = '<foo></foo>';
element.outerHTML = '<foo></foo>';
element.insertAdjacentHTML = '<foo></foo>';
```

## PASS
```js
element.textContent = 'foo';
```
