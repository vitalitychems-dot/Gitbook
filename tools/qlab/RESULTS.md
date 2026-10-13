# Rick's Quantum Lab (qlab) — results, 2026-10-12 (CT)

> **SIMULATION ONLY.** Every number in this file comes from classical simulation on a CPU (statevector or density-matrix). None is a measurement on quantum hardware. Device names refer to public calibration snapshots that were used as model inputs.

All numbers measured on the shared box (8 cores, OMP_NUM_THREADS=1, numpy 2.5.3). Simulated only.

## Run
```
cd /workspace/rick/qlab
OMP_NUM_THREADS=1 python3 test_sim.py    # step 1 (~2 s)
OMP_NUM_THREADS=1 python3 test_opt.py    # step 2 (~10 s)
OMP_NUM_THREADS=1 python3 test_noise.py  # step 3 (~1 s)
python3 test_geom.py                     # step 4
```
Files: qsim.py (statevector), qopt.py (peephole optimizer), qnoise.py (density matrix), geomcheck.py (geometry lib), test_*.py, *_results.json.

## 1. Statevector simulator [SIMULATION]
| Test | Result | Measured |
|-|-|-|
| Bell 50/50 + correlation | PASS | P00=0.5005, P11=0.4995, P(equal bits)=1.0000 (1e5 shots, seed 1) |
| GHZ n=3..20 | PASS | max error 2.2e-16 |
| Unitarity n=4 (20 random circuits) / norm n=16, 2000 gates | PASS | max abs(U†U−I)=1.6e-15; norm error 1.5e-14 |
| QFT == numpy FFT n=2..10 | PASS | max error 2.3e-16 |
| Grover n=4..10 vs sin²((2k+1)θ) | PASS | max error 8.8e-14 (e.g. n=4 P=0.961319, n=10 P=0.999461) |
| Deutsch-Jozsa n=6 | PASS | constant P(0…0)=1.000000, balanced 3e-135 |
| CHSH | PASS | S=2.8284271247 (=2√2); classical brute-force max=2 |
| Hadamard test Re/Im | PASS | max error 8.9e-16 over 9 phases |

Caveat: the Grover oracle/diffuser and the DJ oracle act directly on the statevector, not through gate decompositions. A gate-level Grover n=3 (in test_opt) gives P=0.945312 = sin²(5θ).

Performance (H on every qubit plus a CNOT ring, 2n gates):
| n | wall s | ms/gate | peak traced MB | state MB |
|-|-|-|-|-|
| 10 | 0.0025 | 0.12 | 0.05 | 0.016 |
| 14 | 0.0042 | 0.15 | 0.75 | 0.25 |
| 16 | 0.010 | 0.32 | 3.0 | 1 |
| 18 | 0.046 | 1.28 | 12.0 | 4 |
| 20 | 0.465 | 11.6 | 48.0 | 16 |

## 2. Peephole optimizer [SIMULATION]
Passes: cancel self-inverse pairs (H, X, Y, Z, CNOT, CZ, SWAP) and S/S†, T/T†; merge rotations; merge Z/S/T/P phases; drop identity rotations; commute-through (diagonal–diagonal, diagonal on CNOT control, X/RX on CNOT target, disjoint qubits).
| Test | Result | Measured |
|-|-|-|
| 200 random circuits (n=2..6, 30% injected repeats), fidelity > 1−1e-9 | PASS | min fidelity 1.000000000000 |
| gate reduction on the same set | — | 46.9 ± 8.9 %; depth reduction 47.7 ± 12.8 % |
| 200 uniform random circuits (no injected repeats) | PASS | min fidelity 1.0; gate reduction 17.2 ± 7.2 % |
| QFT5 | no gain | 17 → 17 gates |
| QFT5 · QFT5⁻¹ | PASS | 34 → 0 gates, fidelity 1.0 |
| Grover n=3 (textbook decomposition) | no gain | 51 → 51 gates, depth 29 → 29 |

