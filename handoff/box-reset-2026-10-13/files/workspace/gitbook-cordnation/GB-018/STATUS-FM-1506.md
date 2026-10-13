# Status front-matter fix — GB-018 (15:06 CT Tessera ruling)

**Strip baseline:** `GB-018/GB-018.strip.diff`  
**New diff:** `GB-018/GB-018.diff`  
**Line counts:** strip 130 → status-fm 130

## Principle

Shipped `status:` must be true at Father push → **`published`**. No gate or Ready claims in front matter.

## Front matter now shipped

### `GB-018/proposed/merge/hyb-005-braces-decision.md`

```
(no front matter — new page)
```


## Note lines dropped

(none for this package)

## Notes

- `command-center.md` on main (beadc44) was `corrected-pending-publish`, not `published`; listed under ruling (1) but handled as (2): status → `published`, coordination note kept.
- mesh-lane-map.md: no FM; stale `**Status:**` L13 remains deleted; Instrument line kept.
- New package pages keep no status FM.

## Interdiff (strip.diff → new.diff)

```diff

```
