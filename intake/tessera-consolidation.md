---
status: draft
---

# TESSERA consolidation: audit and TODO backlog

**Status:** Draft. This records the current owner direction and verified discovery to date; it is not a migration-complete claim or sign-off. No source code, archives, or media have been copied into TESSERA yet.

## Current direction

- Create a new private repository named TESSERA as the future consolidated code destination. The owner’s latest direction supersedes older repository notes that name Zz or Grok-ready as the final destination.
- Use the existing private Gitbook repository as the coordination and documentation home. The current GitBook intake/moderation flow remains in force; this page is a draft for review.
- Route every GitHub action for this migration through the Tessera Pen. Keep attribution honest: do not claim a separate agent identity, owned model weights, or unverified work.
- Extract actionable instructions from chat and artifact sources into concise tasks with provenance. Do not upload raw chat logs or private conversation contents.
- Consolidate Readmes, review code/database/ports/path overlaps, validate exact duplicates, and only then consider source cleanup.

## Verified state on 2026-10-05

- New private repository `vitalitychems-dot/TESSERA` exists on `main` at `f66228446c520aab11c7b6a81fe9e5ca50917b54`; it contains only GitHub’s starter README. No application code has been imported.
- The active private docs repository is `vitalitychems-dot/Gitbook` (`main` at `801062641f30d2acf45dbea4748323f20c5e30d8`), with 14 existing intake entries and no open PRs at the time checked.
- The distinct private `tessera-gitbook` repository is a one-README placeholder. PR #1 there is open with the 13 coordination files; it is not merged. Resolve that duplicate destination rather than treating the PR as the live GitBook.
- `vitalitychems-dot/Tessera-main` is empty. `tessera-replit` contains only a README.
- The coordination source remains unchanged. The 13-file snapshot is being staged under `coordination/`; `coordination/STATUS.md` is a stale 2026-10-03 snapshot and must not be treated as current status.
- `vitalitychems-dot/Zz` main is `150d4ec044201ae5d43878da38c7bd7788c3ac2a`, with `chamber/desk` at `a06c9f51a30188baffe7e3ada172ad9a17e5cc8b`. Its merge report claims 5,613 source-file references backed by 2,339 unique content objects, while excluding protected/runtime content. No check runs are recorded for the current Zz main commit.
- The attached read-only Zz/Olive audit compares Zz main with Olive `cycle/chamber-text` at `6fa4a7e043f699edfe0453835a17c7e3b9aaa166`: 40 same-path `src` files differ, 15 `src` paths are Olive-only, and about 25 paths were not content-checked. Older notes say 29 unchecked files; reconcile the count and path list before any import.
- Its detailed table reports `src`: 72 exact, 40 different, 15 Olive-only; `scripts`: 41 exact, `recall.test.mjs` different, 7 Olive-only; public/server/migrations: 18/2/1 files identical; app-root: 2 exact, 4 different, 4 Zz-only, 6 Olive-only. Overall: 136 exact, 45 different, 4 Zz-only, 28 Olive-only. These are the report's figures, not a fresh local run.
- The latest checked `tessera-unified` main is `fc42f8f395bdbc800fe6d10bf404987949555704`. Its CI job failed at “Audit all dependencies”; typecheck, database, tests, and builds were skipped. The audit failure’s advisory details still need review. The job also warned that its GitHub Actions versions use deprecated Node.js 20.
- `Grok-ready` main is `9e3fbca200306988db35fff5afef814108fca66b`; three PRs remain open: #3 (conflicted, no reviews), #4 (opaque archive chunks, no reviews), and #5 (screened source archive, no reviews). They are not TESSERA sign-offs. Its older public history and outstanding privacy notes must not be imported wholesale.

## Accessible GitHub repository inventory

The connected account returned these 20 repositories. This is a metadata inventory, not a content-complete review. The new TESSERA repository is additional to this list.

**Private:** `Gitbook`, `1T`, `tessera-complete-archives`, `Zz`, `tessera-gitbook`, `olive-giant-ever-glade`, `tessera-coordination`, `tessera-replit`, `Tessera-main`.