## 3. Noise (density matrix) [SIMULATION]
| Test | Result | Measured |
|-|-|-|
| Global depolarizing F=(1−p)^k+(1−(1−p)^k)/d, p=0.02, k=1..40 | PASS | max error 3.4e-15 (k=40: F=0.51499) |
| Local 1-qubit depolarizing, Bloch shrink (1−4p/3)^k | PASS | max error 5.6e-15 |
| Amplitude damping P1=(1−γ)^k | PASS | max error 5.6e-16 |
| Optimizer → fidelity (30 circuits, n=4, p=0.005, γ=0.002) | PASS | F 0.8148±0.0166 → 0.9001±0.0207 (+0.0854); improved 30/30; gates −48.7 % |

## 4. Geometry checker (geomcheck.py) on bhnmc/geometry.py [SIMULATION]
| Known issue | Result | Measured |
|-|-|-|
| Corner electrodes on the O-ring (21–23 mm) | PASS | E01, E08, E57, E64 (r=22.27) |
| Fluid ports on the seal | PASS | inlet and outlet at r=22 |
| 4 coils off the board | PASS* | M1, M3, M5, M7 (r=25.46 > 25) |
| Dual 16:1 mux covers 32/64 | PASS | 32; 4×16:1 → 64 |
| Coil–electrode min centre distance | PASS | 3.18 mm (M1–E01) |
*Treats the board as a 50 mm circle and uses coil centres only. The 46→38 pin-count claim is NOT reproduced here (no pin model yet).

## 5. Noise-aware rewriting optimizer v2 (qopt2.py + qnoise2.py), 2026-10-12 (CT) [SIMULATION]
Run: `OMP_NUM_THREADS=1 python3 test_opt2.py` (15.5 s). Results are written to opt2_results.json.
Native basis: U3, CNOT, CZ. Lowering: CP→2 CNOT, SWAP→3 CNOT, CCZ→old (3 CP + 2 CNOT = 8 CNOT) or the standard 6-CNOT/7-T form.
Passes: v1 peephole, 1q-run fusion (ZYZ→U3), H·CZ·H↔CNOT templates, CNOT cancellation through commuting gates (shared control/target, Z-type on control, X on target).
Acceptance rule: a pass is kept only if noisy fidelity rises by more than 1e-6. Noise: p1=1e-3 and p2=1e-2 depolarizing per qubit, γ=1e-3 amplitude damping per touched qubit.
Sanity checks: the fast DM matches the v1 reference DM to 1.0e-15; ZYZ on 500 random U has max infidelity 8.9e-16.

| Set | exact (min F) | gates raw→v1→v2 | depth raw→v1→v2 | 2q raw→v1→v2 | noisy F raw→v1→v2 |
|-|-|-|-|-|-|
| 200 random (n=2..6) | 1.000000000000 PASS | 45.7±15.1→31.5±13.4→21.7±10.8 | 27.1±12.1→18.8±10.0→14.5±8.2 | 16.6±8.1→11.65±7.0→11.62±7.0 | 0.7587±0.0990→0.8225±0.0939→0.8310±0.0931 |
| QFT n=3..8 | 1.0 PASS (all) | v2 = v1 (e.g. n=8: 160→139→139) | n=8: 56→50→50 | unchanged (n=8: 68) | n=8: 0.3832→0.3878→0.3878 |
| Grover n=3, old CCZ | 1.0 PASS | 99→99→75 | 66→66→57 | 32→32→32 | 0.5477→0.5477→0.5608 |
| Grover n=3, 6-CNOT CCZ | 1.0 PASS | 83→83→63 | 49→49→45 | 24→24→24 | 0.6292→0.6292→0.6419 |
| Grover n=4 | 1.0 PASS | 352→352→226 | 295→295→205 | 204→204→132 | 0.0860→0.0860→0.1466 |
| Grover n=5 | 1.0 PASS | 1125→1125→669 | 1025→1025→633 | 784→784→416 | 0.0300→0.0300→0.0320 |

