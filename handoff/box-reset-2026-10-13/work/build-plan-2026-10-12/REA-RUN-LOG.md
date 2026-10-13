# REA run log — batch 1 (cap 25)

**As-of:** 2026-10-12 4:02 PM CT  
**Father yes:** start rea on archive names from `REPO-NAMES-FROM-LOGS.md` that live under Gitbook/TESSERA trees.  
**Tool:** `rea-agents@6.4.0` via `npx -y rea-agents@latest analyze-javascript-application <dir> --json`  
**Node:** system was v20.19.2 (below REA’s ≥22 requirement). Installed portable **Node v22.19.0** at `/workspace/tools/node22` (no system change).  
**Scope:** vitalitychems-dot owned archive content only. **No push. No Claude-Red. No 1T/vault path opens.**

---

## Environment notes

| Item | Result |
|---|---|
| REA CLI install (`npx`) | **OK** after Node 22 + `mkdir -p /home/box/.local/lib` (first npx failed ENOENT on that path) |
| `gh auth` on box | **Not logged in** — cannot sparse-clone private Gitbook/TESSERA archives for full REA |
| Local clone usable for REA | `/workspace/repo-lab/vitalitychems-dot__Grok-ready` (full JS tree) |
| Remote archives | Structure via `cursor-github` `get_git_tree` / `get_file_contents` (names + selective source samples) |

---

## Batch of 25 (priority)

Prefer TESSERA `archives/source-repositories` + `source-variants`, then Gitbook `archive/moved` / `archive/drive-rest` uniques. Cap = 25.

| # | Folder | Location | Mode | Result |
|---:|---|---|---|---|
| 1 | `Grok-ready` (full local clone) | `/workspace/repo-lab/vitalitychems-dot__Grok-ready` | **REA** | PASS — 804 parsed JS, 6083 findings, graph 2806n/3461e (partial) |
| 2 | `Grok-ready/artifacts/tessera` | same clone | **REA** | PASS — 245 parsed JS, 1708 findings, 24 endpoints, 13 storage |
| 3 | `Grok-ready/artifacts/api-server` | same clone | **REA** | PASS — 331 parsed JS, 3400 findings, 13 endpoints |
| 4 | `Grok-ready/artifacts/mockup-sandbox` | same clone | **REA** | PASS — 67 parsed JS, 816 findings, coverage **complete** |
| 5 | `Zz` | TESSERA `archives/source-repositories/Zz` | **inventory** | 235 blobs, 180 js/ts, 5 package.json — **REA blocked** (no local checkout; gh unauth) |
| 6 | `olive-giant-ever-glade` | TESSERA `archives/source-repositories/olive-…` | **inventory + content sample** | 32 blobs, 18 js/ts, 1 package.json — key Tessera UI modules read via MCP (not full REA; incomplete local tree) |
| 7 | `1` | TESSERA source-repositories + source-variants | **inventory** | sr: 2 blobs / sv: 5 js — thin |
| 8 | `5t` | TESSERA sr + sv; Gitbook moved | **inventory** | sr thin; sv 6 js; Gitbook moved 22 blobs / 0 js |
| 9 | `Everything` | TESSERA source-variants | **inventory** | 1 blob, 0 js |
| 10 | `T44` | TESSERA sv + Gitbook moved | **inventory** | **sv: 57 blobs / 52 js** (richest variant); Gitbook moved pointer-thin |
| 11 | `TX` | TESSERA source-variants | **inventory** | 2 blobs, 0 js |
| 12 | `tessera-complete-archives` | TESSERA sv | **inventory** | 2 blobs, 0 js |
| 13 | `tessera-grok-handoff` | TESSERA sv; local zip-parts only | **inventory** | 1 blob in tree; local `/workspace/repo-lab/vitalitychems-dot__tessera-grok-handoff` is split zip — not REA’d |
| 14 | `tessera-grok-handoff-complete` | TESSERA sv | **inventory** | 2 blobs, 0 js |
| 15 | `TESS` | Gitbook `archive/moved/TESS` | **inventory** | 3 blobs, 0 js |
| 16 | `collink1007-XXX` | Gitbook moved | **inventory** | **991 blobs / 786 js / 4 pkgs** — top REA candidate next (needs checkout) |
| 17 | `collink1007-amber-flame-tiger-sand` | Gitbook moved | **inventory** | 49 blobs / 26 js / 1 pkg |
| 18 | `collink1007-z` | Gitbook moved | **inventory** | 29 blobs / 11 js / 0 pkgs |
| 19 | `8-2` | Gitbook drive-rest | **inventory** | 9 blobs, 0 js |
| 20 | `Tesseract-AI-5` | Gitbook drive-rest | **inventory** | 10 blobs, 0 js |
| 21 | `Tesseracxt9` | Gitbook drive-rest | **inventory** | 15 blobs, 0 js |
| 22 | `Tx13` | Gitbook drive-rest | **inventory** | 10 blobs, 0 js |
| 23 | `Tx17-9` | Gitbook drive-rest | **inventory** | 11 blobs, 0 js |
| 24 | `XL1` | Gitbook drive-rest | **inventory** | 66 blobs, 0 js (mostly non-JS) |
| 25 | `Zz` (Gitbook mirror) | Gitbook `archive/moved/Zz` | **inventory** | **4895 blobs / 1404 js / 26 pkgs** — largest archive; REA next after checkout |

