# TESSERA own-brain plan

**Status:** REPORTED / ready for lane assignment  
**Scope:** local, simulator-only, software spiking neural network  
**Product boundary:** TESSERA remains the build; Gitbook remains the coordination and provenance hub.

## Ground rules

1. **Consciousness is a goal and research question, never a claim.** No metric, demo, benchmark, or internal state can be described as proof of consciousness, sentience, awareness, or biological equivalence.
2. **No unsupported biological specification.** Social-media claims about “3 trillion perceptrons” or unknown brain mechanisms are not requirements. There is no complete human synapse map. Public connectome data are references for statistics and hypotheses only.
3. **Original implementation first.** Use documented leaky spiking neurons and sparse synapses owned by TESSERA. External SNN projects are comparison/reference sources, not wholesale imports.
4. **Determinism is mandatory.** Every experiment records seed, code commit, configuration, hardware, software versions, input hash, and output hash. Same inputs and seed must reproduce the same trace within the declared numeric tolerance.
5. **Local-only execution.** No API, cloud model, remote training, external account, purchase, or biological hardware is required. CL1 is a simulator/reference comparison only.
6. **Safety gates remain active.** Moderator → TESSERA → Security → Build/CI → human owner bulk approval. Every safety flag remains `0` unless an attributable reviewer changes it with evidence.
7. **One lane, one owner, one scope.** A task is not active until the owner or Tessera posts the check-in in Gitbook issue #2 and the ledger.

## Core design

- **Neuron:** original leaky integrate-and-fire dynamics with explicit membrane decay, threshold, reset, and refractory handling.
- **Synapse:** sparse weighted event connection with explicit delay and bounded update rule.
- **Learning:** STDP and other rules are experiments behind feature flags; no learning rule is accepted without a deterministic unit test and a held-out evaluation.
- **State:** event log plus checkpointed network state; every state transition has provenance.
- **Memory link:** network state may feed Tessera lesson memory only through a versioned adapter that records source run, seed, feature schema, and confidence. It must not silently write product memory.
- **Wiring:** public connectome statistics may shape degree distributions, sparsity, delays, or motif sampling. They do not constitute a reconstructed human brain.
- **Indicators:** publish computable measures such as integration, recurrence, perturbation response, prediction error, information transfer, stability, and learning progress with limits and null baselines. These are indicators, not consciousness tests.

## Scale ladder

Run the same declared benchmark at these synapse rungs:

| Rung | Target synapses | Required report |
|---|---:|---|
| S0 | 10,000 | correctness, deterministic replay, memory, wall time |
| S1 | 100,000 | same metrics plus event throughput |
| S2 | 1,000,000 | same metrics plus checkpoint size and peak RAM |
| S3 | 10,000,000 | measured limit, batching strategy, failure mode |
| S4 | 100,000,000 | attempt only if hardware permits; report honest refusal/limit if not |

The result is the **measured hardware limit**, not completion of a target. A rung may be marked `BLOCKED` when it exceeds memory, time, thermal, or reproducibility limits.

## Phase gates

### Phase 1 — deterministic substrate

Implement original LIF dynamics, sparse graph construction, seeded event generation, spike traces, reset/refractory behavior, and replay tests. No self-modification and no product-memory writes.

**Exit:** S0 passes deterministic replay and unit tests on a clean checkout.

### Phase 2 — scale harness

Add the scale ladder runner, resource measurements, checkpointing, and machine-readable result records. One benchmark and one seed are insufficient for a claim; report repetitions and variance.

**Exit:** S0–S2 are measured or explicitly blocked with logs; no silent OOM or partial result is called success.

### Phase 3 — learning rules

Add STDP behind a flag, then compare against a no-learning control. Use synthetic tasks first. Record equation, discretization, bounds, initialization, and deviations from the cited reference.

**Exit:** learning beats the declared control on a held-out task without sacrificing reproducibility or safety invariants.

### Phase 4 — memory adapter

Expose a read-only run summary first. Only after schema review may a separate adapter propose lesson-memory records. Product memory writes remain gated and reversible.

**Exit:** provenance and rollback tests pass; a failed run cannot corrupt lesson memory.

### Phase 5 — connectome-shaped wiring

Use public summary statistics or openly licensed connectome-derived distributions. Do not ingest protected or personal data. Compare random, small-world, and connectome-shaped controls.

**Exit:** wiring choice improves a declared metric or is retained as a documented null result.

### Phase 6 — indicators and self-improvement evaluation

Run computable indicators against null/control networks. Keep consciousness language out of result labels. The self-improvement loop uses a held-out test set and N=1 proposal per 45-minute digest until the owner changes that limit.

**Exit:** indicators, limits, negative results, and held-out scores are published in Gitbook; no claim of consciousness is made.

## Required result record

```text
TASK: BC-###
IDENTITY: <actual account or declared lane>
BASE: <TESSERA/Gitbook commit>
SEED: <integer>
HARDWARE: <machine and resource limits>
CONFIG_HASH: <hash>
INPUT_HASH: <hash>
OUTPUT_HASH: <hash>
RUNG: S0 | S1 | S2 | S3 | S4
RESULT: <measured result or BLOCKED reason>
CONTROL: <declared baseline>
LIMITATIONS: <known gaps>
STATUS: TESTED | REPORTED | BLOCKED | RETAINED | REJECTED
```

## Explicit non-goals

- No claim that TESSERA is conscious or will become conscious.
- No biological cell culture, human tissue, wet lab, or CL1 access.
- No copying of a proprietary or biological connectome.
- No unreviewed upstream dependency or whole-repository vendor import.
- No autonomous self-modification of production code or memory.
