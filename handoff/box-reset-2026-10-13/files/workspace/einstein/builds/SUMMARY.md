# Einstein builds - TESSERA commit 0236c802, 2026-10-13 03:36 CDT
Rule: KEEP only if the paired 95% bootstrap CI of the gain excludes 0 (toolkit/vtk.py bench).
## builds/01_llr_consensus/
- 01 LLR consensus vs phi/2-3 (current): decision accuracy baseline 0.7924 [0.7765,0.8076] -> candidate 0.9816 [0.9772,0.9856]; gain 0.1892 [0.1769,0.2016] (n=30) => KEEP
- 01 LLR consensus vs phi weights at 1/2 (stronger baseline): decision accuracy baseline 0.9649 [0.9586,0.9706] -> candidate 0.9816 [0.9772,0.9856]; gain 0.01665 [0.01382,0.01975] (n=30) => KEEP
## builds/02_echo_decoder/
- 02 echo-cluster decoder vs current phi/2-3: decision accuracy baseline 0.7844 [0.7675,0.8019] -> candidate 0.8757 [0.8624,0.8889]; gain 0.09128 [0.07473,0.1086] (n=30) => KEEP
- 02 echo-cluster decoder vs independent LLR (build 01): decision accuracy baseline 0.8657 [0.8502,0.8809] -> candidate 0.8757 [0.8624,0.8889]; gain 0.00995 [-0.005635,0.02543] (n=30) => DROP
## builds/03_sprt_council/
- 03 SPRT early stop: calls per decision: LLM calls/decision baseline 24 [24,24] -> candidate 11.78 [10.92,12.62]; gain 12.22 [11.38,13.08] (n=20) => KEEP
- 03 SPRT accuracy vs current full poll phi/2-3: decision accuracy baseline 0.7948 [0.7758,0.8137] -> candidate 0.9802 [0.9761,0.9837]; gain 0.1853 [0.1687,0.2013] (n=20) => KEEP
- 03 SPRT accuracy vs full-poll LLR (build 01): decision accuracy baseline 0.9839 [0.9796,0.9877] -> candidate 0.9802 [0.9761,0.9837]; gain -0.00375 [-0.0053,-0.002449] (n=20) => DROP
## builds/04_signed_hash_embed/
- 04 fallback embed: cosine error vs exact bag: mean |cos err| baseline 0.1402 [0.1383,0.1423] -> candidate 0.05933 [0.05799,0.06063]; gain 0.08088 [0.07853,0.08344] (n=20) => KEEP
- 04 fallback embed: top-1 snippet retrieval: top-1 hit rate baseline 0.1762 [0.1648,0.189] -> candidate 0.6773 [0.659,0.6935]; gain 0.501 [0.4842,0.5178] (n=20) => KEEP
## builds/05_qubo_diverse_retrieval/
- 05 QUBO-anneal diverse top-5 vs current top-5: subtopics covered /3 baseline 2.047 [1.98,2.107] -> candidate 2.62 [2.54,2.69]; gain 0.5733 [0.5,0.65] (n=12) => KEEP
- 05 QUBO-anneal vs greedy MMR (non-quantum control): subtopics covered /3 baseline 2.6 [2.533,2.667] -> candidate 2.62 [2.54,2.69]; gain 0.02 [-0.07667,0.1167] (n=12) => DROP
## builds/06_anneal_lesson_clusters/
- 06 Potts-anneal lesson clustering vs distillLessons: pairwise F1 baseline 0.4211 [0.3441,0.5063] -> candidate 0.8135 [0.781,0.8445]; gain 0.3924 [0.3072,0.4773] (n=15) => KEEP
- 06 Potts-anneal vs single-link at same tau (non-quantum control): pairwise F1 baseline 0.5603 [0.4951,0.6236] -> candidate 0.8135 [0.781,0.8445]; gain 0.2532 [0.1864,0.3207] (n=15) => KEEP
## builds/07_temporal_repetition_alerts/
- 07 2-of-3 rounds + hysteresis vs single snapshot: false opens/day baseline 69.17 [66.47,71.93] -> candidate 26.03 [24.73,27.33]; gain 43.13 [41.07,45.27] (n=30) => KEEP
- 07 missed incidents (of 6): missed incidents/day baseline 0.1333 [0,0.4] -> candidate 0.2333 [0.06667,0.4333]; gain -0.1 [-0.2667,0.06667] (n=30) => DROP
- 07 detection delay: ticks (30 s) to open baseline 0.2944 [0.02778,0.7501] -> candidate 1.743 [1.163,2.481]; gain -1.448 [-2.122,-0.96] (n=30) => DROP
## builds/08_lowrank_vector_store/
- 08 rank-64 int8 store vs JSON float: bytes/vector (excl. basis) baseline 5508 [5508,5509] -> candidate 68 [68,68]; gain 5440 [5440,5441] (n=10) => KEEP
- 08 recall@10 of compressed search: recall@10 baseline 1 [1,1] -> candidate 0.6674 [0.6607,0.676]; gain -0.3326 [-0.3393,-0.324] (n=10) => DROP (recall < 0.95)
## builds/09_anneal_budget_fit/
- 09 anneal max-coverage vs fitBudget head/tail: needle paragraphs kept baseline 0.6034 [0.5746,0.6294] -> candidate 0.8401 [0.8101,0.8717]; gain 0.2367 [0.2034,0.2696] (n=10) => KEEP
- 09 anneal vs greedy coverage (non-quantum control): needle paragraphs kept baseline 0.8401 [0.8101,0.8717] -> candidate 0.8401 [0.8101,0.8717]; gain 0 [0,0] (n=10) => DROP
## builds/10_parity_snapshots/
- 10 parity k=4 vs full snapshots: snapshot bytes baseline 4.656e+05 [4.656e+05,4.656e+05] -> candidate 2.363e+05 [2.363e+05,2.363e+05]; gain 2.292e+05 [2.292e+05,2.292e+05] (n=5) => KEEP
- 10 restorable at q=0.01: P(all restorable) baseline 1 [1,1] -> candidate 0.9968 [0.9966,0.997]; gain -0.003225 [-0.003445,-0.00296] (n=10) => DROP
- 10 restorable at q=0.05: P(all restorable) baseline 1 [1,1] -> candidate 0.9193 [0.9186,0.9201]; gain -0.08066 [-0.08141,-0.07994] (n=10) => DROP
