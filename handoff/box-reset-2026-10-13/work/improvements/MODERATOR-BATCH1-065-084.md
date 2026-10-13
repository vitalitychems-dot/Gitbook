# Moderator gate: improvements batch 1 add-on (IMP-065 to IMP-084)

IDENTITY: Moderator gate (Grok Bot executor)
Reviewed: 2026-10-05, ~5:45 to 5:48 PM CT
Bases (TESTED via GitHub API reads): TESSERA `5c1137faeb7714482add93c2d6876396f34f1a03`; Gitbook `bc6b32871faed56b13df3dfadc849ec725d60f14`
CI: run 37382015797 / job 112006094090 (validate) on head 5c1137fa: **success**. Log shows API vitest "Test Files 14 passed (14)" and "Tests 99 passed | 1 skipped (100)" (TESTED)
Results file: `gates/moderator.md` (appended lines 65–84; lines 1–64 unchanged, checked by diff)

## Totals (065–084)

- **PASS = 19**
- **FAIL = 1**

## FAIL IDs

| ID | Reason |
| --- | --- |
| IMP-076 | Wording problem: the change would rewrite provenance. In `merge/hyb-005-braces-decision.md`, L7 `**Base:** TESSERA fec56eb · Gitbook 6fe412f` is the base the decision was made against. The page's Evidence section cites the lockfile and CI runs at fec56eb. Swapping in 5c1137fa would make the record claim evidence it never had. This is the same reason IMP-037 failed. Suggested rework: keep the Base line and add a separate line such as `**Current main:** TESSERA 5c1137fa (narrow ignore landed)`, or fold this into IMP-030's Follow-up #1 checkbox. It is not a duplicate of IMP-030; the failure is about wording and provenance only. |

## Soft notes (non-blocking)

- **IMP-024 / IMP-066 / IMP-084:** all three edit `docs/migration-review/VALIDATION.md`. IMP-024 (which passed earlier) already covers the advisory and green-run wording. IMP-066's distinct part is the storefront/Vitality Supply builds and 437-test totals; IMP-084's is the L10 claim that CI has not run. Make one edit together. This report is dated "Checked: 2026-10-02", so add a dated addendum or "superseded" notes rather than rewriting the 2026-10-02 lines in place. IMP-084 already says to keep the historical context.
- **IMP-065 vs IMP-038:** distinct, as instructed (braces/ignore bullet L8 vs CI narrative L9). Same file, so batch them together.
- **IMP-068:** the audit page is a dated record of what was fixed in that pass. Prefer annotating L11 as superseded by the current flow.md Push authority (1) (Tessera opens the PR, Build verifies, Tessera merges after Father's yes; Father may still push) over silently rewriting it.
- **IMP-069:** labels only; behavior and content stay unchanged. `TESSERA_SYSTEM.md` also documents Father-key and admin-key flows. Do not add or echo any key values while editing.
- **IMP-071 / IMP-072:** related but distinct (new docs/eval/README vs a root README pointer); cross-link them. The ledger path `scripts/eval-chatbot.ts` is really `artifacts/api-server/scripts/eval-chatbot.ts`. The README text should say that eval-chatbot needs a running API and `run-eval` needs a build and a database (eval-runner imports `@workspace/db`).
- **IMP-073:** `eval-chatbot.ts` calls `main()` at module top level, which does network fetches and can call `process.exit`. Exporting `CASES` alone would make a vitest import run the network harness. Move `CASES` into its own module (for example `eval-cases.ts`) or guard `main()`; otherwise the "no network" claim fails at implementation time.
- **IMP-083:** the four OS metrics are separate private functions (`testProcessMemory`, `testCPULoad`, `testOSFreeMemory`, `testUptimeStability`). The module imports `@workspace/db` at L1, so an offline test needs the scoring extracted or the db module mocked. The row already allows "extracted".
- **IMP-081:** every number in the filled dashboard must be TESTED (cited claims, check-ins, PRs). No invented counts. Mark it REPORTED where a count cannot be verified.
- **IMP-074 / IMP-075 / IMP-082:** these target distinct orphan sets (`history/source-index/` z-files, `history/handoffs/` notes, `history/recovered/` subtree). They are not duplicates. SUMMARY edits from 074 and 075 should land together.
- **IMP-078 vs IMP-035:** both add a Start-here step to the Gitbook README but link different targets (HYB backlog vs HYB-005 decision). Distinct; one edit.
- **IMP-080:** besides the duplicate credentials block, `_evolutions/` and `.local/` also appear twice in `.gitignore` (Replit and runtime-store sections). That is optional extra cleanup; the deduplication must not drop any pattern.
- **IMP-069 evidence:** the AGI Training line was confirmed by string, not by exact line number. All other cited line numbers matched on tip (validation L8, VALIDATION L9/L10/L15–16, CONSOLIDATION L3/L41, audit L11/L25, hyb-005 L7, consolidated-todo L15, SNN L5–7, .gitignore L75/L85, package.json L11, eval-runner L7/275/298/321/343).
- **Forbidden scan:** no row flips `TESSERA_ENABLE_*`, touches secret values, wallets, payments, or blockchain, opens 1T, deletes data, or edits `.github/workflows/*`. IMP-080 edits the root `.gitignore`, not a workflow.
- Known relationships from the brief were applied as instructed: 068/050, 065/038, 066/084, 076/030, 077/029, 079/026.

## Scope confirmation

- I did not edit `LEDGER.md`. My only writes were the appended lines 65–84 in `gates/moderator.md` and this file.
- No GitHub writes. Every call was a read: get_file_contents, get_git_tree, get_repository, search_repositories, list_workflow_run_jobs, get_job_logs.
