# Bench harness — design brief + demo

**Date:** 2026-10-13 (America/Chicago)  
**Path:** `/workspace/rick/tools/bench/`  
**Merge freeze:** local only; no merges.

## Design brief

### Goal
Replace hand-waved “it improved” claims with a single gate every invention must pass:
fixed held-out TEST, leak-proof retrieval, bootstrap CIs, paired significance,
BH multiple-testing correction, and an automatic KEEP/DROP.

### Data
| Item | Value |
|---|---|
| QA | `/workspace/rick/cycles/c1/qa_set.json` |
| Split | `split == "test"` only (n=215). DEV unused at report time. |
| Index | `allsee.db` read-only |
| Leak denylist | `qa_set`, `/cycles/`, `/tools/fraction/`, `/tools/bench/`, `allsee/rounds`, `synapse` |

### Metrics (all with 95% bootstrap CI, ≥1000 resamples)
1. **hit@1 / hit@5** — gold file in top-k (path or aliases)
2. **accuracy** — extractive number answerer == gold
3. **tokens/query** — `len(brief)//4` (same proxy as allsee / qinvent)
4. **latency p50 / p95** — mean of `--repeats` timed end-to-end calls per query; percentile across queries
5. **disk_bytes** — sum of brief UTF-8 bytes (+ optional artifact dir)

### Inference
| Family | Test |
|---|---|
| Binary (hit, accuracy) | McNemar (exact n&lt;25, continuity-corrected χ² otherwise) |
| Continuous (tokens, per-query latency) | Wilcoxon signed-rank (exact n≤20, normal approx otherwise) |
| Percentile latency | Paired bootstrap of percentile delta |
| Disk | 1% relative threshold (deterministic) |
| Multiplicity | Benjamini–Hochberg FDR, α=0.05 |

### KEEP rule
**KEPT** iff ≥1 BH-significant improvement **and** 0 BH-significant regressions.
Plus regression guard vs frozen `baseline.json` (force-DROP if candidate CI is clearly worse on any frozen metric by &gt;1%).

### CLI
```
python3 bench.py freeze --system raw
python3 bench.py run --baseline raw --candidate stack25 --repeats 3 --n-boot 1000
python3 bench.py check
```
Built-ins: `raw`, `valve`, `stack25`. Also accepts `path.py:fn`.

### Priority (Father)
Token efficiency → speed → accuracy. Only built+tested before/after numbers count.

---

## Demo: qinvent/round3 #2+#5 brief stack

**Candidate:** `stack25` = free_energy(T=1.5) ∘ dedup_lines ∘ valve on allsee k=5  
(source: `/workspace/rick/tools/qinvent/round3/tokens.py` + `combo.py`; files present)  
**Baseline:** `raw` allsee k=5  
**Config:** TEST n=215, timing_repeats=3, n_boot=1000, α=0.05  
**Artifact:** `demo_stack25.json`, `baseline.json` (frozen raw), `last_result.json`

### Aggregate metrics (point [95% CI])

| Metric | Baseline (raw) | Candidate (stack25) |
|---|---:|---:|
| hit@1 | 0.3814 [0.3163, 0.4465] | 0.3814 [0.3163, 0.4465] |
| hit@5 | 0.9674 [0.9442, 0.9907] | 0.9674 [0.9442, 0.9907] |
| accuracy | 0.1953 [0.1442, 0.2512] | 0.1953 [0.1442, 0.2512] |
| tokens/query | 2173 [2095, 2248] | **739.1 [681.2, 797.3]** |
| latency_p50_ms | 45.44 [43.3, 47.78] | 45.01 [44.16, 47.34] |
| latency_p95_ms | 96.39 [86.59, 102.5] | 81.96 [77.74, 91.11] |
| disk_bytes (briefs) | 1.874e6 | **6.366e5** |

### Paired tests (Δ = candidate better when positive)

| Metric | Δ | Δ 95% CI | p_raw | p_BH | |
|---|---:|---:|---:|---:|---|
| hit@1 | 0 | [0, 0] | 1.0 | 1.0 | held |
| hit@5 | 0 | [0, 0] | 1.0 | 1.0 | held |
| accuracy | 0 | [0, 0] | 1.0 | 1.0 | held |
| **tokens/query** | **+1434** | **[+1361, +1507]** | **5.0e-37** | **2.0e-36** | **WIN** |
| latency_mean_ms | +2.02 | [+0.34, +3.72] | 0.92 | 1.0 | ns |
| latency_p50_ms | +0.43 | [−2.06, +2.48] | 0.77 | 1.0 | ns |
| latency_p95_ms | +14.42 | [+0.29, +19.74] | 0.038 | 0.101 | ns after BH |
| **disk_bytes** | **+1.237e6** | — | 0 | 0 | **WIN** |

### Verdict
**KEPT** — significant token (−66.0%: 2173 → 739) and disk wins; hit@1/@5/accuracy held exactly; no significant regressions; regression guard OK vs frozen raw.

Matches the prior qinvent round3 claim (−66% tokens, R@5/acc held). Absolute token levels differ slightly from the older 2326→782 numbers because this harness applies the leak filter to every hit list (fairer held-out); the relative win is the same.

### Reproduce
```
cd /workspace/rick/tools/bench
python3 bench.py freeze --system raw --repeats 3 --n-boot 1000
python3 bench.py run --baseline raw --candidate stack25 --repeats 3 --n-boot 1000 --out demo_stack25.json
```

Exit code 0 on KEPT. Merge freeze unchanged — nothing pushed.