---

## Skipped (by rule)

| Skip | Why |
|---|---|
| `archive/moved/1T` (Gitbook) | Name contains `1T` — not opened, not inventoried beyond existence in listing |
| Any path with `vault` | Vault rule / HYB-011 |
| Claude-Red / attack packs | Standing refuse (even for “own” vuln testing) |
| Catalog **card** / **held** / **tool** / **vitality** names from the 271 list | Not nested vitalitychems-dot archive folders; out of this batch scope |
| Runtime / device / network-capture REA modes | TOOLS-REA: static JS only |
| Hopper / IDA / Ghidra | Not needed for JS source trees |

---

## REA outputs (on box)

| Path | Notes |
|---|---|
| `rea-out/Grok-ready.json` | ~70 MB NDJSON (progress + Evidence) |
| `rea-out/Grok-ready__artifacts_tessera.json` | ~53 MB |
| `rea-out/Grok-ready__artifacts_api-server.json` | ~57 MB |
| `rea-out/Grok-ready__artifacts_mockup-sandbox.json` | ~23 MB |
| `rea-out/compact/*.compact.json` | Small summaries |
| `rea-out/compact/endpoints.json` | Deduped endpoint values |
| `rea-out/inventory-batch25.json` | Structure inventory rows |

---

## Sample findings (TESTED / static)

### A. REA on `Grok-ready` local clone

**Statistics (root):** relevant_files 850 · parsed_javascript_files **804** · findings **6083** · parse_failures **0** · text_bytes_read ~13.3 MB · graph coverage **partial** (semantic budget limits; modules still inventoried).

**Packages seen:** `@workspace/api-server`, `@workspace/tessera`, `@workspace/mockup-sandbox`, `@workspace/db`, `@workspace/api-zod`, `@workspace/api-spec`, `@workspace/api-client-react`, `@workspace/scripts`, `tessera-independent-service` (under docs/grok-packet safe sources).

**api-server endpoints (AST, inert):**  
`/healthz`, `/diagnostics`, `/ws`, `/world`, `/world/agents`, `/world/moon`, `/world/sovereignty-score`, `/provider-sovereignty/providers`, `/tesseract-forum/topics`, `/tsrt/full-market`, plus fetch targets `http://127.0.0.1:3000/health`, `https://allowed.example/resource`, `https://untrusted.replit.dev/private`.

**artifacts/tessera UI routes / fetches (sample):**  
`/fleet`, `/swarm`, `/life`, `/intelligence`, `/arbitrage`, `/income`, `/market`, `/rules`, `/code`, `/tesseract`,  
`/api/feedback`, `/api/moltbook/chat`, `/api/deep-training/status`, `/api/unified-training/state`, `/api/tesseranet/colonel`, `/api/admin/auth`, `/api/keys/bulk-detect`, `/api/wallets/scan`, `/api/natal-chart/identity/verify`, `/api/tessera-bible/secrets`, …

**Root-level API fetch strings also include:** `/api/2da/awareness`, `/api/2da/full-state`, `/api/agi/goals/decompose`, `/api/bio-consciousness/*`, `/api/provider-sovereignty/*`, `/api/conscious-builder/*`, `/api/nexus/recruitment-status`.

