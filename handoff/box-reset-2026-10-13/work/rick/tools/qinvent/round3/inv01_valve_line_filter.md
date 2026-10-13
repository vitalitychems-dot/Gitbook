# #1 Tesla valvular one-way line filter

- **id:** `valve_line_filter`
- **focus:** token
- **verdict:** **KEPT**

## Spec
Keep only brief lines whose tokens intersect the query (one-way: non-matching lines never flow into the brief).

## Target
allsee brief bodies on c1 qa_set

## Metric
tokens_brief (↓), recall5 & acc held

## Baseline
tokens 2326.2, R@5 0.9674, acc 0.1953

## Measured result
tokens 1725.3 (−26%), R@5 0.9674, acc 0.1953
