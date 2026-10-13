# Provenance and content sweep: Gitbook PR #9 merge `ebe003fe` + PR #10 merge `45651521`

**Repo:** vitalitychems-dot/Gitbook (private)
**Subjects:**
1. Merge `ebe003fece89c44a85ff105e688971e8de928d96` = PR #9 (GB-026 rev 3 + GB-027). Head was `b23d9eb8618bc951b21d3abecec717a9874e5cc8`. Frozen: GB-026 `7fe2d5f2…` / GB-027 `8fc78041…` (Security PASS on base `979c35e`).
2. Merge `45651521a137c4448673d6abfaa77e1567230f83` = PR #10 (GB-028 rev 3). Head was `c507f0c2ad67675166c5afe4471eb05b6e6994d3`. Frozen: `102ff79c…` (Security PASS).
**Board RECEIPT:** https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6003943663
**Father yes:** 16:49 CT (cited in both merge messages and the receipt). Tessera merged.
**Report time:** 2026-10-05 ~5:02–5:10 PM CT. Lane: Security. Read-only.
**Tools used:** cursor-github `get_pull_request` #9/#10, `get_commit` (ebe003fe, 45651521, b23d9eb, c507f0c2), `list_commits` (Gitbook main; Gitbook since 21:00Z; TESSERA main; TESSERA since 21:00Z), `list_issue_comments` issue #2 since 21:00Z, `get_file_contents` `history/coordination/command-center.md` at ebe003fe and tip, `get_git_tree` recursive tip `45651521`. On the box: `sha256sum` of three frozen diffs, `git hash-object` of restored command-center and Build after-stack blobs, content sweeps of added lines, reads of Security gates (`GATE-GB-026-rev3-979c35e.md`, `GATE-GB-027-979c35e.md`, `GATE-GB-028-rev3-979c35e.md`), Build gates (`GATE-2026-10-05-PR9-b23d9eb.md`, `GATE-2026-10-05-PR10-c507f0c2.md`), and cloud agent transcripts `bc-eebfc4fa…` / `bc-a9b8d82c…`.
**Not done:** no pushes, comments, merges, labels, or edits to any repo. No secrets printed.

## Verdict

