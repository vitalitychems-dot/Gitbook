# Build gate: PR #11 head baa0daeb vs frozen GB-029 rev 3 (pre-merge, verify-only)

**RESULT: PASS** · **TESTED** (every check below was run by this Build lane. Prior package gate GATE-2026-10-05-GB029-rev3-4565152.md is context only; seed tip blob and post-apply blob were re-verified here.)

Lane: Build (verify-only). Run: 2026-10-05 ~17:27–17:29 CT. No push, merge, comment, branch edit, or full clone.
Workdir: `/workspace/build-gate/work-PR11-baa0daeb/`
Cloud agent cited: bc-49fbd7d3
Frozen package: `/workspace/gitbook-cordnation/GB-029/GB-029-rev3.4565152.diff`

## Receipt (cursor-github)
| Item | Observed |
|---|---|
| PR | https://github.com/vitalitychems-dot/Gitbook/pull/11 "GB-029 rev 3: intake log backfill (PR #8, #9, #10)"; state **open**, **draft=true**, merged=false, mergeable=true, mergeable_state=**clean** |
| Head | `baa0daeb64cf78dbbba3853a617f86421764edcb` (branch `tessera/gb-029-rev3`) — exact pin match |
| Base | `45651521a137c4448673d6abfaa77e1567230f83` (main) — exact expected match |
| Counts | commits=**1**, changed_files=**1**, **+8/−4** (get_pull_request + list_pull_request_files + get_commit stats agree) |
| Commit | single parent `45651521…`; tree **`cd9cf21bddba62b0451bb972652c4df0471c81d3`**; signature verified |
| Author / committer | Cursor Agent `<cursoragent@cursor.com>` / Cursor Agent `<cursoragent@cursor.com>` (2026-10-05T22:26:16Z = 17:26 CT) |
| Co-author | **yes** — trailer `Co-authored-by: Tessera <vitalitychems-dot@users.noreply.github.com>` |
| Main tip start→end | still `45651521…` (tree `b3e423a8…`); open PRs: only #11 |

## Checks
| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Overlap / live state: main tip still 4565152; open PRs | **PASS (TESTED)** | list_commits main tip = `45651521a137c4448673d6abfaa77e1567230f83` at start and end (~17:27 and ~17:28 CT). list_pull_requests open = PR #11 only. Base has **not** drifted. |
| 2 | PR metadata: head/base/draft/branch/mergeable | **PASS (TESTED)** | get_pull_request #11: head SHA exact `baa0daeb…`, base SHA exact `45651521…`, draft=true, branch `tessera/gb-029-rev3`, mergeable=true, mergeable_state=clean, commits=1, additions=8, deletions=4, changed_files=1. |
| 3 | One commit + Tessera co-author | **PASS (TESTED)** | get_commit head: exactly one commit on PR (parent = base). Message: `GB-029 rev 3: intake log backfill for PR #8, PR #9, and PR #10` + `Co-authored-by: Tessera <vitalitychems-dot@users.noreply.github.com>`. Author/committer: Cursor Agent. |
| 4 | Diff scope: only intake/log.md, +8/−4 | **PASS (TESTED)** | list_pull_request_files: 1 file `intake/log.md`, status=modified, additions=8, deletions=4, blob sha `eee24da289936d626e4e0cba29fffe842db0cc71`. |
| 5 | Patch equals frozen + head blob | **PASS (TESTED)** | See frozen hash section below. |
| 6 | No TESSERA_ENABLE_* flips | **PASS (TESTED)** | `TESSERA_ENABLE` appears **0** times in frozen.diff, pr-github.diff, and post-apply `intake/log.md`. Enable-pattern grep (=/: 1/true/yes/on) rc=1 (no hits). |
| 7 | Tree: only intake/log.md blob changed | **PASS (TESTED)** | get_git_tree recursive base vs head: 160 entries each, truncated=false. Path diffs: blob `intake/log.md` `dec5f592…` → `eee24da…`; parent tree `intake` only. No added/removed paths. Head commit tree `cd9cf21b…`; base tip tree `b3e423a8…`. |

## Check 5 detail — frozen hash / blob identity (TESTED)
| Step | Result |
|---|---|
| Frozen file sha256 | `34285eff247dc1e7519e30eb769fcf3a5891a0879170ee2a75cb777901d7ca83` (matches pin) |
| Seed tip blob (local seed `work-PR8…/intake/log.md`) | `git hash-object` = `dec5f592cc44fdec37dd654d5eccaf25d93fb0eb` (= tip blob at 4565152) |
| `git apply --check` frozen on tip seed | rc=0 |
| `git apply` frozen | rc=0; post-apply blob **`eee24da289936d626e4e0cba29fffe842db0cc71`** |
| Head blob from list_pull_request_files / get_commit | **`eee24da289936d626e4e0cba29fffe842db0cc71`** — exact match to post-apply and prior package gate |
| Rebuild frozen-style patch (no index; empty @@ context) from base→post blobs | sha256 = **`34285eff247dc1e7519e30eb769fcf3a5891a0879170ee2a75cb777901d7ca83`** — **binary-identical to frozen** |
| GitHub PR unified diff bytes | sha256 `62f47eb1…` — differs only by `index dec5f59..eee24da 100644` line and longer `@@` context text; **hunk bodies equal** to frozen (TESTED: meta/frozen-hunks.txt == meta/pr-hunks.txt); content PASS |
| numstat | 8 added, 4 removed |

## Co-author evidence (verbatim)
```
GB-029 rev 3: intake log backfill for PR #8, PR #9, and PR #10

Co-authored-by: Tessera <vitalitychems-dot@users.noreply.github.com>
```

## Failures
None.

**OVERALL: PASS (TESTED)**
