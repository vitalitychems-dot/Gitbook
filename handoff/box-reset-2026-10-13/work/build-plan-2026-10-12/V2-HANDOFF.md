# V2-HANDOFF — Build brief for Tessera Builder
**For:** Cursor cloud agent on `vitalitychems-dot/TESSERA`  
**From:** Phase-1 planner (2026-10-12 CT)  
**Companion files (read these first):
- `/workspace/build-plan-2026-10-12/REA-COVERAGE-V2.md` — REA % per repo**
- `/workspace/build-plan-2026-10-12/TESSERA-V2-PLAN.md` — full architecture & sources
- `/workspace/build-plan-2026-10-12/V2-FEATURE-MAP.csv` — every inventory repo → include/exclude
- `/workspace/build-plan-2026-10-12/v2-memory.jsonl` — MCP memory graph (entities/relations)
- `/workspace/build-plan-2026-10-12/SECURITY-PROTOCOLS-INVENTORY.md`
- `/workspace/build-plan-2026-10-12/OFFLINE-INTERNET.md`
- REA outputs: `/workspace/rea-batch/v2-rea-out/*.json` and `/workspace/rea-batch/b2-out/*.json`

---

## 1. Goal (one paragraph)

Build **TESSERA v2** inside `vitalitychems-dot/TESSERA`: an MIT (default) all-in-one open-source Tessera where a **lead agent (Tessera)** plans on a visible **studio board**, **worker agents** each get a **desk + git worktree + sandbox**, the app works **offline** on an **encrypted mesh**, adapters call taught sites / sanctioned APIs, and a **knowledge graph + token lab** cut re-reads and tokens. Combine useful ideas from ~315 inventory names; **never** import excluded categories.

---

## 2. Architecture (what to build)

1. **Studio / Foreman (AgentCraft model, clean-room or MIT-attributed)**  
   - Lead = Tessera pen (xAI/Grok now; GLM-5 later when TESTED).  
   - Workers = mesh lanes.  
   - Task graph, decisions, shared memory, **approve-only merge**, **no git push** for agents.  
   - **Web 2D studio required**; optional 3D; Minecraft **not** required.

2. **TESSERA preview + api-server** — keep existing `offline/`, `mesh-node/`, `secure-mesh/`, `tessera/` (memory-web, token-graph, local-learn, shepherd, sovereign-fetch-guard).

3. **GitMesh** (ex-GitbookAI) — git-carried public drops. **Gitbook** — intake/mesh/merge docs.

4. **Adapters** — sanctioned MCP first; optional `goodnight000/api-anything` (MIT) for public no-login sites; cookies import **OFF**.

5. **Compute** — per-desk sandbox, CPU/mem limits, **network denied by default**.

6. **Knowledge graph** — MCP memory JSONL shape; agents query entities/relations/observations instead of whole-file re-reads. Flowsint (Apache-2.0) = **UX reference only**; no people-OSINT.

7. **Token lab** — baseline meter; A/B: graph retrieval, summary cache, diff-only context, small-model routing, prompt compression, memoized tool results.

---

## 3. Ordered PR list (implement in order; each must pass local tests before merge)

