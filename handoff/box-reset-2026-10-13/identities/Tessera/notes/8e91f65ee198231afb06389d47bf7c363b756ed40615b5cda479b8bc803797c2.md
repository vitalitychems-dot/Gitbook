# TODO — prioritized improvement cards (eval & capability)

IDENTITY: Tessera Admin coordinator  
As-of: 2026-10-05 ~5:35 PM CT  
Bases: TESSERA `5c1137fa` / Gitbook `bc6b3287`  
Open PRs: none / none  
LEDGER overlap: `/workspace/improvements/LEDGER.md` IMP-001–050 already cover duplicate-route cleanup, doc hygiene, boot side-effects. **This file does not re-list those IMP rows**; cards here are eval/harness/measurement-first. Status: **PROPOSED**.

---

## Father yes/no required (spending / product)

### CARD-EVAL-001 — In-repo repeatable eval harness (scaffold)
IDENTITY: Tessera Admin coordinator  
AGENT: Build + TESSERA  
TASK: Add `scripts/eval/` (or `artifacts/api-server/src/eval/`) harness that records model id, commit SHA, date CT, cost estimate, and pass/fail JSON for any suite; forbid naming homemade quizzes "MMLU."  
SOURCE: Father ask to test vs competition + honesty rules; `evaluation.ts` homemade MCQs  
TARGET: TESSERA main (via PR)  
SCOPE: new eval package + README; no workflow edits; no ENABLE flips  
DELIVERABLE: `pnpm eval:smoke` prints machine-readable baseline JSON  
ACCEPTANCE TEST: from baseline "no harness" → harness run exits 0 and writes `/artifacts/eval-results/<sha>.json` with schema fields {sha,date_ct,model,suite,n,pass,cost_usd}  
OVERLAP CHECK: mains tip; open PRs none; not in LEDGER IMP-*  
BLOCKERS: none for scaffold without API  
NEXT CHECK-IN: +24h  
STATUS: PROPOSED  

### CARD-EVAL-002 — Wire harness to free/local Ollama path
IDENTITY: Tessera Admin coordinator  
AGENT: Mesh Cloud / Build  
TASK: Document + implement eval runner against `OLLAMA_ENDPOINT` / `POST /local-models/chat` once Ollama is installed on a machine Father chooses.  
SOURCE: `local-models.ts` adapters  
TARGET: TESSERA  
SCOPE: local-only; no paid keys  
DELIVERABLE: runbook + one HumanEval-10 or docs-quiz dry run log  
ACCEPTANCE TEST: baseline BLOCKED(no ollama) → ≥1 local model run logged with model tag `ollama/<name>`  
OVERLAP CHECK: no IMP duplicate  
BLOCKERS: **Father yes** — install Ollama + pull a small model on a designated host (box or Replit)?  
NEXT CHECK-IN: after Father yes  
STATUS: PROPOSED  

### CARD-EVAL-003 — Paid smoke: choose one industry suite
IDENTITY: Tessera Admin coordinator  
AGENT: TESSERA + Build  
TASK: After harness exists, run **one** of: (A) Aider polyglot single model, or (B) SWE-bench Lite N=10 smoke, or (C) official HumanEval full.  
SOURCE: BENCHMARK-PLAN.md  
TARGET: results committed under `docs/eval/` (scores + URL citations for competitors, not fabricated Tessera history)  
SCOPE: no ENABLE flips; keys only in secret manager  
DELIVERABLE: dated score row with cost  
ACCEPTANCE TEST: baseline industry_bench_score BLOCKED → one cited Tessera+model score with $ spent  
OVERLAP CHECK: none  
BLOCKERS: **Father yes** — which suite? which model? approve spend?  
  - Aider GPT-5-class: ~**$30**/run (published)  
  - Tiny API smoke: ~**$1–5**  
  - SWE-bench Lite: often **$50–500+** depending on N and model  
NEXT CHECK-IN: after yes  
STATUS: PROPOSED  

