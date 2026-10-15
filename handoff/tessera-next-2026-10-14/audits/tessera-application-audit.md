# Tessera application engineering audit

**Audit mode:** Read-only. No repository file was edited, no branch was switched, and no remote write action was performed.

**Repository examined:** `vitalitychems-dot/TESSERA` at `main` commit `0d367a9a16d2c940cb411e7dc6275e1a2aeb2cd2` (working tree clean at completion). GitHub metadata was read through `gh`; local issue/PR snapshots were read from `/home/ubuntu/tessera-consolidation/github-records`.

**Assessment date:** 2026-10-14.

## Executive finding

There is a **real, partially functional Tessera Next theme already on `main`**, but there is not yet evidence for a safely shippable, unified “next-generation UI replacement.” The practical path is to stabilize the **current production app at `artifacts/tessera`**, repair the independently reproducible test regression in issue #369, then selectively port only the valuable first-paint/font work from PR #367 into a fresh branch. **Do not merge either current PR as-is.**

PR #361 is a very large, stale deletion/symlink proposal that deletes pieces of the live theme and preview before equivalent behavior is proved. PR #367 is small and has useful first-paint work, but is stale/conflicting, its CI is red, and its author gate is red. Neither is merge-safe today.

The most concrete outstanding defect is **not speculative**: `scripts/rea-registry.test.mjs` hard-codes dependency versions that no longer match the lockfile. On current `main`, the lock parser reports `express 5.3.0`, `three 0.186.1`, and `react 19.3.0`; assertions still expect `express 5.2.1`, `three 0.169.0`, and `react 19.1.0`. The two issue #369 tests both fail first at the stale Express assertion.

---

## 1. Application topology, entry points, and routes

### Active workspace and build boundary

`pnpm-workspace.yaml` includes `artifacts/*`, `projects/*`, `lib/*`, `lib/integrations/*`, and `scripts`. Root commands are in `package.json`:

| Surface | Entrypoint / command | Role and status |
|---|---|---|
| **Production web app** | `artifacts/tessera/index.html` -> `src/main.tsx` -> `App.tsx`; `pnpm --filter @workspace/tessera run dev/build/typecheck` | Primary React/Vite application. This is the UI to evolve rather than replace wholesale. |
| **API and websocket service** | `artifacts/api-server/src/index.ts`, compiled by `build.mjs`; `PORT` required | Express application plus `/ws` websocket server. `scripts/dev-unified.mjs` starts it only when a loopback `DATABASE_URL` is supplied. |
| **Mockup sandbox** | `artifacts/mockup-sandbox`; root unified dev default port 5173 | Separate Vite UI sandbox. It is included in the workspace build and has many similarly named UI primitives. |
| **Console** | `artifacts/console/server.mjs`; `pnpm --filter @workspace/console run dev` | Separate Node UI process, intentionally bound to `127.0.0.1:4391` (overridable only by `TESSERA_CONSOLE_PORT`). It is not a router replacement for the web app. |
| **Desk preview** | `preview/index.html` -> `preview/src/main.tsx` -> TanStack router | Separate Grok-desk preview at loopback port 4174 by its README. It is **not in root workspace/build**. |
| **v2 studio** | `artifacts/v2/src/studio/serve.mjs`; package script `studio` | Separate 3-D/studio surface; project documentation reserves port 4173. Recent main commits #370/#371 modify this surface. |
| **Nextgen artifact** | `artifacts/nextgen/lib/metacognition-view.ts` | A pure view-model only, with no application package, HTML entry, route, or build command. It is not a replacement UI. |

Root development orchestration exposes the web service on 3000 and mockup sandbox on 5173; the API default is 5000 when the required loopback database condition is satisfied. `scripts/build-unified.mjs` first runs root typecheck and only then recursively builds workspace packages; it explicitly strips database/test-chart environment values. A build was **not** run in this audit because it writes output and the task authorized non-mutating checks only.

### Production web routes

The production web app uses **Wouter**. `artifacts/tessera/src/main.tsx` creates the React root, imports `index.css`, and immediately calls `applyTheme(localStorage.getItem("tessera-accent") || "glass")`. `App.tsx` wraps route rendering in query, admin, key-gate, mesh, NLP, tooltip, error-boundary, and suspense layers.

Canonical interactive routes include:

