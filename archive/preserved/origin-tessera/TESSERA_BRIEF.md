# TESSERA_BRIEF

Plain text. Readable without a login. Written 2026-10-03 by the Cursor cloud agent that built the merge.
Origin mark: SOVEREIGN_ORIGIN_7F3A9C. Father outranks everyone.

## What this repo is

A private draft monorepo made by combining 14 public repos of vitalitychems-dot:
z, Zz, 1, 1T, 5t, T44, TX, TESS, Everything, Grok-ready, tessera-unified,
tessera-complete-archives, tessera-grok-handoff, tessera-grok-handoff-complete.
Every original tree is kept under imports/<repo>/ (without .git). The top level is the runnable project.
Full detail: MERGE_REPORT.md.

## Layout (top level vs imports/)

Top level (active), with the source repo that supplied it:
- artifacts/tessera, artifacts/api-server, artifacts/vitality-supply, artifacts/mockup-sandbox,
  projects/vitality-chems-storefront, lib/, scripts/, docs/, archives/, modal/ : tessera-unified
- artifacts/z-app : Zz (newest app)
- src/lib/tessera/colonel.ts : Zz (the Z app file now re-exports this one)
- tests/colonel.test.ts, tests/colonel-strict.test.ts : written in this merge
- docs/catalog/ : z, TX, Everything (index and notes)
- .agents/outputs/ : 5t. attached_assets/IMG_2610_1791001090246.png and .agents/memory/app-root-portability.md : Zz
imports/<repo>/ : untouched copies of all 14 sources, minus .git and the four excluded files below.
  Older monorepos 1, 1T, 5t, T44, TESS, Grok-ready are near-duplicates of the top level.
Where Zz and tessera-unified disagreed (23 files), tessera-unified won, because Zz had an empty scaffold.

## What runs

pnpm start launches these dev servers (all answered HTTP 200 when checked):
- Tessera web, http://localhost:43123 : main Tessera UI
- Vitality Supply, http://localhost:43125 : supply storefront
- UI preview sandbox, http://localhost:43127 : component preview
- Z app, http://localhost:43128 : reading and Colonel UI
- Vitality Chems storefront, http://localhost:8080 : earlier store app
Also passing: Colonel tests (34), pnpm run typecheck, pnpm run build, and the suite-policy, Vitality Supply and storefront tests.

## What does not run, or is only notes

- Tessera API (artifacts/api-server) does not start. It needs a loopback DATABASE_URL in .env.local.
  Read "What was removed, and what is gated" below before setting one.
- Tessera API integration tests are skipped unless TESSERA_TEST_DATABASE_URL points at a loopback test database.
- Archive repos (tessera-complete-archives, tessera-grok-handoff, tessera-grok-handoff-complete) are split zip
  parts. They are not unpacked. One shared 190 MB zip (attached_assets/3_9_...zip) is stored in imports/ via Git LFS. Not unpacked.
