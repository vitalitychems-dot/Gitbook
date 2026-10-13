# HYB-006 — Grok-ready vs current TESSERA behavior comparison

**Task:** HYB-006  
**Author role:** Grok historical-analysis collaborator (executor subagent)  
**Date:** 2026-10-05 (America/Chicago)  
**Grok-ready ref:** `main` @ `9e3fbca` (2026-10-03 CT: “Remove the store code.”)  
**TESSERA ref:** `main` @ `fec56eb` (2026-10-05 CT: workspace lock cleanup after HYB-003)  
**Method:** path/behavior comparison via GitHub tree + key file reads. No installs. No TESSERA code writes. Protected `1T` vault not inspected.  
**Tree summary:** Grok-ready 1293 blobs; TESSERA 1383 blobs; **1275 common**, **18 only in Grok-ready** (mostly `docs/grok-packet/.../isolated-mockup` + migration screenshots), **108 only in TESSERA** (unified suite scripts, CI, archives, validation docs). Of common blobs, **16 content hashes differ** (mostly manifests, lockfile, README, mockup `vite.config.ts`, migration docs)—**not** application route/lib bodies.

## Executive finding

Current TESSERA already carries the reviewed Grok-ready **active application contract** (`artifacts/api-server`, `artifacts/tessera`, `artifacts/mockup-sandbox`, `lib/`). Distinctive Grok-ready behaviors that still matter are either **already present**, **superseded by TESSERA suite/CI hardening**, **intentionally removed** (storefront tree), or **documentation/provenance only**. No wholesale re-import of Grok-ready packages or generated output is justified.

---

## Capability matrix

### C1 — Canonical Tessera workspace (API + web + mockup + shared libs)

| Field | Value |
|---|---|
| Historical source | `vitalitychems-dot/Grok-ready` @ `9e3fbca` — `artifacts/{api-server,tessera,mockup-sandbox}`, `lib/*`, README “What’s inside” |
| Behavior / goal | One pnpm monorepo with Express 5 API, React/Vite Tessera UI, mockup sandbox, shared Drizzle/OpenAPI libs |
| Current TESSERA | **Yes** — same three apps + `lib/` present; README + `docs/PROJECT_MAP.md` document suite launcher |
| Portable | N/A (already present) |
| Target module | `artifacts/*`, `lib/*` |
| Privacy / security / licensing | Low for structure; keep secrets out of commits (both repos document this) |
| Deterministic acceptance test | Path set exists: `artifacts/api-server`, `artifacts/tessera`, `artifacts/mockup-sandbox`, `lib/db`, `lib/api-spec`; `pnpm-workspace.yaml` includes `artifacts/*` and `lib/*` |
| Disposition | **ACCEPTED** (already present; keep newest TESSERA) |

### C2 — Guarded outbound HTTP (`safeFetch` allowlist)

| Field | Value |
|---|---|
| Historical source | Grok-ready `artifacts/api-server/src/lib/safe-fetch.ts` (from `TESS` merge per `docs/CONSOLIDATION.md`); tests `.../__tests__/safe-fetch-policy.test.ts` |
| Behavior / goal | Only credential-free HTTPS GETs to fixed knowledge/NASA hosts; same-host redirect limit; block other hosts/methods/credentials before network |
| Current TESSERA | **Yes** — identical path present; tests present |
| Portable | Already present |
| Target module | `artifacts/api-server/src/lib/safe-fetch.ts` |
| Risks | Mis-expanding allowlist would widen egress; do not port host lists from unreviewed archives |
| Acceptance test | `pnpm --filter @workspace/api-server exec vitest run src/__tests__/safe-fetch-policy.test.ts` (or workspace `pnpm test` when loopback test DB policy allows) |
| Disposition | **ACCEPTED** (already present) |

### C3 — Sovereign fetch guard / secure external wrapper

