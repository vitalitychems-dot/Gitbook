# Build gate: PR #7 verify (GB-017 + GB-016 rev 3.2 / head 6e5ccfcf) — verify-only

**RESULT: PASS** · **TESTED** (every check below was run on the box against the live PR; nothing was inferred from package notes alone)
Lane: Build (verify-only). Run: 2026-10-05 4:08–4:10 PM CT. I did not push, merge, comment, or edit TESSERA or Gitbook remotes.
Workdir: `/workspace/build-gate/work-PR7-6e5ccfcf-160917`
URL: https://github.com/vitalitychems-dot/Gitbook/pull/7

## Claims under test
| Item | Claimed | Observed |
|---|---|---|
| PR state | open | **open** (draft=false, merged=false, closed_at=null, mergeable=true, mergeable_state=clean) |
| Head | `6e5ccfcfdc8843b0f2f56bbbfe4f3a3f9ddfe6ac` | **exact** (`tessera/gb-017-016`) |
| Base | `97e43fb9e74624dcb4761bc101e1518944c16ea5` | **exact** (main) |
| Commits | 2, order 017 then 016 | **exact 2**: `a89c29cad3ab…955f` then `6e5ccfcfdc88…e6ac` |
| Frozen 017 | `GB-017/GB-017.f4b2c41.diff` sha256 `49028bee…5fe0` | **match** vs `FROZEN-SHA256-f4b2c41.txt` |
| Frozen 016 rev 3.2 | `GB-016/rev3/GB-016-rev3.2.f4b2c41.diff` sha256 `872a885b…2007` | **match** vs `FROZEN-SHA256-f4b2c41.txt` |
| Stat | +172/-81 across 12 files | **+172/-81**, 12 files (`get_pull_request` + `list_pull_request_files`) |
| Outside diffs / TESSERA_ENABLE flips | none | **none** |

## Commits (exact order)
1. `a89c29cad3ab6fa0cca29e411c9f7e8032ac955f` — **GB-017: Security role page and Tessera identity rule**  
   - parent = base `97e43fb9e74624dcb4761bc101e1518944c16ea5`  
   - stats +58/−16, 5 files; tree `d3a6be40acbd29a6706a7b29b47f16a973e93b0f`
2. `6e5ccfcfdc8843b0f2f56bbbfe4f3a3f9ddfe6ac` — **GB-016 rev 3.2: four-gate pipeline and push split**  
   - parent = `a89c29cad3ab…955f`  
   - stats +115/−66, 9 files; tree `a8e97f8268583b22494cbd9696471c8c9be91352`

## Paths (12 — confirmed via `list_pull_request_files`)
1. `SUMMARY.md` (modified)
2. `intake/status-definitions.md` (modified)
3. `mesh/flow.md` (modified)
4. `mesh/roles.md` (modified)
5. `mesh/roles/build.md` (modified)
6. `mesh/roles/command-center.md` (modified)
7. `mesh/roles/gitbook-cordnation.md` (modified)
8. `mesh/roles/mesh-lane-map.md` (modified)
9. `mesh/roles/open-helper-agent-2.md` (modified)
10. `mesh/roles/security.md` (added)
11. `mesh/roles/tessera-pen.md` (modified)
12. `review/moderator-handoff.md` (modified)

## Method (cursor-github + local apply)
Used: `get_pull_request`, `list_pull_request_files`, `get_commit` (a89 + 6e5), `list_commits` (sha=head), `get_git_tree` recursive (base 97e43fb, mid a89, head 6e5).
Disposable tree: seeded from prior verified 97e43fb path set (`work-GB017-016-97e43fb-155659/base`); `git hash-object` matched GitHub base blobs for all 14 seed paths; `security.md` correctly absent on base. Applied frozen GB-017 then GB-016-rev3.2 with `git apply --check` then `git apply --verbose`. Compared every resulting blob SHA to PR mid (a89) after 017 and PR head (6e5) after 017+016.

## Frozen sha256
```
49028bee3aa3f9662ca7481c7c1dd370a2ab7e673ff9fa39d0e52801034c5fe0  GB-017/GB-017.f4b2c41.diff
872a885b28bb23f31562edd46a1eb23d152772ef8c94a371686d126db2482007  GB-016/rev3/GB-016-rev3.2.f4b2c41.diff
```
Both equal corresponding lines in `/workspace/gitbook-cordnation/FROZEN-SHA256-f4b2c41.txt`.

