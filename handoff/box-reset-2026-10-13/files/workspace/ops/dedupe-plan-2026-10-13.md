# Dedupe plan (DRY RUN) — 2026-10-13

Nothing deleted, no repo changed. Box script `/workspace/ops/dedupe-box.sh` is NOT executed.

## Box
Scanned /workspace + /home/box (excluded .git internals, node_modules, agent-data, browser profiles, 1T/natal-vault paths, /cursor/stores). Size→sha256.

- Groups: 18449
- Files involved: 145780
- Removable copies: 127331
- Bytes freeable: 17,091,487,221 (17.09 GB)

Keep rule: prefer /workspace/improvements or /workspace/ops, else newest mtime, else shortest path.

**Caveat:** most savings are files inside duplicate git clones/worktrees. Deleting individual files inside checkouts leaves them dirty; better action is removing whole redundant clones (see below) after confirming no unpushed work (`git status`, `git log @{u}..`).

### Top 10 wins

- 1779 MB — 19 extra × 93.6 MB — keep `/workspace/si/wt-fb/archive/from-gitbook/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip`
- 472 MB — 10 extra × 47.2 MB — keep `/workspace/si/wt-fb/archive/sections/3_9_1776105526328/part-01`
- 472 MB — 10 extra × 47.2 MB — keep `/workspace/si/wt-fb/archive/sections/3_9_1776105526328/part-02`
- 472 MB — 10 extra × 47.2 MB — keep `/workspace/si/wt-fb/archive/sections/3_9_1776105526328/part-03`
- 472 MB — 10 extra × 47.2 MB — keep `/workspace/si/wt-fb/archive/sections/3_9_1776105526328/part-04`
- 123 MB — 1 extra × 123.2 MB — keep `/workspace/build-gate/node-v22.20.0-linux-x64/bin/node`
- 105 MB — 3 extra × 35.0 MB — keep `/home/box/.cache/uv/archive-v0/01A4cdRzLiTGlmTz/mcp_server_appwrite/data/docs_index.npz`
- 62 MB — 13 extra × 4.8 MB — keep `/workspace/si/wt-fb/archive/from-gitbook/archive/moved/5t/artifacts/api-server/data/shepherd-audit.jsonl`
- 55 MB — 14 extra × 4.0 MB — keep `/workspace/si/wt-fb/archive/from-gitbook/archive/moved/collink1007-z/data/ingest/manifest.json`
- 51 MB — 13 extra × 3.9 MB — keep `/workspace/si/wt-fb/archive/from-gitbook/archive/moved/olive-giant-ever-glade/data/ingest/manifest.json`

### Freeable by top-level dir
- 6253 MB `/workspace/gitmesh/repo`
- 782 MB `/workspace/si/tsr`
- 782 MB `/workspace/si/wt-runner`
- 782 MB `/workspace/si/wt-lock`
- 782 MB `/workspace/einstein/r4`
- 782 MB `/workspace/build-gate/tessera`
- 781 MB `/workspace/einstein/round3`
- 778 MB `/workspace/rea-batch/tessera-v2`
- 743 MB `/workspace/tess-opt/archive`
- 743 MB `/workspace/tw/archive`
- 743 MB `/workspace/tv3/archive`
- 584 MB `/workspace/si/gb`
- 554 MB `/workspace/tb3/archive`
- 383 MB `/home/box/.cache`
- 252 MB `/workspace/rea-batch/b3-collink1007_z`
- 235 MB `/workspace/rea-batch/amber-flame-tiger-sand`
- 235 MB `/workspace/rea-batch/b3-collink1007_amber-flame-tiger-sand`
- 226 MB `/workspace/repo-lab/crewAIInc__crewAI`
- 185 MB `/workspace/si/node-v22.20.0-linux-x64`
- 58 MB `/workspace/build-gate/node-v22.20.0-linux-x64`

