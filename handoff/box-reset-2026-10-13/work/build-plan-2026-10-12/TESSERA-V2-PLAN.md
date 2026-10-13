# TESSERA v2 — Full Build Plan
**Date:** 2026-10-12 ~5:35 PM CT  
**Owner:** Father (vitalitychems-dot)  
**Status:** Phase 1 plan complete — no application PRs from this document until Builder runs V2-HANDOFF.md  
**Memory graph:** `/workspace/build-plan-2026-10-12/v2-memory.jsonl` (MCP `@modelcontextprotocol/server-memory`, LOAD_OK)  
**Feature map:** `/workspace/build-plan-2026-10-12/V2-FEATURE-MAP.csv`

---

## 1. Goal

Ship **TESSERA v2**: one all-in-one **MIT** (unless a reused piece forces otherwise) open-source system that:

1. Keeps and improves current `vitalitychems-dot/TESSERA` as the code home.
2. Absorbs **useful capabilities** from every inventory name in `REPO-INVENTORY.csv` (~315), via permissive-license reuse or **clean-room** rebuilds.
3. Makes the **AgentCraft model** the place agents live and build (lead Tessera + worker desks + git worktrees + visible studio — **web 2D/3D**, Minecraft optional).
4. Ships **offline encrypted mesh** (O1–O11), **docs via Gitbook/GitMesh**, **adapters** (api-anything + sanctioned APIs), **compute sandboxes**, and a **token-efficiency lab**.
5. Uses **REA** + **MCP memory** so builders see the full picture without re-reading trees.

---

## 2. Research: api-anything, AgentCraft, Flowsint

### 2.1 goodnight000/api-anything — MIT (~796★)
- **What:** Local website→operation recorder/replayer. Headless Chromium learns a request from two examples; replays via Node `fetch` (tier 1) or in-browser; MCP tools `list_sites`, `list_operations`, `call_operation`, `login`.
- **Fit:** Adapter module for **public, no-login, no-official-API** reads after Security review.
- **Not:** A gateway that replaces GitHub/Gmail/Gitbook connectors. Cookie import from signed-in profiles is a credential risk — default **off**.

### 2.2 blendi-remade/agentcraft — MIT (~723★)
- **What:** Foreman (Node/TS): lead plans → task graph → workers in **git worktrees**; merges only on human approve; no git network for agents. Fabric mod draws a Minecraft studio (desks, Task Wall, monitors).
- **Fit:** **Home of TESSERA v2 agents.** Clean-room (or attributed) reuse of: TaskGraph, DecisionQueue, worktree isolation, merge gate, shared memory library, CI-after-task loop.
- **Non-Minecraft path (required):** Web studio (2D board + optional Three.js/React-Three-Fiber 3D floor) talking the same Foreman WebSocket protocol. Minecraft remains optional for people who own it.
- **Backends:** Claude/Codex in upstream; v2 must plug **Tessera pen** (xAI/Grok until GLM-5 TESTED) — no OpenAI default (GB-052).

### 2.3 reconurge/flowsint — Apache-2.0 (~9.6k★)
- **What:** Local OSINT **entity/relation graph** with enrichers (DNS, WHOIS, etc.).
- **Fit:** **Design reference only** for knowledge-graph UX and enricher-style pivots over **our own** public repo metadata / docs.
- **Hard rule:** Do **not** run people-OSINT. No enrichers aimed at persons.

### 2.4 @modelcontextprotocol/server-memory
- JSONL knowledge graph: `{type:entity|relation,...}`. File: `v2-memory.jsonl`. **Verified LOAD_OK** via stdio MCP `read_graph` (182 entities, 265 relations at first write; regenerates after REA).

### 2.5 morluto/rea-agents@6.4.0
- Static `analyze-javascript-application` on Father-owned trees only. Coverage = `parsed_javascript_files / relevant_files`.

---

## 3. Inventory counts (V2-FEATURE-MAP.csv)

| Metric | Count |
|---|---:|
| Rows (inventory + external tools) | 318 |
| Accessible to vitalitychems-dot token | 9 |
| Public GitHub match found (name exact) | ~129 |
| License UNKNOWN (no public match) | ~180 |
| **include=y** (permissive + in-scope) | ~45 |
| **include=n** (idea-only / clean-room) | ~224 |
| **excluded** (policy) | ~48 |

**Accessible repos:** TESSERA, Gitbook, GitMesh (GitbookAI), vitality, collink1007/{z,XXX,amber-flame-tiger-sand,fleet-moss-monarch-rapid}, thetesseractai/18.

