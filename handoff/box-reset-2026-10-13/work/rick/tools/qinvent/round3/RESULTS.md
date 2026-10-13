# qinvent round3 — 15 inventions (2026-10-13)

Rule: keep only measured wins. Priority: **token efficiency → speed → accuracy**.
Bench: c1 `qa_set` TEST n=215 (DEV n=185 for every tuning choice). Index: `allsee.db` read-only.
Token proxy: `len//4` (same as `allsee/rounds.py`). No venv installs; system PIL for #10.

Reproduce: `python3 tokens.py; python3 speed_acc.py; python3 hardware.py; python3 more2.py; python3 more3.py` (from this dir; `../.venv/bin/python` also fine for non-PIL).

## Scoreboard

| # | Invention | Focus | Baseline → Result | Verdict |
|---|---|---|---|---|
| 1 | Tesla valvular one-way line filter | token | tokens 1725.3 (−26%), R@5 0.9674, acc 0.1953 | **KEPT** |
| 2 | Free-energy / entropy sentence budget | token/thermo | T=1.5 → tokens 1324.0 (−23% vs valve, −43% vs raw) | **KEPT** |
| 3 | Landauer bit-budget / score-gap adaptive k | token/thermo | Bit-budget B≤10 and gap-k thr≤0.5 all either cut DEV recall or matched valve tok | **DROPPED** |
| 4 | Simulated-annealing context prune | token | DEV only λ=0 keeps acc (tokens 1207) | **DROPPED** |
| 5 | Cross-hit entropy-zero line dedup | token | tokens 1088.4 (−37% vs valve). Stack #2+#5: 782.2 (−66% vs raw). | **KEPT** |
| 6 | Tesla resonance query-order batching | speed | resonant 13409 ms (0.98×). No win — FTS cache already warm. | **DROPPED** |
| 7 | Bifilar dual-path query cache | speed/Tesla | bifilar hit 0.707, 10.38s (−24% vs exact, −72% vs cold). | **KEPT** |
| 8 | Canon-path LRU / idf warm memo | speed | memo p50 57ms (no gain) | **DROPPED** |
| 9 | Thermal-aware ncand under contention | hardware/thermo | ncand15 wall_max 6.30s (−12%) | **KEPT** |
| 10 | Pixel/image memory palace (ahash+dhash) | hardware/memory | perceptual-unique 246.3 MB (281 files) | **KEPT** |
| 11 | Shared agent state file (act as one) | speed/AGI-collab | 40 calls, 2.60s (5.01×) | **KEPT** |
| 12 | Valvular one-way bus id dedup | Tesla/collab | valve 8/32 (−75%) | **KEPT** |
| 13 | Zipf / resonance boot prefetch | speed/Tesla | prefetch hit 0.797, 7.18s (−32% time, +8.0 pp hit). | **KEPT** |
| 14 | Thermodynamic η=acc/tokens selector | thermo/token | picks stack η 2.803 (×10.5) | **KEPT** |
| 15 | SQLite mmap hardware path | hardware/speed | mmap p50 42.4 ms (−29%), tot 10140 (−29%), R@5 0.9674. cache_size alone did not  | **KEPT** |

## Net kept (11)

- **#1 Tesla valvular one-way line filter:** tokens 1725.3 (−26%), R@5 0.9674, acc 0.1953
- **#2 Free-energy / entropy sentence budget:** T=1.5 → tokens 1324.0 (−23% vs valve, −43% vs raw); R@5/acc held. Stack with #5 → 782.2 (−66% vs raw).
- **#5 Cross-hit entropy-zero line dedup:** tokens 1088.4 (−37% vs valve). Stack #2+#5: 782.2 (−66% vs raw).
- **#7 Bifilar dual-path query cache:** bifilar hit 0.707, 10.38s (−24% vs exact, −72% vs cold).
- **#9 Thermal-aware ncand under contention:** ncand15 wall_max 6.30s (−12%); recall5/acc unchanged. Solo gain <5% so gate is contention.
- **#10 Pixel/image memory palace (ahash+dhash):** perceptual-unique 246.3 MB (281 files); −12.8% vs raw; −28.7 MB beyond sha1 near-dupes.
- **#11 Shared agent state file (act as one):** 40 calls, 2.60s (5.01×); state 25 KB.
- **#12 Valvular one-way bus id dedup:** valve 8/32 (−75%); 8 unique ids preserved.
- **#13 Zipf / resonance boot prefetch:** prefetch hit 0.797, 7.18s (−32% time, +8.0 pp hit).
- **#14 Thermodynamic η=acc/tokens selector:** picks stack η 2.803 (×10.5); TEST tokens 782.2, R@5/acc held. Correctly ranks free-energy+dedup.
- **#15 SQLite mmap hardware path:** mmap p50 42.4 ms (−29%), tot 10140 (−29%), R@5 0.9674. cache_size alone did not help.

## Dropped (4)

- **#3 Landauer bit-budget / score-gap adaptive k:** Bit-budget B≤10 and gap-k thr≤0.5 all either cut DEV recall or matched valve tokens (noop on TEST). No measurable win.
- **#4 Simulated-annealing context prune:** DEV only λ=0 keeps acc (tokens 1207); λ>0 collapses acc. TEST λ=0 → 1657, worse than free-energy. Dropped.
- **#6 Tesla resonance query-order batching:** resonant 13409 ms (0.98×). No win — FTS cache already warm.
- **#8 Canon-path LRU / idf warm memo:** memo p50 57ms (no gain); idf warm 14.19s (1.005×). Dropped.

## Headline numbers (TEST)

| Config | tokens_brief | recall5 | acc |
|---|---:|---:|---:|
| raw allsee k=5 | 2326.2 | 0.9674 | 0.1953 |
| #1 valve | 1725.3 | 0.9674 | 0.1953 |
| #2 free-energy T=1.5 | 1324.0 | 0.9674 | 0.1953 |
| #5 dedup lines | 1088.4 | 0.9674 | 0.1953 |
| **#2+#5 stack (η-best)** | **782.2** | **0.9674** | **0.1953** |

Speed / hardware:
- Bifilar cache: hit 0.613 → 0.707, 13.72s → 10.38s
- Zipf prefetch on bifilar: hit 0.717 → 0.797, 10.5s → 7.18s
- Shared state (5 agents × 40 q): 13.03s → 2.60s (**5.01×**)
- Thermal ncand 15 under 8-way load: wall 7.16s → 6.30s (−12%), recall held
- SQLite mmap 256MB: p50 59.3 → 42.4 ms (−29%), recall held
- Pixel palace: 282.4 → 246.3 MB (−12.8%); −28.7 MB beyond sha1
- Bus valve: 32 → 8 forwarded (−75% on 4× replay)

## Notes for Einstein
- Accuracy never moved on TEST (0.1953): extractive number-answerer is the ceiling; wins are tokens/speed/storage.
- DEV acc is ~0.61 (different question mix); all gates used DEV for hyperparams, TEST for report.
- `allsee` links table is empty → spread/prior inventions are no-ops (dropped in speed_acc).
- Stack (#2+#5) is the deployable brief transform; #14 is the selector that found it.
- Disk used by this round: code + results JSON ≪ 1 MB (no new DBs, no venv).