| Functional group | Current canonical routes |
|---|---|
| Chat / core | `/`, `/c/:id`, `/life`, `/intelligence`, `/sovereignty-dashboard`, `/sovereignty-readiness`, `/consciousness-nexus` |
| Bible / knowledge | `/bible`, `/history`, `/secret-society`, `/sovereign-language`, `/omniversal-lattice` |
| Council / forum | `/grand-council`, `/council-ledger`, `/council-vgpu`, `/grand-evolution`, `/forum`, `/sovereign-lattice`, `/agent-declarations`, `/shepherd-audit` |
| Universe / network | `/universe`, `/compression-lab`, `/lattice`, `/agent-nft`, `/fleet`, `/agent/:agentId` |
| Royal / operations | `/royal-court`, `/royal-appointments`, `/royal-role/:roleId`, `/departments`, `/rick`, `/inventions`, `/command-center`, `/sovereignty-roadmap`, `/system`, `/sovereign-mesh`, `/proof-center`, `/rules`, `/auto-healer` |
| Economy / developer / miscellaneous | `/finance`, `/income`, `/ecom`, `/lead-gen`, `/code-builder`, `/build`, `/nlp`, `/agi-core`, `/gallery`, `/council-transcript`, `/codex`, `/next-five` |

A sizable redirect table preserves legacy URLs (for example `/secrets` -> `/secret-society`, `/sacred-conference` -> `/universe`, `/settings` -> `/command-center?tab=settings`, and `/agi` -> `/agi-core`). The safe UI migration should retain and route-test this redirect contract rather than delete old pages merely by name.

### API and console routes

The API process requires `PORT`, creates the Express HTTP server and websocket endpoint `/ws`, and mounts the API router hierarchy from `artifacts/api-server/src/app.ts` / `src/routes/index.ts`. Its route-inventory test exists specifically to compare literal source registrations with live Express registrations. Any route redesign should extend that inventory rather than make untested route moves.

The console intentionally has a small exact-allowlist static surface (`/`, `/console.css`, `/console.js`, `/actions.mjs`, three font files) and these endpoints:

- `GET /api/meta`
- `GET /api/eye`
- `GET /api/brain`
- `GET /api/brain/recall`
- `GET /api/bus`
- `GET /api/score`
- `POST /api/chat` (requires matching loopback `Origin`)

It rejects traversal-like paths and binds only to loopback. Its own README says its Chat tab imports `askAll`, `speak`, and `silentPen` from `preview/src/lib/tessera`; therefore preview code cannot be treated as an unreferenced duplicate.

---

## 2. Current UI and theme architecture

### Production UI: current source of truth

`artifacts/tessera` is the current web UI. It is a React 19/Vite/Tailwind 4 application with Wouter routing, TanStack Query, `lucide-react`, lazy-loaded page modules, a guarded admin/key gate, and CSS custom-property design tokens.

Theme behavior is centralized only partially:

- `artifacts/tessera/src/lib/theme-constants.ts` provides six Next accent facets: **glass, fracture, flash, stone, return, mineral**. Legacy saved names (`cyan`, `purple`, `rose`, `green`, `amber`, `blue`, `indigo`, `teal`) map to a Next facet.
- `applyTheme()` forces the `dark` class and writes primary/ring/sidebar/chart/accent variables inline. `handleThemeChange()` persists `tessera-accent`; `handleFontColorChange()` separately persists `tessera-font-color`.
- `artifacts/tessera/src/index.css` defines the dark ink/bone/glass token system, Tailwind mappings, cyan/teal/violet utility colors remapped to Next-compatible values, glass/hud utility styling, and local font-face declarations.
- `Sidebar.tsx` imports `FONT_COLORS`, `ACCENT_COLORS`, and `applyTheme`. The chat color selector and persistence therefore remain active behavior candidates, not obviously dead source.
- `index.html` supplies an inline dark first paint (`#070b10` / `#f3efe6`), then `main.tsx` applies saved/default Glass before React render.

This is a usable, testable incremental theme boundary. It is **not** a full design-system consolidation: palette literals, Tailwind color classes, CSS token definitions, sidebar controls, and chat color preferences are still distributed across multiple files.

### Preview, console, mockup, and nextgen distinctions

