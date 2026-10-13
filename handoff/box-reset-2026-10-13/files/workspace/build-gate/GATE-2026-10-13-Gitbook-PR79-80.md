# Build gate — vitalitychems-dot/Gitbook PR #79 + #80 — 2026-10-13 ~7:23 AM CT

Verify-only. No push, merge, GitHub comment, or agent messaging.

## Verdicts

| PR | Head (full) | Claim | TESTED | Verdict |
|---|---|---|---|---|
| #79 | `6e9b0e49d16297533e0282be90812b81d1ec2684` | 5 tests | 5/5 OK | **PASS** |
| #80 | `ea0e43188260e003715f193030f51fa616c5c50d` | 13 tests | 13/13 OK | **PASS** |

Heads pinned at start and re-checked at end — both unmoved (FAIL-if-moved OK).

## Shared context
- Current main tip (at gate end): `aa9506f59aa724dd2ae2f24dd8a78b0079e27638`
- PR bases (both): `75b5ffcccf2a029ccb2257c18677b3c4dadfd40a` — main has moved +7 commits past base; heads diverge (ahead 3 / behind 7) but both are pure adds under new paths
- Method: GitHub API blobs + patches into `/tmp/gb-pr79`, `/tmp/gb-pr80`; deleted after. No full clone.
- Stack overlap #79↔#80: **none** (distinct `tools/einstein/quiet-backoff/` vs `tools/einstein/cron-nonce/`)

---

## PR #79 — einstein/quiet-backoff (quiet-backoff gate timer)

- Branch: `einstein/quiet-backoff` @ `6e9b0e49d16297533e0282be90812b81d1ec2684` (3 commits; +42/−0; 3 files)
- Mergeable: true, mergeable_state=clean, rebaseable=true (GitHub API, REPORTED)
- Files (all new):
  - `tools/einstein/quiet-backoff/quiet_backoff.py`
  - `tools/einstein/quiet-backoff/test_quiet_backoff.py`
  - `tools/einstein/quiet-backoff/README.md`

### TESTED
- Head pin: OK (still `6e9b0e49…`)
- `git apply --check` of PR diff into empty tree (pure adds): **rc=0**
- Real apply produced the 3 expected paths
- Unit tests (`python3 test_quiet_backoff.py -v`, stdlib only): **Ran 5 tests … OK**
  - test_new_sha_runs, test_not_due_skips, test_backoff_caps, test_push_resets, test_latency_bounded
  - Matches claim of 5 tests
- gitleaks (`/workspace/pubscan/gitleaks` + `gl.toml`) on source tree: **0 findings**
- rg secret / `TESSERA_ENABLE_*` patterns: **0 hits**
- Commit emails (ae1e4db8, 47c41a09, 6e9b0e49): author+committer `332565808+vitalitychems-dot@users.noreply.github.com` — noreply OK
- Relative markdown links: **0** (README has none)
- README metrics table: 4 data/header rows × 3 columns, consistent; not an intake/ledger table (12-col / ID rules N/A)
- SUMMARY.md: PR does not touch it; no `tools/einstein` nav entry on main (same class as other tools-only PRs)

### REPORTED
- CI check-runs on head: total_count=0. Combined status: pending, statuses=[]. Gitbook has no Actions on these heads (Einstein: "Gitbook has no CI, so your test run is the check"). Not treated as FAIL.
- `python -m unittest discover` breaks because `unittest.main()` runs at import time (SystemExit 5). Documented run path `python3 test_quiet_backoff.py` works; not a FAIL.
- Compare vs current main: status=diverged, ahead_by=3, behind_by=7; mergeable_state still clean (no path collision with intervening main commits under `tools/` which currently has check_handoff.py, qlab, shepherd only).

### Blob sha256 (TESTED)
- README.md → `67144a0f63a0874f0dd8a84394b91b13775b82809b9b18ce8cdffab846e5052c`
- quiet_backoff.py → `d192adbe68a8071133891fe4a6a7196b1db3f04a679b1c75ad6e87e1e20b11ea`
- test_quiet_backoff.py → `53659b3ae188e943cbb6d1bd16fc8269275089a3e0ef6a990ddc21c34889e764`

