# GB-023: intake log backfill

**Base:** ecd9022 + GB-022 v4 + GB-024 v3 + GB-025. Stacks last.
**Package:** `GB-023.ecd9022.diff`: 76 lines, 4 files, 4 hunks, +25/−14.
**Depends on GB-022:** GB-022 adds the Reviewer / Check / Next action / Blocker columns and changes the front matter to published. GB-023 applies on ecd9022 + GB-022 alone (rc=0) but not on bare ecd9022 (rc=1, `intake/log.md`).

## intake/log.md
- **GB-004 to GB-014:** status changed from `approved` to `published`, with "Published 8010626" appended. Commit 8010626 (8:25 AM CT, "Publish Ready GitBook batches 003–009 (GB-004 through GB-014)") was found with cursor-github `list_commits` by path. The four fields are filled in.
- **New rows GB-015 to GB-021**, status `published`, with the real merge SHAs:
  - GB-015, 019, 020, 021: `f4b2c41` (PR #5; Father's yes 3:38 PM CT; Build post-merge PASS)
  - GB-018: `97e43fb` (PR #6; head 0025919; Father's yes 3:38 PM CT; Build post-merge PASS; Security PROV PASS)
  - GB-017 and GB-016 rev 3.2: `ecd9022` (PR #7; commits a89c29c and 6e5ccfc; Father's yes 4:06 PM CT; Build post-merge PASS; Security PROV PASS)
- **New rows GB-022 to GB-025**, status `draft` (none has entered a gate). Next action: Cordnation hands the item to Gitbook Moderator (gate 1 of 4). Blocker: none.
- GB-001 to GB-003 are unchanged. Their four new cells stay empty, which the GB-022 intro sentence covers.

## HYB-005 docs decision: DONE
Source: `/workspace/security-gate/PROV-2026-10-05-97e43fb-pr6.md`. Its follow-up says the merged text still reads "IN REVIEW, pending push / SHA backfilled", that the commit now exists as 97e43fb, and that the task can be marked DONE.
- `intake/HYBRID-CONSOLIDATION-BACKLOG.md`, HYB-005 status: now "DONE (decision published `97e43fb`, PR #6; accepted + mitigated; review 2026-11-05)"
- `merge/hyb-005-braces-decision.md`, Status line: now "ACCEPTED + MITIGATED (dated); DONE (published in `97e43fb`, PR #6)"
- `history/coordination/agent-checkins.md`, Completed claims table, Commit cell: "pending Father push (backfill SHA)" replaced with "`97e43fb` (PR #6)". The cell was a placeholder meant to be backfilled.

**Left unchanged (historical check-in records):** in `agent-checkins.md`, the HYB-005 claim/completion block (lines 92–114: "Claim closed as IN REVIEW, pending push", and the two STATUS lines). These record the state at check-in time.
