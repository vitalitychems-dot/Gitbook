# Baseline — are we improving? (honest, no paid keys)

As-of: **2026-10-05 5:34 PM CT**  
SHAs: TESSERA `5c1137faeb7714482add93c2d6876396f34f1a03`; Gitbook `bc6b32871faed56b13df3dfadc849ec725d60f14`

## A. Repo health (TESTED)

| Metric | Value | Evidence |
| --- | --- | --- |
| CI `validate` | **PASS** | Run `37382015797` (created 2026-10-05 5:22 PM CT, completed ~5:25 PM CT) |
| Vitest | **14** files; **99 passed / 1 skipped** | CI log in `/workspace/build-gate/work-TESSERA-PR1-postmerge-5c1137fa/validate-job-112006094090.log` |
| Typecheck | PASS (CI step) | same run |
| Build | PASS (CI step) | same run |
| Audit | PASS with **1** high ignored (`GHSA-vfj7-8cjw-p6xm`) | `pnpm-workspace.yaml` + CI |
| Open PRs | TESSERA **0**; Gitbook **0** | `list_pull_requests` |
| Active route modules | **86** | tree count `artifacts/api-server/src/routes/*.ts` |
| Duplicate METHOD+path collisions | **10** allow-listed (8 non-quantum + 2 quantum) | `route-inventory.test.ts` |
| Registration total ~925 | **NOT TESTED** | Build gate C3 |
| Active api-server test files | **15** (+ helpers) | tree |
| `allowBuilds.core-js` placeholder | invalid string present | `pnpm-workspace.yaml` |
| Local `pnpm test` / typecheck on box | **BLOCKED** — no clone (HTTPS auth fail); no `DATABASE_URL` | this session |
| Model API | **BLOCKED** — `AI_INTEGRATIONS_OPENAI_*` UNSET; Ollama absent | env probe |

## B. Docs health — Gitbook (TESTED against tip tree)

| Metric | Value |
| --- | --- |
| SUMMARY relative links | **72** |
| Broken internal SUMMARY links | **0** |
| Notable orphan (exists, not in SUMMARY) | `intake/CORTICAL-LABS-READINESS.md` (+ other historical orphans; see INVENTORY) |
| Stale backlog wording | HYB-012 still **IN REVIEW** in `HYBRID-CONSOLIDATION-BACKLOG.md` though inventory test is on TESSERA main (REPORTED mismatch; IMP-027) |
| Stale agent-checkins | HYB-012 active claim not closed (REPORTED; IMP-028) |

## C. Knowledge-base retrieval quality

### Question set (25) — answerable from Gitbook tip docs (expected answers abbreviated)

Designed for a future RAG harness. **Tessera runtime retrieval of these: BLOCKED** (no Gitbook RAG path; no DB populated on this box; external LLM off).

| # | Question | Expected (from docs) |
| --- | --- | --- |
| 1 | What are the two active repos' roles? | TESSERA = app; Gitbook = instructions/coordination |
| 2 | What is the single coordination board? | Gitbook issue #2 |
| 3 | Who is Father? | Collin Keane |
| 4 | Does Tessera have owned weights? | No (GOAL until chamber test) |
| 5 | Is Tessera AGI today? | No |
| 6 | What instrument is the Pen? | xAI/Grok |
| 7 | Label TESTED means? | Real output / named check seen |
| 8 | Label REPORTED means? | Stated, not proven |
| 9 | What does HYB-005 decide? | Narrow braces advisory ignore |
| 10 | Which GHSA is ignored? | GHSA-vfj7-8cjw-p6xm |
| 11 | What did HYB-012 deliver? | Route inventory test; duplicates allow-listed |
| 12 | How many ruling-named quantum duplicate routes? | Two |
| 13 | Which module wins GET /quantum/state? | system-runtime (mount order) |
| 14 | May agents flip TESSERA_ENABLE_*? | No |
| 15 | May agents open [REDACTED-PATH] | No |
| 16 | Four gates order? | Moderator → Tessera → Security → CI/Build |
| 17 | Who merges TESSERA? | Needs Father's explicit "merge" |
| 18 | Command Center pushes Gitbook? | Never; only private Replit app-set after yes |
| 19 | Status of Recursive Learning Sponge? | Provisional / not instantiated |
| 20 | HYB-019 blocker? | Father decisions on Cortical Labs readiness |
| 21 | OpenManus full copy into TESSERA? | Not the board rule — recover portable pieces only |
| 22 | Storefront in active workspace? | No |
| 23 | Honesty banner instrument line? | Pen is currently xAI/Grok |
| 24 | What is SOVEREIGN_NO_EXTERNAL_LLM default behavior? | External LLM treated off unless opted in |
| 25 | CI job name? | validate |

**Retrieval path check:** `ingested-recall` / `knowledge-distillation` require Postgres tables + optional embeddings API — **not runnable** here. Scoring this quiz via Tessera API = **BLOCKED** until: (1) retrieval path over Gitbook or ingested corpus exists, (2) `DATABASE_URL` local, (3) either Ollama or `AI_INTEGRATIONS_OPENAI_*` with `SOVEREIGN_NO_EXTERNAL_LLM=0`.

## D. Tiny public benchmark subset locally

| Attempt | Result |
| --- | --- |
| Ollama / local model HumanEval slice | **BLOCKED** — `ollama` not installed; no local weights |
| Paid API HumanEval / Aider smoke | **BLOCKED** — needs `AI_INTEGRATIONS_OPENAI_API_KEY` (or provider key behind that base URL); estimated **$1–5** for a tiny smoke, **~$30** for one Aider polyglot-class run (GPT-5 published cost) |
| Homemade evaluation.ts MCQs as "MMLU" | **Rejected as baseline** — not industry MMLU |

## E. Baseline snapshot (for future deltas)

```
date_ct: 2026-10-05 17:34 CDT
tessera_sha: 5c1137faeb7714482add93c2d6876396f34f1a03
gitbook_sha: bc6b32871faed56b13df3dfadc849ec725d60f14
ci_run: 37382015797 success
tests: 99 passed / 1 skipped
route_modules: 86
duplicate_allow_list: 10
summary_broken_links: 0
gitbook_rag_score: BLOCKED
industry_bench_score: BLOCKED
```

Re-measure after each merge by re-running CI tip + re-counting allow-list length + docs orphans.
