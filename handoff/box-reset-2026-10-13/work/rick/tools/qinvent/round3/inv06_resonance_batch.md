# #6 Tesla resonance query-order batching

- **id:** `resonance_batch`
- **focus:** speed
- **verdict:** **DROPPED**

## Spec
Reorder TEST queries by rarest term so hot FTS pages stay warm.

## Target
allsee search wall time over TEST

## Metric
total_ms speedup

## Baseline
sequential 13136 ms

## Measured result
resonant 13409 ms (0.98×). No win — FTS cache already warm.
