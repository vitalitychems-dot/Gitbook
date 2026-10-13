# Provenance investigation: HYB-012 direct-to-main commits

**Repo:** vitalitychems-dot/Gitbook (private)  
**Mode:** READ-ONLY (no push, revert, comment, clone, or mutation)  
**Window:** ~2026-10-05 19:39–19:48 UTC (2:39–2:48 PM CT)  
**Investigator timebase:** America/Chicago (CT = UTC-5)  
**Report written:** 2026-10-05 ~2:55 PM CT

---

## Verdict: **FLAG**

**One-line:** FLAG — four unsigned, no-PR, direct-to-main Gitbook ledger commits were pushed via the owner GitHub user `vitalitychems-dot` (strong Replit-connected-account evidence; not Manus Connector / not Cursor App), with spoofable git author `Tessera <vitalitychems@gmail.com>`; patches touch only `history/coordination/agent-checkins.md` and contain **no** [REDACTED-PATH] contents or secrets.

**Did anything from 1T appear committed?** **NO** — only path/worktree *references* and explicit non-access claims (`no 1T access`, `protected 1T`, `No protected vault files were opened`). No vault dumps, credentials, customer data, or private-key material in any of the four patches or the cumulative tree delta.

---

## (1) Push / actor identity

### Per-commit metadata (GitHub Commits API)

| Short | Full SHA | Message | Author (git) | Committer (git) | Author/Committer date (UTC) | CT | Verification | Parent | GitHub user (author+committer) |
|---|---|---|---|---|---|---|---|---|---|
| `0af00a1` | `0af00a1bd86c9f490f81410ae14ee40e02b0b19f` | Claim HYB-012 route audit | Tessera \<vitalitychems@gmail.com\> | Tessera \<vitalitychems@gmail.com\> | 2026-10-05T19:39:58Z | 2:39:58 PM CT | **unsigned** (`verified:false`, `reason:unsigned`, signature/payload null) | `d5bd5fd45410d78808ba2af4f49e91ecec78e730` | `vitalitychems-dot` (User id 332565808) |
| `cc720d3` | `cc720d3d0bacb2a6d5863d2051c67cb8ec534cc1` | Update active HYB-012 check-in with route collision evidence | same | same | 2026-10-05T19:44:27Z | 2:44:27 PM CT | unsigned | `0af00a1…` | same |
| `527ee36` | `527ee3687533f5df848f62cd68dd621b3666e951` | Record HYB-012 blocker and verified duplicate route evidence | same | same | 2026-10-05T19:46:48Z | 2:46:48 PM CT | unsigned | `cc720d3…` | same |
| `95993af` | `95993aff649703cf79eb12a2103299781aa8eecf` | docs: record HYB-012 canonical static verification | same | same | 2026-10-05T19:48:26Z | 2:48:26 PM CT | unsigned | `527ee36…` | same |

HTML URLs:
- https://github.com/vitalitychems-dot/Gitbook/commit/0af00a1bd86c9f490f81410ae14ee40e02b0b19f
- https://github.com/vitalitychems-dot/Gitbook/commit/cc720d3d0bacb2a6d5863d2051c67cb8ec534cc1
- https://github.com/vitalitychems-dot/Gitbook/commit/527ee3687533f5df848f62cd68dd621b3666e951
- https://github.com/vitalitychems-dot/Gitbook/commit/95993aff649703cf79eb12a2103299781aa8eecf

**Author vs committer:** identical on every commit (no GitHub `noreply` / `web-flow` / bot committer rewrite).  
**GitHub account type:** `User` (not `Bot`). No deploy-key identity is visible on the commit objects themselves (API does not expose which credential pushed).

### Spoofable git identity (explicit)

Git `author`/`committer` string **`Tessera <vitalitychems@gmail.com>` is not cryptographic proof of Tessera**. Anyone with a push credential can set `user.name` / `user.email`. The email is Father’s known address; the display name conflicts with the bodies’ self-identification as **Replit**. Treat the Tessera git name as **untrusted / spoofable config**, not as Tessera-bot authorship.

### App / token markers (strongest available evidence)

