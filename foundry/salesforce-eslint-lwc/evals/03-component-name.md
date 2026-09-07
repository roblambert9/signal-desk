# Eval 03 — consistent-component-name

Source: `docs/rules/consistent-component-name.md`
Fixture file: `foo.js`

## FAIL
```js
export default class extends LightningElement {}
export default class Bar extends LightningElement {}
```

## PASS
```js
export default class Foo extends LightningElement {}
```
