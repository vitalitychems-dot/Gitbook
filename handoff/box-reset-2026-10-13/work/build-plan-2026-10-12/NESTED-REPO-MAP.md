# Nested repo map (archive / history folders)

Read-only inventory from `cursor-github` `get_repository` + `get_git_tree` (recursive, names only).  
No file contents fetched. No secret search. No pushes or comments.

| Repo | Default branch | Tree SHA (main) | Tree truncated | Tree entries | Dirs |
|------|----------------|-----------------|----------------|--------------|------|
| vitalitychems-dot/Gitbook | main | `cd8faa0a5dfa64e69a7d0a0e179b0b60250cd5a3` | no | 11105 | 699 |
| vitalitychems-dot/TESSERA | main | `a5023224412c535e969d2aecc0c2f4d02be7b972` | no | 4688 | 530 |

**Former-project-like folder count:** **32** path occurrences, **21** unique basenames (19 under Gitbook, 13 under TESSERA).

**Skipped (name contains `1T` or `vault`):** `archive/moved/1T` (Gitbook only). Contents not listed.

---

## Gitbook — top-level dirs

`.codebase-memory/`, `archive/`, `brain/`, `brain-consciousness/`, `forum/`, `history/`, `intake/`, `merge/`, `mesh/`, `operations/`, `posts/`, `review/`, `state/`

### Archive-like roots (L1 → L2)

#### `archive/`
- `drive-rest/`
  - `8-2/`, `Tesseract-AI-5/`, `Tesseracxt9/`, `Tx13/`, `Tx17-9/`, `XL1/`
- `moved/`
  - `1/`, `5t/`, `Grok-ready/`, `T44/`, `TESS/`, `Zz/`, `collink1007-XXX/`, `collink1007-amber-flame-tiger-sand/`, `collink1007-z/`, `olive-giant-ever-glade/`, `tessera-complete-archives/`, `tessera-grok-handoff/`, `tessera-grok-handoff-complete/`
  - *(skipped sibling: `1T/`)*

#### `history/`
- `coordination/` *(no L2 dirs)*
- `handoffs/` *(no L2 dirs)*
- `recovered/`
  - `chronology/`, `coordination/`, `legacy/`, `mirror-notes/`, `source-documents/`, `source-index/`, `source-versions/`, `zz-olive/`
- `source-index/` *(no L2 dirs)*

#### `merge/`
- *(no L1 dirs)*

---

## TESSERA — top-level dirs

`.agents/`, `.codebase-memory/`, `.github/`, `archive/`, `archives/`, `artifacts/`, `data/`, `deliverables/`, `docs/`, `lib/`, `mesh/`, `preview/`, `research/`, `scripts/`

### Archive-like roots (L1 → L2)

#### `archive/`
- `from-gitbook/`
  - `.codebase-memory/`, `archive/`, `brain/`, `brain-consciousness/`, `forum/`, `history/`, `intake/`, `merge/`, `mesh/`, `operations/`, `posts/`, `review/`, `state/`
- `sections/`
  - `3_9_1776105526328/`

#### `archives/`
- `migration-review/`
  - `archive-helpers/`, `legacy-ui/`
- `source-repositories/`
  - `1/`, `5t/`, `Grok-ready/`, `Zz/`, `olive-giant-ever-glade/`
- `source-variants/`
  - `1/`, `5t/`, `Everything/`, `T44/`, `TX/`, `tessera-complete-archives/`, `tessera-grok-handoff/`, `tessera-grok-handoff-complete/`

#### `docs/grok-packet/06_SAFE_SOURCE_FILES/owner-history/`
- *(no L1 dirs; matched by `history` in path)*

---

## Former-project-like folder names

Heuristic: L1/L2 basenames under archive-like roots that look like old app/repo names (codes, Replit-style slugs, Tessera/Grok packs), not generic structure folders (`moved`, `recovered`, `from-gitbook`, etc.).

### Unique basenames (21)

