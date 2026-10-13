# Brain v2 — design (cycle 1, proposal only)
Modules: **Palace** (FTS5 chunks, citations) · **Graph** (fullpicture nodes/edges) · **Bus** (tools/collab bus.py, agent messages) · **Verifier** (citation check + abstain) · **Cache** (semantic, Jaccard≥0.75) · **Compressor** (dedup + summary-first) · **Router** (small extractive path vs large model) · **Mistake library** (dev misses → boosts) · **Tiered memory** (hot LRU / warm rick / cold full).
```mermaid
flowchart LR
 Q[Query from agent via Bus] --> C{Semantic cache}
 C -- hit --> A[Answer + citation]
 C -- miss --> R[Palace retrieve k=5..30] --> G[Graph expand neighbours] --> D[Dedup + summary-first]
 D --> RT{Router: verifier confident?}
 RT -- yes --> S[Small extractive answer] --> V[Verifier: citation check]
 RT -- no --> L[Large model with compressed context] --> V
 V -- pass --> A
 V -- fail --> M[Mistake library + abstain] --> Bus
 A --> Bus
 A --> T[Tiered memory reinforce]
```
Measured each cycle (c1 numbers in RESULTS.md): held-out cloze accuracy, verifier precision, tokens per query, cache hit rate and latency, recall@1/@5, and the no-regression test (test_c1.py).
