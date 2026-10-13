# Simons-style forecasting lab: Tessera's Eye (2026-10-13)
Science forecasting only. No trading, finance, wallets or payments, and no person tracking. The target is the **next-day global USGS M4.5+ count**.
Run it with `python3 fetch.py` (≈1.1 MB of public data), then `python3 simons.py` (≈5 s), then `python3 -m unittest test_simons` (5/5 pass). The folder is 1.2 MB.

## Data
- USGS FDSN M4.5+ catalog, 2021-10-10 → 2026-10-11: 1,828 days, 38,118 events (date, lat, lon, mag). The daily counts match `tessera-eye/data/quake_daily.json` exactly (0 differences).
- GFZ Potsdam daily Kp sum, 2021 → 2026-10-12. The most recent days are mean-filled, because the file lags.
- Not used: the tesseract t5d.db. It holds only derived Eye data, so it would add nothing independent.

## Heat maps (`heatmap.png`)
Events are binned into a grid of 10°×10° cells, 18×36 = 648 of them, for each day. The top panel shows the map of log-intensity over the last 365 days, and the Ring of Fire stands out clearly. The bottom panel is a Hovmöller plot of latitude against day. The PNG writer is pure Python.
**Quantum-inspired (NOT quantum):** each day's normalized grid is turned into an amplitude vector ψ=√p. The features are the interference/fidelity |⟨ψ_t|ψ_{t−k}⟩|² for k = 1, 2, 3, 5, 7 and 14. There are versions on raw counts, on a decayed grid (0.7/day) and on energy, plus one against the expanding climatology. All of it is classical linear algebra.

## Method
- **215 candidate features:** global lags 0–14; rolling mean, std, max and deviation over 3–90 days; EWMAs; energy and max-magnitude lags; recent M5.5/6.0/6.5 counts; the top 20 cells (chosen on the first 60% of days only) and 6 latitude bands; rolling 30-day cross-correlations between regions; Kp lags 0–7 and rolling means; heat-map entropy, concentration and active cells; 19 quantum-inspired fidelities; day-of-week and seasonal terms.
- **Screening, on training rows only:** each feature's rank correlation with the next-day surprise (y − 30-day mean). P-values use Fisher z with an autocorrelation-adjusted effective n (Bartlett). Survivors pass **Bonferroni** (p < 0.05/215) or **BH-FDR at 5%**.
- **Walk-forward:** an expanding window, refit every 7 days, with each forecast using only information known up to day t. There are two models: a ridge on all features and a ridge on the FDR survivors, both log-target with Duan smearing. The **ensemble** is the mean of ridge_all, ridge_survivors, mean30 and mean7.
- **Scoring:** tercile bands come from the training days (window A uses the identical Eye-harness terciles of 17 and 21). I report Wilson 95% CIs, an exact McNemar test against persistence for band accuracy, and a sign test on |error| against mean7 for MAE.

## Results
**A: same held-out window as the Eye (2026-07-13 → 10-11, n=91)**
| model | band acc (95% CI) | MAE |
|---|---|---|
| persistence | **0.505** (0.41–0.61) | 8.31 |
| mean7 | 0.473 | 7.14 |
| mean30 | 0.505 | 7.39 |
| ridge_all | 0.462 | **6.42** |
| ridge_survivors | 0.451 | 6.66 |
| ensemble | 0.462 | 6.65 |
None of the band-accuracy differences are significant (McNemar p ≥ 0.44). In MAE, ridge_all beats mean7 by 10% and persistence by 23%, but the sign test against mean7 gives p = 0.21, so it isn't significant at n=91.

**B: one-year holdout (2025-10-12 → 2026-10-11, n=365, more power)**
| model | band acc | MAE | MAE sign-test vs mean7 |
|---|---|---|---|
| persistence | **0.441** (0.39–0.49) | 7.38 | — |
| mean7 | 0.378 | 6.37 | — |
| ridge_all | 0.422 | **5.63** | **p = 0.009** |
| ridge_survivors | 0.416 | 5.70 | p = 0.14 |
| ensemble | 0.395 | 5.72 | **p = 0.002** |

## Surviving signals
On window A, 44 features survived Bonferroni and 62 survived FDR (41 and 54 on window B). They are all in the same family:
1. **Mean reversion / aftershock decay.** Deviation from the 14–90-day mean has ρ ≈ +0.24 to +0.31, and the long-window mean, max and std are negative. Some of this is built in by measuring surprise against the 30-day mean, so read it as "busy spells relax back toward the norm."
2. **Spatial concentration.** Heat-map entropy, concentration and the active-cell count survive, meaning activity clustered in a few cells (an aftershock zone) tends to fade.
3. **Quantum-inspired decayed-grid fidelity** (lags 1–7, ρ ≈ −0.24, p ~ 1e-15). It survives, but it measures the same thing as #2: how stable the spatial pattern is. It is not new physics.
4. **No Kp feature survived.** Geomagnetic activity carries no detectable next-day earthquake signal here, which is the expected null result.

## Verdict (honest)
- **Band accuracy: no improvement.** Persistence (0.505 on A, 0.441 on B) is still the best band forecaster, and no model beats it significantly.
- **Count accuracy: a small, real edge.** On the one-year holdout the 215-feature ridge and the ensemble cut MAE by ~12% against mean7 (6.37 → 5.6) and by ~24% against persistence, and the sign test passes (p ≤ 0.009). On the 91-day window the edge has the same sign but isn't significant.
- The Simons recipe works the way it should: it found many statistically real but **small** edges, and they all come down to aftershock clustering and mean reversion. The heat-map and quantum-inspired features formalize clustering. They do not predict new earthquakes. I added no further tuning after looking at the test windows (one bias-correction fix, smearing, was applied to both, and the change is in the code history).
