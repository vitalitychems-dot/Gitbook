# HYB-011 exclusion manifest (refresh)

**Checked:** 2026-10-12, ~4:00 PM CT. Base: Gitbook `main` @ `cd8faa0`. Supersedes the 2026-10-05 root-name pass in `merge/HYB-011-EXCLUSION-MANIFEST.md` @ `cd8faa0`.
**Method:** default-branch root names via the GitHub contents API. No file bodies, zips, `parts/`, or `data/` trees were opened.
**Not opened:** `1T`. No API call was made against it.

## Live account (4 repositories)

| Repository | Head | Vis. | Root names that stay excluded (name only) | Secret-shaped root names |
|---|---|---|---|---|
| `TESSERA` | `a502322` | private | `data/`, `archive/`, `archives/`, `.agents/`, `.codebase-memory/`, `.replit` | `.env.example` (template; allowed per HYB-006 C16). No `.env`/`.pem`/`id_rsa` at root. |
| `Gitbook` | `cd8faa0` | private | `archive/` (incl. PR #39 `archive/preserved/`), `history/recovered/` exact records | none observed at root (root not re-listed) |
| `GitbookAI` | `b9945ad` | **public** | none. Never mirror private Gitbook into it (RULES 1–2). | none at root |
| `vitality` | `2cf2931` | private | `archive/` (drive-sections zip parts, `moved/collink1007-*`, `drive-rest/price-list.xlsx`), `attached_assets/`, `artifacts/vitality-supply/public/` | `.npmrc` (name only, not read). No `.env` at root. |

## Repositories no longer on the account (historical, name only)

`1`, `5t`, `Grok-ready`, `T44`, `TESS`, `Zz`, `olive-giant-ever-glade`, `tessera-complete-archives`, `tessera-grok-handoff`, `tessera-grok-handoff-complete`, `tessera-unified`, `1T`.
Prior rows are kept as history in the 2026-10-05 manifest. Where some were moved (e.g. `archive/moved/olive-giant-ever-glade`, per `merge/hyb-008-olive.md`), the archive path inherits the same exclusions.

## `1T` (protected)

Listed **by name only**. It is not among the 4 live repos. Do not open, inspect, copy, or delete. Gitbook's `merge/PROTECTED-1T-CLEANUP-2026-10-09.md` is referenced by name only and was not read in this pass.

## Pattern exclusions (applied to every repo and archive path)

- Secrets: `.env`, `.env.*` (except a blank `.env.example`), `*.pem`, `*.key`, `id_rsa*`, `*secret*`, `*credential*`, `*token*`, `.npmrc` contents, `.replit` secrets
- Runtime state: `data/**`, `data/ingest/**`, `data/school/**`, `data/drive/**`, `data/inbox/**`, `sandbox-runs/**`, `web-study/**`, `.codebase-memory/**`, `.agents/**`, local agent data
- Generated/archive bodies: `parts/**`, `*.zip`, `*.zip.part-*`, `imports/objects/**`, `.vercel/**`, held-packet / study-log bodies
- Wallet/customer/private: `*wallet*`, price lists (`*.xlsx` in vitality), order/customer exports, `father-profile*`, natal data (env only), vault shelves
- Protected: `1T`, anything with a `1T` path prefix

## Open gaps

- Deep-tree, value-redacted pass still not done (unchanged from 2026-10-05).
- TESSERA root has `data/` and `archives/`. Their contents are unverified, so HYB-014's secret-shaped-path gate is the check of record.
- Confirm that the deleted legacy repos reached 100% coverage first (HYB-018).
