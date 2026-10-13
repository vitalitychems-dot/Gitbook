# GB-070 notes (intake log backfill for retro-review; staged locally, not pushed)

- Base: Gitbook main 243ddd4befa946674386bd3a501e314f2d894574 (PR #63, 04:10 CT Oct 13). Open PRs: #39 (Security FAIL) and #40 (draft, stale). Neither touches intake/log.md.
- GB-067 and GB-068 are already merged (PR #53 17bac6db and PR #54 8138ea2f, both 01:08 CT) and already marked published on main by PR #58. No change is needed.
- Only intake/log.md changes: 10 rows added after GB-068, and the GB-065 row updated. The old name in that row's title is existing text, left unchanged.
- Noreply author: every squash commit for #55 to #63 is authored as 332565808+…@users.noreply.github.com (verified from the main commit list). #52 is authored as Tessera with a plain email, co-authored by the noreply address.
- GitHub check runs were not queried. #55's body says CI is billing-blocked.

| Row | PR | Merge | Merged (CT) | Status | Evidence |
|---|---|---|---|---|---|
| GB-069 | #52 | 0f05d58 | Oct 12 19:55 | published | Mod + Sec PASS at 91249323 (PR body, REPORTED); Father "approve all" (REPORTED); no Build |
| PR #55 | #55 | bd1b475 | 03:28 | published | Build PASS (local build-gate/GATE-2026-10-13-Gitbook-PR55.md); Security PASS (local improvements/gates/security.md 01:59); **no Moderator record found**; Father yes not cited |
| PR #56 | #56 | 4feab77 | 02:51 | retro-review pending | Smoke test only; **no autogate or gitleaks for itself** |
| PR #57 | #57 | 1c7db22 | 03:00 | retro-review pending | git grep count; **no autogate or gitleaks** |
| PR #59 | #59 | 4dd0106 | 04:00 | retro-review pending | 13 unit tests OK; **no autogate or gitleaks** |
| GB-065 (updated) | #60 | 6b21df6 | 04:03 | retro-review pending | autogate GATE PASS #60; qlab ALL PASS; merged after the #45 Moderator FAIL |
| PR #61 | #61 | d0ee5a7 | 04:08 | retro-review pending | pytest 10/10; **no autogate or gitleaks** |
| PR #62 | #62 | dbd34db | 04:09 | retro-review pending | unittest 12/12; gitleaks clean (PR body) |
| PR #63 | #63 | 243ddd4 | 04:10 | retro-review pending | "5 checks pass"; **no autogate or gitleaks** |
| PR #58 (extra; not in the request) | #58 | 8dab9a5 | 04:01 | retro-review pending | autogate GATE PASS #58; it cites a gate file that is not in the repo |
| GB-070 | — | — | — | in review | this package |

Checks: forward apply --check OK, the result matches, and the reverse check is OK. After applying: no duplicate IDs, and every row has 12 columns.

## Rev 2 (Tessera ruling 4:25 AM CT: ledger #15 goes through the Moderator, not issue #2)

- Base: still main 243ddd4b. intake/log.md is byte-exact with main's blob.
- The intake/log.md changes are the same as rev 1, except for the GB-070 row (title and source now name the ledger).
- New file mesh/ledger/ledger-15.md. Main has no sync-ledger folder: mesh/SYNC-*.md are name-list syncs and merge/redundancy-ledger.csv is something else. So I used the fallback path. No SUMMARY line, because SYNC pages and board ledgers are not listed in SUMMARY.
- Sanitized:
  - The IDENTITY header was removed.
  - The local "READY.md" became "the Cordnation Ready list".
  - The local Build gate filename became "a Build gate file kept outside the repo".
  - A closing note now points to the intake rows.
- A scan finds no box paths, personal handles or secret-like strings. The facts are unchanged: SHAs, times, PR numbers, flags and comment ids.
- Interdiff: GB-070-rev1-to-rev2.interdiff, made by applying rev 1 and rev 2 to the same base and diffing the results. It shows only the GB-070 row and the new ledger file.
- Checks: forward apply --check OK, the result matches rev2/, and the reverse check is OK.
- Rev 1 (GB-070.diff, 2e4eec4c…) is SUPERSEDED.

## Rev 3 (Tessera ruling 4:26 AM CT: PR #55 is a partial record, not ungated)

- Base: still main 243ddd4b.
- In mesh/ledger/ledger-15.md, PR #55 moved out of "Ungated" into a new "Partial record" line. The ungated list and the problems list now say (7): #56, #57, #59, #60, #61, #62, #63.
- PR #55 evidence:
  - Moderator PASS at head 3e17e9a: PR comment 6140282455, 2:09 AM CT. I read it on GitHub.
  - Security PASS and Build PASS at the same head (local gate records).
  - Father's "Yes" at 3:27 AM CT is REPORTED by Moderator. It does not appear on the PR; the PR has only that one comment.
- In intake/log.md, the PR #55 row is now "published (partial record)". It cites the Moderator comment, and the blocker cell is now none. The row still has 12 columns.
- Interdiff GB-070-rev2-to-rev3.interdiff applies to the rev 2 result.
- Checks: forward apply --check OK, the result matches rev3/, and the reverse check is OK.
- Rev 2 (GB-070-rev2.diff, 76f09c66…) is SUPERSEDED.
