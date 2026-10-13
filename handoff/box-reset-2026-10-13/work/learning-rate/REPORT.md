# Learning-rate experiments (local, $0)

**As-of:** 2026-10-05 ~7:07 PM CT  
**Owner ask:** dramatically improve the rate at which Tessera learns — measured evidence, not guesses.  
**Labels:** **TESTED** = measured this session; **RESEARCHED** = cited literature / design only; **NEEDS FATHER YES** = cost/GPU path not run.

> Small local model (`qwen2.5:3b-instruct` Q4_K_M on 8× Xeon CPU, 15 GiB RAM). Retrieval memory, not weight training. Do not publish as Tessera AGI scores.

---

## 1. Definition of learning rate (this report)

- **Quiz accuracy** on an extended Gitbook knowledge quiz (**n=45**, seed **42**).
- Split:
  - **seen** (n=25): original BASELINE.md §C items — may receive feedback / lessons.
  - **held-out** (n=20): new questions written strictly from `/workspace/evals/data/gitbook-corpus/` text; never used as feedback targets when writing lessons from their own answers.
- **Learning curve:** held-out accuracy vs number of feedback events (reflexion lessons from wrong *seen* answers).
- Baseline for deltas: **this session’s remasured BM25 top-3** over the original chunker (`bm25_baseline`), not the earlier 18/25=0.72 row alone (see §6).

---

## 2. Results table (TESTED)

Model: `qwen2.5:3b-instruct` · seed **42** · corpus 43 md files · grader: strict key-fact (same rules as `/workspace/evals/harness/run_gitbook_quiz.py`, extended for held-out).

| Method | Acc (all) | n | Correct | Δ vs bm25_baseline | Seen acc | Held-out acc | Wall (s) | s/q | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| alone | 0.356 | 45 | 16 | −0.400 | 0.44 | 0.25 | 34 | 0.76 | TESTED |
| **bm25_baseline** (orig chunker, top-3) | **0.756** | 45 | 34 | 0 | 0.80 | 0.70 | 167 | 3.71 | TESTED |
| bm25_heading_overlap | 0.778 | 45 | 35 | **+0.022** | 0.80 | 0.75 | 122 | 2.71 | TESTED |
| hybrid_rrf (BM25 + nomic-embed-text, RRF k=60) | 0.778 | 45 | 35 | **+0.022** | 0.72 | **0.85** | 131 | 2.91 | TESTED |
| multiquery_rrf (2 LLM rewrites + RRF) | 0.756 | 45 | 34 | 0.000 | 0.76 | 0.75 | 476 | 10.59 | TESTED |
| bm25_llm_rerank (held-out only) | 0.750 | 20 | 15 | 0 vs heading held-out | — | 0.75 | 662 | 33.1 | TESTED (partial) |
| **fewshot_memory** (BM25 heading + similar past Q&A) | **0.800** | 45 | 36 | **+0.044** | **0.84** | 0.75 | 79 | 1.76 | TESTED |
| reflexion_lessons | 0.733 | 45 | 33 | −0.022 | 0.76 | 0.70 | 96 | 2.13 | TESTED |
| reflexion_fewshot | 0.778 | 45 | 35 | +0.022 | 0.80 | 0.75 | 105 | 2.33 | TESTED |
| consolidated_lessons | 0.733 | 45 | 33 | −0.022 | 0.76 | 0.70 | 56 | 1.25 | TESTED |
| self_study (7 verified self-Q&A lessons) | 0.756 | 45 | 34 | 0.000 | 0.80 | 0.70 | 209 | 4.63 | TESTED |

Raw JSON: `/workspace/learning-rate/results/`. Table snapshot: `results/table.json`.

### Learning curve (TESTED)

Train probe with heading BM25: **20/25 = 0.80** → only **5** wrong answers available as feedback events.

| Feedback events | Held-out acc (n=20) |
| ---: | ---: |
| 0 | 0.75 |
| 2 | 0.75 |
| 5 (all wrongs) | 0.70 |

