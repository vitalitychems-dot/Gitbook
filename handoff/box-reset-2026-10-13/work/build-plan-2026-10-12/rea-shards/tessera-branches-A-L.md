`git fetch --all` updated `origin/main` to `a7f31534f0e68cf6c8647052bac6fb921f0e6522`. Scope is every `origin/cursor/*` branch whose name after `cursor/` starts with `0-9` or `a-l`: **73** branches. None start with a digit. `m-z` names were left out. Ahead/behind is `git rev-list --left-right --count origin/main...<branch>` (ahead = commits on the branch not in main). Unmerged rows were reviewed with `git diff origin/main...<branch>` only. No `1T/` or vault file was opened.

| Branch | Pre-scrub SHA | Status | Ahead/behind | Summary | Flags | Recommendation |
|---|---|---|---|---|---|---|
| `origin/cursor/agent-cycle` | `4316a038865b7a3d92a1eeb7761812315a41fd1a` | MERGED | 0/114 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/ask-all` | `050289ed0cc57e5a3fd90949bd49a7901b6052a4` | MERGED | 0/220 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/batch-2` | `27f1eebae11ad6d3286ce40b5bdf0e267f2c25fe` | MERGED | 0/329 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/batch-3` | `9ec8c44d35d8552ce9a2d3a1d281fcc422eb97cb` | MERGED | 0/301 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/batch-3-keep` | `c278d17f7ab06de4ab4b8a1a232d642ce2b25065` | MERGED | 0/299 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/batch-50` | `5e4cd6f560388a5cb14a81a8128b2bb544c00b91` | MERGED | 0/373 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/batch-next` | `11f966c109e066989e2c42a440e5cf246f72cf0a` | MERGED | 0/160 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/batch-read` | `88736cbbbd0ffc7d42bd14cd7691e4b09bf4aba4` | MERGED | 0/162 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/brain-canvas` | `9119e35d74bb9edfcad59294ff70c2b195b99f11` | MERGED | 0/291 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/brain-mesh` | `ad2c272eaef5f87b293d2a658df9269ee1c69ae2` | MERGED | 0/327 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/brain-train` | `9b677a32d3339e390ab73940a43ace1eafc03634` | UNMERGED | 1/111 | One commit adds `preview/src/lib/tessera/brain-train.ts` and its test: four teach waves, exact recall score 32, overlap miss left visible. Both files are byte-identical on `origin/main`. | none | needs-review |
| `origin/cursor/brain-volume` | `8cf4516c243284a014d7a9cf671cc5fa9b25c496` | MERGED | 0/295 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/build-herself` | `b84bd287f4f09ae72827a94cadd5b467d4be8c95` | MERGED | 0/188 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/carry-on` | `2d66ca7e078c9f93e9fe7796d9d14f3d2c1d7f81` | MERGED | 0/202 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/catalog-batch-3-aa90` | `f6c45117b3b7467f01ba75494f2782204a84757c` | MERGED | 0/325 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/catalog-batch-4-aa90` | `8b0cb0bf9cd0bf9cd9449c9a2f5b8fad7cbadced` | MERGED | 0/303 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/catalog-train` | `219ff1f5b725dfc8aaedd8a2a17ff396502887a0` | MERGED | 0/424 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/chamber-v5` | `16d0af7eaefee1854a0e0f0af05e8a896b97e718` | MERGED | 0/443 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/chart-ui` | `65883d88d5d81ba0a7f02b8019f6321efe23051f` | UNMERGED | 3/111 | Three commits restore `preview/src/components/tessera/mind-chart.tsx`: stat row, selected-fact card, string-built SVG transform. Main already has that layout. The tip differs by a hyphen and the word "to". | none | needs-review |
| `origin/cursor/chat-desk-training-22dd` | `7c922277c9c7fe7e4f81b59948c8ff64ea0a2a43` | MERGED | 0/552 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/checkout-read` | `38952f8fe27fc0974257471e9a5aa9d845128f80` | MERGED | 0/164 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/city-keeps` | `a2a026eced31cb4cfe8d5cacc1603662067d3996` | MERGED | 0/208 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/civic-agent-world-3a81` | `09ce52c820f6c3aa5f041a680c9151254c22734b` | MERGED | 0/6 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/civic-city` | `ad551fdfb3630c020d3df67d2179a62d826dae3d` | MERGED | 0/212 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/clear-composer` | `b0c4110ae4447a3f8adacca394ad3e8c9be67bc7` | MERGED | 0/279 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/code-hygiene-5146` | `a01b50e9ce997b9a5f4dcd600f14bf0338ee9805` | MERGED | 0/577 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/composer-load` | `78a2bfa0e82e641049766abe4712100ad92a17cd` | MERGED | 0/196 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/copilot-seat` | `3c3b28bc232e5bbf08d18e1da0f0dfc81a86eb96` | MERGED | 0/174 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/curiosity` | `7a6175f45943fc5dc4ef473fec3dc4ad2a100234` | MERGED | 0/124 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/curiosity-fix` | `a025496c1803567ceb63ab2fd177b4627ced7d1f` | MERGED | 0/122 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/delete-openai-class-a-4339` | `558ee4851ac1754b77658dd7cf6a3be1f38c29ba` | UNMERGED | 5/549 | Five commits drop the `openai` package, add `artifacts/api-server/src/lib/tessera-llm-http.ts` plus a test, delete legacy migration-review UI and some source-variant archives, and rename OpenAI env placeholders to `TESSERA_LLM_*`. Main already has no `openai` dependency and a later HTTP client. `openai.yaml` and several deleted archive pages are still on main. Too far behind to merge as-is. | `.env.example`; `docs/SECRETS.md`; wallet text in `archives/migration-review/legacy-ui/DashboardPage.tsx` (`fin-wallet`, `SOL_WALLET`); vault text in that file and `archives/migration-review/legacy-ui/InventionsPage.tsx` (`sovereign-data-vault`); payment/Stripe wording in `.agents/skills/audit-website/README.md` and `docs/migration-review/VALIDATION.md`. No `1T/vault/natal-vault.json`. | needs-review |
| `origin/cursor/desk-drill-preview-1c94` | `1c528a67cedb3d0769672b828db14a18740e5688` | UNMERGED | 1/326 | One commit adds `preview/TRUE-TODAY.md`, a sealed/open status note. The file matches `origin/main`. | none | needs-review |
| `origin/cursor/desk-live` | `d037468162fce251d3b82169e8e8a74e86363ea1` | MERGED | 0/182 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/desk-preview-search-9fab` | `e98087154af5417882d89a563fa3ab0abdf058e2` | UNMERGED | 6/469 | Six commits keep the desk pen local, attach sources to public questions, and fix rooms, row, and five runnable skills. New files `ask-web.ts`, `places.ts`, and `skills.ts` are absent on main; the same rules already live in `preview/src/lib/tessera/public-question.ts`. | `preview/src/lib/tessera/vault-index` (existing import in the `chat.ts` hunk; not read). No `1T/vault/natal-vault.json`. | needs-review |
| `origin/cursor/desk-questions-aa90` | `ea4840850af3374a5e37c3956fffe3b6403f2dd8` | MERGED | 0/411 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/desk-runs` | `98945236c0300a26cd58b49a9c81813c16274b79` | MERGED | 0/186 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/docs-readme-config-5146` | `820d0be57d88fb463bcef74e1ca06e04c4ae6dd7` | MERGED | 0/577 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/drop-two` | `ced288275d8b215a9dd61739896fbc4bf9a58130` | MERGED | 0/234 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/eight-steps` | `ca467e5774755ed6cbc8b2bc660f8bbd0adfc7a8` | MERGED | 0/414 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/engine-session-gate-aa90` | `b1510052413cfbcdf51df4ca53154075af5d577d` | MERGED | 0/321 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/engines-deeper` | `7a6d4017151d21c9fda8573cc3fd55bd47a97e5b` | MERGED | 0/226 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/entry-door` | `56b2a6a246f5165b3097137a0581819b686c2451` | MERGED | 0/180 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/eval-harness-tests-5146` | `39db6a6ec1c74411b1d2cae5e48791aace6abb0a` | MERGED | 0/577 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/evolve` | `88cee3d65ce3c89d9374d2bc4914fd58c69e56ca` | UNMERGED | 1/111 | One commit adds `preview/src/lib/tessera/evolve.ts` and its test: a new line only when two facts produce it. Both files match `origin/main`. | none | needs-review |
| `origin/cursor/exam-waves` | `fb5b2058e904b42a88b9be07e1a5285bd669ed6e` | MERGED | 0/118 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/file-mesh` | `644c6c4cccbc61a0c9c920343f1736620c39242f` | MERGED | 0/178 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/file-recall` | `b067cadde1a7d9b7f48d9398bf9bd924a0cac10a` | MERGED | 0/148 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/finish-engines` | `fac080fa35117c324054a687a0ba7e4e2e884642` | MERGED | 0/222 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/five-pages` | `7f6c2f5b9978773f8a881031e0fba2afdbf73455` | MERGED | 0/420 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/git-pass` | `b33b6a99310781d54fdcf5237b758713c455e609` | MERGED | 0/244 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/gitai-marketplace-1742` | `a7f31534f0e68cf6c8647052bac6fb921f0e6522` | MERGED | 0/0 | Tip SHA is `origin/main`. | — | archive-merged |
| `origin/cursor/gitbook-ai` | `0c636a3ad85033a83dbbcb4b5dfb70437874f5d3` | MERGED | 0/272 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/gitbook-live` | `68829fed3e3a704f122c736863cd1c6efdb75aaa` | MERGED | 0/200 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/gitbook-mcp-connector-301f` | `e898111ae9fe730ad214ec63f9173d338a9df53e` | MERGED | 0/564 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/gitbook-place-aa90` | `f5caec348cd1cab1d60c3f7f80b3b681640d0678` | UNMERGED | 1/492 | One commit adds a Gitbook place (`gitbook-view.tsx`, shell entry, `ViewId`). Main already has Gitbook and Gitbook AI places in a newer shell. | none | needs-review |
| `origin/cursor/guard` | `a086d564430c03421dd9b6f1da0d4046e4b711d8` | UNMERGED | 1/111 | One commit adds `preview/src/lib/tessera/guard.ts` and its test: refuse a missing line and a wrong figure. Both files match `origin/main`. | none | needs-review |
| `origin/cursor/her-voice` | `efdc8ee4a457e5df191757b805ba5736e2fae546` | MERGED | 0/194 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/her-voice-grows` | `ccd2934b947f232b8dceb3bb867c4ca7e786e3fb` | MERGED | 0/190 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/her-vote` | `d937fd3eacd753019fec79e0d1684f4740a5fb77` | MERGED | 0/250 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/her-words` | `ce9cf0df5a485ea8fa517543bb48646835e8cdef` | MERGED | 0/192 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/hyb-005-audit-ignore-943c` | `76716c22d79085e1eb72c1e33ea9471b1c43103d` | MERGED | 0/580 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/imported` | `be1d8c03d90eae11f8738a9608ffcf6df23c2b5a` | MERGED | 0/158 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/include-files` | `7e80b76b894258ee59c82154cea58a71c23a918e` | MERGED | 0/218 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/interactive` | `c17fa87f39434edea7b46618c77100c204be23cc` | MERGED | 0/130 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/keep-dropped-cards-aa90` | `9c5e3ef720bfc2f5c73dab306c46838e5ece84d9` | MERGED | 0/297 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/kept-lessons` | `9718ddeb48be3afa4f906adee563594b950172a9` | MERGED | 0/198 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/kingdom` | `dd52478e8c5cb7ba7e2067f7b4924f986545caf2` | MERGED | 0/184 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/lab-audit` | `03d62c6add320519037147e354f1502b19aae209` | UNMERGED | 1/111 | One commit adds `preview/src/lib/tessera/lab-audit.ts` and its test: local category rows, other systems unscored. Both files match `origin/main`. | none | needs-review |
| `origin/cursor/ledger` | `995d7fe83d3a4bfc9a19f44b00c68ad4061d5ca4` | MERGED | 0/150 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/live-map` | `c8d6e2ad67aa356ca1a19fd01867e467acf6fca3` | MERGED | 0/136 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/local-learn` | `2bd8d672bc03c03516782e1224fe2e39b78ab622` | MERGED | 0/416 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/loop-20` | `eac78a2ad62beec28639582608e17b0fd3b4bc22` | MERGED | 0/142 | Tip is an ancestor of `origin/main`. | — | archive-merged |
| `origin/cursor/loop-times` | `caaf84c99a5edcf391318002a11eca62676e7010` | MERGED | 0/140 | Tip is an ancestor of `origin/main`. | — | archive-merged |

**Counts:** 73 in scope, 64 MERGED, 9 UNMERGED. Recommendations: 64 archive-merged, 0 worth-PR, 9 needs-review.

The nine unmerged tips are not safe to open as PRs from these SHAs. Five of them (`brain-train`, `evolve`, `guard`, `lab-audit`, `desk-drill-preview-1c94`) already match the same paths on `origin/main`. `chart-ui` and `gitbook-place-aa90` are older cuts of UI main has since replaced. `desk-preview-search-9fab` overlaps `public-question.ts` and is 469 behind. `delete-openai-class-a-4339` still deletes archive pages that remain on main, but it also rewrites `.env.example` and `docs/SECRETS.md` against a newer template and is 549 behind. No unmerged diff adds `1T/vault/natal-vault.json`.