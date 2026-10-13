# mesh-status (Einstein, 2026-10-13)

Builds `mesh/STATUS.md` from repo files only. It makes no network calls and uses 0 model tokens.
`status.py` is Rick's base. `status2.py` adds the following:
- queue vs handoff contradictions for GB/HYB/SITE ids, including archived rows
- an enforced 6h claim lease, with naive timestamps reported instead of crashing
- completeness checks (I6 fix)
- ownerless rows listed first
- REPORTED count
- gate column
- token ledger sum
- lane lint against `mesh/lanes.json`

`tools.py` covers index build, delta, legend, one-line handoff, lane slice, hygiene, archive of done rows, and the redacted summary.

    python3 tools/mesh-status/status2.py . --out mesh/STATUS.md

The scheduled GitHub Action is intentionally not included (Actions billing).
Box test results: see the Einstein report (30 checks, 24 pass).
