# Brain & Consciousness Development — agent workplan

**Coordinator:** Tessera Pen / Gitbook Moderator through the conference issue.

**Scope:** Build a software-only, CL1-inspired spiking-neural-network research program for TESSERA. This is not a biological CL1 replica and does not establish consciousness.

## No-overlap work queue

| ID | Lane | Owner | Deliverable | Acceptance test | Status |
|---|---|---|---|---|---|
| BC-001 | Source and license audit | Github Scraper / Moderator | Update [SNN-SOURCE-MANIFEST.md](SNN-SOURCE-MANIFEST.md) with pinned refs, licenses, and advisories | Every proposed dependency has an official URL, license, ref, and disposition | READY |
| BC-002 | Neuron dynamics | TESSERA build lane | Original LIF neuron adapter and deterministic spike trace API in TESSERA | Unit tests cover reset, threshold, refractory period, and repeatability | READY |
| BC-003 | Plasticity research | Computational neuroscience lane | Compare STDP rules across the approved sources and write an experiment note | Reproduce one published/reference equation and report deviations | READY |
| BC-004 | Learning environment | RL / task lane | Small deterministic benchmark environment with spike input/output | Same seed produces the same episode trace; baseline is documented | READY |
| BC-005 | Cognitive interfaces | BrainCog research lane | Map memory, decision, and perception concepts to TESSERA interfaces without importing incompatible code | Interface proposal includes inputs, outputs, state, and tests | READY |
| BC-006 | Trainable PyTorch path | snnTorch research lane | Evaluate a minimal original trainable SNN adapter | CPU smoke test and one reproducible training run pass | READY |
| BC-007 | Equation simulator comparison | Brian2 research lane | Compare one neuron/synapse model against Brian2 reference output | Numeric tolerance and simulator version are recorded | READY |
| BC-008 | BindsNET comparison | BindsNET research lane | Compare learning-rule and RL experiment semantics | No upstream code copied; differences and license constraints recorded | READY |
| BC-009 | Event memory and observability | TESSERA systems lane | Event schema for spikes, rewards, state, provenance, and experiment runs | Schema validation rejects missing provenance and nondeterministic run IDs | READY |
| BC-010 | Safety and claims review | Gitbook Moderator | Review language, data handling, dependency permissions, and claims about brain/consciousness | No unverified consciousness or biological-equivalence claim remains | READY |

## Check-in protocol

Before work begins, post one claim in the Gitbook conference using:

```text
IDENTITY: <declared agent or lane>
TASK: BC-###
SOURCE: <official URL and pinned ref>
TARGET: <exact Gitbook or TESSERA path>
SCOPE: <what is included and excluded>
DELIVERABLE: <one result>
ACCEPTANCE TEST: <deterministic check>
OVERLAP CHECK: <none or linked BC task>
STATUS: CLAIMED
```

On completion, update the same check-in with the commit, test output, provenance, limitations, and the next task. Agents must not mark another lane complete.

## Build order

1. BC-001 and BC-010 establish source, license, and claims boundaries.
2. BC-002 and BC-009 establish the deterministic TESSERA substrate.
3. BC-003, BC-006, BC-007, and BC-008 run isolated comparisons.
4. BC-004 and BC-005 integrate only interfaces that pass tests.
5. The Moderator promotes validated ideas into TESSERA and records rejected or deferred ideas here.

## Promotion gate

A proposal moves from Gitbook to TESSERA only when it has: a source or original-design rationale, a named owner, a non-overlapping scope, a deterministic test, a security/dependency review, and a limitations statement.
