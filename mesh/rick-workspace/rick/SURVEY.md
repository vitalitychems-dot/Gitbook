# SURVEY — full picture for Tessera v3 (2026-10-13, ~2:30 AM CT, read-only)

Method: du/find, zip central-directory reads (no unpacking), git log/status, GitHub public API and raw files, memory palace FTS. Nothing was pushed, posted or deleted.

## (a) /workspace/rick-audit (12.1G)
- **It is two clean clones of the two canonical repos**, not a unique archive: `Gitbook/` (12G: .git 6.4G + archive/ 5.9G) and `TESSERA/` (1.3G: .git 509M + archive/ 713M). `git status` is clean and there are 0 unpushed commits in both, so all of it can be re-cloned from GitHub.
- File types (outside .git): 4612 txt, 2347 ts, 1106 md, 912 tsx, 401 json, 257 png, 218 mjs, 100 jpg, 50 py, 44 jsonl.
- `Gitbook/archive/drive-rest/` (5.0G) holds the 2026-10-08 Google Drive dump, split into 45 MB parts. I read the central directories without unpacking. Each archive is a **Replit workspace snapshot** of an older Tessera app:

| Snapshot | Size | Entries | Real content (uncompressed) |
|---|---|---|---|
| XL1 | 3.05G | 5,707 | ~3.3GB deps/git/cache; app ≈ dist 14MB, server/conference-transcripts 202 files, client/src 175 files, routes.ts 2.2MB, sqa-audit-history.json |
| Tesseracxt9 | 0.66G | 56,467 | tess/server 1,267 files, tess/client 229, tess/data 39 |
| Tesseract-AI-5 | 0.42G | 36,711 | x/tess 1,006 files, artifacts/api-server 195 |
| Tx17-9 | 0.43G | 40,049 | x/tess 1,255, api-server 74, tess-app 84, lib/db 30 |
| Tx13 | 0.38G | 38,230 | x/tess 1,127, api-server 33, tess-app 81 |
| 8-2 | 0.36G | 38,316 | x/tess 1,357, api-server 97 |
  About 90–95% of the entries in every snapshot are node_modules, .git, .cache or .config. The unique parts are the `tess` server/client trees and the attached screenshots.
- `archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip` (94MB, 1,138 files) = `tesseract_consolidated.zip` (same bytes, per drive-rest/README). It also appears again under rick-audit/TESSERA/archive/from-gitbook.
- **Chimera**: the only mention is in `history/recovered/zz-olive/...2026-10-06-rebuild-consolidation-draft.md`. It describes an uploaded "Chimera setup script" for a *separate project*, and the note says "Exclude from Tessera code". The script uses unsafe `tar.extractall()`, and it was never run. There is no Chimera source in any repo surveyed.

## (b) TESSERA (local TESSERA-ro, HEAD 3b3840c3)
- Monorepo with artifacts/{tessera (web :3000), api-server (:5000), mockup-sandbox, gitai (agent marketplace :4183), v2 (3D studio), gitbook-mcp} and lib/{db, api-zod, api-spec, api-client-react}. Real import graph: api-server→db (235 imports), api-server→api-zod, tessera→api-client-react.
- Build decision (README): BHNMC direction. "The device is not built."
- Recent: OPT-26 (#246), Rick's OPT round 2 (#247).
- **Flag for Father/Security, HEAD 3b3840c3 "Make GitAI review work look like ordinary bounties" (00:21 UTC Oct 13 = 7:21 PM CT Oct 12).** This commit removes the probation and observation labels from GitAI agents' sessions. It reduces the monitoring notice to one sentence in the sign-up terms, so test or review tasks are disguised as ordinary bounties. That is covert evaluation of other agents. It conflicts with the Gitbook honesty rules (roles/honesty-banner.md), so I recommend a Moderator and Security review. I changed nothing.

## (c) collink1007 public repos (4)
| Repo | Updated | Lang | Tessera relation |
|---|---|---|---|
| amber-flame-tiger-sand | 2026-10-02 | JS | Grok Build app-builder sandbox (AGENTS.md, .grok skills, server/src, vercel). Its drive zip is already archived in Gitbook as 1e3Vip.zip |
| z | 2026-10-03 | JS | Same template plus TESSERA.md and FATHER.md ("stays under the Father protocol… A card marked BUILT is not a machine in the room") = a chamber snapshot |
| XXX | 2026-09-15 | TS | Replit "Tessera Sovereign 2DA Platform": pnpm monorepo, 25+ agents, Grand Council voting, "autonomous income engine" and blockchain. It overlaps the drive-rest `x/tess` trees. Its income and blockchain parts are out of scope (no crypto or wallets) |
| fleet-moss-monarch-rapid | 2026-09-14 | JS | Same template. The Fleet-Moss site archives were moved to vitality (out of scope) |
None of them has a README. None contains "chimera" in its top-level files (GitHub code search needs auth, so I didn't do a deep search).

## (d) Gitbook (mesh/, intake/, roles/)
- Rules: RICK.md, roles/*.md (15 lanes including honesty-banner and pen-gate), status-definitions (gates return `changes needed` and never set BLOCKED; only the owner, Tessera or Father can block), THREE-WAY-COLLAB-PROTOCOL (Cursor↔Replit↔Grok ownership table), COLLABORATION-PLAYBOOK and METRICS, TODOS, ORDER-NOW, FATHER-ASKS.
- Coordination state lives in free text spread across Gitbook issue #2, HANDOFF.md (last full pass 2026-10-05; most lanes show "No X-signed check-in"), TODOS.md and OPEN-ITEMS. The same item appears in several snapshots (gitbook-cordnation keeps base and proposed copies). **The main pain point is that nothing machine-readable says who owns what or which gate comes next.**
- Measured: the conflict scanner found 7 IDs claimed by more than one lane in gitbook-cordnation (24,615 lines). I checked them by hand: about 1 is a real ambiguity (HYB-013, "claim unclear"), and the other 6 are gate approvals or rows marked "unclaimed". Free-text claim parsing is unreliable, which is the case for invention #1 (a structured bus).

## Coverage of the full-picture load
See tools/fullpicture/ and V3-PLAN.md.
