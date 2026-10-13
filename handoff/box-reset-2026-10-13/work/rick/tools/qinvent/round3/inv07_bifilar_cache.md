# #7 Bifilar dual-path query cache

- **id:** `bifilar_cache`
- **focus:** speed/Tesla
- **verdict:** **KEPT**

## Spec
Path A: exact string. Path B: normalized sorted token-set. Zipf stream of 600 real queries with case/space variants.

## Target
repeated agent queries

## Metric
hit_rate (↑), total_s (↓)

## Baseline
exact-only hit 0.613, 13.72s; nocache 37.52s

## Measured result
bifilar hit 0.707, 10.38s (−24% vs exact, −72% vs cold).
