# #14 Thermodynamic η=acc/tokens selector

- **id:** `thermo_eta`
- **focus:** thermo/token
- **verdict:** **KEPT**

## Spec
On DEV, pick config maximizing η=1000·acc/tokens_brief among {raw,valve,fe,dedup,stack}; apply to TEST.

## Target
brief transform choice

## Metric
η (↑), tokens on TEST

## Baseline
raw η 0.266 (2299 tok DEV)

## Measured result
picks stack η 2.803 (×10.5); TEST tokens 782.2, R@5/acc held. Correctly ranks free-energy+dedup.
