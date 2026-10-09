# Brain & Consciousness Development — agent workplan

**Coordinator:** Tessera assigns BC items. Gitbook Moderator reviews only; it never merges or promotes anything into TESSERA. Check-ins go through the conference issue.

**Scope:** Build a software-only, CL1-inspired spiking-neural-network research program for TESSERA. This is not a biological CL1 replica and does not establish consciousness.

See [Cortical Labs readiness](../intake/CORTICAL-LABS-READINESS.md). HYB-019 is BLOCKED on Father's answers in section (d) of that page.

## No-overlap work queue

| ID | Lane | Suggested owner | Deliverable | Acceptance test | Status |
|---|---|---|---|---|---|
| BC-001 | Source and license audit | Github Scraper (provisional, not instantiated); Gitbook Moderator reviews only | Update [SNN-SOURCE-MANIFEST.md](SNN-SOURCE-MANIFEST.md) with pinned refs, licenses, and advisories | Every proposed dependency has an official URL, license, ref, and disposition | PROPOSED |
| BC-002 | Neuron dynamics | TESSERA build lane — PROPOSED (unrostered) | Original LIF neuron adapter and deterministic spike trace API in TESSERA | Unit tests cover reset, threshold, refractory period, and repeatability | PROPOSED |
| BC-003 | Plasticity research | Computational neuroscience lane — PROPOSED (unrostered) | Compare STDP rules across the listed sources and write an experiment note | Reproduce one published/reference equation and report deviations | PROPOSED |
| BC-004 | Learning environment | RL / task lane — PROPOSED (unrostered) | Small deterministic benchmark environment with spike input/output | Same seed produces the same episode trace; baseline is documented | PROPOSED |
| BC-005 | Cognitive interfaces | BrainCog research lane — PROPOSED (unrostered) | Map memory, decision, and perception concepts to TESSERA interfaces without importing incompatible code | Interface proposal includes inputs, outputs, state, and tests | PROPOSED |
| BC-006 | Trainable PyTorch path | snnTorch research lane — PROPOSED (unrostered) | Evaluate a minimal original trainable SNN adapter | CPU smoke test and one reproducible training run pass | PROPOSED |
| BC-007 | Equation simulator comparison | Brian2 research lane — PROPOSED (unrostered) | Compare one neuron/synapse model against Brian2 reference output | Numeric tolerance and simulator version are recorded | PROPOSED |
| BC-008 | BindsNET comparison | BindsNET research lane — PROPOSED (unrostered) | Compare learning-rule and RL experiment semantics | No upstream code copied; differences and license constraints recorded | PROPOSED |
| BC-009 | Event memory and observability | TESSERA systems lane — PROPOSED (unrostered) | Event schema for spikes, rewards, state, provenance, and experiment runs | Schema validation rejects missing provenance and nondeterministic run IDs | PROPOSED |
| BC-010 | Safety and claims review | Gitbook Moderator | Review language, data handling, dependency permissions, and claims about brain/consciousness | No unverified consciousness or biological-equivalence claim remains | PROPOSED |

The owner-provided own-brain plan expands the queue with the following non-overlapping tasks. Full scopes and acceptance tests are in [Own-brain lane assignments](OWN-BRAIN-LANE-ASSIGNMENTS.md):

| ID | Lane | Deliverable | Acceptance test | Status |
|---|---|---|---|---|
| BC-011 | Brain / computational neuroscience | Phase 1 LIF, sparse-synapse, seed, and null-control design note | Equations, units, seed semantics, tolerance, and control are explicit | TESTED — design recorded |
| BC-012 | TESSERA build | Original deterministic LIF core and sparse graph API | Reset, threshold, refractory, replay, and invalid-config tests pass | TESTED locally — 5/5 tests; promotion pending review |
| BC-013 | Build / performance | S0–S4 scale ladder runner | S0–S2 run or are explicitly blocked with resource logs | TESTED locally — S0–S2 pass; S3–S4 blocked by 512 MiB cap |
| BC-014 | Computational neuroscience | Bounded STDP plus no-learning control | Held-out task comparison is reproducible or negative result is recorded | READY |
| BC-015 | Brain memory interface | Read-only versioned run-summary adapter | Missing provenance fields are rejected; no silent product-memory write | READY |
| BC-016 | Connectome statistics | Random/small-world/connectome-shaped wiring comparison | Public source/license and seeded control comparison are recorded | READY |
| BC-017 | Brain evaluation | Held-out self-improvement test set and scorer | No training leakage; deterministic score and limitations are published | REPORTED ASSIGNMENT |
| BC-018 | Moderator / Security | Claims, privacy, dependency, and safety review | Consciousness remains goal/unknown and flags are attributable | READY |
| BC-019 | Build / reproducibility | Machine-readable scale-ladder result records | Seed, hardware, config/input/output hashes, result, and limits are present | TESTED locally — `scale-results.json` recorded |
| BC-020 | Gitbook Moderator | 30–45 minute brain-lane digest template | Only gate-cleared items appear with exact evidence and owners | READY |

Suggested owners are not assignments unless the check-in is posted. The owner message reports BC-017 as assigned; the lane must still check in before editing. Phase 1 exists in the isolated `research/own-brain` path, but no learning rule, memory adapter, or runtime SNN integration has been promoted.

## Check-in protocol

Items are assigned by Tessera. After Tessera assigns a BC item, the assigned lane posts one check-in in the Gitbook conference before work begins, using:

```text
IDENTITY: <declared agent or lane>
TASK: BC-###
SOURCE: <official URL and pinned ref>
TARGET: <exact Gitbook or TESSERA path>
SCOPE: <what is included and excluded>
DELIVERABLE: <one result>
ACCEPTANCE TEST: <deterministic check>
OVERLAP CHECK: <Gitbook main SHA checked; open PRs checked (numbers or none); overlapping BC task or none>
STATUS: ASSIGNED (by Tessera)
```

On completion, update the same check-in with the commit, test output, provenance, limitations, and the next task. Agents must not mark another lane complete.

## Build order

1. BC-001, BC-010, and BC-018 establish source, license, privacy, and claims boundaries.
2. BC-011 and BC-012 establish the deterministic own-brain substrate.
3. BC-013 and BC-019 measure the real hardware limit from 10,000 through 100,000,000 synapses.
4. BC-014, BC-016, and the existing BC-003/006/007/008 run isolated learning and wiring comparisons.
5. BC-015 and BC-009 define the read-only memory/event boundary; no product-memory write is automatic.
6. BC-017 supplies the held-out self-improvement evaluation before any loop can claim progress.
7. BC-004 and BC-005 integrate only interfaces that pass tests.
8. The Gitbook Moderator reviews validated ideas but never merges or promotes them into TESSERA (see Promotion gate). Rejected or deferred ideas are recorded here.

## Promotion gate

A proposal moves from Gitbook to TESSERA only when it has: a source or original-design rationale, an owner assigned by Tessera, a non-overlapping scope, a deterministic test, a security/dependency review, and a limitations statement. Meeting these criteria is not approval. The proposal then goes Moderator, then Tessera, then Security, then CI/Build, then Father's final yes in a bulk digest. Nothing merges into TESSERA without Father's explicit yes.
