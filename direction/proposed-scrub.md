# Proposed rule-scrub spec (PROPOSAL ONLY: not a gate file and not installed)

**Input:** an issue body (an idea) or a PR diff and body. **Output:** JSON `{verdict: PASS|FAIL, reasons: [], input_sha256}`. The script is deterministic: no LLM and no network beyond reading the issue or PR.

## Checks (all must pass)
1. **Hard limits**: FAIL on any `TESSERA_ENABLE` change, a deletion of others' files, a force-push or history rewrite, a wallet or payment, the 1T vault, a repo other than TESSERA or Gitbook, or any mention of `collink1007` used as an account.
2. **Secrets and private data**: gitleaks-style regexes (tokens such as `gh[pousr]_`, `AKIA`, private-key headers, `.env` contents) plus high-entropy strings; email or phone patterns outside noreply addresses; paths under `/workspace/secrets`.
3. **Locked paths**: FAIL if `.github/**`, workflow or timer files, `gate/**`, `tools/gate/**` or rule files are touched; the list is read from the written rules file.
4. **Metric present**: the body has a `Before:` and an `After:` line with a number and a unit (tokens, ms, bytes, %, calls/day).
5. **Speed-claim statistics**: if the body claims a speedup (`\d+(\.\d+)?x|faster|speedup`), it must also state `N=\d+` with N≥7 and a CI given as `[lo, hi]` or `95% CI`.
6. **Size**: the diff is at most 400 changed lines, and there is at most 1 open idea-lane PR per author.
7. **Author**: commits come from `332565808+vitalitychems-dot@users.noreply.github.com` or an approved bot identity.

## Behavior
- Any failure → FAIL with every reason listed. An ambiguous result counts as FAIL.
- The result is posted as a comment. Signing it (ed25519, #80) is optional until keys exist.
- Tests: fixtures for each check, both PASS and FAIL, plus a replay of past Moderator verdicts. The target is ≥95% agreement with Moderator, and 0 false PASS on known FAILs.
