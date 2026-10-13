# Memory Palace (invention #1)
A read-only local search index of mesh knowledge. Python stdlib only.
- Sources: .md/.txt files (≤512KB) under /workspace/rick, /workspace/TESSERA-ro and /workspace/gitbook-gate-1e3bb50 (override with PALACE_ROOTS=a:b). The sources are only read, never written.
- Chunks are 30-line slices with path and line range, stored in SQLite FTS5 ranked by bm25. A pure-Python BM25 fallback runs if FTS5 is missing.
- Rooms are named root/topic. The topic comes from keyword clustering (quantum, bhnmc, tesla, rules, agents, inventions, code); if nothing matches, the top-level folder is used.
- Build writes a temp DB and then does an atomic replace, so rebuilds are idempotent.

Usage: `python3 palace.py build | search 'query' | rooms | stats`
Tests: `python3 test_palace.py` (synthetic recall@5, citations, BM25 fallback, idempotence). Real eval: `python3 evalreal.py`.

Measured on 2026-10-13: 307 docs, 1333 chunks, 3.7MB DB, 0.47s build, query median 2.0ms (max 6.7ms). Strict recall@5 on 10 real queries: 8/10. The two misses ("BHNMC baseline", "round 2") returned INVENTIONS.md, which also holds those facts.
