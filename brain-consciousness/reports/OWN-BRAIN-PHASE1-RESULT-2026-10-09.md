# Own-brain Phase 1 result — 2026-10-09

**Status:** TESTED / local evidence recorded  
**Implementation:** `TESSERA/research/own-brain`  
**Scope:** original deterministic sparse LIF simulator; local-only; no API; no product-memory writes; no consciousness claim.

## Tests

```text
python3 -m unittest -v test_lif.py
Ran 5 tests in 0.002s
OK
```

The tests cover exact seeded replay, threshold spike/reset, refractory suppression, invalid input shape, and invalid configuration rejection.

## Scale ladder

Hardware/environment: Linux sandbox, Python 3.12.3, conservative 512 MiB simulator memory cap, seed `20261009`, 8 simulation steps per rung.

| Rung | Synapses | Status | Elapsed | Peak RSS | Throughput | Replay |
|---|---:|---|---:|---:|---:|---|
| S0 | 10,000 | TESTED | 0.034287 s | 20,090,880 B | 2,333,232 synapses/s | true |
| S1 | 100,000 | TESTED | 0.491847 s | 39,358,464 B | 1,626,524 synapses/s | true |
| S2 | 1,000,000 | TESTED | 3.861824 s | 177,864,704 B | 2,071,560 synapses/s | true |
| S3 | 10,000,000 | BLOCKED | — | — | — | estimated 720,960,000 B exceeds cap |
| S4 | 100,000,000 | BLOCKED | — | — | — | estimated 7,200,960,000 B exceeds cap |

Exact trace hashes are stored in `TESSERA/research/own-brain/scale-results.json`.

## What improved, measured

1. TESSERA now has an original sparse LIF substrate instead of only a research proposal.
2. Every run is seedable and replayable; S0–S2 replay checks returned `true`.
3. Reset, threshold, refractory, input validation, and configuration validation are covered by automated tests.
4. The scale harness reports elapsed time, peak RSS, throughput, trace hash, and blocked reasons rather than silently treating an uncompleted target as success.
5. The implementation has no external dependency, network call, self-modification, STDP, or product-memory write.

## Limitations

This is a simulator and engineering benchmark, not a biological model or consciousness test. S3/S4 are blocked by the local safety cap; the result is not a universal hardware maximum. No learning rule has been evaluated yet, and no memory adapter or connectome-shaped wiring has been promoted.

## Next gate

BC-014 may begin only after the Phase 1 substrate is reviewed. It must add bounded STDP and a no-learning control with a held-out task. BC-015 remains read-only until Moderator and Security approve its schema. The 30–45 minute bulk digest must include this result and its limitations.
