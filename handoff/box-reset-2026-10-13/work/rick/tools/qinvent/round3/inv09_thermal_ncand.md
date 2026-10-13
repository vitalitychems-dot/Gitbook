# #9 Thermal-aware ncand under contention

- **id:** `thermal_ncand`
- **focus:** hardware/thermo
- **verdict:** **KEPT**

## Spec
If load1 > 0.75·ncpu (or under N-way parallel searchers), cut ncand 30→15. Accuracy verified equal on TEST.

## Target
allsee under parallel load

## Metric
wall_max (↓) with recall5 held

## Baseline
8 workers ncand30 wall_max 7.16s; recall5 0.9674

## Measured result
ncand15 wall_max 6.30s (−12%); recall5/acc unchanged. Solo gain <5% so gate is contention.
