# REPOS — vitalitychems-dot account inventory and classification

IDENTITY: Tessera Admin coordinator (executor: Grok Bot)
As-of: 2026-10-05 ~6:00 PM CT. **Read-only pass: no GitHub writes were made.**
Labels: **TESTED** = verified this session via cursor-github MCP · **REPORTED** = a doc/commit/PR says so · **UNKNOWN** · **BLOCKED**.

Sources (TESTED): `search_repositories q="user:vitalitychems-dot fork:true"` → `total_count 13`, `incomplete_results false`; `list_branches` and `list_pull_requests state=all` per repo; recursive `get_git_tree` per repo (1T excluded); `list_commits` on default and non-default branches. Raw JSON is in `/workspace/consolidation/raw/`.
Bases (TESTED): TESSERA `main@5c1137fa`, Gitbook `main@bc6b3287`.
Reused prior work: `/workspace/full-picture/INVENTORY.md`; Gitbook `merge/CURRENT-REPOSITORY-STATUS.md`, `merge/DELETION-MANIFEST.md`, `merge/FULL-AUDIT-SUMMARY.md`, `merge/full-audit-report.json`, `merge/hyb-006-grok-ready.md`, `merge/hyb-007-z-app.md`, `review/source-branch-review.md`. `/workspace/repo-lab/REPOS.csv` and `REPORT.md` **do not exist**. `repo-lab/` holds third-party clones only (TESTED `ls`).

## Fresh coverage scan (TESTED, blob-SHA)

Method (`scan_coverage.py`): a source file counts as **covered** when its git blob SHA appears anywhere in TESSERA `main` or Gitbook `main`. Equal git blob SHAs mean byte-identical content. The scan reads tree metadata only. It does not read any file bodies, and it does not touch **1T**.

| Repo (ref) | Files | Covered by TESSERA+Gitbook | Uncovered | Uncovered MB | Uncovered after also counting other source repos |
|---|---:|---:|---:|---:|---:|
| `1` (main) | 913 | 721 | 192 | 212.6 | **0** (all 192 also exist in 5t/T44/TESS) |
| `1` (`subrepl-nftoz8d7`) | 2,613 | 810 | 1,803 | 193.6 | 1,629 |
| `5t` | 1,318 | 1,094 | 224 | 223.4 | 11 |
| `T44` | 1,276 | 1,067 | 209 | 216.8 | 2 |
| `TESS` | 1,297 | 1,093 | 204 | 212.7 | 2 |
| `Grok-ready` | 1,293 | 1,271 | 22 | 3.5 | 5 |
| `Zz` (main) | 8,024 | 2,137 | 5,887 | 95.9 | 3,646 |
| `olive-giant-ever-glade` | 4,319 | 1,994 | 2,325 | 67.2 | 202 (2,123 shared with Zz) |
| `tessera-complete-archives` | 316 | 4 | 312 | 162.4 | 312 |
| `tessera-grok-handoff` | 29 | 3 | 26 | 53.0 | 26 |
| `tessera-grok-handoff-complete` | 328 | 12 | 316 | 164.6 | 316 |
| `1T` | — | — | — | — | **not scanned (PROTECTED)** |

Result (TESTED): **no source repo is 100% covered by TESSERA+Gitbook.** This matches Gitbook `merge/CURRENT-REPOSITORY-STATUS.md` (REPORTED, which found "no additional repository eligible for deletion"). Heads have moved since that doc for `Zz` (main `ec2118d6`, was `150d4ec0`), `5t` (`57ff01d2`, was `8b3b9ce`), and `1T` (pushed 5:09 PM CT today). My scan uses the current heads.

## Live-use signal (TESTED via list_commits)

Some repos are still being written to by a **Replit Agent** today. Deleting them would break a live workspace.
- `5t` main: 6 Replit Agent commits from 4:21 to 5:05 PM CT today ("Update shepherd audit log entries", …).
- `1` `subrepl-nftoz8d7`: 3 Replit Agent commits from 4:11 to 4:38 PM CT today ("Update memory and consolidation scope documentation").
- `Zz` main: Replit Agent commits at 4:23 PM and 4:57 PM CT today ("Add new ingest data…", "Update data manifest…").
- `1T`: pushed 5:09 PM CT today (metadata only; contents not inspected).

## Inventory

Times are CT (converted from GitHub UTC). Size is GitHub `size` in KB. Open PRs are TESTED via `list_pull_requests`. No repo is archived, and no repo is a fork (TESTED `archived:false`, `fork:false` for all 13). No repo declares a license (TESTED `license:null` for all 13).