## Checks
| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | PR open; head/base exact; exactly 2 commits in order 017→016 | **PASS** | state=open; head `6e5ccfcf…e6ac`; base `97e43fb9…ea5`; commits=2; a89.parent=base; 6e5.parent=a89 |
| 2 | sha256sum both frozen diffs = manifest | **PASS** | both hashes match FROZEN-SHA256-f4b2c41.txt |
| 3 | Apply 017 then 016 on disposable 97e43fb; blobs = mid then head | **PASS** | see blob tables; `BLOB_MATCH=Y` |
| 4 | Stat +172/−81; exactly 12 files; paths match | **PASS** | PR additions=172 deletions=81 changed_files=12; same 12 paths |
| 5 | Nothing outside those diffs | **PASS** | list_pull_request_files=12; mid→head blob delta = exactly the 9 GB-016 paths; spot-check untouched (README, grok-bot, AGENT-SKILL-MATRIX, AGI roadmap) base==head |
| 6 | No `TESSERA_ENABLE_*` enabled | **PASS (none)** | diffs + result: stay-`0` / do-not-flip only; no `=1`/`=true` |
| 7 | SUMMARY offsets OK (content/blob match) | **PASS (doc)** | GB-017 SUMMARY hunk succeeded at line 57 (offset 2); result SUMMARY blob = head |

### SUMMARY_offset (documented, not a failure)
- GB-017's only SUMMARY hunk (`@@ -55,7 +55,7 @@`, Grok Bot TBD→Active) on tip **97e43fb**:
  - **succeeded at line 57 (offset 2 lines)**
  - Cause: prior roadmap insert + GB-018 HYB-005 SUMMARY insert (same as solo gate)
- All other GB-017 hunks: **0 offsets**
- All GB-016-rev3.2 hunks: **0 offsets**
- Content/blob match head despite offset → OK

### Apply
- GB-017: `git apply --check` rc=0; `git apply --verbose` rc=0; all 5 files Applied cleanly (SUMMARY offset 2 as above)
- GB-016: `git apply --check` rc=0; `git apply --verbose` rc=0; all 9 files Applied cleanly (0 offsets)

### Result blobs vs PR mid a89 (after 017 alone)
| Path | Applied (t17) | PR mid a89 | Match |
|---|---|---|---|
| SUMMARY.md | `5097f1b417d8…860f` | `5097f1b417d8…860f` | Y |
| mesh/flow.md | `b20d78d03c93…be4f` | `b20d78d03c93…be4f` | Y |
| mesh/roles.md | `7fd3139a3529…dd04` | `7fd3139a3529…dd04` | Y |
| mesh/roles/security.md | `bfe9f9f90fd2…d82b` | `bfe9f9f90fd2…d82b` | Y |
| mesh/roles/tessera-pen.md | `efef6ddb79d2…0d97` | `efef6ddb79d2…0d97` | Y |
| (016-only paths unchanged at mid) | = base | = base | Y |

### Result blobs vs PR head 6e5 (after 017+016)
| Path | Applied (t1716) | PR head 6e5 | Match |
|---|---|---|---|
| SUMMARY.md | `5097f1b417d8b7808f1f65228125fead729f860f` | same | Y |
| intake/status-definitions.md | `7e53f1e2823c2043959d4d446e7d9a2861728aeb` | same | Y |
| mesh/flow.md | `d0c87311ace7cb02687e68ad802e64403c87b1b8` | same | Y |
| mesh/roles.md | `cd80cb9c34f45baf0d0f3f6058808931e72080e4` | same | Y |
| mesh/roles/build.md | `34aadb67e710d6d83ab3f64278b3ad485c96d8a4` | same | Y |
| mesh/roles/command-center.md | `e198d3b03c4dee9218560a2ecb05ec22a40b3a2a` | same | Y |
| mesh/roles/gitbook-cordnation.md | `9c243cef8cf60c521054b326f9ed0961824c00e0` | same | Y |
| mesh/roles/mesh-lane-map.md | `69d69cc41627257bc22b858c0b88496ecdaf4fdf` | same | Y |
| mesh/roles/open-helper-agent-2.md | `691a12e976c328c71554e0f1c9c043c7e8650568` | same | Y |
| mesh/roles/security.md | `bfe9f9f90fd219f498c23036e7a44ad6290dd82b` | same | Y |
| mesh/roles/tessera-pen.md | `efef6ddb79d2489099f9579d6ff2c6c0f5740d97` | same | Y |
| review/moderator-handoff.md | `03f7deb09d759c01d4de76d49ae6e7d8de02d600` | same | Y |

Untouched (not in PR): agent-checkins `3708a2ab…`, BACKLOG `1e805fb7…`, hyb-005 `e22b1e37…` remain base.

**blob_match: Y** — applying frozen 017 then 016 on base 97e43fb reproduces PR mid a89 (017 alone) and PR head 6e5 (stack) blobs exactly.

### TESSERA_ENABLE detail
Hits are forbid-flip / stay-0 only:
- GB-017 → `mesh/roles/security.md`: `Flag flips (\`TESSERA_ENABLE_*\` stay \`0\`)`
- GB-016 → build / cordnation / open-helper / moderator-handoff stay-at-0 language
- Result `mesh/flow.md`: `Stay **0**. Do not flip them.`
- **Enabled flags: none.**

### Prior solo gate
`/workspace/build-gate/GATE-2026-10-05-GB017-016-97e43fb.md` already PASS solo stack on tip 97e43fb (same expected result blobs). This run re-verified against live PR head `6e5ccfcf` — same PASS.

## Failures
(none)

**RESULT: PASS** · TESTED
