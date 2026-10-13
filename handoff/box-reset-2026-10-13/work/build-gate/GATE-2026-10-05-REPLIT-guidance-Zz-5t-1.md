# Build gate — Replit-guidance PRs (Zz#1, 5t#1, 1#1)

**Date:** 2026-10-05 ~6:52 PM CT
**Mode:** verify-only (Build). Nothing was pushed, merged, commented on GitHub, cloned, flag-flipped, LEDGER-edited, or messaged to Tessera/Father.
**Method:** cursor-github MCP (`get_pull_request`, `list_pull_request_files`, `list_check_runs_for_ref`, `get_file_contents`, `get_commit`, `get_issue`).
**Context:** Father decision 6:44 PM CT 2026-10-05 — no paid Replit connector; Replit agents sync via GitHub/Gitbook. These PRs add Tessera mesh guidance for Replit agents.

**Gitbook tip (re-checked):** `cdc95b76232ee066d6c55d0531b02d88426f4beb` (unchanged from earlier PR-12 postmerge tip).

---

## OVERALL: PASS (TESTED) — all three

| PR | Verdict | Head (full) | Base | Docs-only | Gitbook links | mergeable_state | CI |
|---|---|---|---|---|---|---|---|
| Zz#1 | **PASS** | `7935a4cdc524461290fa64fec2dd06f221d6d391` | `main` @ `6e64ca612e450cf30eb924162ca76f771deee44d` | yes | 2 checked, 0 broken | clean (mergeable=true) | none (OK) |
| 5t#1 | **PASS** | `a267efa588a9ab0d4ca7566065f9daab9d222c9a` | `main` @ `ea874b7a391ce6d207038215700ce97101114884` | yes | 2 checked, 0 broken | clean (mergeable=true) | none (OK) |
| 1#1 | **PASS** | `71a8876e90751484f83c28144e097a09a0d2be00` | `subrepl-nftoz8d7` @ `7de2b4a778ec62f084e92dd4ed5a3e9be35e45ab` | yes | 2 checked, 0 broken | clean (mergeable=true) | none (OK) |

All three are **draft=true**. Content and mergeability PASS; undraft before merge.

---

## 1. vitalitychems-dot/Zz pull/1 — PASS (TESTED)

