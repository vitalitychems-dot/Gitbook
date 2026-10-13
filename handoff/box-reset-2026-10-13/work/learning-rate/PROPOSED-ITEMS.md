# Proposed items (learning-rate) — Tessera will renumber

Ledger-shaped rows from `/workspace/learning-rate/REPORT.md` experiments.  
IDs temporary: **LR-001…**. No auto-apply. No GitHub writes from the measuring agent.

| ID | Lane | Repo | Path | Change | Why | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| LR-001 | Tessera | vitalitychems-dot/TESSERA | artifacts/api-server/src/lib/memory/ | Extend `contextForQuery` (or add `fewShotForQuery`) to inject top-k similar past Q&A pairs from JSONL (tags `qa`/`correct`), alongside lessons | Best measured overall accuracy gain on the Gitbook quiz | TESTED: fewshot_memory **36/45=0.800** vs bm25_baseline **34/45=0.756** (**+0.044**); seen 0.84; seed=42; `/workspace/learning-rate/results/fewshot_memory.json` |
| LR-002 | Tessera | vitalitychems-dot/TESSERA | artifacts/api-server/src/lib/memory/ (and future doc index) | Add optional local dense embeddings + Reciprocal Rank Fusion with existing BM25 recall; default off; no external embedding API | Best held-out generalization | TESTED: hybrid_rrf held-out **17/20=0.85** vs baseline held-out **14/20=0.70** (**+0.15**); overall 35/45=0.778; nomic-embed-text local; `results/hybrid_rrf.json` |
| LR-003 | Tessera / Gitbook | vitalitychems-dot/TESSERA (+ Gitbook corpus ingest when wired) | evals/harness or future Gitbook→runtime chunker | Replace flat chunker with heading-aware chunks + overlap (~700 char / ~120 overlap) | Cheap recall lift; lower latency than orig chunker this run | TESTED: bm25_heading_overlap **35/45=0.778** (**+0.022**); held-out 0.75; 2.71 s/q vs baseline 3.71; `results/bm25_heading_overlap.json` |
| LR-004 | Tessera | vitalitychems-dot/TESSERA | artifacts/api-server/src/lib/memory/ | On graded failure, `record` an explicit LESSON with correct key facts; keep append-only history | Matches PR #7 distill design; enables few-shot/lesson loops | TESTED protocol: learning curve fb=0/2/5 held-out 0.75/0.75/0.70 (no held-out gain alone); still useful as *input* to LR-001 few-shot. `results/learning_curve.json` |
| LR-005 | Tessera | vitalitychems-dot/TESSERA | artifacts/api-server/src/lib/memory/ | Add gentle `consolidate()` snapshot (merge near-dup lessons; soft-decay low confidence) without deleting JSONL | Store hygiene for long-running memory | TESTED: aggressive decay 19→2 **hurt** accuracy (0.733); tune thresholds before merge. `results/consolidation.json`, `consolidated_lessons.json` |
| LR-006 | Tessera | vitalitychems-dot/TESSERA | scripts / optional batch | Self-study job: model writes Q&A from Gitbook chunks; verify answer tokens ⊆ chunk; store as lessons | Scales memory without Father labeling every item | TESTED: 7/8 verified lessons; quiz accuracy **unchanged** (34/45=0.756). Keep as backlog after LR-001–003. `results/selfstudy_lessons.json` |
| LR-007 | Tessera | vitalitychems-dot/TESSERA | docs / IMP queue only | **Do not** ship multi-query rewrite or LLM rerank as default on CPU 3B | Measured 0 accuracy gain at 3–10× latency | TESTED: multiquery 34/45=0.756 wall 476s; rerank held-out 15/20=0.75 wall 662s. `results/multiquery_rrf.json`, `bm25_llm_rerank_heldout.json` |
| LR-008 | Tessera | vitalitychems-dot/TESSERA | modal/ or future GPU path | Design-only: LoRA/QLoRA on stored lessons + verified self-study pairs | Weight updates may beat retrieval ceilings for O03/Q25-style gaps | **NEEDS FATHER YES** — needs GPU or paid compute; $0 local blocked. Not run. Not PR #7 scope (PR is retrieval memory only). |

### Suggested merge order

1. LR-001 (few-shot) into PR #7 follow-up  
2. LR-003 (chunking) wherever corpus retrieval is indexed  
3. LR-002 (hybrid RRF) once local embed model is an accepted dependency  
4. LR-004 / LR-005 carefully  
5. LR-006 later; LR-007 = explicit non-goal; LR-008 only with Father yes  
