# Build gate: PR #6 (GB-018) post-merge verify — verify-only

**RESULT: PASS** · **TESTED** (all checks re-run by Build at 2026-10-05 ~3:57 PM CT via cursor-github reads + local hash-object / frozen apply; no pushes, edits, or comments)
PR: https://github.com/vitalitychems-dot/Gitbook/pull/6 ("Approved digest: GB-018")

## Merge facts
| Item | Observed |
|---|---|
| PR state | closed, merged=true, merged_at 2026-10-05T20:55:09Z (3:55 PM CT), merged_by vitalitychems-dot |
| Merge commit / main tip | `97e43fb9e74624dcb4761bc101e1518944c16ea5` (confirmed `list_commits` main HEAD) |
| Merge parents | `fd3c2ce04fa4…1ea76` (prior base) + `002591996a10…dab1c` (PR head) |
| Merge tree | `4ea36623c335ed3fe7ff8eac3db13e820dffe37b` |
| PR head tree (00259199) | `4ea36623c335ed3fe7ff8eac3db13e820dffe37b` — **identical** |
| Stat | +71/−3 across exactly 4 files |

## Checks
| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Main tip is the PR #6 merge; parents = fd3c2ce + 00259199 | **PASS** | list_commits + get_commit |
| 2 | Merge tree == verified PR head tree (no extras) | **PASS** | both `4ea36623…7b` |
| 3 | Frozen diff integrity | **PASS** | sha256 `e6242006524510333b26baf7032c4e71c882f1a712cf3f2cf4e36279e6cf4e93` = FROZEN-SHA256-f4b2c41.txt |
| 4 | Main blobs == frozen-diff-applied-on-fd3c2ce blobs | **PASS** | table below (local `git apply` of frozen on disposable fd + `git hash-object` vs tip) |
| 5 | HYB-012 / fb984ad lines intact on tip | **PASS** | agent-checkins tip blob `3708a2ab`; anchors: NEXT CHECK-IN ×2, LATEST GITBOOK BASE ×1, WAITING ON ×1, issuecomment-6002431534 ×2 (LATEST ISSUE COMMENT + FOLLOW-UP), BLOCKER ×1, `## HYB-012` ×2 |
| 6 | No TESSERA_ENABLE_* flips | **PASS** | 0 hits in frozen GB-018 and in tip's 4 GB-018 files |

## Blob table (main 97e43fb vs frozen apply on fd3c2ce)
| Path | Main blob | Applied blob | Match |
|---|---|---|---|
| SUMMARY.md | b51dc3a6fac867aa07e30e6300c2d6af1b42d176 | b51dc3a6…d176 | Y |
| history/coordination/agent-checkins.md | 3708a2abd6f9854d518d56ddd5144c3ba6ce15c4 | 3708a2ab…15c4 | Y |
| intake/HYBRID-CONSOLIDATION-BACKLOG.md | 1e805fb7e8a8c0cde2d18386fd444e44b3f03be0 | 1e805fb7…3be0 | Y |
| merge/hyb-005-braces-decision.md | e22b1e37797dd2222dff9564c5082995e839a27d | e22b1e37…a27d | Y |

Also blob-identical to prior PR head 00259199 for the same 4 paths.

## Failures
(none)

**RESULT: PASS** · TESTED
