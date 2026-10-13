# Repo names from logs inside TESSERA & Gitbook

**As-of:** 2026-10-12 ~3:53 PM CT (Father yes). Read-only via `cursor-github`. No pushes. Paths with `1T` or `vault` in the name were not opened. Wallet/secret-looking files skipped by name.

## Summary

- **Unique repo-like names (clean):** **271**
- **Noise / not-a-repo rows kept aside:** 11
- **Primary source:** `Gitbook:mesh/GITHUB-REPOS.txt` (**272** lines) and `Gitbook:mesh/CATALOG-PASS.md` (272 catalog rows; 224 present / 48 missing).
- **Also used:** `mesh/mentioned-repos.txt` (182), `merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md`, `archive/moved/olive-giant-ever-glade/data/workshop/REPOS.md` + `CATALOG.md`, `history/source-index/z-repository-index.md`, TESSERA `CONSOLIDATION_TWO_REPOS.md`.
- **Account today:** only `TESSERA`, `Gitbook`, `GitbookAI`, `vitality` are listed under `vitalitychems-dot`. Older family repos live as nested archives (see `NESTED-REPO-MAP.md`).
- **1T:** existence recorded in routing/catalog only; **not inspected** (HYB-011 / vault rule).

### Catalog home buckets (from CATALOG-PASS)

| Home | Meaning | Count in this list |
|---|---|---:|
| `card` | Public research/reference cards — pointer, not cloned | 193 |
| `gap` | Named in logs but unresolved / deleted / not found on 2026-10-08 | 23 |
| `held` | Trading/chain — excluded from Tessera mind by prior rule | 17 |
| `gitbook` | Legacy family — archived into Gitbook (and often TESSERA archives) | 16 |
| `legacy-or-live` | Named in routing as owned/legacy (may already be deleted) | 8 |
| `tool` | Tool repos — README only; do not install without a separate yes | 8 |
| `live` | Active destinations (TESSERA / Gitbook) | 2 |
| `vitality` | Store / product — stay in vitalitychems-dot/vitality | 2 |
| `?` | Listed without a catalog home | 2 |

## Unique names