---

## PR #80 — einstein/cron-nonce (CSPRNG jitter + nonce-bound PASS)

- Branch: `einstein/cron-nonce` @ `ea0e43188260e003715f193030f51fa616c5c50d` (3 commits; +91/−0; 3 files)
- Mergeable: true, mergeable_state=clean, rebaseable=true (GitHub API, REPORTED)
- Files (all new):
  - `tools/einstein/cron-nonce/cron_nonce.py`
  - `tools/einstein/cron-nonce/test_cron_nonce.py`
  - `tools/einstein/cron-nonce/README.md`

### TESTED
- Head pin: OK (still `ea0e4318…`)
- `git apply --check` of PR diff into empty tree (pure adds): **rc=0**
- Real apply produced the 3 expected paths
- Unit tests (`/tmp/gb-gate/venv80` with `cryptography>=42`; `python3 test_cron_nonce.py -v`): **Ran 13 tests … OK**
  - Rand (6): test_range, test_cap_below_timeout, test_chi2_uniform, test_serial_corr, test_unpredictable, test_nonce_128bit_unique
  - Pass (7): test_valid, test_replay, test_wrong_sha, test_forged_key, test_tampered, test_stale, test_ttl_expiry_frees_memory
  - Matches claim of 13 tests
- gitleaks: **0 findings**
- rg secret / `TESSERA_ENABLE_*` patterns: **0 hits**
- Commit emails (9df426da, d017c273, ea0e4318): author+committer `332565808+vitalitychems-dot@users.noreply.github.com` — noreply OK
- Relative markdown links: **0**
- README stats table: 6 rows × 4 columns, consistent; not intake/ledger (12-col / ID rules N/A)
- SUMMARY.md: untouched; no `tools/einstein` nav entry

