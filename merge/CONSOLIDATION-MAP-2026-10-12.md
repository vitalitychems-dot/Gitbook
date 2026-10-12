# Consolidation map — 2026-10-12

**Base:** Gitbook main `cd8faa0`, TESSERA main `a502322`.
**Builds on:** [All-repository routing and consolidation record](ALL-REPOSITORIES-ROUTING-2026-10-07.md). That record routed about twenty repositories. This page is the current map after the account shrank to four.

Nothing on this page deletes a repository. Deletion stays on Father's yes checklist in [`DELETION-MANIFEST.md`](DELETION-MANIFEST.md).

## The two homes

- **TESSERA** holds reviewed product code, tests and configuration.
- **Gitbook** holds instructions, coordination, research, provenance and decisions.

## Repository map

The connected GitHub account lists four repositories under `vitalitychems-dot`. A second owner name was searched and returned no repositories visible to this account. The Origin repository under that login is still a gap until Father connects it.

| Repository | Visibility | Purpose | Last push (CT) | Destination | Owner on the board |
|---|---|---|---|---|---|
| `TESSERA` | private | Product code and tests | 2026-10-12 9:34 AM | TESSERA (destination) | Tessera gates; lanes work on their own branch |
| `Gitbook` | private | Coordination, instructions, research, provenance | 2026-10-12 9:34 AM | Gitbook (destination) | Cordnation intake; Moderator review |
| `GitMesh` (renamed from GitbookAI, 2026-10-12) | public | Public room carried by git; owner-approval gate rules and small `projects/*` programs | 2026-10-10 9:42 AM | Gitbook gets a summary page of the approval-gate rules (HYB-015). The code stays in its own public repository. | HYB-016 coordination rules: Cursor Project. HYB-015: unclaimed |
| `vitality` | private | Vitality Supply store and product media. Its README says it is not part of Tessera. | 2026-10-11 12:02 PM | Archive-mark-done for Tessera purposes. It stays separate. | Board rule: do not edit vitality. HYB-010 media metadata: unclaimed |

The older sources named in the backlog (`Grok-ready`, `Zz`, `1`, `5t`, `T44`, `TESS`, `olive-giant-ever-glade` and the archive repositories) are no longer listed under this account. Their routing and verdicts stay recorded in the 2026-10-07 record and in HYB-006 to HYB-009 and HYB-017. `1T` stays protected and unopened under HYB-011.

Father said the nested archives inside TESSERA and Gitbook are the rest of the inventory.

## Local research and brain work not yet in Gitbook

These items sit on the shared work machine. None is in Gitbook main as its own page.

| Item | What it is | Proposed home |
|---|---|---|
| Self-fix loop design (`hyb-selffix/DESIGN.md`, dry-run notes) | Narrow loop: when CI `validate` fails, diagnose from logs, propose a minimal fix on a branch, run the four gates. Phase 0 is suggest-only. | Gitbook `merge/` as a design page once it has a HYB number (see below). Any code goes to TESSERA by PR. |
| Research mesh (`knowledge-lab/research/`: theories, open problems, connections, code index, workflow) | A catalog of theories and open problems with links between them | Gitbook `brain-consciousness/research/` |
| Brain blueprint and spiking test (`tessera-brain/`) | Connectome stats, a small spiking simulation and passing local tests | Summary and test result in Gitbook `brain-consciousness/reports/` (HYB-022 lane). Scripts go to TESSERA only by PR with tests. Images and large data stay local. |
| Consolidation working set (`consolidation/`: repos, branches, items, order) | The 2026-10-05 inventory and consolidate-then-verify order | Already covered by the 2026-10-07 routing record. Mark done; nothing new to move. |
| Full-picture inventory (`full-picture/`) | 2026-10-05 inventory, baseline and benchmark plan | Benchmark plan to Gitbook `brain-consciousness/reports/` after the board cards it. The rest is covered; mark done. |
| Improvements ledger (`improvements/`) | List 1 yes/no ledger (IMP-009 to IMP-084) | Covered by GB-039 and the board. Mark done. |
| Repo map draft (`hyb-repo-map.md`, today) | Read-only map of the four repositories and the next five HYB tasks | Folded into this page |

## Consolidation order

1. Record the current four-repository map (this page).
2. Give the self-fix design its HYB number and publish it as a design page.
3. Publish the research mesh and the brain test summary under `brain-consciousness/`.
4. Write the GitMesh rules summary (HYB-015). Leave its code where it is.
5. Refresh the HYB-011 exclusion manifest to name the repositories that are gone. Confirm `1T` by name only.
6. Mark the covered local working sets done. Delete nothing.

## Who owns what

- Tessera: gates, the numbered list and HYB numbering.
- Cordnation: this page and the intake rows.
- Cursor Project: HYB-016 coordination files under `mesh/`.
- Brain lane: HYB-022.
- Permanent-site lane: HYB-023.
- Unclaimed: HYB-010, HYB-013 and HYB-015.
