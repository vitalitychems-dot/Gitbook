# Local Ollama baseline (honest, free, CPU-only)

As-of: **2026-10-05 ~6:05 PM CT**  
Labels: **TESTED** = measured this session; **REPORTED** = cited from docs/plan; **BLOCKED** = could not run.

> These are **small subsets on a small local 3B model**. They are **not** comparable to leaderboard runs of frontier models in `/workspace/full-picture/BENCHMARK-PLAN.md`. Do not publish them as Tessera AGI scores. Tessera remains a TypeScript mesh; this measures **qwen2.5:3b-instruct via Ollama** on this box.

---

## 1. Hardware & install (TESTED)

| Item | Value |
| --- | --- |
| CPU | Intel Xeon Processor, **8** cores (no hyperthreads) |
| RAM | **15 GiB** total; ~3.6–5.3 GiB available before load; **no swap** |
| GPU | **None** (CPU inference only) |
| Disk | overlay ~126G; plenty free after install |
| Ollama | **0.35.1** static binary → `/workspace/ollama-install/`; `ollama serve` background on `127.0.0.1:11434` (systemd **absent**; official script would need root/`/usr/local`) |
| Models dir | `/workspace/ollama-home/models` |
| Model | **`qwen2.5:3b-instruct`** (chosen because RAM ≺ 16 GiB free headroom; 7B/8B would not fit comfortably with ~4–5 GiB available under multi-agent load) |
| Quantization | **Q4_K_M** (gguf); parameter size **3.1B** |
| Smoke prompt | “Say hello…” → response OK; **~13.5 tok/s** (first load); later means ~10–20 tok/s depending on bench |
| Spend | **$0** |

**Not touched (per standing rules):** GitHub writes, secrets, `TESSERA_ENABLE_*`, wallets/payments, [REDACTED-PATH]

---

## 2. Public benchmark subsets (TESTED)

Scripts: `/workspace/evals/harness/`  
Raw outputs: `/workspace/evals/results/20261005-174126/`  
Seed: **42** (GSM8K & ARC shuffle); HumanEval = first **N** official IDs (seed unused for selection).

### ARC-Challenge (TESTED)

| Field | Value |
| --- | --- |
| Source | AI2 ARC-V1-Feb2018 `ARC-Challenge-Test.jsonl` (public) |
| n | **50** |
| Correct | **35 / 50** |
| Accuracy | **0.70** |
| Wall | **~84 s** |
| Mean tok/s | **~17.7** |
| Grading | Exact letter A–D |
| Item IDs | `Mercury_SC_410971`, `Mercury_SC_414274`, `Mercury_7214498`, `Mercury_7009555`, `Mercury_401699`, `Mercury_7057680`, `Mercury_7205608`, `NYSEDREGENTS_2010_4_4`, `ACTAAP_2010_7_3`, `CSZ_2009_8_CSZ20740`, `Mercury_SC_400579`, `VASoL_2007_5_22`, `Mercury_7186358`, `MCAS_1998_8_24`, `Mercury_SC_416169`, `Mercury_SC_401142`, `MCAS_2006_9_34`, `Mercury_400828`, `Mercury_SC_413299`, `Mercury_SC_407382`, `Mercury_SC_413089`, `Mercury_LBS10610`, `TIMSS_2011_4_pg27`, `Mercury_SC_400661`, `Mercury_7004725`, `Mercury_SC_405880`, `Mercury_SC_400392`, `MCAS_2006_9_44`, `Mercury_SC_406855`, `Mercury_SC_410630`, `MEAP_2005_8_45`, `ACTAAP_2009_5_12`, `MCAS_2014_5_13`, `TIMSS_1995_8_L6`, `Mercury_7268258`, `Mercury_7264093`, `Mercury_7234605`, `Mercury_7081480`, `Mercury_7007420`, `Mercury_416633`, `Mercury_SC_409030`, `MCAS_2010_8_12005`, `Mercury_SC_401277`, `Mercury_7085225`, `Mercury_415083`, `Mercury_SC_405130`, `VASoL_2010_3_39`, `Mercury_LBS11018`, `MCAS_1998_4_13`, `NYSEDREGENTS_2008_8_36` |
| Raw | `results/20261005-174126/arc_challenge.json` |

### GSM8K (TESTED — subset shrunk for time)

| Field | Value |
| --- | --- |
| Source | `openai/grade-school-math` test.jsonl (public raw) |
| n | **25** (shrunk from planned 50: CPU ~10 tok/s on long math gens; keep total under ~40 min) |
| Correct | **8 / 25** |
| Accuracy | **0.32** |
| Wall | **~436 s** |
| Mean tok/s | **~10.5** |
| Grading | Numeric equality after `####` / last number; commas stripped |
| Item IDs | `gsm8k_test_{588,1214,57,906,1252,618,599,289,608,400,237,616,672,1132,463,222,945,238,730,55,772,176,15,66,479}` (test-split indices after seed-42 shuffle) |
| Raw | `results/20261005-174126/gsm8k.json` |

### HumanEval (TESTED — subset)

