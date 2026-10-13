# #13 Zipf / resonance boot prefetch

- **id:** `zipf_prefetch`
- **focus:** speed/Tesla
- **verdict:** **KEPT**

## Spec
Prefetch top-50 zipf-popular queries into bifilar token-set cache at boot.

## Target
600-query zipf stream w/ case variants

## Metric
hit_rate, seconds

## Baseline
bifilar (no prefetch) hit 0.717, 10.5s

## Measured result
prefetch hit 0.797, 7.18s (−32% time, +8.0 pp hit).