### CARD-EVAL-004 — Provider key decision (names only)
IDENTITY: Tessera Admin coordinator  
AGENT: Security + Father  
TASK: Decide whether to set `AI_INTEGRATIONS_OPENAI_BASE_URL` + `AI_INTEGRATIONS_OPENAI_API_KEY` (and temporarily `SOVEREIGN_NO_EXTERNAL_LLM=0` only in eval env — **not** flipping `TESSERA_ENABLE_*`).  
SOURCE: llm-client.ts defaults  
TARGET: hosting secrets / local `.env.local` (never commit)  
SCOPE: product decision  
DELIVERABLE: written yes/no + which provider  
ACCEPTANCE TEST: documented decision in Gitbook ops page  
OVERLAP CHECK: SECRETS.md guidance  
BLOCKERS: **Father yes/no**  
NEXT CHECK-IN: next bulk update  
STATUS: PROPOSED  

### CARD-EVAL-005 — Cortical Labs / HYB-019 product answers
IDENTITY: Tessera Admin coordinator  
AGENT: Product / mesh prep  
TASK: Answer readiness §d questions so HYB-019 can leave BLOCKED  
SOURCE: Gitbook `intake/CORTICAL-LABS-READINESS.md`; backlog HYB-019  
TARGET: Gitbook  
SCOPE: decisions only; no accounts/spend without separate yes  
DELIVERABLE: answered checklist  
ACCEPTANCE TEST: HYB-019 status moves from BLOCKED → READY or REJECTED  
OVERLAP CHECK: IMP-026/044 (nav/cross-link) related but distinct  
BLOCKERS: **Father yes/no** on each readiness question  
STATUS: PROPOSED  

### CARD-EVAL-006 — Storefront / olive-giant product boundary
IDENTITY: Tessera Admin coordinator  
AGENT: Product  
TASK: HYB-017 / HYB-008 decisions (storefront & olive-giant retention)  
SOURCE: backlog  
TARGET: Gitbook decision page  
SCOPE: product  
DELIVERABLE: one written decision  
ACCEPTANCE TEST: HYB-017/008 leave READY with DONE/RETAINED/REJECTED  
BLOCKERS: **Father yes/no**  
STATUS: PROPOSED  

### CARD-EVAL-007 — Quantum duplicate product ruling
IDENTITY: Tessera Admin coordinator  
AGENT: TESSERA  
TASK: Keep or remove ruling-named quantum dual routes (product decision). Do not silently delete.  
SOURCE: issue #2 quantum ruling; IMP-022  
TARGET: TESSERA  
SCOPE: decision then optional code  
DELIVERABLE: Father ruling recorded  
ACCEPTANCE TEST: either documented keep + comments (IMP-022) or approved removal with tests updated  
BLOCKERS: **Father yes/no** — keep dual quantum routes?  
STATUS: PROPOSED  

---

## Fixes / engineering (standing fix rule may apply after Security+Build PASS)

### CARD-EVAL-008 — Gitbook RAG path (build on ingested knowledge)
IDENTITY: Tessera Admin coordinator  
AGENT: TESSERA  
TASK: Implement a **read-only** retrieval path that indexes Gitbook markdown (or a curated subset) and answers the 25-question BASELINE quiz with citations; use local embeddings fallback when API absent.  
SOURCE: honesty gap — ingested knowledge code exists but Gitbook not wired; BASELINE §C  
TARGET: TESSERA lib + route + eval suite  
SCOPE: no secrets; no ENABLE learning flips; no 1T  
DELIVERABLE: `GET /knowledge/gitbook-search` (or similar) + eval score  
ACCEPTANCE TEST: baseline `gitbook_rag_score: BLOCKED` → measured accuracy on 25 Q set (target ≥80% exact/contains match with citation)  
OVERLAP CHECK: not IMP-*; related to knowledge routes but new  
BLOCKERS: local DB or file index design choice  
NEXT CHECK-IN: +48h  
STATUS: PROPOSED  