| Actor hypothesis | Evidence |
|---|---|
| **Manus Connector** | **Ruled out for these commits’ companion Issue #2 posts.** Earlier Issue #2 comments (e.g. launch) carry `performed_via_github_app.slug = manus-connector`. The five HYB-012-window comments below all have **`performed_via_github_app: null`**. |
| **Cursor GitHub App** | **Ruled out for these posts.** Multiple earlier Security/Tessera Admin comments carry `performed_via_github_app.slug = cursor`. HYB-012-window comments do **not**. |
| **GitHub web UI (`web-flow`)** | No `web-flow` committer; author=committer=Tessera email; unlikely. |
| **Replit via connected owner GitHub account** | **Best fit.** Bodies repeatedly claim Replit; HTML marker `<!-- replit-hyb012-static-verification-2026-10-05 -->`; Issue comments timed to the second with commits; `performed_via_github_app: null` (typical of PAT/OAuth user token, not App installation events); self-quote: *“Replit Agent collaborator via the connected owner GitHub account; not a separate GitHub identity”*. |
| **Father (Collin) local push** | Possible in the abstract (same GitHub user + email), but contemporaneous Issue #2 text self-attributes to Replit and describes a Replit worktree pointing at protected 1T — consistent with Replit session using the owner OAuth/PAT, not a separate Father digest-yes push. |
| **Tessera bots** | Git name says Tessera, but bodies deny being Tessera and claim Replit; unsigned; no Tessera-bot GitHub login. |

### Issue #2 comments locked to the same second as commits

All as `user: vitalitychems-dot`, `author_association: OWNER`, **`performed_via_github_app: null`**:

| Comment id | Created (UTC) | Aligns with | Self-label |
|---|---|---|---|
| 6001698692 | 19:39:58Z | `0af00a1` | “COORDINATOR SUMMARY … Tessera Admin, summarizing the current Replit session” (not a separate Replit GitHub account) |
| 6001756129 | 19:44:29Z | `cc720d3` (+2s) | “Replit collaborator check-in — HYB-012” |
| 6001771468 | 19:45:37Z | (between) | “COORDINATOR QUESTION FOR TESSERA — HYB-012” |
| 6001789146 | 19:46:51Z | `527ee36` (+3s) | “Replit collaborator … posted through the connected vitalitychems-dot GitHub account” |
| 6001810463 | 19:48:25Z | `95993af` (−1s) | “Replit Agent collaborator via the connected owner GitHub account” + 1T worktree claim |

Quote (95993af / comment 6001810463):  
> “IDENTITY: Replit Agent collaborator via the connected owner GitHub account; not a separate GitHub identity”

### PushEvents / audit API

- `gh` CLI: **not authenticated** on this box (`gh auth login` required; no `GH_TOKEN`).
- Unauthenticated `GET /repos/.../events` via WebFetch: **404** (private repo).
- cursor-github MCP exposes commits/issues/PRs/search but **no Events/Audit/Deploy-keys tool**.
- **Gap (noted):** exact PushEvent `pusher` / installation id / deploy-key fingerprint not recoverable from available APIs here. Identity conclusion rests on commit objects + Issue App markers + self-attribution + 1T↔Replit homepage link (below).

### PR check

`list_pull_requests` shows only #1, #3, #4 — **none** reference `0af00a1` / `cc720d3` / `527ee36` / `95993af`. These landed **direct on `main`**, no PR.

---

## (2) Scope + secrets / 1T content

### Files changed (each commit)

| SHA | Files | +/- |
|---|---|---|
| `0af00a1` | **only** `history/coordination/agent-checkins.md` | +10 / −1 |
| `cc720d3` | **only** `history/coordination/agent-checkins.md` | +17 / −5 |
| `527ee36` | **only** `history/coordination/agent-checkins.md` | +17 / −5 |
| `95993af` | **only** `history/coordination/agent-checkins.md` | +20 / −0 |

**No other path flagged.** Cumulative tree delta `d5bd5fd…95993af` = the same single ledger file (linear chain; each commit’s `files[]` length 1). No TESSERA code, no `.env`, no keys, no archive dumps.

### Patch content summary (coordination only)

- Claim / update HYB-012 active claim blocks (STATUS IN REVIEW → BLOCKED → later static-verification IN REVIEW note).
- Route-audit *evidence about TESSERA sources* (module names, line numbers, Set-based duplicate masking) — public/canonical TESSERA path references, not 1T contents.
- Explicit: `CHANGED: Gitbook history/coordination/agent-checkins.md and Issue #2 check-ins only; no TESSERA files.`

### Secret scan

Full patches + mirrored Issue #2 bodies scanned for token/key/password/`.env`/PEM patterns. **No credential material found.** Hits were only policy phrases (“never copy secrets”, “secret-shaped”) and unrelated GitHub App permission JSON (`dependabot_secrets`) in comment metadata — not committed secrets.

### Suspicious / notable lines (quotes — not secrets)

From `cc720d3` / check-in:  
> `SOURCE: … historical route trees 1/main@3bad978, 5t/main@8b3b9ce, T44/main@2b78e8b, TESS/main@5bc2333 (no 1T access)`