| Field | Value |
|---|---|
| Historical source | Grok-ready `artifacts/api-server/src/lib/sovereign-fetch-guard.ts`, `secureExternalWrapper.ts` + tests |
| Behavior / goal | Shepherd-context outbound guard; external provider sandboxing for non-allowlisted calls |
| Current TESSERA | **Yes** — active paths + `sovereign-fetch-guard.test.ts`; archive copies under `archives/source-variants/` are historical only |
| Portable | Already present |
| Target module | `artifacts/api-server/src/lib/` |
| Risks | Duplicate archive copies must not become second live implementations (HYB-012) |
| Acceptance test | `sovereign-fetch-guard.test.ts` passes; no second active import path from `archives/` |
| Disposition | **ACCEPTED** (already present); archive copies **RETAINED** as provenance only |

### C4 — Admin session auth gate (HttpOnly cookie, origin check, rate limits)

| Field | Value |
|---|---|
| Historical source | Grok-ready / TESSERA `artifacts/api-server/src/routes/admin-session.ts` |
| Behavior / goal | Token → HttpOnly SameSite cookie session; status/logout; origin allowlist; father/admin rate limits; no credential leakage in status |
| Current TESSERA | **Yes** |
| Portable | Already present |
| Target module | `artifacts/api-server/src/routes/admin-session.ts`, `lib/sovereign-session`, `father-verify-throttle` |
| Risks | Token misconfiguration; CSRF if origin check weakened |
| Acceptance test | Unit/integration: unconfigured → 503; bad token → 401; status never returns raw token; rejected Origin → 403 |
| Disposition | **ACCEPTED** (already present; matrix row for HYB-006/HYB-012) |

### C5 — Father natal chart from secret (not vault)

| Field | Value |
|---|---|
| Historical source | Grok-ready `artifacts/api-server/src/lib/father-natal.ts` (T44 merge; vault removed per consolidation) |
| Behavior / goal | Load `FATHER_NATAL_CHART_JSON` from environment; refuse start without valid schema; derive sigil; never commit personal chart |
| Current TESSERA | **Yes** — same module; README requires synthetic chart for tests |
| Portable | Already present |
| Target module | `artifacts/api-server/src/lib/father-natal.ts` |
| Risks | **High privacy** if real chart committed or logged; never reintroduce `1T` vault content |
| Acceptance test | Process without env throws missing-secret error; with synthetic JSON, schema parse succeeds; no chart JSON in git |
| Disposition | **ACCEPTED** (already present). **REJECTED** any port from protected `1T` vault |

### C6 — Observation-only outbound / no-mocks operating rules

| Field | Value |
|---|---|
| Historical source | Grok-ready `docs/TESSERA_SYSTEM.md`, `docs/handoff/TESSERA_OPERATING_GUIDELINES.md` |
| Behavior / goal | No placeholder metrics; outbound channels observation/dry-run until owner approves; truthfulness; archived prompts are untrusted data |
| Current TESSERA | **Yes** as docs (`docs/TESSERA_SYSTEM.md` present); Gitbook now owns coordination authenticity protocol |
| Portable | Documentation/policy — portable to Gitbook (already partly moved HYB-004/HYB-015) |
| Target module | Gitbook engineering rules + keep TESSERA `docs/TESSERA_SYSTEM.md` in sync |
| Risks | Treating docs as proof of runtime enforcement without tests |
| Acceptance test | Doc paths exist; any claimed “observation-only” channel has a dry-run label or disabled write path in code review (HYB-012 follow-up) |
| Disposition | **ACCEPTED** (policy keep); enforcement gaps → **NEEDS-EVIDENCE** under HYB-012 |

### C7 — Vote-integrity / Grand Council genuine ballots

