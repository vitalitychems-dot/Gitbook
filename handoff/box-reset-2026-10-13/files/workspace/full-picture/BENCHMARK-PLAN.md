# Benchmark plan — Tessera vs industry agent/LLM categories

As-of: 2026-10-05 ~5:35 PM CT  
Honesty: competitor scores only from cited public sources with date. **No Tessera industry scores inventable** — Tessera has none published. Homemade `MMLU_STYLE_QUESTIONS` in `evaluation.ts` is **not** MMLU-Pro.

Underlying model for any Tessera agent run = whatever is behind `AI_INTEGRATIONS_OPENAI_BASE_URL` (or Ollama). Tessera is a **TypeScript agent/app mesh**, not a model with weights. Scores measure (model + harness + tools), not "Tessera AGI."

## Env / keys needed (names only) — TESTED

Configured in `.env.example` / code: `AI_INTEGRATIONS_OPENAI_BASE_URL`, `AI_INTEGRATIONS_OPENAI_API_KEY`, optional `OLLAMA_ENDPOINT`, `VLLM_ENDPOINT`, `LLM_TIMEOUT_MS`, `SOVEREIGN_NO_EXTERNAL_LLM` (must be `0` to allow external LLM), `DATABASE_URL` / `TESSERA_TEST_DATABASE_URL` for DB-backed paths.  
**This box:** all unset; no Ollama binary (TESTED).

---

## Category matrix

### 1. Coding agents

| Benchmark | Measures | How Tessera would run | Runnable now? | Cost estimate | Public reference scores (cited) |
| --- | --- | --- | --- | --- | --- |
| **SWE-bench Verified** | Resolve real GH issues with agent + tests | Wrap coding agent that edits repos; call underlying model via OpenAI-compatible endpoint; use official or mini-SWE-agent harness | **BLOCKED** — needs model API + Docker/harness + substantial $ | Full Verified often **hundreds–thousands USD** per model (vendor-dependent); Lite cheaper | Vals/Ridge board (archived 2026-09-01): Claude Opus 5 **97%**, DeepSeek V4 Pro **96.4%**, GPT-5.6 Sol **96.2%**, Grok 4.6 **95.6%**, Gemini 3.7 Flash **80.8%** — https://ridgebench.com/benchmarks/swe-bench (fetched 2026-10-05). Official board: https://www.swebench.com/ |
| **SWE-bench Lite** | Smaller subset | Same | **BLOCKED** (API key) | Lower than Verified; still paid | Same sources; Lite tab on swebench.com |
| **Aider polyglot** | Edit/fix 225 hard Exercism tasks via Aider | Point Aider at same OpenAI-compatible model Tessera uses | **BLOCKED** (API key; ~$0.3–$150/run per model on published board) | GPT-5 high run cost ~**$29** (published) | BenchLeader 2026-10-05: GPT-5 **88.0%**, o3-pro **84.9%**, Gemini 2.5 Pro **83.1%**, Grok 4 **79.6%**, Claude Opus 4 **72.0%** — https://www.benchleader.com/benchmarks/aider_polyglot ; official https://github.com/Aider-AI/aider (leaderboards) |
| **HumanEval / MBPP** | Function synthesis pass@k | Simple harness calling `callLLM` | **BLOCKED** (API) or local Ollama if installed | HumanEval ~164 problems: few $ on cheap models; free if local | Use papers / eval harnesses; do not invent Tessera scores |

### 2. General assistants & tool use

| Benchmark | Measures | Tessera harness | Runnable now? | Cost | Public references |
| --- | --- | --- | --- | --- | --- |
| **GAIA** | Multi-step tool-using assistant Qs | Need browser/search/code tools wired to Tessera agent loop | **BLOCKED** — no keys; no GAIA harness in-repo | Agent runs expensive; vendor runs vary | HF GAIA leaderboard/dataset: https://huggingface.co/datasets/gaia-benchmark/results_public ; space https://huggingface.co/spaces/gaia-benchmark/leaderboard . Example rows (dataset): Hugging Face Agents + GPT-4o **44.24%** (2024-06-26); Alita v2.1 (Claude Sonnet 4 + GPT-4o) **87.27%** (2025-05-24) — from HF results_public. **Manus** vendor-reported GAIA L1/L2/L3 **86.5% / 70.1% / 57.7%** (Mar 2025 launch coverage) — secondary reporting e.g. https://codersera.com/blog/manus-ai-vs-open-manus-which-ai-powered-writing-tool-is-best/ ; treat as **vendor claim**, not Tessera. **OpenManus:** no first-party published GAIA score (OpenManus README plans benchmarks; community submit attempt without published official number) — https://github.com/OpenManus/OpenManus |
| **GAIA-2** | Newer agent eval | Same | **BLOCKED** | Paid | HF ARE leaderboard commit (2026-04): Claude Opus 4.6 (high) pass@1 **57.0%**, GPT-5.4 (high) **55.6%**, Gemini 3.1 Pro (high) **52.0%** — https://huggingface.co/spaces/meta-agents-research-environments/leaderboard |
| **BFCL** (Berkeley Function Calling) | Tool/function call accuracy | Map Tessera tool schemas to BFCL | **BLOCKED** (API keys for proprietary models) | Moderate | Live board https://gorilla.cs.berkeley.edu/leaderboard.html (updated **2026-04-12**). Reproduce via `bfcl-eval` package — do not invent scores here without fetching table rows. |
| **tau-bench / AgentBench** | Domain agent tasks | Custom adapter | **BLOCKED** | Paid | Cite papers/leaderboards when run; not executed this session |