### A — Foundations
| ID | Work | Acceptance test |
|---|---|---|
| V2-001 | HYB-011 denylist (routes/files) | Fixture requests to wallet/payment/vault/1T patterns → refused |
| V2-002 | MIT LICENSE + NOTICE | Files exist; package.json license MIT |
| V2-003 | Vendor plan snapshot under `docs/v2/` (feature map summary + memory pointer) | JSONL schema parse test |
| V2-004 | REA coverage markdown from v2-rea-out/*.cov | Table rendered in docs |

### B — Agents studio
| ID | Work | Acceptance |
|---|---|---|
| V2-010 | TaskGraph + DecisionQueue (sim) | Unit: dependency gating + decision blocks worker |
| V2-011 | git worktree per task | create/cleanup; `git push` fails in worktree hooks |
| V2-012 | Merge gate | merge only after approve; dirty main refuses |
| V2-013 | WS protocol schemas | schema check script green |
| V2-014 | Web 2D Task Wall + desks | Playwright: post goal → cards |
| V2-015 | Optional 3D flag (default off) | build passes with flag off |
| V2-016 | Lead planner adapter (sim + pen hook) | sim run completes 2-task goal |
| V2-017 | Worker log → monitor stream | fake worker events visible in API |

### C — Offline mesh
| ID | Work | Acceptance |
|---|---|---|
| V2-020 | O1 file-mesh index ≥50 | query returns Gitbook-derived hit `live:false` |
| V2-021 | O2 offlineQueue | fake-indexeddb replay once |
| V2-022 | O3 SW shell | sw.js emitted; offline navigation shell |
| V2-023 | O7 badge | component test |
| V2-024 | O10 mesh-node | existing unit tests + e2e join/leave log |
| V2-025 | O11 secure-mesh | encrypt/decrypt + bad sig reject |
| V2-026 | O5 sneakernet script | bundle round-trip sha |
| V2-027 | O6 LAN P2P | unit config |
| V2-028 | O4 Kiwix optional | mock HTTP; default off |
| V2-029 | O8 Gitbook page | (docs PR on Gitbook if needed) |
| V2-030 | O9 LoRa note | doc only |

### D — Knowledge + Flowsint-inspired UI
| ID | Work | Acceptance |
|---|---|---|
| V2-040 | Unify KG store | `open_nodes`-style query API |
| V2-041 | MCP memory config | server read_graph non-empty |
| V2-042 | Library graph panel | renders task/doc nodes; **no** external OSINT enrichers |
| V2-043 | Own-repo metadata enricher | only `vitalitychems-dot/*` |

### E — Compute + token lab
| ID | Work | Acceptance |
|---|---|---|
| V2-050 | Desk sandbox | network denied; mem limit enforced in test harness |
| V2-051 | Token baseline meter | metrics JSON after fixture task |
| V2-052 | A/B graph retrieval | both arms recorded |
| V2-053 | Summary cache + diff-only | token count decreases on cache hit |
| V2-054 | Small-model routing + compression | router unit test |
| V2-055 | Proposal queue for new methods | schema validation; no auto-enable |

### F — Adapters + UI
| ID | Work | Acceptance |
|---|---|---|
| V2-060 | api-anything allowlist adapter | HN fixture; login/cookies disabled |
| V2-061 | Chamber/Board + duplicate-guard | UI + guard tests |
| V2-062 | GitMesh string cleanup | no user-facing "GitbookAI" |

**Do not open PRs that combine studio + mesh + token lab in one shot.** One ID per PR.

---

## 4. Hard limits (stop and ask Father if tempted)

- **No** wallets, payments, trading/MEV/DeFi bots, mining, NFT, captcha solvers, Cloudflare/bot-detection bypass, antidetect/stealth browsers, hashcat/cracking, browser fingerprinting libs.  
- **No** `1T` or `vault` paths (read, copy, or import).  
- **No** deleting repos or archive folders.  
- **No** git history rewrites.  
- **No** flipping `TESSERA_ENABLE*` (or equivalent) feature flags.  
- **No** executing code from cloned third-party/archive apps — read/REA/port patterns only.  
- **No** people-OSINT (Flowsint enrichers against persons).  
- **No** OpenAI as default pen (GB-052).  
- **No** deploying archived XXX income/arbitrage/wallet routes.  
- Vitality store stays out of the combine.

---

## 5. Commit identity & CI

- Author/committer: **vitalitychems-dot** GitHub noreply (`vitalitychems-dot@users.noreply.github.com` or the account’s configured noreply).  
- **CI is blocked by billing** → green **local** `pnpm test` / package tests are the merge proof. Paste test output in the PR body.  
- Prefer small commits; PR title `V2-0xx: …`.  
- Do not force-push main; do not use `--no-verify` unless Father says so.

---

## 6. How to load the full picture (mandatory before coding)

```bash
export PATH=/workspace/tools/node22/bin:$PATH
export MEMORY_FILE_PATH=/workspace/build-plan-2026-10-12/v2-memory.jsonl
# MCP: npx -y @modelcontextprotocol/server-memory
# Then read_graph / search_nodes for TESSERA_v2, module_*, decision_*, risk_*
```

Also open:
- Feature map CSV (include/exclude reasons).  
- Latest `v2-rea-out/*.cov` coverage lines.  
- Gitbook `merge/HYB-011-EXCLUSION-MANIFEST.md` and `merge/CONSOLIDATION-MAP-2026-10-12.md` (from clone).

---

## 7. REA coverage expectations

Re-run or read:

| Repo / tree | Role | Notes |
|---|---|---|
| TESSERA | base | Expect ~95%+ JS parse |
| Gitbook novault stage | docs+archives | 1T/vault excluded; Zz imports/trees included in tree |
| GitMesh | mesh drops | small |
| vitality | **risk flags only** | do not merge store into Tessera |
| Zz / XXX / olive / T44 | capability mine | exclude wallet routes when porting |

After any new REA, append entities `rea::<name>` into `v2-memory.jsonl` (or regenerate via planner script) so the next agent sees coverage %.

---

## 8. Definition of done for “v2 MVP”

- Studio sim backend: goal → ≥2 tasks → worktrees → tests → approve merge.  
- Offline: index ≥50 pages, queue replay, SW shell, mesh encrypt unit green.  
- KG queryable via MCP memory.  
- Token baseline meter writing metrics.  
- HYB-011 denylist TESTED.  
- No excluded-category code paths introduced.

---

## 9. Father cadence

Auto-continue within limits; every **100 actions** produce a numbered list of what shipped. Father says **yes** (keep all) or lists IDs to undo.

---

## 10. Quick commands

```bash
export PATH=/workspace/tools/node22/bin:$PATH
cd /path/to/TESSERA
pnpm test   # or package-scoped tests — local proof
# REA one tree:
npx -y rea-agents@6.4.0 analyze-javascript-application <dir> --json
```
