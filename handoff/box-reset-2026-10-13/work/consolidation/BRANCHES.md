# BRANCHES — merged status and safe-to-delete plan

As-of: 2026-10-05 ~6:00 PM CT. TESTED via `list_branches`, `list_commits` (ancestry and ahead/behind), `list_pull_requests state=all`, and tree comparison.
**Plan only. No branches have been deleted.** A branch is SAFE-TO-DELETE when it is fully merged (its tip is in default-branch history, or its squash-merged tree is identical to a main commit), has no open PR, is not the default branch, and is not protected. Times are CT.

## TESSERA (default `main`)
| Branch | Tip | Merged into main? | Ahead/behind | Last commit (CT) | PR | Verdict |
|---|---|---|---|---|---|---|
| main | 5c1137fa | — | — | Oct 5 | — | KEEP (default) |
| cursor/hyb-005-audit-ignore-943c | 76716c22 | yes, tip is in main history | 0 ahead | Oct 5 4:57 PM | #1 merged | **SAFE-TO-DELETE** |
| tessera/hyb-012-route-inventory | cb19f210 | yes, squash #2 → 50876d40, tip tree 42fb940d == main commit tree | 0 ahead (by content) | Oct 5 5:14 PM | #2 merged | **SAFE-TO-DELETE** |
| tessera-pen-gate | 41e702ce | **no** | 1 ahead / 8 behind | Oct 5 12:01 PM | none | KEEP until CONS-001 is done |

## Gitbook (default `main` bc6b3287)
| Branch | Tip | Merged? | Last commit (CT) | PR | Verdict |
|---|---|---|---|---|---|
| cursor/ready-batches-003-009-9e09 | 80106264 | yes (in main) | Oct 5 8:25 AM | #1 merged | **SAFE** |
| cursor/hyb-006-grok-ready-b214 | 4da54d5a | yes | Oct 5 1:34 PM | #3 merged | **SAFE** |
| cursor/hyb-007-z-app-5404 | 580a3dc3 | yes | Oct 5 1:50 PM | #4 merged | **SAFE** |
| tessera/gb-015-019-021-020 | 91068166 | yes | Oct 5 3:43 PM | #5 merged | **SAFE** |
| tessera/gb-018 | 00259199 | yes | Oct 5 3:52 PM | #6 merged | **SAFE** |
| tessera/gb-017-016 | 6e5ccfcf | yes | Oct 5 4:07 PM | #7 merged | **SAFE** |
| tessera/gb-022-024-025-023 | cba4140d | yes | Oct 5 4:27 PM | #8 merged | **SAFE** |
| tessera/gb-026-027 | b23d9eb8 | yes | Oct 5 4:50 PM | #9 merged | **SAFE** |
| tessera/gb-028 | c507f0c2 | yes | Oct 5 4:55 PM | #10 merged | **SAFE** |
| tessera/gb-029-rev3 | baa0daeb | yes | Oct 5 5:26 PM | #11 merged | **SAFE** |
| tessera-consolidation-draft | db5b0a18 | **no** (1 ahead of 80106264) | Oct 5 12:01 PM | none | KEEP until CONS-002 is done |
| main | bc6b3287 | — | — | — | KEEP (default) |

## Grok-ready (default `main` 9e3fbca2)
| Branch | Tip | Merged? | Last commit | PR | Verdict |
|---|---|---|---|---|---|
| migration/source-omission-review-20261002-1790942612150 | 52fd4369 | yes (in main) | Oct 2 | #2 merged | **SAFE** |
| maintenance-redact-user-pasted-filenames-20261002 | 81d7ef1a | no | Oct 2 | **#3 open** | KEEP (CONS-010/011) |
| migration/approved-archive-chunks-20261002 | f0e69e90 | no | Oct 2 | **#4 open** | KEEP. Private ZIP chunks, do not import (CONS-011) |
| migration/amber-flame-tiger-sand-review-20261002 | 075ef226 | no | Oct 2 | **#5 open** | KEEP. Unlicensed third-party code plus a withheld credential-pattern blob (CONS-011) |

## Zz (default `main` ec2118d6)
| Branch | Tip | Merged? | Last commit (CT) | PR | Verdict |
|---|---|---|---|---|---|
| replit/cl1-offline-mock | 150d4ec0 | yes (ancestor of main; main is 2 ahead) | Oct 3 9:15 PM | none | **SAFE** (first confirm no Replit workspace tracks this branch) |
| chamber/desk | a06c9f51 | **no** (1 ahead; note blob differs from the Gitbook copy) | Oct 3 1:32 PM | none | KEEP until CONS-003 is done |

## `1` (default `main` 3bad9785)
| Branch | Tip | Merged? | Last commit (CT) | PR | Verdict |
|---|---|---|---|---|---|
| subrepl-nftoz8d7 | 7de2b4a7 | **no**, unrelated history | Oct 5 4:38 PM (live Replit) | none | KEEP / PROTECTED (natal-vault, CONS-018/019) |

## Single-branch repos (default only, nothing to delete)
5t, T44, TESS, tessera-grok-handoff, tessera-grok-handoff-complete, tessera-complete-archives (`main`); olive-giant-ever-glade (`cycle/chamber-text`). TESTED.
`1T`: **not inspected** (PROTECTED).

## Safe-to-delete branch counts
| Repo | SAFE | KEEP (non-default) |
|---|---:|---:|
| TESSERA | 2 | 1 |
| Gitbook | 10 | 1 |
| Grok-ready | 1 | 3 |
| Zz | 1 | 1 |
| 1 | 0 | 1 |
| others (8 incl. 1T unchecked) | 0 | 0 |
| **Total** | **14** | **7** |

Pre-step before any branch delete: re-run `list_branches` and `list_pull_requests`, and confirm each tip SHA still equals the one above. If a SHA has moved, skip that branch.