| Lane | Result |
|---|---|
| **Provenance (merge ebe003fe / PR #9)** | **PASS.** Merged through PR #9. GitHub web-flow PGP signature (`verified:true`, `valid`). 2 parents: `979c35e0` (main) + `b23d9eb` (PR head). Author "Tessera". Message cites Father's yes 16:49 CT and Build PASS on b23d9eb. merged_by vitalitychems-dot. **Not** a Manus direct-to-main push. |
| **Provenance (2 PR #9 commits)** | **PASS.** Both signed by Cursor Agent (`verified:true`, SSH) with Tessera co-author. Branch `tessera/gb-026-027`. Linear: GB-026 rev3 `1e107de5` → GB-027 `b23d9eb` on `979c35e0`. |
| **Provenance (merge 45651521 / PR #10)** | **PASS.** Merged through PR #10 onto tip after #9. Web-flow PGP (`verified:true`, `valid`). Parents: `ebe003fe` + `c507f0c2`. Author "Tessera". Cites Father's yes 16:49 CT and Build PASS c507f0c2. merged_by vitalitychems-dot. **Not** Manus. |
| **Provenance (1 PR #10 commit)** | **PASS.** Cursor Agent signed (`verified:true`, SSH) with Tessera co-author. Branch `tessera/gb-028`. Parent `979c35e0` (opened in parallel with #9; disjoint paths). |
| **Content (PR #9)** | **PASS.** 30 files, +97/−131. Secrets / ENABLE flips / gate-drop / Pen-as-gate / 1T dump: clean. "silently impersonate" appears only in the corrective Pen-is-voice line (Pen does **not** silently impersonate). |
| **Content (PR #10)** | **PASS.** 5 files, +68/−9 (1 new). Branch+PR / never push to main; `TESSERA_ENABLE_*` stay 0; HYB-012 IN REVIEW cites 6003216455 without re-authorizing direct-to-main. Path overlap with PR #9: **0**. |
| **Frozen carryover** | **PASS.** All three sha256 values match Security PASS + PR bodies + FROZEN-SHA256-979c35e.txt. Build head gates: TREE_MATCH for both PRs. Independent: Build after-stack 30/30 blobs = merge ebe003fe file blobs; tip recursive tree holds all 5 PR #10 blobs + restored CC. |
| **command-center.md** | **RESTORED.** Tip and ebe003fe: blob `9916da0b186760f5fa09d5da672347485ec6a785`, **262 B**. Present after PR #9/GB-027; PR #10 did not touch it. |
| **Manus-offline unexpected** | **N.** No Manus-attributed commit on Gitbook or TESSERA after the PR merges (~17:01 CT) or since 21:00Z. Tip SHAs noted below. |
| **Overall** | **PASS both. No FLAG. No Father wake.** |

## Tip SHAs (sweep time ~5:02–5:10 PM CT)

| Repo | Tip SHA | Note |
|---|---|---|
| Gitbook `main` | `45651521a137c4448673d6abfaa77e1567230f83` | PR #10 merge; nothing newer |
| TESSERA `main` | `fec56eb09d19907832663d5f16fcbc24f3d00317` | Unchanged; last Manus author at 12:29 PM CT (17:29Z), **before** offline window / before these merges |

## Provenance — PR #9 / merge ebe003fe

### Merge commit ebe003fe
| Field | Value |
|---|---|
| Message | `Merge PR #9: GB-026 rev 3, GB-027 (Father's yes 16:49 CT, Build PASS b23d9eb)` / `Approved: GB-026 rev 3, GB-027` |
| Git author | `Tessera <vitalitychems@gmail.com>` (login vitalitychems-dot) |
| Git committer | `GitHub <noreply@github.com>` (login web-flow) |
| Date | 2026-10-05T22:00:46Z = **5:00:46 PM CT** |
| Verification | `verified:true`, `reason:valid`, PGP (web-flow) |
| Parents | `979c35e0be9a27ab143c7dcfc714d979b11e10a0` + `b23d9eb8618bc951b21d3abecec717a9874e5cc8` ✔ |
| Tree | `dd386cd427f29b38b58614694b0111dbb66e4bfb` = **identical to head b23d9eb tree** |
| Stats | +97/−131, 30 files |

### PR #9
| Field | Value |
|---|---|
| Title | `Approved: GB-026 rev 3, GB-027` |
| Body | `IDENTITY: Tessera Admin coordinator` + frozen hashes `7fe2d5f2…` / `8fc78041…` (exact). Footer agent `bc-eebfc4fa-1296-54a1-8b64-57ab0dbb5526` |
| Opened | vitalitychems-dot at 21:50:17Z = **4:50:17 PM CT** |
| Head / base | `tessera/gb-026-027` @ b23d9eb → `main` @ 979c35e0 |
| Merged | merged=true at 22:00:46Z (**5:00:46 PM CT**), merged_by **vitalitychems-dot**, merge_commit_sha = ebe003fe ✔ |
| Commits / files | 2 commits, 30 files, +97/−131 |

### PR #9 commits
| Commit | Message | Author | Verified | Parent |
|---|---|---|---|---|
| 1e107de5 | GB-026 rev 3: cleanup rulings and Tessera-push rule | Cursor Agent + Tessera co-author, 4:49:54 PM CT | true/valid (SSH) | 979c35e0 |
| b23d9eb8 | GB-027: restore history/coordination/command-center.md and align leftovers | Cursor Agent + Tessera co-author, 4:50:01 PM CT | true/valid (SSH) | 1e107de5 |

### Cloud agent transcript bc-eebfc4fa
- Instruction: verify both sha256s, apply in order 026→027, open PR, **DO NOT MERGE**.
- Transcript: checksums matched, applied cleanly, PR #9 opened, agent reported "was not merged". 0 merge commands in the agent run. Merge happened separately via GitHub web-flow.

## Provenance — PR #10 / merge 45651521

### Merge commit 45651521
| Field | Value |
|---|---|
| Message | `Merge PR #10: GB-028 rev 3 (Father's yes 16:49 CT, Build PASS c507f0c2)` / `Approved: GB-028 rev 3` |
| Git author | `Tessera <vitalitychems@gmail.com>` (login vitalitychems-dot) |
| Git committer | web-flow |
| Date | 2026-10-05T22:00:51Z = **5:00:51 PM CT** |
| Verification | `verified:true`, `reason:valid`, PGP (web-flow) |
| Parents | `ebe003fece89c44a85ff105e688971e8de928d96` + `c507f0c2ad67675166c5afe4471eb05b6e6994d3` ✔ |
| Tree | `b3e423a8c1ebe3754b1ea2fc6a5f059e616a3059` (≠ head-alone tree `d6d238e9…` — expected: parallel PR on 979c35e merged after #9; union of disjoint path sets) |
| Stats | +68/−9, 5 files |
| Position | **main HEAD** at sweep time |

### PR #10
| Field | Value |
|---|---|
| Title | `Approved: GB-028 rev 3` |
| Body | `IDENTITY: Tessera Admin coordinator` + `GB-028-rev3.979c35e.diff 102ff79c…aa122`. Footer agent `bc-a9b8d82c-db47-5156-86ea-a52d7541464e` |
| Opened | vitalitychems-dot at 21:55:27Z = **4:55:27 PM CT** |
| Head / base | `tessera/gb-028` @ c507f0c2 → `main` @ 979c35e0 (same base as #9; parallel) |
| Merged | merged=true at 22:00:51Z (**5:00:51 PM CT**), merged_by **vitalitychems-dot**, merge_commit_sha = 45651521 ✔ |
| Commits / files | 1 commit, 5 files, +68/−9 |

### PR #10 commit
| Commit | Message | Author | Verified | Parent |
|---|---|---|---|---|
| c507f0c2 | GB-028 rev 3: Replit agents start-here page and HYB-012 unblock | Cursor Agent + Tessera co-author, 4:55:08 PM CT | true/valid (SSH) | 979c35e0 |

### Cloud agent transcript bc-a9b8d82c
- Instruction: verify sha256, apply once, open PR, **DO NOT MERGE**.
- Transcript: checksum matched, applied cleanly on base 979c35e0, PR #10 opened, "was not merged". 0 merge commands. Merge via web-flow after #9.

### Sequence (CT)
- **4:41–4:45 PM:** Security PASS GB-026 rev3 + GB-027 on base 979c35e (frozen 7fe2d5f2 / 8fc78041)
- **4:48–4:49 PM:** Security PASS GB-028 rev3 (frozen 102ff79c)
- **4:49 PM:** Father yes (cited)
- **4:49:54–4:50:01 PM:** PR #9 commits (agent bc-eebfc4fa)
- **4:50:17 PM:** PR #9 opened
- **4:52–4:58 PM:** Build PASS on PR #9 head b23d9eb (TREE_MATCH both steps)
- **4:55:08 PM:** PR #10 commit (agent bc-a9b8d82c)
- **4:55:27 PM:** PR #10 opened
- **4:56–4:58 PM:** Build PASS on PR #10 head c507f0c2; path overlap with #9 = 0
- **5:00:46 PM:** merge PR #9 → ebe003fe
- **5:00:51 PM:** merge PR #10 → 45651521 (onto ebe003fe)
- **5:00:57 PM:** board comment 6003943663 (IDENTITY Tessera, via Cursor app)

### Receipt match (Tessera-authorized; do not FLAG impersonation)
| Receipt | Evidence | Match |
|---|---|---|
| Board #issuecomment-6003943663 | IDENTITY Tessera Admin coordinator; cites ebe003fe / 45651521 / heads / Father 16:49 / main now 4565152 / CC restored 9916da0b / Manus offline until ~16:52 CT Tue. Via Cursor app at 5:00:57 PM CT. | **YES** |
| Merges cite Father 16:49 + Build PASS heads | Both merge messages and PR bodies align with frozen hashes and Build gates. | **YES** |

**Attribution note (INFO, not a FLAG):** Tessera / Father / connectors share vitalitychems-dot. Attribution rests on receipts, IDENTITY, "Tessera" merge author, and Cursor agent chain. Nothing contradicts it: every feature commit signed, merges are web-flow PR merges, Manus not involved.

## Frozen-hash / package carryover

1. `sha256sum` (re-run ~5:03 PM CT):
   - `GB-026/GB-026-rev3.979c35e.diff` = `7fe2d5f273ac9826b10eb6bec1358986bb608433a681e1cb98da7a25ed1f7730` ✔
   - `GB-027/GB-027.979c35e.diff` = `8fc780410bef373aebf06f9c4ac6ba52a1f24e0569d4851d29d2b6d55a803121` ✔
   - `GB-028/GB-028-rev3.979c35e.diff` = `102ff79c700790c6c9167e187aff5ea41066fb01fbb5b4c0efce4459026aa122` ✔
   Match Security PASS gates, FROZEN-SHA256-979c35e.txt, and both PR bodies.
2. Same base `979c35e0` for all three packages; PR bases were `979c35e0`. #10 merged after #9 with **0 path overlap** → clean union on tip.
3. Build head gates (TESTED): PR #9 TREE_MATCH Y for e9989067 (026) and dd386cd4 (027); PR #10 head tree d6d238e9 = tip+028, 5/5 blobs.
4. Independent Security check: Build after-stack files for the 30 PR #9 paths → **30/30** `git hash-object` match ebe003fe merge file blobs (incl. CC `9916da0b`). Tip recursive tree: all 5 PR #10 blobs present and matching Build post-apply list; CC still `9916da0b` / 262 B. **No drift.**

## Content sweeps (added lines of frozen diffs)

| Check | GB-026 | GB-027 | GB-028 |
|---|---|---|---|
| Secrets (ghp_/github_pat_/gho_/sk-/AKIA/xox/PEM/cred assigns) | 0 | 0 | 0 |
| `TESSERA_ENABLE_*` nonzero | 0 | 0 | 0 (stay-0 language only) |
| Pen-as-gate / Pen assigns | 0 | 0 | 0 |
| "silently impersonate" | 1 (corrective: Pen does **not**) | 0 | 0 |

PR #9 paths (union 30) ∩ PR #10 paths (5) = **∅**.

## history/coordination/command-center.md

| Ref | Blob | Size |
|---|---|---|
| 979c35e0 (pre-#9) | `e69de29b…` (empty) | 0 |
| ebe003fe (after #9) | `9916da0b186760f5fa09d5da672347485ec6a785` | **262** |
| 45651521 (tip, after #10) | `9916da0b186760f5fa09d5da672347485ec6a785` | **262** |

GB-027 restore matches INV / Security PASS target (blob `9916da0b` / 262 B; `\ No newline at end of file`). Local `git hash-object` of the 262-byte no-trailing-newline form = `9916da0b…`. Tip tree entry confirms size 262. **Restored by PR #9/GB-027; still present on tip after ebe003fe and after 45651521.**

## Manus-offline watch

**Father REPORTED:** Manus offline until ~16:52 CT Oct 6.
**FLAG rule:** any Manus-attributed commit on Gitbook/TESSERA before then = unexpected.

| Check | Result |
|---|---|
| Gitbook commits since 21:00Z (4:00 PM CT) | 13 commits; **0** Manus-authored (all Tessera merges or Cursor Agent) |
| Gitbook after merges (~17:01 CT) | Tip still `45651521`; no newer commit |
| TESSERA commits since 21:00Z | **[]** empty |
| TESSERA tip | `fec56eb` — Manus Consolidation author at **12:29 PM CT** (pre-offline / pre-merge); **not** after ~17:01 CT |
| Unexpected Manus during offline window / post-merge | **N** |

## Pastes

### Tessera
```
Security PROV PASS on main 45651521 (PR #9 ebe003fe: GB-026 rev3 + GB-027; PR #10 45651521: GB-028 rev3). Provenance: Tessera web-flow PR merges (verified PGP; #9 parents 979c35e0+b23d9eb at 5:00:46 PM CT; #10 parents ebe003fe+c507f0c2 at 5:00:51 PM CT; both cite Father's yes 16:49 CT and Build PASS heads). Not Manus. Receipts hold: heads b23d9eb / c507f0c2 (Cursor Agent SSH-signed + Tessera co-author; agents bc-eebfc4fa / bc-a9b8d82c; DO NOT MERGE honored), merges, board #issuecomment-6003943663. Frozen hashes match (7fe2d5f2 / 8fc78041 / 102ff79c). Path overlap #9∩#10 = 0; tip holds both packages. Independent: 30/30 PR #9 blobs = ebe003fe; tip has all 5 PR #10 blobs. Content sweeps clean (secrets, ENABLE, Pen-as-gate). command-center.md RESTORED: blob 9916da0b / 262B on ebe003fe and tip. Manus-offline unexpected: N (Gitbook tip 45651521; TESSERA tip fec56eb, last Manus 12:29 PM CT, none after ~17:01 CT). No FLAG. No Father wake. Report: /workspace/security-gate/PROV-2026-10-05-pr9-pr10-merges.md
```

## Father wake
**None** (no FLAG, no secrets, Manus-offline unexpected = N).