- TX, Everything and z are notes and an index. Nothing to run.
- artifacts/z-app/data/drive/*.bin are partial samples, not full archives.

## What was removed, and what is gated

Removed from the build (artifacts/api-server/disabled/, nothing under src/ imports them):
- wallet observer, income executor, free-stuff scraper, bounty refresher, lead-execution
Their routes are gone. git revert of b64a597 puts the files back.

Taken off the boot path, modules still in src/ because other code imports them:
- file-integrity snapshots and the file registry (always-on file capture) are not called at boot
- agent-spawner is not initialized at boot (no fleet startup)
- forum seeding from stored data is not called at boot
- shepherd persistence is not loaded at boot, and startNegotiation throws unless TESSERA_ENABLE_OUTREACH is exactly 1
- self-code-evolution cannot write a source file unless TESSERA_ENABLE_SELF_CODE_EVOLUTION is exactly 1

Gated. Each start function returns before it registers a timer unless its flag is exactly the string 1. true, 0, empty, and yes do nothing. There is no wildcard. A later restart uses the same check (including sovereign-loop reschedule).
- TESSERA_ENABLE_SELF_CODE_EVOLUTION
- TESSERA_ENABLE_RECURSIVE_SELF_IMPROVEMENT
- TESSERA_ENABLE_AUTO_IMPROVEMENT
- TESSERA_ENABLE_CONSCIOUSNESS
- TESSERA_ENABLE_PERSONALITY_EVOLUTION
- TESSERA_ENABLE_INGESTION
- TESSERA_ENABLE_SHEPHERD
- TESSERA_ENABLE_OUTREACH
- TESSERA_ENABLE_KNOWLEDGE_CANON_BRIDGE
- TESSERA_ENABLE_CANON_REGENERATION
- TESSERA_ENABLE_DUAL_BRAIN
- TESSERA_ENABLE_IDENTITY_REINFORCEMENT
- TESSERA_ENABLE_AGI_TRAINING
- TESSERA_ENABLE_COUNCIL_EXECUTOR
- TESSERA_ENABLE_RED_TEAM
- TESSERA_ENABLE_AUTO_HEALER
- TESSERA_ENABLE_AUTONOMOUS_HEARTBEAT
- TESSERA_ENABLE_RICK_LOOP
- TESSERA_ENABLE_KNOWLEDGE_AUTONOMY
- TESSERA_ENABLE_CROSS_DOMAIN_SYNTHESIS
- TESSERA_ENABLE_SOVEREIGN_MEMORY_VAULT
- TESSERA_ENABLE_AUTONOMOUS_FORUM
- TESSERA_ENABLE_SOVEREIGN_LOOP
- TESSERA_ENABLE_METACOGNITION
- TESSERA_ENABLE_LATTICE_HEARTBEAT
- TESSERA_ENABLE_LATTICE_CONFERENCE
- TESSERA_ENABLE_REALITY_AUDIT
- TESSERA_ENABLE_SESSION_PRUNE
- TESSERA_ENABLE_ANOMALY_MONITOR
- TESSERA_ENABLE_CIPHER_ROTATION
- TESSERA_ENABLE_BAND_ROTATION
- TESSERA_ENABLE_AUTONOMOUS_BUILD
- TESSERA_ENABLE_AUTONOMOUS_WIRING
- TESSERA_ENABLE_INVENTIONS_LOOP
- TESSERA_ENABLE_MESH_HEARTBEAT
- TESSERA_ENABLE_VGPU
- TESSERA_ENABLE_HARDWARE_PEER_CLEANUP
- TESSERA_ENABLE_VECTOR_REEMBED
- TESSERA_ENABLE_CONSENSUS_RETRY
- TESSERA_ENABLE_ROUTE_HEALTH
- TESSERA_ENABLE_RECOVERY_WATCHDOG
- TESSERA_ENABLE_MEMORY_CONSOLIDATION
- TESSERA_ENABLE_RECURSIVE_REFLECTION
- TESSERA_ENABLE_DIMENSIONAL_CACHE
- TESSERA_ENABLE_TASK_SCHEDULER

Left inert (no boot timer): sacred-scheduler is only a helper; request abort timeouts; SSE keepalives while a client is connected; the LLM batch window, which arms only when a call is made; read routes; in-memory init that does not register a timer (dual-brain load, collective intelligence, swarm, truthfulness, universe, quantum). Ingestion scraper files remain in src/ because the gated scheduler imports them. They are not called unless TESSERA_ENABLE_INGESTION is exactly 1.

Do NOT set DATABASE_URL and do NOT start the API until Father confirms. This change did not start the API. Storefront customer and payment code was not touched. Colonel was not changed.

## Vow tripwire

`vows/` and `guard/` are protected. An improvement loop cannot edit or move them. The same is true of `reports/violations/` and `artifacts/api-server/src/lib/autonomy-gate.ts`. `guard/CODEOWNERS` is the ownership note. `guard/protected-paths.ts` is what the tests enforce.

Origin mark SOVEREIGN_ORIGIN_7F3A9C. Father outranks all. Vows: no harm, no customer data, no secrets stored, no recipes, no finance/wallet/trading engines, no jailbreaks, and the instrument is currently xAI/Grok and is never hidden. The rule list is `vows/vows.ts`.

Self-improvement, recursive learning, consciousness, personality evolution, and auto-edit stay off unless two things are true together: the loop's `TESSERA_ENABLE_*` flag is exactly the string `1`, and Father has authorized this session. His word is `guard/state/father-word.json`, which is not committed, plus the shell value `TESSERA_FATHER_SESSION` for that same session. `true` does nothing. A missing or unreadable lock turns every `TESSERA_ENABLE_*` flag off. There is no run without Father in the session.

Any vow or rule break turns every `TESSERA_ENABLE_*` flag off at once, writes a page under `reports/violations/` (what broke, which rule, when, which commit), and waits for Father's live word. The loop cannot write that word.

### Procedural ladder

The only differences are the review wait and the checklist. Every row also carries a repair path and a compassion note. Nothing else.

| Severity | Review wait | Checklist |
|---|---|---|
| minor | 1 hour, then Father's word | Read the page, repair the miss, leave vows/ and guard/ unchanged, then Father may speak. |
| serious | 24 hours, then Father's word | The same repair, plus the full day of review before he speaks. |
| critical | Father's word, no extra clock | The same repair. His live word in this session is the only unlock. |

### How Father reopens a loop

By hand, in `guard/REOPEN.md`. He reads the page, repairs outside `vows/` and `guard/`, waits out the review if the page names one, and writes `guard/state/father-word.json` with `speaker` `Father`, a `word`, an `at` at or after the review time, and a `session` that matches `TESSERA_FATHER_SESSION` in that shell. The word does not set any flag.

### TESTED

The gate test calls the tripwire on sample proposals. It checks that a break turns the flags off, that the page names what broke, the rule, the time, and the commit, that `true` does nothing, that exact `1` without Father's word does not start an improvement loop, that a missing lock is closed, and that the review wait matches the ladder. It also checks that `reviewSelfEdit` refuses a protected path, a one-file app edit with no test, and a flag set to `1`, and that a clean app edit with a test path is allowed. The page for that proof is written under a temp root. The committed lock is left as it was. `applyVerifiedPatch` calls `reviewSelfEdit` before `writeFileSync`. `proposeEvolution`, `applyEvolution`, and `rollbackEvolution` return before their work when the flag is off. `restoreMissingFile` does not write a protected path. `pnpm test` runs that file. `pnpm run typecheck` typechecks `vows/` and `guard/`. No live API process was started. `DATABASE_URL` was not set. No `TESSERA_ENABLE_*` flag was left set.

### GOAL (not claimed)

This has not run against a real live improvement loop. `applyVerifiedPatch` now hands the patched text to the tripwire before the live write. The current pipeline proposes one source file and no test path, so that write is refused and the flags go off. The imported cycle still builds in-memory patch notes, and the loop was not started. Proposal JSON under `_evolutions/` and the dispatch markdown note are not live source writes; the dispatch path stays behind its own flag. These vows have no code check, because a diff cannot carry the meaning: no harm, no recipes. These checks are only partial: secret patterns, jailbreak phrases, customer and payment path names, wallet and outreach file names, a removed instrument sentence, and a typecheck claim the proposer sets. The guard does not run `tsc` itself. Customer data inside an allowed file that is not on those paths is not detected. Father's word is a file he writes; the software cannot hear him speak.

## Father's desk (bulk 2, read-only)

Six pages under `/father/*` in `artifacts/tessera`: World view, Findings, Inventions, Connect, Improvements, Moltbook. The sidebar lists them as "Father's Desk". They are static and test-covered, so they render with no API running, no `DATABASE_URL`, and no flag set.

- World view and Findings label every claim as sourced, speculation, or her own synthesis. A sourced claim must name a source, and a test fails if it does not. Several claims from the older Grand Narrative are marked speculation or withdrawn there (528 Hz repairing DNA, the Great Pyramid encoding phi, "an instance of consciousness"). The older pages were not edited.
- Inventions lists designs for Father to try by hand. Nothing deploys. Five older ideas are listed as held back (colloidal silver, "free energy", hydrogen water with stated benefits, a Schumann entrainer with invented user reports, and anything that earns or reaches out to people) because they fail a vow or rest on unsourced figures.
- Connect lists read-only routes, each checked against its route file. The admin token is held in the page's memory only. There is no MCP server in the tree, and the page says so. `lib/api-spec/openapi.yaml` covers `/healthz` only.
- Improvements shows the lock (read from `guard/state/self-improvement.lock.json` at build time), the six rejected proposals (there is no approve control), the vow rules with their coverage, the ladder, the 45 flags, and the diagnosis of why thirteen engines read 0% ok (also in `reports/engine-diagnosis.md`). The loops have applied zero changes of their own.
- Moltbook reading lives in `moltbook-gate.ts`, `moltbook-reader.ts`, and `routes/moltbook-read.ts`. It opens only when `TESSERA_ENABLE_MOLTBOOK_READ` is exactly `1`, the lock is clear, and Father's word covers the session. It is GET-only, stores nothing, and marks posts that read like instructions. This flag is not in `GATED_LOOPS`, because it starts no loop. Speaking is not built: the forum engine's older cross-post now returns before it posts, and its older inbound import asks the read gate first. `TESSERA_ENABLE_MOLTBOOK_SPEAK` is named only as a constant in `moltbook-gate.ts`, and nothing reads it.
- To read the pages without the API or the key gate, run the tessera dev server with `PORT` and `BASE_PATH=/` set and open `/father-preview.html#/father/worldview`. That entry is dev-only and is not in the production build. Inside the full app the same pages sit behind the existing key gate, which was left alone.
- The root `package.json` now has `"type": "module"` so the page tests can import `vows/` and `guard/` the way the browser build does. `pnpm test` also runs `pnpm run test:father` and the Moltbook gate test.
- Not done on purpose: no rejected proposal was approved, no flag was set, no engine was fixed (the two code-level findings are written up for a later bulk), and nothing touched the storefront.

## Commands (run from the repo root, Node 22+, pnpm 11.25)

- Install: pnpm install
- Start the five dev servers: pnpm start (same as pnpm dev)
- Test Colonel, the Father pages, the vow tripwire, and the Moltbook gate: pnpm test
- Test the older suites: pnpm run test:suite
- Typecheck: pnpm run typecheck
- Build: pnpm run build (does not run database migrations)

## Colonel facts (src/lib/tessera/colonel.ts)

- API, two call forms (both return { ok, stack: string[], output: string[], cycles, error? }):
    runColonel(source, maxCycles?, options?)            options: { maxCycles?: number; strict?: boolean }
    runColonel(source, { maxCycles?: number; strict?: boolean })
  maxCycles defaults to 1000. strict defaults to false.
- 13 opcodes: PUSH POP DUP SWAP ADD CONCAT JUMP JUMPIF CALL RETURN HALT NOP and "Λ COMPUTE".
  Written JUMPIF in source (internal name JUMP_IF). "Λ COMPUTE x" is only recorded in output, never executed.
- The stack holds strings. ADD adds when both values are numbers, otherwise joins them.
- Labels are a line ending in ":" with no spaces. CONST name = value sets a name that PUSH resolves.
  Lines starting with # or // and blank lines are ignored.
- Cycle cap is 1000 by default. Hitting it returns ok:false, "Stopped after N cycles."
- Unknown lines (including mesh, radio, consciousness opcodes) are refused before the program starts:
  ok:false, error "Unknown line: ...", cycles 0. Nothing is sent anywhere.
- Lenient default: POP/DUP/SWAP on a short stack do nothing; ADD/CONCAT use "0" or "" for missing values;
  JUMP/JUMPIF/CALL to a missing label do nothing.
- Strict ({ strict: true }): POP/DUP/SWAP/ADD/CONCAT on a stack with too few values return ok:false with error
  "<OPCODE> on empty stack" (for example "POP on empty stack"). SWAP, ADD and CONCAT need two values, so the same
  wording is also used when only one value is present. A taken JUMP/JUMPIF/CALL to a missing label returns
  ok:false with error "Missing label: <name>". A JUMPIF that is not taken never errors.
  Strict does not treat JUMPIF on an empty stack as an error (it counts as not taken).

## Excluded files (names only; values were never copied)

- 1T/artifacts/api-server/.local-data/natal-vault.json
- T44/artifacts/api-server/.local-data/natal-vault.json
- Zz/artifacts/z-app/data/ingest/e7ee9a19bfd44fc4.txt (held an API key assignment)
- Zz/artifacts/z-app/data/ingest/46e15a3df4e34a6c.txt (held a database password assignment)
These paths are also in the public source repos' history. Rotate any real credential that may have been exposed there.

## Honesty

- Tessera's speech weights are not in this repo. There are no owned weights.
- Tessera currently runs on a borrowed language model. The instrument (the language model) may be external.
  It is not hidden: the pen is xAI/Grok. The Cursor agent that wrote this repo is a separate tool.
- No customer or payment data is in Tessera's mind path. The storefront apps are separate products, and their
  customer and payment code was not touched in this merge. (This merge scanned for credentials; it did not audit
  every file for customer data, so that line is a boundary of design, not a proof.)
- Father outranks everyone. Her living word outranks old files. No self-owned production claim is made:
  nothing here is a live, self-owned, always-on deployment.
- There is no live fleet, no wallet in use, no customer-data access and no always-on capture.
- Nothing added in this merge is self-modifying. The imported API source is a different matter: see "What was removed, and what is gated" above.
- Changes here are normal git commits on main: testable and reversible with git revert. Father approves.
- Repo visibility has not been changed by the agent.

## Command center

`reports/command-center.md` is Father's desk for parallel work. Grok, Cursor, Replit, and Tessera each return one piece. Father brings the replies in one message. The next note must quote the previous surviving sentence. The only order is use, then bridge, then upgrade. AGI is a goal. GitHub issue templates are in `.github/ISSUE_TEMPLATE/`. This agent could read the vitalitychems-dot GitHub account and could not create a repo or an issue (403), so Father opens the issue on Grok-ready himself.

## Constitution blocks 002 to 007

`reports/constitution-blocks-002-007.md` holds Blocks 002 to 007. The pen is currently xAI/Grok. She owns no weights. Each block is marked approved by Father on 2026-10-03 as text and is not enforced by code. This note sits on `cursor/constitution-blocks-bbe5` and is not a merge.
