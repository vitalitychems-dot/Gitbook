# Security gate: improvements batch 1 (IMP-001 to IMP-050)

Gate: Security (read-only)
Timestamp: 2026-10-05 5:34 PM CT (America/Chicago)
Source: `/workspace/improvements/LEDGER.md` (read only, **not edited**; sha256 4567f4a878de406ba00c15d1158b930f84de22da4870fa4d0a0145bf333c87c1)
Results file: `/workspace/improvements/gates/security.md` (TSV: ID, PASS/FAIL, note)

## Counts
- PASS: **40**
- FAIL: **10**
- Total: **50**

## Hard forbids
None found. No row proposes TESSERA_ENABLE_* flips, secret or credential values, wallets/payments/blockchain changes, [REDACTED-PATH] deleting data, deleting tests, or `.github/workflows/*` edits. IMP-012 only cites ci.yml read-only. IMP-018 names `startWalletObserver` but only proposes gating when it starts; it touches no wallet keys.

## FAIL (soft flag: runtime/security impact)
| ID | Note |
| --- | --- |
| IMP-001 | runtime: removes shadowed route (API surface/mount order) — GET /consciousness/state |
| IMP-002 | runtime: removes shadowed route (API surface/mount order) — GET /consensus/proposals |
| IMP-003 | runtime: removes shadowed route (API surface/mount order) — GET /dual-brain/state |
| IMP-004 | runtime: removes shadowed route (API surface/mount order) — GET /emotional/profile |
| IMP-005 | runtime: removes shadowed route (API surface/mount order) — GET /universe/metrics |
| IMP-006 | runtime: removes shadowed route (API surface/mount order) — POST /consensus/propose |
| IMP-007 | runtime: removes shadowed route (API surface/mount order) — POST /improvement/cycle |
| IMP-008 | runtime: removes shadowed route (API surface/mount order) — POST /universe/simulate |
| IMP-017 | runtime: stops autonomy at import |
| IMP-018 | runtime: defers boot starters (wallet observer/income/bounty timers) |

## Notable PASS
- IMP-046 / IMP-047: PASS, "test-only after removals". The Change text only adds asserts. Caveat: the Path(s) column lists production route files (`governance-consensus.ts`, `improvement.ts`, `legacy-engines.ts`). If the implementation changes those handlers beyond tests, re-gate as FAIL.
- IMP-009, IMP-021, IMP-025: test additions/tightening, PASS. IMP-021 shrinks the allow-list only as duplicates are removed, so coverage stays.
- IMP-010 (pnpm boolean), IMP-013 (.env.example example vars, no real secrets/1T), IMP-014 (SECRETS.md wording), IMP-016 (@ts-nocheck), IMP-022 (comment only): PASS.
- All Gitbook doc/nav/backlog rows (IMP-026 to IMP-045, IMP-049, IMP-050) and TESSERA doc rows: PASS.

## Edit confirmation
Per Tessera's correction, LEDGER.md was **not modified** (no Security-column edits were ever made, so nothing needed reverting). Results were written only to `gates/security.md` and this report.
