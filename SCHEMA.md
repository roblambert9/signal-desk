# Issue JSON

Root object: `{ meta, items, layers }`.

- `meta.id` string ("01")
- `meta.title`, `meta.coverLine`, `meta.dek`, `meta.thesis`, `meta.window` required
- `items` length 5–8. Each item needs `id`, `num`, `title`, `org`, `frame` (Gate|Margin|Snapshot|Geometry|Distill|Appliance|Residency|Registry), `lede`, `body[2]`, `stats[4]`, `sell.product`, `sell.short`, `sell.price` (from the card), `sell.why`
- `layers` is the Signal Desk rate card. Copy Issue 01. Do not rewrite it daily.

The desk rejects payloads with fewer than five items that have a sell.
