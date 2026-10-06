# 20-item execution board

**Status:** Active coordination board
**Source:** `AGI-COLLABORATION-IMPROVEMENT-ROADMAP.md`
**Rule:** Analysis is not implementation. A task is `DONE` only with an attributable commit, checks, provenance, limitations, and review.

| ID | Workstream | Current status | Next owner | Evidence / next gate |
|---|---|---|---|---|
| AGI-01 | Shared world model | **IMPLEMENTED — Gitbook slice** | Gitbook Moderator | Validate `state/validate_world_model.py`; refresh on repo drift |
| AGI-02 | Provenance-aware memory | **IMPLEMENTED — Gitbook contract slice** | Gitbook Moderator | Validate `provenance-memory/validate_records.py`; TESSERA API phase deferred |
| AGI-03 | Task decomposition planner | **ANALYSIS COMPLETE** | TESSERA | Owner recorded: TESSERA (TESSERA ruling 2026-10-06). Still requires schema/migration decision, isolated PostgreSQL, and tests |
| AGI-04 | Skill routing | **PROPOSED** | Pen / Moderator | Claim one task; use skill matrix evidence |
| AGI-05 | Cross-agent handoffs | **EXISTING POLICY** | Gitbook / Cordnation | Apply playbook handoff packet and collect independent resumption evidence |
| AGI-06 | Independent verification | **PROPOSED** | Build lane | Define second-run protocol and record a reproduction |
| AGI-07 | Self-critique/red-team | **PROPOSED** | Moderator | Add critique section to proposal submissions |
| AGI-08 | Evidence confidence | **EXISTING POLICY** | Moderator | Normalize status vocabulary across records |
| AGI-09 | Safe tool planning | **PROPOSED** | Operations lane | Produce dry-run/rollback template |
| AGI-10 | Deterministic experiments | **PROPOSED** | TESSERA research lane | Define seed/environment/metric fixture |
| AGI-11 | Regression benchmarks | **PROPOSED** | Build lane | Select first route/UI/history benchmark |
| AGI-12 | Conflict resolution | **EXISTING POLICY** | Moderator | Exercise overlap and contradictory-instruction scenario |
| AGI-13 | Debate-to-decision forum | **EXISTING POLICY** | Gitbook forum | Link one idea to one task and decision |
| AGI-14 | Capability registry | **PROPOSED** | Tessera / Pen | Define capability-vs-goal record schema |
| AGI-15 | Repository drift detection | **PROPOSED** | Release steward | Add repeatable link/head/status check |
| AGI-16 | Dependency/license governance | **EXISTING POLICY** | TESSERA maintainer | Apply to next dependency or upstream adapter |
| AGI-17 | Learning from failures | **PROPOSED** | Gitbook / Cordnation | Add searchable lesson record for the stopped 20-agent run |
| AGI-18 | Multi-agent role evaluation | **PROPOSED** | Research lane | Define controlled scenarios and scoring |
| AGI-19 | Human approval boundaries | **EXISTING POLICY** | Human owner / Moderator | Preserve explicit yes/no/revise and merge gates |
| AGI-20 | Bulk digest execution | **EXISTING POLICY** | Tessera Grok bot / Command Center | Publish 30–45 minute digest with exact bases and checks |

## Run interruption record

The approved 20-workstream orchestration run produced three report files (`AGI-01`, `AGI-02`, and `AGI-03`) before stopping. The remaining workstreams are **not** marked complete and have no fabricated agent responses. Their reports must be generated or completed by declared agents under the normal claim lock.

## Immediate sequence

1. Moderator verifies the new AGI-01 and AGI-02 validators.
2. Gitbook records one owner for AGI-03 before any TESSERA schema/API edit. Recorded 2026-10-06: the AGI-03 owner is TESSERA (TESSERA ruling).
3. Build independently reruns the validators.
4. Command Center includes these exact commits and checks in the next bulk digest.
5. Father decides `yes`, `no`, or `revise`; no TESSERA code is claimed from analysis alone.
