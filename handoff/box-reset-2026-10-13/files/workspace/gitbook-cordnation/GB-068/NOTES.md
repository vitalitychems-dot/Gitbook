# GB-068 notes (HYB-024 self-fix design page; staged locally, not pushed)

- Base: Gitbook main 0f05d58b. The base files are byte-exact.
- Files: new merge/hyb-024-selffix-design.md, written in plain language from /workspace/hyb-selffix/DESIGN.md plus dryrun/LEDGER.md (13 runs); SUMMARY line after HYB-007; the backlog row HYB-SELFFIX becomes HYB-024 (same 5 columns); intake/log.md GB-068 row, in review.
- Phase 0 approval is REPORTED from Tessera's comment 6004515093 (Father approved the 5:30 PM CT bulk update that included the phase 0 dry run). The design's open question 1 ("approve phase 0") is therefore dropped. The rest are kept.
- Removed: a personal name in the audience line, IDENTITY headers, and the literal flag-name pattern (it now reads "flip a feature flag"). 1T appears only as a forbidden path name.
- Stale record to flag to Cursor Project (HYB-016): the ledger row "Self-fix loop design … BLOCKED: file is not on any disk the board lanes can read" will be out of date once this lands. Cordnation does not edit that ledger.
- Variants: GB-068.diff applies alone on main. GB-068-on-GB-067.diff applies after GB-067. Both log rows go after GB-066, so the two plain diffs do not stack in either order.
- Checks: GB-068.diff forward OK, reverse OK. Stacked variant forward OK, result matches stacked-on-067/, reverse of the full stack OK.
