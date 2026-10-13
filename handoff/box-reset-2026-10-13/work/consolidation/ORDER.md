# ORDER OF WORK — consolidate → verify → delete

1. **Freeze sources (Father).** Stop or repoint the Replit agents still writing to `5t`, `1/subrepl-nftoz8d7`, and `Zz` (commits today 4:11–5:05 PM CT). Record frozen head SHAs.
2. **Protected decisions (Father).** Confirm 1T, natal-vault (CONS-018), declarations data (CONS-015), olive, and the archive repos (CONS-022) are kept privately and never imported.
3. **Father's yes/no on ITEMS.md** (CONS-001…023), batched with LEDGER.md.
4. **Consolidate via PRs** (one PR per item group; Security and Build gates; Tessera approval):
   - a. Branch content: CONS-001, 002, 003.
   - b. History/docs: CONS-004, 005, 010, 012, 013, 014 (summary), 016 (inventory).
   - c. Code ports: CONS-006, 007 (lib + test + rollback note). CONS-008 is an intake brief.
   - d. Records: CONS-011 (Grok-ready PR closures, Father closes them), CONS-019, 020, 022, 023.
5. **Verify.** Rerun `scan_coverage.py` against new trees at the frozen heads. Update Gitbook `merge/CURRENT-REPOSITORY-STATUS.md`.
6. **Backups.** Father downloads a zip or mirror of every repo that will be deleted and records its sha256.
7. **Branch cleanup** (only after a plan approval): delete the 14 SAFE branches in BRANCHES.md after re-checking the tip SHAs. Then delete pen-gate, consolidation-draft, and chamber/desk once CONS-001/002/003 are merged.
8. **Repo deletion (Father only).** Expected order as each reaches 0 uncovered: Grok-ready → TESS → T44 / 1 (after the protected decisions) → archive repos (after offline verification). Use the SAFE-TO-DELETE.md checklist and exact names. Never delete 1T, TESSERA, or Gitbook.