| # | Name | Catalog home | State | Source path(s) |
|---:|---|---|---|---|
| 1 | `vitalitychems-dot/Gitbook` | live | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 2 | `vitalitychems-dot/TESSERA` | live | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 3 | `collink1007/amber-flame-tiger-sand` | gitbook | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 4 | `collink1007/XXX` | gitbook | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 5 | `collink1007/z` | gitbook | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 6 | `vitalitychems-dot/1` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 7 | `vitalitychems-dot/1T` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 8 | `vitalitychems-dot/5t` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 9 | `vitalitychems-dot/Everything` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 10 | `vitalitychems-dot/GitbookAI` | legacy-or-live | account-history | Gitbook:merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md |
| 11 | `vitalitychems-dot/Grok-ready` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 12 | `vitalitychems-dot/olive-giant-ever-glade` | legacy-or-live | account-history | Gitbook:merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md |
| 13 | `vitalitychems-dot/Run-Z-app` | legacy-or-live | account-history | Gitbook:merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md |
| 14 | `vitalitychems-dot/Run-Z-app2` | legacy-or-live | account-history | Gitbook:merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md |
| 15 | `vitalitychems-dot/T44` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 16 | `vitalitychems-dot/TESS` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 17 | `vitalitychems-dot/tessera-complete-archives` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 18 | `vitalitychems-dot/tessera-gitbook` | legacy-or-live | account-history | Gitbook:merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md |
| 19 | `vitalitychems-dot/tessera-grok-handoff` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 20 | `vitalitychems-dot/tessera-grok-handoff-complete` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 21 | `vitalitychems-dot/Tessera-main` | legacy-or-live | account-history | Gitbook:merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md |
| 22 | `vitalitychems-dot/tessera-replit` | legacy-or-live | account-history | Gitbook:merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md |
| 23 | `vitalitychems-dot/tessera-unified` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 24 | `vitalitychems-dot/TX` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 25 | `vitalitychems-dot/vitality` | legacy-or-live | account-history | Gitbook:merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md |
| 26 | `vitalitychems-dot/Zz` | gitbook | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 27 | `continue-dev/continue` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 28 | `sovereign-archive/T5` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 29 | `sovereign-origin/tessera-sovereign-complete` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 30 | `sovereign-origin/tessera-sovereign-ultimate` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 31 | `sovereign-origin/tesseract-quantum-agi` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 32 | `sovereign-origin/tesseract-v4-ollama` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 33 | `sovereign-origin/TessV1` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 34 | `tesseract-swarm/node-runtime` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 35 | `TheTesseractAI/consolidated-project-all-in-one` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 36 | `TheTesseractAI/Tesseract-Sovereign-Moon-v2-Consolidated` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 37 | `TheTesseractAI/Tesseract-Sovereign-Moon-v3.0` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 38 | `TheTesseractAI/Tesseract-Unified-Ecosystem` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 39 | `TheTesseractAI/Tesseract2.0` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 40 | `TheTesseractAI/Tesseraxt-Sovereign-Brain` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 41 | `twopirllc/pandas-ta` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 42 | `vitalitychems-dot/tessera-coordination` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 43 | `vitalitychems-dot/z` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 44 | `Yatrogenesis/CORTEXIA-Framework` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 45 | `Yatrogenesis/Drugs-Simulato-R` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 46 | `Yatrogenesis/iatrogene-sys` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 47 | `Yatrogenesis/lirs-lab` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 48 | `Yatrogenesis/Materials-Simulato-R` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 49 | `Yatrogenesis/Simulato-R_v2.0` | gap | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 50 | `colbymchenry/codegraph` | tool | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md; Gitbook:archive/moved/olive-giant-ever-glade/data/workshop/REPOS.md |
| 51 | `heygen-com/hyperframes` | tool | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md; Gitbook:archive/moved/olive-giant-ever-glade/data/workshop/REPOS.md |
| 52 | `JuliusBrussee/caveman` | tool | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md; Gitbook:archive/moved/olive-giant-ever-glade/data/workshop/REPOS.md |
| 53 | `mksglu/context-mode` | tool | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md; Gitbook:archive/moved/olive-giant-ever-glade/data/workshop/REPOS.md |
| 54 | `mvschwarz/openrig` | tool | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md; Gitbook:archive/moved/olive-giant-ever-glade/data/workshop/REPOS.md |
| 55 | `NVIDIA/OpenShell` | tool | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md; Gitbook:archive/moved/olive-giant-ever-glade/data/workshop/REPOS.md |
| 56 | `obra/superpowers` | tool | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md; Gitbook:archive/moved/olive-giant-ever-glade/data/workshop/REPOS.md |
| 57 | `Panniantong/Agent-Reach` | tool | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md; Gitbook:archive/moved/olive-giant-ever-glade/data/workshop/REPOS.md |
| 58 | `0x0funky/agent-sprite-forge` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 59 | `269652/artificial-consciousness-ai` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 60 | `269652/artificial-consciousness-blueprint` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 61 | `activepieces/activepieces` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 62 | `adamgallas/FireFly-v1` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 63 | `adamgallas/FireFly-v2` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 64 | `adamgallas/firefly_v1_cifar_test` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 65 | `adamgallas/SpinalDLA` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 66 | `alexander-turner/attainable-utility-preservation` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 67 | `androoAGI/starnet` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 68 | `appwrite/appwrite` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 69 | `AudiusProject/audius-protocol` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 70 | `AUTOMATIC1111/stable-diffusion-webui` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 71 | `BabylonJS/Documentation` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 72 | `BerriAI/litellm` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 73 | `bharanidharanrangaraj/interfacing_rtc_with_raspberrypi_pico` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 74 | `BindsNET/bindsnet` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 75 | `Brain-Cog-Lab/Brain-Cog` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 76 | `Brain-Cog-Lab/CACE-Net` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 77 | `Brain-Cog-Lab/casc` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 78 | `Brain-Cog-Lab/ETC` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 79 | `Brain-Cog-Lab/msg` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 80 | `Brain-Cog-Lab/PSU` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 81 | `Brain-Cog-Lab/sgad` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 82 | `Brain-Cog-Lab/TKS` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 83 | `Brain-Cog-Lab/Transfer-for-DVS` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 84 | `BrainCog-X/Brain-Cog` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 85 | `braincog-X/Brain-Cog` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 86 | `BrainCog-X/tonic_braincog` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 87 | `brian-team/brian2` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 88 | `browser-use/browser-use` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 89 | `bryc/code` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 90 | `Calamari/BehaviorTree.js` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 91 | `CanastaWiki/Canasta-CLI` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 92 | `ClickHouse/ClickHouse` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 93 | `cognitivecomputations/agi-memory` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 94 | `commonsense/conceptnet5` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 95 | `conan-io/cmake-conan` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 96 | `coral-xyz/anchor` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 97 | `Cortical-Labs/cl-sdk` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 98 | `deepmind/deepmind-research` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 99 | `deepseek-ai/DeepSeek-V3` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 100 | `DeepVoltaire/AutoAugment` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 101 | `dexaai/dexter` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 102 | `dimforge/rapier.js` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 103 | `donmccurdy/three-pathfinding` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 104 | `EfekanSalman/NeuroConscious` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 105 | `enricoros/big-AGI` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 106 | `ericjang/gumbel-softmax` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 107 | `explosion/spaCy` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 108 | `facebookresearch/tribev2` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 109 | `fangwei123456/spikingjelly` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 110 | `fastai/fastai` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 111 | `FloyedShen/tonic` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 112 | `future-agi/future-agi` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 113 | `FutureAIGuru/BrainSimII` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 114 | `gadicc/node-yahoo-finance2` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 115 | `geekan/MetaGPT` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 116 | `ggerganov/llama.cpp` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 117 | `Gil-ADDA/Piezoelectric-Energy-Generation-HarvestWalk` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 118 | `goldfire/howler.js` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 119 | `google/mediapipe` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 120 | `HandingWang/RF-CMOCO` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 121 | `hmans/miniplex` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 122 | `huggingface/text-generation-inference` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 123 | `huggingface/transformers` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 124 | `hyperspaceai/agi` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 125 | `ikostrikov/pytorch-ddpg-naf` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 126 | `ildoonet/pytorch-gradual-warmup-lr` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 127 | `infiniflow/ragflow` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 128 | `isaac-mason/recast-navigation-js` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 129 | `jacobgil/pytorch-grad-cam` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 130 | `jakearchibald/idb` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 131 | `jbhinky/Theophilus-UDC` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 132 | `jeshraghian/snntorch` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 133 | `jhlywa/chess.js` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 134 | `joaomdmoura/crewAI` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 135 | `jupyterhub/outreachy` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 136 | `jwagner/simplex-noise.js` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 137 | `kortix-ai/suna` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 138 | `ku2482/fqf-iqn-qrdqn.pytorch` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 139 | `kyegomez/swarms` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 140 | `langchain-ai/langchain` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 141 | `langchain-ai/langgraph` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 142 | `langflow-ai/langflow` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 143 | `langgenius/dify` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 144 | `lichess-org/chessground` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 145 | `localForage/localForage` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 146 | `lyh983012/ES-imagenet-master` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 147 | `maximecb/gym-minigrid` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 148 | `mem0ai/mem0` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 149 | `microsoft/autogen` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 150 | `microsoft/semantic-kernel` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 151 | `Mintplex-Labs/anything-llm` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 152 | `mit-han-lab/once-for-all` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 153 | `monero-project/monero` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 154 | `msu-coinlab/pymoo` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 155 | `mxgmn/WaveFunctionCollapse` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 156 | `n8n-io/n8n` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 157 | `NateTheGreatt/bitECS` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 158 | `numpy/numpy` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 159 | `ollama/ollama` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 160 | `open-jarvis/OpenJarvis` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 161 | `open-webui/open-webui` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 162 | `openai/baselines` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 163 | `openai/gym` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 164 | `openai/gym-http-api` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 165 | `OpenCausaLab/Awesome-LLM-Consciousness` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 166 | `opencv/opencv` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 167 | `OpenHands/OpenHands` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 168 | `oxwhirl/smac` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 169 | `pandas-dev/pandas` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 170 | `phaserjs/phaser` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 171 | `piqnt/planck.js` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 172 | `PIX2NVS/NVS2Graph` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 173 | `pkuxmq/OTTT-SNN` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 174 | `pmndrs/cannon-es` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 175 | `pmndrs/drei` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 176 | `pmndrs/react-three-rapier` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 177 | `public-apis/public-apis` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 178 | `pybind/pybind11` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 179 | `python-lsp/python-lsp-server` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 180 | `pytorch/examples` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 181 | `pytorch/pytorch` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 182 | `pytorch/vision` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 183 | `qiao/PathFinding.js` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 184 | `quark0/darts` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 185 | `QuixiAI/Hexis` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 186 | `ranaroussi/yfinance` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 187 | `recastnavigation/recastnavigation` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 188 | `replit/replit-cursor-plugin` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md; Gitbook:archive/moved/olive-giant-ever-glade/data/workshop/REPOS.md |
| 189 | `rgeirhos/texture-vs-shape` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 190 | `rohansx/agidb` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 191 | `run-llama/llama_index` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 192 | `rust-lang/crates.io-index` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 193 | `rust-lang/rust-analyzer` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 194 | `Sairamg18814/shvayambhu` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 195 | `SanderMertens/ecs-faq` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 196 | `scrapy/scrapy` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 197 | `screenpipe/screenpipe` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 198 | `seba-1511/dist_tuto.pth` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 199 | `siddhant-rajhans/cortexlab` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 200 | `Significant-Gravitas/AutoGPT` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 201 | `singnet/das` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 202 | `singnet/das-toolbox` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 203 | `solana-labs/solana-program-library` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 204 | `songrotek/DDPG` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 205 | `spacejack/carphysics2d` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 206 | `starry-sky6688/MADDPG` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 207 | `Steake/GodelOS` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 208 | `StockSharp/StockSharp` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 209 | `stripe/stripe-node` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 210 | `Superalgos/Superalgos` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 211 | `SushiSwap/sushiswap` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 212 | `SWE-agent/SWE-agent` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 213 | `SYNTAEXIST-AI/TPIS-AGI-Architecture` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 214 | `TA-Lib/ta-lib-python` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 215 | `TabbyML/tabby` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 216 | `tensorflow/tensorflow` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 217 | `tensorflow/tpu` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 218 | `theelderemo/Project-Aura` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 219 | `therealdreg/pico-freq-meter-tcxo-ref` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 220 | `TheTesseractAI/18` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 221 | `three-types/three-ts-types` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 222 | `thu-ml/tianshou` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 223 | `tlcdv/the_consciousness_ai` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 224 | `tomgoldstein/loss-landscape` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 225 | `trailhq/Graft` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 226 | `TransformerOptimus/SuperAGI` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 227 | `trueagi-io/hyperon-experimental` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 228 | `trueagi-io/jetta` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 229 | `trueagi-io/metta-examples` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 230 | `trueagi-io/protobuf-metta` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 231 | `tweenjs/tween.js` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 232 | `Uniswap/v3-core` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 233 | `venturaEffect/the_consciousness_ai` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 234 | `vercel/ai` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 235 | `vitejs/vite` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 236 | `vllm-project/vllm` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 237 | `VRSEN/agency-swarm` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 238 | `wayou/t-rex-runner` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 239 | `WingedGuardian/GENesis-AGI` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 240 | `xai-org/grok-1` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 241 | `xmrig/xmrig` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 242 | `YangyulinAi/Neurotech-Controls-for-AGI-Motivational-Framework` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 243 | `Yatrogenesis/HumanBrain` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 244 | `yatrogenesis/HumanBrain` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 245 | `yearn/yearn-vaults-v3` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 246 | `yn-sun/e2epp` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 247 | `yoannmoinet/nipplejs` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 248 | `youngbryan97/aura` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 249 | `Zae-Project/brain-emulation` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 250 | `zai-org/GLM-5` | card | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 251 | `1inch/1inch-v2-contracts` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 252 | `aave/aave-v3-core` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 253 | `alpacahq/alpaca-trade-api-js` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 254 | `balancer/balancer-v2-monorepo` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 255 | `binance/binance-connector-node` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 256 | `ccxt/ccxt` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 257 | `coinbase/coinbase-pro-node` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 258 | `compound-finance/compound-protocol` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 259 | `CryptoSignal/Crypto-Signal` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 260 | `curvefi/curve-contract` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 261 | `Drakkar-Software/OctoBot` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 262 | `filecoin-project/lotus` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 263 | `flashbots/mev-boost` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 264 | `freqtrade/freqtrade` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 265 | `hummingbot/hummingbot` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 266 | `jesse-ai/jesse` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 267 | `mementum/backtrader` | held | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/CATALOG-PASS.md |
| 268 | `collink1007/fleet-moss-monarch-rapid` | vitality | present | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 269 | `collink1007/Vitalitychems` | vitality | missing | Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md |
| 270 | `lqnankai/Music-Dataset.` | — | — | Gitbook:mesh/mentioned-repos.txt |
| 271 | `vitalitychems-dot/Zz.` | — | — | Gitbook:mesh/mentioned-repos.txt |

