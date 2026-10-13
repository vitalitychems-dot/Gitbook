`origin/main` is `a7f31534f0e68cf6c8647052bac6fb921f0e6522`. Ahead/behind is commits on the branch / commits on main (`git rev-list --left-right --count origin/main...tip`). MERGED means the pre-scrub tip is an ancestor of `origin/main`. Only the five UNMERGED tips were diffed (`origin/main...<branch>`). No `natal-vault.json` path appears in those diffs. No 1T or vault files were opened.

| Branch | Pre-scrub SHA | Status | Ahead/behind | Summary | Flags | Recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| `make-it-real-bridge-3a81` | `a60f20d59e78a81ebd5ecb5fa9baf2e4864f53b2` | MERGED | 0/4 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `memory-done` | `360342f14feb6c1985fe3ce7255f8f3f2322f720` | MERGED | 0/437 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `memory-redaction-patterns-301f` | `25183afb894194cb28c17ef3898b70b81d2115cb` | MERGED | 0/567 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `mesh-net` | `ccc9fdae3a26cd554c1efc35013611361d9ccb77` | MERGED | 0/270 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `metrics-25` | `f987209a18c27b802e7e4ed1f449e7af00722e28` | MERGED | 0/264 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `metrics-lean` | `d80ee5fa83b02d53cfc97a1a7029aa6a1918ef44` | MERGED | 0/262 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `mind-chart` | `2fd74ad14ed1d3222e0cd6d121fe3ad2cd76f846` | MERGED | 0/132 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `moltbook-check` | `0ce59dfdeac403731ea49cd0dd9a0f16cdc6a47f` | MERGED | 0/268 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `name-a-card` | `caa9a30a4bbc0f5d4ea5c4ff38865af9efc7f443` | MERGED | 0/422 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `no-client-fs` | `d354bfaaa7e6f154361a78f6693ea518d36e451a` | MERGED | 0/289 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `open-one-room` | `6e9295f66e27c91b8085fd83a01b1f186a98ebc2` | MERGED | 0/274 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `open-room` | `8df4ab039b5bc8fbcad98bc456e036d416879ba0` | MERGED | 0/242 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `orders` | `2be11982454522863e47616e729c0aac80779bba` | MERGED | 0/138 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `outer-door-link` | `e91faa07152c2336223b309865d782e523957fc1` | MERGED | 0/232 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `pack` | `5d8e62b5d041ff9ec714ea39edc54b18c3231e2f` | MERGED | 0/172 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `page-3` | `fbddef154eab08304db7846c053e4fc2c2f17665` | MERGED | 0/441 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `page-4` | `ff7a8c094c3561128e78f88a01fe3ad668c17bff` | MERGED | 0/439 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `pages-15` | `57b9a8155cdeaccb768a1017500b189ddca29313` | MERGED | 0/418 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `reality-seed` | `3c59a0b87d4f8dab810fa521ac8d6a40e3d6fc4b` | MERGED | 0/230 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `recall-exact` | `a1582412e160aa0f400ce3678c81ad1a062226da` | MERGED | 0/112 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `recall-sheet` | `337dfb135c0a1e63e255382e74856f26507167a2` | MERGED | 0/152 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `recursive-proof` | `0102b6e49678c4725fc87a4541820bdc363f2087` | MERGED | 0/128 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `remove-openai-sdk-691d` | `54fbd2484056983528960252af1590473081b50b` | UNMERGED | 5/549 | Five commits drop the OpenAI SDK, add `artifacts/api-server/src/lib/tessera-llm-http.ts`, and delete large legacy UI plus archive copies (56 files, +274/−7832). `package.json` already matches main, so the SDK removal is already there. The same diff still deletes archive UI main kept. Not worth a PR. | `.env.example`; `docs/SECRETS.md`; `docs/migration-review/VALIDATION.md`; `docs/pen/glm53-flash-prep.md` (text path `Zz/1T/T44`); `docs/cl1/cl1-sim-prep.md`; `docs/image-text/ocr.jsonl`; `.agents/skills/audit-website/README.md`; `artifacts/api-server/src/lib/centrality-boundary.ts` (comment only); `archives/migration-review/legacy-ui/DashboardPage.tsx`; `archives/migration-review/legacy-ui/InventionsPage.tsx`; `archives/source-variants/T44/main/artifacts/api-server/src/routes/rick.ts` | needs-review |
| `restore-guarded-fetch-bd32` | `ca77aae3cb017b54ac9fc2c22b4df53960ddedd1` | UNMERGED | 1/485 | One commit restores guarded fetch, adds a NASA hostname allowlist, and sends Rick proposal and conversation calls through `secureExternalFetch`. `secureExternalWrapper.ts` is byte-identical to main. Not worth a PR. | `.env.example` | needs-review |
| `rick-five` | `c6d71a16305121d3b2859f27522ada11a8edbdd5` | MERGED | 0/281 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `rick-github` | `d7593639a1e7de17c2753a94d2f42495b76be3bf` | MERGED | 0/238 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `rick-home` | `e89d2957a6d837d52c09e774383d9acb2ae7dfb7` | MERGED | 0/260 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `rick-inside` | `e81d84f4cbd89240542ea0cb35ab0bb64e1fb3c0` | MERGED | 0/236 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `rick-loop` | `924dca227545952fb88330a6180d6b112760de6f` | MERGED | 0/283 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `rick-metrics` | `b66dda942263cb188d19a8c5d703d9958f787c29` | MERGED | 0/266 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `rick-pick` | `b501ecfd5638731833829d3e2a5b98eefd19d5cd` | MERGED | 0/120 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `rick-runs` | `95aaabf0614dda37f8e97383c148d85033c8f738` | MERGED | 0/258 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `rick-shift` | `5e4539c3fc57bd55f2d6c44d6a91d23c8c2a8f04` | MERGED | 0/214 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `rick-thirty` | `a2a54624beaaf8745fe8ecb91fe3196b10156994` | UNMERGED | 3/111 | Adds `preview/src/lib/tessera/evolve.ts`, `guard.ts`, and a 30-row before/after harness (`rick-thirty.ts`). `evolve.ts` and `guard.ts` match main. Main already has a longer `rick-thirty.ts`. Not worth a PR. | `preview/src/lib/tessera/rick-thirty.ts` | needs-review |
| `rick-workshop` | `d3ac0d5b8a60eb2c31c268ee67723d5c32e7b630` | MERGED | 0/252 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `room-camera` | `19d6f261a82a4fbfac514e83f0abb548be9a9d7a` | MERGED | 0/206 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `rooms` | `85d39a983e47da557965f6c20bf0180b78dc7f05` | MERGED | 0/240 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `root-next` | `9b976689e7474b96b46814238202b9a6694fa990` | MERGED | 0/144 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `root-skills` | `10749045cc9930f94fedf76dbd28bf6b6285a9b3` | MERGED | 0/146 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `runs-itself` | `a1cf4a32aad531f1267655623c293aa35dbe3a3e` | MERGED | 0/216 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `secret-engines` | `64c400cba3a5d3716a1c4a4f40ff1ff42716c1d2` | MERGED | 0/228 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `shared-house` | `126a13f02614c50cefcf7a6e419aa6e8af901e5e` | MERGED | 0/204 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `she-reads` | `9b34d9c8851f3820e1c2201c45d095961e2d6e36` | MERGED | 0/210 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `shelf` | `f81044c856cc10e6186941b010745f319c28791b` | MERGED | 0/176 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `site-002-diagnostics-gate-7ea3` | `352cb5748797c5cdd997c26ec99ac164ff5cc211` | UNMERGED | 1/290 | Gates remaining diagnostics routes with `requireAdminSession` and updates the release note. The route and session-gate test are byte-identical to main. Not worth a PR. | — | needs-review |
| `sovereign-desk` | `cf54f85aafd27e381d673871352b99fb1052f078` | MERGED | 0/285 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `sparse` | `45068f8c1cfaefafc108340a24cf9cc52d4911e4` | MERGED | 0/156 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `sparse-batch` | `886c717656cac4544ad029d7d06b54ee1805687a` | MERGED | 0/154 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `spin-house` | `36cf176a294932683c17871517d8d49f4af02cfd` | MERGED | 0/256 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `spin-try` | `2483b6078190c0cb74b82226a40a6c4513dbce71` | MERGED | 0/254 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `studio-3d-floor-3a81` | `0357acf2724db73e08e6d09c915e75e755773c1e` | MERGED | 0/8 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `studio-denylist-gate-3a81` | `66db9cf3fecda39b8600e8e1e0cbd13fc27b13cf` | MERGED | 0/2 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `synapse-weight` | `5ac35a5dfba8eb77585b06cda90421a8e0d1a052` | MERGED | 0/126 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `synapses` | `0b09ece0c766e6df795b5a091031e4e48f94d77a` | MERGED | 0/134 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `tabs-brain` | `de67cf1563afba02c98e8359a1ee088af1b2c25d` | MERGED | 0/287 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `tessera-learning-memory-301f` | `f57c40aa3863a8f688fb0e61e75bee289c296baa` | MERGED | 0/569 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `tessera-voice-chamber-22dd` | `c8c8295307c5bed122d416480a0e3583a5972932` | MERGED | 0/560 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `tests-pass` | `e94f71734959037361517108c3f852aa3e3cef99` | MERGED | 0/166 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `train-pass` | `943fbeca11789ce9a892239d75ae87f711ce4dcd` | MERGED | 0/170 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `train-wider` | `80f8bacf43084f4a5847d4c6317d1109d33049c4` | MERGED | 0/168 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `tunnel` | `8e7c80b9dc1848f5e5e27fc55b87bc81eac3e437` | MERGED | 0/246 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `twenty` | `8616953344078d4203b26dc5bc9cc2cdb28ac8a0` | MERGED | 0/116 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `ui-cut` | `c895742228ab9dad9574b5add491f59249822487` | UNMERGED | 3/111 | Cuts the preview shell from twenty rooms to nine and folds old room ids into Brain. `brain-view.tsx`, `live-tick.tsx`, and `reward-tick.ts` match main. The nine-room list is already on main aside from a GitbookAI vs GitMesh label. Not worth a PR. | `preview/src/components/tessera/app-shell.tsx`; `preview/src/components/tessera/rooms-sheet.tsx`; `preview/src/components/tessera/brain-view.tsx`; `preview/src/lib/tessera/vault-index` (referenced, not added) | needs-review |
| `use-engines` | `9057733da6d11f0b655de800b69e278a18ab679c` | MERGED | 0/224 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-001-hyb011-denylist-3a81` | `cfd5d61f5fbc35348661d76efaba885a42deb477` | MERGED | 0/101 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-002-mit-license-3a81` | `fffc5546ec60fb9be68dd536eb808a99b6a88c15` | MERGED | 0/78 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-003-vendor-snapshot-3a81` | `c8757434be031c36aad6e1a3a475a356dc63da5c` | MERGED | 0/76 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-004-rea-coverage-3a81` | `19d67ab40d8d71deb38f8d00dd5415d643e0c833` | MERGED | 0/74 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-010-task-graph-3a81` | `233866fb8135d8fd0f9f6895342b39cfe0334a47` | MERGED | 0/72 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-011-worktrees-3a81` | `86b438f1a7b2d381aa29c8fc3b47c7e1af497f50` | MERGED | 0/70 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-012-merge-gate-3a81` | `0f239b8a77bad9ceebee1e31b1b9a5a43cdc65e4` | MERGED | 0/68 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-013-ws-protocol-3a81` | `463034fced620a8ec8b498e60facc761f83c19ba` | MERGED | 0/66 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-014-studio-wall-3a81` | `bfebe4c44fd4fbeb733489ae58ab5694e371cc12` | MERGED | 0/64 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-015-studio-3d-off-3a81` | `792515d3f648acc7cac4e416ec6896222c4d81ba` | MERGED | 0/62 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-016-lead-planner-3a81` | `ec7622d66a2f10f39e66ed30f87430d32b192877` | MERGED | 0/60 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-017-worker-stream-3a81` | `be716c32a15531eb52a316e99fe85858d5b346c0` | MERGED | 0/58 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-020-file-mesh-3a81` | `d4a65012ff870499f61d0f8c962a46807b69a07c` | MERGED | 0/56 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-021-offline-queue-3a81` | `1ce1214df914fcb8b74f26b33d8f19be788f145f` | MERGED | 0/54 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-022-sw-shell-3a81` | `5b07f461f6f4646fba861e89035b8951ac61c868` | MERGED | 0/52 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-023-mesh-badge-3a81` | `a9b4054bbf750ed3b56d05523ce1def2e9fc47dc` | MERGED | 0/50 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-024-mesh-node-3a81` | `76f66a5d8a3c2278e3dec5154d2f1f68e3a2bc66` | MERGED | 0/48 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-025-secure-mesh-3a81` | `9bdde17de5b3e210ffd8e977b7b3d0e5ff4f38c8` | MERGED | 0/46 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-026-sneakernet-3a81` | `6ba8e163631e2753cc8def5afd1c115a1d958792` | MERGED | 0/44 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-027-lan-p2p-3a81` | `35660e3dac1addbe14b93cf4e9ad3853ba99915b` | MERGED | 0/42 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-028-kiwix-off-3a81` | `e36820f98d23e5033e6b6a68c67b9feccfacfce7` | MERGED | 0/40 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-029-offline-internet-3a81` | `aa3a6d4695c3b606be71fbdb5bcbc8ed1eb7ec50` | MERGED | 0/38 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-030-lora-note-3a81` | `7fc143d8f69b435762ead873596dfb5a709b0991` | MERGED | 0/36 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-040-kg-store-3a81` | `64f6b3f47b172887e02e3de04bccbe68396ad6f7` | MERGED | 0/34 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-041-mcp-memory-3a81` | `af5d53bf33771d0792a0fd0ab07b1bdf1a0353c9` | MERGED | 0/32 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-042-library-panel-3a81` | `901c92783c65d34cb776a771f4b1bc242b805efb` | MERGED | 0/30 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-043-own-repo-meta-3a81` | `02e080d530b72b11b12bf6429a2c6cb80961c9d9` | MERGED | 0/28 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-050-desk-sandbox-3a81` | `c1881bc289b3e784b6f85430c20157326e24dba7` | MERGED | 0/26 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-051-token-meter-3a81` | `596e772a3571a8088f3d6be4d18c3df071818c22` | MERGED | 0/24 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-052-ab-graph-3a81` | `9addf13ce5d18f4143d6aaf36242e2d54c086cef` | MERGED | 0/22 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-053-summary-cache-3a81` | `be56d2b8df51a5adba75ce761401ce8f8d7649b6` | MERGED | 0/20 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-054-small-model-3a81` | `7bc8c28789564eb73c87ddea802a1b5625d6dd67` | MERGED | 0/18 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-055-proposal-queue-3a81` | `efcd233a982bfaf11f9496673b5c72c65cc24f73` | MERGED | 0/16 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-060-hn-allowlist-3a81` | `aaa5167afee213e9b97bb745e20c706d959891f8` | MERGED | 0/14 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-061-chamber-board-3a81` | `875c74be4d1e10b0bbaedc5f5534c6b9bec30090` | MERGED | 0/12 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `v2-062-gitmesh-label-3a81` | `7c3f530da210fd44bca18d44868b4ab11b1278fb` | MERGED | 0/10 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `whiten` | `721ac0ef52a9073dd31426b06e8c4338c8b09468` | MERGED | 0/297 | Tip is an ancestor of `origin/main`. | — | archive-merged |

**Counts:** 101 branches (`origin/cursor/*`, name after `cursor/` starts with m–z). 96 MERGED, 5 UNMERGED. Recommendations: 96 archive-merged, 0 worth-PR, 5 needs-review.