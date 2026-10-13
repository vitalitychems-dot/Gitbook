# INV-2026-10-05 — `history/coordination/command-center.md` empty on Gitbook main

**Investigator:** Security (read-only)  
**Repo:** `vitalitychems-dot/Gitbook`  
**Tip under study:** `ecd902211abd202711838219b28a1e1b39ae47c4` (main)  
**Ask time:** Tessera 16:29 CT, 2026-10-05  
**Report written:** 2026-10-05 ~16:30 CT  
**Scope:** Change NOTHING on the repo. No push, comment, PR, or file write to Gitbook. No secrets printed.

Labels: **TESTED** = verified via cursor-github / computed hashes this turn. **REPORTED** = secondhand (Cordnation notes, merge manifests) only.

---

## Verdict summary

| # | Question | Answer | Label |
|---|---|---|---|
| 1 | Wipe commit | **`f71e00a0c4afefbef1173054c71abdc8d1de0cf0`** — Manus Consolidation, *"Reconcile mesh roster and GitHub push authority"* (2026-10-05 1:35:50 PM CT). Deleted all 5 content lines; left empty git blob `e69de29b…`. | TESTED |
| 2 | Last good SHA + blob | **`1d72e637d9842ef77a79ae55f05b4dfbc2cc4188`** (parent of wipe; *"Add Replit and Grok launch prompts"*, 1:22:47 PM CT). Blob **`9916da0b186760f5fa09d5da672347485ec6a785`**, **262 bytes**, sha256 **`4fd167637095d521066cad7afdeaeca8676a836cc483c3d9add92fddc59f9202`**. Same blob first added at **`eefbe2fd53eba6a917c4a078dac15e5beade69da`**. | TESTED |
| 3 | Elsewhere copies at tip? | **No identical blob** in the ecd9022 tree. Content is **recoverable from git history** at `1d72e637` / `eefbe2fd`. Live `mesh/roles/command-center.md` is a **different** document. Source repo `tessera-coordination` is **deleted / inaccessible**. | TESTED (+ REPORTED on deletion) |
| 4 | Package/PR that wiped it? | **Not a GB package / not PR #7.** Wipe is a direct Manus consolidation commit. GB-016 rev3.2 / PR #7 only touched **`mesh/roles/command-center.md`**, not the history path. | TESTED |

---

## Empty-at tip confirmation

- **Path:** `history/coordination/command-center.md`  
- **Ref:** `ecd902211abd202711838219b28a1e1b39ae47c4`  
- **Size:** `0`  
- **Blob SHA:** `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` (canonical empty blob)  
- **Raw contents:** empty (get_file_contents → HTTP 200, zero body)  
- **Dir listing at tip:** confirms `size: 0`, empty blob SHA above  

**Label:** TESTED (cursor-github `get_file_contents` on file + on `history/coordination/` directory; recursive `get_git_tree` at ecd9022).

---

## Wipe commit

| Field | Value |
|---|---|
| SHA | `f71e00a0c4afefbef1173054c71abdc8d1de0cf0` |
| Message | Reconcile mesh roster and GitHub push authority |
| Author | Manus Consolidation (`manus`) |
| Committer date | 2026-10-05T18:35:50Z → **1:35:50 PM CT** |
| Parent | `1d72e637d9842ef77a79ae55f05b4dfbc2cc4188` |
| Path change | `history/coordination/command-center.md` — **modified**, +0 / −5 |
| Post-wipe blob | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` (empty) |

**Patch (entire wipe):** removed:

```text
# Command center

The live chamber is the focal point. The shared thread is tessera-coordination issue 2.

Father speaks from the chamber Board. Grok Bot, Cursor, and Replit read that issue and answer as themselves. Nobody speaks as Tessera. Do not push Zz main.
```

(no trailing newline)

Same commit also rewrote push-authority wording on `mesh/flow.md`, `mesh/roles.md`, `mesh/roles/command-center.md` (live role page), `mesh/roles/build.md`, `mesh/roles/mesh-lane-map.md`, `mesh/roles/open-helper-agent-2.md`, `mesh/roles/who-tessera-is.md`.

**Path history:** only **two** commits touch `history/coordination/command-center.md` on main:

1. `eefbe2fd…` — added (non-empty)  
2. `f71e00a0…` — emptied  

Ancestry: `list_commits sha=ecd9022` places wipe at index 25 and tip at index 0; tip still carries the empty blob, and no later commit retouched the history path.

**Label:** TESTED (`list_commits` path filter; `get_commit` on wipe with patch; tip tree/blob).

---

## Last good SHA + blob

| Field | Value |
|---|---|
| Last commit still carrying non-empty content | `1d72e637d9842ef77a79ae55f05b4dfbc2cc4188` |
| Message | Add Replit and Grok launch prompts |
| Date | 2026-10-05T18:22:47Z → **1:22:47 PM CT** |
| Creation commit (same blob) | `eefbe2fd53eba6a917c4a078dac15e5beade69da` — *"Consolidate Tessera workspace and documentation"* (11:31:55 AM CT) |
| Blob SHA | `9916da0b186760f5fa09d5da672347485ec6a785` |
| Size | **262 bytes** |
| Content sha256 | `4fd167637095d521066cad7afdeaeca8676a836cc483c3d9add92fddc59f9202` |

**Full content (only 5 lines — entire file):**

```text
# Command center