Notes:
- Accepted passes: fusion 201/201 on random circuits, plus cxcomm 3/3. The H·CZ·H template found no matches on any circuit. Fusion was rejected on every QFT circuit because fidelity didn't rise.
- QFT does not shrink beyond v1. Its CNOTs are interleaved with phase gates that this pass set can't remove.
- In Grover n=4/5, the multi-controlled Z is a naive phase-polynomial (parity-network) construction. Most of the 2-qubit cut there comes from cancelling that construction's redundant CNOTs, so it overstates the gain against a good MCZ.
- The 6-CNOT CCZ vs the old 8-CNOT lowering is the real CCZ win on Grover n=3: 32→24 2-qubit gates, and F 0.5608→0.6419 after v2.
- Grover n=5 fidelity (0.03) is at the fully-mixed floor (1/32=0.031) in every version, so its fidelity change says nothing.

## 6. Phase-polynomial rewriter v3 (qopt3.py), 2026-10-12 (CT) [SIMULATION]
Run: `OMP_NUM_THREADS=1 python3 test_opt3.py` (33.6 s). Results are written to opt3_results.json.
Method: gather maximal CNOT/CZ/CP/P/RZ/T/S/Z regions (gates on blocked qubits are deferred, which is order-safe). Represent each region as phase terms {parity mask: angle} plus a GF(2) linear map. Resynthesize with a greedy parity network (distance heuristic, with an exact fallback), then a Gauss-Jordan CNOT fix-up of the linear map. Replace a region only if it has fewer 2q gates; keep the whole pass only if noisy fidelity rises (same noise as v2). Note: the network is greedy and heuristic, not exact GraySynth.
Fair Grover baseline: an ancilla-free Gray-code MCZ (2^n−2 CNOTs: n=3: 6, n=4: 14, n=5: 30), exact to fidelity 1.000000000000.

| Set | exact v1/v2/v3 | gates v1→v2→v3 | depth | 2q | noisy F |
|-|-|-|-|-|-|
| 200 random | 1.0/1.0/1.0 PASS | 31.48±13.37→21.68±10.79→20.58±10.45 | 18.78±10.02→14.47±8.18→13.45±7.51 | 11.65±7.00→11.62±6.97→10.56±6.57 | 0.8225±0.0939→0.8310±0.0931→0.8439±0.0893 |
| QFT n=3..8 | PASS | no change (n=8: 139/139/139) | n=8: 50 | n=8: 68 | n=8: 0.3878 all |
| Grover n=3 | PASS | 83→59→59 | 61→49→49 | 24→24→24 | 0.6276→0.6433→0.6433 |
| Grover n=4 | PASS | 232→190→190 | 187→169→169 | 84→84→84 | 0.2410→0.2492→0.2492 |
| Grover n=5 | PASS | 581→517→517 | 505→481→481 | 240→240→240 | 0.0454→0.0462→0.0462 |

Pass log, v3 stage on random circuits: phasepoly tried 228, accepted 68 (fidelity gate); fusion re-run accepted 50/67.
Honest nulls: QFT does not shrink in v3 either. Its regions are a single CP per H-separated block, and the per-region rewrite found nothing cheaper. Grover with the fair Gray-code MCZ gets no extra 2q cut from v3, because that MCZ is already an optimal-size parity network.
With the fair baseline, the earlier v2 Grover n=4/5 2q cuts (204→132, 784→416) disappear. The fair baseline itself is far cheaper: n=4 has 84 2q gates vs 132 for v2-on-naive, and n=5 has 240 vs 416.

## 7. Approximate QFT (aqft.py), 2026-10-12 (CT) [SIMULATION]
Run: `OMP_NUM_THREADS=1 python3 test_aqft.py` (484 s; aqft_results.json) and `python3 test_aqft_avg.py` (20 s; aqft_avg_results.json).
Rule: drop CP with angle < 2π/2^m. Ideal F is the mean over 8 random basis inputs of |⟨QFT x|AQFT x⟩|². Noise is the same as v2/v3 (p1=1e-3, p2=1e-2, γ=1e-3); circuits are lowered to CNOT (no further optimization). Noisy F compares against the exact QFT output.

