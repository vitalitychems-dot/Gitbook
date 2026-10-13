# #15 SQLite mmap hardware path

- **id:** `sqlite_mmap`
- **focus:** hardware/speed
- **verdict:** **KEPT**

## Spec
PRAGMA mmap_size=256MB on read-only allsee.db (OS page cache maps index).

## Target
allsee.search TEST latency

## Metric
p50_ms, total_ms, recall5

## Baseline
p50 59.3 ms, tot 14224 ms, R@5 0.9674

## Measured result
mmap p50 42.4 ms (−29%), tot 10140 (−29%), R@5 0.9674. cache_size alone did not help.