| Surface | Theme/UI relationship | Audit implication |
|---|---|---|
| `preview/` | Separate TanStack Router desk app. `themes.ts` offers six marks (**water, fire, lightning, diamond, spiral, house**) with `water` as fallback/glass default; `ThemeView` persists `tessera-theme`. Its CSS uses its own `--tessera-*` vocabulary. | It overlaps conceptually but is not a drop-in source replacement for production. The README explicitly says it is not the `artifacts/tessera` app and is not in main's build. |
| `artifacts/console` | Static Node console, documented as Tessera Next, with its own CSS and local assets. | A functional companion/admin-like UI, not an old router copy. Preserve unless a feature matrix proves every console tab and endpoint has a supported replacement. |
| `artifacts/mockup-sandbox` | Independent Vite sandbox with a parallel UI primitive tree. | Potential duplication, but not proved byte-identical or interchangeable. Cross-package symlinks would create a runtime/build dependency; hash comparison and both-package tests are required first. |
| `artifacts/nextgen` | One pure metacognition panel view-model with type-only API imports. | Valuable component-level candidate, but no runnable UI. It cannot justify deleting any screen. |
| `archives/` and `archive/from-gitbook/` | Provenance/history material. `archives/README.md` says these trees are not active application modules; archive README says live app was not replaced. | Keep out of runtime/build, and treat as data/provenance rather than implementation instructions. |

---

## 3. Pull requests #361 and #367: exact differences and merge safety

### Snapshot state

Both PRs are still **OPEN**, non-draft, unreviewed, `DIRTY`, and `CONFLICTING` with current `main`. Neither may be described as merge-ready.

