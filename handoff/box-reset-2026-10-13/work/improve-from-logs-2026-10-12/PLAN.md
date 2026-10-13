# PLAN — gates and bulk list

As-of: **2026-10-12 ~4:00 PM CT**  
Worktree: `/workspace/improve-from-logs-2026-10-12/` (local only; **no pushes**).

## Done this session (TESTED)

1. Extracted **506** unique repo-like names → `REPO-NAMES.md` + `repo-names.json`.
2. Proposed **24** items (IMP-085–108, RS-011–012) → `PROPOSED-ITEMS.md`.
3. Ran before/after quiz → `RESULTS.md` (retrieval 40%→70%; model RAG 30%→40%).
4. Built `expanded-repo-index.md` used as the after-corpus document.

## Top sources for the name extract

1. `Gitbook:mesh/GITHUB-REPOS.txt` (~275 owner/repo lines)
2. `Gitbook:mesh/mentioned-repos.txt` (superseded subset)
3. Archive folder names under Gitbook `archive/moved|drive-rest` and TESSERA `archives/source-*`
4. `merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md`, `merge/repo-audit.tsv`, `DELETION-MANIFEST.md`, `FULL-AUDIT-SUMMARY.md`
5. Local `consolidation/REPOS.md`, `full-picture/INVENTORY.md`, `repo-lab/REPOS.csv`, `hyb-staging/archive-map.md`

## How items enter Father's bulk list

1. **Moderator** — claim on Gitbook issue #2; open **draft** PRs (Gitbook docs first for IMP-085/087/089/093/095/101; TESSERA code behind flags for IMP-086/088/090/092).
2. **Security** — path scan; reject any touch of EXCLUDED names; confirm no cookie/credential import; rea limited to owned artifacts if used.
3. **Build** — TESSERA: tests green (local harness + existing vitest). Gitbook: markdown/SUMMARY only.
4. **Bulk digest** — Command Center / Tessera lists IMP/RS IDs with one-line plain English in the 30–45 min digest; Father replies yes / numbers to reject.
5. **Merge** — Gitbook after yes; TESSERA only with explicit "merge" when required by standing rules.

## Suggested first wave (after Father yes)

| Wave | IDs | Rationale |
| --- | --- | --- |
| A (docs) | IMP-085, IMP-087, IMP-093, IMP-101, IMP-103, IMP-108 | Pure Gitbook; unlocks retrieval win already measured |
| B (memory) | IMP-086, IMP-088, IMP-094, IMP-105 | Wire index + learning memory + regression |
| C (research) | IMP-096, IMP-097, RS-011, RS-012 | Extends knowledge-lab TESTED loop |
| D (optional spikes) | IMP-090, IMP-092, IMP-102, IMP-107 | Flags default off; AgentCraft ideas-only; rea only if lost source exists |

## Overlap / coordination

- Historical Analysis Collab: HYB-015 / HYB-011 drafts in `/workspace/hyb-staging/` — align IMP-095/101 with those PRs; do not double-edit `mesh/*` claimed by PR #40.
- Cordnation GB-062 consolidation map — IMP-093 cross-links; do not replace Oct 7 routing page.
- Live account inventory is **4** repos; the "hundreds" are log mentions + nested archives. IMP-108 tracks the Origin/other-login gap.

## Stop lines

- No GitHub write from this folder until Father yes + gates.
- No Claude-Red. No api-anything install. No 1T open.
