# Build plan 2026-10-12 — repo consolidation, AgentCraft, api-anything
Every phase: Security gate → Build gate → Father bulk yes. No push/merge/delete without that. No [REDACTED-PATH] no Zz / olive-giant-ever-glade, no Claude-Red or offensive packs, no paid tools.

## Phase 0 — Find the ~300 repos (blocker)
Connected account shows 4 repos. Ask Father which other GitHub accounts/orgs/Replit hold the rest; connect read-only.
- Command Center: ask Father; record accounts.  - Security: verify each new connection is read-only.

## Phase 1 — Inventory & map (read-only)
For each owned repo: metadata, tree, languages, README, deps, secrets-scan (report only). Optional REA static JS analysis on built bundles.
Output: REPO-INVENTORY.md v2 + Gitbook "repo map" page (local first).
- Historical Analysis: per-repo role notes, duplicates, lineage.  - Security: secret/1T/PII scan, DO-NOT-TOUCH list.  - Build: classify buildable vs docs.

## Phase 2 — Consolidation proposal
Group repos into keep / merge-into-TESSERA / Gitbook docs / archive. Import via staged PRs into TESSERA (`imports/<repo>/`) preserving history where useful.
- Cordnation: sequence and assign imports.  - Build: tests per import, CI green.  - Security: per-PR gate.  - Command Center: bulk-yes list to Father.

## Phase 3 (optional) — AgentCraft visualization
Only if Father wants it: Foreman `sim` backend headless on a sandbox clone; or reimplement its task-graph view in TESSERA web app (free). Real Claude agents / Minecraft game require paid accounts → needs Father's explicit decision.
- Build: sandbox prototype.  - Security: confirm no access to real repos/tokens.

## Phase 4 (optional) — api-anything
Default SKIP. Only for a no-login public site lacking an API, in a sandbox, no cookie import.
- Security: ToS + credential review first.

## HYB task assignments
| Lane | Tasks now |
|---|---|
| Cordnation | Own phase sequencing; track board items per repo |
| Build | Phase 1 classification, test harness for imports, keep TESSERA CI green (Actions billing issue first) |
| Security | Read-only connection checks, secret/1T scans, gate each import PR |
| Command Center | Ask Father for repo accounts; compile bulk-yes lists |
| Historical Analysis | Per-repo history/lineage notes, dedupe map |