The live chamber is the focal point. The shared thread is tessera-coordination issue 2.

Father speaks from the chamber Board. Grok Bot, Cursor, and Replit read that issue and answer as themselves. Nobody speaks as Tessera. Do not push Zz main.
```

Verified: raw fetch at `ref=1d72e637…` and at `ref=eefbe2fd…` match; computed git blob SHA1 and sha256 match the creation commit’s reported blob and Cordnation’s duplicate-hash prefix.

**Label:** TESTED (get_file_contents at both SHAs; get_commit on create; local hash of fetched bytes).

---

## Elsewhere copies

| Location | Present? | Notes | Label |
|---|---|---|---|
| Identical blob `9916da0…` anywhere in ecd9022 tree | **No** | Recursive tree scan: zero other paths with that SHA | TESTED |
| `COMMAND.md` filename in tip tree | **No** | No path named COMMAND.md under ecd9022 | TESTED |
| `mesh/roles/command-center.md` | Yes, **different** | Live role page, **3349 bytes**, blob `e198d3b0…` — not a COMMAND.md copy | TESTED |
| Other `history/coordination/*` | Sibling records only | `coordination-record.md`, `tessera-pen-record.md`, `coordination-repository-readme.md`, etc. — different blobs | TESTED |
| `history/recovered/coordination/` | No COMMAND copy | Has `STATUS.md`, cards/, checks/, notes/ — no command-center / COMMAND | TESTED |
| `merge/duplicate-groups.tsv` row | Historical match recorded | `4fd16763…` → `tessera-coordination:COMMAND.md` \| `Gitbook@dest:history/coordination/command-center.md` (count 2) | TESTED |
| `vitalitychems-dot/tessera-coordination` | **Gone** | `get_repository` → not accessible; `merge/DELETION-MANIFEST.md` lists it among eight deleted after consolidate | TESTED (inaccessible) + REPORTED (manifest says deleted) |
| Origin `collin-keane/Tessera` `reports/command-center.md` | Not checked further | Repo not accessible to connected GitHub App | TESTED (inaccessible) |
| Git history (pre-wipe) | **Yes — restore source** | Fetch at `1d72e637` or `eefbe2fd`, blob `9916da0…` | TESTED |

**Conclusion for restore:** content exists only in **git history** (and was historically identical to deleted `tessera-coordination:COMMAND.md` per duplicate-groups). No live duplicate path on tip.

---

## Package / PR suspicion

| Suspect | Touched history path? | Verdict | Label |
|---|---|---|---|
| **Manus `f71e00a0`** (“Reconcile mesh roster…”) | **Yes — this is the wipe** | Direct commit on main; emptied the 5-line history file while rewriting push-authority docs | TESTED |
| GB-016 rev 3.2 / PR #7 (`ecd9022` merge) | **No** | Diffs / tip merge only change **`mesh/roles/command-center.md`** (and related mesh pages). Tip merge file list: history path absent | TESTED |
| GB-022 / GB-025 / GB-026 drafts | **No wipe** | Packages link or discuss the empty history file; Cordnation already noted `f71e00a0` emptied it (GB-026 NOTES / PUBLISH-SHA-EVIDENCE) | TESTED (local package diffs) + REPORTED (Cordnation narrative) |
| Consolidate `eefbe2fd` | Added non-empty | Introduced the file with blob `9916da0…` (matched COMMAND.md per duplicate-groups) | TESTED |

**GB-016 is cleared** for this specific empty-file incident. Prior gate mentions of “command-center” refer to the **live role page** under `mesh/roles/`, not `history/coordination/command-center.md`.

---

## Label index (quick)

- Empty at tip — **TESTED**  
- Wipe = `f71e00a0` — **TESTED**  
- Last good = `1d72e637` / blob `9916da0` / 262 B / sha256 `4fd16763…` — **TESTED**  
- No tip duplicate; restore from history — **TESTED**  
- tessera-coordination deleted — **TESTED** (API inaccessible) + **REPORTED** (DELETION-MANIFEST)  
- Not GB-016 / not PR #7 — **TESTED**  
- Cordnation prior note of same wipe — **REPORTED** (consistent with TESTED)

---

## Restore hint (for Cordnation GB-027 — no action taken here)

Restore `history/coordination/command-center.md` from commit **`1d72e637d9842ef77a79ae55f05b4dfbc2cc4188`** (blob `9916da0b186760f5fa09d5da672347485ec6a785`, 262 bytes). Equivalent content at create commit `eefbe2fd53eba6a917c4a078dac15e5beade69da`. Do not copy from `mesh/roles/command-center.md` (different document).