Best m by noisy fidelity:
| n | log2n+2 | best m, single input | best m, 4-input mean | noisy F best (4-input) vs exact m=n | ideal F at best | 2q best/exact |
|-|-|-|-|-|-|-|
| 3 | 3.58 | 3 | 3 | 0.8676 vs 0.8676 | 1.000000 | 9/9 |
| 4 | 4.00 | 4 | 3 | 0.7609 vs 0.7578 | 0.990485 | 16/18 |
| 5 | 4.32 | 1 (artifact*) | 3 | 0.7012 vs 0.6686 | 0.959550 | 20/26 |
| 6 | 4.58 | 3 | 3 | 0.6301 vs 0.5580 | 0.906327 | 27/39 |
| 7 | 4.81 | 4 | 4 | 0.5352 vs 0.4597 | 0.971404 | 39/51 |
| 8 | 5.00 | 4 | 4 | 0.4603 vs 0.3581 | 0.959902 | 48/68 |
| 9 | 5.17 | 4 | 3 (corrected) | 0.4341±0.0971 vs 0.2871±0.0085 | 0.696714 | 42/84 |
| 10 | 5.32 | 3 | 4 (corrected) | 0.3522±0.0043 vs 0.2060±0.0028 | 0.949404 | 63/105 |
*The single-input run used one input on which m=1 happens to be nearly exact (mean ideal F at m=1 is 0.35, worst 0.000027). The 4-input average fixes this. n=9 and n=10 were redone with 4 inputs (see 7b).
Full sweep tables (all m, gates, 2q, ideal min) are in aqft_results.json and the test output.

Phase estimation (t counting qubits plus 1 eigen ancilla, 10 random φ, P(correct) = probability of measuring round(φ·2^t)):
| t | exact ideal / noisy | best-m (m) ideal / noisy | m=2 ideal / noisy |
|-|-|-|-|
| 3 | 0.617 / 0.487 | (3) same | 0.585 / 0.476 |
| 4 | 0.832 / 0.545 | (4) same | 0.742 / 0.533 |
| 5 | 0.799 / 0.446 | (1, artifact; superseded by 7b: m=3) 0.143 / 0.114 | 0.575 / 0.388 |
| 6 | 0.868 / 0.380 | (3) 0.792 / 0.415 | 0.498 / 0.303 |
| 7 | 0.635 / 0.230 | (4) 0.618 / 0.264 | 0.255 / 0.150 |
| 8 | 0.729 / 0.195 | (4) 0.699 / 0.249 | 0.305 / 0.158 |
| 9 | 0.666 / 0.139 | (4) 0.639 / 0.201 | 0.256 / 0.125 |
Std across φ is about 0.13–0.19 ideal and 0.03–0.13 noisy (see output); a 10-φ sample is small.
Verdict on m ≈ log2(n)+2: the 4-input best m (3,3,3,3,4,4,3,4 for n=3..10) sits 0.6–1.6 below log2(n)+2 (rounded: 4,4,4,5,5,5). It tracks the growth trend but is about 1 lower at these noise levels. More noise should push it lower still.

### 7b. Cleanup rerun, 2026-10-12 (CT) — `OMP_NUM_THREADS=1 python3 test_aqft_fix.py` (327 s; aqft_fix_results.json) [SIMULATION]
- Phase estimation t=5, 10 fresh random φ (seed 55), m=3 vs exact on the same φ. Ideal P(correct): exact 0.7860±0.1656, m=3 0.7488±0.1729. Noisy: exact 0.4403±0.0888, m=3 0.4581±0.1028. m=3 wins under noise by 0.018, which is well inside the spread across φ.
- n=9 and n=10, noisy F averaged over 4 random basis inputs (seed 11). Swept m=2..8 plus 9 for n=9, and m=2..7 plus 10 for n=10; m=1 and m=8,9 at n=10 were skipped to fit the time budget (they lost clearly in the single-input sweep).
  - n=9: m2 0.3202±0.1777, m3 0.4341±0.0971, m4 0.4218±0.0257, m5 0.3778, m6 0.3391, m7 0.3120, m8 0.2952, exact 0.2871±0.0085. Best m=3, but m=4 is within error and much less input-dependent.
  - n=10: m2 0.1189, m3 0.3303±0.0155, m4 0.3522±0.0043, m5 0.3117, m6 0.2729, m7 0.2437, exact 0.2060±0.0028. Best m=4 (the single-input pick was m=3).