## Appendix — not-a-repo / noise (from same logs)

These appeared in the 272-name lists but are topics, sponsors, placeholders, or invalid paths — not repositories to import.

- `en/get-started` — sources: Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md
- `repos/vitalitychems-dot` — sources: Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md
- `sponsors/ai` — sources: Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md
- `topics/agi` — sources: Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md
- `topics/cognitive-architecture` — sources: Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md
- `topics/consciousness` — sources: Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md
- `topics/emergent-systems` — sources: Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md
- `topics/global-workspace-theory` — sources: Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md
- `user-attachments/assets` — sources: Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md
- `xxx/Brain-Cog` — sources: Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md
- `yourusername/godelOS` — sources: Gitbook:mesh/GITHUB-REPOS.txt; Gitbook:mesh/mentioned-repos.txt; Gitbook:mesh/CATALOG-PASS.md

## Protected (name only)

| Name | Note | Source |
|---|---|---|
| `vitalitychems-dot/1T` | Protected vault. Existence only. Contents not opened, indexed, or copied. | `Gitbook:merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md`, `CATALOG-PASS.md` (home=gitbook) |

## Method notes

- Prefer ordinary source analysis (tree + file reads + tests) over REA for trees that already have source.
- REA (`morluto/rea`): optional later, only on Father-owned built bundles missing source. Documented in `TOOLS-REA.md`.
- api-anything: skip (see `TOOLS-API-ANYTHING.md`). Does not remove the need for real APIs.
- Claude-Red / attack packs: **not used**.

