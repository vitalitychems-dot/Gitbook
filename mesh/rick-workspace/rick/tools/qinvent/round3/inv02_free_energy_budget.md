# #2 Free-energy / entropy sentence budget

- **id:** `free_energy_budget`
- **focus:** token/thermo
- **verdict:** **KEPT**

## Spec
Keep sentence s iff marginal query-term info (idf-weighted coverage + numeric bonus) > T·√tokens(s). T tuned on DEV.

## Target
valve-filtered briefs

## Metric
tokens_brief (↓), recall5 & acc held

## Baseline
valve tokens 1725.3

## Measured result
T=1.5 → tokens 1324.0 (−23% vs valve, −43% vs raw); R@5/acc held. Stack with #5 → 782.2 (−66% vs raw).
