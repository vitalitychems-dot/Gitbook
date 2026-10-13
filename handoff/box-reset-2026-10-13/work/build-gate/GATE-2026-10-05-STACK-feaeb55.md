# CI/Build gate — seven-package stack vs tip `feaeb558`

**Date:** 2026-10-05, ~3:40–3:42 PM CT  
**Gate:** CI/Build (verify-only). **Label: TESTED.**  
**Base tip (this gate):** `feaeb558b88df9679a45b4a03a375f58e50bcb4d` (short `feaeb55`)  
**Message:** Define Tessera Gitbook admin and bulk approval workflow  
**Parent:** `fb984add87063443043dcae7392393c2b596ce65` (HYB-012 request; Tessera; ~3:35 PM CT)  
**Packages (Father / Tessera order):** 015 → 017 → 018 → 019 → 021 → 020 v3 → 016 rev 3.1  
**Frozen hashes:** `/workspace/gitbook-cordnation/FROZEN-SHA256-1e3.txt` — all OK (`sha256sum -c`)  
**Mode:** Local disposable apply only. **No push. No remote writes. No branches created.**  
**Plan note:** Tessera intends one PR `tessera/gb-015-021-approved` (one commit per package). Father will not push himself.

---

## Overall — **FAIL** (TESTED) for full seven-stack / one-PR land

| Check | Result |
|------|--------|
| 1 Tip confirm `feaeb558` (start + final) | **PASS** |
| 1b Branch/PR `tessera/gb-015-021-approved` | **NOT FOUND** (no open PRs) |
| 2 Frozen SHA256 vs `FROZEN-SHA256-1e3.txt` | **PASS** |
| 3 Disposable feaeb55 blob-matched tree | **PASS** |
| 4 Solo `git apply --check -p1` (seven) | **4 PASS / 3 FAIL** |
| 5 Stacked apply Father order | **FAIL** (stops clean land at 017, 018, 016) |
| 6 GB-018 preserves fb984ad HYB-012 lines | **YES** (see Item 6) |
| **Overall seven-stack** | **FAIL** |

**Pushed:** nothing. **Remote writes:** none.

---

## Item 1 — Tip / open PRs / branch — **PASS tip / PR absent** (TESTED)

| When | main SHA | Message | Parent | Open PRs |
|------|----------|---------|--------|----------|
| Gate (~3:40 CT) | `feaeb558b88df9679a45b4a03a375f58e50bcb4d` | Define Tessera Gitbook admin and bulk approval workflow | `fb984ad…` | none `[]` |
| Final re-check (~3:42 CT) | `feaeb558b88df9679a45b4a03a375f58e50bcb4d` | same | `fb984ad…` | none; search `tessera gb-015` = 0 |

**Tip commit date:** 2026-10-05T20:38:23Z → **3:38:23 PM CT**  
**Branches listed:** `main`, `cursor/*`, `tessera-consolidation-draft` — **no** `tessera/gb-015-021-approved`.

**feaeb558 touched (relevant to stack):** `SUMMARY.md`, `mesh/flow.md`, `mesh/roles.md`, `mesh/roles/command-center.md`, **new** `mesh/TESSERA-GITBOOK-OPERATING-MODE.md`.  
**Did not touch:** `history/coordination/agent-checkins.md` — tip blob still `905a92c619bee042e142352b71e367ccc0eaf2ac` (= fb984ad HYB-012 content).

---

## Item 2 — Frozen SHA256 — **PASS** (TESTED)

```text
eb81d94f…fea1dffe  GB-015/GB-015.diff  OK
ca3ef700…33576d34  GB-017/GB-017.diff  OK
96d8861c…e6752664  GB-018/GB-018.diff  OK
4ecfef83…9b14eee   GB-019/GB-019.diff  OK
68bcb522…db850a    GB-021/GB-021.diff  OK
2e3b5400…062a99    GB-020/GB-020.diff  OK
af18bc3b…af23b45   GB-016/rev3/GB-016-rev3.1.diff  OK
```

---

## Item 3 — Disposable tree — **PASS** (TESTED)

**Path:** `/workspace/gitbook-gate-feaeb55`  
**Method:** seed from prior 1e3 disposable + tip-matched blobs for feaeb558 deltas; `git hash-object` vs recursive tree at `feaeb558`.  
**agent-checkins.md:** tip blob `905a92c6…` matched (HYB-012 lines present pre-apply).

All package-touched paths blob-matched (including `mesh/flow.md` `9db73946…`, `mesh/roles.md` `0b4cfe32…`, `mesh/roles/command-center.md` `d1a63a90…`, `SUMMARY.md` `d499d643…`, `mesh/TESSERA-GITBOOK-OPERATING-MODE.md` `90545f55…`).

---

## Item 4 — Solo `git apply --check -p1` — TESTED