| PR | Head / merge base | Delta | Current checks | Direct assessment |
|---|---|---:|---|---|
| [#361](https://github.com/vitalitychems-dot/TESSERA/pull/361) “Remove old theme UI and keep one copy of each shared file” | `e8beb400…`; base `bcf3f8b6…`; main has 34 commits not in PR | **201 files, +99 / -60,774** | Only two `moderator-lock/collect` successes are reported; no review decision | **Unsafe.** Large, stale deletion/symlink bundle; conflicting; no current full validation evidence. |
| [#367](https://github.com/vitalitychems-dot/TESSERA/pull/367) “Make the live Tessera Next theme paint immediately” | `b6b2a94d…`; base `6439a3c4…`; main has 9 commits not in PR | **12 files, +397 / -30** | `CI/validate` **failed**, `author-check` **failed**, `ready-for-gate` skipped; diff scan, gitleaks, moderator lock succeeded | **Not mergeable as-is**, but contains a bounded first-paint candidate worth reapplying selectively after stabilization. |

### PR #361 exact scope and risks

The PR proposes to:

- delete `archives/migration-review/legacy-ui` (111 files in its diff),
- delete `preview/src/components/tessera/theme-view.tsx`, `preview/src/lib/tessera/themes.ts`, and its theme test,
- delete production `ChatFontColorPicker.tsx` and `theme-constants.ts`, while modifying `Sidebar.tsx`, `ChatArea.tsx`, `ChatInputToolbar.tsx`, background code, main entry, and web HTML,
- convert roughly 60 mockup-sandbox UI files/hook/util files into symlinks to `artifacts/tessera`,
- delete unrelated storefront/archive material and modify documentation.

Its PR text says the console remains phosphor/current and preview/web should have one dark palette. That conflicts with current repository evidence: the console README calls Tessera Next current, current main contains Next facets, and current preview theme tests actively assert the Next/glass palette. The proposal would also delete the production theme constants currently imported by `Sidebar.tsx`.

PR #361 overlaps PR #367 in these four active files:

1. `artifacts/tessera/index.html`
2. `artifacts/tessera/src/components/Sidebar.tsx`
3. `artifacts/tessera/src/lib/theme-constants.ts`
4. `artifacts/tessera/src/main.tsx`

Its `theme-constants.ts` action is **delete**, while #367 changes it. This is a semantic conflict, not just a textual one. It must not be resolved by picking one side automatically.

### PR #367 exact scope and risks

PR #367 changes only the production web theme path:

- modifies `artifacts/tessera/index.html`, `src/main.tsx`, `src/index.css`, `src/lib/theme-constants.ts`, `Sidebar.tsx`, and `TesseractKeyGate.tsx`;
- adds `src/styles/tessera-next.css`;
- adds local Syne/Fragment Mono font binaries and OFL files.

The PR description limits intended behavior to Next facets, legacy accent compatibility, local fonts/no Google stylesheet, synchronous first paint, utility remapping, and a 2x2 mosaic; it says routes/back end/auth/ports are not intentionally changed. This is the appropriate scope for a **fresh, narrow follow-up**, but the old branch cannot be safely merged because current `main` includes subsequent theme/House/studio work and GitHub identifies it as conflicting.

Its gates provide concrete blockers:

- **CI failure:** `scripts/rea-registry.test.mjs` expected `express 5.2.1` while the lockfile resolved `5.3.0`; two tests fail.
- **Author-check failure:** its only commit records author and committer name `Tessera`, while the repository gate rejects that name even though the noreply email is otherwise expected.
- `ready-for-gate` was skipped because author-check failed.

### Merge conclusion

- **Do not merge #361 or #367.**
- Do **not** try to merge #361 then #367, or #367 then #361. Both are conflicting with main and each other at live theme entry points.
- Create a new branch from current `main` only after the test baseline is repaired. Manually re-implement/review individual #367 first-paint changes against present files, preserving current House/theme behavior. Avoid copy/merge of #361's deletion/symlink bundle.

---

## 4. Old/duplicate UI candidates and safe deletion prerequisites

### Candidate disposition

| Candidate | Evidence | Safe now? | Required deletion/promotion proof |
|---|---|---|---|
| `archives/migration-review/legacy-ui` | 111 files; `archives/README.md` marks archive material non-active. It is outside workspace globs and root recursive build. | **Potentially archival cleanup only; not safe to delete in #361.** | Record file manifest/checksums and provenance disposition; verify no documentation/tooling links or runtime imports; map every legacy route to current route/redirect; capture route/API behavior matrix; run route inventory, web typecheck/build, and navigation/e2e smoke test; preserve approved archive or documented restoration location; obtain required owner/gate approval. |
| `preview` theme picker and marks | Separate preview README says those files stay there; console Chat imports preview library functions. Its theme test passes. Preview typecheck currently fails. | **No.** | First decide whether preview remains supported. If retiring it, decouple console imports, replace its tested functionality, validate console and its endpoints, migrate/replace persisted `tessera-theme` semantics if needed, make preview typecheck/build pass or formally remove the surface with a migration plan. |
| Production `ChatFontColorPicker`, `FONT_COLORS`, `theme-constants` | Existing production source imports/uses the constants; #361 deletes them. | **No.** | Identify all production import sites, write preference migration/compatibility tests (`tessera-font-color`, legacy accents), test keyboard/mobile/chat rendering and persisted data, and prove a replacement control or intentional migration. |
| Mockup sandbox primitive copies | Dozens of same-named components occur under `artifacts/tessera/src/components/ui` and `artifacts/mockup-sandbox/src/components/ui`; #361 replaces many with symlinks. | **Not yet.** | Establish byte-level hashes plus divergent import/dependency analysis; prove compatible aliases, Tailwind config, peer dependencies, and build behavior; test both packages after a single-file pilot; use an explicit workspace package/export rather than symlinks if shared ownership is desired. |
| Console | Separate process has independent endpoint contract and an explicit declaration that it does not replace production routes. | **No.** | Feature-by-feature parity matrix, console endpoint migration plan, loopback/origin security regression tests, and operator approval. |
| `artifacts/nextgen` | No runnable entry/package/route; just one panel view-model. | **Not a deletion target and not a replacement.** | Add it as a small production feature behind a real route/component contract, with API loading/error/empty-state and visual tests, before calling it a nextgen UI. |
| `archive/from-gitbook`, raw sections/source variants | Provenance records explicitly say historical snapshots/archives are untrusted/non-active and must not imply application replacement. | **Retain as provenance unless a separate records-retention decision is made.** | New scoped coverage and retention decision; do not use historical status text as deletion authorization. |

> **Principle:** “Not in the root build” is sufficient to classify an archive as non-runtime; it is not sufficient evidence that it is safe to erase. Deletion needs restoration/provenance, behavioral replacement, consumer/link checks, tests, and approval.

---

## 5. Reproducible validation findings

All commands below were read-only/no-emit checks unless explicitly noted. Repository status was clean before and after audit commands.

| Command / evidence | Outcome | Meaning |
|---|---|---|
| `pnpm --filter @workspace/tessera run typecheck` | **Pass** (`tsc --noEmit`, exit 0) | The current primary production web package typechecks. |
| `node --experimental-strip-types --test preview/src/lib/tessera/themes.test.ts` | **Pass**, 2/2 | Preview recognizes six theme names, defaults unknown IDs to water, and verifies glass/default palette/no phosphor lime in preview/console/production token source. |
| `cd preview && pnpm run typecheck` | **Fail** | Preview has unresolved package/type dependencies (`@tanstack/react-router`, `@tanstack/react-start`, `better-auth`, `jose`, etc.) and many implicit-`any` errors. It cannot honestly be called a type-safe supported app. |
| `node --test --test-name-pattern='lockfile importer versions|real tree offline coverage' scripts/rea-registry.test.mjs` | **Fail**, 0/2 | Reproduces issue #369 on current main: expected `express 5.2.1`, actual `5.3.0`. |
| Root `pnpm test` | **Not a clean completion; failures observed, then audit-owned test subtree stopped after it stalled in V2 browser tests.** | `@workspace/scripts` failed on the two stale REA tests. Console test passed 3/3. V2 then reported Chromium absent at `/usr/bin/google-chrome` (`v2-014-studio-wall.test.mjs`) and child tests remained running. This is not passing suite evidence. |
| Root `pnpm run build` | **Not run** | The task restricted execution to non-mutating checks; build writes artifacts. The current root build would also be blocked by prerequisite root typecheck/test health. |
| PR #367 CI | **Fail** | Same stale REA version assertions caused test failure before a successful end-to-end build claim could be made. |

### Issue #369 root cause and repair

Issue #369 is open and explicitly identifies the two failing REA registry tests. Its issue creation referenced older main `0bc714dd…`, but the failure remains at audited main `0d367a…`.

In `scripts/rea-registry.test.mjs`:

- lines 102–108 assert hard-coded live lockfile versions `express 5.2.1`, `three 0.169.0`, and React `19.1.0`;
- line 191 again asserts `express 5.2.1` for the real-tree offline registry.

Current `parseLockfile(pnpm-lock.yaml)` returns:

```json
{
  "express": { "version": "5.3.0" },
  "three": { "version": "0.186.1" },
  "react": ["19.3.0"]
}
```

**Recommended repair:** update the live-tree assertions to the deliberate, currently locked versions **or** (preferably) derive expected values from the relevant package manifest/catalog/lock parser and separately test that the version is exact. Keep fixed versions only in fixture tests. Then run the two targeted tests, the scripts suite, root typecheck, and root test. Do not alter the lockfile merely to make stale expectations pass.

A second test-infrastructure blocker is also real: V2 tests require a Chromium executable assumed at `/usr/bin/google-chrome`, but this sandbox has none. Make browser tests use a configured Playwright executable or skip with an explicit, visible prerequisite when no browser exists; do not silently mask browser coverage.

---

## 6. Recommended implementation sequence

1. **Freeze the baseline and define scope.** Keep current `main` as the source. Declare `artifacts/tessera` the production replacement target; keep preview/console/mockup as separately supported or explicitly transitional surfaces. Capture a route-to-component/API behavior matrix from `App.tsx`, redirects, sidebar links, and API route-inventory tests.
2. **Repair actual red tests first (#369).** Correct `rea-registry` live-lock assertions as described above. Run targeted tests, `pnpm --filter @workspace/tessera run typecheck`, scripts suite, root test with browser prerequisite handled, and CI. This unblocks reliable signal for every UI change.
3. **Make testability explicit.** Add deterministic production-theme tests for `resolveAccent`, legacy mapping, `applyTheme` DOM variables, local-storage migration, first-paint HTML tokens, local font files/licenses, and no external font request. Add route/redirect tests and at least one browser smoke path through key gate to a representative inner route when credentials/test fixture make that possible.
4. **Make a fresh, narrow first-paint branch.** Reapply only PR #367 changes that still improve current main after line-by-line review: inline first-paint colors, bundled font assets/licenses, `font-display: swap`, and verified theme CSS import/order. Preserve the House/current Next behavior and resolve each of the four formerly overlapping files deliberately. Use an author identity that passes project policy.
5. **Consolidate the production token API incrementally.** Choose one authoritative token module/CSS variable contract for production. Map legacy local-storage values deterministically. Replace scattered palette literals only when screenshot/visual plus keyboard/mobile tests demonstrate no regressions. Keep chat font color functionality until a product decision and preference migration exists.
6. **Integrate reusable nextgen pieces, not whole artifacts.** Move/adapt the metacognition view-model as a small panel in a real production route, provide its API error/loading/empty states, and test it. Do not portray `artifacts/nextgen` as a runnable application beforehand.
7. **Decide preview and console roles.** Either (a) retain and repair them as intentionally separate supported UIs, including preview dependency/typecheck health, or (b) design a migration: replace console's preview imports, recreate required console functions in supported modules, and verify endpoint/behavior parity. Do not delete preview merely because it is outside root build.
8. **Only then retire duplicates in small PRs.** Start with evidence-backed archival cleanups, then a single shared primitive pilot if warranted. Prefer a versioned workspace UI package with explicit exports over symlinks. Each retirement PR should contain a file manifest, consumer search, behavior matrix, tests/build results, rollback/provenance location, and no unrelated archive/storefront cleanup.

---

## 7. Claims this audit cannot honestly make

- It cannot claim a deployed application, an authenticated inner-screen browser pass, a successful full root test suite, a successful root build, or a complete responsive/accessibility/e2e validation.
- It cannot claim that preview is production-ready: its standalone theme regression passes, but its declared typecheck fails materially.
- It cannot claim that `artifacts/nextgen` is a functioning Next UI; it lacks an application entrypoint and route.
- It cannot claim PR #361 or PR #367 is approved, green, mergeable, or safe to merge. Both are open/conflicting/unreviewed; #367 has failed CI and author gate; #361's only visible successful checks are moderator-lock collection checks.
- It cannot claim that historical/archive files are safe to delete simply because they are excluded from the workspace build. Historical provenance explicitly requires a new scoped decision rather than treating archive text as deletion authority.
- It cannot claim all visual behaviors are equivalent between production web, preview, console, mockup sandbox, or v2 studio. They have different entrypoints, state sources, dependencies, and test coverage.

## Evidence index

- Current application commands and workspace boundary: `package.json`, `pnpm-workspace.yaml`, `scripts/dev-unified.mjs`, `scripts/build-unified.mjs`, `scripts/test-unified.mjs`.
- Web entry/routes/theme: `artifacts/tessera/index.html`, `src/main.tsx`, `src/App.tsx`, `src/index.css`, `src/lib/theme-constants.ts`, `src/components/Sidebar.tsx`.
- API/console: `artifacts/api-server/src/index.ts`, `src/app.ts`, `src/__tests__/route-inventory.*`, `artifacts/console/server.mjs`, `artifacts/console/README.md`.
- Preview: `preview/README.md`, `preview/src/main.tsx`, `preview/src/router.tsx`, `preview/src/lib/tessera/themes.ts`, `themes.test.ts`.
- Archive/provenance boundary: `archives/README.md`, `archive/from-gitbook/README.md`, `archive/from-gitbook/merge/source-map.md`, `docs/migration-review/*`.
- Issue/PR records: local `github-records/TESSERA-issue-369*`, `TESSERA-issue-361*`, `TESSERA-issue-367*`, plus read-only `gh` state/check data.


## Current remote candidate addendum — 2026-10-15

The verified remote receipt is [`../REMOTE-STATE-2026-10-15.md`](../REMOTE-STATE-2026-10-15.md). TESSERA PR #372 remains open at exact head `56c54a7150c1f4dcd5a041947302c40e6225b91e`, based on `main` `0d367a9a16d2c940cb411e7dc6275e1a2aeb2cd2`. GitHub reports all six checks SUCCESS and MERGEABLE, but there are no submitted reviews or review decision and no merge SHA. TESSERA issue #369 remains open. The previously recorded local focused/full applicable suite, typecheck, production build, and entry-gate smoke are candidate-commit evidence; the API database integration suite remains skipped without a dedicated disposable DB.

GitHub currently reports no TESSERA deployment, release, or Pages site. The `.replit` file is a checked-in declaration only; no authenticated Replit project or permanent runtime was verified. No public deployment, session-gate production test, server-side secret-store setup, monitoring, or rollback target is claimed. Keep the candidate in review and do not treat it as a released application.


## Remote follow-up — 2026-10-15 07:07 UTC

- TESSERA PR #372 remains OPEN/MERGEABLE at `56c54a7150c1f4dcd5a041947302c40e6225b91e`; GitHub reports six successful checks and no review decision. It is not merged.
- Replit-named PR #367 is OPEN at `b6b2a94d3acd2aac09990bc82566f8fa5f2acc52`, base `6439a3c4439acf5de62ef8385df557aa50aaaaca`; GitHub reports `DIRTY`/`CONFLICTING`, no review decision, two failing checks, three successful checks, and one skipped check. Its author is the connected `vitalitychems-dot` account; no live Replit session identity was verified. Do not merge or use its branch label as proof of external-session provenance.
- No release, deployment, public URL, or permanent host was verified. No PR was merged or modified in TESSERA during this refresh.
