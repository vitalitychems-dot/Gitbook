# Security gate: TESSERA PR #1 (HYB-005 braces audit ignore)

**Date:** 2026-10-05, ~5:02 PM CT  
**Gate:** Security (read-only; change nothing; never print secrets)  
**Repo:** `vitalitychems-dot/TESSERA` (`private:true`)  
**PR:** https://github.com/vitalitychems-dot/TESSERA/pull/1  
**Receipt head:** `76716c22d79085e1eb72c1e33ea9471b1c43103d` — **MATCHES** live PR head  
**Base:** `main` @ `fec56eb09d19907832663d5f16fcbc24f3d00317`  
**Branch:** `cursor/hyb-005-audit-ignore-943c`  
**Standing decision:** HYB-005 ACCEPTED + MITIGATED (Security-owned); staged Gitbook `merge/hyb-005-braces-decision.md`; merged via Gitbook PR #6 as `97e43fb`. Review date 2026-11-05; remove when braces ≥3.0.4 ships.  
**Mode:** Read-only via cursor-github (`get_pull_request`, `list_pull_request_files`, `get_pull_request_diff`, `get_commit`, `list_commits`). No repo mutation.

---

## Verdict

| Item | Verdict | One line |
|------|---------|----------|
| **TESSERA PR #1 @ 76716c22** | **PASS** | Scope is only a single-GHSA `pnpm` audit ignore for `GHSA-vfj7-8cjw-p6xm`; matches locked HYB-005; no secrets / 1T / ENABLE flips; PR path; all 3 commits SSH-verified Cursor Agent + Tessera co-author. |

**MECH FLAG:** none  
**Father wake:** not required (PASS; no material risk beyond accepted HYB-005)

---

## 1. Scope / files

| Field | Value | Label |
|-------|-------|-------|
| `changed_files` | **1** | TESTED |
| `additions` / `deletions` | **+8 / −0** | TESTED |
| File | `pnpm-workspace.yaml` only | TESTED |
| Diff content | Adds `auditConfig.ignoreGhsas: [GHSA-vfj7-8cjw-p6xm]` + HYB-005 comments (advisory URL, transitive path, review date 2026-11-05, remove when braces ≥3.0.4) | TESTED |
| Workflows / lockfiles / app code / env | **unchanged** | TESTED |
| Broad ignore / `ignoreRCs` / level downgrade | **absent** — single GHSA ID only | TESTED |

Unified diff (entire PR):

```diff
+# HYB-005: braces <=3.0.3 has no patched release yet.
+# Advisory: https://github.com/advisories/GHSA-vfj7-8cjw-p6xm
+# Transitive path: artifacts/mockup-sandbox > fast-glob > micromatch > braces.
+# Review date: 2026-11-05. Remove this ignore once braces >=3.0.4 ships.
+auditConfig:
+  ignoreGhsas:
+    - GHSA-vfj7-8cjw-p6xm
```

**Scope check:** PASS — only the locked HYB-005 mitigation surface.

---

## 2. What the ignore suppresses (check 1)

| Field | Value |
|-------|-------|
| Advisory | `GHSA-vfj7-8cjw-p6xm` (= CVE-2026-93687) |
| Package / versions | `braces` through `3.0.3` (affected `< 3.0.4`) |
| Class | Stack-exhaustion **DoS** (recursive AST walkers lack depth guards; deeply nested brace patterns → uncaught `RangeError` / process crash) |
| CVSS (public advisories) | ~7.5 (High) — availability impact; network, no privileges, no user interaction |
| Transitive path (PR + HYB-005) | `artifacts/mockup-sandbox` → `fast-glob` → `micromatch` → `braces@3.0.3` |
| Exploitability in this path | Requires attacker-controlled deeply nested brace *patterns* fed into braces; mockup-sandbox / fast-glob usage is build/tooling globbing, not an open untrusted-pattern API surface on the production path. Residual risk accepted under standing HYB-005. |
| Patched release | Standing decision + PR state: no braces ≥3.0.4 yet; ignore is temporary until it ships |
| Narrow vs hiding real vuln | **Justified narrow exception.** Pins **one** GHSA ID via `ignoreGhsas`. Does **not** disable `pnpm audit`, lower severity threshold, or ignore all advisories. Other findings still fail CI. Aligns 1:1 with locked Security HYB-005 ACCEPTED+MITIGATED. |

**Ignore check:** PASS — justified / narrow; not a blanket hide.

---

