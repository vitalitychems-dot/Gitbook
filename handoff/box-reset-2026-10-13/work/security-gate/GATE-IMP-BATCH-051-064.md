# Security gate: improvements batch 2 (IMP-051 to IMP-064)

Gate: Security (read-only, append-only)
Timestamp: 2026-10-05 5:37 PM CT (America/Chicago)
Source: `/workspace/improvements/LEDGER.md` (read only, **not edited**; sha256 dfa2043ffb87db5950cdd77b824e4f661d4bd935884505061b533aa6d182dcea, mtime 2026-10-05 17:36:02 CT, same before and after this gate)
Results file: `/workspace/improvements/gates/security.md` (TSV: ID, PASS/FAIL, note). 14 lines appended after IMP-050. Lines 1–50 are byte-identical to before.

## Counts (IMP-051 to IMP-064)
- PASS: **6**
- FAIL: **8**
- Total: **14**

Overall file: 64 data lines (IMP-001 to IMP-064, in order, no duplicates). PASS 46 / FAIL 18.

## Hard forbids
None found in 051–064. No row proposes TESSERA_ENABLE_* flips, committing secret values, wallets/payments/blockchain, opening or touching the [REDACTED-PATH] deleting data or tests, or `.github/workflows/*` edits. IMP-054 says "secrets manager only (never commit values)" and "no TESSERA_ENABLE_* flips". IMP-061 says no workflow edit without a separate yes. IMP-064 says 1T is forbidden.

## FAIL: held out of batch (Tessera attention list)
| ID | Note |
| --- | --- |
| IMP-052 | needs Father yes: Ollama/local model install |
| IMP-053 | needs Father yes: paid industry suite spend (~$1–5 smoke / ~$30 Aider / $50–500+ SWE-Lite) |
| IMP-054 | needs Father yes: provider keys / SOVEREIGN_NO_EXTERNAL_LLM=0. Never commit values; using a secrets manager is the right process, but the row stays FAIL until Father says yes |
| IMP-055 | needs Father yes: Cortical Labs product answers |
| IMP-056 | needs Father yes: storefront retention boundary |
| IMP-057 | needs Father yes: quantum dual-route product ruling (do not silently delete routes) |
| IMP-058 | runtime: new Gitbook RAG retrieval path (read-only still expands surface) |
| IMP-063 | needs Father yes: Origin connector reconnect/grant |

## PASS
| ID | Note |
| --- | --- |
| IMP-051 | honesty: eval harness JSON; forbids calling homemade quizzes MMLU; no external spend in this row alone |
| IMP-059 | honesty: rename/relabel homemade quiz (not MMLU) |
| IMP-060 | test: assert/log registration count |
| IMP-061 | scripts/ merge-gate only; no workflow edit |
| IMP-062 | docs: competitor score card (cited, honest) |
| IMP-064 | privacy recheck of archives; 1T forbidden |

Caveats: IMP-051 runs only homemade or offline suites until IMP-053 and IMP-054 get Father yes. If it starts calling an external LLM or spending money, re-gate it. If IMP-061 needs a CI hook later, the workflow edit needs its own Father yes.

## Edit confirmation
LEDGER.md was not modified. Its sha256 was different when batch 1 ran (4567f4a8…) because the ledger was updated after batch 1 (rows 051–064 now exist). Security did not make that change, and the hash was already dfa2043f… when this gate started. This gate only appended to `gates/security.md` and created this report.
