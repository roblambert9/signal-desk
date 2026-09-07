# Eval 01 — no-document-query

Source: salesforce/eslint-plugin-lwc `docs/rules/no-document-query.md`

## FAIL
```js
const item = document.querySelector('.my-item');
```

## PASS
```js
const item = this.template.querySelector('.my-item');
```