### 3. Web / computer use

| Benchmark | Measures | Runnable now? | Notes / refs |
| --- | --- | --- | --- |
| **WebArena** | Web agent success | **BLOCKED** — env + model $ | See WebArena project pages/papers |
| **OSWorld** | Desktop computer use | **BLOCKED** — heavy VM + multimodal API | https://os-world.github.io/ |

### 4. Reasoning & knowledge (model-centric)

These mostly score the **underlying LLM**, not Tessera scaffolding. Run only if Father wants model comparison with a chosen provider.

| Benchmark | Runnable now? | Public references (dated) |
| --- | --- | --- |
| **MMLU-Pro** | **BLOCKED** (API) | Saturated / directional only in 2026 commentary; prefer GPQA/HLE for frontier (secondary analyses). Do not confuse with Tessera's homemade MCQs. |
| **GPQA Diamond** | **BLOCKED** | Secondary aggregators quote GPT-6 Astra ~**96%** GPQA / ~**95.8%** Diamond, Gemini 3.1 Pro **94.3%** (e.g. https://anotherwrapper.com/tools/llm-pricing/leaderboards/reasoning as of 2026-10-03). Prefer primary papers/boards when spending. |
| **ARC-AGI-1/2** | **BLOCKED** | Live: ARC Prize leaderboard. Secondary: Gemini 3.1 Pro ARC-AGI-2 **77.1%**, GPT-6 Astra claims high on some boards (aggregator divergence — cite primary before decisions). |
| **Humanity's Last Exam (HLE)** | **BLOCKED** | Artificial Analysis via https://pricepertoken.com/leaderboards/benchmark/hle (data as of **2026-10-04**): Claude Fable 5.1 **59.1%**, Claude Fable 5 **55.5%**, GPT-6 Astra **54.7%**, Grok 4.6 **44.1%**, Gemini 3.7 Flash **47.9%**. Note Scale AI official board can diverge (documented elsewhere). |

### 5. Long context / RAG over **our** docs

| Eval | Measures | Runnable now? |
| --- | --- | --- |
| **Gitbook RAG quiz (20–30 Q)** | Retrieval + answer fidelity on Tessera/Gitbook docs | **BLOCKED for Tessera answering** — no Gitbook→runtime RAG path found (INVENTORY). Can score **human/agent reading SUMMARY** as docs-health baseline only. |
| Long-context needle-in-haystack on Gitbook zip | Model context | **BLOCKED** (API) |

### 6. Reliability / safety

| Eval | Measures | Runnable now? |
| --- | --- | --- |
| CI green rate, duplicate-route allow-list, sovereignty middleware unit tests | Engineering reliability | **Runnable / partially TESTED** via CI metrics (see BASELINE) |
| Prompt-injection / untrusted LLM sanitization | `external-sandbox-policy` | Unit-level possible without paid keys if tests cover it; full red-team **GOAL** |
| Secret/scan gates | Security lane process | Process TESTED; not a public leaderboard |

---

## OpenManus / Manus vs Tessera (honesty)

| System | Relation to Tessera | Scores |
| --- | --- | --- |
| **Tessera** | Documented persona + TS mesh on third-party LLMs; OpenManus-based history is **REPORTED** background | **No** published SWE/GAIA/HLE scores (TESTED search of repos/docs this session) |
| **OpenManus** | Open-source agent framework; Tessera archives may contain related history | No first-party GAIA number published |
| **Manus** | Separate commercial agent (GitHub App "Manus Connector" appears on issue #2 activity) | Vendor GAIA L1/L2/L3 86.5/70.1/57.7 (Mar 2025, secondary sources) |

---

## Recommended first measurable ladder (GOAL)

1. In-repo **eval harness** (repeatable) that records: model id, harness version, commit SHA, cost, date CT — without claiming AGI.
2. Free/local: Ollama + tiny HumanEval subset **or** docs RAG quiz answered by a **documented** retrieval path once built.
3. Paid (Father yes): Aider polyglot one model (~$30 for GPT-5 class) **or** SWE-bench Lite before full Verified.
4. Never publish homemade MCQ accuracy as "MMLU."
