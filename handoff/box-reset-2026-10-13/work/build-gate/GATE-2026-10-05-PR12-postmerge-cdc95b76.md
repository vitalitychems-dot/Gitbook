# Build gate — Gitbook PR #12 post-merge check @ cdc95b76

**Date:** 2026-10-05 ~6:05 PM CT
**Mode:** verify-only. Nothing was pushed or merged, no GitHub comments were posted, LEDGER.md was not edited, and no flags were changed.
**Repo:** vitalitychems-dot/Gitbook, branch `main`
**Method:** cursor-github MCP (`list_commits`, `get_git_tree` recursive, `get_file_contents`, `list_pull_requests`). Working files are in `build-gate/work-PR12-postmerge-cdc95b76/`.

## OVERALL: PASS (TESTED)

| # | Check | Result |
|---|---|---|
| 1 | main tip SHA | `cdc95b76232ee066d6c55d0531b02d88426f4beb`, matches expected. PASS |
| 2 | Merge shape | True merge commit (not a squash). Parents: `bc6b32871faed56b13df3dfadc849ec725d60f14` (pre-merge base) and `64778b33dacdff02434c7effd2d2b9441586f966` (pre-merge PASS head). Commit is GitHub-signed (verified: true). PASS |
| 2b | Tree vs head 64778b33 | **Equal.** Both use tree `5b81e836c17eb0cb43cf35527f259b3cd19cc81f`, so nothing was added at merge time. PASS |
| 3 | Open PRs | 0 |
| 4 | SUMMARY.md at tip | 79/79 relative entries resolve to blobs in the tip tree. The entry list matches pre-merge `summary-paths.txt` exactly. PASS |
| 5 | Link spot-check | SUMMARY.md 79/79. `merge/HYB-011-EXCLUSION-MANIFEST.md`: 1/1 relative link resolves (`DELETION-MANIFEST.md` → `merge/DELETION-MANIFEST.md`). `mesh/HANDOFF.md`: 0 relative links; all 13 links are external issue #2 comment URLs and were not fetched. **0 broken.** PASS |
| 6 | Forbidden paths | The tip tree (162 entries, 130 blobs, not truncated) has no `.github/` path, no `.github/workflows`, no wallet path, and no `.env`, `.pem`, `id_rsa`, or `.key` file. One name-match exists: `history/recovered/source-versions/tessera-unified/docs/SECRETS.md`. It is a pre-existing recovered doc that was already in base bc6b3287 and was not touched by PR #12. Not new. PASS |

## Notes
- The merge message reads: "Merge PR #12: list 1 Gitbook items (Father yes 5:54 PM CT; Security+Build PASS @64778b33)". Author is Tessera. Committed 2026-10-05 6:04:56 PM CT.
- Because the tree is identical, the pre-merge gate (`GATE-2026-10-05-PR12-64778b33.md`) applies to the tip unchanged, including 31/31 PR-added links. The cosmetic note about 4 trailing-two-space lines still applies.
- Board receipt (FYI, not re-read): https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6005027503
