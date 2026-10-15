# Tessera consolidation — status and evidence

**Date:** 2026-10-15
**Current result:** TESSERA PR #372 is merged at `564811dc5f74073802e38c701ec98b4c32402bc3`, with post-merge CI, secret-scan, and provenance runs successful. The app is not permanently deployed. Gitbook PR #123 remains open and CI-failing at its last verified head; the current documentation follow-up needs a fresh exact-head check.
**Remote snapshot:** GitHub state rechecked 2026-10-15 10:34 UTC. The exact merge, close, open-PR, and workflow receipts are appended in [REMOTE-STATE-2026-10-15.md](REMOTE-STATE-2026-10-15.md); this docs-only update advances Gitbook PR #123 and must receive its own exact-head check.
**Scope audited:** TESSERA, Gitbook, GitMesh, Box backup metadata, and the supplied directive. Replit login was not completed; the first supplied invite URL redirected to login, other invite URLs were not tested, no invite was accepted, and no Replit source was read. No separate Vitality repository content was read or changed.

## Executive summary

- TESSERA PR #372 was merged by `vitalitychems-dot` at 2026-10-15 10:25:58 UTC; merge commit `564811dc5f74073802e38c701ec98b4c32402bc3`. The six PR checks and post-merge CI, secret-scan, and provenance workflows succeeded. GitHub's `reviewDecision` field was empty; this report does not claim a submitted review. The merge was not performed by this session.
- Gitbook PR #123 was last verified OPEN at head `4a9e68ef860a1ab2bf4e713eccffea1b7e5790a4`; exact-head [CI run 38698025357](https://github.com/vitalitychems-dot/Gitbook/actions/runs/38698025357) failed JSON validity on the excluded historical artifact at line 36, column 2. The artifact and validator were not changed; owner decision and review remain required. This docs-only update needs a new exact-head run.
- The Gitbook proposal now includes a timestamped remote-state receipt, Box path/hash metadata ledger, external-source inventory, duplicate-resolution ledger, repository synchronization matrix, deployment and rollback runbooks, and blockers/owner matrix. These records do not imply CI success, review, merge, or publication.
- Prior local TESSERA focused/full applicable tests, typechecks, production build, and desktop/mobile entry-gate smoke passed on the candidate commit. The database integration suite was not run because no dedicated disposable `TESSERA_TEST_DATABASE_URL` was configured. Remote exact-head checks are separately recorded above.
- No deployment/release, protected-path edit, branch-protection bypass, repository/file deletion, archive replay, or Vitality-content transfer was performed by this session. GitHub records PR #372 merged by the repository owner; this session did not merge it.

## Implemented in TESSERA PR #372

- Corrected the registry suite to derive current real-tree locked dependency facts from package/lock evidence, while preserving fixed fixture tests; regenerated the REA registry.
- Hardened storage access so unavailable browser storage does not prevent the first-paint/theme update.
- Added the production `tessera-next.css` theme layer, locally hosted Syne and Fragment Mono fonts with their license files, and refreshed the live sidebar/key-gate identity surfaces. Existing six accent facets, legacy-name mappings, theme/font-color controls, key gate, route behavior, and redirects are retained.
- Added tests that execute theme resolution and DOM token changes; test preference persistence/events and blocked-storage fallback; verify local font/license assets and no external font URL; and derive/test the 113-entry production route manifest from current Wouter source.
- Added `plan.md` and `TODO.md` so scope and acceptance criteria are explicit. Unchecked items remain unchecked when merge or independent product decisions are still needed.

### Validation recorded on the candidate commit

| Check | Result |
|---|---|
| Focused REA, theme, and route-manifest contracts | 10 passed, 0 failed |
| Full applicable `pnpm run test` suite with Chromium | scripts 148; console 3; Gitbook MCP 30; v2 157; GitAI 28; API optional-boot 4; learning memory 5 — all passed |
| Scripts and production web typechecks | Passed |
| Full workspace production build | Passed; Vite still warns about large Chat/Three.js chunks |
| Production preview HTTP smoke | App and `/manus-routes.json` returned 200 locally and via the public sandbox URL; all three self-hosted font files returned 200 |
| Visual smoke | Reviewed actual production entry/key-gate view at desktop 1440×1000 and mobile 390×844 |
| API DB integration suite | Skipped by the repository runner: no dedicated test DB URL was configured |
| Deployment | **Not performed**; the temporary sandbox preview is not the managed production site |

The screenshots are [desktop](evidence/tessera-next-desktop.png) and [mobile](evidence/tessera-next-mobile.png). The key gate was intentionally preserved; no fake credential or route bypass was used.

## Gitbook checklist and audit outcomes

The proposed Gitbook PR adds a new blocked follow-up (**HYB-026**) after the local Gitbook queue gate test exposed five failures: cases for enabled/changed gate flags, unlisted-host detection, code-tamper detection and rogue-flag reporting. These tests exercise CODEOWNERS-protected `mesh/queue/` paths. No protected implementation was changed; the owner must review and authorize any fix.

