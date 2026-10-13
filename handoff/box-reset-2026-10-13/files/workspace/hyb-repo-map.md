# HYB repo map: owned repos toward TESSERA / Gitbook (read-only)

Prepared Mon Oct 12 2026, ~3:55 PM CT. Read-only: no writes to any repo, issue, or PR.

## 1. Overlap check
- **Gitbook main HEAD:** `cd8faa0a5dfa64e69a7d0a0e179b0b60250cd5a3` ("Record the full name-list sync.", 9:34 AM CT Oct 12). Note: Command Center's 3:10 PM note said main was at `beadc44`; the API returns `cd8faa0`. Recheck before claiming anything.
- **Open Gitbook PRs:**
  - **#40** (draft) "Record Father's yes and the drill already on TESSERA": touches `mesh/TODOS.md`. Base `be90f68`.
  - **#39** "GB-061 rev 2: archive/preserved preservation pack": additions under `archive/preserved/` only. Head `71a8c78`. Marked do not merge.
- **Issue #2 (200 comments), latest activity:**
  - Sync ledger #8 (Oct 12, 12:13 PM CT): read-only.
  - HYB-008/017 REJECTED (`b7df2db`).
  - HYB-009/012 DONE at the level stated (`6779831`). Open follow-ups: HYB-010, 011, 013, 015, 016.
  - Cursor Project has claimed HYB-016 (AUTO-COLLAB; Gitbook `mesh/*` and coordination files).
  - The board says "Do not edit vitality."
- **No live claim found** for HYB-010, HYB-013, or HYB-015. HYB-023 (permanent site) is IN REVIEW by another lane.

## 2. Already done (backlog)
DONE: HYB-001–007, 009, 012, 014, 020, 021.
REJECTED: HYB-008 (olive), HYB-017 (storefront).
READY: HYB-010, 011, 013, 015, 016.
BLOCKED: HYB-018, 019.
HYB-006 (Grok-ready, PR #3) and HYB-007 (Zz z-app, PR #4) were reviewed and are DONE.

## 3. Repos owned by vitalitychems-dot
`search_repositories user:vitalitychems-dot` returns **4 repos**: TESSERA, Gitbook, GitbookAI, and vitality. Archived and forked repos: 0.

The older sources the backlog names (Grok-ready, Zz, 1, 5t, TESS, T44, olive-giant-ever-glade, 1T) **are no longer listed under this account.** They were likely deleted or moved under HYB-002/HYB-018, or preserved inside Gitbook/vitality archives. **1T is excluded under HYB-011.** It was not opened or inspected.

| Repo | Vis. | Useful part (light tree) | Candidate idea | Target | Disposition | HYB | Claimed on #2? |
|---|---|---|---|---|---|---|---|
| TESSERA | private | destination | — | — | (destination) | — | — |
| Gitbook | private | destination | — | — | (destination) | — | — |
| GitbookAI | public | `README.md`, `RULES.md`, `BANNED.md`, `mesh/{DOOR,TUNNEL}.md`, `mesh/index.json`, `projects/{admit,carry,house,live,pass,shift,spin,tie}`, `index.html` | Public "mesh" room. "Drop" = note, delivered only after the owner comments APPROVED. The `admit` admission script turns away machines and handles no payment. | Gitbook `mesh/` (as a docs/provenance page about the public room and approval-gate rules). No TESSERA code. | NEEDS-EVIDENCE for the approval-gate/admission rules → topic page. RETAINED for the `projects/*` code (stays public/separate; don't fold a public repo into the private Gitbook). | HYB-015 (topic page); HYB-016 (coordination rules) | HYB-016 claimed by Cursor Project. HYB-015 unclaimed. |
| vitality | private | `artifacts/vitality-supply` (current storefront), `artifacts/mockup-sandbox`, `archive/` (drive-sections zips, `moved/collink1007-fleet-moss-monarch-rapid`, `drive-rest/price-list.xlsx`), `attached_assets/`, `legacy-ui-VitalityPage.tsx` | Storefront and product media. README: "not part of Tessera." | none (kept out of TESSERA/Gitbook by owner) | REJECTED for TESSERA (matches HYB-017). RETAINED in vitality. Media only via HYB-010 provenance review, metadata-only. Price list and customer/archive contents: excluded (HYB-011), not opened. | HYB-017 (done), HYB-010, HYB-011 | #2 says "Do not edit vitality." No HYB-010 claim found. |
| 1T | — | not listed / not inspected | — | — | Excluded | HYB-011 | — |

## 4. Top 5 suggested next HYB tasks (for Tessera to assign)
1. **HYB-015: Gitbook topic pages** (product goals, engineering rules, safety/privacy, coordination, media, deferred ideas). Fold in the HYB-006/007/008/017 verdicts and the GitbookAI approval-gate rules as provenance-linked pages. *Overlap risk:* HYB-016 (Cursor Project) owns the `mesh/*` coordination files, so keep HYB-015 pages under a separate topic dir and don't edit `mesh/TODOS.md` (PR #40).
2. **HYB-013: UI flow audit.** Pick one user-valued missing flow from the HYB-006/007 ACCEPTED/RETAINED rows (e.g. Z10 own-lab is already parked under HYB-013), with a test and rollback. *Overlap risk:* the HYB-023 permanent-site build in TESSERA. Needs a named TESSERA path and Tessera's product call.
3. **HYB-011: exclusion manifest refresh.** The repo set has shrunk to 4, so the manifest should record which legacy repos are gone and confirm 1T status by name only. *Overlap risk:* low. Privacy steward lane; must not open bodies.
4. **HYB-018: coverage recheck (currently BLOCKED).** Confirm whether the legacy repos were deleted after 100% coverage, and record a manifest pointer. *Overlap risk:* deletion gates, so this needs Father's confirmation. Analysis only.
5. **HYB-010: media provenance (metadata only).** Classify vitality/Gitbook theme and screenshot media by source and license without copying. *Overlap risk:* the "do not edit vitality" rule and open PR #39 (`archive/preserved/`). Read-only listing only. Needs Tessera's call because the owner keeps vitality separate.

## Notes and limits
- No secrets, `.env` files, data dumps, the price sheet, zips, or customer data were opened. Only directory listings and two READMEs were read.
- GitbookAI is public. Anything mirrored into private Gitbook should be a summary, not a copy.