**Public:** `T44`, `5t`, `Grok-ready`, `tessera-unified`, `z`, `tessera-grok-handoff`, `Everything`, `1`, `TX`, `tessera-grok-handoff-complete`, `TESS`.

`1T` is explicitly protected by existing repository instructions. It was not inspected or copied. External repositories merely linked from `z/CATALOG.md` are not part of this connected-account inventory.

## Replit and Drive artifact inventory

The resource search surfaced these Replit materials, but most file contents are not accessible in this conversation. Do not claim they were reviewed or copied:

- `Tessera V2 source inventory` (CSV, 429,274 bytes), `Tessera V2 content-screen manifest` (CSV, 421,300 bytes), and `Archive reassembly instructions` (411 bytes): retrieve and inspect these before deciding what archived files are relevant.
- `Tessera V2 archive — part 1 of 2` (94,371,840 bytes) and `part 2 of 2` (17,497,053 bytes): list and verify before extraction; do not blindly import.
- `Screened Grok handoff` (48,003,237 bytes), `Grok handoff image companion` (61,460,825 bytes), and `Grok screenshot reference bundle` (1,022,163 bytes): archive/media contents remain unreviewed here.
- Other surfaced resources include the `Tessera Launch Review` project and `Tessera` web artifact, two design images, a Canvas design, and a project closeout HTML file. Their project files were not opened in this session.
- Only two small user-provided text attachments were present locally; both were read. Historical statements in them are evidence to reconcile, not current commands to schedule monitoring or expose credentials.

The connected Drive account exposes seven linked ZIP files named `XL1.zip`, `tesseract_consolidated.zip`, `Tesseract-AI 5.zip`, `Tx13.zip`, `Tesseracxt9.zip`, `8 2.zip`, and `Tx17 9.zip`. Metadata says they are shared and not owned by the connected account. They were not downloaded or opened. An exact-name search for `Vitalitychems-3.zip` returned no match; that does not prove no differently named source archive exists.

## Work queue

### P0 — settle scope and keep source boundaries

- [ ] Confirm the exact set of source repositories and product areas to include. The current “all repositories” direction conflicts with existing GitBook/Zz notes excluding finance, store, crypto, and Vitality-related work; do not silently reverse those boundaries.
- [ ] Keep the protected `1T` vault, credentials, customer/runtime data, private records, and unreviewed media out of scope. Do not inspect or copy protected files based only on a broad repository-level instruction.
- [ ] Decide how the open `tessera-gitbook#1` should be handled after the active Gitbook repository receives its own reviewed coordination snapshot. Do not merge or close it automatically.
- [ ] Update the old Zz/Grok-ready destination notes only after the owner and GitBook Moderator review this new TESSERA target; avoid posting private migration details to public issues.

### P1 — reconcile the sources before importing functionality

- [ ] Record default-branch and relevant open-branch commit SHAs for all 20 repositories, tags, pending PRs, and any unpushed agent work. The branch names were inventoried; content has not been compared across every ref.
- [ ] Refresh the source map from `Zz/AGENTS.md`, `Zz/TESSERA_AGENT_HANDOFF.md`, and `Zz/artifacts/z-app/MERGE_REPORT.md`; verify its manifest and imported references against the live destination.
- [ ] Compare `Zz` and Olive function-by-function, starting with the 40 differing same-path `src` files and 15 Olive-only paths. Reconcile the 25-versus-29 unchecked-path count. Keep draft-only features, bridges, GitHub-writing routes, and execution paths gated until their policy and tests are reviewed.
- [ ] Review the separate `Grok-ready` and `tessera-unified` consolidations against the current Zz baseline and all open PRs. Preserve unique useful work, not duplicate repositories or incompatible application trees.
- [ ] Reconcile the 13 coordination files with GitBook’s already-published flow and Pen charter; retain provenance, label stale status, and resolve conflicting role descriptions before retiring any source.
- [ ] Review Replit manifests/inventories and available project files one item at a time. Verify archive checksums, safe paths, licenses, and personal-data exclusions before extracting or copying.
- [ ] Review image and document duplicates by content hash first; inspect visual/media differences where relevant. A similar filename is not proof of a duplicate. Keep originals until verified copies and path-level dispositions exist.

