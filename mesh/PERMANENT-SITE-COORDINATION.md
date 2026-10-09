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

### SITE-002 — Application quality / Cursor lane

**Exact scope:** read-only review of current TESSERA typecheck, tests, build, route manifest, error boundaries, and public/authorized content boundaries.  
**Do not edit:** deployment configuration, database schema, SNN semantics, protected files, or unrelated historical repositories.  
**Acceptance:** exact errors are reproduced or marked absent; each recommendation has a file path, risk, deterministic check, and rollback path.

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

## Current known state

- TESSERA typecheck and full workspace tests pass at `c71b4ef`.
- Gitbook coordination is at `ddd8b4c` before this record.
- Own-brain Phase 1 is tested; S3 is available only under an explicit 1 GiB local budget; S4 remains blocked.
- Managed website initialization created a project workspace, but no production publication is claimed.
- The existing local preview is not the permanent site.

## Missing before permanent publication

- Deployment architecture report and chosen serving mode.
- Route manifest and authorized/public content review.
- Production build and health-path evidence from the managed project.
- GitHub checkpoint with the intended canonical source commit.
- Security/privacy report and secret-shaped-path scan.
- Human bulk approval for the exact release payload.