- **URL:** https://github.com/vitalitychems-dot/Zz/pull/1
- **Title:** Replit agent guidance: Gitbook start-here, PR-only, status on issue #2
- **Body summary:** Command Center adds Tessera mesh rules for Replit agents (Gitbook start-here, PR-only, status on Gitbook issue #2, stop committing once work lands in TESSERA/Gitbook). Aligns with Father's no-paid-connector decision.
- **State:** open, **draft=true**, not merged; commits=1; +19/−1; changed_files=2
- **Head SHA (pin):** `7935a4cdc524461290fa64fec2dd06f221d6d391` (`cc/replit-agent-guidance`)
- **Base:** `main` @ `6e64ca612e450cf30eb924162ca76f771deee44d`
- **mergeable:** true · **rebaseable:** true · **mergeable_state:** `clean` (test merge `0d5558e2bf34e351e24b3759aa3822faf45d2816`)

### Files changed
| File | Status | +/- | Notes |
|---|---|---|---|
| `AGENTS.md` | modified | +10/−1 | Appends "Tessera mesh rules for Replit agents" section |
| `replit.md` | modified | +9/−0 | Same guidance block |

**docs-only: yes** — markdown/guidance only. No code, workflows, lockfiles, secrets, wallets, ENABLE flips.

### Hard limits
- No [REDACTED-PATH] secrets / credential dumps (text *warns against* reading/committing [REDACTED-PATH] / natal-vault.json).
- No wallets/payments.
- No `.github/workflows`.
- PASS.

### Gitbook links (unique targets in PR patches)
1. `https://github.com/vitalitychems-dot/Gitbook/blob/main/mesh/replit-agents-start-here.md` — `get_file_contents` on `mesh/replit-agents-start-here.md` @ Gitbook `main` (**tip cdc95b76**) → **exists** (GB-028 Replit start-here).
2. `https://github.com/vitalitychems-dot/Gitbook/issues/2` — `get_issue` → **exists**, open ("Tessera hybrid consolidation agent conference").

**Gitbook links: 2 checked, 0 broken.**

### CI / "nothing breaks"
- `list_check_runs_for_ref` on head → total_count=0.
- Docs-only with no CI is OK. Content PASS.

---

## 2. vitalitychems-dot/5t pull/1 — PASS (TESTED)

- **URL:** https://github.com/vitalitychems-dot/5t/pull/1
- **Title:** Replit agent guidance: Gitbook start-here, PR-only, status on issue #2
- **Body summary:** Same Command Center / Father no-paid-connector guidance as Zz#1.
- **State:** open, **draft=true**, not merged; commits=1; +18/−1; changed_files=2
- **Head SHA (pin):** `a267efa588a9ab0d4ca7566065f9daab9d222c9a` (`cc/replit-agent-guidance`)
- **Base:** `main` @ `ea874b7a391ce6d207038215700ce97101114884`
- **mergeable:** true · **rebaseable:** true · **mergeable_state:** `clean` (test merge `a1bc75a84de44add7c0b3f7b1f024f1711ee72b3`)

### Files changed
| File | Status | +/- | Notes |
|---|---|---|---|
| `AGENTS.md` | **added** | +8/−0 | New file; mesh rules only |
| `replit.md` | modified | +10/−1 | Appends same guidance block |

**docs-only: yes.**

### Hard limits
- Same advisory-only vault wording; no secrets/wallets/workflows/ENABLE. PASS.

### Gitbook links
Same two unique targets as Zz#1; both resolve on tip cdc95b76 / issue #2 open.
**Gitbook links: 2 checked, 0 broken.**

### CI
- Head check runs: 0. Docs-only OK.

---

## 3. vitalitychems-dot/1 pull/1 — PASS (TESTED)

- **URL:** https://github.com/vitalitychems-dot/1/pull/1
- **Title:** Replit agent guidance: Gitbook start-here, PR-only, status on issue #2
- **Body summary:** Same Command Center / Father no-paid-connector guidance.
- **State:** open, **draft=true**, not merged; commits=1; +18/−1; changed_files=2
- **Head SHA (pin):** `71a8876e90751484f83c28144e097a09a0d2be00` (`cc/replit-agent-guidance`)
- **Base (claimed & confirmed):** `subrepl-nftoz8d7` @ `7de2b4a778ec62f084e92dd4ed5a3e9be35e45ab` (not main; default_branch of repo is still `main`)
- **mergeable:** true · **rebaseable:** true · **mergeable_state:** `clean` (test merge `358198e8634079e6fed29e62158db6796549b143`)

### Files changed
| File | Status | +/- | Notes |
|---|---|---|---|
| `AGENTS.md` | **added** | +8/−0 | New file; mesh rules only |
| `replit.md` | modified | +10/−1 | Appends same guidance block |

**docs-only: yes.**

### Hard limits
- Same as above. PASS.

### Gitbook links
Same two unique targets; both resolve.
**Gitbook links: 2 checked, 0 broken.**

### CI
- Head check runs: 0. Docs-only OK.

### Base-branch note
Base `subrepl-nftoz8d7` matches the claimed Replit working branch. Merge lands guidance on that branch, not necessarily on `main`. Callers should expect a follow-up if guidance must also exist on `main`.

---

## Shared content check (all three)

Guidance block (substance identical across repos):
1. Read Gitbook start-here + issue #2; check latest main commits/open PRs.
2. Branches/PRs only; never push to main/default.
3. Status on Gitbook issue #2 with `AGENT: <name>`.
4. Stop committing to old repo once work lands in TESSERA/Gitbook.
5. Do not read/modify/commit [REDACTED-PATH] natal-vault.json, or personal data.

Aligns with Father's 6:44 PM CT decision and the live start-here page on Gitbook main.

---

## Merge advice (one sentence)

All three PASS TESTED as docs-only guidance with clean mergeability and 0 broken Gitbook links — undraft then merge (1#1 into `subrepl-nftoz8d7` as intended; Zz/5t into `main`) after Father/Tessera gate yes; no CI required.

**Report path:** `/workspace/build-gate/GATE-2026-10-05-REPLIT-guidance-Zz-5t-1.md`
