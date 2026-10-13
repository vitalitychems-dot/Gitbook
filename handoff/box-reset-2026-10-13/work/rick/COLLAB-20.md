# COLLAB-20: inventions for mesh communication, collaboration and task order (proposals)

Lanes: Tessera, Command Center, Mesh Cloud, Security, Build, Gitbook Moderator, Gitbook Cordnation, Rick. Gate order: Moderator > Tessera > Security > CI/Build > Father. Every item below is a proposal. Another lane implements and tests it, and it lands only through a gated Gitbook PR.

| # | Invention | First runnable step | Test |
|---|---|---|---|
| 1 | **Mesh bus** (BUILT): typed JSONL envelopes in `mesh/bus/YYYY-MM-DD.jsonl` | `python3 tools/collab/bus.py validate sample-bus.jsonl` | Rejects zoneless ts, % without evidence, non-owner BLOCK and non-Tessera→Father messages (unit test) |
| 2 | **Gate-aware scheduler** (BUILT): critical-path order over the dependency and gate chain | `python3 tools/collab/sched.py sample-tasks.json` | Every dependency finishes before its dependents start, gates stay in order, makespan ≤ FIFO |
| 3 | **Claim-conflict detector** (BUILT): IDs or paths claimed by 2+ lanes | `python3 tools/collab/conflict.py /workspace/gitbook-cordnation` | Synthetic double claim is flagged; path prefix overlap is flagged |
| 4 | Lane digest: per-lane "your next action" view built from the bus | `bus.py digest FILE --lane security` | Only refs owned by that lane, or waiting at its gate, are shown |
| 5 | Handoff card: required fields (state, next step, blockers, evidence links) | `kind:"handoff"` schema check in bus.py | Missing `next`/`evidence` → reject |
| 6 | Forum digest: issue #2 comments → one bus `note` per lane per day | Read-only `gh api` dump → jsonl | Count of digests equals the count of active lanes |
| 7 | Gate SLA timer: flags items waiting at one gate for more than N hours | `digest` plus a `last` age check | Fixture item 7h old at Security → flagged |
| 8 | Lane heartbeat: a `note` with `kind:"pulse"` every 45 min | Cron line that appends a pulse | Missing pulse for 2 periods → "silent lane" warning |
| 9 | Ask-router: an `ask` goes to the lane whose role file matches best (palace search over roles/) | `palace.py search "<ask>"` limited to roles/ | 10 hand-labelled asks: top-1 lane matches the label |
| 10 | Dedup guard: refuse a new task whose title matches an open one (palace bm25) | Score new title against open refs | Near-duplicate fixture scores above the threshold |
| 11 | Evidence linker: every `result` must cite a file:line or a commit | Regex check in the validator | A result without a citation → reject |
| 12 | Snapshot pruner advice: find the same file in base/proposed/gate clones | Hash md files across clones | Identical hashes grouped; never deletes |
| 13 | Token budget meter: per-lane token spend per day vs the 20k idle cap | Sum `tokens` field per lane | Over-cap fixture → warning to Tessera |
| 14 | Father-ask queue: only Tessera sends, batched, one card each | FATHER-ASKS.md ← bus `ask to:father` via Tessera | A non-Tessera sender is rejected (already in bus.py) |
| 15 | Replay sandbox: re-run a day's bus to reproduce the state at time T | `digest` with `--until T` | Digest at T equals the stored snapshot |
| 16 | Skill-matrix matcher: assign work by AGENT-SKILL-MATRIX plus current load | Parse matrix and score (skill, idle) | Assignments never exceed one step per lane |
| 17 | Merge-order planner: topo-sort PRs by touched paths and dependencies | Reuse sched.py with PRs as tasks | No two PRs that touch the same path are scheduled in parallel |
| 18 | Honesty lint: flags unmeasured %, "BUILT" without proof, and disguised review tasks | Grep rules over a PR diff | Commit 3b3840c3 pattern ("does not label") is flagged |
| 19 | Memory-graph diff: graph.json before and after a PR shows new or lost links | `graph.py` on two DBs, then diff edges | Removed doc → its edges listed as lost |
| 20 | Retro card: weekly metrics (median gate wait, conflicts, silent lanes) | Aggregate from bus files | Matches a hand count on the fixture week |

## Prototype results (tools/collab/, 5/5 tests pass)
- bus: the 5-message fixture → 2 bad lines caught, with all 4 rule classes (Father routing, zoneless ts, unauthorised BLOCK, % without evidence). The digest gives `collab-bus: owner=rick next_gate=tessera`.
- sched: on 9 real pending items (PR55, IDLE-MODE r2, disk cleanup, v3 graph/plan...), the critical-path makespan is **25 vs 32 for FIFO** (−22% in simulated time units; the costs are my estimates, not measurements). It also prints the next step for each lane.
- conflict: mesh/ (2,904 lines) → 0. gitbook-cordnation (24,615 lines) → 7 flagged; a hand check found about 1 real (precision ≈ 1/7). Text heuristics are weak, so use the structured bus (#1) as the source of truth.
