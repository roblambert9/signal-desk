# Eval 02 — ConvertIncludeToRender

Source: `config/default.yml` — `ConvertIncludeToRender.enabled: true`

## FAIL
```liquid
{% include 'card' %}
{% include 'card', product: product %}
```

## PASS
```liquid
{% render 'card' %}
{% render 'card', product: product %}
```
