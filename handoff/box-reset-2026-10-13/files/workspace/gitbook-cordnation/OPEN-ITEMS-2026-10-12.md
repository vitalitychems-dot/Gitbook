# Open intake and board items — 2026-10-12, 3:55 PM CT (read-only)

Base: Gitbook main `cd8faa0a5dfa64e69a7d0a0e179b0b60250cd5a3`. Open PRs: #39 (GB-061 rev 2, archive/preserved/, marked do not merge) and #40 (draft, mesh/TODOS.md).
Sources: intake/log.md, the backlog, mesh/HANDOFF.md, mesh/TODOS.md, board issue #2 (last 100 comments) and the local packages.
"Ready" here means ready to package as-is.

## 1. Priority items

| ID | Title | Status | Owner | Blocker | Ready? |
|---|---|---|---|---|---|
| GB-062 rev 2 | Consolidation map 2026-10-12 | Staged locally; awaiting Moderator, then Security and Build | Cordnation | Gates only | Packaged (`6691071e…667a`) |
| HYB-015 | Gitbook topic pages (incl. the GitbookAI approval-gate summary) | READY | unclaimed (backlog role: Gitbook moderator) | Needs a claim. Keep out of mesh/* (HYB-016) | Needs drafting |
| HYB-011 | Exclusion manifest refresh (name the gone repos; 1T by name only) | READY | unclaimed (Privacy steward) | Privacy lane. Bodies stay unopened | Needs drafting; Privacy/Security sign-off |
| HYB-024 | Self-fix loop design (`/workspace/hyb-selffix/DESIGN.md`, 10.9K, plus dry-run notes) | Number approved 3:53 PM CT; REPORTED phase 0 | Tessera (admin) wrote it | The doc is Tessera's. Cordnation only renumbers and publishes it | Nearly: renumber HYB-SELFFIX→HYB-024 in the backlog plus a design page |
| — | Research mesh (`/workspace/knowledge-lab/`, 288K) | Local only | unclaimed | Pick the subset to publish (README, THEORIES, OPEN-PROBLEMS, CONNECTIONS, WORKFLOW) | Nearly; light edit |
| HYB-022 | Brain test summary (`/workspace/tessera-brain/`, 19M; tests PASS) | TESTED LOCALLY | **Brain lane (don't take)** | Brain lane must write or approve the summary | No; ask the Brain lane |

## 2. Consolidation items

| ID | Title | Status | Owner | Blocker | Ready? |
|---|---|---|---|---|---|
| HYB-010 | Media provenance (metadata only) | READY | unclaimed (Media steward) | "Do not edit vitality"; PR #39 overlaps archive/ | No; needs Tessera's call |
| HYB-013 | UI flow audit; one missing flow | READY (TODOS: "active ledger claim") | Claim unclear, so treat as claimed | Product call; TESSERA code | No |
| HYB-016 | Coordination rules under mesh/* | READY | **Cursor Project (don't take)** | — | Not ours |
| HYB-018 | Coverage recheck before deletion | BLOCKED | Release steward | Father's confirmation | No |
| HYB-019 | Product and mesh prep | BLOCKED | Product/mesh | Father's decisions | No |
| HYB-023 | Permanent site | IN REVIEW | **Permanent-site lane (don't take)** | SITE-001–004 reports | Not ours |
| PR #39 / GB-061 rev 2 | archive/preserved pack | Open, not TESTED | Another lane (**don't take**) | Mod, Security and TESSERA gates on `71a8c78` | Not ours |
| PR #40 | Father's yes and drill record (mesh/TODOS.md) | Draft | **Cursor (don't take)** | Base `be90f68` is stale | Not ours |
| Local working sets (`consolidation/`, `full-picture/`, `improvements/`) | — | Covered | Cordnation | — | Mark done inside GB-062; no package |

## 3. Everything else

- **GB-030 to GB-053 (23 rows):** all are `in review` in the intake log, except GB-039, which is not in the list. Owners: Cordnation for most; Tessera Pen for 034, 045, 047, 051 and 053; Build for 037 and 038. Every row says "Gitbook Moderator reviews (gate 1 of 4)". Main has had 25 PR merges and 130 direct pushes since Oct 6 (sync ledger #8), so many of these are probably already on main and the log is stale. Each row needs a check: is the content on main, and through which PR or commit?
- **GB-054 to GB-061:** used on the board or in PRs (GB-059 in commit `fbb67a52`, GB-061 in PR #39), but **no intake rows**.
- **Held, not logged:** four direct commits to main (44f5266, d2b8339, 779135e, fcabd13). Their attribution waits on Father.
- **TODOS still open (not ours):** rotate the keys (Father only); TESSERA PRs #34, #80 (adds weights, so do not merge), #82 and #87; the mesh/TRUE-TODAY.md refresh.

## 4. Proposed sequence (next free GB numbers; GB-062 is in use)

1. **GB-062 rev 2.** Finish the gates (Moderator, Tessera, Security, Build). No new work.
2. **GB-063: intake log reconciliation.** For GB-030 to GB-053, set each row that is on main to `published` with its commit or PR. Add rows for GB-054 to GB-061 from their board and PR records. Changes `intake/log.md` only. Best done first, so later rows land on a log that is correct.
3. **GB-064: HYB-024 self-fix.** Add a backlog row (HYB-SELFFIX→HYB-024, as Tessera numbered it) and a new page `merge/hyb-024-selffix-design.md` from DESIGN.md plus the dry-run summary. Needs Tessera's OK on the text, since it is her design.
4. **GB-065: research mesh.** New pages `brain-consciousness/research/` (README, THEORIES, OPEN-PROBLEMS, CONNECTIONS, WORKFLOW), plus SUMMARY entries.
5. **GB-066: HYB-015 topic pages.** Start with the GitbookAI approval-gate summary (summary only, no copied code). Needs a HYB-015 claim on the board first, posted by Tessera.
6. **GB-067: HYB-011 exclusion manifest refresh.** Name the gone repos and confirm 1T by name only. Needs a Privacy/Security owner.
7. **Brain test summary:** hand to the Brain lane (HYB-022). If they hand it back, it becomes GB-068.

Not ours: HYB-016 (Cursor Project), HYB-022 (Brain lane), HYB-023 (Permanent-site lane), PR #39 / GB-061, PR #40 (Cursor), HYB-013 (claim unclear).
