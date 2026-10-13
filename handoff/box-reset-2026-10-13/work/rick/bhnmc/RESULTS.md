# BHNMC v1.3 vs v1.4 — RESULTS (SIMULATION ONLY, 2026-10-12. No biology was measured.)
Files: engine.py (v1.3 port with fixes), sim_v14.py, mlcore.py, geometry.py, and the raw outputs in v13_output.txt, v14_output.txt, v14_results.json and geometry_output.txt.
Re-run: `OMP_NUM_THREADS=1 python3 sim_v14.py` (about 10 s; without the thread cap, BLAS contention made it run for more than 10 minutes on this box).
Deviation: sklearn could not be installed because the disk was full. Ridge is reimplemented in numpy with the same closed form. SVC(precomputed RBF) is **replaced by RBF kernel-ridge**, so "rbf" numbers are not literally SVC.

## v1.3 as written (seed 42, 80/20 unshuffled)
Ridge 1.000, RBF 1.000, QI-Ridge 1.000 (n_test = 20). Bug fixed: `dna_sequence_string` is now stored in the manifest.

## v1.4 measurements (10 seeds, stratified shuffled 5-fold CV, mean ± std over seeds)
|Test|Result|
|-|-|
|v1.3 task, state carried over (leak)|1.000±0.000|
|v1.3 task, state reset per trial|1.000±0.000|
|v1.3 task, **no reservoir** (raw input)|1.000±0.000 → the v1.3 task cannot show any reservoir benefit|
|Hard task (all 64 channels mixed, classes differ only in frequency 0.30/0.36/0.42, noise 0.3), reservoir: CV ridge / RBF|0.476±0.021 / 0.673±0.058|
|Same, + 4-frequency impedance features: CV ridge / RBF|0.501±0.038 / 0.655±0.076|
|Same, no reservoir: CV ridge / RBF|0.419±0.031 / 0.567±0.037|
|**Held-out amplitude/phase families**: reservoir ridge / RBF|0.257±0.039 / 0.187±0.036 (chance = 0.333)|
|Held-out, multi-frequency: ridge / RBF|0.281±0.035 / 0.150±0.032|
|Held-out, no reservoir: ridge / RBF|0.261±0.033 / 0.248±0.026|
|QI using the first 64 of 192 features (held-out)|0.324±0.055|
|QI using all 192 features (held-out)|0.340±0.054|
|Memory capacity at ρ = 0.8 / 0.95 / 1.15|2.34±0.27 / 2.78±0.33 / 3.17±0.44 (max 40)|
|NARMA-10 NMSE at ρ = 0.8 / 0.95 / 1.15|0.591±0.034 / 0.580±0.032 / 0.567±0.035|
|NARMA-10 NMSE, no reservoir (input only)|1.033±0.022 (3 seeds only)|

Reading the results:
- The reservoir adds about 6–11 accuracy points in within-distribution CV.
- It helps NARMA a lot (NMSE 0.57 vs 1.03).
- **Nothing generalizes to held-out stimulus families**: every model is at or below chance. The v1.3 features (final R, ΔR, var X) encode amplitude and phase rather than frequency.
- The QI branch does not beat ridge or RBF. It has not earned its place.
- Multi-frequency features gave a small, within-noise change (the Cole dispersion model is assumed, not measured).

## Audit / design issues
1. The v1.3 classes drive disjoint channel blocks, so the task is trivially separable (the no-reservoir baseline scores 1.000).
2. The 80/20 split is unshuffled, giving n_test = 20 and a single seed with no variance estimate.
3. There is no held-out stimulus test. The twin requirement (unseen stimuli) is not met.
4. QI uses only F[:, :64], the final-R block. Using all 192 changed the result by +0.016, which is within noise.
5. Reservoir state carries over between trials, which leaks information. It made no measured difference here because of the ceiling, but it is still a bug.
6. There is no f dimension in X(t, f, e), even though the spec claims it.
7. ρ = 1.15 > 1 is outside the usual echo-state regime. It measured slightly better here, but this needs an echo-state-property check.
8. Memory capacity is only about 3 out of 40: short memory with leak 0.2 and this input scaling.
9. **Geometry:** fluid ports at r = 22 sit inside the O-ring groove (21–23), right on the seal. The 4 corner electrodes (E01, E08, E57, E64) at r = 22.27 cross the O-ring inner radius of 21. Diagonal coils M1/3/5/7 are at r = 25.46, which is outside a 50 mm board's inscribed radius of 25 and outside the seal, while M2/4/6/8 are at r = 20, inside it. That is inconsistent. Diagonal coil centers are only 3.18 mm from the corner electrodes. The Z stack is 12.5, which is correct.
10. **MUX:** 4 × 16 = 64 is correct. "Dual ADG706" is wrong: the ADG706 is a single 16:1, and 2 of them give only 32 channels. The 16 address pins could shrink to 4 shared address + 4 enable = 8.
11. The engine used `default` RNG for both the noise and the weights, so runs are not independent per seed. v1.4 seeds each separately.

## Improvements (name — one runnable step — test — measured effect)
1. **reset-per-trial**: set `p.state = 0` at the start of every trial. Test: carried-over vs reset accuracy on a non-ceiling task. Effect: unmeasured (the v1.3 task is at ceiling, 1.000 in both).
2. **no-reservoir gate**: always score raw-input features with the same readout. Test: reservoir minus baseline > 2σ. Effect: +0.057 ridge and +0.106 RBF (CV, hard task). Held-out: no gain.
3. **held-out families**: train on 4 amplitude/phase families and test on 2 unseen ones. Test: acc > 0.333 + 2σ. Effect: exposed generalization failure, 0.187–0.281 against 1.000 in v1.3.
4. **frequency-invariant readout features**: add per-channel FFT power / zero-crossing rate of the R history. Test: held-out acc > 0.5. Effect: unmeasured (next step).
5. **multi-freq impedance f-axis**: 4 frequencies, Cole model. Test: CV ridge improvement. Effect: +0.025 ridge (within 1σ), −0.018 RBF. Not significant.
6. **QI full-feature + matched random-feature control**: Test: QI > RBF. Effect: 0.340 vs 0.324. QI loses to the CV RBF and is not justified.
7. **ρ sweep with MC/NARMA**: Effect: MC 2.34 → 3.17 and NMSE 0.591 → 0.567 as ρ goes 0.8 → 1.15.
8. **thread cap**: set OMP_NUM_THREADS=1. Effect: the run took about 10 s versus more than 600 s without it (killed) on a loaded 8-core box (load 10).
9. **geometry fix**: move ports to r ≤ 19 (e.g. ±19, 0, inside the seal with a channel), move the O-ring to r = 23.5–25 or shrink the pitch to 4.0 (max r = 19.8), and put all coils on a single radius. Test: geometry.py shows 0 electrodes and 0 ports touching the seal. Effect: unmeasured.
10. **MUX BOM fix**: use 4× ADG706 (or ADG1206) with shared address lines. Test: pin count 46 → 38. Effect: unmeasured.
