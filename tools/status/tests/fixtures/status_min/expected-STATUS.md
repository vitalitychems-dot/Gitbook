# Mesh status

Built 2026-10-13 15:00 CT by status.py from files only (0 model tokens). Source: HANDOFF.md as of 2026-10-12, TASKS.json, intake/log.md.

## Needs attention

- HANDOFF.md 'As of' is 1 day(s) old (2026-10-12)
- Q-1 is 'queued' but GB-001 is 'published' in HANDOFF.md -> close or re-scope
- Q-2 claim by Build is older than 6h with no PR -> re-queue
- GB-002: missing Link
- GB-002: HANDOFF says 'in review', intake log says 'published'

## By lane: doing and next

| Lane | Item | State | Next |
|---|---|---|---|
| Build | GB-002 | in review | Re-gate (Build) |
| Moderator | GB-003 | stale | Reassign (Tessera) |

## Queue (mesh/queue/TASKS.json)

| Task | Lane | Status | Title |
|---|---|---|---|
| Q-1 | Build | queued | Land GB-001 |
| Q-2 | Build | claimed | Fix GB-002 |

## Done

- GB-001 (Build): merged `abc1234`

## Can be cleaned up

- GB-001: done with next step 'none' -> move line to archive
- GB-003: stale -> Reassign (Tessera)
