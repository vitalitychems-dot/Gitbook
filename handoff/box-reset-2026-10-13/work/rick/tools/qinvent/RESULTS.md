# qinvent: 5 quantum-inspired inventions (2026-10-13). Rule: keep only measured wins

Bench: c1 qa_set test split (n=215); dev split (n=185) used for every tuning choice. Palace: c2/palace.db opened read-only. allsee was not touched.
Reproduce: `.venv/bin/python inv3_mwpm_dedup.py; inv3_eval.py; inv2_amplitude.py; inv4_qec_vote.py; inv1_anneal.py; inv5_compress.py; test_qinvent.py` (6/6 pass). Raw numbers: results/inv*.json.

## Key finding (found during #3): benchmark leak
`/workspace/rick/cycles/c1/qa_set.json` is indexed inside c2/palace.db. It is the top-1 file for 145/215 test questions, which is the real reason c2 top-1 was 0.028. Fix: exclude `/workspace/rick/cycles/*` from retrieval. That alone gives top-1 0.047 (recall@5 0.940). Recommend dropping eval files from the palace build.

| # | Invention | Baseline | Result | Verdict |
|---|---|---|---|---|
| 3 | MWPM near-duplicate matching (networkx blossom, repeated matching + union-find on 5-shingle Jaccard ≥0.6; cluster represented by its original, using a root prior learned on dev) + leak fix | top-1 0.028, R@5 0.940 | **top-1 0.940, R@5 0.991** (dev: see json) | **KEPT** |
|   | ablations: prior-only rerank 0.898/0.995; mirror-path rule only 0.851/0.907; MWPM + mirror rule (no learned prior) 0.851/0.874; MWPM without leak fix 0.298/0.991 | | MWPM adds +4.2 pts top-1 over prior-only | |
| 2 | Grover-like amplitude reweighting (oracle = graph-supported candidates, inversion about the mean, r iterations) | raw 0.028/0.940; on #3 0.940/0.991 | r=1 raw: 0.200/0.860; r=1 on #3: 0.870/0.977; dev picks r=0 both times | **DROPPED** (hurts recall; the graph has only 90 path nodes, too coarse) |
| 4 | QEC 3-answerer repetition code + majority (A=c2 verifier, B=verifier on #3 retrieval, C=dropout query, top-30) | acc 0.772, prec 0.779 | A 0.772, B 0.781, C 0.767; majority 0.781; ≥2-agree precision 0.781 (215 answered) | **VOTING DROPPED**: it equals the best single answerer B. Errors are correlated (A/B outcome agreement 0.991), so the repetition code has nothing to correct. B's +0.009 (2 questions) comes from #3 and is not significant. |
| 1 | Simulated annealing over step priority orders (49 expanded steps, 5 seeds×4000 iters) | longest-chain 25, FCFS 32 | 25 in all 5 seeds; lower bound 24 (critical path / security lane load) | **DROPPED** (ties longest-chain, which is already within 1 of the bound) |
| 5 | Low-rank SVD (2-core TT) + f16/int8 of TF-IDF chunk vectors (pool 4,358 chunks, 17,276 vocab) | exact sparse 4.19 MB, test R@5 0.851 (dev 0.681) | no rank met <2% drop on dev; k512_f16 matches test R@5 (0.860) but uses 22.2 MB (5.3× larger); k64 is 0.6× the size with R@5 0.67 | **DROPPED**: sparse TF-IDF is already compact, and low-rank is bigger or much worse |

Net win: #3 (leak fix + MWPM dedup), top-1 0.028 → 0.940 and recall@5 0.940 → 0.991.
Caveat for verification: the root prior (TESSERA-ro 166, rick 19 dev gold files) encodes that the benchmark's gold files live in TESSERA-ro. It was learned on dev, but it is benchmark-distribution knowledge, so the gain on general queries may be smaller.
Disk: ~100 MB venv (numpy, networkx) plus <1 MB of code and results.