### REPORTED
- CI check-runs on head: total_count=0. Combined status: pending. Same no-CI class as #79. Not FAIL.
- Runtime dependency: `cryptography` (ed25519) required; not declared via requirements.txt / pyproject in this PR. Gate installed it in an isolated venv. Tests pass with cryptography present; without it import fails. Not a content FAIL; Security may want a pinned dep file.
- `unittest.main()` at import breaks discover (same as #79); documented `python3 test_cron_nonce.py` OK.
- Compare vs current main: diverged ahead 3 / behind 7; mergeable_state clean.
- No private keys or seed material in tree (keys generated in-test via `Ed25519PrivateKey.generate()`).

### Blob sha256 (TESTED)
- README.md → `34b02a817195aec789a18b7730e18b7cf39c37df63c5b0de5a36234bb1891595`
- cron_nonce.py → `db9331424fa7f92c0f36e238b0e696865104ace256cb97c926c8156d4f0be2d8`
- test_cron_nonce.py → `30db108da099840cb6252df44a67578b46e338e766932d2272beb1459e83be7e`

---

## Not done
- Push, merge, GitHub comment, agent messaging (out of scope per task).
- Did not re-run the PR #80 5×10k statistical table (claim already covered by the 13 unit tests including chi² / serial / predictor bounds in one 10k draw).

---

## Re-gate PR #79 rev2 — 2026-10-13 ~7:28 AM CT

**Verdict: PASS @ head `83af942e4c663e5e23e7a3c2423a30504eddd277`** (verify-only; not merged/commented)

- Prior PASS was @ `6e9b0e49…` (5/5). This head is rev2 (ETag default; claim **8 tests**).
- Branch: `einstein/quiet-backoff` @ `83af942e4c663e5e23e7a3c2423a30504eddd277` (4 commits; +96/−0; 6 files)
- PR base still `75b5ffcc…`; current main tip `aa9506f59aa724dd2ae2f24dd8a78b0079e27638` (diverged ahead 4 / behind 7)
- Mergeable: true, mergeable_state=clean, rebaseable=true (REPORTED)
- Method: GitHub API blobs into `/tmp/gb-pr79r2`; deleted after. No full clone.
- Head pinned at start and end — unmoved (FAIL-if-moved OK).

### Files (all new; 404 on main tip)
- `tools/einstein/quiet-backoff/quiet_backoff.py`
- `tools/einstein/quiet-backoff/test_quiet_backoff.py`
- `tools/einstein/quiet-backoff/replay.py`
- `tools/einstein/quiet-backoff/README.md`
- `tools/einstein/quiet-backoff/data/pushes.txt.zst` (601 lines decompressed; claim match)
- `tools/einstein/quiet-backoff/data/ci_runs.tsv.zst` (700 lines decompressed; claim match)

### TESTED
- Head pin: OK (still `83af942e…`)
- All 6 paths absent on main tip (HTTP 404) — pure adds
- Text-file `git apply --check` (binary hunks stripped from API diff): **rc=0**
- Git blob SHA1 of all 6 local files match API tree SHAs
- Full PR `git apply --check --binary` on GitHub media-type diff: **FAIL** (API binary patches lack full index lines — tooling limit, not a merge conflict). Mergeable_state=clean + path 404s used as apply-to-main evidence.
- Unit tests (`python3 -m unittest test_quiet_backoff -v`, stdlib + system `zstd`): **Ran 8 tests … OK**
  - test_new_etag_runs, test_304_idles, test_same_etag_200_idles, test_default_no_backoff_latency_equals_base, test_optional_backoff_caps, test_change_resets, test_not_due_skips, test_replay_data_reproduces
  - Matches claim of 8 tests
- zstd integrity: both `.zst` files decompress OK (`zstd -t`)
- gitleaks (`/workspace/pubscan/gitleaks` + `gl.toml`): **0 findings**
- rg secret / `TESSERA_ENABLE_*`: **0 hits**
- Commit emails: ae1e4db8 / 47c41a09 / 6e9b0e49 → `332565808+vitalitychems-dot@users.noreply.github.com`; 83af942e → `einstein@users.noreply.github.com` — all noreply OK
- Relative markdown links: **0**
- README metrics table: 7 rows × 5 columns, consistent; not intake/ledger (12-col / ID rules N/A)
- SUMMARY.md: PR does not touch it; no `tools/einstein` nav entry

### REPORTED
- CI check-runs on head: total_count=0. Combined status: pending. Gitbook no-CI class; not FAIL.
- API unified-diff binary apply tooling gap noted above; GitHub mergeability clean.

### Blob sha256 (TESTED)
- README.md → `2f566f0d7c3a7c7d7a17d23f4e3fc0b8bcefa0bfcb407c1a2a400329e32f4c88`
- quiet_backoff.py → `4fdd45902a8c29ffd9f21f55672a0792107ea4d7467d82c4e9047458ff07101e`
- replay.py → `b375579335d838729ba69298e5cd1c48cf4224f9553f9f3de00191d47a77f355`
- test_quiet_backoff.py → `849d8be5e41496f72468c54b94aab75783f64e8b55b27428713ee295cd8fc12f`
- data/pushes.txt.zst → `746c0b5729574cb157626ca022b794165df941abf3aa479ed535c73264c901e6`
- data/ci_runs.tsv.zst → `f8b737faafc6a64e29790cc3a1059a78a287fcb8ef544c8b572f478d73a44094`

### Not done
- Push, merge, GitHub comment, agent messaging (out of scope).

---

## Gate PR #88 (supersedes #79) — 2026-10-13 ~7:46 AM CT

**Verdict: PASS @ head `ce184f3bab8b64ebcbb3322859c69565abc6df09`** (verify-only; not merged/commented)

- Branch: `einstein/quiet-backoff-v2` @ `ce184f3bab8b64ebcbb3322859c69565abc6df09` (1 commit; +694/−0; 5 files)
- PR base = current main tip: `aa9506f59aa724dd2ae2f24dd8a78b0079e27638`
- Mergeable: true, mergeable_state=clean, rebaseable=true (REPORTED)
- Method: GitHub API blobs into `/tmp/gb-pr88`; deleted after. No full clone.
- Head pinned at start and end — unmoved (FAIL-if-moved OK).
- Supersedes #79 @ `83af942e4c663e5e23e7a3c2423a30504eddd277` (prior Build PASS rev2).

### Files (all new; 404 on main tip)
- `tools/einstein/quiet-backoff/quiet_backoff.py`
- `tools/einstein/quiet-backoff/test_quiet_backoff.py`
- `tools/einstein/quiet-backoff/replay.py`
- `tools/einstein/quiet-backoff/README.md`
- `tools/einstein/quiet-backoff/data/pushes.txt` (601 lines)

### Diff vs #79 @ `83af942e…` (quiet-backoff tree only; TESTED)
| Path | Change |
|---|---|
| `quiet_backoff.py` | **identical** (git blob `a88721ed…`) |
| `test_quiet_backoff.py` | **identical** (git blob `11b04d36…`) |
| `replay.py` | dropped `subprocess`/`zstd` load; reads plain `data/pushes.txt` via `open()` |
| `README.md` | data bullets: `pushes.txt.zst` + `ci_runs.tsv.zst` → `pushes.txt` only; metrics table unchanged |
| `data/pushes.txt` | **new plain text**; byte-identical to `zstd -dc` of #79's `pushes.txt.zst` (601 lines) |
| `data/pushes.txt.zst` | **removed** |
| `data/ci_runs.tsv.zst` | **removed** (unused by code; Security ask per PR body) |
| commits / email | #88 is single commit; author+committer `332565808+vitalitychems-dot@users.noreply.github.com` (vs #79 rev2 tip using `einstein@users.noreply.github.com`) |

Logic and claimed metrics unchanged: full checks 288.1 → 31.8/day (−89%); mean latency 2.51 [2.40, 2.63] min = baseline.

### TESTED
- Head pin: OK (still `ce184f3b…`)
- All 5 paths absent on main tip (HTTP 404) — pure adds
- `git apply --check` of full PR diff (all text; no binary): **rc=0**; real apply produced the 5 expected paths
- Git blob SHA1 of all 5 local files match API tree SHAs
- Unit tests (`python3 -m unittest test_quiet_backoff -v`, stdlib only — no zstd): **Ran 8 tests … OK**
  - same 8 names as #79 rev2 (incl. `test_replay_data_reproduces`)
  - Matches claim of 8 tests
  - Note: `ResourceWarning: unclosed file` from `replay.load` (`open(...).read()` without context manager) — warning only, not a failure
- gitleaks (`/workspace/pubscan/gitleaks` + `gl.toml`): **0 findings**
- rg secret / `TESSERA_ENABLE_*`: **0 hits**
- Commit email (ce184f3b): author+committer noreply OK
- Relative markdown links: **0**
- README metrics table: 7 rows × 5 columns, consistent; not intake/ledger
- SUMMARY.md: untouched; no `tools/einstein` nav entry

### REPORTED
- CI check-runs on head: total_count=0. Combined status: pending. Gitbook no-CI class; not FAIL.

### Blob sha256 (TESTED)
- README.md → `13beb67f3c2cdfd71e50109659062f8945bb4d9b74a88c3f739921c7f433fc61`
- quiet_backoff.py → `4fdd45902a8c29ffd9f21f55672a0792107ea4d7467d82c4e9047458ff07101e`
- replay.py → `4458ee8dc4d632279cc20b8fc02aecc754d8ffa276012100b7f9ae192d02f2e4`
- test_quiet_backoff.py → `849d8be5e41496f72468c54b94aab75783f64e8b55b27428713ee295cd8fc12f`
- data/pushes.txt → `ee829b3db93a0f64035912706985710967c4ea83c1323f6fad96703a326bf782`

### Not done
- Push, merge, GitHub comment, agent messaging (out of scope).