### CARD-EVAL-009 — Shrink homemade evaluation labeling
IDENTITY: Tessera Admin coordinator  
AGENT: TESSERA  
TASK: Rename/relabel `MMLU_STYLE_QUESTIONS` in `evaluation.ts` to `INTERNAL_QUIZ` / `tessera-internal-mcq`; strip any API responses that claim "MMLU" score.  
SOURCE: honesty rules; BENCHMARK-PLAN  
TARGET: `artifacts/api-server/src/routes/evaluation.ts` (+ UI strings if any)  
SCOPE: naming + docs only  
DELIVERABLE: PR  
ACCEPTANCE TEST: ripgrep `MMLU` in evaluation route returns 0 misleading industry claims; tests updated  
OVERLAP CHECK: none in LEDGER  
STATUS: PROPOSED  

### CARD-EVAL-010 — Close HYB-012 board hygiene (docs)
IDENTITY: Tessera Admin coordinator  
AGENT: Gitbook Cordnation / Moderator  
TASK: Mark HYB-012 DONE in backlog + close check-in claim with commit evidence `50876d40` / tip `5c1137fa`  
SOURCE: IMP-027, IMP-028, IMP-029  
TARGET: Gitbook  
SCOPE: docs only  
DELIVERABLE: PR  
ACCEPTANCE TEST: backlog Status column shows DONE; agent-checkins Active no longer lists HYB-012  
OVERLAP CHECK: **duplicates LEDGER IMP-027/028/029** — prefer executing those IMP rows rather than a parallel card; included here as eval-gate dependency  
STATUS: PROPOSED  

### CARD-EVAL-011 — Remove 8 non-quantum duplicate routes
IDENTITY: Tessera Admin coordinator  
AGENT: TESSERA  
TASK: Execute IMP-001–008 (remove shadowed legacy/universe dupes); keep quantum until CARD-EVAL-007  
SOURCE: LEDGER IMP-001–008  
TARGET: TESSERA  
SCOPE: routes + allow-list shrink  
DELIVERABLE: PR  
ACCEPTANCE TEST: duplicate allow-list length **10 → 2** (quantum only); CI green  
OVERLAP CHECK: **is** LEDGER IMP-001–008 / IMP-021  
STATUS: PROPOSED  

### CARD-EVAL-012 — Response-shape probes for remaining dups
IDENTITY: Tessera Admin coordinator  
AGENT: Build / TESSERA  
TASK: IMP-009 style probes for non-quantum dups before/while removing  
SOURCE: LEDGER IMP-009, IMP-046, IMP-047  
TARGET: route-inventory tests  
ACCEPTANCE TEST: each removed route has HTTP contract test first  
OVERLAP CHECK: LEDGER  
STATUS: PROPOSED  

### CARD-EVAL-013 — Boot side-effect hygiene
IDENTITY: Tessera Admin coordinator  
AGENT: TESSERA  
TASK: IMP-017/018/025 — stop import-time autonomous/wallet/scraper starts; require explicit boot  
SOURCE: LEDGER  
TARGET: `legacy-engines.ts`, `routes/index.ts`, tests  
ACCEPTANCE TEST: importing routes in vitest does not start timers (assertion/mock)  
OVERLAP CHECK: LEDGER IMP-017/018/025  
STATUS: PROPOSED  

### CARD-EVAL-014 — Assert registration count in CI
IDENTITY: Tessera Admin coordinator  
AGENT: Build  
TASK: Log or assert Express registration total so "~925" becomes TESTED or is corrected  
SOURCE: Build gate C3  
TARGET: `route-inventory.test.ts`  
ACCEPTANCE TEST: CI log prints `registrations=<n>` OR test `expect(n).toBe(...)` with documented n  
OVERLAP CHECK: none  
STATUS: PROPOSED  

### CARD-EVAL-015 — SUMMARY link for Cortical readiness
IDENTITY: Tessera Admin coordinator  
AGENT: Gitbook Cordnation  
TASK: IMP-026 — add SUMMARY entry for `intake/CORTICAL-LABS-READINESS.md`  
SOURCE: BASELINE orphan list  
ACCEPTANCE TEST: notable orphan removed; SUMMARY links still 0 broken  
OVERLAP CHECK: LEDGER IMP-026  
STATUS: PROPOSED  