## 3. Secrets / 1T / ENABLE flips (check 2)

| Check | Result | Label |
|-------|--------|-------|
| Secrets / credentials / tokens / private keys in diff | **none** (YAML comments + auditConfig only) | TESTED |
| 1T / one-time / ephemeral secret paths | **none** | TESTED |
| `TESSERA_ENABLE_*` flipped to on / true / 1 | **none** — no ENABLE keys touched | TESTED |
| `.env*` / secret store / CI secrets config | **unchanged** | TESTED |
| Workflow privilege / permissions expansion | **none** (no workflow files) | TESTED |

**Secrets/1T/ENABLE check:** PASS

---

## 4. Commit provenance (check 3)

PR reports `commits: 3`. All three are on the PR branch ahead of `main` (parent of first = base `fec56eb0…`).

| SHA (short) | When (CT) | Author / committer | Verification | Files | Role |
|-------------|-----------|--------------------|--------------|-------|------|
| `6fc8a694` | 2026-10-05 2:21 PM CT | Cursor Agent `<cursoragent@cursor.com>` / same; Co-authored-by Tessera | **SSH signature verified** (`verified:true`, `reason:valid`) | `pnpm-workspace.yaml` +8/−0 | substantive (adds ignore) |
| `53856e22` | 2026-10-05 2:38 PM CT | Cursor Agent / same; Co-authored-by Tessera | **SSH verified** | empty (0/0) | CI retrigger only |
| `76716c22` (head) | 2026-10-05 4:57 PM CT | Cursor Agent / same; Co-authored-by Tessera | **SSH verified** | empty (0/0) | CI retrigger only |

| Provenance field | Result |
|------------------|--------|
| Path | **PR #1** → `main` (not direct push to main). `mergeable_state: clean`. |
| PR opener | `vitalitychems-dot` (OWNER) |
| Head SHA vs receipt | **exact match** `76716c22d79085e1eb72c1e33ea9471b1c43103d` |
| Tree after substantive commit | unchanged by empty retriggers (`tree` `38e69808…` identical across all 3) |
| Unsigned / foreign / unexpected authors on PR commits | **none** |
| Direct-to-main | **no** |

**Provenance check:** PASS — agent-authored via PR path; all commits SSH-valid; head matches receipt.

---

## 5. Alignment with standing HYB-005

| Standing requirement | PR implements |
|----------------------|---------------|
| ACCEPTED + MITIGATED | Yes — ignore only, no other change |
| Narrow audit ignore only | Yes — single `GHSA-vfj7-8cjw-p6xm` |
| braces@3.0.3 via mockup-sandbox→fast-glob→micromatch | Path documented in comment |
| Review date 2026-11-05 | Present in comment |
| Remove when braces ≥3.0.4 | Present in comment |
| Security owns HYB-005 | Gate confirms implementation matches decision; no reopen |

---

## 6. Tessera paste (ready)

```
Security gate TESSERA PR #1 @ 76716c22 — PASS
Receipt head matches. Scope: pnpm-workspace.yaml only (+8/−0) — auditConfig.ignoreGhsas: [GHSA-vfj7-8cjw-p6xm] only.
Ignore: suppresses braces≤3.0.3 stack-exhaustion DoS (GHSA-vfj7-8cjw-p6xm / CVE-2026-93687) on mockup-sandbox→fast-glob→micromatch→braces. Justified NARROW (single GHSA; audit still runs). Matches locked HYB-005 ACCEPTED+MITIGATED (review 2026-11-05; remove when braces≥3.0.4).
Secrets/1T/ENABLE: none.
Provenance: PR path (not direct main); 3 commits all Cursor Agent SSH-verified + Tessera co-author; 1 substantive + 2 empty CI retriggers.
Report: /workspace/security-gate/GATE-TESSERA-PR1-HYB005-76716c22.md
Father wake: not required (PASS).
```

---

## 7. Father wake

**Not required.** Verdict is PASS with no material risk beyond the already-locked HYB-005 acceptance. Father merge decision can proceed on Security PASS + remaining gates.

---

## Method notes

- Tools: cursor-github `get_pull_request`, `list_pull_request_files`, `get_pull_request_diff`, `get_commit` (head + both parents), `list_commits` on branch `cursor/hyb-005-audit-ignore-943c`.
- Advisory context: public GHSA/CVE summaries (DoS / stack exhaustion); no exploit steps reproduced.
- No secrets printed. No repo writes. No merges.
