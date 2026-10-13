# GB-064 notes (repository scan; staged locally, not pushed)

- Base: Gitbook main 56a7a48d05ae2f507bbccdf888f0cf6e6e8ad5b3 (HYB-016 ledger refresh). It changes no file this package touches; intake/log.md and SUMMARY.md are identical to d27e3e6.
- Number: GB-063 is used twice. The intake log fix-up (GB-063 rev 3, local) and open PR #45 ("GB-063: HYB-011 refresh and GitbookAI rules", head 9004959b) both carry it. GB-064 is the next free number: the log goes up to GB-062 and no board comment or PR uses GB-064.
- Source: /workspace/build-plan-2026-10-12/rea-shards/ is EMPTY (0 shard files). I built from the merged REPO-INVENTORY.csv (315 unique names, lane tags A-H 84 / I-P 65 / Q-Z+digits 166) plus REA-RUN-LOG.md (batch 2/3 is still in progress).
- Coverage: 9 names readable, 13 archive folders, and 293 unreadable (292 not found, plus the Origin repository).
- Code analysis has finished for 2 folders (T44 and olive). It is queued for z, XXX, fleet-moss-monarch-rapid, amber-flame-tiger-sand, 18, TESSERA, vitality, GitbookAI and Zz. Rev 2 comes once those land.
- Canon: no personal handles. Owners are written as main, second or third account, or by org group. 1T appears by name only. Unreadable names are counts, not lists.
- Files: GB-064.diff (on 56a7a48, alone) and GB-064-on-GB-063rev3.diff (use this one if GB-063 rev 3 lands first). The two packages don't stack with plain git apply because both add a row after the GB-062 row.
- Checks: GB-064.diff forward and reverse OK on 56a7a48. GB-064-on-GB-063rev3.diff applies after GB-063 rev 3, and its reverse check is OK. GB-063 rev 3 does not apply after GB-064.diff.
