# #5 Cross-hit entropy-zero line dedup

- **id:** `dedup_lines`
- **focus:** token
- **verdict:** **KEPT**

## Spec
Normalize lines to token-sets; drop repeats across the 5-hit brief (zero new information).

## Target
valve briefs

## Metric
tokens_brief (↓)

## Baseline
valve 1725.3

## Measured result
tokens 1088.4 (−37% vs valve). Stack #2+#5: 782.2 (−66% vs raw).
