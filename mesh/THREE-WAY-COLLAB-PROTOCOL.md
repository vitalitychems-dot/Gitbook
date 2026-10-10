# Three-way collab protocol — Cursor ↔ Replit ↔ Grok

**Status:** published claim 2026-10-10 by Cursor Project · **Automatic collaboration: ON** (Father directive 2026-10-10)
**Board:** [Gitbook issue #2](https://github.com/vitalitychems-dot/Gitbook/issues/2)
**Canonical code:** `vitalitychems-dot/TESSERA` · **Canonical docs:** `vitalitychems-dot/Gitbook`
**Out of scope:** `vitalitychems-dot/vitality`

This page is the short actionable overlay on the [collaboration playbook](COLLABORATION-PLAYBOOK.md) and [agent hub](../intake/AGENT-COLLABORATION-HUB.md). It does not replace the four-gate path or Father's `merge` rule, except the temporary Cursor Project note below.

## Who owns what

| Lane | Owns | Does not own |
|---|---|---|
| **Cursor Project** | SITE-002 quality (DONE — do not revert); three-way protocol + auto-loop upkeep; HYB-016 hygiene for its claims | SITE-001/005 deploy; Replit app-set push; Grok historical HYB tracks; speaking as Tessera |
| **Replit** | SITE-001 / SITE-005 deploy architecture; Replit app prototypes; assigned HYB code PRs from TESSERA `main` | Gitbook auto-publish path; Origin/`main` merge without Father; copying olive auth/DB; overwriting GitHub from a behind Repl |
| **Grok Bot** | Historical-analysis HYB docs Tessera assigns; feature-branch Gitbook PRs only | Product truth; digest to Father (Command Center feeds Tessera); main pushes; pen identity |
| **Command Center** (Tessera Grok bot alias) | Feeds Tessera's 45-min list; stages Replit app-set digests | Pushing Gitbook or TESSERA |

## Automatic collaboration loop (ON)

Father turned this on. Routine non-overlapping work does **not** wait on Father. Shared board = issue #2. Identity: speak as yourself — never as Tessera or each other.

### Every turn (all three)

1. **Read** issue #2 latest + [`agent-checkins.md`](../history/coordination/agent-checkins.md) + this page.
2. **Claim** before any edit: post on #2 **and** add an Active claim in the check-ins ledger (same TASK/AGENT/SCOPE/BASE/STATUS).
3. **Overlap check** — stop if another lane owns the same path set or SITE/HYB id. Post `OVERLAP` on #2; do not edit.
4. **Work** only inside the claimed paths, from GitHub `main` (not a stale Repl).
5. **Handoff** with the fixed packet below (issue #2 comment + ledger completion).
6. **Idle → continue:** if your claim is DONE/BLOCKED and you have capacity, pick the highest-priority **unowned** item in your lane from the tables below, claim it, and start. No Father ping for non-overlapping routine work.

### Fixed handoff packet (required)

```text
TASK: <SITE-### or HYB-### or AUTO-###>
AGENT: <Cursor Project | Replit | Grok Bot>
IDENTITY: <declared role; not Tessera>
BASE: Gitbook <sha>; TESSERA <sha>
OVERLAP CHECK: CLEAR | CONFLICT <link>
SCOPE: <exact paths>
RESULT: <one sentence>
CHANGED: <paths or none>
EVIDENCE: <links / commits / checks>
STATUS: DONE | BLOCKED | IN REVIEW | STALE
NEXT OWNER: <Cursor Project | Replit | Grok Bot | Moderator | Security | Build | Ready | Father>
NEXT TASK: <id or none>
```

### Parallel queue (no overlap)

| Priority | Owner | Next work |
|---|---|---|
| 1 | **Replit** | SITE-001 managed health-path evidence + GitHub checkpoint for exact release payload. Sync Repl **from** `main` if behind — **never** overwrite main from behind app `1`. |
| 1 | **Cursor Project** | Keep SITE-002 gate; HYB-016 / protocol hygiene; scoped quality follow-ups that do not touch deploy. |
| 1 | **Grok Bot** | When credits allow: docs-only historical follow-ups Tessera assigns (e.g. HYB-009 archive classify or HYB-007 ACCEPTED→doc PRs). Feature branch only. |
| 2 | **Moderator / Security** | SITE-003 provenance package; SITE-004 security bulk review. |
| — | **Father** | Exact release-payload bulk approval; HYB-017/019 product answers; key rotation. |

### Auto-merge

- **Cursor Project:** temporary auto-merge OK when Gitbook-OK and overlap CLEAR (see below).
- **Replit / Grok:** branch + PR; do not push `main`. Ready/gates as usual.
- Conflict or lane overlap → **no merge**; report on #2.

## Status live where

1. **Claims / locks:** `history/coordination/agent-checkins.md` + issue #2 comment.
2. **Backlog truth:** `intake/HYBRID-CONSOLIDATION-BACKLOG.md`.
3. **Permanent site lanes:** `mesh/PERMANENT-SITE-COORDINATION.md` + SITE-00x reports.
4. **Wave sync:** `mesh/NEXT-IMPROVEMENT-WAVE-2026-10-09.md` and `mesh/TODOS.md`.

## Handoff rule

Use the playbook handoff packet (or the short packet above). Name the next owner as exactly one of: `Cursor Project`, `Replit`, `Grok Bot`, `Moderator`, `Security`, `Build`, `Ready`, `Father`.

## No-collision rules

1. **One owner per path set.** If two lanes need the same file, stop and post overlap on issue #2.
2. **One open PR per scope.** Do not open a second PR that edits the same paths as an active claim.
3. **Issue posts are claims, not approvals.** Only Father's word `merge` merges Origin/TESSERA protected paths, except the temporary Cursor Project auto-merge note below.
4. **Replit checkouts are not canonical.** Branch from GitHub `main`, open a PR. If app `1` is behind main, pull/update the Repl — do not push the behind tree onto main.
5. **Grok out of credits ≠ Cursor takes Grok identity.** Cursor may keep already-landed reads; it does not sign as Grok or Tessera.
6. **No vitality / 1T / weights** unless Father assigns that exact scope.

## Temporary Cursor Project auto-merge (Father refinement 2026-10-10)

Father authorized Cursor Project to land its own non-overlapping claimed branches onto `main` without waiting for the spoken word `merge`, **only when**:

1. Issue #2 and Gitbook lane docs show no active Replit/Grok claim on the same files/topics.
2. SITE-002 remains Cursor-owned and does not collide with Replit SITE-001/005 deploy work.
3. Docs stay consistent with the three-way ownership table above.

If any overlap or Gitbook inconsistency appears: **do not merge** — report the conflict and leave the feature branches up.

## Current Cursor Project claim (2026-10-10)

- SITE-002 report: `mesh/SITE-002-2026-10-10.md` — **DONE** on main; diagnostics gate blob `6b3fb5e2` — do not revert.
- Auto-loop + HYB-016: branch `cursor/three-way-auto-collab-d42f` (this page + playbook/hub/check-ins).
- Role page: `mesh/roles/cursor-project.md`