**Excluded categories (always):** captcha solving; Cloudflare/bot-detection bypass; antidetect/stealth; hashcat/cracking; MEV/DeFi/trading bots; wallets; payments; mining; NFT; vitality store; 1T/vault; browser fingerprinting libraries.

**License rule:** Code reuse only under MIT / Apache-2.0 / BSD / ISC / MPL / similar. Else **idea-only, clean-room**.

---

## 4. Architecture

```
Web Studio (2D / optional 3D)
  Task Wall · Desks · Monitors · Merge UI
        | WebSocket (localhost)
Foreman / Tessera Lead
  TaskGraph · Decisions · Memory · Merge
   |              |              |
Worker sandboxes  Knowledge     Token lab
(compute limits,  graph MCP     baseline + A/B
 no net default)  memory
   \              /
    TESSERA preview + api-server
      offline/ · mesh-node/ · secure-mesh/ · tessera/
      adapters (api-anything + sanctioned MCP)
           |                    |
    GitMesh (git drops)   Gitbook (intake/mesh/merge)
```

### Modules

| Module | Lands in | Sources |
|---|---|---|
| **Agents studio** | `preview` + new `studio/` / `foreman/` | AgentCraft MIT patterns; mesh roles; THREE-WAY-COLLAB |
| **Adapters** | `artifacts/api-server` + MCP | api-anything; httpie/SDK public matches; existing Gmail/GitHub connectors |
| **Offline mesh O1–O11** | `preview/src/lib/{offline,mesh-node,secure-mesh,tessera}` | OFFLINE-INTERNET.md; mesh/offline-internet.md; mesh/secure-mesh.md; XXX lattice (MIT) |
| **Docs / GitMesh** | Gitbook + GitMesh repos | consolidation map; intake log; HANDOFF |
| **Compute sandbox** | per-desk workers | AgentCraft worktrees; quarantine design doc |
| **Knowledge graph** | MCP memory + `memory-web`/`token-graph` reuse | CODEBASE-MEMORY-MCP; Flowsint UX ref; provenance-memory |
| **Token lab** | `preview` + scripts | token-graph.ts; GB-050 mesh-speed; PERF-001 |
| **Security / shepherd** | api-server lib | SECURITY-PROTOCOLS-INVENTORY; HYB-011 |
| **UI Chamber/Board** | artifacts/tessera + preview | olive archives; duplicate-guard |
| **Exclusion HYB-011** | manifests + route denylist | HYB-011-EXCLUSION-MANIFEST |

---

## 5. Gaps vs current TESSERA

| Gap | Today | v2 target |
|---|---|---|
| Agent studio home | Roles/pages; no Foreman/worktrees UI | Lead+workers desks, board, merge gate |
| Offline depth | file-mesh stub (3 pages); O2/O3 branches local | Full index, SW shell, queue, LAN P2P |
| Mesh E2E crypto | Product ciphers (sacred/colonial) — not peer mesh | AES-256-GCM + Ed25519 peer payloads (o11) |
| IP-less live data | LAN multicast + HTTP URLs | Topic hashes + pluggable transports; honest WAN gateway separate |
| Shared KG | memory-web / catalog-pass / ask-memory fragments | Unified MCP-memory-compatible graph agents query |
| Token efficiency | token-graph core string; PERF-001 | Meter + A/B lab |
| Compute isolation | quarantine **design** doc | Real sandboxes per desk |
| Adapters | Sanctioned MCP only | + taught public-site ops (guarded) |
| Archive absorption | Many HYB packets; duplicates remain | Capability extract → modules; no wholesale XXX copy |

---

## 6. REA coverage (accessible inputs)

Rerun suite: `/workspace/rea-batch/v2-rea-out/` (1T/vault excluded from Gitbook stage).  
Prior batch: `/workspace/rea-batch/b2-out/`.

| Target | Prior parsed/relevant | Prior % | v2-rea (this phase) |
|---|---|---:|---|
| Gitbook (novault stage) | 952/1094 | 87.0% | **1006/1186 (84.8%)** |
| TESSERA | 1341/1405 | 95.4% | **1367/1431 (95.5%)** |
| GitMesh (GitbookAI) | 7/9 | 77.8% | **7/9 (77.8%)** |
| vitality (risk flags) | 692/716 | 96.6% | **692/716 (96.6%)** |
| Zz (incl. imports/trees) | 115/137 | 83.9% | **115/137 (83.9%)** |
| amber-flame | cancelled | 0% | **147/178 (82.6%)** |
| XXX (archive) | 786/878 | 89.5% | prior OK |
| olive | 48/65 | 73.8% | prior OK |
| T44 | 52/52 | 100% | prior OK |
| TheTesseractAI_18 | 1605/2668 | 60.2% | prior (heap limits) |
| amber-flame | ERROR cancelled | 0% | queued retry |

