# Tessera full-picture inventory

IDENTITY: Tessera Admin coordinator / Grok Bot executor  
As-of: 2026-10-05 ~5:35 PM CT  
Honesty labels: **TESTED** = verified this session; **REPORTED** = doc/commit/source says it; **GOAL**; **UNKNOWN**; **BLOCKED**.

Bases (TESTED):
- TESSERA `main@5c1137faeb7714482add93c2d6876396f34f1a03` (CI run `37382015797` success)
- Gitbook `main@bc6b32871faed56b13df3dfadc849ec725d60f14` (board = issue #2)
- Open PRs (TESTED): TESSERA none; Gitbook none
- Origin (`collin-keane/Tessera`): **BLOCKED** — `cursor-origin` `list_namespaces` returned `[]`; cannot list or read Origin repos from this connector

---

## 1. Repository sources

| Source | Visibility | Size (GitHub `size` KB / blob bytes) | Last push (UTC→CT) | What it is | Label |
| --- | --- | --- | --- | --- | --- |
| `vitalitychems-dot/TESSERA` | private | 5074 KB; tree blobs ~22.5 MB | 2026-10-05 5:22 PM CT | Active TypeScript pnpm monorepo (web + API + mockup) | TESTED |
| `vitalitychems-dot/Gitbook` | private | 1186 KB; tree blobs ~6.0 MB | 2026-10-05 5:28 PM CT | Docs, mesh coordination, HYB backlog, history | TESTED |
| `vitalitychems-dot/Zz` | private | 69486 KB | 2026-10-05 ~5:05 PM CT | Archive / historical (do not copy wholesale) | TESTED (meta only) |
| `vitalitychems-dot/1T` | private | 190110 KB | 2026-10-05 ~5:09 PM CT | Protected vault — **not inspected** | REPORTED (README forbids) |
| `vitalitychems-dot/1` | public | 190046 KB | 2026-10-05 | Historical snapshot family | TESTED (listed) |
| `vitalitychems-dot/5t` | public | 193926 KB | 2026-10-05 | Historical snapshot family | TESTED (listed) |
| `vitalitychems-dot/T44` | public | 190743 KB | 2026-10-04 | Historical snapshot family | TESTED (listed) |
| `vitalitychems-dot/TESS` | public | 188791 KB | 2026-10-02 | Historical snapshot family | TESTED (listed) |
| `vitalitychems-dot/Grok-ready` | public | 191888 KB | 2026-10-03 | Consolidation destination archive | TESTED (listed) |
| `vitalitychems-dot/olive-giant-ever-glade` | private | 127233 KB | 2026-10-04 | Separate app candidate (HYB-008) | TESTED (listed) |
| `vitalitychems-dot/tessera-grok-handoff` | public | 205256 KB | 2026-10-03 | Privacy-screened handoff | TESTED (listed) |
| `vitalitychems-dot/tessera-grok-handoff-complete` | public | 160371 KB | 2026-10-02 | Sanitized combined archive handoff | TESTED (listed) |
| `vitalitychems-dot/tessera-complete-archives` | private | 158436 KB | 2026-10-02 | Private complete archive (credentials redacted claim) | TESTED (listed) |
| `user:collin-keane` GitHub search | — | — | — | **422** — no permission / user not searchable | BLOCKED |
| Origin `collin-keane/Tessera` | — | — | — | Namespace list empty | BLOCKED |

HTTPS clone of private TESSERA without credentials: **failed** (TESTED). Inventory uses MCP `get_file_contents` / `get_git_tree` only.

### Box files (TESTED)

| Path | Role |
| --- | --- |
| `/workspace/improvements/LEDGER.md` | 50 IMP-* proposals (IMP-001–050), PROPOSED |
| `/workspace/hyb-selffix/DESIGN.md` + `dryrun/` | Self-fix phase-0 design (Father-approved phase 0) |
| `/workspace/hyb012/` | HYB-012 comments notes |
| `/workspace/gitbookai/GITBOOKAI-PLAN.md` | Product plan draft (GOAL-heavy) |
| `/workspace/build-gate/` | Build gate reports + CI log excerpts (incl. validate log for run tip) |
| `/workspace/security-gate/` | Security gate worktrees |
| `/workspace/gitbook-cordnation/`, `gitbook-gate-*` | Local Gitbook worktrees (SHAs ≠ necessarily main tip) |
| `/workspace/tessera-gate/` | Review notes |

---

## 2. What TESSERA actually does (code)

### Apps (TESTED — README + tree)

| App | Path | Port (default) | Role |
| --- | --- | --- | --- |
| Tessera web | `artifacts/tessera` | 3000 | Main UI |
| Tessera API | `artifacts/api-server` | 5000 | Express API; suite starts API only for loopback `DATABASE_URL` |
| Mockup sandbox | `artifacts/mockup-sandbox` | 5173 | Component preview |
| Shared libs | `lib/` (`db`, `api-client-react`, `api-spec`, `api-zod`) | — | Drizzle DB + generated clients |
| Modal / scripts | `modal/`, `scripts/` | — | GPU tasks + `dev-unified` / `test-unified` / `build-unified` |
| Archives | `archives/source-variants/`, `archives/drive-export/` | — | Historical variants; **not** active workspace packages |

### Route surface (TESTED)

- **86** route modules under `artifacts/api-server/src/routes/*.ts` (TESTED tree count).
- Mount order in `routes/index.ts` (TESTED): `sovereignEngines` first … `legacyEngines` later … many domain routers (knowledge, council, evaluation, agi, ingestion, inventions, …).
- **10 exact METHOD+path duplicate collisions** allow-listed in `route-inventory.test.ts` (TESTED): 8 non-quantum + 2 ruling-named quantum (`GET /quantum/state`, `POST /quantum/gate`). First-mounted module wins.
- Registration total "~925" is **NOT TESTED** (Build gate explicitly: CI never prints it).

### How an LLM is invoked (TESTED)

1. Primary client: `artifacts/api-server/src/lib/llm-client.ts` → OpenAI SDK against `AI_INTEGRATIONS_OPENAI_BASE_URL` + `AI_INTEGRATIONS_OPENAI_API_KEY` (dummy key fallback string if unset).
2. Default model string in `callLLM`: `"gpt-5-mini"` (TESTED in source).
3. **External LLM gate:** `isLLMAvailable()` returns false unless `SOVEREIGN_NO_EXTERNAL_LLM` is unset/false **and** `AI_INTEGRATIONS_OPENAI_BASE_URL` is set. Default of `SOVEREIGN_NO_EXTERNAL_LLM` is `"1"` → **external LLM off by default** (TESTED).
4. Side paths: semantic cache, knowledge distillation injection into prompts, dream-prompt bridge, llm-batcher, output sanitization via `external-sandbox-policy`.
5. Embeddings: `neural-embeddings.ts` tries OpenAI `text-embedding-3-small` via same base URL; falls back to local hash embedding (TESTED).
6. Local adapters: `local-models` route — Ollama is "reference-implementation"; llama.cpp / vLLM / LM Studio / TGI marked **stub** (TESTED). Env names: `OLLAMA_ENDPOINT`, `LLAMA_CPP_ENDPOINT`, `VLLM_ENDPOINT`, `LM_STUDIO_ENDPOINT`, `TGI_ENDPOINT` (+ `*_ENABLED` for stubs).
7. `provider-registry.ts` lists cloud provider **catalog** ids (anthropic, openai, google, deepseek, xai, groq, mistral, meta, qwen, moonshot, ollama, puter) — catalog/metadata, not proof each has live keys (TESTED as code; runtime = UNKNOWN without secrets).

### Flag / learning gates

| Item | Status |
| --- | --- |
| `TESSERA_ENABLE_*` learning flags = 0 | **REPORTED** (Father / task instruction). Code search `TESSERA_ENABLE` in `vitalitychems-dot/TESSERA` returned **0 hits** (TESTED search). Do not flip. |
| `SOVEREIGN_NO_EXTERNAL_LLM` default `"1"` | TESTED in `llm-client.ts` |
| Module-load side effects | TESTED: `routes/index.ts` starts wallet observer, free-stuff scraper, bounty refresher, income executor, autonomous build timer, shepherd persistence on import |

### Env var **names** (never values) — TESTED from `.env.example` + SECRETS.md

`DATABASE_URL`, `FATHER_NATAL_CHART_JSON`, `TESSERACT_ADMIN_KEY`, `SIGIL_ADMIN_KEY`, `SOVEREIGN_ADMIN_TOKEN`, `SESSION_SECRET`, `AI_INTEGRATIONS_OPENAI_BASE_URL`, `AI_INTEGRATIONS_OPENAI_API_KEY`, `MODAL_TOKEN_ID`, `MODAL_TOKEN_SECRET`, `BETTER_AUTH_SECRET`, `ADMIN_EMAIL`, `ADMIN_PASSWORD`, `ADMIN_TOKEN`, `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `WEBHOOK_SECRET`, `REPLIT_CONNECTORS_HOSTNAME`, `GROK_CONNECTOR_ACCESS_TOKEN`, `GITHUB_TOKEN`, `MOLTBOOK_API_KEY`, `NASA_API_KEY`, `TESSERA_API_KEY`, `FORUM_ADMIN_TOKEN`, `AGENT_PRIVATE_KEY`, ports/base paths, `VITALITY_*` storefront ports/DB URLs (stale per README), `TESSERA_TEST_DATABASE_URL`, `TESSERA_TEST_FATHER_NATAL_CHART_JSON`, plus SECRETS.md: `OLLAMA_ENDPOINT`, `VLLM_ENDPOINT`, `LLM_TIMEOUT_MS`.

**Box env (TESTED):** all AI/DB keys above **UNSET** on this machine. No Ollama binary present.

### Tests and CI (TESTED)

| Check | Result | Evidence |
| --- | --- | --- |
| Workflow | `.github/workflows/ci.yml` job `validate` | TESTED file |
| Steps | install → `pnpm audit` → typecheck → db push → `pnpm test` → build | TESTED |
| Tip run | `37382015797` **success** on `5c1137fa` | TESTED API |
| Vitest | **14 files passed**, **99 passed / 1 skipped (100)** | TESTED CI log |
| Route-inventory | 5 tests green | TESTED |
| Audit | 1 high ignored (`GHSA-vfj7-8cjw-p6xm` braces) via `pnpm-workspace.yaml` `auditConfig.ignoreGhsas` | TESTED |
| `pnpm-workspace.yaml` `allowBuilds.core-js` | placeholder string `set this to true or false` (invalid) | TESTED |
| Active `__tests__` files | 15 under api-server (excl. helpers) | TESTED tree |

### Internal "evaluation" (TESTED — honesty)

`routes/evaluation.ts` embeds a homemade `MMLU_STYLE_QUESTIONS` list (~60 MCQs). This is **not** the official MMLU / MMLU-Pro dataset or harness. Treating its scores as industry MMLU would be a claim without evidence. Similarly `agi.ts` exposes in-process "working memory / bus / causal / metacognition" HTTP stubs — engineering modules named AGI, **not** AGI capability proof (aligns with who-tessera-is: not AGI).

---

## 3. Gitbook docs (TESTED)

| Item | Value |
| --- | --- |
| Tree | 128 blobs; ~6.0 MB |
| Nav | `SUMMARY.md` — **72** relative links; **0 broken** vs tip tree |
| Notable orphan page | `intake/CORTICAL-LABS-READINESS.md` exists but **not** in SUMMARY (also IMP-026) |
| Board | Issue #2 "Tessera hybrid consolidation agent conference" (open, 40 comments) |
| Backlog | `intake/HYBRID-CONSOLIDATION-BACKLOG.md` — HYB-001–019; HYB-012 still **IN REVIEW** in backlog text despite code merge (stale REPORTED) |
| Honesty | `mesh/roles/honesty-banner.md`, `who-tessera-is.md`: persona + TypeScript mesh on third-party LLMs; no owned weights; no AGI as present fact |
| Mesh agents | Cordnation, Moderator, Command Center, Tessera, Mesh Cloud, Build, Grok Bot, Security = Active; several Provisional/TBD |

---

## 4. Ingested knowledge — where, format, runtime use

| Store / path | Format | Runtime use | Label |
| --- | --- | --- | --- |
| DB `ingestedDataTable` + `recallIngestedKnowledge` | rows: title/content/source; keyword `ilike` | Optional context strings for sovereign paths | TESTED code; population **UNKNOWN** without DB |
| DB `distilledKnowledgeTable` / `knowledgeCanonicalTable` | fact strings + confidence; optional embeddings | `lookupKnowledge` injects into LLM prompts / short-circuit | TESTED code; needs DB + usually LLM |
| `lib/ingestion/*` (scrapers, rss, github, pipeline, scheduler) | ingestion pipelines | Flag/route gated; not exercised here | TESTED files exist |
| Gitbook markdown corpus | markdown in repo | **No** dedicated RAG index over Gitbook found in TESSERA | TESTED absence for Gitbook→API retrieval path |
| Archives / OCR / screenshots | docs + `review/image-text/` | Explicitly untrusted / lossy; not runtime product memory | TESTED docs |
| `.agents/memory/outbound-knowledge-sources.md` | notes | Agent memory note, not product RAG | TESTED path |

**Conclusion:** there is code that *can* recall distilled/ingested DB facts when a local DB is populated and LLM/cache paths run. There is **no TESTED** path that answers questions from Gitbook docs as a RAG corpus today. Gitbook is coordination docs for humans/agents, not a live retrieval backend.

---

## 5. Real capability today

1. **Coordination mesh works as process** (TESTED): private Gitbook + TESSERA, issue #2, HYB board, four gates, Build/Security reports, green CI after HYB-005/012.
2. **Shipable monorepo** (TESTED): typecheck + 99 tests + build pass in CI with disposable Postgres.
3. **HTTP product surface is large** (TESTED): dozens of Express routers; many domains (knowledge, council, inventions, evaluation, agi-named modules). Capability of each route beyond unit tests = mostly **UNKNOWN** without live server + DB + keys.
4. **LLM features are opt-in and currently off on this box** (TESTED): no `AI_INTEGRATIONS_OPENAI_*`, no Ollama; default sovereignty kill-switch on.
5. **Honest self-description exists** (TESTED docs): who-tessera-is / honesty-banner deny AGI, owned weights, consciousness as facts.
6. **Historical archives are large** (TESTED repo list) but intentionally not product; OpenManus lineage is **REPORTED** background (task + archives), not a live OpenManus harness in active apps.

## 6. Claims without evidence (do not treat as capability)

- AGI / continuous consciousness / owned weights / finished sovereign self — **GOAL** or archive claim; denied by who-tessera-is.
- "~925 routes" as a measured CI number — **NOT TESTED**.
- Official MMLU / SWE-bench / GAIA / ARC-AGI scores for "Tessera" — **none found**; homemade MCQ list ≠ MMLU.
- Manus/OpenManus scores attributed to Tessera — **none**; Manus GAIA numbers are vendor-reported for Manus product, not this repo.
- Screenshot / OCR / Drive archive capability claims — docs say untrusted (TESTED `09_ARCHIVE_REVIEW_AND_CLAIMS.md`).
- Live storefront / wallets / payments / [REDACTED-PATH] contents — out of scope; storefront not active workspace (TESTED README).
- Origin engine as running system — **BLOCKED** (no Origin access).
- `TESSERA_ENABLE_*` named flags in code — **not found** (search 0); do not invent scores or flip flags.
