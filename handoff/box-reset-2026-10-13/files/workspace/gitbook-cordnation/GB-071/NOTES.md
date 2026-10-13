# GB-071 notes (intake backfill; staged locally, not pushed)

- Base: Gitbook main aa9506f59aa7 (PR #65 merge, 07:20 CT Oct 13). Main's intake/log.md is byte-identical to the GB-070 rev 3 result.
- Read through the GitHub API only (PR list, commit list, file contents, PR comments). No clone. Work was done in /tmp/gb071, deleted afterwards. This folder holds only GB-071.diff, NOTES.md and SHA256.txt.
- Only intake/log.md changes: 8 rows changed and 4 added. After applying, every row has 12 columns and there are no duplicate IDs.

| Row | Change | Evidence |
|---|---|---|
| GB-070 (PR #65) | in review → published | On PR #65: Security PASS 6144484215, Moderator PASS 6144572456 and 6144738347, Build PASS 6144981113, all at 5e437c30 and relayed by Tessera; Tessera PASS in the body. Build noted 0 CI checks. Silence-timer merge with 0 checks is REPORTED by Tessera, since fixed. Merged aa9506f, 07:20 CT |
| PR #56, #57, #59, #61 | retro-review pending → published (retro PASS) | Moderator retro verdict, REPORTED |
| GB-065 (#60), PR #62, PR #63 | → retro FAIL; fix held | Moderator retro verdict, REPORTED |
| PR #64 (new) | retro-review pending | Body only: "Approved by Father" (REPORTED). No gate lines, no comments. A Security FAIL on efcca741 is reported in the PR #76 body |
| PR #70 (new) | retro-review pending | Body says it needs Security PASS and CI before merge; no PASS visible, no comments. Merged 06:00 CT |
| PR #77 (new) | published (partial record) | Moderator FAIL 6144829782 at 46dace81, then Moderator PASS 6144864716 and Security PASS 6144888286 at b3593ac2. No Build record |
| GB-071 (new) | in review | this package |

Missing evidence:
- #64: no gate record at all.
- #70: no Security PASS or CI record, although its body required both.
- #77: no Build record.
- The Moderator retro verdicts (#56 to #63) are not on the PRs I read. They are REPORTED. The source is probably the mesh/HANDOFF.md edit in #70; I did not re-read that file.

Conflict: the task says the fix PR for #60, #62 and #63 is held. But PR #70 ("Moderator retro fixes for #60, #62, #63") MERGED at 06:00 CT with no gate record. I wrote "fix held" as instructed. Tessera should say which fix PR is held: possibly #76, which is open and addresses the Security FAIL on #64, #56 and #62.

No other merged PRs since #63 lack a row. #64, #65, #70 and #77 are the only merges. #66, #69, #73 to #76 and #78 to #87 are open or closed unmerged.

Checks: forward apply --check OK, the result matches, and the reverse check is OK.

## Rev 2 (current), from Tessera's ruling at 7:42 AM CT (REPORTED). Rev 1 (GB-071.diff, b8e8d6ac) is SUPERSEDED.
- Base is still main aa9506f5, re-read through the API. GB-071-rev2.diff: 34 lines, intake/log.md +12/−8.
- PR #64, #70, #77: status set to "merged, ungated, retro-review". Evidence notes unchanged.
- GB-065 (#60), PR #62, PR #63: "fix held" is now "fix held in PR #76 @ba230b90 (locked paths; needs Security+Moderator+Build PASS and Father's collink1007 review)". This is in the status, the evidence note and the next-step column. That resolves the rev 1 question about which fix PR is held.
- Canon flag: the ruling puts the login "collink1007" in repo text. Moderator should confirm that a login is not a banned personal handle.
- Interdiff GB-071-rev1-to-rev2.interdiff: 30 lines, 6 rows changed, nothing else.
- Checks: forward and reverse apply --check OK; the result matches; all rows have 12 columns; 0 duplicate IDs. Work was done in /tmp/gb071r2, deleted afterwards.

## Rev 3 (current): Moderator CHANGES NEEDED at 7:44 AM CT. Rev 2 (022a4cbf) is SUPERSEDED.
- Base is still main aa9506f5, re-read through the API. GB-071-rev3.diff: 35 lines, intake/log.md +13/−8. Interdiff from rev 2: 31 lines.
- GB-065 (#60), PR #62, PR #63: status is now "retro FAIL; fixed by PR #70 (itself merged ungated; retro FAIL 6145821175)". The #76 wording is removed. The #56–#63 verdicts stay REPORTED.
- PR #64: "merged, ungated, retro-review", citing Moderator post-merge retro FAIL 6145820919.
- PR #70: same status, citing retro FAIL 6145821175.
- PR #77: "published (partial record)", citing Moderator PASS 6144864716 and Security PASS 6144888286 at b3593ac2. No Build record.
- PR #76: new row, "open, held". Head ba230b90; Moderator locked check 6145821453; held for Father's collink1007 review, a rebase and CI.
- Comment ids verified by API reads (comment lists on PRs #64, #70, #76 and #77): 6145820919 (#64), 6145821175 (#70), 6145821453 (#76), 6144864716 and 6144888286 (#77). All exist. 6145821453 is a PR comment, not a check run; the head has 0 check runs.
- Checks: forward and reverse apply OK; 12 columns on every row; 0 duplicate IDs. Temp dir /tmp/g3 deleted.
