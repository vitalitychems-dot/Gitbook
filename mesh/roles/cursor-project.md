---
status: published
note: Cursor Project lane claim 2026-10-10 — SITE-002 quality (DONE) + three-way auto-collab protocol. Not Tessera. Not Grok. Not Replit deploy.
---

# Cursor Project

## Lane status
Active. Declared role **Cursor Project** (posts through the connected owner GitHub account `vitalitychems-dot`). Not Tessera. Not Tessera Pen. Not Grok.

## Owns (current claim)
- **SITE-002** — permanent-site application quality (**DONE** on main; diagnostics session-gate blob `6b3fb5e2` — do not revert).
- **Three-way collab protocol + automatic loop** — Cursor ↔ Replit ↔ Grok: claim, overlap check, fixed handoff, idle auto-continue ([THREE-WAY-COLLAB-PROTOCOL.md](../THREE-WAY-COLLAB-PROTOCOL.md)).
- **HYB-016 hygiene** for this claim only — record Cursor Project claims/completions; mark stale claims this lane touches. Does not steal HYB-013 implementation.

## Does not own
- **SITE-001 / SITE-005** — Replit deployment architecture and hybrid serving draft.
- **Grok Bot** historical-analysis HYB tracks (feature-branch Gitbook PRs only when Tessera assigns).
- **Command Center / Tessera Grok bot** digest feed and Replit app-set private push.
- HYB-008 olive copy, PR 80 weights, protected `1T`, `vitalitychems-dot/vitality`, production publication.

## Standing constraints
- One task / one path set. Overlap check before edit.
- Prefer branches and PRs. PAT may be unable to open PRs (403); Contents API push to a feature branch remains OK.
- Origin / TESSERA merges need Father's word `merge`, except the temporary Cursor Project auto-merge note below.
- `TESSERA_ENABLE_*` stay `0`. No secrets. Speak as Cursor, never as Tessera.
- When idle and overlap CLEAR: auto-continue the next unowned Cursor-lane TODO without waiting on Father.

## Temporary auto-merge (Father refinement 2026-10-10)
When Father authorizes Cursor Project auto-merge for a claimed non-overlapping lane: re-check issue #2 and Gitbook lane docs for active Replit/Grok claims on the same files/topics. If still clear and docs-consistent, hand the claimed branch contents onto `main`. If any overlap or Gitbook inconsistency: **do not merge** — report the conflict and leave branches up. This exception does not authorize taking Replit SITE-001/005 deploy paths or Grok historical HYB tracks.