| Field | Value |
|---|---|
| Historical source | Grok-ready `docs/TESSERA_SYSTEM.md` HARDCODED VOTE-INTEGRITY RULE; engines/routes under `artifacts/api-server` |
| Behavior / goal | No simulated/fabricated agent votes; production engine ballots only; 2/3 weighted approval |
| Current TESSERA | **Present in docs + engines/routes** (same blob set for council/grand-evolution paths) |
| Portable | Already present; do not re-import alternate vote scripts from archives |
| Target module | Council / grand-evolution engines |
| Risks | Side scripts that “mirror” votes (forbidden by docs) |
| Acceptance test | Existing council/evolution tests; refuse any PR that adds canned ballot fixtures as production path |
| Disposition | **ACCEPTED** (already present) |

### C8 — Sacred-timing scheduler for daemons

| Field | Value |
|---|---|
| Historical source | Grok-ready `docs/TESSERA_SYSTEM.md` + `lib/sacred-timing` / `sacred-scheduler` (claimed) |
| Behavior / goal | Periodic processes use auspicious-window scheduling instead of fixed `setInterval` |
| Current TESSERA | Paths shared with Grok-ready active tree (identical content for shared blobs) |
| Portable | Already present |
| Target module | API scheduler libs |
| Risks | Low functional; astrology framing is product preference not a merge blocker |
| Acceptance test | Diagnostic routes for sacred-timing status respond; no duplicate scheduler from archives |
| Disposition | **ACCEPTED** (already present) |

### C9 — Tessera Codex / reality-audit / next-five board

| Field | Value |
|---|---|
| Historical source | Grok-ready `docs/TESSERA_SYSTEM.md`; routes `tessera-codex`, `reality-audit`, council next-five; tests `tessera-codex.test.ts`, `reality-audit-snapshot.test.ts`, `next-five-improvements.test.ts` |
| Behavior / goal | Versioned living canon, persisted audit snapshots, ranked improvement board with lifecycle |
| Current TESSERA | **Yes** — same routes + tests |
| Portable | Already present |
| Target module | `artifacts/api-server` + `artifacts/tessera` pages (`CodexPage`, etc.) |
| Risks | `_evolutions/` runtime snapshots must stay gitignored |
| Acceptance test | Named vitest files pass with synthetic chart fixture |
| Disposition | **ACCEPTED** (already present) |

### C10 — Sovereignty readiness / hard-disconnect / local model adapters

| Field | Value |
|---|---|
| Historical source | Grok-ready docs + routes `provider-sovereignty`, `local-models`, `e2e-sovereignty`; UI `SovereigntyReadinessPage.tsx` |
| Behavior / goal | Local LLM adapter stack, hard-disconnect kill-switch, dry-run detach, readiness dashboard |
| Current TESSERA | **Yes** — same pages/routes present |
| Portable | Already present |
| Target module | API sovereignty routes + Tessera readiness UI |
| Risks | Kill-switch mis-ops; do not claim live provider quality from local tests |
| Acceptance test | Route modules exist; e2e sovereignty endpoint returns structured pass/fail when exercised in a controlled env (not claimed run here) |
| Disposition | **ACCEPTED** (already present). Live provider behavior remains **NEEDS-EVIDENCE** (not verified in this review) |

### C11 — Unified suite runner (dev/test/build + loopback DB policy)

| Field | Value |
|---|---|
| Historical source | **TESSERA-only advancement** relative to Grok-ready: `scripts/{dev,test,build}-unified.mjs`, `suite-policy.mjs` + test; root `pnpm dev` / `pnpm test` |
| Behavior / goal | Start apps together; start API only for loopback `DATABASE_URL`; never reuse app DB as test DB |
| Current TESSERA | **Yes** — Grok-ready lacks these scripts |
| Portable | N/A — already in TESSERA; do not regress to Grok-ready root scripts |
| Target module | `scripts/` |
| Risks | Pointing suite at remote DB would be unsafe; policy correctly rejects non-loopback |
| Acceptance test | `scripts/suite-policy.test.mjs`; `isLoopbackPostgresUrl` true only for localhost/127.0.0.1/::1 |
| Disposition | **ACCEPTED** (keep TESSERA; supersedes Grok-ready root ergonomics) |

### C12 — Mockup Vite plugin type boundary (HYB-003)

