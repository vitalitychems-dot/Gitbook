# GB-025: coordination board moved to Gitbook issue #2

**Rule:** Father, 3:56 PM CT 2026-10-05. tessera-coordination was merged into Gitbook, and Gitbook issue #2 (https://github.com/vitalitychems-dot/Gitbook/issues/2) is now the coordination board. It replaces `vitalitychems-dot/tessera-coordination` issue #4.
**Base:** Gitbook `ecd902211abd202711838219b28a1e1b39ae47c4` + GB-022 v4 + GB-024 v3. Stacks after GB-024 and before GB-023.
**Package:** `GB-025.ecd9022.diff`: 83 lines, 7 files, 7 hunks, +7/−7.
**Search:** I scanned all 127 files in the ecd9022 tree. The 28 files that packages touch were grepped locally on the stacked tree; the other 99 were read through cursor-github at ecd9022, and the four large data files were grepped from saved copies. Patterns: `tessera-coordination`, `issue #4`, `issue **#4**`, a bare `#4` meaning the board, and `tessera-coordination/issues/4`.

## Changed (7 references, 7 files): live board references

Each edit swaps only the repo and issue number and adds the issue #2 link. The surrounding sentence is unchanged.

| # | File (line on stacked tree) | Before | After |
|---|---|---|---|
| 1 | `intake/how-to-submit.md` (35) | Single coordination board: `vitalitychems-dot/tessera-coordination` issue **#4** | Single coordination board: [`vitalitychems-dot/Gitbook` issue **#2**](…/Gitbook/issues/2) |
| 2 | `mesh/TESSERA-GITBOOK-OPERATING-MODE.md` (7) | **Coordination board:** [`vitalitychems-dot/tessera-coordination` issue #4](…/tessera-coordination/issues/4) | **Coordination board:** [`vitalitychems-dot/Gitbook` issue #2](…/Gitbook/issues/2) |
| 3 | `mesh/flow.md` (51) | One board only: GitHub `vitalitychems-dot/tessera-coordination` issue **#4**. | One board only: GitHub [`vitalitychems-dot/Gitbook` issue **#2**](…/Gitbook/issues/2). |
| 4 | `mesh/roles.md` (39) | Single coordination board: `vitalitychems-dot/tessera-coordination` issue **#4**. | Single coordination board: [`vitalitychems-dot/Gitbook` issue **#2**](…/Gitbook/issues/2). |
| 5 | `mesh/roles/command-center.md` (40) | Create new coordination boards (board is issue **#4** only) | … (board is [Gitbook issue **#2**](…/Gitbook/issues/2) only) |
| 6 | `mesh/roles/open-helper-agent-2.md` (24) | The one board is `vitalitychems-dot/tessera-coordination` issue #4. | The one board is [`vitalitychems-dot/Gitbook` issue #2](…/Gitbook/issues/2). |
| 7 | `review/moderator-handoff.md` (19) | (only issue **#4**) | (only [Gitbook issue **#2**](…/Gitbook/issues/2)) |

After the edits, the stacked tree has zero matches for `issue #4`, `issue **#4**`, or `tessera-coordination/issues/4`.

## Skipped: not live board references

### A. Live page, but a source-repo reference, not the board (needs a Tessera decision)
| File | Text | Why skipped |
|---|---|---|
| `mesh/roles/tessera-pen.md` (52, Sources list) | `vitalitychems-dot/tessera-coordination — PEN.md, COORDINATION.md, COMMAND.md, STATUS.md` | This names the source repo, not the board. The merged copies appear to be `history/coordination/tessera-pen-record.md`, `coordination-record.md`, `command-center.md` (an empty file) and `history/recovered/coordination/STATUS.md`. Repointing would change a provenance line, so it is left for Tessera. |

### B. Live pages with an older "issue #2" that may not mean Gitbook issue #2 (needs a Tessera decision)
| File | Text | Why skipped |
|---|---|---|
| `mesh/flow.md` (73, Lane boundaries, CC bullet) | "Never pushes GitBook or TESSERA; see issue **#2** / `COMMAND.md`." | `COMMAND.md` was a tessera-coordination file, so this "issue #2" probably means the old tessera-coordination issue, not Gitbook #2. Now that Gitbook #2 is the board, readers could take it to mean the board. Not a #4 reference, so it is unchanged. |
| `mesh/roles/command-center.md` (23) | "- References: issue **#2** / `COMMAND.md`" | Same ambiguity. |

### C. Pages that already point at Gitbook issue #2 (no change needed)
- `intake/AGENT-LAUNCH-PROMPTS.md`, `history/coordination/agent-checkins.md` (issue #2 comment links, lines 30/41/201), `merge/hyb-005-braces-decision.md` (Conference link).
- `brain-consciousness/AGENT-WORKPLAN.md:3` says "Conference issue" without a link. It is not a board reference.

### D. Historical records and inventories: they record past events, so they stay unchanged
| File | Reference |
|---|---|
| `merge/source-map.md`, `merge/DELETION-MANIFEST.md`, `merge/FULL-AUDIT-SUMMARY.md` | tessera-coordination named as a merged/deleted source repo |
| `merge/repo-audit.tsv`, `merge/full-audit-summary.tsv` | tessera-coordination inventory rows |
| `merge/full-audit-report.json` | 10 × `"repository": "tessera-coordination"` |
| `merge/exact-duplicates.tsv`, `merge/duplicate-groups.tsv` | `tessera-coordination:` path entries (checks/ability.test.mjs, README.md, PEN.md, COORDINATION.md, COMMAND.md) |
| `history/coordination/tessera-pen-record.md` | "Admin of … tessera-coordination" (historical Pen record) |
| `history/recovered/legacy/tessera-replit-readme.md` | "The cards stay in `tessera-coordination`." (historical Replit README) |
| `history/recovered/coordination/notes/2026-10-03-chamber-sync.md` | "A post from this page reached issue 2." (Oct 3 record of the old repo's issue 2) |
| `history/recovered/coordination/checks/ability.test.mjs` | "Cursor/Grok Bot/Replit replies on issue 2 as itself" (archived test strings) |
| `intake/HYBRID-CONSOLIDATION-BACKLOG.md:36` | "[PR #4]" is a Gitbook pull request, not the board |

No matches in: `merge/redundancy-ledger.csv`, `review/image-text/ocr.jsonl`, and the remaining history/review/forum/operations pages.

## Counts
- Live board references changed: **7** (in 7 files)
- Skipped: **1** source-repo line (A), **2** ambiguous old "issue #2" lines (B), **3** pages already on Gitbook #2 (C), and **12** historical/inventory files (D, plus the PR #4 false positive)
