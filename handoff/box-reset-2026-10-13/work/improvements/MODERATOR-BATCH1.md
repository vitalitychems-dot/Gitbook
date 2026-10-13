# Moderator gate — Improvements batch 1 (IMP-001 to IMP-064)

IDENTITY: Moderator gate (Grok Bot executor)
Reviewed: 2026-10-05, ~5:33 to 5:45 PM CT
Bases (TESTED via GitHub API): TESSERA `5c1137faeb7714482add93c2d6876396f34f1a03` (parents 50876d40 HYB-012 + 76716c22); Gitbook `bc6b32871faed56b13df3dfadc849ec725d60f14`
CI: run 37382015797 = CI / push / main / head 5c1137fa / conclusion **success** (TESTED)
Results file: `gates/moderator.md` (one line per item)

## Totals

- **PASS = 61**
- **FAIL = 3**

## FAIL IDs

| ID | Reason |
| --- | --- |
| IMP-020 | Already done. The TESSERA README "Workspace checks" block already lists `pnpm audit`, and the README has no scripts table. The cited path (`package.json`) does not match the change (README). |
| IMP-037 | Wording is wrong. `SOURCE-HEADS-2026-10-05.md` lists no Gitbook SHA ("this source-head record is being published now"); it lists only TESSERA `fec56eb`. It is a dated "Checked: 2026-10-05" snapshot, so changing its SHAs would rewrite the historical record. The evidence also says the file had not been read ("re-read file before edit"). Suggested rework: append a "current mains" note instead of refreshing the listed SHAs. |
| IMP-050 | The cited content does not exist. `review/COLLABORATION-AUDIT-2026-10-05.md` has no "no multi-agent" finding; that "no replies" text is in agent-checkins.md (IMP-036 already covers it). The audit page does have a different stale claim, "Father alone performs the GitBook → GitHub push" (now Tessera pushes after Father's yes). A reworked row could target that. |

## Soft notes (non-blocking)

- IMP-001–008: the CI-green inventory test on 5c1137fa asserts the live duplicates equal the allow-list exactly, so all 10 entries are TESTED. Mount order was checked in `routes/index.ts`: sovereign-engines, governance-consensus, system-runtime, then improvement, legacy-engines, universe.
- IMP-015: PROJECT_MAP's table is a "Project" table, not an "Applications" table. The meaning is the same.
- IMP-018: passes only as boot hygiene. Nothing about wallet keys or config may change.
- IMP-031/039/040/045: the Father approvals (phase-0 ~5:28 PM CT; 50–100 batched lists) are REPORTED and not in the cited files. `DESIGN.md` §open-questions still lists "Approve phase 0 dry-run now?". The 5:21 PM CT standing fix rule is cited in DESIGN.md.
- IMP-032 vs IMP-045: both document selffix/standing rules (flow.md vs ops guidelines). Pick one canonical page and cross-link from the other.
- IMP-033: `mesh/roles/tessera.md` says Active / "Build lane: code builds and branches". The "admin" wording is in `roles.md`.
- IMP-009/021/046/047, IMP-017/018/025, IMP-022/057: related but distinct, as instructed.
- IMP-051: an in-repo harness already exists (`artifacts/api-server/scripts/eval-chatbot.ts`, 10 golden cases writing JSON to `.local/`; plus `POST /evaluation/run`). Neither is an industry harness, so the claim holds. Prefer extending them over adding a parallel one. The "forbid MMLU naming" clause overlaps IMP-059.
- IMP-053/054/063: these pass only as decisions awaiting Father. Spend, provider keys, and Origin reconnect each need an explicit yes. No key values are allowed anywhere. Key presence on the box was checked as set/unset only (both UNSET); no values were read.
- IMP-064: findings must stay value-redacted. 1T stays unopened.
- Other stale items seen but not in the ledger (candidates for batch 2): `intake/consolidated-todo.md` still lists HYB-005 as open; `review/validation.md` says CI "has not yet run on GitHub".

## Scope confirmation

- I did not edit `LEDGER.md`. My only writes were `gates/moderator.md` and this file. LEDGER.md's mtime (5:36 PM CT) comes from the IMP-051–064 rows the coordinator added; every Moderator cell is still empty.
- No GitHub writes: no pushes, PRs, comments, or issue edits. All GitHub calls were reads.
