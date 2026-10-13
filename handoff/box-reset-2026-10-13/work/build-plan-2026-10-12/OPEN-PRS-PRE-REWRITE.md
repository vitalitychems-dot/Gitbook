# Open TESSERA PRs: snapshot before the rewrite
Generated: 2026-10-12 19:24 CT (read-only; nothing on GitHub was changed)
Compared against origin/main: 3b3840c3789004a8d175ccf080be12f462ffd672
Method: fetched refs/pull/*/head. Files are the diff from each PR's merge-base to its head, and each file at the PR head was compared byte-for-byte with main.

Open PRs: #194, #110, #87, #82, #80. **#242 is NOT open.** It was MERGED 2026-10-12 18:40 CT (head 09ce52c8, branch cursor/civic-agent-world-3a81).

| # | Title | Head branch | Head SHA | Base | Behind/ahead main | Status | Rebase risk |
|---|---|---|---|---|---|---|---|
| 194 | Point the docs at the Gitbook consolidation map | desk/consolidation-pointer | 445dbce394f2c68f941352eee1e770bdaa190cca | main | 105 / 1 | NEEDED (1 new file, not on main) | LOW: one new doc file, no conflicts. Its text pins old SHAs (a502322, Gitbook d27e3e6), which go stale after the rewrite. |
| 110 | SITE-002: gate remaining diagnostics behind owner session | cursor/site-002-diagnostics-gate-7ea3 | 352cb5748797c5cdd997c26ec99ac164ff5cc211 | main | 293 / 1 | SUPERSEDED: code byte-identical to main | LOW: nothing to keep. Close it instead of rebasing. |
| 87 | Gate system-runtime and shadow-winning admin routes | security/gate-system-runtime-and-shadow-winners | 9b3a0931f6aac5cc8c6f0ce79a78b1c007aa68ab | main | 377 / 2 | PARTIALLY NEEDED | HIGH: see notes |
| 82 | Allow api-server to boot without a database | fix/api-server-db-optional-boot | 640bb34a7778eed47f91df16a20f9cba40764ecb | main | 379 / 3 | NEEDED (feature absent on main) | MED-HIGH: see notes |
| 80 | Add an opt-in loopback pen with deterministic gates | feat/local-pen-adapter | 1ad3ac57552f18a638bd5453551753668b5196ec | main | 340 / 9 | NEEDED (all 18 files are new; pen-local/ is absent on main) | LOW-MED: pure additions. Only package.json is shared, and main has not touched it since the base. 9 commits to replay. |

## Files and notes
- **#194**: docs/CONSOLIDATION-POINTER.md (new, 8 lines).
- **#110**: api-server/src/__tests__/sovereign-engines-session-gate.test.ts (IDENTICAL to main), api-server/src/routes/diagnostics.ts (IDENTICAL), docs/PERMANENT-SITE-RELEASE.md (differs by 1 line, and main's version is the newer one).
- **#87**: route-inventory.test.ts (main changed it 4x since base), system-runtime-admin-gate.test.ts (new), routes/governance-consensus.ts, improvement.ts, system-runtime.ts (main has no requireAdmin in any of these, so the gating is still missing), routes/sovereign-engines.ts (main has 33 requireAdmin refs vs 4 in the PR, so the PR version is stale and taking it would regress main), tessera pages ConsciousnessNexusPage (main touched it 1x), LatticeBrowserPage, SovereigntyDashboardPage, SystemPage. Its system-runtime, improvement and governance-consensus gating is still worth landing. Redo it on new main rather than rebasing.
- **#82**: api-server tests db-optional-boot (new), healthz; app.ts, index.ts, lib/db-availability.ts (new), semantic-compression.ts, routes/health.ts, routes/index.ts (main touched it 1x), inventions.ts, legacy-engines.ts (main touched it 3x, 91+/87- churn, the likely conflict), ontology.ts; lib/db/src/index.ts.
- **#80**: api-server/package.json, scripts/pen-local-gate.mjs, src/__tests__/pen-local.test.ts, src/lib/pen-local/* (15 files, all new).

## #110 verdict: the cloud pass is right (the code is byte-identical); the box pass is wrong
`git diff 3b3840c3 352cb574 -- <#110's 3 files>` gives:
```
 docs/PERMANENT-SITE-RELEASE.md | 2 +-
-- SITE-002 follow-up gates ... Healthz stays open. Landed via Cursor Project auto-merge after overlap CLEAR vs Replit SITE-001/005.
+- SITE-002 follow-up gates ... Healthz stays open.
```
diagnostics.ts and the test file show no diff. Main already landed SITE-002 (commit 57119ecf, "record diagnostics session-gate on release readiness"). Merging #110 would only delete main's provenance sentence. **Close #110 as superseded. Do not merge it.**