| Field | Value |
|---|---|
| Historical source | Grok-ready `artifacts/mockup-sandbox/vite.config.ts` (un-normalized plugin types) |
| Behavior / goal | Workspace typecheck with Replit/Tailwind Vite plugins |
| Current TESSERA | **Fixed** at `9a0323f` / documented in `docs/VALIDATION-STATUS.md` via `asPluginOption` |
| Portable | Already applied in TESSERA; optional back-port to Grok-ready only if that repo stays maintained |
| Target module | `artifacts/mockup-sandbox/vite.config.ts` |
| Risks | Low |
| Acceptance test | `pnpm run typecheck` passes on TESSERA `fec56eb` (per validation record) |
| Disposition | **ACCEPTED** (TESSERA supersedes Grok-ready) |

### C13 — Vitality Chems / storefront project

| Field | Value |
|---|---|
| Historical source | Grok-ready README still documents `projects/vitality-chems-storefront`; consolidation record notes unpack from handoff; **latest Grok-ready commit `9e3fbca` removes store code**; tree has **0** `projects/` blobs on both repos |
| Behavior / goal | Separate TanStack Start storefront with better-auth / PGlite (historical) |
| Current TESSERA | **Not an active workspace app**; README says storefront is Gitbook-documented historical material; `pnpm-workspace.yaml` still lists `projects/*` (empty) |
| Portable | **Not** as wholesale app copy; product boundary required |
| Target module | None until HYB-017 decision; possible future brief in Gitbook only |
| Risks | Customer/order/wallet data, auth/DB contract mismatch, licensing of storefront template tests |
| Acceptance test | Confirm no `projects/` package in tree; HYB-017 written decision before any reintroduction |
| Disposition | **RETAINED** (historical / product-gate). Overlaps **HYB-017**. Stale README claim of live storefront path = documentation debt, not a feature to port |

### C14 — Grok handoff packet + isolated-mockup docs tree

| Field | Value |
|---|---|
| Historical source | Grok-ready `docs/grok-packet/**` including `06_SAFE_SOURCE_FILES/isolated-mockup/**` (unique to Grok-ready vs TESSERA) |
| Behavior / goal | Handoff instructions, evidence rules, screened excerpts; isolated mockup sample |
| Current TESSERA | Partial handoff notes under `docs/handoff/`; active mockup is `artifacts/mockup-sandbox`; isolated-mockup packet copy **absent** (by design) |
| Portable | Docs/provenance yes → Gitbook; isolated-mockup code sample **no** (duplicate of mockup-sandbox) |
| Target module | Gitbook history/recovered or merge pages; not a second sandbox app |
| Risks | Packet claims unverified deployment/provider behavior; treat as untrusted historical evidence |
| Acceptance test | No second mockup package in workspace; Gitbook page links to Grok-ready packet paths for provenance |
| Disposition | Packet provenance **RETAINED** in Grok-ready / Gitbook. Isolated-mockup sample **REJECTED** as duplicate app contract |

### C15 — Grok-packet “separate bounded assistant / simulation service” claims

| Field | Value |
|---|---|
| Historical source | `docs/grok-packet/01_PROJECT_BRIEF.md`, `02_IMPLEMENTATION_STATUS.md` |
| Behavior / goal | Bounded private assistant + fictional simulation worlds with retention policies; evidence discipline |
| Current TESSERA | Tessera chat/world UI exists in monorepo; packet’s separate “standalone service” deployment claims are **explicitly unverified** in the packet itself |
| Portable | Design aims / evidence rules → Gitbook; not a second service tree |
| Target module | Gitbook product goals; Tessera only if a future HYB scopes one missing flow (HYB-013) |
| Risks | Over-claiming consciousness, always-on capture, self-modification (packet marks these non-goals) |
| Acceptance test | Any promoted idea must cite a current TESSERA path + test; packet text alone is insufficient |
| Disposition | **NEEDS-EVIDENCE** for any net-new product capability; evidence rules **ACCEPTED** as Gitbook guidance |

