## tools/bench/harness.mjs: shared cached bench harness with bootstrap 95% CIs
Adds one 48-line file with no dependencies. It times before/after fns with N>=5 runs plus a warmup, and reports the median, a bootstrap 95% CI (B=2000, seeded) and a speedup ratio CI. It also checks that before and after outputs are equal (JSON). A result counts as a win only when the outputs are equal and the low end of the speedup CI is above 1. We recommend N>=7; the CIs are below. Results are cached in .cache/bench/<mainSHA>-<benchHash>-r<N>.json, and BENCH_NOCACHE=1 forces a fresh run.

### Before/after: real bench, #319 router (old router at 54a6904, new at b2adc4f), 88 queries
| | wall time | runs | stats |
|---|---|---|---|
| Before: old r4-21 bench.mjs | 925–1035 ms (3 runs) | fixed 7, median only | no CI; speedup 1.24–1.29 |
| Harness, cold, N=5 | 959 ms | 5 | speedup 1.17, CI [0.94, 1.36], **not a win** |
| Harness, cold, N=7 | 1161 ms | 7 | 1.45, CI [1.03, 1.68] |
| Harness, cold, N=11 | 1610 ms | 11 | 1.63, CI [1.45, 1.91] |
| Harness, cached | 202–234 ms (34–48 ms in-script) | 0 | same as cold |

A cached re-check is about 4.5× faster in wall time (about 20× in-script) and runs the bench 0 times instead of 7. Outputs were equal in all runs. Finding: the router speedup is real but noisy. The 1.74× claimed in #319 is not reproduced here (1.2–1.6×). N=5 can't separate it from 1×, so we recommend N>=7 for effects under 1.5×.