### Duplicate repo clones
- TESSERA (9+): /workspace/build-gate/tessera, si/tsr, tb3, tess-opt, codeowners-followup/TESSERA, einstein/r4, einstein/round3/tess, rea-batch/tessera-v2, tw (plus si/wt-* worktrees, tv3)
- Gitbook (5): sec-retro/gbfix/r, si/gb, codeowners-followup/Gitbook, gitmesh/repo (~6.2 GB of dup content), rea-batch/b2-Gitbook; plus 7 gitbook-gate-<sha> and ~20 build-gate/security-gate work-* checkouts without origin
- collink1007/amber-flame-tiger-sand ×2 (rea-batch/amber-flame-tiger-sand, rea-batch/b3-collink1007_amber-flame-tiger-sand)
- node-v22.20.0 extracted twice (build-gate/, si/)

## Repos (main, git tree recursive=1, grouped by blob SHA)

### TESSERA
- Duplicate groups: 94; real redundancy: 86; intentional: 8; touching locked paths: 0
- Redundant bytes (real): 3,473,145

- [real redundancy] 1922832B ×2: `archive/from-gitbook/archive/moved/Grok-ready/docs/migration-review/remote-archive-verification.json`, `archives/source-repositories/Grok-ready/docs/migration-review/remote-archive-verification.json`
- [real redundancy] 287371B ×2: `archive/from-gitbook/archive/moved/Grok-ready/docs/migration-review/raw-media-inventory.json`, `archives/source-repositories/Grok-ready/docs/migration-review/raw-media-inventory.json`
- [real redundancy] 264665B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/package-lock.json`, `archives/source-repositories/olive-giant-ever-glade/package-lock.json`
- [real redundancy] 201430B ×2: `archive/from-gitbook/archive/moved/5t/.agents/outputs/tx-local-branches-manifest.json`, `archives/source-repositories/5t/.agents/outputs/tx-local-branches-manifest.json`
- [real redundancy] 199933B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/data/imports/manifest.json`, `archives/source-repositories/olive-giant-ever-glade/data/imports/manifest.json`
- [real redundancy] 177196B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/data/imports/read.json`, `archives/source-repositories/olive-giant-ever-glade/data/imports/read.json`
- [real redundancy] 130450B ×2: `archive/from-gitbook/archive/moved/Grok-ready/docs/migration-review/represented-at-other-paths.json`, `archives/source-repositories/Grok-ready/docs/migration-review/represented-at-other-paths.json`
- [real redundancy] 20123B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/data/coordination/board.json`, `archives/source-repositories/olive-giant-ever-glade/data/coordination/board.json`
- [real redundancy] 17450B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/src/lib/tessera/chat.ts`, `archives/source-repositories/olive-giant-ever-glade/src/lib/tessera/chat.ts`
- [real redundancy] 15215B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/src/lib/tessera/identity.ts`, `archives/source-repositories/olive-giant-ever-glade/src/lib/tessera/identity.ts`
- [real redundancy] 13964B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/src/components/tessera/chamber.tsx`, `archives/source-repositories/olive-giant-ever-glade/src/components/tessera/chamber.tsx`
- [real redundancy] 13496B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/src/components/tessera/board-view.tsx`, `archives/source-repositories/olive-giant-ever-glade/src/components/tessera/board-view.tsx`
- [real redundancy] 12314B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/src/lib/tessera/github-desk.ts`, `archives/source-repositories/olive-giant-ever-glade/src/lib/tessera/github-desk.ts`
- [real redundancy] 10135B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/scripts/tessera-worker.mjs`, `archives/source-repositories/olive-giant-ever-glade/scripts/tessera-worker.mjs`
- [real redundancy] 8608B ×2: `artifacts/mockup-sandbox/src/components/ui/menubar.tsx`, `artifacts/tessera/src/components/ui/menubar.tsx`
- [real redundancy] 7606B ×2: `artifacts/mockup-sandbox/src/components/ui/dropdown-menu.tsx`, `artifacts/tessera/src/components/ui/dropdown-menu.tsx`
- [real redundancy] 7569B ×2: `artifacts/mockup-sandbox/src/components/ui/calendar.tsx`, `artifacts/tessera/src/components/ui/calendar.tsx`
- [real redundancy] 7406B ×2: `artifacts/mockup-sandbox/src/components/ui/context-menu.tsx`, `artifacts/tessera/src/components/ui/context-menu.tsx`
- [real redundancy] 6750B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/vite.config.ts`, `archives/source-repositories/olive-giant-ever-glade/vite.config.ts`
- [real redundancy] 6477B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/src/components/tessera/world-stage.tsx`, `archives/source-repositories/olive-giant-ever-glade/src/components/tessera/world-stage.tsx`
- [real redundancy] 6210B ×2: `artifacts/mockup-sandbox/src/components/ui/carousel.tsx`, `artifacts/tessera/src/components/ui/carousel.tsx`
- [real redundancy] 6098B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/data/web-study.json`, `archives/source-repositories/olive-giant-ever-glade/data/web-study.json`
- [real redundancy] 6044B ×2: `artifacts/mockup-sandbox/src/components/ui/field.tsx`, `artifacts/tessera/src/components/ui/field.tsx`
- [real redundancy] 5745B ×2: `artifacts/mockup-sandbox/src/components/ui/select.tsx`, `artifacts/tessera/src/components/ui/select.tsx`
- [real redundancy] 5450B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/src/components/tessera/app-shell.tsx`, `archives/source-repositories/olive-giant-ever-glade/src/components/tessera/app-shell.tsx`
- [real redundancy] 5124B ×2: `artifacts/mockup-sandbox/src/components/ui/navigation-menu.tsx`, `artifacts/tessera/src/components/ui/navigation-menu.tsx`
- [real redundancy] 4887B ×2: `artifacts/mockup-sandbox/src/components/ui/command.tsx`, `artifacts/tessera/src/components/ui/command.tsx`
- [real redundancy] 4845B ×2: `artifacts/mockup-sandbox/src/components/ui/toast.tsx`, `artifacts/tessera/src/components/ui/toast.tsx`
- [real redundancy] 4776B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/src/components/tessera/code-view.tsx`, `archives/source-repositories/olive-giant-ever-glade/src/components/tessera/code-view.tsx`
- [real redundancy] 4538B ×2: `archive/from-gitbook/archive/moved/1/pnpm-workspace.yaml`, `archives/source-repositories/1/pnpm-workspace.yaml`
- [real redundancy] 4504B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/data/tools/workshop-pass.mjs`, `archives/source-repositories/olive-giant-ever-glade/data/tools/workshop-pass.mjs`
- [real redundancy] 4494B ×2: `artifacts/mockup-sandbox/src/components/ui/item.tsx`, `artifacts/tessera/src/components/ui/item.tsx`
- [real redundancy] 4419B ×2: `artifacts/mockup-sandbox/src/components/ui/alert-dialog.tsx`, `artifacts/tessera/src/components/ui/alert-dialog.tsx`
- [real redundancy] 4280B ×2: `artifacts/mockup-sandbox/src/components/ui/sheet.tsx`, `artifacts/tessera/src/components/ui/sheet.tsx`
- [real redundancy] 4175B ×2: `artifacts/mockup-sandbox/src/components/ui/form.tsx`, `artifacts/tessera/src/components/ui/form.tsx`
- [real redundancy] 3835B ×2: `artifacts/mockup-sandbox/src/components/ui/dialog.tsx`, `artifacts/tessera/src/components/ui/dialog.tsx`
- [real redundancy] 3546B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/package.json`, `archives/source-repositories/olive-giant-ever-glade/package.json`
- [real redundancy] 3356B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/data/tessera-proof.json`, `archives/source-repositories/olive-giant-ever-glade/data/tessera-proof.json`
- [real redundancy] 3007B ×2: `artifacts/mockup-sandbox/src/components/ui/drawer.tsx`, `artifacts/tessera/src/components/ui/drawer.tsx`
- [real redundancy] 2859B ×2: `artifacts/mockup-sandbox/src/components/ui/table.tsx`, `artifacts/tessera/src/components/ui/table.tsx`
- [real redundancy] 2751B ×2: `artifacts/mockup-sandbox/src/components/ui/pagination.tsx`, `artifacts/tessera/src/components/ui/pagination.tsx`
- [real redundancy] 2712B ×2: `artifacts/mockup-sandbox/src/components/ui/breadcrumb.tsx`, `artifacts/tessera/src/components/ui/breadcrumb.tsx`
- [real redundancy] 2396B ×2: `artifacts/mockup-sandbox/src/components/ui/empty.tsx`, `artifacts/tessera/src/components/ui/empty.tsx`
- [real redundancy] 2209B ×2: `artifacts/mockup-sandbox/src/components/ui/button-group.tsx`, `artifacts/tessera/src/components/ui/button-group.tsx`
- [real redundancy] 2143B ×2: `artifacts/mockup-sandbox/src/components/ui/input-otp.tsx`, `artifacts/tessera/src/components/ui/input-otp.tsx`
- [real redundancy] 2001B ×2: `artifacts/mockup-sandbox/src/components/ui/accordion.tsx`, `artifacts/tessera/src/components/ui/accordion.tsx`
- [real redundancy] 1877B ×2: `artifacts/mockup-sandbox/src/components/ui/tabs.tsx`, `artifacts/tessera/src/components/ui/tabs.tsx`
- [real redundancy] 1828B ×2: `artifacts/mockup-sandbox/src/components/ui/card.tsx`, `artifacts/tessera/src/components/ui/card.tsx`
- [real redundancy] 1753B ×2: `artifacts/mockup-sandbox/src/components/ui/toggle-group.tsx`, `artifacts/tessera/src/components/ui/toggle-group.tsx`
- [real redundancy] 1723B ×2: `artifacts/mockup-sandbox/src/components/ui/resizable.tsx`, `artifacts/tessera/src/components/ui/resizable.tsx`
- [real redundancy] 1642B ×2: `artifacts/mockup-sandbox/src/components/ui/scroll-area.tsx`, `artifacts/tessera/src/components/ui/scroll-area.tsx`
- [intentional: test fixture] 1630B ×2: `archive/from-gitbook/archive/moved/olive-giant-ever-glade/scripts/import-pass.test.mjs`, `archives/source-repositories/olive-giant-ever-glade/scripts/import-pass.test.mjs`
- [real redundancy] 1598B ×2: `artifacts/mockup-sandbox/src/components/ui/alert.tsx`, `artifacts/tessera/src/components/ui/alert.tsx`
- [real redundancy] 1486B ×2: `artifacts/mockup-sandbox/src/components/ui/toggle.tsx`, `artifacts/tessera/src/components/ui/toggle.tsx`
- [intentional: LICENSE] 1467B ×2: `.agents/skills/pdf/LICENSE.txt`, `.agents/skills/pptx/LICENSE.txt`
- [real redundancy] 1419B ×2: `artifacts/mockup-sandbox/src/components/ui/avatar.tsx`, `artifacts/tessera/src/components/ui/avatar.tsx`
- [real redundancy] 1410B ×2: `artifacts/mockup-sandbox/src/components/ui/radio-group.tsx`, `artifacts/tessera/src/components/ui/radio-group.tsx`
- [real redundancy] 1342B ×2: `artifacts/mockup-sandbox/src/components/ui/popover.tsx`, `artifacts/tessera/src/components/ui/popover.tsx`
- [real redundancy] 1237B ×2: `artifacts/mockup-sandbox/src/components/ui/hover-card.tsx`, `artifacts/tessera/src/components/ui/hover-card.tsx`
- [real redundancy] 1148B ×2: `artifacts/mockup-sandbox/src/components/ui/switch.tsx`, `artifacts/tessera/src/components/ui/switch.tsx`
- …34 more (see repo-dups-TESSERA.json)

