# Repo-lab report — Tessera mesh improvement from GitHub sources

**When:** 2026-10-05 ~5:55 PM CT  
**Identity:** Tessera Admin coordinator (Grok Bot executor) for Father (Collin Keane)  
**Bases:** TESSERA `main@5c1137fa`; Gitbook `main@bc6b3287`  
**Baseline ref:** `/workspace/full-picture/BASELINE.md` (CI 99 pass / 1 skip; gitbook_rag_score BLOCKED; industry_bench_score BLOCKED)  
**Labels:** TESTED / REPORTED / GOAL / UNKNOWN / BLOCKED as marked.  
**Bounds honored:** read-only GitHub for vitalitychems-dot/* + Origin; no credentials/spend; no secrets / TESSERA_ENABLE_* / wallets / payments / blockchain / Monero / [REDACTED-PATH] no wholesale Zz or olive-giant; no killing Ollama/eval; no sudo install scripts; per-repo venvs under `/workspace/repo-lab/<owner>__<name>/`; ≤~5 min install/test each.

## Counts (TESTED)

| Metric | Count |
|---|---:|
| Unique repos listed in REPOS.csv | **40** |
| Attempted (clone + install/inspect) | **17** |
| Working (PASS install/import or docs-ok) | **15** |
| SKIP (clone ok, full install not appropriate) | **2** (Grok-ready, tessera-grok-handoff) |
| BLOCKED (private/auth/vault/gone) | **14** |
| NOT_ATTEMPTED (lower priority / large snapshots / langchain) | **6** |
| UNKNOWN (redirects only) | **2** |

Files: `/workspace/repo-lab/REPOS.csv`, `/workspace/repo-lab/INSTALL-RESULTS.tsv`, `/workspace/repo-lab/SMOKES.md`, this report, `/workspace/repo-lab/PROPOSED-ITEMS.md`.

## Sources scanned (TESTED)

1. **Gitbook** `@bc6b3287` recursive tree — `merge/SOURCE-HEADS-2026-10-05.md`, `merge/source-manifest.csv`, `merge/CURRENT-REPOSITORY-STATUS.md`, `merge/repo-audit.tsv`, `merge/FUNCTIONAL-MERGE-MATRIX.md`, `brain-consciousness/SNN-SOURCE-MANIFEST.md`, `intake/CORTICAL-LABS-READINESS.md`, `mesh/roles/github-scraper.md` (no repo list).
2. **TESSERA** `@5c1137fa` — root + app `package.json` files: **no git URL dependencies** (npm/catalog only) — TESTED.
3. **Workspace** — `full-picture/INVENTORY.md`, `BENCHMARK-PLAN.md`, `TODO.md`, `BASELINE.md`, `gitbookai/`, `hyb012/`, `cl1-sim/TESSERA-FIT.md`.
4. **Account** — `search_repositories user:vitalitychems-dot` → **13** repos (TESTED).

## Install/test matrix (attempted)

| Repo | License | TESTED result | Tessera relevance |
|---|---|---|---|
| Cortical-Labs/cl-sdk | CC BY-NC 4.0 | PASS import + `cl.open()` sim | CL1 bridge (HYB-019) |
| Cortical-Labs/cl-api-doc | none listed | PASS docs clone | Tutorials for bridge |
| jeshraghian/snntorch | MIT | PASS + LIF smoke | Preferred SNN (BC-006) |
| BrainCog-X/Brain-Cog | Apache-2.0 | PASS import | Cognitive interfaces (BC-005) |
| BindsNET/bindsnet | AGPL-3.0 | PASS import | Reference-only (BC-008) |
| brian-team/brian2 | CeCILL (NOASSERTION API) | PASS via **PyPI** (editable shallow clone failed setuptools_scm) | Reference (BC-007) |
| FoundationAgents/OpenManus | MIT | PASS `app` import | Agent framework lineage |
| Aider-AI/aider | Apache-2.0 | PASS import + `--help` | Eval harness (polyglot) |
| SWE-bench/SWE-bench | MIT | PASS via PyPI `swebench` | Eval harness (paid runs) |
| mem0ai/mem0 | Apache-2.0 | PASS import | Persistent agent memory / RAG |
| chroma-core/chroma | Apache-2.0 | PASS `chromadb` | Vector index for Gitbook RAG |
| lancedb/lancedb | Apache-2.0 | PASS import | Embedded vector alt |
| crewAIInc/crewAI | MIT | PASS `crewai` | Multi-agent orchestration patterns |
| microsoft/autogen | CC-BY-4.0 | PASS `autogen-agentchat` | Multi-agent patterns |
| browser-use/browser-use | MIT | PASS import | Browser tool agent |
| vitalitychems-dot/Grok-ready | MIT (package.json) | SKIP full pnpm | Historical; HYB-006 behavior only |
| vitalitychems-dot/tessera-grok-handoff | n/a | SKIP | Zip parts; no app install |

### Key failures / caveats (TESTED)

- **brian2 editable** from shallow clone: `setuptools_scm` InvalidVersion `unknown` → recovered via PyPI.
- **SWE-bench editable** failed similarly → PyPI `swebench` OK; **full benchmark runs** need model API + $ → BLOCKED here.
- **OpenManus / aider / mem0 / crewAI / autogen / browser-use**: import/`--help` only; **live agent runs need LLM keys** → BLOCKED for end-to-end (aligns with BASELINE industry_bench_score BLOCKED).
- **BindsNET AGPL-3.0**: install works but **must not vendor into TESSERA** without AGPL review — reference/separate process only.
- **cl-sdk CC BY-NC 4.0**: mesh study OK; **commercial product embedding needs Cortical Labs grant**.
- **Private clones** (TESSERA, Gitbook, Zz, 1T, olive-giant, tessera-complete-archives): HTTPS without credentials → BLOCKED (known from INVENTORY).
- **Account snapshots** `1`/`5t`/`T44`/`TESS`/`tessera-grok-handoff-complete`: listed, **not attempted** (large historical; prefer framework priority).
- **langchain**: listed metadata only, **not attempted** (size; chroma/lancedb/mem0 cover RAG need).

## Top 8 integrations (recommended)

Measured against BASELINE: raise test/eval clarity, unlock Gitbook RAG score, CL1 readiness, agent patterns — **prefer dependency or idea adaptation over copying code**.

| # | Repo | License fit | Target place in TESSERA / Gitbook | What it adds vs baseline | Father gate |
|---|---|---|---|---|---|
| 1 | **FoundationAgents/OpenManus** | MIT — OK adapt w/ attribution | Gitbook: `merge/` or `intake/` portable-behavior note; TESSERA: optional `scripts/agents/` **ideas only** (board: no full OpenManus copy) | Recovers lineage patterns for tool-loop; does **not** invent GAIA scores | **NEEDS FATHER YES** if adding runtime dep |
| 2 | **jeshraghian/snntorch** | MIT — OK | TESSERA `modal/` or `scripts/snn/` tiny original adapter; Gitbook BC-006 | Software SNN smoke → measurable brain-lane experiments (not CL1 biology) | **NEEDS FATHER YES** for torch dep in product path |
| 3 | **mem0ai/mem0** + **chroma-core/chroma** (or **lancedb**) | Apache-2.0 — OK | TESSERA knowledge/RAG path (`lib/` + `artifacts/api-server` knowledge routes); score BASELINE 25-Q | Moves `gitbook_rag_score` from BLOCKED toward TESTED | **NEEDS FATHER YES** (new deps + runtime) |
| 4 | **Aider-AI/aider** | Apache-2.0 — OK | TESSERA `scripts/eval/` wrapper + `docs/eval/` | Industry coding-edit harness; costed runs | **NEEDS FATHER YES** (API spend ~$1–30) |
| 5 | **Cortical-Labs/cl-sdk** | CC BY-NC — **flagged** | Separate Python service under `/workspace/cl1-sim` → future `POST /cl1/*` bridge; Gitbook readiness | Simulator closed-loop already TESTED; no learning claims | Adapter code: digest yes; Cloud/hardware still blocked |
| 6 | **BrainCog-X/Brain-Cog** | Apache-2.0 — OK | Gitbook BC-005 interface map; TESSERA research adapters only | Cognitive module vocabulary for brain lane | Prefer ideas over heavy torch stack in api-server |
| 7 | **SWE-bench/SWE-bench** | MIT — OK | `scripts/eval/` harness only | Lite N=10 path for competition honesty | **NEEDS FATHER YES** (Docker + $) |
| 8 | **crewAIInc/crewAI** (alt: autogen) | MIT (autogen CC-BY caution) | Gitbook mesh playbook patterns; optional research sandbox — **not** replacing mesh roles | Multi-agent handoff patterns for ROADMAP items 3–5 | **NEEDS FATHER YES** if runtime |

### License policy applied (REPORTED + TESTED)

- **Permissive (MIT/Apache):** OK to depend or adapt with attribution.
- **GPL/AGPL (BindsNET):** reference-only or separate service; flagged.
- **NC (cl-sdk):** study/local OK; commercial embedding flagged.
- **CeCILL (brian2):** keep comparison/reference until compatibility review.
- **CC-BY-4.0 (autogen repo license field):** treat as documentation/content caution; verify code package licenses before vendoring.

## Mapping notes (GOAL)

- Do **not** merge OpenManus tree into `artifacts/*` (BASELINE Q21 / board rule).
- Do **not** copy Zz / olive-giant wholesale (HYB-007/008).
- Prefer Gitbook docs updates first for CL1/SNN license notes (Moderator path), then Father digest for dependency-adding IMPs.

## Not attempted (priority deferral)

`vitalitychems-dot/{1,5t,T44,TESS,tessera-grok-handoff-complete}`, `langchain-ai/langchain`, `OpenManus/OpenManus-RL` (secondary). Listed in REPOS.csv as NOT_ATTEMPTED / UNKNOWN.

## Next artifacts

- Improvement proposals: `/workspace/repo-lab/PROPOSED-ITEMS.md` (IMP-065+; includes 4 CL1 items from `/workspace/cl1-sim/TESSERA-FIT.md` renumbered). **Do not edit** `/workspace/improvements/LEDGER.md` (another job appends).