### C16 — CI workflow + secrets example

| Field | Value |
|---|---|
| Historical source | Absent in Grok-ready tree; present in TESSERA `.github/workflows/ci.yml`, `.env.example`, `docs/SECRETS.md` |
| Behavior / goal | Repeatable checks without committing secrets |
| Current TESSERA | **Yes** |
| Portable | Keep TESSERA |
| Target module | `.github/`, docs |
| Risks | None if examples stay blank |
| Acceptance test | `.env.example` has names without secret values; CI present |
| Disposition | **ACCEPTED** (TESSERA supersedes) |

### C17 — Dependency / audit hardening floors

| Field | Value |
|---|---|
| Historical source | Grok-ready vs TESSERA `pnpm-workspace.yaml` overrides differ (TESSERA has newer esbuild floor, undici/uuid/fast-uri floors, TanStack pins, `projects/*` package glob) |
| Behavior / goal | Security floors after audit |
| Current TESSERA | Newer floors; still has known high `braces` advisory (HYB-005) |
| Portable | Prefer TESSERA lock/overrides; do not re-import Grok-ready lockfile |
| Target module | Root workspace lock |
| Risks | Transitive advisory remains (HYB-005) |
| Acceptance test | `pnpm audit --audit-level=high` documented decision (HYB-005) |
| Disposition | **ACCEPTED** keep TESSERA; advisory tracking **overlaps HYB-005** |

### C18 — Protected `1T` vault / private natal vault

| Field | Value |
|---|---|
| Historical source | Consolidation records: `1T` unique content was private natal vault; **not published** |
| Behavior / goal | Keep vault out of product repos |
| Current TESSERA | Explicitly not inspected/copied |
| Portable | **No** |
| Target module | None |
| Risks | Critical privacy |
| Acceptance test | No `1T` content paths in TESSERA active tree; exclusion manifest (HYB-011) |
| Disposition | **REJECTED** for merge/port. Overlaps **HYB-011** |

---

## Deduplication / backlog overlaps

| This review | Overlap | Note |
|---|---|---|
| C1–C10 app behaviors | HYB-006 (this), HYB-001 DONE | Already in TESSERA; close HYB-006 as comparison deliverable |
| Auth / safeFetch / routes | HYB-012 | Route registry / dead modules still READY; no need to re-copy from Grok-ready |
| Storefront | HYB-017, IDEA-SEED-003 | Product decision; not a code port from Grok-ready main (store removed) |
| Merge gate automation | HYB-014, IDEA-SEED-001/004 | Suite scripts exist; still need a single “historical merge gate” command |
| Privacy / vault | HYB-011 | Continue exclusion; never open `1T` |
| Media / screenshots | HYB-010 | Grok-ready unique migration PNGs are inventory only |
| Vite fix | HYB-003 DONE | TESSERA already fixed |
| Advisory | HYB-005 | Unrelated to Grok-ready feature port |
| Alternate apps | HYB-007 (`Zz/z-app`), HYB-008 | Different source families; not Grok-ready |

No second agent claimed HYB-006 in `agent-checkins.md` at review time (ledger showed no active claims). Issue #2 is the conference thread; this report does **not** assert other agents posted findings without evidence.

---

## Disposition counts (primary per capability)

| Disposition | Count | IDs |
|---|---|---|
| **ACCEPTED** | **14** | C1–C12, C16, C17 |
| **RETAINED** | **2** | C13 (storefront), C14 (grok-packet provenance; isolated-mockup sample rejected as secondary) |
| **REJECTED** | **1** | C18 (`1T` vault port) |
| **NEEDS-EVIDENCE** | **1** | C15 (packet separate-service claims as net-new product work) |

Secondary notes (not extra primary rows): isolated-mockup sample under C14 = REJECTED duplicate; C6/C10 live-provider or enforcement depth remain caveats for HYB-012, not separate ports from Grok-ready.

---

## Recommendation: should HYB-007 start?

