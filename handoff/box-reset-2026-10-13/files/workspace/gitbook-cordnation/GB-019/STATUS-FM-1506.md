# Status front-matter fix — GB-019 (15:06 CT Tessera ruling)

**Strip baseline:** `GB-019/GB-019.strip.diff`  
**New diff:** `GB-019/GB-019.diff`  
**Line counts:** strip 87 → status-fm 87

## Principle

Shipped `status:` must be true at Father push → **`published`**. No gate or Ready claims in front matter.

## Front matter now shipped

### `GB-019/proposed/intake/CORTICAL-LABS-READINESS.md`

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
