# GB-063 notes (intake log fix-up; staged locally, not pushed)

Base: Gitbook main cd8faa0a5dfa64e69a7d0a0e179b0b60250cd5a3 (unchanged during this work). Only intake/log.md changes. The GB-062 row and the four held direct commits are untouched.

Evidence method (read-only): list_commits on main (269 commits back to Oct 5) and the list of closed PRs. Each row below has its own GB-tagged commit in main's history. Per-file contents were not diffed line by line. Ancestry of the commit tagged with that GB number is the evidence.

For changed rows: Status becomes published, the Published note is appended to the Moderator note, Reviewer is set to the merger, Check is "Commit on main history at cd8faa0 (read-only)", and Next action is none.

| Row | Commit | Route | Merged (CT) | Flag |
|---|---|---|---|---|
| GB-030 | 3b7ff6b2 | PR #14 (rebase merge, tip 9511a776) | 2026-10-06 18:55 | |
| GB-031 | 77d80370 | PR #14 | 2026-10-06 18:55 | |
| GB-032 | f49f8c46 | PR #14 | 2026-10-06 18:55 | |
| GB-033 | 8da7c4ae | PR #14 | 2026-10-06 18:55 | |
| GB-034 | 37517d60 | PR #14 | 2026-10-06 18:55 | PEN: Tessera to approve |
| GB-035 | 37cb41af | PR #14 | 2026-10-06 18:55 | |
| GB-036 | 0be7a677 | PR #14 | 2026-10-06 18:55 | |
| GB-037 | c1086269 | PR #14 | 2026-10-06 18:55 | BUILD: Tessera to approve |
| GB-038 | 9511a776 | PR #14 | 2026-10-06 18:55 | BUILD: Tessera to approve |
| GB-040 | 46654c24 | PR #15 | 2026-10-06 18:57 | |
| GB-041 | f2f4bc0a | direct push, no PR | 2026-10-06 19:19 | |
| GB-042 | a82fb6c6 | direct push | 2026-10-06 19:19 | |
| GB-043 | 9ded2208 | direct push | 2026-10-06 19:19 | |
| GB-044 | c000e6ef | direct push | 2026-10-06 19:19 | |
| GB-045 | 24eb48e6 | direct push | 2026-10-06 19:19 | PEN: Tessera to approve |
| GB-046 | 92f01e09 | direct push | 2026-10-06 19:19 | |
| GB-047 | 37f749ff | direct push | 2026-10-06 19:19 | PEN: Tessera to approve |
| GB-048 | 8261ddee | direct push | 2026-10-06 19:19 | |
| GB-049 | 0f3e1ecc | direct push | 2026-10-06 19:19 | |
| GB-050 | d24359a3 | direct push | 2026-10-06 19:19 | |
| GB-051 | f6a3cf69 | direct push | 2026-10-06 19:19 | PEN: Tessera to approve |
| GB-052 | e16bef17 | direct push | 2026-10-06 19:19 | |
| GB-053 | 35a0ecb2 | direct push | 2026-10-08 10:33 | PEN: Tessera to approve |

Direct pushes were authored by "Cursor Agent", co-authored by Tessera.

Added rows:
- GB-059: published fbb67a52, direct push 2026-10-09 03:07 CT (Cursor Agent, co-authored by Tessera).
- GB-061: in review. PR #39 is open (head 71a8c78f), not TESTED, and marked do not merge. PR #38 (rev 1) was closed unmerged.

Not added because there is no evidence: GB-054, GB-055, GB-056, GB-057, GB-058 and GB-060. There is no commit message, PR or board mention of them.

Unverified rows left as they are: none in GB-030 to GB-053. (GB-039 was already published.)

Stacking: GB-063 and GB-062 rev 2 do NOT stack in either order with plain git apply. Both touch the same hunk: GB-063 edits the GB-051 to GB-053 rows, which are GB-062's context lines. So this package also includes GB-063-on-GB-062rev2.diff, the same change rebased on top of GB-062 rev 2. It applies cleanly after GB-062 rev 2, and its reverse check passes.

## Rev 2 (Tessera ruling 3:58 PM CT: keep the Pen and Build rows)

- Base: Gitbook main d27e3e6c31d4909e23ac2937d35133bfbc6c3884. That is the PR #44 merge commit (parents cd8faa0a and 4dc54792), merged 2026-10-12 15:58 CT.
- Main matches GB-062 rev 2 (6691071e): intake/log.md, SUMMARY.md and merge/CONSOLIDATION-MAP-2026-10-12.md on main are byte-identical to GB-062/proposed-rev2/.
- Rev 2 is GB-063-rev2.d27e3e6.diff. Its content is the same as d939b37b, plus the GB-062 row set to published. The note on that row: four gates cleared; Father's yes 3:57 PM CT; Published d27e3e6 (PR #44, merged 15:58 CT; commit 4dc54792); board receipt 6132496036.
- Evidence for Father's yes: board comment 6132496036 (Tessera Admin coordinator: "Father yes 3:57 PM CT — merged GB-062 PR #44"). The PR #44 body does NOT record Father's yes. It lists the four gates as passed and still says "Do not merge", but it was merged.
- Direct-push rows (GB-041 to 053 and GB-059) say only "direct push to main, no PR". None of them claims the four gates; I checked that their notes contain no gate wording.
- Interdiff (GB-063-d939b37b-to-rev2.interdiff): both versions were applied to their bases, which are the same file (main == GB-062 rev 2 result), and the resulting logs were compared. The only difference is the GB-062 row.
- apply --check: forward OK, the result matches rev2/, and the reverse check is OK.
- SUPERSEDED: GB-063.diff (3b34baad) and GB-063-on-GB-062rev2.diff (d939b37b).

## Rev 3 (rebased onto 56a7a48d)
- 56a7a48d (HYB-016 check-in ledger refresh, Cursor Project, 4:09 PM CT) does not change intake/log.md. The log is byte-identical to d27e3e6.
- GB-063-rev3.56a7a48.diff is byte-identical to rev 2 (same sha256 f0b2eca5…). The interdiff is empty (GB-063-rev2-to-rev3.interdiff, 0 bytes).
- Forward apply --check OK, the result matches rev2/, and the reverse check is OK.
- Rev 2 (GB-063-rev2.d27e3e6.diff) is SUPERSEDED in name only. The bytes are the same.
- ID collision: open PR #45 ("GB-063: HYB-011 refresh and GitbookAI rules", 9004959b, base d27e3e6c) also uses GB-063. It touches intake/log.md (+1 row placed after the "Held, not logged" line) and edits other files too. Its log hunk conflicts with this package (both touch the GB-062 row area). One of the two needs a new number.