**Note:** `<100%` is usually non-JS “relevant” assets or heap truncation (`status: partial`), not silent skip. 1T/vault never opened. Coverage % refreshed into `v2-memory.jsonl` when the suite finishes.

---

## 7. Top 15 capabilities to bring in

1. **Lead + worker agent studio** (AgentCraft model, web view)  
2. **Git worktree isolation + human merge gate**  
3. **Offline file-mesh index** (O1 — real Gitbook/GitMesh pages)  
4. **Offline queue + apiCache** (O2)  
5. **Service worker app shell** (O3)  
6. **Encrypted mesh sync** (O10/O11 — Ed25519 + AES-GCM)  
7. **On-demand agent mesh toggle** (need-based; owner allow once)  
8. **Knowledge graph memory** (MCP memory format; Flowsint-inspired UX)  
9. **Sandbox compute per desk**  
10. **Token lab** (graph retrieval, summary cache, diff-only context, small-model routing, compression, memoized tools + A/B)  
11. **api-anything adapters** (public read sites only)  
12. **Shepherd egress allowlist + audit** (keep/extend)  
13. **Chamber/Board UI** from olive (with duplicate-guard)  
14. **Kiwix optional + USB sneakernet + LAN P2P** (O4–O6)  
15. **HYB-011 exclusion enforcement** in router + CI grep  

---

## 8. Phased PR list (~32 small, testable)

Each PR: local tests = proof (CI billing blocked). Commit as `vitalitychems-dot` noreply.

### Phase A — Foundations & exclusions
| ID | PR | Acceptance |
|---|---|---|
| V2-001 | HYB-011 route/file denylist + unit tests | Grep/fixture: wallet/payment/vault/1T paths refused |
| V2-002 | LICENSE MIT clarify + NOTICE for attributions | `LICENSE` present; package.json `MIT` |
| V2-003 | Wire `v2-memory` snapshot into `docs/v2/` | File present; schema test parses JSONL |
| V2-004 | REA coverage report page (Gitbook) | Table of repo → %; links to artifacts |

### Phase B — Agents studio (AgentCraft home)
| ID | PR | Acceptance |
|---|---|---|
| V2-010 | Foreman stub: TaskGraph + DecisionQueue (no LLM) | Unit: deps block start; decide→resume |
| V2-011 | Worktree runner (git worktree per task) | Test: create/remove worktree; no push capability |
| V2-012 | Merge gate (approve-only) | Test: merge refused without approve; refused dirty main |
| V2-013 | WebSocket protocol schemas (docs/protocol) | `npm run check` schemas |
| V2-014 | Web 2D studio: Task Wall + desk list + status lamps | Playwright: goal→task cards appear |
| V2-015 | Optional 3D floor (feature flag off) | Builds; flag off = 2D only |
| V2-016 | Tessera lead planner adapter (pen) | Sim backend TESTED without paid Minecraft |
| V2-017 | Worker agent adapter + log stream to monitor | Test: fake worker emits tool events |

### Phase C — Offline mesh (O1–O11)
| ID | PR | Acceptance |
|---|---|---|
| V2-020 | O1 file-mesh index ≥50 pages | Unit query hits real page `live:false` |
| V2-021 | O2 offlineQueue + apiCache (no knowledgeVault) | fake-indexeddb: replay once, no dupes |
| V2-022 | O3 service worker shell | `sw.js` emitted; offline shell loads |
| V2-023 | O7 real online badge | Component test navigator.onLine + queue length |
| V2-024 | O10 mesh-node opt-in + agent join/leave log | Tests already local — merge + e2e |
| V2-025 | O11 secure-mesh encrypt/sign | Unit: encrypt→decrypt; reject bad sig |
| V2-026 | O5 sneakernet git bundle script + Gitbook page | Bundle→clone sha match |
| V2-027 | O6 LAN P2P config | Unit empty ICE; localhost two-tab doc |
| V2-028 | O4 Kiwix hook (default off) | Mock kiwix HTTP |
| V2-029 | O8 Offline Internet Gitbook page | SUMMARY link |
| V2-030 | O9 LoRa research note only | Doc only |

