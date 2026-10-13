# Cycle 1 results (2026-10-13, ~2:20 AM CT): measured, local only, nothing pushed
Rerun: `python3 quantum.py && python3 brain.py && python3 empathy.py && python3 test_c1.py`. Tests pass 7/7.
QA set (qa_set.json): 400 cloze questions auto-built from /workspace/rick and TESSERA-ro .md files (one number masked per sentence). The dev/test split is held out **by file** (185 dev / 215 test). Caveat: only 101 of the 215 test gold files are in the palace (the rest are >64KB or outside its roots), so **the recall ceiling is about 0.47**. Tokens ≈ chars/4.

**SMARTER**
1. S1 RAG + citation check: palace top-5, extract a number, check that it appears in the cited chunk. Test: held-out accuracy. Result: acc 0.181 (same as the k=1 baseline). The check accepted 206/215, but precision was only 0.165, so **the check is too weak**. Propose: no, rework it.
2. S2 self-consistency (5 query variants, majority vote). Result 0.181, **no gain** over S1. Propose: no.
3. S3 verifier/critic loop (widen k 5→15→30, abstain if the citation fails). Result: answered 206, precision 0.165, acc_all 0.158 (worse). Propose: no (it needs a stronger verifier, e.g. an LLM judge).
4. S4 mistake library (78 dev misses → file boosts at test time). Result 0.181, **no gain** (held-out files never appear in the dev library because of the split by file). Propose: yes as infrastructure (logging), no as an accuracy claim.
5. S5 curriculum eval harness (easy/medium/hard by query length). Result: easy 0.116 (n=138), medium 0.265 (68), hard 0.556 (9). Finding: long queries do *worse* (BM25 OR-query dilution). Propose: **yes**, the harness is useful.

**FASTER / TOKENS**
6. F1 prompt compressor (keep only lines with query terms). It saved 5.9% of tokens with the answer kept 100%. Small win. Propose: yes (cheap).
7. F2 semantic cache (Jaccard ≥0.75 on term sets). 430 queries, hit rate 0.756; hit 0.028 ms vs miss 9.7 ms (~350×). Note: half the stream was synthetic paraphrases. Propose: **yes**.
8. F3 context dedup (5-shingle Jaccard ≥0.5) on top-10 context: 2.05M → 0.80M tokens, **60.8% saved, answer kept 100%**. Propose: **yes (best result)**.
9. F4 summary-first retrieval (2 heading lines + the best line per chunk): **89.1% saved**, answer kept 94.7%. Propose: yes, with a fallback to full chunks.
10. F5 small-to-large router (extractive path when the verifier passes): 95.8% routed small, avoiding 1.02M of 1.05M large-model tokens, **but the small-path accuracy is only 0.165**, so the router trusts a weak verifier. Propose: not until #1 and #3 improve.

**STORAGE / CONTEXT / RECALL** (gold file in top-k; ceiling ≈0.47)
11. M1 tiered memory (hot LRU 64 / warm rick / cold full). recall@5 0.451 (= baseline); 2-pass tiers hot 27, warm 6, cold 397; 15.9 ms avg. The hot tier works, but the warm tier rarely hits. Propose: yes (hot tier only).
12. M2 graph-linked recall (expand the query with top graph neighbours). @1 0.428, @5 0.451, **identical to the baseline**, so no measurable effect. Propose: no.
13. M3 decay + reinforcement (dev successes, 0.9^age boost). @1 0.423 (−0.005), @5 0.451. Propose: no.

**QUANTUM** (quantum.py, numpy + qlab, all CONFIRMED in simulation)
14. Q1 CHSH: classical max over all 16 deterministic strategies = 2; Bell state = 2.828427 = 2√2 (Tsirelson); a 20k random-observable search maxed at 2.784 ≤ 2√2. CONFIRMED.
15. Q2 no-cloning: the Bužek-Hillery cloner isometry gives fidelity 0.833333 = 5/6; the CNOT copier gives 0.656 (MC estimate of 2/3); the best of 3,000 random isometries is 0.801 < 5/6. CONFIRMED (sampling evidence, not a proof of optimality).
16. Q3 Grover: optimal iterations for N=16..1024 fit a log-log slope of 0.523 (theory 0.5); N=1024 → 25 iterations, p=0.9995. CONFIRMED.
17. Q4 AQFT error bound ‖QFT−AQFT_m‖₂ ≤ πn·2^-m (n=4..6): it holds for all 12 cases. Example: n=6, m=5 gives err 0.098 vs bound 0.589. The bound is loose (~6×) and is vacuous for small m (err ≤2 anyway). CONFIRMED.
18. Q5 VQE H2 (STO-3G, R≈0.735 Å, 2-qubit reduced Hamiltonian, standard literature coefficients; 1-parameter particle-conserving ansatz): E = −1.857275 Ha electronic, error 7e-16 vs exact diagonalization (chemical accuracy 1.6e-3). CONFIRMED (the ansatz is exact for this 2-qubit H, as expected).

**EQ / BRAIN**
19. EQ plan (EQ-PLAN.md): 7 open datasets with licenses and sizes, plus a 4-step curriculum. NC licenses (EmpatheticDialogues, DailyDialog) are flagged. Propose: yes.
20. Empathy baseline (empathy.py): GoEmotions (Apache-2.0, 3.9MB) single-label → pos/neg/ambiguous/neutral, numpy Naive Bayes with bigrams. Test n=4,590: **acc 0.590 vs majority 0.349, macro-F1 0.509** (pos 0.69, neg 0.47, amb 0.29, neu 0.58). Propose: yes as a baseline to beat.
21. Brain v2 design (BRAIN-V2.md): palace + graph + bus + verifier + cache + compressor + router + mistake library + tiers, with a mermaid data flow and the metrics per cycle. Propose: yes as the design.
22. Held-out QA benchmark (qa_set.json, 400 Qs, split by file): the first reproducible cycle-over-cycle metric. Propose: **yes**.
23. Palace coverage gap finding: 114/215 test gold files are not indexed (the 64KB cap and the roots), which caps recall at ≈0.47. Fixing coverage beats any reranker tried. Propose: **yes (top next step)**.
24. test_c1.py regression gate (7 assertions over all result files). Propose: yes.
25. Cleanup: removed /workspace/rick-audit (12,909,166,864 bytes, clean clones) and rebuilt the palace without it (2,441 docs, 18.9MB, 1.5s). Disk went from 92% to 82%, with 23.6GB free.

Honest bottom line: the real wins are token savings (dedup 61%, summary-first 89%, cache ~350× on hits). None of the "smarter" tricks beat the baseline yet, because the extractor and verifier are lexical. Next cycle: fix palace coverage, add an LLM or NLI verifier, and remeasure.
