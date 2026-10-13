# #3 Landauer bit-budget / score-gap adaptive k

- **id:** `landauer_adaptive_k`
- **focus:** token/thermo
- **verdict:** **DROPPED**

## Spec
Cap hits by cumulative softmax self-information (bits) or shrink k when top-1 score gap is large.

## Target
allsee top-k

## Metric
tokens_brief (↓) with R@5/acc held on DEV

## Baseline
k=5 valve tokens 1725

## Measured result
Bit-budget B≤10 and gap-k thr≤0.5 all either cut DEV recall or matched valve tokens (noop on TEST). No measurable win.
