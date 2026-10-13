# Gitbook free CI: (a) self-hosted runner vs (b) box script — 2026-10-13 (CT)

## Measured: (b) `run.sh`, DRY-RUN, 16 open PRs
- Shared bare blobless clone `/workspace/repos/Gitbook` (5.0 GB, already holds the blobs that were fetched). Fetches only `refs/pull/N/head`.
- Sparse worktree per SHA (`*.json *.jsonl *.py /tools/ /mesh/`, excluding archive/history), removed right after.
- Script: `ci-check.sh` pinned from PR #87 @ a1d2d74e (`ci-check.pinned.sh`). The PR's own copy is never used.

| metric | run 1 (cold, 16 PRs) | run 2 (all cached) |
|---|---|---|
| wall time | 57 s total, 1.3–5.6 s per PR (median ~3.5 s) | 0.5 s total, 0 s per PR |
| peak disk per PR | ~36 MB (worktree; up to 94 MB on #73), freed after | 0 |
| GitHub API calls | 1 (list PRs) + 0 per PR in dry run (+1 per PR live = 17) | 1 total |
| git fetches | 1 per PR | 0 |
| tokens | 0 (plain bash) | 0 |

Results (WOULD post `gitbook-ci`):
- success: #87 86 85 84 83 82 81 80 79 78 76 66
- failure: #74 and #73 (invalid JSON committed: `handoff/.../FULLPICTURE-LOADED.json` and `mesh/rick-workspace/.../health.json`), #40 and #39 (their base predates `tools/shepherd`, so they need a rebase).

Lesson: a full worktree checkout was ~6 GB per PR and pushed the disk to 96%. Sparse checkout cut that to 36 MB (about 170× smaller).

## Comparison
| | (a) self-hosted Actions runner | (b) box script |
|---|---|---|
| cost | free (private repos) | free |
| disk | ~0.6–1 GB for the runner and its bundled node, plus a full `_work` checkout per job (~6 GB for this repo unless the workflow is sparse) | 36 MB per PR, transient; shares the existing clone |
| idle CPU/RAM | long-poll daemon, ~50–100 MB RSS, always on | none (cron or one-shot) |
| setup | repo-admin registration token, a service, updates | one script, already built |
| security | runs workflow and PR code on the shared box, with the runner's token in its environment. GitHub warns against self-hosted runners on any repo where PRs aren't fully trusted. Agents write the PRs here. | still runs PR code (python tests) on the box. Mitigations: pinned trusted script, timeout 300, no token in the child env is still TODO (gh creds sit in ~/.config). A sandbox (`bwrap`, or a separate user with no `~/.config/gh`) should be added before going live. |
| native UI and required checks | yes | yes, through a commit status |

## Trust (same gap as #71)
A `gitbook-ci` status posted with Father's token is self-attested: anyone or any agent holding that token can post "success". Recommendation:
1. Treat `gitbook-ci` as **advisory now**. Gates re-run `run.sh` or check `runs.tsv`; they don't trust the status alone.
2. Later, make it **required, but accepted only from a separate bot identity** (a GitHub App or machine user whose token the agents can't read), and have the gate check the status `creator`.
3. Post `pending` first, and include the pinned script SHA in the description.

## Recommendation
Go with **(b)**. It costs zero tokens and ~36 MB of disk transiently, and repeat runs are near zero. Add the sandbox before going live. Reject (a) for now: more disk, an always-on daemon, the same untrusted-code risk, and it needs an admin token.

## Run live (only after approval)
    cd /workspace/ops/gitbook-ci && LIVE=1 ./run.sh
For cron: `*/10 * * * * cd /workspace/ops/gitbook-ci && LIVE=1 ./run.sh >>live.log 2>&1`
Note: SHAs already cached from the dry run are skipped. Run `rm cache.tsv` first so the first live pass posts statuses for all of them.