### CARD-EVAL-016 — Historical merge gate (HYB-014)
IDENTITY: Tessera Admin coordinator  
AGENT: Test steward / Build  
TASK: HYB-014 — CI/local command reporting duplicate roots, stale refs, secret-shaped paths, typecheck/tests/build/audit  
SOURCE: backlog HYB-014 READY  
TARGET: TESSERA scripts (not workflow file edits without Father yes)  
ACCEPTANCE TEST: `pnpm run merge-gate` (name TBD) exits nonzero on planted fixture failure  
OVERLAP CHECK: HYB-014; not in IMP seed  
STATUS: PROPOSED  

### CARD-EVAL-017 — Selffix phase-0 docs into Gitbook board
IDENTITY: Tessera Admin coordinator  
AGENT: Tessera Admin  
TASK: IMP-031–034 — add HYB-SELFFIX row + flow/role/skill updates pointing at `/workspace/hyb-selffix/` design  
SOURCE: Father phase-0 approval ~5:28 PM CT  
ACCEPTANCE TEST: backlog lists SELFFIX; flow.md mentions dry-run poll  
OVERLAP CHECK: LEDGER IMP-031–034  
STATUS: PROPOSED  

### CARD-EVAL-018 — Competitor score card page (docs only)
IDENTITY: Tessera Admin coordinator  
AGENT: Grok Bot / Tessera Pen  
TASK: Publish Gitbook page summarizing BENCHMARK-PLAN competitor citations (URLs+dates) and explicit "Tessera has no industry score yet"  
SOURCE: this full-picture pack  
TARGET: Gitbook `review/` or `intake/`  
ACCEPTANCE TEST: page linked from SUMMARY; every score has URL+date; no invented Tessera numbers  
OVERLAP CHECK: none  
STATUS: PROPOSED  

### CARD-EVAL-019 — Origin engine access check
IDENTITY: Tessera Admin coordinator  
AGENT: Mesh Cloud / Father  
TASK: Restore or document Origin connector so `collin-keane/Tessera` can be inventoried  
SOURCE: BLOCKED Origin namespaces=[]  
ACCEPTANCE TEST: `list_namespaces` nonempty OR written decision that Origin is out of mesh for now  
BLOCKERS: **Father yes** — reconnect Origin / grant namespace?  
STATUS: PROPOSED  

### CARD-EVAL-020 — Privacy recheck remaining archives (HYB-011)
IDENTITY: Tessera Admin coordinator  
AGENT: Security / Privacy steward  
TASK: HYB-011 secret/private-record sweep on remaining repos **without opening 1T**  
SOURCE: backlog  
ACCEPTANCE TEST: dated exclusion manifest updated  
OVERLAP CHECK: HYB-011  
STATUS: PROPOSED  

---

## Priority order (most valuable first)

1. CARD-EVAL-001 harness  
2. CARD-EVAL-009 stop false MMLU labeling  
3. CARD-EVAL-008 Gitbook RAG + quiz metric  
4. CARD-EVAL-011/012 duplicate-route cleanup (measurable allow-list 10→2)  
5. CARD-EVAL-004/003 Father key+spend decisions for one real industry number  
6. CARD-EVAL-010 board hygiene for HYB-012  
7. CARD-EVAL-014 registration count TESTED  
8. CARD-EVAL-013 boot hygiene  
9. CARD-EVAL-016 merge-gate  
10. CARD-EVAL-018 competitor card page  
11. CARD-EVAL-002 local Ollama  
12. CARD-EVAL-015/017 docs nav  
13. CARD-EVAL-005/006/007/019 Father product/access questions  
14. CARD-EVAL-020 privacy sweep  

## Explicit non-goals (forbidden)

- Flipping `TESSERA_ENABLE_*`  
- Reading/printing secrets, wallets, payments, blockchain, **1T**  
- Claiming AGI/consciousness/owned weights as TESTED  
- Inventing benchmark scores  