**Module export sample:** `src/lib/agent-spawner.ts:getSpawnerMetrics` (api-server).

**Storage (tessera UI):** `localStorage` / `sessionStorage` keys such as `tessera-font-color`, `tessera-voice-speed`.

**Electron:** mockup-sandbox marked coverage complete; root shows a few `electron-renderer` HTML entry refs — not a full Electron app analysis.

**Safety / product flags (for Improve plan, not executed here):**
- Several route names look **held/trading/vault-adjacent** (`/api/wallets/scan`, `/income`, `/arbitrage`, `/api/natal-chart/…`, `/api/tessera-bible/secrets`). Treat as **exclusion / gate candidates** under HYB-011 — do **not** wire into Tessera mind without a separate Father yes + Security.
- Static only: REA did **not** execute bundles or hit live networks.

### B. Olive archive content sample (MCP file reads — not full REA)

From `TESSERA/archives/source-repositories/olive-giant-ever-glade/` (package name `app-builder-workspace`):

- **Stack:** Vite 8 + TanStack Start/Router + React 19 + Nitro/Vercel + better-auth + PGLite/Kysely + Zod 4.
- **UI shell:** `AppShell` nav — Chamber / World / Board / Conversations / Bible / Secrets / Knowledge / Narrative / Self / Council / Memory / Code / Language.
- **Chamber:** yes/no board approvals via `postApproval`; untrusted web/GitHub file append; `speakAsTessera` pen; Learn button with `vowCheck`.
- **WorldStage:** Chicago-local clock, Esri imagery tiles, agent dots (Grok/Cursor/Replit/Desk), `LIST_DONE` banner — “map is a picture, not a fact.”
- **chat.ts:** pen resolution order self-hosted → local OpenAI-compatible → xAI; modes chat/learn/awaken/…; recall from school/imports/ledger; **VAULT_INDEX titles only** in prompt (vault bodies not opened here).
- **github-desk.ts:** secret-shaped regex refusal; duplicate-guard on board posts; issues 2/3/4 coordination patterns.
- **tessera-worker.mjs:** ingest loop over former repo names including **`1T` in the REPOS array** — worker itself skips natal/wallet/secret paths by regex; we did **not** follow 1T contents.

### C. Structure inventory highlights (next REA targets)

| Archive | Why next |
|---|---|
| Gitbook `moved/Zz` | 1404 js / 26 pkgs — largest |
| Gitbook `moved/collink1007-XXX` | 786 js / 4 pkgs |
| TESSERA `sv/T44` | 52 js without package.json (likely extracted modules) |
| Gitbook `moved/olive` | 48 js (built `.vercel` chunks + source) |
| TESSERA `sr/Zz` | 180 js (smaller mirror of Gitbook Zz) |

---

## Link to improve / test plan

See `IMPROVE-TESSERA-PLAN.md`. Immediate TESTED-metric follow-ups suggested by this batch (still need Security → Build → bulk yes before product merges):

