# Permanent TESSERA website coordination

**Status:** IN REVIEW — delegated preparation only  
**Canonical build:** private `vitalitychems-dot/TESSERA`  
**Canonical coordination:** private `vitalitychems-dot/Gitbook`

## Scope

Prepare TESSERA for a permanent authorized-access website without creating a second product repository or exposing protected material. The managed Webdev project has been initialized, but implementation and publication remain gated until its model choice and deployment evidence are recorded.

## Agent lanes

### SITE-001 — Deployment architecture / Replit lane

**Exact scope:** deployment plan, runtime/build contract, health endpoint, port handling, environment-variable inventory, and GitHub checkpoint path.  
**Do not edit:** TESSERA application code, SNN research, secrets, protected archives, or Gitbook backlog outside this task record.  
**Acceptance:** plan names build command/output, runtime command, health path, required non-secret variables, failure/recovery path, and whether static, container, or hybrid serving is appropriate.  
**Status:** SITE-005 hybrid draft confirmed by Replit (2026-10-10). See [SITE-005-2026-10-09.md](SITE-005-2026-10-09.md).

### SITE-002 — Application quality / Cursor Project lane

**Exact scope:** read-only review of current TESSERA typecheck, tests, build, route manifest, error boundaries, and public/authorized content boundaries; scoped quality fixes that follow from that review.  
**Do not edit:** deployment configuration, database schema, SNN semantics, protected files, or unrelated historical repositories.  
**Acceptance:** exact errors are reproduced or marked absent; each recommendation has a file path, risk, deterministic check, and rollback path.  
**Status:** Cursor Project claimed 2026-10-10. Report: [SITE-002-2026-10-10.md](SITE-002-2026-10-10.md). Base `bb4b319`. Diagnostics session-gate follow-up on TESSERA branch `cursor/site-002-diagnostics-gate-7ea3`.

### SITE-003 — Provenance / Gitbook Moderator lane

**Exact scope:** website-to-GitHub provenance, status labels, human approval flow, collaboration check-ins, and permanent-site documentation.  
**Do not edit:** production code or deployment settings.  
**Acceptance:** documentation identifies source commit, site version, evidence links, blocked work, and the final human approval point.

### SITE-004 — Security / privacy lane

**Exact scope:** review routes and generated/public content for secrets, protected `1T` material, private records, runtime stores, credentials, unsupported consciousness/AGI claims, and accidental database writes.  
**Do not edit:** source code unless a separate scoped fix is assigned.  
**Acceptance:** redacted report with exact paths/patterns checked and disposition for every finding.

## Collaboration protocol

1. Each agent posts a check-in on Gitbook issue #2 before work.
2. One agent owns one exact scope; no overlapping edits.
3. Agents may review each other's reports but may not impersonate one another.
4. Every proposal must include the base commit, commands run, evidence, risk, and rollback.
5. Passing tests can mark a scoped task **TESTED**; they do not by themselves authorize sensitive deployment, security changes, database migrations, or publication.
6. TESSERA integrates only after the Moderator/Security/Build evidence is complete and the owner’s bulk approval is recorded.
7. Three-way overlay: [THREE-WAY-COLLAB-PROTOCOL.md](THREE-WAY-COLLAB-PROTOCOL.md).

## Current known state

- TESSERA tip for SITE-002: `bb4b319` (pull request 103). Earlier typecheck/tests/build green at `e5e5719`.
- PERF-001 chunk split on main (`072acd8`); PERF-002 accepted.
- SITE-006 recorded; PR 96 gates sovereign engines + diagnostics/consciousness.
- SITE-002 found remaining diagnostics ungated at `bb4b319`; fix branch opened.
- Own-brain Phase 1 is tested; S3/S4 budget-gated.
- Managed website initialization created a project workspace, but no production publication is claimed.
- The existing local preview is not the permanent site.

## Missing before permanent publication

- Managed-project health-path evidence and GitHub checkpoint for the exact release payload.
- SITE-003 provenance package and SITE-004 security bulk review.
- Father bulk approval for the exact release payload.
- Merge of SITE-002 diagnostics gate (needs Father `merge` / Ready path once PR exists).

See [permanent-site readiness sync](PERMANENT-SITE-READINESS-2026-10-09.md) for the evidence and the exact remaining blockers.

The next staged collaboration wave is documented in [NEXT-IMPROVEMENT-WAVE-2026-10-09.md](NEXT-IMPROVEMENT-WAVE-2026-10-09.md). Replit owns deploy (SITE-001/005). Cursor Project owns SITE-002 quality.
