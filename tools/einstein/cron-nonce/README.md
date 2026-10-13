# Unpredictable gate cron timing + nonce-bound PASS (Gitbook #72, for Security)

**Entropy:** the runner OS CSPRNG via Python `secrets` only. Nothing is derived from commit SHA, wall time or `run_id`, since all three are public or guessable.

**Jitter:** an Actions cron at a fixed coarse slot (e.g. `*/30`), then `sleep $(python3 -c 'import cron_nonce as c;print(c.jitter(N, TIMEOUT_S))')`. `jitter` is uniform over `[0, min(N, timeout-60s))` and raises an error if the cap is ≤ 0, so the job can never time out from its own sleep.

**Nonce:** 128-bit `secrets.token_hex(16)`. The signed message is `PASS <sha> <nonce> <ts>` (ed25519, one key per gate). The verifier:
- checks the SHA equals the head being merged;
- requires ts within `[now-TTL, now+60s]`;
- rejects a nonce already seen;
- checks the signature against pinned public keys;
- drops seen-nonces older than TTL, so memory is bounded.

**Tests** (`python3 test_cron_nonce.py`, 13 tests, 5/5 runs OK). 10k draws, N=600:

| Run | chi² (20 bins, df 19; crit 43.8 @ p=.001) | lag-1 serial r (bound 0.04) | Next-bin predictor hit rate (chance 0.050) |
|---|---|---|---|
| 1 | 27.3 | 0.0174 | 0.0467 |
| 2 | 12.5 | 0.0063 | 0.0452 |
| 3 | 23.0 | -0.0014 | 0.0482 |
| 4 | 22.7 | 0.0055 | 0.0549 |
| 5 | 17.7 | -0.0060 | 0.0504 |

- Replay, wrong-SHA, forged key, tampered nonce and stale ts are all rejected; a valid PASS is accepted.
- **Limits:** the statistical tests detect gross bias only; the security comes from the CSPRNG itself. Key pinning and CODEOWNERS locking of the pubkey file are Tessera's #71 work; not touched here.
