# Cursor ↔ GitHub sync check (read-only), checked Mon Oct 12 2026 about 6:45 PM CT

Scope: vitalitychems-dot/TESSERA and vitalitychems-dot/Gitbook. Read through the cursor-github connector only. Nothing was pushed, commented on, merged, deleted or launched.

## BLOCKED: cloud agent lookup
The CloudAgent tool (list/get) isn't available in this executor. GetDynamicTools shows no CloudAgent or agent namespace. Because of that, every agent-state claim below is REPORTED or UNKNOWN. The parent agent should run `CloudAgent list scope:all` and `get` for bc-26260d7a and bc-12653339.

## 1. Main SHAs
| Repo | main SHA | Label |
|---|---|---|
| TESSERA | f76d648462f85dceaa447c532e0b885869ec7822 (Oct 12, 6:30 PM CT, "Turn the 3D studio floor on by default") | TESTED |
| Gitbook | 2344334e689ad8fdfc9b5c7848aa8f1fdeac6afb (Oct 12, 5:18 PM CT, merge of PR #50 o11-secure-mesh-doc) | TESTED |

- TESSERA PR #241 is **merged** (merged_at 2026-10-12 6:30 PM CT), and its merge commit is f76d6484, which is the current tip of main. Head branch: cursor/studio-3d-floor-3a81. The PR body links to bc-26260d7a-5e88-5a66-b198-b89c60053a81. TESTED.
- bc-26260d7a: **MATCH** with the reported last merge (f76d6484, PR #241). The GitHub side is TESTED. The agent's own current state is unknown (no CloudAgent access).

## 2. bc-12653339 (GitAI, in progress): UNKNOWN
- No PR on either repo references bc-12653339 (search_pull_requests returned 0 results). No PR titled "GitAI" on TESSERA. TESTED.
- Candidate branch: TESSERA `cursor/gitbook-ai` (tip 0c636a3a) exists, and so does TESSERA `cursor/gitbook-mcp-connector-301f` (e898111a). Nothing links either branch to bc-12653339. UNKNOWN.
- Branch, ahead/behind count, pushed or unpushed: UNKNOWN. This needs CloudAgent get to name the branch. The connector has no compare call for counting commits ahead or behind.

## 3. Open PRs (ages in days measured from Oct 12, 6:40 PM CT; all authored by vitalitychems-dot)
| Repo | # | Title | Head | Created d | Updated d | Draft | Mergeable | Linked agent | Stale |
|---|---|---|---|---|---|---|---|---|---|
| TESSERA | 194 | Point the docs at the Gitbook consolidation map | desk/consolidation-pointer | 0 | 0 | no | unknown (GitHub still computing) | – | no |
| TESSERA | 110 | SITE-002: gate remaining diagnostics behind owner session | cursor/site-002-diagnostics-gate-7ea3 | 2 | 2 | no | unknown | – (cursor/ branch) | no* |
| TESSERA | 87 | Gate system-runtime and shadow-winning admin routes | security/gate-system-runtime-and-shadow-winners | 3 | 2 | yes | unknown | bc-5dbf29a1 | no* |
| TESSERA | 82 | Allow api-server to boot without a database | fix/api-server-db-optional-boot | 3 | 2 | no | unknown | bc-465db0f1 | no* |
| TESSERA | 80 | Add an opt-in loopback pen with deterministic gates | feat/local-pen-adapter | 3 | 3 | no | unknown | bc-746dd5ed | no* |
| Gitbook | 45 | GB-063: HYB-011 refresh and GitbookAI rules | desk/gb-063-hyb-011 | 0 | 0 | no | clean | – | no |
| Gitbook | 40 | Record Father's yes and the drill already on TESSERA | cursor/father-yes-record-b14e | 3 | 3 | yes | **dirty (conflicting)** | bc-01a122c3 | **YES (conflicts)** |
| Gitbook | 39 | GB-061 rev 2: archive/preserved preservation pack | ready/gb-061-rev2-archive-preserved | 3 | 3 | no | clean | bc-c73eee5c | no |
\* None is 7 or more days old. The TESSERA PRs are based on older main SHAs (7f46d3b7, 26f4b6d0, 4ca91b31, 797e0191), so they're behind main, but GitHub reported their mergeability as "unknown". Conflict status: UNKNOWN. All TESTED except where marked unknown.

## 4. Flagged branches (TESTED that they exist; whether they're merged into main is UNKNOWN)
- TESSERA has about 251 branches, about 170 of them `cursor/*`. Gitbook has 61 branches, 19 of them `cursor/*`. Only 3 of the cursor/* branches have open PRs. Checking every branch for whether it's merged was out of reach without a compare call.
- TESSERA `cursor/v2-0xx-*-3a81` series (V2-001 through V2-062, plus studio-3d-floor-3a81): these are bc-26260d7a's branches, judging by the -3a81 suffix that matches the agent id ending ...3a81. The PRs for #241 and V2-061/062 are merged into main, and the remaining branches are still on GitHub. Probably merged leftovers. UNKNOWN until compared.
- Gitbook `cursor/chamber-desk-sync-bf31` and `chamber-desk-sync-bf31` both point at the same commit 9bd972c7 (a duplicate branch). No open PR.
- Gitbook `cursor/father-yes-record-b14e` (PR #40): open draft and conflicting.
- Unpushed agent branches: UNKNOWN (needs CloudAgent).
- Note: TESSERA also has `tessera-v2-stage1`, `replit-agent` and several `security/*` branches with no open PR. I didn't check them.
