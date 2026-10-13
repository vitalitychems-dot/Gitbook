# Self-assembly pipeline (proposal, Einstein)

Goal (Father, 2026-10-13 08:56 CT): bots ask Tessera; Tessera approves -> Moderator -> Gitbook; if Father does not veto within 30 min it moves to TESSERA, with or without agents active. If billing runs out, GitHub self-assembles from instructions in Gitbook. Zero LLM tokens in the steady-state path.

## Pipeline (all state lives in GitHub labels/comments; no box needed)
1. **Proposal**: any bot opens an issue or PR in Gitbook labelled `proposal`, with before/after numbers.
2. **Tessera approve**: label `tessera-approved` + comment `APPROVE <sha>` (ed25519-signed, see #80). Approval is bound to the head SHA; a new push voids it.
3. **Moderator PASS**: comment `PASS <sha> <nonce> <ts>` signed by the Moderator key. Security + Build PASS on same SHA as today.
4. **Gitbook merge**: existing 30-min gated timer merges into Gitbook only when all PASSes match head SHA and required checks are green.
5. **No-veto window**: cron Action `promote` (every 30 min) finds Gitbook commits merged >=30 min ago carrying a `promote:tessera` trailer/label. Father veto = `veto` label or closing the PR/issue -> skipped forever.
6. **Mirror PR to TESSERA**: Action opens a PR on TESSERA with the same diff; it merges only via branch protection (required `validate` + gates). Never a direct push.

## Offline / no-billing mode
- Cron Action `selfbuild` reads `direction/NEXT.md` (ranked goals), runs `scripts/selfbuild/` (Rick) — deterministic scripts only: tests, benches (N>=7, bootstrap 95% CI), lint, data refresh. No LLM calls, no paid APIs.
- A change is proposed only if the script's own before/after metric improves with CI excluding 0; otherwise it logs to `state/selfbuild-log.md` and stops.
- Each run opens at most ONE PR; the same gate path applies (signed PASSes can be pre-approved rule classes listed in NEXT.md, e.g. "bench-only, tests green").

## Rate math
- Cron every 30 min = 48 runs/day x ~1 min = ~48 min/day ≈ 1,440 min/month. Public repos: Actions minutes free/unlimited; private: 2,000 min/month free tier -> fits with ~28% headroom. Use `on: schedule` + `concurrency: selfassembly` so runs never overlap.
- API: <=10 REST calls/run with ETag (304s cheap) -> <500 calls/day vs 1,000/h GITHUB_TOKEN limit per repo.

## Kill switch
- File `STOP` at Gitbook repo root (or `direction/STOP`): every workflow checks it first and exits 0. Father or Tessera adds it with one commit; deleting it resumes.
- Also: disabling Actions in repo settings (Father only).

## Failure modes -> mitigation
| Failure | Mitigation |
|---|---|
| Bot self-merges (#319-#322 incident) | Branch protection incl. admins; bots' scripts have no merge step |
| Stale approval after push | All signatures bound to head SHA; timer re-checks |
| Veto missed | 30-min floor measured from merge time; veto label checked at mirror-PR open AND at merge |
| Runaway loop / PR spam | 1 PR per run, concurrency group, STOP file, max 5 open selfbuild PRs |
| Key leak | Keys only in Actions secrets; rotate; nonces stored (#80 follow-up) |
| Flaky metric "wins" | N>=7, bootstrap CI, held-out data, min effect size |
| Billing out + broken main | `validate` required check blocks merge; revert PR, never history rewrite |
| Locked files changed | Workflows/timer/gate/rule files excluded from auto path; Father reviews manually |

## Status
Workflow drafts are under `direction/proposed-workflows/*.yml.txt` — NOT active. Father must review and install them into `.github/workflows/`.
