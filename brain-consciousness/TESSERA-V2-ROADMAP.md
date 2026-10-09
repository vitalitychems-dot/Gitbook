# TESSERA V2 build roadmap

**Status:** PROPOSED / gated roadmap  
**Meaning of “launch”:** run the current private TESSERA application locally for inspection. It does not mean consciousness, independent agency, or permission to modify production code without review.

## V2 objectives

V2 is a more testable TESSERA build: deterministic local SNN experiments, explicit evidence records, safer memory boundaries, and a UI/API surface that reports what was actually tested. V2 does not promise AGI or consciousness.

## Build order

| Gate | Scope | Evidence required | Promotion state |
|---|---|---|---|
| V2.0 | Preserve current private TESSERA and Phase 1 SNN | typecheck, tests, clean worktree, Phase 1 report | READY for review |
| V2.1 | Add bounded STDP experiment and no-learning control | held-out task, equation, seed, control score, negative-result path | BLOCKED until BC-014 check-in |
| V2.2 | Add read-only run-summary adapter | schema/rollback tests; no automatic product-memory write | BLOCKED until BC-015 review |
| V2.3 | Add scale dashboard | exact result JSON, blocked-rung visualization, no invented values | BLOCKED until Build review |
| V2.4 | Compare wiring controls | random vs small-world vs public-statistics-shaped, with licenses and null result | BLOCKED until BC-016 review |
| V2.5 | Self-improvement evaluation | held-out fixtures, no training leakage, N=1 proposal per 45-minute digest | BLOCKED until BC-017 check-in |

## Launch checklist

1. Run TESSERA locally in private mode.
2. Confirm health/readiness and record the commit.
3. Run the existing typecheck and test suite.
4. Run the own-brain Phase 1 tests and scale harness.
5. Inspect the result record and limitations.
6. Stop before production-memory writes, external APIs, autonomous code changes, or deployment.

## V2 non-goals

- No autonomous self-rewrite or self-merge.
- No claim of consciousness, sentience, or biological equivalence.
- No remote/cloud training or external API dependency for the own-brain lane.
- No importing whole upstream SNN repositories or protected/private data.