### Gitbook
- Duplicate groups: 1913; real redundancy: 1843; intentional: 70; touching locked paths: 0
- Redundant bytes (real): 18,428,248

- [real redundancy] 174530B ×2: `archive/moved/5t/.agents/outputs/tx-t44-unique/.agents__outputs__github-push-review.md`, `history/recovered/source-documents/5t/.agents/outputs/tx-t44-unique/.agents__outputs__github-push-review.md`
- [real redundancy] 138545B ×2: `archive/moved/Zz/artifacts/z-app/data/drive/979328c534040010.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/drive/979328c534040010.txt`
- [real redundancy] 132250B ×2: `archive/moved/Zz/artifacts/z-app/imports/objects/e93ae843c05b2f936efaaa5946d506ca70a7cc15fa2f7adf79f9d4c70659b2cc`, `history/recovered/source-documents/Zz/artifacts/z-app/imports/trees/tessera-complete-archives--grok-workspace_1789591148371/.grok/skills/threejs/references/llms-full.txt`
- [real redundancy] 113091B ×2: `archive/moved/olive-giant-ever-glade/data/school/z-paths.txt`, `history/recovered/source-documents/olive-giant-ever-glade/data/school/z-paths.txt`
- [real redundancy] 98351B ×2: `archive/moved/olive-giant-ever-glade/data/school/local.txt`, `history/recovered/source-documents/olive-giant-ever-glade/data/school/local.txt`
- [real redundancy] 79161B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/4d75f682368d8042.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/4d75f682368d8042.txt`
- [real redundancy] 78547B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/b6e4c5d723cd00b7.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/b6e4c5d723cd00b7.txt`
- [real redundancy] 78240B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/778625ef9c6b0690.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/778625ef9c6b0690.txt`
- [real redundancy] 77063B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/15c8f28aa442bb9d.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/15c8f28aa442bb9d.txt`
- [real redundancy] 76563B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/ea20dc1e96ff0808.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/ea20dc1e96ff0808.txt`
- [real redundancy] 76003B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/6c576d7034be2a89.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/6c576d7034be2a89.txt`
- [real redundancy] 71879B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/9fcffcd3d9f5a112.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/9fcffcd3d9f5a112.txt`
- [real redundancy] 69569B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/043ca152b3fa7ec2.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/043ca152b3fa7ec2.txt`
- [real redundancy] 67982B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/e62df619c43cc1a7.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/e62df619c43cc1a7.txt`
- [real redundancy] 64768B ×2: `archive/moved/1/artifacts/tessera/src/components/ChatArea.tsx`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/b78d6581c8b3e9a1.txt`
- [real redundancy] 63046B ×2: `archive/moved/Zz/artifacts/z-app/imports/objects/9bbc8a5f844440450022b09bf8abddea2dbecf1c79cf360ffe4ab3af07fc6f8d`, `history/recovered/source-documents/Zz/artifacts/z-app/imports/trees/tessera-complete-archives--grok-handoff/grok-packet/07_LINK_INDEX.md`
- [real redundancy] 62905B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/942dd0718141b738.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/942dd0718141b738.txt`
- [real redundancy] 62496B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/40d63331414205bd.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/40d63331414205bd.txt`
- [real redundancy] 62034B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/9de08511eaacd9de.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/9de08511eaacd9de.txt`
- [real redundancy] 61397B ×2: `archive/moved/5t/.agents/outputs/tx-snapshot-diffs-frontend.md`, `history/recovered/source-documents/5t/.agents/outputs/tx-snapshot-diffs-frontend.md`
- [real redundancy] 61035B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/d52ec55b9efae274.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/d52ec55b9efae274.txt`
- [real redundancy] 59759B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/f42c82b448bef5b1.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/f42c82b448bef5b1.txt`
- [real redundancy] 59342B ×2: `archive/moved/Grok-ready/docs/grok-packet/06_SAFE_SOURCE_FILES/storefront-static/public/product-images/manifest.json`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/702ccbe94b644cfa.txt`
- [real redundancy] 58884B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/61922009caa3b2fa.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/61922009caa3b2fa.txt`
- [real redundancy] 57450B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/0c2a5e5fef7633a8.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/0c2a5e5fef7633a8.txt`
- [real redundancy] 56621B ×2: `archive/moved/Zz/artifacts/z-app/imports/objects/31d65b396621eff3ed50cd57ae10a1d62085ff049447451a4cdd0482c41c359f`, `history/recovered/source-documents/Zz/artifacts/z-app/imports/trees/shared-lfs-zip/3/attached_assets/Pasted--WHO-S-RUNNING-THE-PSYOP-The-Architecture-TIER-1-OWNERS_1776047368974.txt`
- [real redundancy] 55890B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/9de3504e38104048.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/9de3504e38104048.txt`
- [real redundancy] 54710B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/2ca2379575f9dc4b.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/2ca2379575f9dc4b.txt`
- [real redundancy] 54462B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/9fcca6519614f8bf.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/9fcca6519614f8bf.txt`
- [real redundancy] 53771B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/d726a1b9d281f41b.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/d726a1b9d281f41b.txt`
- [real redundancy] 53718B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/55ecbdf3d30b0559.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/55ecbdf3d30b0559.txt`
- [real redundancy] 52940B ×2: `archive/moved/olive-giant-ever-glade/data/school/retained.txt`, `history/recovered/source-documents/olive-giant-ever-glade/data/school/retained.txt`
- [real redundancy] 52362B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/d1b73a7bc4103462.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/d1b73a7bc4103462.txt`
- [real redundancy] 52018B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/ee8ffcc833162a10.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/ee8ffcc833162a10.txt`
- [real redundancy] 49275B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/609d8f66e15c4cf2.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/609d8f66e15c4cf2.txt`
- [real redundancy] 49131B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/b0f80b01c5794758.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/b0f80b01c5794758.txt`
- [real redundancy] 49014B ×2: `archive/moved/Grok-ready/artifacts/api-server/src/lib/eval-runner.ts`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/7d128dc4a686a70c.txt`
- [real redundancy] 49006B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/eeac398b249fdac3.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/eeac398b249fdac3.txt`
- [real redundancy] 48841B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/661422d39757eec6.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/661422d39757eec6.txt`
- [real redundancy] 48086B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/41ec733a4c7af016.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/41ec733a4c7af016.txt`
- [real redundancy] 47996B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/4e0d0be1510e05f9.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/4e0d0be1510e05f9.txt`
- [real redundancy] 47374B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/7a6f5b73e744dcae.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/7a6f5b73e744dcae.txt`
- [real redundancy] 47344B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/e9b306255a0a6831.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/e9b306255a0a6831.txt`
- [real redundancy] 47139B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/87c99d4b2268e66a.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/87c99d4b2268e66a.txt`
- [real redundancy] 46709B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/fe69487f97e279f7.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/fe69487f97e279f7.txt`
- [real redundancy] 46252B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/8c830b764b3b117d.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/8c830b764b3b117d.txt`
- [real redundancy] 44660B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/13196839c0987615.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/13196839c0987615.txt`
- [real redundancy] 44470B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/0f1a424b4eeb9383.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/0f1a424b4eeb9383.txt`
- [real redundancy] 43606B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/b93b6b68ab64965d.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/b93b6b68ab64965d.txt`
- [real redundancy] 43591B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/d101be412ea7623b.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/d101be412ea7623b.txt`
- [real redundancy] 43065B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/d3021de3094157dc.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/d3021de3094157dc.txt`
- [real redundancy] 43036B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/19a5ea7f5a4c3315.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/19a5ea7f5a4c3315.txt`
- [real redundancy] 42737B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/e1697fdea65d7e17.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/e1697fdea65d7e17.txt`
- [real redundancy] 41597B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/3529363ab67d44d4.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/3529363ab67d44d4.txt`
- [real redundancy] 41377B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/7aacacf5e999b891.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/7aacacf5e999b891.txt`
- [real redundancy] 41171B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/b7224f9666cbf889.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/b7224f9666cbf889.txt`
- [real redundancy] 41128B ×2: `archive/moved/Zz/artifacts/z-app/data/sandbox-runs/humanbrain.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/sandbox-runs/humanbrain.txt`
- [real redundancy] 41114B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/63ffec11d6c3a949.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/63ffec11d6c3a949.txt`
- [real redundancy] 40596B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/25e25cd858ae5994.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/25e25cd858ae5994.txt`
- [real redundancy] 40411B ×2: `archive/moved/Zz/artifacts/z-app/data/ingest/bfd017890d3efedd.txt`, `history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/bfd017890d3efedd.txt`
- …1853 more (see repo-dups-Gitbook.json)