### Phase D — Knowledge graph + Flowsint-inspired UX
| ID | PR | Acceptance |
|---|---|---|
| V2-040 | Unify memory-web/token-graph/ask-memory → KG store | Query by entity name returns observations |
| V2-041 | MCP memory server config in Tessera | `read_graph` returns entities |
| V2-042 | Studio “library” panel (Flowsint-like graph view of tasks/docs) | Renders nodes from KG; no external enrichers |
| V2-043 | Repo-metadata enricher (own repos only) | Fetches gh meta for vitalitychems-dot/* only |

### Phase E — Compute + token lab
| ID | PR | Acceptance |
|---|---|---|
| V2-050 | Desk sandbox (bubblewrap/docker/node worker) | Resource limits; network denied by default |
| V2-051 | Token baseline meter (tokens/task, success) | Fixture run writes metrics JSON |
| V2-052 | Method: graph retrieval vs full-file | A/B ≥1 task; both rates recorded |
| V2-053 | Method: summary cache + diff-only context | Cache hit reduces tokens in test |
| V2-054 | Method: small-model routing + prompt compression | Router picks small model for classify fixture |
| V2-055 | Agents propose methods → queued A/B | Proposal schema validated; no auto-prod |

### Phase F — Adapters + UI
| ID | PR | Acceptance |
|---|---|---|
| V2-060 | api-anything optional adapter (allowlist sites) | Call HN search fixture; cookies import disabled |
| V2-061 | Port olive Chamber/Board + duplicate-guard | UI test + guard test |
| V2-062 | GitMesh rename residual strings | No GitbookAI user-facing left |

---

## 9. License approach

- **Default:** MIT for TESSERA v2.  
- **Reuse:** only permissive SPDX; keep `NOTICE` / file headers.  
- **AgentCraft / api-anything / Flowsint / Tink / etc.:** prefer clean-room of patterns; if copying MIT/Apache files, attribute.  
- **NONE/UNKNOWN/proprietary:** idea-only.  
- **Minecraft assets:** never vendored; optional user-owned client.

---

## 10. Hard limits (non-negotiable)

- No wallets, payments, trading/MEV, mining, NFT, captcha/CF-bypass, antidetect, cracking.  
- No 1T / vault path opens or imports.  
- No repo deletes; no history rewrites without Father explicit ask.  
- No `TESSERA_ENABLE*` flag flips.  
- No executing cloned third-party app code.  
- No people-OSINT.  
- Agents never auto-push; merge gate stays.  
- CI billing blocked → **local tests are the proof**.

---

## 11. Sources appendix (input → v2 module)

| Input | → Module |
|---|---|
| REPO-INVENTORY.csv / V2-FEATURE-MAP.csv | all (routing) |
| REA-RUN-LOG + b2-out + v2-rea-out | exclusions, adapters, UI extract list |
| OFFLINE-INTERNET.md + mesh/offline-internet.md | offline mesh |
| mesh/secure-mesh.md + SECURITY-PROTOCOLS-INVENTORY | secure mesh / shepherd |
| mesh/CODEBASE-MEMORY-MCP.md + provenance-memory | knowledge graph |
| mesh/HANDOFF.md + roles/* + THREE-WAY-COLLAB | agents studio lanes |
| merge/CONSOLIDATION-MAP + FUNCTIONAL-MERGE-MATRIX + ALL-REPOSITORIES-ROUTING | docs + absorption order |
| merge/HYB-011-EXCLUSION-MANIFEST | exclusion module |
| intake/log.md + HYBRID-CONSOLIDATION-BACKLOG | docs cadence |
| brain-consciousness/TESSERA-V2-ROADMAP + OWN-BRAIN-* | agents/brain (pen rules) |
| history/handoffs/* | archive context (idea) |
| review/lora-meshtastic-research.md | O9 |
| NESTED-REPO-MAP + archive/moved/* (no 1T) | capability mine via REA |
| goodnight000/api-anything | adapters |
| blendi-remade/agentcraft | agents studio |
| reconurge/flowsint | knowledge graph UX (reference) |
| live `preview/src/lib/{offline,mesh-node,secure-mesh,tessera}` | offline + token + memory |
| vitality repo REA | risk flags only — not combined |

---

## 12. Operating cadence

Father rule: auto-build/merge within hard limits; **list every 100 actions**; reply yes or pick undos. Studio agents may toggle mesh when needed if owner allowed once.
