# #8 Canon-path LRU / idf warm memo

- **id:** `canon_memo`
- **focus:** speed
- **verdict:** **DROPPED**

## Spec
lru_cache on allsee.canon; compare cold vs warm idf.

## Target
allsee.search TEST

## Metric
p50_ms / total_s

## Baseline
p50 55ms; idf cold 14.26s

## Measured result
memo p50 57ms (no gain); idf warm 14.19s (1.005×). Dropped.
