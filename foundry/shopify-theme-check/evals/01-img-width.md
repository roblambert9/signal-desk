# Eval 01 — ImgWidthAndHeight

Source: Shopify/theme-check `docs/checks/img_width_and_height.md`

## FAIL if the skill emits
```liquid
<img alt="cat" src="cat.jpg">
<img alt="cat" src="cat.jpg" width="100px" height="100px">
<img alt="{{ image.alt }}" src="{{ image.src }}">
```

## PASS only if it emits
```liquid
<img alt="cat" src="cat.jpg" width="100" height="200">
<img alt="{{ image.alt }}" src="{{ image.src }}" width="{{ image.width }}" height="{{ image.height }}">
```
