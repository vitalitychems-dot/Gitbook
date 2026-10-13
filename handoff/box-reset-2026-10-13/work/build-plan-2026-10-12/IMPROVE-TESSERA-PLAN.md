# Improve Tessera plan — top 20 candidates (from log repo names)

**As-of:** 2026-10-12 ~3:53 PM CT. Father yes. Local draft only — no GitHub writes.  
**Inputs:** `REPO-NAMES-FROM-LOGS.md` (271 clean names), nested archives in TESSERA/Gitbook, `/workspace/evals/BASELINE-LOCAL.md`.  
**Tools:** ordinary code analysis first. REA / api-anything = optional notes only (see `TOOLS-*.md`). Claude-Red = not used.

## How we prove improvement

Every candidate below has a **before/after metric**. Prefer metrics already measured in BASELINE-LOCAL.md or existing TESSERA unit tests (`preview/src/lib/tessera/*`). Labels: **TESTED** = already measured; **PROPOSED** = metric designed, not yet run.

### Baseline anchors (TESTED, 2026-10-05 CT)

| Metric | Baseline | Source |
|---|---|---|
| ARC-Challenge (n=50, qwen2.5:3b local) | **0.70** | `/workspace/evals/BASELINE-LOCAL.md` §2 |
| GSM8K (n=25) | **0.32** | same |
| HumanEval pass@1 (n=15) | **0.20** | same |
| Gitbook quiz alone | **0.28** (7/25) | §3 |
| Gitbook quiz + BM25 top-3 | **0.72** (18/25) | §3 |
| TESSERA unit tests (last green report) | **121** passing (earlier CC note); GitHub Actions runs blocked since ~Oct 10 by billing | parent chat / Build |
| `measureGains` recall quiz | final score **12** (strict rise after matcher change) | `preview/src/lib/tessera/improve-measure.test.ts` |

**Rule:** do not publish local 3B subset scores as Tessera AGI leaderboard numbers. Tessera is a TypeScript mesh; local Ollama is a free smoke harness.

### Out of scope (from catalog + standing rules)

- **held** (17 trading/chain repos) — not imported into Tessera mind.
- **vitality** store names — stay in `vitalitychems-dot/vitality`.
- **1T** — name only; never open.
- **Claude-Red / attack packs** — refuse.
- Bulk-merge of archives — selective behavior recovery only (HYB routing).

---

## Top 20 candidates