- Corrected best m for n=3..10: 3,3,3,3,4,4,3(≈4),4. log2(n)+2 is 3.6–5.3, so the best m runs about 1 below it.

## 8. Calibrated noise twin + CLI package (qlab/), 2026-10-13 (CT) [SIMULATION]
Data source (free, keyless; fetched 2026-10-13 01:07 CT; Apache-2.0):
https://raw.githubusercontent.com/Qiskit/qiskit-ibm-runtime/main/qiskit_ibm_runtime/fake_provider/backends/{manila,nairobi,guadalupe}/props_{name}.json
Snapshots: ibmq_manila 2024-05-27 (5q, 4 couplers), ibm_nairobi 2024-05-27 (7q, 6), ibmq_guadalupe 2021-04-20 (16q, 16).
Medians — manila: T1 144.7 us, T2 54.4 us, sx 3.54e-4, cx 1.01e-2, readout 0.022. nairobi: 87.3, 106.1, 3.96e-4, 7.80e-3, 0.022. guadalupe: 71.9, 88.3, 3.06e-4, 1.01e-2, 0.016.
Twin: per-gate thermal relaxation (T1, then T2 via phase damping, with T2 clamped to ≤2T1). Idle relaxation for every qubit over each ASAP layer's duration. Depolarizing sized to (calibrated error − thermal infidelity). Readout confusion from prob_meas1_prep0/prob_meas0_prep1. Greedy SWAP routing on the coupling map (SWAP = 3 CX).

| Test (qlab/selftest_twin.py) | Result | Measured |
|-|-|-|
| T1 decay P1=exp(−t/T1), t=5..200 us | PASS | max err 4.4e-16 |
| Ramsey P0=(1+exp(−t/T2))/2 (zero-length pulses) | PASS | max err 4.4e-16 |
| Readout confusion | PASS | P(0\|1)=0.0300 for injected 0.03 |
| RB injected-error recovery, e=1e-4, 5e-4, 2e-3 (tol 5%) | PASS | fit 1.000e-4, 5.000e-4, 2.000e-3 (0.00%; pure-depolarizing case, so exact by construction) |
| RB on thermal device recovers calibrated U3 error 7.0e-4 (tol 10%) | PASS | fit 7.023e-4 (0.3%) |
| Noiseless routed exact QFT5 with permutation tracking | sanity | F=0.99999999994 (9 swaps) |

Layout and AQFT m per device (n=5, AQFT_m vs EXACT QFT reference, mean of 4 basis inputs, twin incl. idle relaxation, no readout). Naive = BFS-from-qubit-0 subset in index order; best = ESP-ranked candidates, top 3 by twin:
| Device | m=2 naive→best | m=3 | m=4 | m=5 (exact) | best m | best combo vs naive exact QFT |
|-|-|-|-|-|-|-|
| manila | 0.3887→0.4136 | 0.5342→0.5403 | 0.5299→0.5514 | 0.4731→0.4982 | 4 | 0.5514 vs 0.4731 (+0.078) |
| nairobi | 0.3610→0.4456 | 0.3863→0.5181 | 0.3136→0.5878 (swaps 10→4) | 0.2766→0.3780 | 4 | 0.5878 vs 0.2766 (+0.311) |
| guadalupe | 0.3775→0.4594 | 0.4328→0.4971 | 0.3421→0.5657 (swaps 11→4) | 0.2968→0.5063 | 4 | 0.5657 vs 0.2968 (+0.269) |
Layout gain alone ranges from +0.006 to +0.274; it is largest on nairobi and guadalupe, where the naive subset forces many SWAPs. On a 5-qubit line (manila) there is little layout freedom.

CLI (`python3 -m qlab optimize`, predicted from |0…0>):
- examples/small3.json on manila: gates 9→4, 2q 4→2, twin F 0.9200 (naive) → 0.9788 (layout [2,4,3], swaps 1→0).
- examples/aqft5.json on nairobi: gates 56→51, 2q 24→24, twin F 0.4118 → 0.7167 (swaps 10→4).
`python3 -m qlab test` runs all 8 test scripts: ALL PASS in about 80 s. The PR plan is in PR-PLAN.md.
