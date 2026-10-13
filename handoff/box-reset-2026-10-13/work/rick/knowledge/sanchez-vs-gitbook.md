# Rick (TESSERA server) vs Gitbook mesh/RICK.md — static audit
Gitbook main: 3fc9d8966f78424419d1768f300e86088c4e9abd (mesh/RICK.md)
TESSERA main: dfca510e6891630fcc3978ce0bad21bab72ada8b
Method: shallow clone, read/grep only. Nothing run, nothing posted. All paths exist at expected locations. Line numbers are REPORTED from static read.
Rules: (R1) only measured numbers; (R2) Rick proposes, never approves/implements/spawns; (R3) only Tessera messages Father.

## A. Unmeasured numbers / expected-impact (R1) — 9
| file:line | issue | fix |
|---|---|---|
| lib/rick-proposals.ts:170 | template expectedImpact "+12 within 2 weeks; ~1-2 points" | replace with "UNMEASURED — test: <metric> before/after" |
| lib/rick-proposals.ts:190 | "grounding above 90% within a week" | same |
| lib/rick-proposals.ts:207 | "above 90%… free ~30% budget" | same |
| lib/rick-proposals.ts:225 | "5-10% recall latency drop" | same |
| lib/rick-proposals.ts:326 (+254-255) | LLM prompt requires expectedImpact; proposal rejected without it | rename field to `testPlan` (metric + pass line); forbid numeric forecasts in prompt; drop from required check |
| lib/rick-sanchez-agent.ts:337,348,359,370,381,392,403,414 | hardcoded invention expectedImpact "25-35%", "10x", "40-60%", "70-85%", "40%" etc. | strip numbers → "UNMEASURED"; add test plan |
| lib/rick-sanchez-agent.ts:454 | "EXPECTED IMPACT" injected into council proposal text | send test plan instead |
| routes/rick.ts:251 | submit-custom defaults expectedImpact "Unknown" (ok) but passes user forecasts through | label as UNMEASURED |
| routes/rick.ts:54 | comment "V2-RICK (100% approval)" unmeasured claim | remove % or cite run |
(Also lib/rick-improvement-program.ts:355,625 echo expectedImpact into dispatch body/reflections → label UNMEASURED.)

## B. Self-approve / mark-implemented (R2) — 7
| file:line | issue | fix |
|---|---|---|
| lib/rick-proposals.ts:441-446 approveProposal | Rick module sets state "approved" | move to gate module; require approver != rick, record approver id |
| lib/rick-proposals.ts:466-471 markImplemented | Rick marks own work implemented | require implementer lane + passed test ref |
| routes/rick.ts:115 POST /rick/proposals/:id/approve | approval under Rick namespace, no auth/approver | remove or move to /gate/* with Tessera auth |
| routes/rick.ts:138 POST /rick/proposals/:id/implemented | same | require testRef + non-Rick actor |
| routes/rick.ts:971 improvement-program decision | approve/reject under Rick | gate-auth, approver != rick |
| routes/rick.ts:985 + lib/rick-improvement-program.ts:366-420 dispatch | Rick dispatches tasks (writes .local/dispatched-tasks) | Rick can only emit proposal; dispatch by another lane |
| routes/rick.ts:995,1030 dispatch-status/task-queue PATCH | Rick routes set "completed" | completion only with failing/passing test evidence from implementer |
(lib/rick-sanchez-agent.ts:459-473: auto-celebrates council approval "exactly as predicted" — cosmetic; lib/rick-improvement-program.ts:284 advance gate fine.)

## C. Meeseeks / spawning (R2) — 4
| file:line | issue | fix |
|---|---|---|
| routes/rick.ts:709-729 POST /rick/meeseeks/spawn | spawns agents as "rick-sanchez-c137" | delete route or 403; spawning belongs to Tessera |
| routes/rick.ts:752,769 complete/result | Rick closes Meeseeks | move off Rick namespace |
| lib/rick-proposals.ts:169,189,206 | proposal text tells system to schedule/auto-spawn Meeseeks | reword as proposal to Tessera, no auto-spawn |
| lib/rick-sanchez-agent.ts:712 | static activity "Mandated Meeseeks Task Spawner Protocol" | remove fabricated feed entry |

## D. Ungated autonomous loops (R2) — 3
| file:line | issue | fix |
|---|---|---|
| app.ts:598 → lib/rick-autonomous-loop.ts:379-385 | 240s loop runs at boot, no flag | gate behind TESSERA_ENABLE_RICK_LOOP (default 0) |
| lib/rick-autonomous-loop.ts:~340-370 tick | inserts inventions to DB + ledger without review | write to pending-review only |
| lib/rick-autonomous-loop.ts:304 | mints new categories autonomously | require approval |
(routes/rick.ts:105, 241, 961 generate/submit routes are proposal-only: OK if outputs land pending-review.)

## E. Messaging Father (R3) — 0
No father/sendTo/notify path found in the five files. lib/rick-sanchez-agent.ts:452 submits to council (createProposal) — not Father, but auto-submission should be gated.

## Fabricated data
lib/rick-sanchez-agent.ts:~705-715 static "activity" feed ("Patent Filed… approved by Grand Council") — presents unmeasured history as fact; remove or label demo.

Total: 23 (A9 B7 C4 D3 E0)
