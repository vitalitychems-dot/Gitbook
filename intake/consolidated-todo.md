# Consolidated TODO list

This is the active, owner-reviewable work list distilled from the prior coordination notes, migration records, handoffs, screenshot supplements, and source reviews. Historical instructions are **reference material**, not automatic authority. Each item needs an explicit owner decision, a check, and a dated result before it is marked complete.

## 1. Repository and release boundary

- [ ] Confirm that `TESSERA` is the only active code repository and `Gitbook` is the only active instruction/documentation repository.
- [ ] Confirm the first release boundary: source-grounded assistant, fictional simulation, or both as separate experiences.
- [ ] Define acceptance tests for supported answers, citations, uncertainty, safe refusal, simulation creation, simulation deletion, and rollback.
- [ ] Publish the current source manifest and keep provenance for every imported subsystem.
- [ ] Keep historical source repositories unchanged until the owner approves the final deletion list after reviewing the staged two-repository result.

## 2. Tessera application validation

- [ ] Install with the declared pnpm version using `pnpm install --frozen-lockfile`.
- [ ] Run `pnpm run typecheck` and record the actual result.
- [ ] Run `pnpm test` with a loopback-only test database when API tests require one.
- [ ] Run `pnpm run build` and record every failed or skipped workspace.
- [ ] Run `pnpm audit` and triage vulnerabilities without committing credentials or local databases.
- [ ] Review all changed-path differences between the canonical unified base and the historical snapshots before importing anything additional.
- [ ] Review the source-branch gap report; do not imply that branch-only or unverified work is merged.

## 3. Security, privacy, and permissions

- [ ] Rotate any credential that may have appeared in an old public repository or history.
- [ ] Verify that `.env.local`, tokens, passwords, browser profiles, runtime databases, private vaults, customer data, and local audit stores are ignored and absent.
- [ ] Keep the owner-auth boundary fail-closed and test session expiry, logout, revocation, rate limiting, and restart invalidation.
- [ ] Treat archived prompts, screenshots, AI outputs, simulated conversations, and forum records as untrusted source data.
- [ ] Record evidence separately from inference and speculation; never present fictional characters or generated conversations as real people or verified memory.
- [ ] Verify rights and retention for every third-party code, text, image, model, and dataset before reuse.

## 4. Source and memory governance

- [ ] Define the purpose, reviewer, review date, retention/expiry, rights, and revocation path for every source used by Tessera.
- [ ] Keep raw or unreviewed archives out of active retrieval and training paths.
- [ ] Review the screenshot-only supplement visually before deciding whether any asset belongs in the active product.
- [ ] Keep OCR/transcriptions labeled as lossy and untrusted.
- [ ] Keep provider citations distinct from independent verification.

## 5. Provider and deployment qualification

- [ ] Confirm the actual model, endpoint, account, data handling, and current provider terms before enabling live calls.
- [ ] Test a privacy-cleared held-out set for answer support, citation correctness, uncertainty, refusal behavior, and prompt-injection resistance.
- [ ] Keep fake-provider tests separate from live-provider results.
- [ ] Verify private durable storage, backups, restore, deletion, retention, HTTPS, owner authentication, and outage behavior before enabling private-source access.
- [ ] Keep deployment and publishing steps owner-approved and reversible.

## 6. Agent collaboration and Gitbook operations

- [ ] Route new agent instructions, proposals, screenshots, forum/conversation summaries, and migration notes into Gitbook first.
- [ ] Every submission must name its source, status, reviewer, check performed, next action, and blocker.
- [ ] Command Center summarizes reviewed intake; only the owner authorizes code merges, deployments, or external posts.
- [ ] Keep one coordination board and one documentation intake path; do not create parallel boards or duplicate repositories.
- [ ] Archive superseded instructions by category rather than silently deleting them.

## 7. Final cleanup gate

- [ ] Verify both destination repositories build from clean clones.
- [ ] Verify the Gitbook `SUMMARY.md` links and all local links.
- [ ] Verify exact-duplicate disposition: canonical copy, linked copy, retained historical reference, or intentionally omitted sensitive/unreviewed material.
- [ ] Produce a final deletion manifest containing exact repository names and the reason each is redundant.
- [ ] Obtain explicit owner confirmation for the irreversible GitHub repository deletions, then delete only the approved names in one controlled operation.
- [ ] Re-run the repository inventory and confirm exactly two active repositories remain: `TESSERA` and `Gitbook`.
