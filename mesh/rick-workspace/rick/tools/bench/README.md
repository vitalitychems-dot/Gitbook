# Rigorous invention bench

Honest before/after with confidence intervals, paired significance, and
Benjamini–Hochberg FDR. Father's rule (2026-10-13): **token efficiency →
speed → accuracy**; only measured wins that beat baseline count.

## What it measures

| Metric | Direction | How |
|---|---|---|
| `hit@1` / `hit@5` | ↑ | Gold `file` in top-k (path or aliases) |
| `accuracy` | ↑ | Extractive number answerer == gold `a` |
| `tokens/query` | ↓ | `len(brief)//4` proxy (same as allsee/qinvent) |
| `latency_p50_ms` / `latency_p95_ms` | ↓ | Per-query mean over `--repeats` timed runs; percentile across queries |
| `disk_bytes` | ↓ | Sum of brief UTF-8 bytes (+ optional artifact dir) |

Every aggregate gets a **95% bootstrap CI** (`--n-boot`, default 1000).

## Held-out + leak guard

- Fixed TEST: `split=="test"` rows from `/workspace/rick/cycles/c1/qa_set.json`.
- DEV is **not** used here (tune elsewhere; report on TEST only).
- Leak filter drops hits whose path matches `qa_set`, `/cycles/`,
  `/tools/fraction/`, `/tools/bench/`, `allsee/rounds`, `synapse`.

## Significance + keep rule

Paired tests on the same TEST items:

- Binary (`hit@*`, `accuracy`): **McNemar** exact / continuity-corrected.
- Continuous (`tokens/query`, per-query latency): **Wilcoxon signed-rank**.
- Percentile latency / disk: paired **bootstrap** (disk uses 1% relative threshold).

All raw p-values are BH-adjusted at α=0.05.

**KEPT** iff ≥1 BH-significant improvement **and** 0 BH-significant regressions.
Otherwise **DROPPED** (or `SOFT_KEEP_NS` if only non-significant point gains and no regressions — still not a keep for Father's gate).

## Regression guard

`baseline.json` freezes a reference system (usually `raw`). Any candidate
whose CI sits clearly on the worse side of a frozen metric (>1% relative)
is force-dropped, even if it beat the run's `--baseline`.

```
python3 bench.py freeze --system raw
python3 bench.py check          # re-check last_result.json
```

## CLI

```
python3 bench.py run --baseline raw --candidate stack25
python3 bench.py run --baseline path.py:fn --candidate other.py:fn
python3 bench.py freeze --system raw
python3 bench.py check
```

Built-ins: `raw`, `valve`, `stack25` (#2 free-energy + #5 dedup on valve).

Options: `--k 5`, `--repeats 5`, `--n-boot 1000`, `--alpha 0.05`, `--out result.json`.

Exit code 0 only on `KEPT`.

## Layout

```
bench.py      CLI
stats.py      bootstrap CI, McNemar, Wilcoxon, BH
metrics.py    per-query eval + aggregates
systems.py    builtins + path.py:fn loader
leak.py       path denylist
baseline.json frozen regression reference
last_result.json most recent run
RESULTS.md    demo write-up
```

## Merge freeze

Open PRs only. This harness stays local under `/workspace/rick/tools/bench/`.
No merges until Security PASS on the exact head SHA and CI green.
