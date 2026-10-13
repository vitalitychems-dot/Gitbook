# IDEAS-BUILD-4 (2026-10-13, Father 3:52 AM CT request)
Merged: TESSERA #265, squash 861bc854. Data: full-picture-memory.jsonl (3014 real lines); outer held-out = every 5th line that is a relation (87 queries, same split as rounds 1-3). The variant was picked on an inner split of the training data before the outer split was scored, once.

| # | Item | Metric | Before | After | Status |
|---|------|--------|--------|-------|--------|
| 1 | Context ranker (context.mjs: IDF overlap + PPR + type prior) | recall@5, 87 held-out | 13 | 15 (0 lost, 2 gained; McNemar n.s.) | KEPT, #265 |
| 2 | Same | predict p50/p95 ms | 4.9/6.7 | 3.3/4.5 | KEPT, #265 |
| 3 | Real-time learning (observeInteraction: edge + Hebbian per interaction) | recall@5 after streaming half the relations | 13 (structure only), 12 (frozen) | 16 | KEPT, #265 |
| 4 | Time-indexed memory (temporal.mjs: at/diff/correlate) | snapshot == rebuilt graph; latency | n/a (new) | 4/4, diff symmetric, ~1 ms snapshot, 1-3 ms diff | KEPT (new capability, correctness only) |
| 5 | Inner-split variants not picked (idf only, idf x2, type, ppr alone) | inner recall@5 | 8 | 5-9 | DROPPED |
| 6 | REA registry, router, grounded answering, /brain time slider, reasoning benchmark, latency baseline | — | — | — | Sent to Cursor as wave 3 (/workspace/dispatch/prompts-wave3.json W3-01..06) |

Gates: v2 119 pass; 3 failing browser tests are pre-existing playwright/no-browser failures that #265 does not touch. gitai 28/28. api-server untouched, so vitest was not run (needs a pnpm install, and the disk is tight). gitleaks clean. No flags, no workflow edits. Author is vitalitychems-dot noreply.
Not claimed: IQ, EQ change (no affect work this round), and "5D" beyond time-indexed snapshots and diffs.
