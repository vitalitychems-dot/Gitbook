# Tesseract rebuild: phase 1 map of repos and files (Gitbook issue #72)

Written 2026-10-13, 8:40 AM CT. This map reuses earlier scans and makes only 2 new GitHub API reads (the top-level trees). It is a map only: nothing is moved or deleted. **Any deletion needs Father's explicit yes.** 1T appears by name only; its contents and any secrets were not opened or copied.

## 1. Repos by group (scan date 2026-10-12)

The scan found 315 unique repo names after dedupe (REPO-INVENTORY.csv). 9 are readable. The rest (306 in the CSV) are not readable from the scan's login.

| Group | Names | Readable | Unreadable | Notes |
|---|---|---|---|---|
| TESSERA (main account) | 1 | 1 | 0 | Product code; the destination repo |
| Gitbook (main account) | 1 | 1 | 0 | Coordination, research, provenance; the destination repo |
| Other main-account repos | 17 | 2 (`GitbookAI`, `vitality`) | 15 | 12 of the 15 survive only as archive folders inside TESSERA/Gitbook (`1`, `5t`, `T44`, `TESS`, `TX`, `Zz`, `Everything`, `Grok-ready`, `1T`, `tessera-complete-archives`, `tessera-grok-handoff`, `tessera-grok-handoff-complete`). `tessera-coordination`, `tessera-unified` and `z` return 404 |
| Second account | 6 | 4 (`z`, `XXX`, `fleet-moss-monarch-rapid`, `amber-flame-tiger-sand`) | 2 | App and store snapshots |
| Third account (thetesseractai) | 7 | 1 (`18`) | 6 | |
| sovereign-core / -origin / -archive | 92 | 0 | 92 | Login not connected |
| Origin account (collin-keane) | 1 | 0 | 1 | Gap until Father connects it read-only |
| External third-party names found in notes | 190 | 0 | 190 | Not Tessera history; names only |

Count mismatch: the CSV shows 306 unreadable, the GB-064 page shows 297, and the brief says 293. The difference comes from how the second account's `z` and the archived-folder names are counted. Use 306 until the scan is reconciled.

## 2. Top-level layout (GitHub API, read 2026-10-13)

### TESSERA (32 entries)
| Path | Purpose (inferred from name and earlier scans) |
|---|---|
| `.agents/`, `skills-lock.json` | Agent skills and config |
| `.codebase-memory/` | Code-index artifacts |
| `.github/` | Workflows and CI (locked paths) |
| `archive/`, `archives/` | Folded-in old repos. **Two near-duplicate folder names: a merge candidate** |
| `artifacts/`, `deliverables/` | Build outputs and handed-over work |
| `config/`, `data/` | Runtime config and data sets |
| `docs/`, `research/` | Documentation and research notes |
| `lib/`, `scripts/`, `tools/` | Product code, scripts and tools |
| `mesh/` | Mesh coordination copied into product repo (overlaps with Gitbook `mesh/`) |
| `preview/` | Preview app |
| `package.json`, `pnpm-*`, `tsconfig*`, `.npmrc` | JS/TS monorepo build |
| `.replit`, `.replitignore` | Replit hosting |
| `CONSOLIDATION_TWO_REPOS.md`, `README.md`, `LICENSE`, `NOTICE`, `.env.example` | Top-level docs; `.env.example` holds placeholders only (not opened) |

### Gitbook (18 entries; 10,410 files at 2344334e)
| Path | Purpose | Files |
|---|---|---|
| `archive/` | Folded-in repos and moved files | 7,126 |
| `history/` | Historical records | 3,110 |
| `mesh/` | Lane handoffs, ledger, queue, charter | 62 |
| `merge/` | Consolidation and HYB pages | 31 |
| `brain-consciousness/`, `brain/` | Brain research and reports | 24 |
| `review/` | Review evidence and transcriptions | 19 |
| `intake/` | Intake log and backlog | 12 |
| `posts/`, `forum/` | Posts and forum | 9 |
| `operations/`, `state/` | Ops notes and state | 11 |
| `tools/` | Tooling (added after the inventory) | n/a |
| `.codebase-memory/` | Code-index artifacts | 3 |
| `SUMMARY.md`, `README.md`, `.gitbook.yaml`, `CODEOWNERS` | Table of contents, config and owners | 4 |

## 3. Candidate buckets (proposals only; nothing deleted)

| Bucket | Count | Examples |
|---|---|---|
| Keep (live destination) | 2 repos | TESSERA, Gitbook |
| Keep separate | 2 repos | `GitbookAI` (public room; summary only in Gitbook), `vitality` (store; not Tessera) |
| Merge (already folded in; mark done) | 12 repos | `T44`, `TESS`, `TX`, `Zz`, `tessera-grok-handoff(-complete)` folders inside TESSERA/Gitbook |
| Merge (pending code analysis) | 5 repos | `z`, `XXX`, `fleet-moss-monarch-rapid`, `amber-flame-tiger-sand`, `18` |
| Duplicate / overlap (files) | 3 areas + 636 handoff/log files | TESSERA `archive/` vs `archives/`; TESSERA `mesh/` vs Gitbook `mesh/`; 636 handoff and log files in Gitbook (single HANDOFF.md from GB-067 is the merge target) |
| Unknown | 293–306 repos | sovereign-* (92), thetesseractai (6), second account (2), origin (1), external (190, names only), plus `tessera-coordination` and `tessera-unified` |
| Protected | 1 | `1T`: name only, never opened |

Housekeeping found by the memory-graph scan: 39 orphan pages that are not in SUMMARY.md (for example `mesh/TODOS.md`, `merge/hyb-008-olive.md`) and 46 broken internal links.

## 4. Known gaps

1. **Gitbook `archive/` (7,126 files) and `history/` (3,110 files)** have not been scanned for secrets or for 1T material. They need a gitleaks-only pass, plus a 1T name check that does not open contents, before anything moves.
2. **TESSERA `archive/` and `archives/`** have not been scanned for secrets either, and their file counts were not taken.
3. **Unreadable repos (293–306)** need their logins connected read-only (sovereign-*, thetesseractai, second account, origin/collin-keane).
4. **Code analysis is still queued** for `z`, `XXX`, `fleet-moss-monarch-rapid`, `amber-flame-tiger-sand`, `18`, and the TESSERA, vitality, GitbookAI and Zz folders.
5. **Last activity** has not been recorded for the second-account repos.
6. **The rea-shards** cover the A-H, I-P and Q-Z lanes plus security, build and branch shards. Their coverage was not re-checked for this map.
7. **TESSERA file-level inventory** is missing. The memory-graph inventory covers Gitbook only.
8. **The Gitbook inventory is from main `2344334e`** (2026-10-12, 6:40 PM CT). Later merges (#51 to #77) are not counted in it.

## 5. Sources

| Source | Date |
|---|---|
| `/workspace/build-plan-2026-10-12/REPO-INVENTORY.csv` (315 rows) | 2026-10-12 |
| `/workspace/gitbook-cordnation/GB-064/` (repo-scan page draft, base 56a7a48) | 2026-10-12 |
| `/workspace/gitmesh/memory-graph-inventory.md` (Gitbook @2344334e) | 2026-10-12 18:40 CT |
| `/workspace/build-plan-2026-10-12/rea-shards/` (A-H, I-P, I-P-public, Q-Z, SECURITY, BUILD-VERIFY, cursor-branch*) | 2026-10-12 |
| GitHub API top-level trees: TESSERA, Gitbook main | 2026-10-13 ~8:40 AM CT |