1. **Product RAG (#1)** — olive/Grok-ready already speak through pens + recall; port BM25/harness path into live `ask-*` with quiz 0.28 → ≥0.72.
2. **Chamber / Board (#2, #13)** — olive `Chamber` + `BoardView` are reference UIs; compare to current `preview/src` for missing flows (Z10 / own-lab).
3. **Exclusion refresh (#15 / HYB-011)** — add REA-found wallet/natal/secrets route names as **name-only** exclusion rows; do not open vault.
4. **Repo-ask (#14)** — answer “what archives?” from `NESTED-REPO-MAP.md` + this inventory (≥20 basenames).
5. **Duplicate-guard (#17)** — olive `github-desk` + worker hash ingest already encode the pattern; keep on import PRs.
6. **CI (#5)** — still blocked on GitHub Actions billing (separate Father action).

---

## Blockers / next batch

1. **`gh auth login`** (or other approved private checkout) so REA can run on Zz / collink1007-XXX / T44 / olive full trees.  
2. Cap next REA batch at those 4–5 richest folders; keep static-only.  
3. Optional: delete or compress raw `rea-out/*.json` (200+ MB) after compact extracts are committed to planning docs — **not done** this turn.  
4. Do **not** treat REA endpoint lists as permission to enable trading, wallet scan, or vault features.

---

## Acceptance for this pass

- [x] REA CLI available on Node 22  
- [x] Cap 25 folders processed (REA or inventory)  
- [x] 1T / vault / Claude-Red skipped  
- [x] Sample findings recorded  
- [x] No git push  
- [ ] Full REA on remote archives — **blocked** until private checkout available  

---

# REA batch 2/3 — 2026-10-12 (progress checkpoint 4:55 PM CT)

**Method:** shallow `gh repo clone --depth 1 --filter=blob:none --sparse`, sparse rules exclude `**/1T/**` and `**/*vault*/**`; REA `rea-agents@6.4.0 analyze-javascript-application --json` on Node 22; no code executed, no push/PR/issue.
**Finding:** T44 / Zz / collink1007-XXX / olive are NOT standalone repos under vitalitychems-dot — they are archive folders (Gitbook `archive/moved/*`, TESSERA `archives/source-variants/T44`). Scanned those.
**Inventory:** `REPO-INVENTORY.csv` — 314 unique repo refs (gh list + grep of clones/notes + archive folder names). 9 accessible, 305 `n` (404 to this token: [REDACTED] → BLOCKED/UNKNOWN). Origin `collin-keane/Tessera`: BLOCKED (scm_repo_not_accessible). `gh repo list collin-keane`: owner not recognized.
**REA status:** T44 TESTED (exit 0), olive TESTED (exit 0); XXX, Zz, TESSERA, vitality, GitbookAI, collink1007/{z,fleet-moss-monarch-rapid,XXX,amber-flame-tiger-sand}, TheTesseractAI/18 queued.

## Scope change 4:56 PM CT (Father): TESSERA + Gitbook only

Dropped: other accounts, mentioned-only repos, separate T44/Zz/olive/XXX clones, vitality, GitbookAI (their REA JSONs in `/workspace/rea-batch/b2-out/` are not used for conclusions; the b3-* collink1007/TheTesseractAI runs were killed). `REPO-INVENTORY.csv` (315 refs: 9 accessible, rest BLOCKED 404, Origin collin-keane/Tessera BLOCKED) stays as reference only.

**Checkout:** `gh repo clone --depth 1 --filter=blob:none --sparse`; sparse rules `!**/1T/**`, `!**/*vault*/**`. TESSERA also skipped duplicate mirrors `archives/source-repositories/{Zz,olive-giant-ever-glade}` and `archive/from-gitbook/` (same bytes as Gitbook archive/moved). Gitbook: all top-level dirs + `archive/moved/{T44,Zz,collink1007-XXX,olive-giant-ever-glade}`; 20 1T/vault paths in archive/moved never checked out. No code executed, no push/PR/issue/edit.

| Repo | REA | Relevant files | Parsed JS/TS | Findings | Parse fails | Label |
|---|---|---|---|---|---|---|
| TESSERA | exit 0 | 1405 | 1341 | 9327 | 0 | TESTED (static) |
| Gitbook (whole checkout) | exit 0 | 1094 | 952 | 14386 | 0 | TESTED (static); REA selected 952 of ~2,240 JS files on disk — rest UNKNOWN |
| ↳ Gitbook archive/moved/collink1007-XXX | exit 0 | 878 | 786 | 13294 | 0 | TESTED |
| ↳ Gitbook archive/moved/Zz | exit 0 | 137 | 115 of 1404 | 1336 | 0 | TESTED partial — 1290 files are `artifacts/z-app/imports/trees` (nested repo copies) → UNKNOWN |
| ↳ Gitbook archive/moved/olive-giant-ever-glade | exit 0 | 65 | 48 | 656 | 0 | TESTED (28 are built `.vercel` chunks) |
| ↳ Gitbook archive/moved/T44 | n/a | 3 files, 0 JS | — | — | — | REPORTED (real T44 code is TESSERA `archives/source-variants/T44`: 52 JS, REA exit 0, 1777 findings) |

Gitbook non-archive content is docs (brain, forum, history, intake, merge, mesh, operations, posts, review, state) — 3 JS files.

### Useful pieces → where they belong
| Piece | Source | Target |
|---|---|---|
| Offline queue + apiCache (IndexedDB) `lattice-mesh.ts` | TESSERA artifacts/tessera + Gitbook XXX copy | TESSERA `preview/src/lib/offline/` (see OFFLINE-INTERNET.md O2) |
| WebRTC full-mesh `multiplayer/p2p.ts` | TESSERA preview | keep; add LAN mode (O6) |
| file-mesh / mesh-net (tested stubs) | TESSERA preview | expand index (O1) |
| Chamber/WorldStage/github-desk duplicate guard | Gitbook olive | TESSERA preview Board (already noted batch 1) |
| api-server routes (86 route files), db schema, api-zod | TESSERA artifacts/api-server, lib/db | canonical — Gitbook XXX/Zz route copies are superseded |
| XXX `tess/client/src/pages` (78) + components (47) | Gitbook XXX | UI reference only; port per page, never wholesale |
| Zz `z-app/src/lib` (20) + components (19) | Gitbook Zz | reference; nested `imports/trees` = duplicates of TESSERA/Grok-ready |

### Excluded / risky routes (HYB-011, names only)
- TESSERA: `/api/income/{wallet,wallet/refresh,methods,processes,stats,strategies}`, `/api/agent-secrets/all`, `/api/arbitrage/state`, `/api/grand-council/secret-*`, `/api/natal-chart/father`, `/api/ad-exchange/income-tasks`; 144 files mention wallet/payment/crypto terms.
- Gitbook XXX: `/api/agent-wallets{,/transactions,/treasury}`, `/api/agent-secrets/all`, `/api/arbitrage/{scan,start,risk,opportunities,conference}`, `/api/ad-exchange/income-*`; 317 risky-term files.
- Gitbook Zz: `/api/income/{engine,execute-all,collect-all-profit,scan-airdrops,wallets}`, `/api/secret-knowledge/*`.
- Gitbook T44 variant (in TESSERA): `/api/wallets/scan`, `/api/sigil/father/natal-*`.
- **Secret-shaped strings (values not printed):** TESSERA `artifacts/api-server/src/__tests__/learning-memory.test.ts` (placeholder-like), `preview/src/lib/tessera/github-desk.test.ts` (1 `ghp_`-shaped, likely redaction fixture — UNKNOWN, Security to confirm); Gitbook `archive/moved/collink1007-XXX/tess/client/src/pages/CredentialsPage.tsx` (placeholder). `.env.example` only in TESSERA root; no real `.env`.

### Fully-absorbed candidates (for Father's safe-to-delete *checklist* — nothing deleted)
- TESSERA `archive/from-gitbook/` — likely mirror of Gitbook archive/moved (path names match; bytes NOT verified — UNKNOWN).
- TESSERA `archives/source-repositories/{Zz,olive-giant-ever-glade}` — likely mirrors of Gitbook copies (not byte-verified).
- Gitbook `archive/moved/Zz/artifacts/z-app/imports/trees/*` — nested copies (1290 files).
- Gitbook `archive/moved/T44` (3 files) — superseded by TESSERA source-variants/T44.

### Top consolidation candidates
1. Offline queue/cache from lattice-mesh → TESSERA preview (O2).
2. Service worker precache (from XXX pattern) → TESSERA preview (O3).
3. file-mesh real index from Gitbook pages (O1).
4. Dedupe the 3 archive mirror sets above (checklist only).
5. olive Chamber/Board + duplicate-guard → TESSERA preview Board.
6. HYB-011 exclusion list refresh with the route names above.
7. XXX client pages → per-page reference port list (no wholesale copy).

### Blockers
- Gitbook REA coverage 952/~2240 JS; Zz nested trees not analyzed (UNKNOWN).
- TESSERA CI still red (Actions billing) — not touched.

## 2026-10-12 18:20–18:45 CT round 3 + inventory impact
- Fresh TESSERA clone f6c9362, plus fleet-moss and amber REA. Results are in REA-COVERAGE-V2.md.
- Checked access for all 315 inventory names: 9 accessible (4 owned + 5 public collink1007/TheTesseractAI), 306 returned 404 or private.
- Ran a same-name GitHub search. It was rate-limited partway (search API 30/min). Same-name hits are other owners' repos, so they're listed as unverified and weren't REA'd.
- Wrote KEYLESS-SOURCES.md and REPO-IMPACT-part1.csv (rows 1-158). No pushes.