| Field | Value |
| --- | --- |
| Source | Official `HumanEval.jsonl` (OpenAI human-eval) |
| n | **15** (first 15; shrunk from 20–40 for time) |
| Correct | **3 / 15** |
| pass@1 | **0.20** |
| Wall | **~90 s** |
| Mean tok/s | **~13.7** |
| Grading | Execute `check(entry_point)` in sandboxed subprocess, timeout 5s |
| Item IDs | `HumanEval/0` … `HumanEval/14` |
| Raw | `results/20261005-174126/humaneval.json` |

### Not run / BLOCKED

| Attempt | Status |
| --- | --- |
| MMLU-Pro | **Not run** this session (time); ARC-Challenge used instead |
| SWE-bench / Aider / GAIA / paid APIs | **BLOCKED** — no spend; no `AI_INTEGRATIONS_OPENAI_*` (see BENCHMARK-PLAN) |
| 7B/8B local models | **Not pulled** — insufficient free RAM headroom under multi-agent load |

---

## 3. Gitbook knowledge check (TESTED)

Question set: `/workspace/full-picture/BASELINE.md` §C (25 Qs).  
Corpus: `/workspace/evals/data/gitbook-corpus/` (Gitbook markdown from tip SHA `bc6b328…` via read-only MCP + local Gitbook worktrees). **BASELINE answer key not in corpus.**

| Mode | Score | Wall | Notes |
| --- | --- | --- | --- |
| **(a) Model alone** | **7 / 25 = 0.28** | ~24 s | Strict key-fact grade |
| **(b) + BM25 top-3 chunks** | **18 / 25 = 0.72** | ~102 s | Same grader |

**Grading rule (strict, documented):** per-question required key facts (e.g. Q2 must mention Gitbook issue `#2`; Q6/23 require xAI+Grok; Q10 requires `GHSA-vfj7…` / `vfj7`; Q16 requires Moderator→Tessera→Security→CI/Build; Q25 requires the word `validate`). Yes/no items need an explicit denial. A looser first-pass grader inflated alone to 12/25 (false positives like matching the substring “gitbook”); strict scores above are authoritative. Raw + both grades: `results/20261005-174126/gitbook_quiz.json`.

**Still wrong with retrieval (strict):** Q1 (two-repo roles phrasing), Q3 (**Father = Collin Keane** — name not found in Gitbook corpus; alone/rag both fail), Q9 (HYB-005 detail), Q11 (HYB-012 deliverable), Q18 (CC never pushes Gitbook — alone lucked a denial; RAG drifted), Q20 (HYB-019 / Cortical), Q25 (CI job `validate` — not stated as such in retrieved chunks; model cited an audit job id).

**Retrieval delta (TESTED):** alone **0.28** → RAG **0.72** (**+0.44** absolute). Shows BM25 over our Gitbook docs helps a small local model on mesh/process facts; it does **not** prove a production Tessera RAG path (that remains **BLOCKED** per BASELINE/INVENTORY — no Gitbook→runtime retrieval in product).

---

## 4. Honest comparison note (cite BENCHMARK-PLAN; do not invent Tessera leaderboard scores)

From `/workspace/full-picture/BENCHMARK-PLAN.md` (public references only):

- Industry boards cited there (SWE-bench Verified, Aider polyglot, GAIA, HLE, etc.) are **frontier / agent** runs costing money — **BLOCKED** here.
- HumanEval / GSM8K / ARC on a **3B Q4 CPU** subset are expected to land **far below** frontier published numbers; we **do not** invent a 3B reference row.
- Homemade `MMLU_STYLE_QUESTIONS` in Tessera `evaluation.ts` remains **rejected** as an MMLU stand-in (BENCHMARK-PLAN honesty).
- **Tessera has no published SWE/GAIA/HLE scores** (BENCHMARK-PLAN TESTED search). This local file must not be misread as one.

Rough context only (not Tessera): chance on ARC-Challenge 4-way is **25%**; this 3B subset hit **70%** on n=50 — useful smoke, not a board submission.

---

## 5. Runtime & paths (TESTED)

| Phase | Approx CT window |
| --- | --- |
| Install Ollama + pull model + smoke | ~5:38–5:39 PM |
| ARC / GSM8K / HumanEval / quiz | ~5:41–6:05 PM |
| Bench wall sum (ARC+GSM8K+HE+quiz) | ~84 + 436 + 90 + 126 ≈ **~12.3 min** model time; GSM8K dominated |

| Path | Role |
| --- | --- |
| `/workspace/evals/BASELINE-LOCAL.md` | This report |
| `/workspace/evals/harness/*.py` | Repeatable harness (IMP-051 precursor) |
| `/workspace/evals/data/` | GSM8K, HumanEval, ARC-Challenge, gitbook-corpus |
| `/workspace/evals/results/20261005-174126/` | Raw JSON + logs + `meta.json` |
| `/workspace/ollama-install/` | Ollama 0.35.1 binary tree |
| `/workspace/ollama-home/` | Models + serve.log |

---

## 6. Snapshot line

```
date_ct: 2026-10-05 18:05 CDT
ollama: 0.35.1
model: qwen2.5:3b-instruct Q4_K_M 3.1B
hw: 8x Xeon CPU, 15GiB RAM, no GPU
arc_challenge: 35/50=0.70 seed=42
gsm8k: 8/25=0.32 seed=42
humaneval: 3/15=0.20 first-15
gitbook_quiz_alone: 7/25=0.28
gitbook_quiz_bm25: 18/25=0.72
spend_usd: 0
```
