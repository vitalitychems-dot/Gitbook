# Own-brain Phase 1 result — 2026-10-09

**Status:** TESTED / local evidence recorded  
**Implementation:** `TESSERA/research/own-brain`  
**Scope:** original deterministic sparse LIF simulator; local-only; no API; no product-memory writes; no consciousness claim.

## Tests

```text
python3 -m unittest -v test_lif.py
Ran 6 tests
OK
```

The tests cover exact seeded replay, threshold spike/reset, refractory suppression, invalid input shape, invalid configuration, and equivalence between the object-based reference path and the packed scale path.

## Memory-safe scale ladder

The scale runner now uses packed CSR-like arrays for sources and weights. The default guard is 512 MiB and fails closed before allocation when the conservative peak estimate exceeds that budget. A larger run requires an explicit local budget; no guard is silently bypassed.

| Rung | Synapses | Default 512 MiB | Explicit 1 GiB run | Peak RSS in 1 GiB run |
|---|---:|---|---|---:|
| S0 | 10,000 | TESTED | TESTED | 19,124,224 B |
| S1 | 100,000 | TESTED | TESTED | 28,278,784 B |
| S2 | 1,000,000 | TESTED | TESTED | 78,303,232 B |
| S3 | 10,000,000 | BLOCKED before allocation | TESTED | 576,499,712 B |
| S4 | 100,000,000 | BLOCKED before allocation | BLOCKED before allocation | — |

The explicit S3 command was:

```bash
OWN_BRAIN_MEMORY_CAP_BYTES=1073741824 python3 scale_ladder.py
```

The 10-million-synapse run completed in 19.212303 seconds in the earlier packed measurement, with deterministic replay `true`. The default 512 MiB run correctly blocks it because the conservative estimate is 601,120,000 bytes; actual peak RSS is recorded for the explicit-budget run.

## What improved, measured

1. Per-synapse Python object/list overhead was replaced on the scale path with packed integer/float arrays.
2. The same seeded packed trace matches the reference implementation in an automated equivalence test.
3. The packed implementation improved the measured 1-million-synapse run from 3.861824 s / 177,864,704 B to 1.939107 s / 78,479,360 B in the comparable run.
4. The 10-million-synapse rung became runnable under an explicit 1 GiB local budget, while the default guard remained fail-closed.
5. S4 remains blocked; there is no silent OOM attempt.

## Limitations

This is a simulator and engineering benchmark, not a biological model or consciousness test. The memory override is a controlled local resource decision, not proof of a larger universal hardware limit. No learning rule has been evaluated yet, and no memory adapter or connectome-shaped wiring has been promoted.

## Next gate

BC-014 may begin only after the Phase 1 substrate is reviewed. It must add bounded STDP and a no-learning control with a held-out task. BC-015 remains read-only until Moderator and Security approve its schema. The 30–45 minute bulk digest must include the packed optimization, explicit budget, actual RSS, and limitations.