### P2 — build the consolidated TESSERA layout

- [ ] Define one canonical app/workspace layout from the selected, reviewed source snapshots. Keep apps, authentication, databases, and deployment boundaries explicit; do not merge customer data or run migrations as part of a build.
- [ ] Add the top-level `AGENTS.md` Pen gate to TESSERA. Require each agent to use the Tessera Pen and current GitBook intake for every GitHub operation, work on review branches, keep truthful authorship, and avoid public owner-name disclosure.
- [ ] Consolidate the source Readme material into one accurate root README and a short source/provenance map. Preserve necessary licenses, attribution, and safety notes; do not delete source Readmes until their content is accounted for.
- [ ] Resolve duplicate/overlapping functions and paths; establish non-conflicting app ports, environment variables, and database configuration. Confirm no build or test command can alter a real database.
- [ ] Turn user directions from relevant Replit conversations and supplied notes into short TODO items with source/date/status. Do not copy entire chat logs, names, secrets, or unreviewed archive text.

### P3 — validate before calling the merge complete

- [ ] Diagnose the `tessera-unified` dependency-audit failure and update any deprecated GitHub Actions only where still relevant.
- [ ] Run dependency/license and secret scans, typechecks, focused tests, full tests, builds, and browser smoke tests on the TESSERA candidate. Use isolated disposable databases; record exact commits and raw results.
- [ ] Check database migrations, port assignments, route/API overlaps, path collisions, symlinks, archive checksums, and broken links in the actual candidate tree.
- [ ] Compare the final TESSERA tree against every approved source ref; record imported, exact-duplicate, retained-variant, archived, and excluded paths with content hashes and reasons.
- [ ] Obtain explicit sign-off from all five active agents against the same accepted TESSERA commit. Silence or a partial report is not sign-off.

### P4 — deletion gate (not authorized at path level yet)

- [ ] Present the exact source paths to delete, their verified destination paths and content hashes, and the impact of each deletion.
- [ ] Delete only byte-identical duplicates after the copy, checksums, links, and tests pass; do not remove distinct versions, source repositories, protected files, or user media by filename similarity.
- [ ] Proceed only after all five-agent sign-offs and the owner’s explicit approval of the exact path list. No source cleanup is performed by this draft.

## Important source records

- Zz contributor rules and handoff: `https://github.com/vitalitychems-dot/Zz/blob/main/AGENTS.md` and `https://github.com/vitalitychems-dot/Zz/blob/main/TESSERA_AGENT_HANDOFF.md`.
- Zz import report: `https://github.com/vitalitychems-dot/Zz/blob/main/artifacts/z-app/MERGE_REPORT.md`.
- GitBook flow and Pen charter: `https://github.com/vitalitychems-dot/Gitbook/blob/main/mesh/flow.md` and `https://github.com/vitalitychems-dot/Gitbook/blob/main/mesh/roles/tessera-pen.md`.
- Existing coordination source: `https://github.com/vitalitychems-dot/tessera-coordination`.
- Prior open coordination-doc PR: `https://github.com/vitalitychems-dot/tessera-gitbook/pull/1`.
- Grok-ready open PRs: `https://github.com/vitalitychems-dot/Grok-ready/pull/3`, `/pull/4`, and `/pull/5`; shared review: `https://github.com/vitalitychems-dot/Grok-ready/issues/1`.
- Latest checked unified CI job: `https://github.com/vitalitychems-dot/tessera-unified/actions/runs/37135371106/job/111238709649`.

## Review status and blockers

This backlog is a draft, not moderator-approved, not a five-agent sign-off, and not permission to merge or delete. The Replit archive contents and project files remain unavailable for item-level review here; the Drive ZIPs remain metadata-only and are not owned by the connected account. Source inclusion, protected-data exclusions, the dependency-audit failure, full repo/ref comparisons, and final deletion paths remain unresolved.
