# Build gate: PR #7 (GB-017 + GB-016 rev 3.2) post-merge verify — verify-only

**RESULT: PASS** · **TESTED** (re-run by Build 2026-10-05 ~4:11 PM CT via cursor-github reads + local sha256/blob compare; no pushes, edits, or comments)
PR: https://github.com/vitalitychems-dot/Gitbook/pull/7 ("Approved digest: GB-017, GB-016 rev 3.2")

## Merge facts
| Item | Observed |
|---|---|
| PR state | closed, merged=true, merged_at 2026-10-05T21:10:21Z (4:10 PM CT), merged_by vitalitychems-dot |
| Merge commit / main tip | `ecd902211abd202711838219b28a1e1b39ae47c4` (list_commits main HEAD) |
| Merge parents | `97e43fb9e746…6ea5` (prior base) + `6e5ccfcfdc88…e6ac` (verified PR head) |
| Merge tree | `a8e97f8268583b22494cbd9696471c8c9be91352` |
| PR head tree (6e5ccfcf) | `a8e97f8268583b22494cbd9696471c8c9be91352` — **identical** |
| Stat | +172/−81, 12 files, 2 commits (a89c29ca GB-017 → 6e5ccfcf GB-016 rev 3.2) |
| Open PRs after merge | none |

## Checks
| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Main tip is PR #7 merge; parents = 97e43fb + 6e5ccfcf | **PASS** | list_commits main |
| 2 | Merge tree == verified PR head tree (no extras) | **PASS** | both `a8e97f82…1352` |
| 3 | Frozen diff integrity | **PASS** | GB-017 sha256 `49028bee3aa3f9662ca7481c7c1dd370a2ab7e673ff9fa39d0e52801034c5fe0`; GB-016 rev3.2 sha256 `872a885b28bb23f31562edd46a1eb23d152772ef8c94a371686d126db2482007`; both = FROZEN-SHA256-f4b2c41.txt |
| 4 | Main blobs == frozen 017→016 applied on 97e43fb | **PASS** | 15/15 paths match `work-PR7-6e5ccfcf-160917/meta/t1716-blobs.txt` vs main recursive tree (0 mismatches) |
| 5 | No TESSERA_ENABLE_* flips | **PASS** | 0 hits for `TESSERA_ENABLE_*=1/true` in applied result; only stay-0 / do-not-flip language |
| 6 | Prior PR #6 content intact | **PASS** | agent-checkins `3708a2ab`, BACKLOG `1e805fb7`, hyb-005 `e22b1e37` unchanged on tip |

## Failures
(none)

**RESULT: PASS** · TESTED
