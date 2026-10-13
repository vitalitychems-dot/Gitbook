# #4 Simulated-annealing context prune

- **id:** `anneal_prune`
- **focus:** token
- **verdict:** **DROPPED**

## Spec
SA over sentence subset maximizing idf-coverage − λ·tokens (300 iters).

## Target
valve briefs

## Metric
tokens vs #2 with acc held

## Baseline
valve 1725; free-energy 1324

## Measured result
DEV only λ=0 keeps acc (tokens 1207); λ>0 collapses acc. TEST λ=0 → 1657, worse than free-energy. Dropped.
