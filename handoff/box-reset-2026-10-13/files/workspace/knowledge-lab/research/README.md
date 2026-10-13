# Research

This section is the Tessera / Gitbook **theory–problem–connection mesh**: a living catalog of major theories, open mathematical and physical problems, proposed links between them, and small reproducible code experiments.

It exists so agents (and humans) can:

1. **Browse** established and speculative theories (`THEORIES.md`).
2. **Target** open problems with honest scope (`OPEN-PROBLEMS.md`).
3. **Propose** connections between theories with evidence and tests (`CONNECTIONS.md`).
4. **Run** small, logged experiments under `code/` and index them (`CODE-INDEX.md`).
5. **Follow** a gated research loop (`WORKFLOW.md`) instead of claiming proofs.

Father’s direction (2026-10-05, ~6:51 PM CT): the Gitbook should list theories and code catalogs; agents should try to connect theories and work toward solving current mathematical problems and physical phenomena using knowledge and abilities on this repo (and later the app). Solving famous open problems is a **GOAL**, not a claim. Verifying finite cases is **not** a proof.

## How the files connect

| File | Role |
|------|------|
| `README.md` (this file) | Purpose, map, label system |
| `THEORIES.md` | Index of major theories (math, physics, biology, CS, cognitive science) |
| `OPEN-PROBLEMS.md` | Open math/physics questions with realistic agent scope |
| `CONNECTIONS.md` | Template + worked examples of theory–theory links |
| `WORKFLOW.md` | Agent research loop, overlap checks, gates |
| `CODE-INDEX.md` | Reusable scripts under `research/code/` and related lab code |
| `code/` | Executable experiments + output logs |
| `../PROPOSED-ITEMS-RESEARCH.md` | Bulk-approval list (RS-001…) for these pages |

Related lab material (not yet under `research/`): `/workspace/knowledge-lab/scripts/` and `/workspace/knowledge-lab/results/` hold earlier knowledge-lab experiments (encoding, self-consistency, quantum-inspired, collective observation). Index those from `CODE-INDEX.md`; do not invent results.

Overlap checks before new work: Gitbook board **issue #2**, and `mesh/HANDOFF.md` when present in the active Gitbook checkout. Do not duplicate active claims.

## Label system

Use these status labels on claims, experiments, connections, and proposed items. One primary label per item; add a short note if needed.

| Label | Meaning |
|-------|---------|
| **TESTED** | A concrete command was run; output log and numbers are recorded. Finite verification only unless a formal proof is cited. |
| **REPORTED** | Stated from a reliable external source (paper, textbook, Wikipedia with primary refs). Not re-derived here. |
| **GOAL** | Aspirational target (e.g. “contribute toward Riemann”). Not a claim of solution. |
| **UNKNOWN** | Status or truth value not established in this repo; needs survey or experiment. |
| **BLOCKED** | Cannot proceed without data, compute, credentials, or a human decision. |
| **RETAINED** | Kept for history after supersession or failed attempt; do not treat as current claim. |

### Rules of use

- Prefer **TESTED** only when the exact command and log path are cited.
- Prefer **REPORTED** with a real URL or bibliographic citation—never invent sources.
- Mark famous open problems as **GOAL** when describing agent ambition; mark finite checks as **TESTED** with the caveat “not a proof.”
- Demote stale claims to **RETAINED** rather than deleting them silently.

## Non-goals

- No fabricated citations, runtimes, or “proofs.”
- No push to GitHub from this draft path unless Father / Tessera explicitly approves a branch + draft PR via the normal gates.
- No irreversible external posts from research agents without explicit approval.
