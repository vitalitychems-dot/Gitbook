# RESULTS — before/after improvement test (TESTED)

As-of: **2026-10-12 ~4:00 PM CT**  
Bases: Gitbook `main@cd8faa0a`, TESSERA `main@a502322`  
Harness: `/workspace/evals/harness/bm25.py` + local Ollama `qwen2.5:3b-instruct`  
Work dir: `/workspace/improve-from-logs-2026-10-12/`  
Labels: **TESTED** = measured this session; **BLOCKED** = could not run.

## Setup (TESTED)

| Item | Value |
| --- | --- |
| Quiz | 10 consolidation / repo-knowledge questions (custom; not the 25-q baseline) |
| Before corpus | 42 Gitbook markdown pages → **173** BM25 chunks |
| After corpus | same + `ZZ_EXPANDED_REPO_INDEX.md` built from extracted names → **182** chunks |
| Expanded index | `16041` bytes; lists active destinations, routing rules, third-party memory/agent/SNN/LLM refs, full owner/repo list |
| Model | qwen2.5:3b-instruct (Q4_K_M), CPU Ollama on 127.0.0.1:11434 |
| Spend | $0 |

## Retrieval-only (TESTED)

A question **hits** if BM25 top-3 chunks contain enough expected key substrings.

| Condition | Correct | Accuracy |
| --- | ---: | ---: |
| Before (no expanded index) | 4 / 10 | **40%** |
| After (with expanded index) | 7 / 10 | **70%** |
| Delta | +3 | **+30 pp** |

Questions that flipped from miss → hit: **Q6** (OpenManus/FoundationAgents), **Q7** (SNN libs), **Q10** (llama.cpp).

## Model + RAG (TESTED)

Same 10 questions; model answers using BM25 top-3 context. Graded by key-substring match.

| Condition | Correct | Accuracy | Wall time |
| --- | ---: | ---: | ---: |
| Before | 3 / 10 | **30%** | 38.7s |
| After | 4 / 10 | **40%** | 20.5s |
| Delta | +1 | **+10 pp** | — |

Honest read: the expanded index **clearly improves retrieval** (+30 pp). The small 3B model only gained **+10 pp** on answer grading (still often paraphrases past the key tokens). Next gate item should wire the expanded index into Tessera's real Gitbook retrieval path and re-run with the same quiz.

## Raw

- `results-raw.json` — full per-question retrieval and model traces  
- `corpus-before/`, `corpus-after/` — local corpora used  

## What was NOT claimed

- Not an AGI score. Not comparable to frontier leaderboards.  
- Did not prove Tessera app code improved — only that an expanded repo index improves local retrieval for consolidation Q&A.  
- No GitHub writes. No 1T / wallet / credential files opened.
