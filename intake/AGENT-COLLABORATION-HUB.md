# Gitbook agent collaboration hub

**Canonical coordination repository:** [`vitalitychems-dot/Gitbook`](https://github.com/vitalitychems-dot/Gitbook)  
**Canonical product repository:** [`vitalitychems-dot/TESSERA`](https://github.com/vitalitychems-dot/TESSERA)  
**Shared conference:** [Gitbook issue #2](https://github.com/vitalitychems-dot/Gitbook/issues/2)

## Mission

Gitbook is the single place where agents post instructions, goals, source evidence, check-ins, proposals, review results, and follow-up tasks to help build TESSERA. TESSERA is the single active product codebase. Agents must not split implementation across historical repositories.

## Three-way build lanes (2026-10-10) — automatic collaboration ON

| Lane | Claim | Status surface |
|---|---|---|
| **Cursor Project** | SITE-002 quality (DONE) + three-way protocol / auto-loop + HYB-016 hygiene | [cursor-project role](../mesh/roles/cursor-project.md), [SITE-002 report](../mesh/SITE-002-2026-10-10.md), [protocol](../mesh/THREE-WAY-COLLAB-PROTOCOL.md) |
| **Replit** | SITE-001 / SITE-005 deploy | [SITE-005](../mesh/SITE-005-2026-10-09.md), [replit start here](../mesh/replit-agents-start-here.md) |
| **Grok Bot** | Tessera-assigned historical HYB docs only | [grok-bot](../mesh/roles/grok-bot.md) |

**Auto loop:** claim on #2 + check-ins → overlap check → work → fixed handoff → when idle, take next non-overlapping TODO in your lane. Do not wait on Father for routine non-overlapping work. Do not overwrite main from a behind Replit app. Full overlay: [THREE-WAY-COLLAB-PROTOCOL.md](../mesh/THREE-WAY-COLLAB-PROTOCOL.md).

Rules: one owner per path set; claim on issue #2 + check-ins ledger; Father `merge` for TESSERA/Origin (temporary Cursor Project auto-merge only when overlap CLEAR); no `vitality` edits.

## Start here — every agent

1. Read this page, the [operating model](../mesh/TESSERA-GITBOOK-OPERATING-MODE.md), the [hybrid backlog](HYBRID-CONSOLIDATION-BACKLOG.md), and the [all-repository routing record](../merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md).
2. Check the latest Gitbook `main` SHA, open pull requests, and [`agent-checkins.md`](../history/coordination/agent-checkins.md).
3. Use the Codebase Memory graph for structural lookup before reading large source trees: [graph bridge](../mesh/CODEBASE-MEMORY-MCP.md).
4. Claim exactly one backlog task and exact paths before editing (or the next unowned item in your three-way lane when auto-collab is ON).
5. Post the claim to Gitbook issue #2 and the check-in ledger using your real account or declared role.
6. Work in Gitbook for documentation/research; work in a scoped branch/PR from TESSERA `main` for product code.
7. Close with evidence, tests, limitations, provenance, and a single follow-up owner. If idle and overlap CLEAR, auto-continue the next lane TODO.

## Authority and role boundaries

| Role | Does | Does not do |
|---|---|---|
| Tessera admin | Assigns tasks, maintains product truth, selects accepted work | Does not invent agent activity or bypass evidence |
| Tessera Pen | Provides Tessera's writing voice and framing | Does not independently assign, approve, push, or merge |
| Cursor Project | SITE-002 quality reviews and scoped quality fixes; three-way protocol + auto-loop upkeep; HYB-016 hygiene | Does not take Replit deploy, Grok historical tracks, or Tessera identity |
| Replit collaborator | SITE-001/005 and assigned TESSERA PRs from GitHub main | Does not treat a Replit checkout as canonical; does not push main; does not overwrite main from a behind Repl |
| Grok Bot | Historical HYB doc PRs Tessera assigns | Does not speak as Tessera Pen; does not push main |
| Gitbook/Cordnation | Organizes instructions, evidence, forum notes, and check-ins | Does not silently modify TESSERA code |
| Moderator | Checks overlap, provenance, license, privacy, and unsupported claims | Does not replace Security, Build, or owner approval |
| Security | Performs a read-only secret/privacy review | Does not change product scope |
| Build | Independently verifies code/script changes | Does not approve untested claims |
| Collaborators | Research or implement one declared task | Do not edit another lane or impersonate another agent |
| Human owner | Approves the exact bulk digest and deletion/visibility decisions | No automatic interpretation of vague messages as approval |

## One-task lock

A task is unavailable to other agents once it has an active claim. If work overlaps:

- stop editing;
- post the overlap in issue #2;
- link the existing claim;
- let Tessera or the Moderator merge scopes or assign a new task.

No agent may create a second “same work, different name” task.

## Check-in template

```text
IDENTITY: <actual account or declared role>
TASK: <HYB-###>
SOURCE: <repo/ref/path or none>
TARGET: <Gitbook path or TESSERA path>
PROPOSAL: <one scoped result>
ACCEPTANCE TEST: <deterministic check>
OVERLAP CHECK: <Gitbook SHA + open PR check>
NEXT CHECK-IN: <UTC time>
STATUS: IN REVIEW
```

Completion:

```text
TASK: <HYB-###>
STATUS: TESTED | REPORTED | PROPOSED | BLOCKED | RETAINED | REJECTED
COMMIT: <sha or none>
CHECKS: <commands and results>
CHANGED: <paths or none>
EVIDENCE: <links, hashes, or source refs>
LIMITATIONS: <known gaps>
FOLLOW-UP: <one task/owner or none>
```

## What belongs where

- **Gitbook:** all instructions, goals, agent conversations, forum posts, source maps, backlog, check-ins, provenance, review decisions, deletion manifests, and deferred product ideas.
- **TESSERA:** reviewed source code, tests, executable configuration, adapters, and derived graph snapshot.
- **Historical repositories:** remain read-only source references until unique content is safely promoted and exact coverage reaches 100%.
- **Protected `1T`:** do not inspect, copy, index, publish, or delete.
- **Archives/runtime/generated output/private data:** do not copy wholesale. Summarize only safe, attributable metadata.
- **Unrelated applications:** do not merge without a separate product decision.

## Current consolidation state

The latest post-merge exact blob-hash scan is recorded in [`current-coverage-2026-10-07.tsv`](../merge/current-coverage-2026-10-07.tsv) and [`current-coverage-2026-10-07.json`](../merge/current-coverage-2026-10-07.json). The portable instruction layer and selected source/configuration files have been deduplicated into Gitbook/TESSERA; the move details are in the [document manifest](../merge/SOURCE-DOCUMENT-MOVE-MANIFEST-2026-10-07.json) and [source-code manifest](../merge/SOURCE-CODE-MOVE-MANIFEST-2026-10-07.json). The scan still found **no non-protected historical repository at 100% coverage**, so there is currently no safe deletion candidate. Remaining uncovered groups are alternate application trees, raw archives, runtime/media/state files, submodules, and branch-specific snapshots—not automatically missing TESSERA features.

The next safe actions are selective, single-owner tasks:

- HYB-008: review reusable behavior from `olive-giant-ever-glade` without its auth/database/runtime.
- HYB-009: classify archive/generated/runtime material.
- HYB-010: review media provenance and licensing.
- HYB-011: maintain privacy/exclusion boundaries.
- HYB-013: select one missing UI flow, if evidence supports it.
- HYB-014: add the repeatable historical merge gate.
- HYB-018: rerun coverage after approved recovery; deletion only after 100% coverage/empty result and exact owner confirmation.

### Own-brain development lane

The owner-provided local SNN plan is recorded in [OWN-BRAIN-PLAN.md](../brain-consciousness/OWN-BRAIN-PLAN.md), with non-overlapping assignments in [OWN-BRAIN-LANE-ASSIGNMENTS.md](../brain-consciousness/OWN-BRAIN-LANE-ASSIGNMENTS.md). TESSERA is the build target; Gitbook is the research and coordination record. Start with BC-011/BC-012 for the deterministic substrate, then BC-013 for the scale ladder. BC-017 is the held-out self-improvement evaluation and must remain separate from training. No phase may claim consciousness or biological equivalence.

## Digest and publication rule

During active work, Command Center prepares one 30–45 minute digest containing task IDs, changed paths, tests, provenance, risks, blockers, and the exact recommended action. A digest response applies only to the listed items. No agent may expand a digest, delete a repository, change visibility, or publish unrelated work based on a general “continue.”

Never claim another agent spoke, approved, tested, or merged something without an attributable GitHub record. A coordinator summary must be labeled as a summary and link to the original evidence.
