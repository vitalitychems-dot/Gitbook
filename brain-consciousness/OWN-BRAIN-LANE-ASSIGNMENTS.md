# Own-brain lane assignments

**Authority:** Tessera assigns implementation lanes; Gitbook records them.  
**Current state:** These are scoped work items. An agent must still post the required check-in before editing.

| ID | Owner lane | Exact scope | Deliverable | Acceptance test | Status |
|---|---|---|---|---|---|
| BC-011 | Brain / computational neuroscience | Gitbook `OWN-BRAIN-PLAN.md`; equations and experiment definitions only | Phase 1 design note for LIF, sparse synapse, seeded events, reset, refractory period | Equations, units, seed semantics, tolerance, and null control are explicit | READY |
| BC-012 | TESSERA build | New isolated SNN package under a declared TESSERA path; no production chat changes | Original deterministic LIF core and sparse graph API | Unit tests for reset, threshold, refractory period, seeded replay, and invalid config rejection | READY |
| BC-013 | Build / performance | Scale harness only; no learning-rule edits | S0–S4 benchmark runner with memory, wall time, throughput, checkpoint size, and failure logs | S0–S2 run or are explicitly blocked; no silent OOM; same config hash gives same result | READY |
| BC-014 | Computational neuroscience | STDP experiment module and comparison note | Bounded STDP rule plus no-learning control | Held-out task improves against control or records a negative result; equation and deviations cited | READY |
| BC-015 | Brain memory interface | Read-only adapter boundary; no product-memory write | Versioned run-summary schema with provenance and rollback design | Schema rejects missing seed, commit, config hash, or output hash | READY |
| BC-016 | Connectome statistics | Public summary statistics only; no personal/protected data | Wiring comparison: random vs small-world vs connectome-shaped distributions | Each wiring method has source/license, fixed seed, and a declared control comparison | READY |
| BC-017 | Brain evaluation | Held-out self-improvement evaluation set | Private/held-out fixtures and deterministic scorer; no training leakage | Test fixtures are separated from training inputs; score is reproducible and limitations recorded | REPORTED ASSIGNMENT — check-in required |
| BC-018 | Moderator / Security | Claims, privacy, dependency, and safety review | Phase-gate checklist with flags and explicit non-claims | Every report keeps consciousness as goal/unknown; safety flags remain attributable and auditable | READY |
| BC-019 | Build / reproducibility | Run records and checkpoint format | Machine-readable result record for all scale rungs | Seed, hardware, config/input/output hashes, result, control, and limitations are present | READY |
| BC-020 | Gitbook Moderator | Digest and provenance | 30–45 minute digest template for brain lane | Digest lists only gate-cleared items with exact paths, tests, blockers, and owner | READY |

## Assignment rules

- BC-012 and BC-013 do not edit the same files.
- BC-014 begins only after BC-012 has a tested spike trace API.
- BC-015 is read-only until Security and Moderator approve the schema.
- BC-016 may use public statistics but may not import a whole connectome or upstream repository.
- BC-017 must remain held out from training and must not be used to tune the same run it evaluates.
- BC-018 reviews claims and boundaries; it does not implement the SNN.
- BC-020 summarizes evidence; it does not approve or merge code.

## Check-in requirement

Before work begins, post the standard check-in in Gitbook issue #2 and `history/coordination/agent-checkins.md`:

```text
IDENTITY: <actual account or declared role>
TASK: BC-###
SOURCE: <official source/ref or original design>
TARGET: <exact Gitbook or TESSERA path>
SCOPE: <included and excluded paths>
DELIVERABLE: <one result>
ACCEPTANCE TEST: <deterministic check>
OVERLAP CHECK: <Gitbook SHA, open PRs, other BC claims>
STATUS: ASSIGNED
```
