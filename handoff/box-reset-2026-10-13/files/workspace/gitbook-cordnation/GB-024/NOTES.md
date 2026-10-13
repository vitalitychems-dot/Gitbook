# GB-024: canon fixes to the AGI collaboration roadmap page (DRAFT v2, held; queued after GB-022)

- **v2 (Tessera rulings 15:51 CT, built 15:52 CT):**
  - `ASSIGNED BY` field kept.
  - **OVERLAP CHECK line added** next to it, worded exactly like GB-022's playbook line.
  - PROPOSED kept in the STATUS options.
  - Held until GB-016, GB-017 and GB-018 land.
  - v1 (`75a944bc…`, 63 lines) is kept as `GB-024.v1.diff`; `INTERDIFF-v1-to-v2.diff` shows the one added line.

- **Task:** Tessera, 15:49 CT. A later delta, held in drafts. It has not been sent to any gate and is not in READY.md or any FROZEN file.
- **Target:** `brain-consciousness/AGI-COLLABORATION-IMPROVEMENT-ROADMAP.md`. Father added it directly on main in `fd3c2ce04fa4230c32cf917f36c662f268a1ea76` at 15:47 CT (parent f4b2c41).
- **How the source was read:** cursor-github get_file_contents at ref fd3c2ce. The rebuilt file matches the commit's blob `d92eaf61cc02d8321a279452ff9b78b7cbf6cb2b` (`git hash-object`), 79 lines.
- **Base:** fd3c2ce. The page has no front matter, so none was added. No gate banners. The page's own `**Status:** Proposed …` line is page content, not a gate banner; it was kept and extended.
- **Diff:** `GB-024.diff` v2, 64 lines, 1 file, +11/−7, sha256 `3fc1fc11…` (in SHA256.txt).
- **Copies:** `base/` holds the fd3c2ce file and `proposed/` holds it with GB-024 applied.
- **Overlap:** no other package (GB-016/017/018/022) touches this page. SUMMARY.md is not touched; the label already matches the page.

## Per-change table

| # | Canon rule | Location | Before | After |
|---|---|---|---|---|
| 1 | (a) PROPOSED until Tessera assigns | Status line | "Proposed research and engineering roadmap" | adds "Every item is PROPOSED until Tessera assigns it." |
| 2 | (a)/(e) owner comes from Tessera | Item 3, Improvement | "tasks with one owner and one acceptance test" | "one owner (assigned by Tessera)" |
| 3 | (e) routing is not assignment | Item 4, Acceptance evidence | "Routing decision cites skill IDs…" | "Routing proposal cites skill IDs, evidence level, and a review lane; Tessera assigns" |
| 4 | (c) Moderator returns changes needed, not decisions; (d) gates | Item 13, Improvement + Acceptance evidence | "record a moderator decision"; "Each accepted idea links to a task" | "record the review outcome (the Gitbook Moderator returns `changes needed`, not decisions)"; "Each idea accepted through Moderator, then Tessera, then Security, then CI/Build, then Father's final yes links to a task Tessera assigns" |
| 5 | (d) full gate sequence | Item 19, Acceptance evidence | "without the required gate" | "without the required gates: Moderator, then Tessera, then Security, then CI/Build, then Father's final yes" |
| 6 | (d) digest carries Ready work | Item 20, Improvement | "summarize completed, blocked, and proposed work … a single owner decision request" | "summarize Ready work (cleared Moderator, then Tessera, then Security, then CI/Build), plus blocked and proposed work … (Father's final yes)". The `yes`/`no`/`revise` cell is unchanged (feaeb558 canon). |
| 7 | (e) claim only after assignment | Agent completion rule, intro | "may claim one roadmap item only when it posts:" | "only after Tessera assigns it, and only when it posts:" |
| 8 | (e) checkable assignment | Completion template | — | new field `ASSIGNED BY: Tessera <link to the assignment>` after TASK ID |
| 8a | Father's 3:10 PM overlap rule (Tessera 15:51) | Completion template | — | new line `OVERLAP CHECK: <Gitbook main SHA checked + open PRs checked (numbers or none)>` right after ASSIGNED BY (same wording as GB-022's playbook line) |
| 9 | (b) who sets BLOCKED; (c) | after template | — | "`BLOCKED` is set only by the task owner (in its own check-in) or by Tessera. Gates, the Gitbook Moderator included, return `changes needed` and never set `BLOCKED`." The template's STATUS line is unchanged; PROPOSED is kept (Tessera 15:51). |

**Left unchanged on purpose:**
- The disclaimer blockquote (it is content, not a gate banner).
- Items 1, 2, 5–12, 14–18.
- The phases and the Success definition.
- "moderator roles" in item 18: these are simulated roles, not the gate.
- "one documented decision" in item 12: this names no decider, so it is canon-neutral.

## Apply check (fd3c2ce snapshot)

The snapshot is f4b2c41 plus fd3c2ce's two files, whose blobs match the commit: SUMMARY `41c1580a` and page `d92eaf61`.
- **GB-024 alone:** clean, 0 offsets; the result equals `proposed/`.
- **Stack GB-017 → GB-018 → GB-016 rev 3.2 → GB-024:** all rc=0. GB-017 has one hunk offset by 1 line (from fd3c2ce's SUMMARY line); the others have 0 offsets.
- GB-022 is still on its 1e3 + 7 base and gets rebased after the push. GB-024 shares no file with it.
- **v2 (15:52 CT):** GB-024 v2 alone on fd3c2ce is clean and equals `proposed/`. Stack 017 → 018 → 016 rev 3.2 → 024 is all rc=0; GB-017 still has its 1-line offset, the others 0.
- **Correction (15:56 CT):**
  - The earlier fd3c2ce stack lines above (v1 and v2) are unreliable, for two reasons:
    - The fd3c2ce snapshot had picked up 2 leftover untracked files from an earlier check (`mesh/roles/security.md`, `merge/hyb-005-braces-decision.md`).
    - The loop printed the exit code of `basename`, not of `git apply`.
  - GB-024 by itself was unaffected: the diff touches only the roadmap page, which matched the fd3c2ce blob.
  - Rebuilt clean fd3c2ce snapshot, with rc captured directly: 017 rc=0 (1 offset) → 018 rc=0 → 016 rev 3.2 rc=0 → GB-024 rc=0, 0 fuzz.
  - On 97e43fb (PR #6) + GB-017 + GB-016 rev 3.2: GB-024 rc=0, 0 offsets.


## v3: rebased onto ecd9022 + GB-022 v4 (2026-10-05 ~16:16 CT)

**File:** `GB-024-v3.ecd9022.diff`, sha256 `3fc1fc11…74e1c6`: 64 lines, 1 file, 5 hunks, +11/−7. This is **byte-identical to v2** (`GB-024.diff`). The roadmap page blob d92eaf61 is unchanged from fd3c2ce through ecd9022, and GB-022 does not touch it. `git apply --check` gives rc=0 both solo on ecd9022 and stacked after GB-022 v4.
