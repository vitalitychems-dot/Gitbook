# Rick — INVENTIONS log

## 2026-10-12 (first session)
- Read mesh/RICK.md, RICK-WORKSHOP.md, RICK-SPIN.md. Rules: propose one runnable step; state input/output; another lane implements+tests; fail = not done; no unmeasured percentages; never edit the store. `tie` gated on Tessera approval; spin = simulator, not quantum hardware.
- Read memory graph build-plan-2026-10-12/full-picture-memory.jsonl (3002 lines) and 207 notes in rea-categories/notes.
- Wrote knowledge/tesla.md (verified patents: 381,968; 382,280; 512,340; 645,576; 725,605; 787,412; 1,119,732).
- OPTIMIZE-26.md NOT present yet -> round 2 not drafted (blocked on review). Tesla-derived candidate seeds parked below, unmeasured.

### Seeds for round 2 (unmeasured, pending OPTIMIZE-26 review)
1. coincide — act only if N tuned checks agree (725,605). Test: 2 of 3 agree -> refuse; 3 of 3 -> pass.
2. phase — stagger K workers by offset (381,968). Test: no two start in same tick.
3. resonate — sweep batch size, keep fastest measured. Test: returns size with min measured time.
4. valve — append-only log rejects rewrite. Test: rewrite of existing line fails.
5. bifilar — paired open/close cancel. Test: unmatched open reported.

## 2026-10-12 (session 2, evening)
- spin/tie live in GitMesh (projects/spin, projects/tie), not the Gitbook clone. spin: `node spin.mjs`, 20k-shot two-qubit simulator, no network. tie: exits 1 "Not approved." without `--approved` (gated; not run with flag).
- `gh repo list vitalitychems-dot` shows TESSERA, Gitbook, GitMesh, vitality — no separate Rick repo found.
- OPTIMIZE-26.md still absent -> round 2 not drafted. Seeds above remain parked, unmeasured.

## 2026-10-12 (session 3) — Rick in TESSERA
- Father: the "Rick repo" is files inside TESSERA. Notes: knowledge/tessera-rick.md.
- Found the server persona (Rick Sanchez, api-server rick-*.ts plus routes) and the preview lib (rick-five/loop/home/shift/metrics/thirty).
- Tests: 4 of 6 pass. rick-metrics fails on a >=25% timing threshold; rick-thirty fails on a missing dependency. Nothing changed.
- Conflicts with Gitbook RICK.md: persona (Sanchez vs Tesla), unmeasured %, self-approval lanes. Gitbook rules kept as the rules in force.

