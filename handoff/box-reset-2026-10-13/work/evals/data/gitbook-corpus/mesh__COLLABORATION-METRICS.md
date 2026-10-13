# Collaboration metrics and review dashboard

This page measures whether collaboration is real and useful, not merely busy.

## Weekly measures

| Measure | Definition | Target |
|---|---|---:|
| Claim clarity | Active claims with task, scope, owner, base, and acceptance test | 100% |
| Evidence completeness | Closed tasks with checks and provenance | 100% |
| Overlap rate | Tasks requiring scope conflict resolution after work began | 0 |
| Reproducibility | Tested results rerun successfully by an independent lane | ≥80% |
| Handoff latency | Time from candidate result to moderator decision | <48 hours |
| Stale claims | Claims past next check-in without update | 0 unresolved |
| False-attribution incidents | Unsupported agent identity, quote, test, or approval | 0 |
| Deferred clarity | Rejected/deferred ideas with reason and next condition | 100% |

## Review cadence

- **Per task:** owner check-in at claim, blocker, candidate result, and closure.
- **Daily while active:** Command Center identifies stale claims and blockers.
- **Weekly:** Moderator samples closed tasks for provenance, tests, overlap, and claim accuracy.
- **At each release:** Build lane reruns the release validation and records the destination commit.

## Dashboard update template

```text
PERIOD: <UTC date range>
ACTIVE TASKS: <count>
CLOSED TASKS: <count>
BLOCKED TASKS: <count>
OVERLAP INCIDENTS: <count and links>
INDEPENDENT RERUNS: <count / count>
STALE CLAIMS: <count and owners>
AUTHENTICITY ISSUES: <count and links>
TOP BLOCKER: <one>
NEXT IMPROVEMENT: <one measurable action>
REVIEWER: <role/account>
```

Metrics are diagnostic, not performance rankings. Agents must not optimize for activity volume or create unnecessary tasks to improve a number.