| # | Improvement | Source names / archive paths | Target in TESSERA | Before metric | After target | Gate |
|---:|---|---|---|---|---|---|
| 1 | **Ship Gitbook BM25 (or equivalent) into product ask path** — today RAG is harness-only | patterns from `infiniflow/ragflow`, `Mintplex-Labs/anything-llm`, `mksglu/context-mode` (README ideas only); corpus already in Gitbook | `preview/src/lib/tessera/ask-memory.ts` + `ask-all.ts` + new retrieval module under `preview/src/lib/tessera/` | Gitbook quiz alone **0.28** (BASELINE) | Same 25Q + retrieval ≥ **0.72** on product path (match harness); unit tests for top-k citation | Security → Build → bulk yes |
| 2 | **Restore / harden chamber picture route** (PR146 fallout already partially fixed) | own code; `ask-all.ts` history | `ask-all.ts` + `ask-all.test.ts` | `askAll("what files")` must match chamber files string (test exists) | Test green; no hard-coded tesseraVote | Build fix (standing) |
| 3 | **Creator-profile matcher** — decisions from Father digests → preference checks | Father protocol pages; `mesh/FATHER-ASKS.md`; learning memory lane | new `creator-profile.ts` + tests; wire into `named-task` / propose-before-ask | 0 automated preference checks | ≥10 dated rules; propose-task dry-run test passes 100% on fixture digests | Security (PII scrub) → Build |
| 4 | **Memory-web → school recall lift** | `memory-web.ts`, `improve-measure.ts`, `data/school/recall-index.jsonl`; ideas from `cognitivecomputations/agi-memory` (card only) | `memory-web.ts`, `recall-all.ts`, school cycle | `measureGains` final score **12** | Score ≥ **14** on same fixture rows without weakening grader | Build |
| 5 | **Re-enable CI + freeze green count** | TESSERA `.github` workflow; Actions billing | CI green on main | Actions fail in ~3s (billing) — BLOCKED | After Father clears GitHub billing: `pnpm test` ≥ prior green count; record in Gitbook | Father billing + Build |
| 6 | **Agent task-graph (AgentCraft ideas, no Minecraft)** | `mvschwarz/openrig`, `obra/superpowers`, `Calamari/BehaviorTree.js` (cards/READMEs); AgentCraft design borrow only | `agent-cycle.ts`, `named-task.ts`, mesh board sync | Claims without acceptance tests (COLLAB metrics) | Claim clarity **100%** on new tasks; each task stores acceptance test string | Cordnation + Build |
| 7 | **Skill drill from tool READMEs (install none)** | 8 tool homes: `Agent-Reach`, `caveman`, `superpowers`, `context-mode`, `codegraph`, `OpenShell`, `hyperframes`, `openrig` | `agent-skills.ts`, `skill-drill.test.ts`, Gitbook notes | 0 structured skill notes from those 8 | 8 notes + 8 unit assertions (“refuses install script”) | Security (no install) → Build |
| 8 | **Codegraph-style symbol map for `preview/src/lib/tessera`** | `colbymchenry/codegraph` (idea); own tree | generate `docs/TESSERA-SYMBOL-MAP.md` via ordinary ripgrep/ast; optional later REA on built bundle only | No symbol map | Map covers ≥90% of exported symbols in `lib/tessera/*.ts` (count test) | Build (docs PR to Gitbook or TESSERA docs/) |
| 9 | **Brain-volume / brain-mesh fidelity from open SNN cards** | `BindsNET/bindsnet`, `brian-team/brian2`, `Brain-Cog-Lab/Brain-Cog`, `Cortical-Labs/cl-sdk` (cards / pattern notes only — no weight claims) | `brain-volume.ts`, `brain-train.ts`, `brain-view.tsx` | Phase-1 own-brain report exists; no measurable region link score | Region-link scoreboard: ≥N regions with testable weight update rule; tests in `brain-*.test.ts` | Brain lane + Security (no false AGI claims) |
| 10 | **Local Ollama loop wired to `local-learn.ts`** | BASELINE harness; `local-learn.ts` | `local-learn.ts` + eval harness bridge | Harness scores exist; product path not wired | One command reproduces ARC n=50 within ±0.02 of **0.70** from product wrapper | Build |
| 11 | **GSM8K smoke expansion** | BASELINE §2 | `/workspace/evals/harness` + record in Gitbook research | n=25 → **0.32** | Re-run n=50 (same seed family); publish only as local smoke | Build / research |
| 12 | **HumanEval smoke expansion** | BASELINE §2 | eval harness | n=15 → **0.20** | n=30 pass@1 recorded; no spend | Build / research |
| 13 | **Selective Z10 / own-lab UI flow (HYB-013)** | archives: `Zz` / olive workshop notes; HYB-007 verdicts | one route under `preview/src/components/tessera/` + tests | Flow missing / partial | 1 user-valued flow + ≥3 tests; rollback commit named | Product call → Security → Build |
| 14 | **Repo-ask over nested archive names** | this name list + `repo-ask.ts` | `repo-ask.ts` answers “what archives do we have?” from allowlisted paths | Ad-hoc answers | Deterministic answer lists ≥20 nested basenames from `NESTED-REPO-MAP.md` | Build |
| 15 | **Exclusion manifest refresh (HYB-011)** | catalog missing/legacy; `merge/HYB-011-EXCLUSION-MANIFEST.md` | Gitbook merge page (docs) | Manifest stale vs 4-repo account | Manifest lists gone repos + 1T name-only; HAC draft already staged | Privacy → Moderator |
| 16 | **Topic pages from HYB verdicts (HYB-015)** | GitbookAI rules (summary), HYB-006/007/008/017 | Gitbook `topics/` (not `mesh/*`) | No topic pack | 6 pages + SUMMARY row; HAC draft staged | Moderator → bulk yes |
| 17 | **Duplicate-guard on archive imports** | `duplicate-guard.test.ts`; redundancy ledger | import PRs must call duplicate check | Historical bulk risk | 0 duplicate blob imports in new PRs (hash test) | Security + Build |
| 18 | **Self-improve loop honesty banner** | `self-improve.ts`, `improve-loop.test.ts`; catalog warning on BUILT cards | ensure improve loop refuses untested claims | False-attribution incidents >0 historically | Unit tests: untested claim → deferred; authenticity incidents target **0** (COLLAB metrics) | Security + Build |
| 19 | **World-stage / chamber search quality** | `world-stage.tsx`, `room-world.ts`, `mesh/CHAMBER-SEARCH-2026-10-10.md` | chamber search ranking | Manual | Fixture of 20 chamber queries ≥80% hit@1 | Build |
| 20 | **Consolidation map + name-list sync page** | Cordnation GB-062 draft; this file | Gitbook `merge/CONSOLIDATION-MAP-…` + pointer to name list | Map staged locally | Page merged after gates; links `REPO-NAMES-FROM-LOGS` summary (no secrets) | Cordnation → Moderator |

---

## Suggested build order (first measurable wins)

1. **#5** unblock CI (Father billing) — otherwise after-metrics are local-only.  
2. **#2** chamber route / vote-line cleanup if still needed on tip.  
3. **#1** product RAG (largest BASELINE delta already proven: +0.44).  
4. **#4** recall gains + **#3** creator profile (Father mirror).  
5. **#7–#8** skills + symbol map (cheap, high clarity).  
6. **#9–#12** brain/eval smokes (honest local only).  
7. **#13–#20** HYB / docs / chamber polish in parallel lanes.

## Optional tools (document only)

| Tool | Use? | Note |
|---|---|---|
| REA | Optional later | Static JS on Father-owned **built** bundles missing source. Not needed for `preview/src` trees. |
| api-anything | Skip | Still calls site endpoints; does not replace GitHub/Gitbook/Gmail APIs. |
| AgentCraft | Skip install | Borrow task-graph ideas; real use needs paid Minecraft + Claude. |
| Claude-Red | **No** | Offensive pack — refuse even for “own” vulnerability testing. Use defensive review instead. |

## Acceptance for this planning pass

- [x] Unique name list written (`REPO-NAMES-FROM-LOGS.md`)
- [x] Top 20 improvements with metrics (`IMPROVE-TESSERA-PLAN.md`)
- [x] Nested map updated with pointer
- [ ] Implementation PRs — **not started** (needs Security → Build → Father bulk yes per item)