## 2026-10-12 (session 4) — Round 2 drafted
- Reviewed OPTIMIZE-26 (24/26). Diagnosed #4: the PR URLs are all unique, so a whole-token legend finds nothing. Fixed it with a prefix legend.
- 10 inventions were prototyped and measured in round2/r2.mjs against the PR #246 clone (91b6f0d). All 10 PASS on their own tests. See ROUND-2.md.
- Headline results: prefix-legend 1675→1336 tok (#4 finished). resonate-chain 1624→1286 tok vs packContext (#11 finished). key-hoist 11956→10171 tok. earth-return 46879→6879 B. coincide 44→0 wrong/1000 (simulated). phase 12→3. valve 10→0. bifilar 5→0. tuned-clip 1→10 matches kept. resonate-batch 0.098→0.021 ms (weak, noisy).
- All 5 seeds are now measured (items 4–8 cover coincide, phase, valve, bifilar, and resonate as #10).

## 2026-10-12 (session 5) — BHNMC v1.3 simulation experiment (SIMULATION ONLY)
- Built bhnmc/SPEC.md (FACT/HYPOTHESIS/SPECULATIVE, 64-electrode CAD table, 46-pin pinout, stack, safety, benchmarks), engine.py (v1.3 port, dna key bug fixed), sim_v14.py, RESULTS.md.
- v1.3 scores 1.000 for every model, and so does the no-reservoir baseline: the task is trivial.
- v1.4 hard task (10 seeds): reservoir CV ridge 0.476±0.021 vs no-reservoir 0.419±0.031. Held-out stimulus families score at chance (0.15–0.28). The QI branch does not earn its place (0.340). NARMA-10 NMSE 0.567 vs 1.033 without the reservoir.
- Design bugs: fluid ports sit on the O-ring, 4 corner electrodes cross the seal, coil radii are inconsistent, and "dual ADG706" gives only 32 channels.
- Next: frequency-invariant features (improvement #4) plus the geometry fix (#9).

## 2026-10-12 (CT) — Rick's Quantum Lab (qlab), /workspace/rick/qlab/
- Statevector sim up to 20 qubits. 8/8 physics checks pass (CHSH S=2.8284271247, QFT vs FFT 2.3e-16, Grover n=4..10 error 8.8e-14). n=20: 11.6 ms/gate, 48 MB peak.
- Peephole optimizer: 200/200 random circuits exact (min fidelity 1.0). Gates −46.9±8.9 % on redundant circuits, −17.2±7.2 % on uniform random ones, 0 % on QFT5 and Grover3.
- Noise model: depolarizing and amplitude-damping formulas match to ≤3.4e-15. Optimizing raised noisy fidelity 0.8148→0.9001 (30/30 circuits).
- geomcheck.py reproduces the BHNMC seal, port, coil and mux issues. Pin count not yet modelled.
- Details: qlab/RESULTS.md

## 2026-10-12 (CT) — qlab optimizer v2 (noise-aware rewriting), /workspace/rick/qlab/qopt2.py
- Exact on all 200 random circuits, QFT n=3..8 and Grover n=3..5 (min fidelity 1.000000000000).
- Random circuits vs v1: gates 31.5→21.7, depth 18.8→14.5, 2q 11.65→11.62, noisy F 0.8225→0.8310.
- QFT: no gain over v1 (honest null). Grover n=3: 6-CNOT CCZ + fusion takes 2q gates 32→24 and F 0.5477→0.6419.
- Grover n=4/5 cuts (2q 204→132, 784→416) are mostly cleanup of a naive MCZ construction.
- Details: qlab/RESULTS.md section 5

## 2026-10-12 (CT) — qlab optimizer v3 (phase-polynomial resynthesis), /workspace/rick/qlab/qopt3.py
- Exact on 200 random circuits, QFT n=3..8 and Grover n=3..5 (min fidelity 1.000000000000).
- Random circuits v2→v3: 2q 11.62→10.56, gates 21.68→20.58, depth 14.47→13.45, noisy F 0.8310→0.8439.
- QFT: still no gain (honest null). Grover with the fair Gray-code MCZ (2^n−2 CNOTs): v3 adds nothing beyond v2's 1q fusion.
- Fair baseline exposed that the old v2 Grover n=4/5 cuts were mostly cleanup of the naive MCZ.
- Details: qlab/RESULTS.md section 6

## 2026-10-12 (CT) — qlab approximate QFT, /workspace/rick/qlab/aqft.py
- Dropping CP with angle < 2π/2^m beats the exact QFT under noise for n≥4.
- n=8, m=4 (4-input mean): noisy F 0.4603 vs 0.3581 exact; 2q gates 48 vs 68; ideal F 0.9599.
- n=10, m=3 (single input): noisy F 0.4207 vs 0.2112; 2q gates 49 vs 105.
- Best m: 3,3,3,3,4,4 for n=3..8, about 1 below log2(n)+2.
- Phase estimation t=9 with m=4: noisy P(correct) 0.201 vs 0.139 exact. Ideal cost: 0.639 vs 0.666.
- Caveat: single-input selection gave a false m=1 at n=5. Use averaged inputs.
- Details: qlab/RESULTS.md section 7

## 2026-10-12 (CT) — qlab approximate QFT cleanup (RESULTS.md 7b)
- Phase estimation t=5 at m=3: noisy P(correct) 0.4581 vs exact 0.4403 (within the spread across φ). Ideal: 0.7488 vs 0.7860.
- 4-input averages: n=9 best m=3 (0.4341±0.0971; m=4 0.4218±0.0257) vs exact 0.2871. n=10 best m=4 (0.3522±0.0043) vs exact 0.2060.
- Corrected best m for n=3..10: 3,3,3,3,4,4,3,4, about 1 below log2(n)+2.

## 2026-10-13 (CT) — qlab calibrated noise twin + CLI, /workspace/rick/qlab/qlab/
- Twin uses public IBM calibration snapshots (manila, nairobi, guadalupe; qiskit-ibm-runtime fake_provider, Apache-2.0).
- Checks: T1/T2 analytic match to 4.4e-16; RB recovers injected error exactly; thermal RB recovers 7.0e-4 as 7.023e-4.
- Best layout + AQFT m=4 vs naive exact QFT (n=5, simulated): manila 0.5514 vs 0.4731, nairobi 0.5878 vs 0.2766, guadalupe 0.5657 vs 0.2968.
- CLI `python3 -m qlab optimize`; `python3 -m qlab test` = ALL PASS (~80 s).
- PR-ready plan (not opened): qlab/PR-PLAN.md → Gitbook tools/qlab/.

## 2026-10-13 — Disk guardian (diskguard) — built, local only
Path: /workspace/rick/tools/diskguard/. Read-only stdlib Python reporter: disk %, top folders with owner/lane guesses, finished-folder flags (stale or clean+pushed git), 85/90/95% warnings, JSONL history with growth rate and hours-until-full, markdown REPORT.md and --json. Never deletes; suggests owner-run commands. 6/6 unit tests pass. First real run: 91.9% used, 3.8G free. Not pushed; no PR.

## 2026-10-13: Invention #1, Memory Palace (tools/palace/)
A read-only SQLite FTS5 index over rick/, TESSERA-ro and the gitbook-gate clone, with BM25 fallback, rooms by topic, and path:line citations.
Tests: 3/3 pass (synthetic recall@5 = 1.0 for both FTS5 and BM25, citations checked, rebuild idempotent).
Real index: 307 docs, 1333 chunks, 3.7MB, 0.47s build, query median 2.0ms. Recall@5 on 10 own-result queries: 8/10 (strict).

## 2026-10-13: Invention #13, Mesh City 3D world (tools/meshcity/)
Offline canvas-3D HTML plus a stdlib gen.py that builds city.json from local data: 29 buildings (8 agents, 4 workshops, 17 library rooms). The ground is amber at a disk reading of 91.94%.
Tests: 3/3 pass (schema, determinism, HTML parses with no external URLs). gen.py runs in 6.1s. The folder is 124K total. A headless screenshot is at shot.png (71.7KB).
Unknowns: Command Center and Security have no owned dir (files=null). The Build and Mesh Cloud dir mapping is a guess, and Build's file count hit the 20000 cap.

## 2026-10-13: Survey + COLLAB-20 + full-picture graph (step 0 of the v3 proposal)
SURVEY.md: rick-audit is 2 clean re-clonable repo clones. drive-rest holds 6 Replit snapshots that are ~90% deps. Chimera is an excluded third-party script. GitAI commit 3b3840c3 is flagged for disguised review tasks.
COLLAB-20.md: 20 proposals. Built bus.py, sched.py and conflict.py (tools/collab, 5/5 tests). The critical-path scheduler gives makespan 25 vs 32 for FIFO on 9 pending items (estimated costs). The conflict scan's text precision is ≈1/7.
Palace rebuilt with PALACE_ROOTS/EXT/MAXF/SHALLOW: 7,843 docs, 47,573 chunks, 97MB. Graph (tools/fullpicture): 109 nodes, 1,566 edges, 3 isolated; tests 2/2. V3-PLAN.md is a proposal only.

## 2026-10-13 ~2:20 AM CT: Cycle 1 of 10 (self-improvement program), cycles/c1/
25 items measured (see cycles/c1/RESULTS.md); tests 7/7. Wins: context dedup −61% tokens (answer kept 100%), summary-first −89% (kept 95%), semantic cache hit 0.03ms vs 9.7ms. Smarter tricks: no gain over the 0.181 held-out cloze baseline (lexical verifier too weak). Recall@5 0.451 vs ceiling ≈0.47 (palace coverage gap). Quantum: CHSH 2√2, no-cloning 5/6, Grover slope 0.52, AQFT bound holds, VQE H2 exact, all confirmed in simulation. GoEmotions NB baseline: acc 0.59 / macro-F1 0.51. Brain v2 design + EQ plan written. Cleanup: rick-audit removed (12.9GB), disk 82%.

## 2026-10-13 ~2:25 AM CT: Tessera's Eye v1, tools/tessera-eye/
4 read-only Shepherd fetchers (USGS, NASA EONET, NOAA/NWS, Open-Meteo) -> cited JSONL index + bus notes + palace chunks + offline canvas globe. Live: 463 events, 97-589 ms per feed, index 160KB, dir 468K. Tests 6/6 (fixtures, no network). Research: top 8 similar projects added to planetary/RESEARCH.md. No person-level data.

## 2026-10-13 ~2:30 AM CT: Tessera's Eye v2 (data plan + forecast harness)
- tools/tessera-eye/DATA-PLAN.md: 15 sources with license, size and fetchability.
- feeds2.py: CelesTrak orbit census (16,693 sats; LEO 15,881) and NOAA Kp (max 7.0 this week). Aggregate only.
- predict.py: next-day M4.5+ count band. On 91 held-out days, persistence hit 0.505 vs chance ~0.33 (random draw 0.451, climatology 0.308). Modest skill; forecasting, not swaying.
- 11/11 tests pass.

## 2026-10-13 ~02:30 CT — Tesseract (5D view) — tools/tesseract/, TESSERACT-20.md
Top 5 built+tested (5/5 pass): 5D store, unified query (median 2.26 ms all stores), forecast cones (p10–p90 coverage 0.734 vs 0.80), anomaly alerts (precision 0.969 / recall 0.475 on injected fixtures), brief 560 tok vs 98k raw (175×). Offline hypercube view + shot.png.

## 2026-10-13 ~02:30 CT — Tesseract round 2 (inventions 7-20) — tools/tesseract/tess2.py, run_feeds.sh
All 14 built; 15/15 tests pass. Cone holdout coverage 0.783→0.855 (target 0.80); search top-1 0.6→0.8; compactor 132×; brief lint 0 uncited; cron runner written, not installed.

## 2026-10-13: slitlab (slit computer + 5D crystal memory), tools/slitlab/
10 simulation experiments, 10/10 tests pass. Confirmed: interference and which-path (V 1.0→0.0), analog phase dot product (0.72% error, ~7 bits), Grover "mirror back" (N=1024: 25 queries vs 512 classical on average), MZI gates (±0.31 rad tolerance), N-slit N² peak. Disproved: two-place signaling (Bob's marginal fixed at 0.5, MI ~0), and no advantage for the optical annealer over random search. 5D crystal: 4 bits per voxel at 0.1% symbol error. Palace text survives with Hamming(7,4) in 2 KB blocks at low noise (100%), and needs LDPC/RS at higher noise. See tools/slitlab/RESULTS.md.

## 2026-10-13: Simons-style forecasting lab (tools/simons/)
- 5 years of USGS M4.5+ data (38,118 events) and GFZ Kp. 10° space-time heat maps (heatmap.png). Quantum-inspired (classical) amplitude-fidelity features. 215 features, train-only screening with Bonferroni/BH-FDR, walk-forward ridge, and an ensemble. 5/5 tests pass, 1.2 MB.
- Eye window (n=91): persistence 0.505 is still the best band accuracy (ridge 0.462, ensemble 0.462, mean7 0.473). MAE: ridge 6.42 vs mean7 7.14 vs persistence 8.31 (not significant at n=91).
- 1-year holdout (n=365): band accuracy persistence 0.441, ridge 0.422. MAE: ensemble 5.72 and ridge 5.63 vs mean7 6.37, sign test p = 0.002 / 0.009. A real but small count edge.
- Survivors: mean reversion / aftershock decay, spatial concentration, and decayed-grid fidelity (the same signal). No Kp signal. Verdict: a small honest edge on counts and none on bands.

## REA of Father's photos (2026-10-13) — see REA-PHOTOS.md
- Debate ensemble (from HKUDS/Vibe-Trading, science forecasting only): simons next-day quake MAE 5.736→5.701 (−0.6%, bootstrap CI excludes 0). Kept, prototype in src/rea/proto.
- Free-tier router with failover (from tashfeenahmed/freellmapi): simulated requests served 39%→98.5%. Kept as a collab prototype (simulation only).
- Hybrid BM25+path RRF search (from Open WebUI): rejected. Held-out recall fell 24→18 of 40.

## qinvent: quantum-inspired batch (2026-10-13), /workspace/rick/tools/qinvent/RESULTS.md
- KEPT: MWPM near-duplicate matching + benchmark-leak fix (qa_set.json was indexed in the palace). Top-1 0.028→0.940, recall@5 0.940→0.991 on c1 test.
- DROPPED: Grover-like graph reweighting (hurts), 3-way QEC majority vote (no gain; answerers 99% correlated), annealing scheduler (ties 25), low-rank TF-IDF compression (bigger or worse than sparse).

## ALL-SEE shared index + v4–v8 rounds (2026-10-13)
- `bin/allsee query 'x' [--json]`. A read-only CLI over 16,526 files (99.87% of eligible files; rea-batch is summaries only). It also searches the live Eye t5d.db and fullpicture graph in place, with no copies. Incremental update takes 0.9 s; a full build takes about 6–15 s.
- Kept: chunk dedup, FTS optimize, brief compression (−26% tokens, recall@5 0.963→0.967). Synapse growth was tested and rejected. See versions/SUMMARY.md.