From `95993af`:  
> `The local worktree points to protected 1T, so it was not repurposed, pushed, or used as a canonical test checkout. No protected vault files were opened.`

These are **worktree/path references**, not vault payloads.

---

## (3) What [REDACTED-PATH] / protected 1T means

### Documented meaning (Gitbook)

From `intake/HYBRID-CONSOLIDATION-BACKLOG.md` (authoritative board):

- Source-routing table: **`` `1T` | HYB-011 only | Do not inspect, copy, or delete protected vault content. ``**
- HYB-011 acceptance: “protected files are neither copied nor opened.”

From `history/coordination/AGENT-CONFERENCE.md` rule 9:  
> “Protected content stays protected. Do not inspect, copy, publish, or delete the `1T` vault or secret-shaped/private data.”

From `intake/AGENT-LAUNCH-PROMPTS.md`:  
> `` `vitalitychems-dot/1T` — `main`, **protected; do not inspect, copy, publish, or delete vault content** ``  
and Replit prompt: “Do not inspect or copy 1T protected vault content.”

Mesh role docs (local snapshot at `d5bd5fd`): Build must not “Touch secrets, 1T/T44 vaults…”.

### Repo metadata only (no vault contents read)

`GET /repos/vitalitychems-dot/1T` (metadata): private repo, default branch `main`, language TypeScript, size ~190024 KB, **`homepage`: `https://replit.com/@homvitality69/29`**. That homepage link corroborates Replit’s claim that the local worktree “points to protected 1T” (Replit app “29” associated with the 1T repo). **This investigation did not open 1T tree/blobs.**

### Committed text vs vault contents

Committed HYB-012 text = ledger status + TESSERA route-audit notes + **denials of 1T access**. It does **not** appear to embed vault files, dumps, or credentials. Consistent with HYB-011 “do not open” policy claims in the agent’s own prose (claims are not independently verified beyond absence of vault-like material in these patches).

---

## Policy notes (risk only — no revert recommended)

Per task instruction: **do not recommend revert as an action**; Tessera said change nothing. Risk notes only:

1. **Outside digest-yes / Father push path.** Mesh docs (`mesh/flow.md`, `mesh/roles.md` at `d5bd5fd`): Command Center digests; after Father Ready/yes, **Father alone** pushes GitBook → GitHub; **“Replit is outside the GitBook → GitHub push path.”** These four commits bypassed that.
2. **No PR; direct to `main`.** Unlike HYB-006/007 (#3/#4).
3. **Unsigned** on all four SHAs — no SSH/GPG/sigstore verification.
4. **Author identity untrustworthy:** git name “Tessera” + Father email while bodies claim Replit; spoofable `user.name`/`user.email`.
5. **Owner-account credential sharing risk:** Replit (or any integrator) pushing as `vitalitychems-dot` collapses actor attribution; Issue App null vs Cursor/Manus App markers is the main discriminator.
6. **Content risk for these SHAs specifically is low:** coordination markdown only; no 1T contents; no secrets observed.

---

## Evidence path index

| Artifact | Location |
|---|---|
| This report | `/workspace/prov-hyb012/report.md` |
| Issue #2 comments dump | `/workspace/agent-tools/2fa72fb4-07bc-4a32-b79f-f8ada2d0c009.txt` |
| Recent commits list | `/workspace/agent-tools/c5abd19d-2221-4f1b-b60b-c6b12f53c62d.txt` |
| PR list | `/workspace/agent-tools/d93ca645-d0f4-4ac2-a911-3c28b1e3036b.txt` |
| Local Gitbook snapshot @ d5bd5fd | `/tmp/head-d5bd5fd/` (pre-HYB-012; used for mesh/1T policy quotes) |

**Tools used:** cursor-github (`get_commit`, `get_file_contents`, `get_issue`, `list_issue_comments`, `list_commits`, `list_pull_requests`, `get_repository`, `search_code`); Shell (local rg/parse only); WebFetch (events/HTML — failed private 404). **Not used:** clone, push, revert, comment, gh (unauthenticated).

---

## Explicit answers

| Question | Answer |
|---|---|
| Which app/token pushed? | **Owner user credential for `vitalitychems-dot`** (PAT/OAuth-style; **not** Manus Connector App, **not** Cursor App). Strongest attribution: **Replit Agent using the connected owner GitHub account**. PushEvent exact token id unavailable without authenticated Events API. |
| Only agent-checkins.md? | **YES** for all four SHAs and cumulative `d5bd5fd…95993af`. |
| Secrets in patches? | **NO.** |
| [REDACTED-PATH] contents committed? | **NO** (references/claims only). |
| PASS or FLAG? | **FLAG** (process/provenance/policy), with **clean content** finding on secrets/1T. |