The Gitbook checkout was sparse. Its full local CI script stops at an absent tracked `.codebase-memory/artifact.json`. That file was not fabricated or opened. The independently runnable shepherd suite passed 13/13 and scoreboard tests passed 5/5; `test_spawn` failed five assertions. Changed Markdown passes whitespace and relative-link checks. GitHub CI was pending at that earlier local-audit snapshot; the 2026-10-15 exact remote result is recorded in the linked state receipt.

Cross-repository dispositions from the audits:

- **Box backup:** partial, dated provenance—not an implementation source. Do not replay bundles, patches or WIP. The corrected public index contains 455 path/hash/size rows and withholds 21 names. Six safe exact-blob matches to current main trees are documented; they are not confirmed moves and no Box file was deleted. The prior audit screened 355 safe eligible text/log/patch/plan/verification files, but does not map every review to a current TSV row.
- **GitMesh:** retain as a standalone public proposal room/manual intake surface. No trusted runtime, admission/auth source, or automated TESSERA bridge is implemented or added. The 22-file/44-commit count describes the 2026-10-14 audit snapshot; the new local-vault and source-sync proposal was reviewed separately in its dated addendum and is not approved for integration.
- **Legacy UI/theme PRs:** TESSERA #367 is now closed unmerged; PR #361 remains open and conflicting, with 201 reported changed files and 60,774 deletions. Its path metadata includes deletions of active app/preview UI; its diff exceeds the GitHub 20,000-line limit and was not fully reviewed. No file deletion was performed by this work. Preserve preview, console, mockup, archives, production routes, and the current key gate until replacement/consumer/rollback evidence is complete.
- **Other Gitbook tasks:** media provenance and privacy/exclusion work remain open because source repositories are unavailable locally; repository deletion remains blocked pending fresh exact-coverage evidence and explicit approval; permanent-site publication is blocked, with no current release, deployment, Pages site, host/project, URL, or rollback target verified.
- **Pen / claimed independent identity:** deferred. There is no approved product brief/data contract or evidence-backed independent identity, authorship, external action, or authorization capability. The UI must not simulate any of those claims.

## Current remote status and next steps