`1`, `5t`, `8-2`, `Everything`, `Grok-ready`, `T44`, `TESS`, `TX`, `Tesseract-AI-5`, `Tesseracxt9`, `Tx13`, `Tx17-9`, `XL1`, `Zz`, `collink1007-XXX`, `collink1007-amber-flame-tiger-sand`, `collink1007-z`, `olive-giant-ever-glade`, `tessera-complete-archives`, `tessera-grok-handoff`, `tessera-grok-handoff-complete`

### Occurrences by path

| Repo | Path |
|------|------|
| Gitbook | `archive/drive-rest/8-2/` |
| Gitbook | `archive/drive-rest/Tesseract-AI-5/` |
| Gitbook | `archive/drive-rest/Tesseracxt9/` |
| Gitbook | `archive/drive-rest/Tx13/` |
| Gitbook | `archive/drive-rest/Tx17-9/` |
| Gitbook | `archive/drive-rest/XL1/` |
| Gitbook | `archive/moved/1/` |
| Gitbook | `archive/moved/5t/` |
| Gitbook | `archive/moved/Grok-ready/` |
| Gitbook | `archive/moved/T44/` |
| Gitbook | `archive/moved/TESS/` |
| Gitbook | `archive/moved/Zz/` |
| Gitbook | `archive/moved/collink1007-XXX/` |
| Gitbook | `archive/moved/collink1007-amber-flame-tiger-sand/` |
| Gitbook | `archive/moved/collink1007-z/` |
| Gitbook | `archive/moved/olive-giant-ever-glade/` |
| Gitbook | `archive/moved/tessera-complete-archives/` |
| Gitbook | `archive/moved/tessera-grok-handoff/` |
| Gitbook | `archive/moved/tessera-grok-handoff-complete/` |
| TESSERA | `archives/source-repositories/1/` |
| TESSERA | `archives/source-repositories/5t/` |
| TESSERA | `archives/source-repositories/Grok-ready/` |
| TESSERA | `archives/source-repositories/Zz/` |
| TESSERA | `archives/source-repositories/olive-giant-ever-glade/` |
| TESSERA | `archives/source-variants/1/` |
| TESSERA | `archives/source-variants/5t/` |
| TESSERA | `archives/source-variants/Everything/` |
| TESSERA | `archives/source-variants/T44/` |
| TESSERA | `archives/source-variants/TX/` |
| TESSERA | `archives/source-variants/tessera-complete-archives/` |
| TESSERA | `archives/source-variants/tessera-grok-handoff/` |
| TESSERA | `archives/source-variants/tessera-grok-handoff-complete/` |

---

## Notes

- Nested archive mirrors: TESSERA `archive/from-gitbook/` copies Gitbook top-level layout (including nested `archive/` and `history/`); deeper than L2 not expanded here.
- Overlap: `5t`, `Grok-ready`, `Zz`, `olive-giant-ever-glade`, `T44`, and the tessera-*-handoff packs appear in both repos under different archive roots.
- Folder `1/` listed (name does not contain `1T`); `1T` path skipped per rules.
- Method: tree path names only via GitHub git trees API; no blob/content reads.

---

## Update 2026-10-12 ~3:53 PM CT — names from logs

Father yes: extract repo names mentioned in logs inside TESSERA and Gitbook (not only folder basenames).

| Deliverable | Path | Count |
|---|---|---:|
| Unique clean names + sources | `REPO-NAMES-FROM-LOGS.md` | **271** |
| Noise / not-a-repo appendix | same file | 11 |
| Top-20 improve plan + metrics | `IMPROVE-TESSERA-PLAN.md` | 20 |
| Primary log sources | `Gitbook:mesh/GITHUB-REPOS.txt`, `mesh/CATALOG-PASS.md`, `mesh/mentioned-repos.txt`, `merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md`, workshop `REPOS.md`/`CATALOG.md` | — |

**Catalog homes (CATALOG-PASS):** live 2 · gitbook-archive 16 · gap 23 · tool 8 · card 193 · held(trading) 17 · vitality 2 · plus routing-only legacy names.

**Nested folder basenames (21)** above remain the on-disk archive map. Many of the 271 log names are *public cards* (not nested folders) and must not be bulk-cloned.

**Still skipped by name:** any path containing `1T` or `vault`; wallet/secret-looking filenames. `vitalitychems-dot/1T` existence-only.

