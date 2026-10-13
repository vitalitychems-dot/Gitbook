# Deletion list — 2026-10-13 (PROPOSAL ONLY, nothing deleted)

Rule (Father, 7:47 AM CT): delete only (a) duplicates, (b) things that can't serve us or be fixed, (c) things that lower performance. KEEP anything we can build on or improve.
[REDACTED-PATH] never touched. No locked paths or Moderator rules in this list. Disk: 98G/125G (78%), 28 GB free when checked at 7:48 AM CT.
Earlier draft saved as deletion-list-2026-10-13.prev-0747.md.

## Items to delete (once Father says yes)
| # | path | size | cat | reason | canonical / archive |
|-|-|-|-|-|-|
| 1 | /tmp/t299 | 1270 MB | a | clean clone of PR #299 (already merged); nothing dirty or unpushed | origin/ci/fix-v2-history-and-db-env @9de9f876 (tree 9eb3c410); sha256 not needed because git hashes it |
| 2 | /workspace/fatherlogin-fallback/TESSERA | 4 MB | a | clean clone; nothing dirty or unpushed | origin/followup/fatherlogin-fallback @80c85e0c (tree 8b794baa) |
| 3 | /workspace/fatherlogin-fallback/Gitbook | 3 MB | a | clean clone; nothing dirty or unpushed | origin/followup/fatherlogin-fallback @48f75322 (tree 5a81fd81) |
| 4 | 33 stale gate scratch dirs: build-gate/work-* (21), security-gate/work-* (5), gitbook-gate-* (7) | ~13 MB | b | snapshots of PRs that were already gated or merged; no git remote, can't be fixed or reused | archive: archive-before-delete/stale-gate-scratch-2026-10-13.tar.zst, sha256 6b812b4239314cc25713be5b1079a2c54bda184eeb76a8cb598c7f0549536003 (includes the dirty files from 4 gitbook-gate dirs) |
| 5 | TESSERA repo: archive/from-gitbook/archive/moved/* copies (86 groups) | 3.47 MB | a | byte-identical blobs (same git blob SHA) | TESSERA archives/source-repositories/* ; remove through a gated PR |
| 6 | Gitbook repo: duplicate archive trees (1843 groups) | 18.4 MB | a | byte-identical blobs | first copy of each group, per repo-dups-Gitbook.json; remove through a gated PR |

**Totals: 6 items (item 4 covers 33 dirs). Box: ~1.29 GB freed. Repos: ~0.022 GB. Total: ~1.31 GB.**

## Excluded under "can be built on / still serves us" (KEEP)
- The 22 a2 clones/worktrees in the prev draft (~56 GB: build-gate/tessera, si/gb, si/tsr, tess-opt, tv3, tw, einstein/*, gitmesh/repo, rea-batch/*, tb3, codeowners-followup/*, fix-agent-login, /tmp/tess, repo-lab/crewAI, sec-retro): they are dirty or have unpushed commits, which is live work. Each one becomes an (a) duplicate once its owner pushes. That is the big win (gitmesh/repo alone has ~6.2 GB of dup content).
- /home/box/.cache (740 MB): it makes installs faster, so it helps performance.
- node-v22.20.0 in si/ and build-gate/: NOT exact duplicates. The si/ copy has lib/npm and the build-gate/ copy does not; only bin/node matches (sha256 b1cbec89…). Both may be in use.
- TESSERA artifacts/mockup-sandbox/src/components/ui/* (same as artifacts/tessera ui): this sandbox is meant to be built on.
- TESSERA theme files (4) and the 8 "intentional" groups (LICENSEs, test fixtures): live code or kept on purpose.