| Package | Solo | Exit | Break reason |
|---------|------|-----:|--------------|
| **GB-015** | **PASS** | 0 | — |
| **GB-017** | **FAIL** | 1 | `mesh/flow.md`, `mesh/roles.md` — tip already rewrote frontmatter/status/CC rows that the frozen diff still searches (`corrected-pending-publish`, old CC one-liner). SUMMARY hunk alone would offset-succeed. |
| **GB-018** | **FAIL** | 1 | `history/coordination/agent-checkins.md` hunk #1 — expects `BLOCKER:…` then closing fence; tip has `WAITING ON` / `LATEST ISSUE COMMENT` between (fb984ad). Other files (SUMMARY, backlog, new decision page) would apply. |
| **GB-019** | **PASS** | 0 | — |
| **GB-021** | **PASS** | 0 | — |
| **GB-020** | **PASS** | 0 | — |
| **GB-016 rev 3.1** | **FAIL** | 1 | `mesh/flow.md`, `mesh/roles/command-center.md`, `mesh/roles.md` — same tip rewrite collision as GB-017 (expects pre-feaeb “30 minutes” / old CC row / old push-rule blockquote). |

---

## Item 5 — Stacked apply (015→017→018→019→021→020→016-rev3.1) — **FAIL** (TESTED)

| Step | Package | Exit | Notes |
|-----:|---------|-----:|-------|
| 1 | GB-015 | **0** | Applied |
| 2 | GB-017 | **1** | No partial apply (atomic fail) |
| 3 | GB-018 | **1** | Atomic fail on agent-checkins hunk #1 |
| 4 | GB-019 | **0** | Applied on tip backlog (no GB-018 backlog delta present) |
| 5 | GB-021 | **0** | Applied |
| 6 | GB-020 | **0** | Applied |
| 7 | GB-016-rev3.1 | **1** | Fail on tip-rewritten flow/roles/CC |

**Stack result:** cannot land the approved seven as one clean apply chain on `feaeb558` without rebasing 017 / 018 / 016.

Post-stack HYB-012 tip lines still present (018 never landed):

```text
NEXT CHECK-IN: 2026-10-05T21:35:39.828Z
LATEST GITBOOK BASE: main@1e3bb5009fa7fc5164b4f08ded48c1b62899b1ea
WAITING ON: Tessera maintainer / Gitbook moderator to identify the canonical checkout owner and provide next instructions
LATEST ISSUE COMMENT: https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6002431534
FOLLOW-UP: Await instructions at https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6002431534; then enable the canonical TESSERA checkout and resume the test-first route audit
```

---

## Item 6 — GB-018 vs fb984ad HYB-012 lines — **YES preserves** (TESTED)

**Precondition:** feaeb558 did **not** touch `agent-checkins.md`; tip content = fb984ad (+6/−3 HYB-012 update).

| Mode | Result |
|------|--------|
| Strict `git apply -p1` (solo/stack) | **FAIL** — entire package refused; tip HYB-012 lines unchanged |
| Diagnostic `git apply -p1 --reject` | Hunk #1 **rejected** (blank-line delete above `## HYB-012 — blocker evidence`); hunks #2–#4 **applied** (HYB-005 table row + claim blocks + trailing blank before Replit verification). |

**After --reject, all fb984ad HYB-012 tip lines still present (quoted):**

```text
NEXT CHECK-IN: 2026-10-05T21:35:39.828Z
LATEST GITBOOK BASE: main@1e3bb5009fa7fc5164b4f08ded48c1b62899b1ea
WAITING ON: Tessera maintainer / Gitbook moderator to identify the canonical checkout owner and provide next instructions
LATEST ISSUE COMMENT: https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6002431534
FOLLOW-UP: Await instructions at https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6002431534; then enable the canonical TESSERA checkout and resume the test-first route audit
```

**Explicit answer:** **YES** — GB-018 does **not** drop fb984ad HYB-012 lines. It fails because its blank-line hunk context is stale relative to those new lines; it does not overwrite them.

**Flag:** GB-018 **cannot land as frozen** on `feaeb558` until that agent-checkins hunk is rebased (drop or retarget blank-line hunk; keep HYB-005 inserts).

---

## Recommendation (Tessera one-PR / Father) — TESTED

**Do not open/merge `tessera/gb-015-021-approved` with the frozen seven as-is on `feaeb558`.**

| Package | Land on feaeb558 now? | Action |
|---------|----------------------|--------|
| GB-015 | **YES** | Apply as-is |
| GB-017 | **NO** | **Rebase** onto tip flow/roles (much already published by feaeb558); keep security.md + tessera-pen.md + non-colliding SUMMARY |
| GB-018 | **NO** | **Rebase** agent-checkins hunk #1 only; HYB-012 tip lines must stay |
| GB-019 | **YES** | Apply as-is (solo PASS; stack PASS even without 018) |
| GB-021 | **YES** | Apply as-is |
| GB-020 v3 | **YES** | Apply as-is |
| GB-016 rev 3.1 | **NO** | **Rebase** onto tip flow/roles/command-center (feaeb558 already moved CC digest wording) |

**Clean-now subset (order preserved among survivors):** **015 → 019 → 021 → 020** (skip 017/018/016 until rebased).  
**One-PR of all seven:** **blocked** until 017, 018, 016-rev3.1 are tip-rebased and re-gated.

**PR status:** branch/PR **does not exist yet** — see `/workspace/build-gate/PR-VERIFY-tessera-gb-015-021.md`.

---

## Flags (overwrite / fail)

1. **GB-017 FAIL** — would collide with feaeb558 flow/roles (not HYB-012).  
2. **GB-018 FAIL** — agent-checkins context stale vs fb984ad HYB-012; **does not overwrite** those lines.  
3. **GB-016-rev3.1 FAIL** — flow / command-center / roles collide with feaeb558.  
4. No package that successfully applies drops HYB-012 tip content.