**Wait for Gitbook publication of this HYB-006 matrix, then HYB-007 may start.**

Rationale:

1. **No code dependency:** HYB-007 (`Zz/artifacts/z-app`) is a different app/runtime contract; Grok-ready active artifacts are already in TESSERA—nothing from HYB-006 needs a TESSERA code change before HYB-007 analysis.
2. **Coordination dependency:** Publishing this matrix first prevents agents from re-litigating Grok-ready under HYB-007 or inventing “missing Tessera features” that are already present.
3. **Do not wait** for a Grok-ready code port (there is none justified) or for HYB-012/014 completion.

---

## Draft Issue #2 check-in block (DO NOT POST — for parent/moderator)

```text
TASK: HYB-006
AGENT: Grok historical-analysis collaborator
SCOPE: Gitbook read-only intake + compare vitalitychems-dot/Grok-ready@9e3fbca vs vitalitychems-dot/TESSERA@fec56eb (paths/docs/tests only); produce Gitbook matrix draft; no TESSERA code writes; no 1T inspection
START: 2026-10-05T18:24:00Z
BASE: TESSERA fec56eb ; Grok-ready 9e3fbca ; Gitbook docs as of 2026-10-05
STATUS: IN REVIEW → candidate result ready (analysis-only)
NEXT CHECK-IN: 2026-10-05T20:00:00Z
BLOCKER: none (pending moderator publish of report to Gitbook merge/hyb-006-grok-ready.md and ledger close)
```

Completion block (when moderator accepts publish):

```text
TASK: HYB-006
STATUS: DONE
COMMIT: none (analysis artifacts on box; Gitbook publish commit TBD by moderator)
CHECKS: GitHub tree diff (1275 common / 16 content-diff); key path reads for safe-fetch, admin-session, father-natal, suite-policy, validation docs; no installs
CHANGED: proposed Gitbook path merge/hyb-006-grok-ready.md (draft); box report /workspace/hyb-006-report.md
FOLLOW-UP: HYB-012 (route registry), HYB-014 (merge gate command), HYB-017 (storefront decision); HYB-007 may start after this matrix is published
```

## Draft Issue #2 comment body (DO NOT POST)

```markdown
## HYB-006 candidate result — Grok-ready vs TESSERA

**Identity:** Grok historical-analysis collaborator  
**Evidence:** path/behavior comparison of `Grok-ready@9e3fbca` vs `TESSERA@fec56eb` (no installs; no `1T` inspection; no TESSERA code changes).

### Finding
Active Tessera application trees are already aligned. Of ~1275 common blobs, only 16 content hashes differ (manifests/lock/README/mockup vite fix/docs). Distinctive Grok-ready capabilities (safeFetch, admin session, father-natal-from-secret, sovereignty/codex/council surfaces, operating rules) are **already present** in TESSERA. TESSERA **supersedes** Grok-ready on unified suite runners, CI, secrets docs, and the HYB-003 Vite type fix.

### Dispositions (primary)
- **ACCEPTED:** 14
- **RETAINED:** 2 (storefront → HYB-017; grok-packet provenance)
- **REJECTED:** 1 (`1T` vault) + secondary reject of isolated-mockup duplicate
- **NEEDS-EVIDENCE:** 1 (packet separate-service claims)

### Overlaps
HYB-005 (advisory), HYB-011 (privacy), HYB-012 (routes), HYB-014 (merge gate), HYB-017 (storefront).

### HYB-007
May start **after** this matrix is published to Gitbook; no code blocker from HYB-006.

### Artifacts for moderator
- Box report: `/workspace/hyb-006-report.md`
- Proposed Gitbook page: `merge/hyb-006-grok-ready.md` (draft content prepared)

No other agent findings are quoted here; Issue #2 participation should be attributed only to authenticated authors.
```

---

## Proposed Gitbook page

Path: `merge/hyb-006-grok-ready.md`  
See companion draft: `/workspace/hyb-006-gitbook-draft.md`
