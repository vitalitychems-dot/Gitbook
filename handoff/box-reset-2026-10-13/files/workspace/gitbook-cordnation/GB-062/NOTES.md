# GB-062 notes (staged locally; not pushed)

- Asked for as "GB-030". GB-030 is already used in intake/log.md (PR #11/#12 backfill, in review), and the highest GB on the board/PRs is GB-061 (PR #39). So this is staged as GB-062. Tessera should confirm the number.
- Base: Gitbook main cd8faa0a5dfa64e69a7d0a0e179b0b60250cd5a3. Base files are byte-exact (git blob hashes match the main tree).
- Files: SUMMARY.md (+1), intake/log.md (+1, GB-062 row, status in review), merge/CONSOLIDATION-MAP-2026-10-12.md (new, +56). It goes in merge/ next to the 2026-10-07 routing record, which already serves as a consolidation map. This page updates that record and does not replace it.
- git apply --check on a clean base: OK. Applied result matches proposed/. Reverse check: OK.
- Overlap: open PR #39 touches archive/preserved/ only. Open PR #40 touches mesh/TODOS.md only. Neither overlaps.
- No TESSERA_ENABLE_* in the diff. No gate banners.
- The HYB-SELFFIX design has no number. The backlog goes up to HYB-023, so the next free number is HYB-024 (Tessera assigns it).

## Rev 2 (2026-10-12, 3:53 PM CT ruling by Tessera: GB-062 and HYB-024 numbers approved; page stays next to the Oct 7 record)
- Rev 1 is SUPERSEDED. Kept as GB-062-rev1.diff (= GB-062.diff, sha256 405302e8…8418) and proposed-rev1/.
- Rev 2 is GB-062-rev2.diff, built from rev 1 (proposed-rev2/). It adds only two notes to merge/CONSOLIDATION-MAP-2026-10-12.md:
  (a) the nested archives inside TESSERA and Gitbook are the rest of the inventory (Father);
  (b) Origin under the second login is still a gap until Father connects it. This is folded into the existing gap line, which does not name the handle, per the no-personal-handle rule.
- Main re-checked read-only: still cd8faa0a5dfa64e69a7d0a0e179b0b60250cd5a3.
- Forward apply --check OK, applied result matches proposed-rev2/, reverse check OK.
