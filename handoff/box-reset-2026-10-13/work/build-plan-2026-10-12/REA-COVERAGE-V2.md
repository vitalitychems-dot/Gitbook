# REA coverage — v2 full suite (2026-10-12 CT)
Tool: `npx -y rea-agents@6.4.0 analyze-javascript-application`
Gitbook stage excluded `1T` and `*vault*` paths. Zz `imports/trees` present in staged tree.

| Target | Relevant JS | Parsed | Coverage |
|---|---:|---:|---:|
| GitMesh | 9 | 7 | 77.8% |
| Gitbook-full | 1186 | 1006 | 84.8% |
| TESSERA | 1431 | 1367 | 95.5% |
| Zz | 137 | 115 | 83.9% |
| amber | 178 | 147 | 82.6% |
| vitality | 716 | 692 | 96.6% |

JSON artifacts: `/workspace/rea-batch/v2-rea-out/<name>.json`

## Round 3 (18:28–18:32 CT), read-only
| Target | Relevant | Parsed | Coverage |
|---|---:|---:|---:|
| TESSERA @f6c9362 (post-v2, fresh shallow clone) | 2715 | 2456 | 90.5% |
| fleet-moss-monarch-rapid | 219 | 207 | 94.5% |
| amber (b3 re-run) | 178 | 147 | 82.6% (no change) |
| XXX (b3) | 1936 | 1740 | 89.9% |
| TheTesseractAI/18 (b3) | 2668 | 1605 | 60.2% |
| T44 | 52 | 52 | 100% |
| olive (local) | 65 | 48 | 73.8% |
The gap between relevant and parsed is files REA counts but doesn't parse as JS (json/html/assets). REA reported 0 parse failures. That means 100% of the parseable JS was parsed, and the remaining % is non-JS files. Vault, 1T and natal paths were skipped.
TESSERA baseline (MEASURED 18:2x CT): artifacts/v2 45/45 tests pass in 1.49 s; V2-051 fixture = 10 tokens.