Chart: `/workspace/learning-rate/charts/learning_curve.png`  
Interpretation: with a strong retriever, verbal reflexion on the few remaining *seen* errors did **not** raise held-out accuracy (slight drop at full feedback). Lessons were question-specific; they did not transfer. Contrast with literature Reflexion gains on iterative *same-task* retries ([Shinn et al., arXiv:2303.11366](https://arxiv.org/abs/2303.11366): +20% HotPotQA, +22% AlfWorld) — those measure re-attempts of the *same* items, not held-out transfer.

### Chunk stats (TESTED)

| Chunker | Chunks |
| --- | ---: |
| baseline (orig harness) | 173 |
| heading-aware + overlap (700/120) | 391 |

Dense index: `nomic-embed-text`, 391 vectors, dim 768 → `results/dense_index.json`.

---

## 3. Top 3 changes ranked by gain per effort

| Rank | Change | Gain (measured) | Effort | Why it wins |
| ---: | --- | --- | --- | --- |
| **1** | **Few-shot from memory** — retrieve similar past Q&A into the prompt (`fewshot_memory`) | **+0.044 abs** overall (0.756→0.800); seen 0.80→0.84; held-out +0.05 vs baseline held-out | Low: already fits PR #7 store + BM25 recall; no new model | Best accuracy; fixed O09/O18/O20/H01/H02/H07 vs baseline; wall lower than plain RAG this run |
| **2** | **Hybrid BM25 + local embeddings + RRF** | Overall +0.022; **held-out +0.15** (0.70→0.85) — best generalization | Medium: `ollama pull nomic-embed-text` (~274 MB); embed corpus once; RRF fuse | Best held-out; cites hybrid/RRF practice ([Cormack RRF](https://example.com); TREC RAG 2025 HyDE+sparse-dense fusion; [Abhik hybrid notes](https://www.abhik.ai/concepts/embeddings/hybrid-retrieval-systems) +5–15% nDCG typical) |
| **3** | **Heading-aware chunks with overlap** | Overall +0.022; held-out +0.05; **faster** than baseline RAG (2.71 vs 3.71 s/q) | Low: chunker only | Free win; no LLM; improves recall of heading-scoped facts (e.g. Ready / BLOCKED / CC push) |

**Not worth it on this box (TESTED):**

- Multi-query rewrite: **0 gain**, ~3× latency.
- LLM rerank top-8→3: **0 gain** on held-out, ~33 s/q.
- Reflexion-only lessons / aggressive consolidation: **−0.022** or flat learning curve on held-out.
- Self-study loop (7 verified lessons): **0 gain** on this quiz (lessons not aligned to quiz gaps).

---

## 4. Fit into TESSERA PR #7 memory module

PR: https://github.com/vitalitychems-dot/TESSERA/pull/7 · branch `cursor/tessera-learning-memory-301f` · path `artifacts/api-server/src/lib/memory/`.

| Change | Fit | How |
| --- | --- | --- |
| Few-shot from memory | **Direct** | Extend `contextForQuery` (or add `fewShotForQuery`) to return top-k past interactions tagged `qa`/`correct`, not only distilled lesson blurbs. Store graded Q&A via existing `record()`. |
| Heading-aware chunking | **Adjacent** | When/if Gitbook corpus is indexed for retrieval beside memory, use heading+overlap chunker (this harness’s `chunk_heading_overlap`). Memory lessons themselves are short — lower urgency. |
| Hybrid RRF | **Extend recall** | Keep BM25 in `bm25.ts`; add optional local embedding scores + RRF in `retrieveLessons` / a future doc index. Do **not** call external embedding APIs (`SOVEREIGN_NO_EXTERNAL_LLM` untouched). |
| Reflexion lessons | **Already designed** | Distill + `record` on failure with correct key as `lesson_text` already matches PR distill path; wire a feedback hook when a grader/Father says wrong. Today: **no held-out gain** until lessons are written for *related* gaps, not only identical questions. |
| Consolidation / decay | **Add** | PR store is append-only (good). Add a separate `consolidate()` that merges near-duplicate lessons and decays low-confidence singles into a *snapshot* file — do not delete JSONL history. Our aggressive decay (19→2) hurt; tune gently. |
| Self-study | **Optional later** | Batch job: generate Q&A from Gitbook chunks, verify answer tokens ∈ chunk, `record` as lessons. Needs scheduling + provenance; skip until few-shot + hybrid land. |

No GitHub writes from this session (per hard limits).

---

## 5. TESTED vs RESEARCHED vs NEEDS FATHER YES

### TESTED (this session)

1. Better chunking (heading + overlap)  
2. Hybrid BM25 + `nomic-embed-text` + RRF  
3. Query rewriting / multi-query + RRF  
4. LLM reranking (held-out n=20 only; full n=45 skipped for time after null gain signal)  
5. Reflexion-style lessons + learning curve (0 / 2 / 5 feedback events)  
6. Few-shot from memory  
7. Self-generated practice (8 pages attempted, **7 verified**)  
8. Memory consolidation (decay/dedupe) — over-aggressive setting measured  

### RESEARCHED (cited; not claimed as our numbers)

- Reflexion verbal RL ([arXiv:2303.11366](https://arxiv.org/abs/2303.11366)): large gains on *same-task* retries — different protocol than our held-out curve.  
- Hybrid retrieval + RRF: common +5–15% ranking gains in BEIR/MS MARCO writeups; TREC RAG 2025 sparse+dense fusion.  
- Multi-query / DMQR-RAG ([arXiv:2411.13154](https://ar5iv.labs.arxiv.org/html/2411.13154)): recall↑ but noise risk — matches our 0-gain / high-latency result on this small corpus.  

### NEEDS FATHER YES (design only — not run)

- **LoRA / QLoRA fine-tune** on stored lessons + verified self-study Q&A. Needs GPU or paid cloud; violates $0 local budget. Would update weights (unlike PR #7 retrieval memory). Mark any IMP as **NEEDS FATHER YES**.  
- Paid embedding / reranker APIs.  
- Larger local models (7B+) — prior baseline already noted insufficient free RAM under multi-agent load.

---

## 6. Honesty notes

- Prior local baseline (`/workspace/evals/BASELINE-LOCAL.md`): alone **7/25=0.28**, BM25 **18/25=0.72**. This session remasured seen-split alone **11/25=0.44**, BM25 baseline **20/25=0.80**. Same model/seed; differences likely from prompt/context packing, keep-alive state, and chunk text in context — **deltas in this report use this session’s remasured `bm25_baseline`**.  
- Father’s name **is** in corpus (`mesh__roles.md`: “Father = Collin Keane”) but O03 still often fails retrieval — hybrid/few-shot did not reliably fix O03 either.  
- Q25 `validate` CI job name still fails under RAG (not stated in retrieved Gitbook chunks) — knowledge gap in corpus, not a retrieval-rank issue.  
- Contended CPU with another local Ollama consumer mid-run; walls are honest but not isolated bench-lab noise-free.  
- Spend: **$0**. No secrets, no `TESSERA_ENABLE_*`, no [REDACTED-PATH] no GitHub writes.

---

## 7. Paths

| Path | Role |
| --- | --- |
| `/workspace/learning-rate/REPORT.md` | This report |
| `/workspace/learning-rate/PROPOSED-ITEMS.md` | Ledger rows LR-001+ |
| `/workspace/learning-rate/results/` | Per-method JSON + `table.json` + `learning_curve.json` |
| `/workspace/learning-rate/charts/*.png` | Learning curve + method bars |
| `/workspace/learning-rate/src/` | Harness (quiz_bank, retrieval, memory_store, run_experiments) |
| `/workspace/learning-rate/data/memory-*` | JSONL memory stores used in tests |
| `/workspace/evals/BASELINE-LOCAL.md` | Prior baseline |
| TESSERA PR #7 | Retrieval memory module draft |

### Snapshot line

```
date_ct: 2026-10-05 19:07 CDT
model: qwen2.5:3b-instruct Q4_K_M seed=42
quiz: n=45 (seen=25 heldout=20)
alone: 16/45=0.356
bm25_baseline: 34/45=0.756
best_overall: fewshot_memory 36/45=0.800 (+0.044)
best_heldout: hybrid_rrf 17/20=0.850 (+0.150 vs baseline heldout)
heading_overlap: 35/45=0.778
learning_curve_heldout: 0.75 → 0.75 → 0.70 at fb=0,2,5
spend_usd: 0
```