1. TESSERA PR #372 is already merged by the repository owner at `564811dc5f74073802e38c701ec98b4c32402bc3`; its post-merge CI, secret scan, and provenance workflows succeeded. Complete only the remaining product acceptance checks, including the API DB integration suite with a dedicated disposable database. Keep PR #361 unmerged while conflicting; reconcile the UI-retirement scope and review its exact active-path effects before any deletion.
2. Keep [Gitbook PR #123](https://github.com/vitalitychems-dot/Gitbook/pull/123) unmerged until its protected JSON-scan owner decides HYB-027 and the final exact head passes CI and review. At the last pre-follow-up check, run 38698025357 failed on the historical JSON artifact; this documentation update requires a fresh exact-head result. Route HYB-026 to the protected queue-gate owner and HYB-028 to the user for exact destination/scope.
3. Run the DB integration suite only with a dedicated disposable test database.
4. Publish through the managed-site release path only after its release checklist, security review, and owner approval. Local build/HTTP evidence is not publication.
5. Do not delete the Gitbook repository or old UI/archive surfaces based on this local test pass. The repository records Gitbook as the coordination/provenance source of truth, and the user-specified “after proven” condition is not satisfied until reviewed/merged exact-head work and successful release validation exist.

## Audit reports

- [TESSERA application audit](audits/tessera-application-audit.md)
- [Gitbook coordination audit](audits/gitbook-coordination-audit.md)
- [GitMesh integration audit](audits/gitmesh-integration-audit.md)
- [Box recovery audit](audits/box-recovery-audit.md)

The audits preserve their evidence limitations; they do not claim every past conversation, unavailable repository, excluded protected artifact, or separate external log was accessible or reviewed.


## Status update — 2026-10-14 16:53 CT

- TESSERA PR #372: all six GitHub checks are **SUCCESS**, but the PR remains **OPEN / UNMERGED** with no recorded review decision or merge commit. TESSERA issue #369 remains open.
- Gitbook PR #123: its required CI check **FAILED**. The job stopped in JSON validation on the existing handoff artifact `handoff/box-reset-2026-10-13/files/workspace/build-gate/work-TESSERA-PR2-postmerge-50876d40/runs.json` (`Extra data: line 3 column 1`). This failure is in an existing historical evidence file, not the newly edited Markdown. Preserve the source evidence; resolve it through an explicit repository-owner decision before claiming Gitbook CI success. Gitbook issue #2 remains open.
- I have now attached this report, the full safe audit reports, the TESSERA plan/TODO, and desktop/mobile screenshots to the Gitbook handoff branch for PR #123, with an index for future agents.
- The gate reads the backend secret `TESSERACT_ADMIN_KEY`; the browser submits it to `/api/admin/session`, which issues an HttpOnly session cookie on success. It must be stored server-side by the selected host—not committed, copied into browser configuration, or sent in chat. I have not collected or installed the new value.
- Hosting is still unresolved: the current task has GitHub connected, but no existing Manus Webdev project resource/declaration. Vercel, Netlify, Render, and Cloudflare integrations are disabled. Tessera is not a static-only site: its production route requires the Node API server and a protected server-side secret. No permanent deployment has been created.


## Latest correction — 2026-10-14 16:58 CT

TESSERA PR #372 has six successful required checks but still has no recorded review decision or merge. The prior Gitbook PR #123 CI failure was traced to an Actions API JSON response with an appended HTTP `Link` pagination header. The Gitbook review branch now preserves the exact 81,798 original bytes in `runs.json.raw.txt`, leaves the exact valid JSON response body (six entries; `total_count` 8 with a page-2 link) at `runs.json`, and adds `runs-evidence.md` explaining the provenance. Local JSON parsing, byte-preservation assertions, and `git diff --check` pass. A new remote full CI run is still required; the protected queue-gate tests are a separate known blocker. No PR has been merged and no permanent website or key has been configured.


## Latest external-status update — 2026-10-14 18:22 CT

The new Gitbook PR #123 head `4dccca895e296776ba4aa5f459b3d42abe04be1f` failed CI run [38644541275](https://github.com/vitalitychems-dot/Gitbook/actions/runs/38644541275). The raw-preserving `runs.json` correction got past the earlier JSON error, and the validator then stopped on `handoff/box-reset-2026-10-13/work/build-plan-2026-10-12/FULLPICTURE-LOADED.json` at line 36, column 2 (`Expecting property name enclosed in double quotes`). The manifest contains Vitality repository metadata; the user-directed destination is not identified among the authorized selected repositories, so I did not edit, copy, or move it. HYB-027 and HYB-028 record the blocked decisions; HYB-026's five protected queue tests remain separate.

At the pre-merge observation, TESSERA PR #372 was still open with six successful checks. GitHub now records it merged at `564811dc5f74073802e38c701ec98b4c32402bc3`; the post-merge CI, secret-scan, and provenance runs succeeded, but no permanent website, external hosting account, or server secret is configured. The repository's `.replit` declaration is not proof of a deployed or authenticated Replit project, and GitHub Pages is not enabled. No hosting change was made. `TESSERACT_ADMIN_KEY` was not provided or stored; it belongs only in the chosen host's server-side secret store. Do not ask for it in chat.


## Remote reconciliation — 2026-10-15 06:40 UTC

This is a historical pre-merge snapshot. The 10:34 UTC remote follow-up below supersedes the TESSERA PR #372/#367 states and repository tips.

- **TESSERA PR #372** is still OPEN/MERGEABLE at exact head `56c54a7150c1f4dcd5a041947302c40e6225b91e`; the six checks `validate`, `diff-scan`, `gitleaks`, `collect`, `author-check`, and `ready-for-gate` are SUCCESS. There is no submitted review/review decision, merge SHA, release tag, or deployment. TESSERA issue #369 remains open.
- **Gitbook PR #123** is still OPEN/MERGEABLE at exact head `f80f3a5eeb63fe3d7de8359bfa720c4e43dfe8e6`, with no review decision. Current run [38653862921](https://github.com/vitalitychems-dot/Gitbook/actions/runs/38653862921) fails JSON validity on the historical `FULLPICTURE-LOADED.json` path at line 36, column 2. The file contains Vitality metadata; this refresh did not open, alter, copy, delete, or transfer it. HYB-027 remains blocked on the protected JSON-scan owner; HYB-028 remains blocked on the user's exact authorized destination and scope.
- GitHub reports no TESSERA/Gitbook deployments, releases, Pages site or repository rulesets; the classic branch-protection endpoint returns 404. These API results do not waive the instructed human/owner review. No production host/project or URL exists.
- GitMesh `main` is `951acb79a7825fff181617fa48d5d37270418ea3`; every fetched work ref is ancestral. Its local-vault CLI was reviewed as a separate proposal, not run or copied. Its GitHub source-sync script writes allowlisted files directly to `main`, so it is not approved as a synchronization path under this governance.
- Box branch `files` is `46baaf7d87e41ee89555c61617a8e31c1d35bdc9`; its tree is catalogued as metadata in the Box intake TSV. The prior 355-file safe-screened review is retained as prior evidence but not presented as a per-file current certification; no remaining candidate is approved for replay.
- New handoff artifacts include the remote-state receipt, external-source inventory, Box ledger/index, duplicate ledger, repository sync matrix, deployment and rollback runbooks, and blocker/owner matrix. This documentation remains a PR proposal and is not merged or CI-green.