| # | Repo | Vis. | Size KB | Last push (CT) | Default | Open PRs | Archived | Fork | Description | Class | Label |
|---|---|---|---:|---|---|---:|---|---|---|---|---|
| 1 | `TESSERA` | private | 5,074 | Oct 5 5:22 PM | main | 0 (2 merged) | no | no | Private Tessera consolidation destination… | **KEEP** | TESTED |
| 2 | `Gitbook` | private | 902 | Oct 5 5:28 PM | main | 0 (10 merged; issue #2 open) | no | no | (none) | **KEEP** | TESTED |
| 3 | `Zz` | private | 69,486 | Oct 5 5:05 PM | main | 0 (none ever) | no | no | (none) | **KEEP** (in use) + CONS items | TESTED |
| 4 | `5t` | public | 193,926 | Oct 5 5:11 PM | main | 0 | no | no | T5 | **KEEP** (in use) + CONS items | TESTED |
| 5 | `1T` | private | 190,110 | Oct 5 5:09 PM | main | not checked | no | no | (none) | **PROTECTED** | REPORTED (vault; not inspected) |
| 6 | `1` | public | 190,046 | Oct 5 5:04 PM | main | 0 | no | no | C2 | **PROTECTED** | TESTED (see reason) |
| 7 | `T44` | public | 190,743 | Oct 4 4:15 AM | main | 0 (not listed; 0 open issues) | no | no | (none) | **PROTECTED** | TESTED (see reason) |
| 8 | `olive-giant-ever-glade` | private | 127,233 | Oct 4 6:16 AM | cycle/chamber-text | 0 (open_issues 0) | no | no | (none) | **PROTECTED** | TESTED (see reason) |
| 9 | `Grok-ready` | public | 191,888 | Oct 3 11:02 AM | main | **3** (#3, #4, #5) | no | no | Consolidation destination for Tessera repositories… | **CONSOLIDATE** | TESTED |
| 10 | `TESS` | public | 188,791 | Oct 1 10:59 PM | main | 0 (open_issues 0) | no | no | (none) | **CONSOLIDATE** (archive-only remainder) | TESTED |
| 11 | `tessera-grok-handoff` | public | 205,256 | Oct 3 10:08 AM | main | 0 | no | no | Privacy-screened Tessera handoff files… | **UNKNOWN** | TESTED meta / UNKNOWN content |
| 12 | `tessera-grok-handoff-complete` | public | 160,371 | Oct 1 10:59 PM | main | 0 | no | no | Sanitized combined Tessera archive handoff | **UNKNOWN** | TESTED meta / UNKNOWN content |
| 13 | `tessera-complete-archives` | private | 158,436 | Oct 1 10:59 PM | main | 0 | no | no | Private complete … archive; credential literals redacted | **UNKNOWN** (+ secrets flag) | TESTED meta / REPORTED redaction |

Open-PR counts for T44, TESS, olive, and the archive repos come from `open_issues_count = 0` in the search result (TESTED). GitHub counts open PRs inside open_issues, so 0 means no open PRs. `list_pull_requests` was run directly on TESSERA, Gitbook, Grok-ready, Zz, and 1.

## Class counts

| Class | Count | Repos |
|---|---:|---|
| KEEP | 4 | TESSERA, Gitbook, Zz, 5t |
| CONSOLIDATE | 2 | Grok-ready, TESS |
| DUPLICATE | **0** | — |
| EMPTY/TRIVIAL | **0** | — (the 8 empty/100%-covered repos were already deleted earlier today per Gitbook `merge/DELETION-MANIFEST.md`, REPORTED: Everything, TX, Tessera-main, tessera-coordination, tessera-gitbook, tessera-replit, tessera-unified, z) |
| PROTECTED | 4 | 1T, 1, T44, olive-giant-ever-glade |
| UNKNOWN | 3 | tessera-grok-handoff, tessera-grok-handoff-complete, tessera-complete-archives |

## Per-repo reasoning

- **TESSERA**: KEEP (destination code). It has 1,385 blobs on main. CI run 37382015797 is green on `5c1137fa` (TESTED earlier in INVENTORY.md).
- **Gitbook**: KEEP (destination docs). It has 128 blobs on main. Board issue #2 is open.
- **Zz**: KEEP (in use). A Replit Agent wrote to main twice today. HYB-007 marks Z9 colonel, Z10 own-lab, Z11 vow-check, and Z14 world as **RETAINED** in Zz (REPORTED, `merge/hyb-007-z-app.md`). It also has unique `.agents/memory` notes, `tessera-control/` READMEs, and a `chamber/desk` note that differs from the Gitbook copy. Per the rule it is **not copied wholesale**. It also contains sensitive-review paths: 16 per `full-audit-report.json` (REPORTED), plus `data/ingest|drive|school|inbox|checkouts` runtime state (TESTED path names only) and a `father-profile.ts` that injects a natal chart (REPORTED, HYB-007 Z20). Never a delete candidate until Replit is detached and the CONS items are done.
- **5t**: KEEP (in use). A Replit Agent appended `shepherd-audit.jsonl` six times today. It holds the **only surviving copies** of the deleted TX repo's local branch blobs and snapshot diffs (`.agents/outputs/tx-*`, 11 files, ~4 MB, uncovered by dest+siblings: TESTED). It also has unique audit/runtime data and `applicant-declarations.jsonl` / `declarations.jsonl`, which may be third-party personal data (UNKNOWN; bodies not opened).
- **1T**: **PROTECTED**. Vault, never a delete candidate, not inspected. Pushed today 5:09 PM CT.
- **1**: **PROTECTED**. Main is fully duplicated: 0 uncovered blobs once 5t/T44/TESS are counted (TESTED). But branch `subrepl-nftoz8d7` (unrelated history, live Replit writes today) holds 1,629 blobs found nowhere else, including `artifacts/api-server/.local-data/natal-vault.json` (personal/secret-class data by path name; body not opened), 1,520 `_evolutions/*` generated files, and 161 `attached_assets/*` (173 MB).
- **T44**: **PROTECTED**. Only 2 blobs are unique after counting siblings (TESTED). One is `artifacts/api-server/.local-data/natal-vault.json` (personal/secret-class data, unique to T44, body not opened). The other is an older `artifacts/tessera/public/opengraph.jpg`. With the natal vault moved to Father's private storage, T44 would otherwise be nearly a duplicate. Father decides.
- **olive-giant-ever-glade**: **PROTECTED**. It is a separate app with its own `better-auth`/PGlite auth (`src/lib/auth/*`), `data/ingest` (1,624 files), `data/drive`, `data/school`, `attachments/` (47), `screenshots/` (14), and `.vercel/output` (TESTED path names). That data is out of scope for inspection per the TESSERA `tessera-pen-gate` AGENTS.md guard (TESTED file on branch) and HYB-008/011. 9 sensitive-review paths per the audit (REPORTED). Not copied wholesale (rule). 2,123 of its uncovered blobs also exist in Zz (TESTED).
- **Grok-ready**: CONSOLIDATE. 1,271/1,293 blobs are already in TESSERA+Gitbook. 5 blobs are unique: `docs/migration-review/{raw-media-inventory.json, remote-archive-verification.json, represented-at-other-paths.json}`, root `README.md`, and `.gitignore`. 3 open unreviewed PRs: #3 redaction, #4 private ZIP chunks, #5 unlicensed `amber-flame-tiger-sand` source with a credential-pattern blob withheld (REPORTED in `review/source-branch-review.md`). HYB-006: no missing code port (REPORTED).
- **TESS**: CONSOLIDATE (archive-only remainder). 2 blobs are unique after counting siblings: `artifacts/api-server/data/ingress-audit.jsonl` (84 B) and `shepherd-audit.jsonl` (54 KB) (TESTED). Everything else not in TESSERA/Gitbook is the shared `attached_assets/` media family (182 files, 212 MB, also in 1/5t/T44) plus runtime data. It becomes a **DUPLICATE candidate** only after CONS-016 (media home decided and kept) and CONS-014 (audit logs summarized). Because it depends on sibling repos that are themselves retained, it is not listed as safe today.
- **tessera-grok-handoff / -complete / tessera-complete-archives**: UNKNOWN. These are chunked ZIP payloads (`*.zip.part-*`, 26/312/312 parts). Their readable summaries are already in Gitbook `history/handoffs/` (TESTED: `privacy-screened-handoff-summary.md` 10,682 B matches the handoff README size; the 3 covered handoff files are exact blobs). The payloads are not in TESSERA/Gitbook. Zz `artifacts/z-app/imports/trees/` contains folders named after each ZIP (`tessera-grok-handoff--grok-workspace_1789591148371`, etc.), so the contents may have been unpacked into Zz (REPORTED by path name, not byte-verified). `tessera-complete-archives` says "credential literals redacted" (REPORTED, not TESTED), so treat it as possibly holding secrets. `-complete` also has 4 unique screenshot-supplement files (2.2 MB).

## Protected items for Father (never delete candidates)

1. `1T` vault: not inspected, not copied, never deleted by Tessera.
2. `natal-vault.json` in `T44` main and `1`/`subrepl-nftoz8d7` (personal/secret-class by path; bodies not opened).
3. `olive-giant-ever-glade` auth + `data/` + `attachments/` + `screenshots/`.
4. `applicant-declarations.jsonl`, `declarations.jsonl`, `lattice-*.jsonl` in `5t`/`TESS` (possible third-party personal data; UNKNOWN).
5. `tessera-complete-archives` (redaction claim only REPORTED) and Grok-ready PR #4 (ZIP holds excluded browser/runtime/private material, REPORTED).
6. Wallet/payments/blockchain code paths (`wallet-observer.ts`, `TokenEconomyPage.tsx`, etc.) exist in TESSERA and the snapshots. They were not touched and are not consolidation items.

## Not checked / blocked

- `1T` branches/PRs/tree: **not inspected** (PROTECTED by rule).
- Origin `collin-keane/Tessera`: **BLOCKED** (cursor-origin `list_namespaces` returned `[]` per INVENTORY.md).
- File bodies of runtime/data/secret-class paths: intentionally **not opened**.
