# GB-066 notes (intake log backfill for PR #46 to PR #50; staged locally, not pushed)

- Base: Gitbook main 2344334e689ad8fdfc9b5c7848aa8f1fdeac6afb (PR #50 merge, 17:18 CT). Unchanged at 6:40 PM CT. Main's intake/log.md is byte-identical to the GB-063 rev 3 result.
- Number: the log goes up to GB-063 (PR #46). GB-064 is HELD (repo scan) and GB-065 is reserved (desk PR #45, ruling 6133318944), so GB-066 is next free. No PR or board comment uses GB-066.
- Open PRs: #45 (desk, still titled GB-063, ruled GB-065), #39 (GB-061 rev 2) and #40 (draft). Only #45 touches intake/log.md. Its hunk already fails on current main, because its context is the old "in review" GB-062 row and main has GB-062 published. GB-066 does not make that worse, but #45 needs a rebase either way. #39 and #40 do not touch the log.
- Only intake/log.md changes: 6 rows added after GB-062. No existing row is edited.
- GB-063 had no row of its own, so this package adds one and marks it published via PR #46.

| PR | Merge SHA | Merged (CT) | Title | ID | Gate / yes evidence | Board receipt |
|---|---|---|---|---|---|---|
| #46 | 961858fae4fa | 2026-10-12 17:12 | GB-063 rev3: intake log update | GB-063 | PR body: four gates PASS, Build rev 3 4:56 PM, Father yes 5:08 PM bulk list (REPORTED) | None from Tessera; sync ledger #12 (6133804182, Gitbook helper) |
| #47 | 78bd20c7f76e | 17:15 | Docs: rename to GitMesh | none | PR body: Father yes 5:08 PM CT (REPORTED); link check 0 broken; no gate record | Ledger #12 only |
| #48 | 71817098578c | 17:17 | O8: Offline Internet page | O8 | PR body: auto-approved under Father's 5:15 PM standing rule (REPORTED); secret grep clean; docs only | Ledger #12 only |
| #49 | 3bdcd4529b0e | 17:17 | O9: LoRa/Meshtastic research note | O9 | Same as #48 (REPORTED) | Ledger #12 only |
| #50 | 2344334e689a | 17:18 | O11: mesh/secure-mesh.md | O11 | PR body says only "Link check clean". There is NO gate, secret-grep or yes record | Ledger #12 only |

Unverifiable:
- None of the five merges has a Tessera receipt on the board. Ledger #12 says that receipt is pending.
- The Father yes times (5:08 and 5:15 PM) appear only in the PR bodies. I did not find the 5:15 PM standing rule itself on the board.
- PR #50 has no gate evidence at all.
- The author lane is not recorded for #47 to #50, so those rows say "not recorded".
- #47, #48, #49 and #50 carry no GB number. Their rows use the PR or O ids; Tessera may want GB numbers assigned instead.

Canon: GitMesh is used in all new text (the old name does not appear in the diff). No personal handles, no banners.
Checks: forward apply --check OK, the result matches proposed/, and the reverse check is OK.
