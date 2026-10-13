# GB-026 rev 2: evidence for the publish SHA on the six GB-004–014 pages

Prepared 2026-10-05 16:30 CT for Build to confirm. All checks were read-only through the GitHub API (cursor-github `get_commit` and `list_commits`). Nothing was pushed.

## Result
**801062641f30d2acf45dbea4748323f20c5e30d8** is an ancestor of ecd902211abd202711838219b28a1e1b39ae47c4. It is the commit that **landed (added)** all six pages on Gitbook main. GB-026 rev 2 uses this full SHA in each page's front-matter note.

- **No commit set these pages to `status: published`.** 8010626 added them with `status: approved` and the note "Status: Ready — awaiting Father GitHub push (…)". They are still that way at ecd9022, which is why GB-026 changes them.
- **Only one page changed after landing.** who-tessera-is.md was edited by f71e00a0 (see below), which did not change its front matter. The other five pages are byte-identical at ecd9022 to what 8010626 added.

## Commit 801062641f30d2acf45dbea4748323f20c5e30d8
- **Date:** 2026-10-05T13:25:25Z (8:25:25 AM CT)
- **Author:** Cursor Agent, co-authored by Tessera. The SSH signature is verified.
- **Parent:** ffc2b87ea7a7316a22660d1a17fcf6dcf437a580 ("Publish the second Tessera GitBook batch.")
- **Message:** "Publish Ready GitBook batches 003–009 (GB-004 through GB-014)."
- **Files** (from `get_commit`; raw JSON in `apply-rev2/github-get_commit-8010626.json`):

| Status | File | Blob after 8010626 | Blob at ecd9022 | Same? |
|---|---|---|---|---|
| added | mesh/roles/who-tessera-is.md | 6c893164d271dd5885d16e36549e1f94d7cfa4eb | 001e40346240b47f1ac2eee03b1c91042cead2fa | no (f71e00a0) |
| added | mesh/roles/pen-ability-set-framing.md | 492be9371222818396aa15424ddcce9d9b49725b | 492be937… | yes |
| added | mesh/roles/refuse-and-offer.md | 3375d675badfb5a24bbf3e59334a6dea7473a4ad | 3375d675… | yes |
| added | mesh/roles/board-world-chamber.md | 3644ba3bda12b3eb4ffc0360b6436e549680a68f | 3644ba3b… | yes |
| added | mesh/roles/pen-gate-refuse-companion.md | b12f05e74bac858022341b225669209c55bf2ced | b12f05e7… | yes |
| added | mesh/roles/honesty-banner.md | d658fe10b117b6ea55747329875e9468b016d143 | d658fe10… | yes |

  The same commit also touched SUMMARY.md, intake/log.md, mesh/roles.md, build.md, mesh-lane-map.md (added), open-helper-agent-2.md (added), pen-tone-guide.md and tessera-pen.md. In total: +469/−31 across 14 files.
- **How the ecd9022 blobs were confirmed:** `git hash-object` on the files fetched at ref ecd9022, compared against the ecd9022 tree listing.

## Per-page history (`list_commits sha=ecd9022 path=<page>`)
| Page | Commits reachable from ecd9022 that touched it |
|---|---|
| who-tessera-is.md | f71e00a0c4afefbef1173054c71abdc8d1de0cf0 (2026-10-05T18:35:50Z = 1:35 PM CT, Manus, "Reconcile mesh roster and GitHub push authority"); 801062641f30… (added) |
| board-world-chamber.md | 801062641f30… only |
| honesty-banner.md | 801062641f30… only |
| pen-ability-set-framing.md | 801062641f30… only |
| pen-gate-refuse-companion.md | 801062641f30… only |
| refuse-and-offer.md | 801062641f30… only |

f71e00a0 changed two lines on who-tessera-is.md and left the front matter alone:
- the body Status line ("…until Command Center posts the final push…" → "…until Father completes the GitBook → GitHub push…")
- the CC table row ("posts final push after TESSERA" → "does not push")

So 8010626 is still the commit that landed that page. Note for the record: f71e00a0 also emptied history/coordination/command-center.md (−5 lines).

## Ancestry: 8010626 → ecd9022
From `list_commits sha=ecd9022 perPage=100`, 50 commits (saved in `apply-rev2/ecd9022-history-50.tsv`). Walking parent links from ecd9022 reaches 8010626. The first-parent chain is:

ecd9022 → 97e43fb → fd3c2ce → f4b2c41 → feaeb55 → fb984ad → 1e3bb50 → e73fb18 → beadc44 → 95993af → 527ee36 → cc720d3 → 0af00a1 → d5bd5fd → 6fe412f → f71e00a → 1d72e63 → 74f1601 → 4a798ee → da736de → cdc1ff1 → a02d11d → 197794d → 42106b6 → 54839dc → 115bfa2 → 3633b37 → 547e4ba → cf36e5d → e29edbe → b18643e → 2f7984e → eefbe2f → **8010626** → ffc2b87 → 98fa6c7 → aa9125a (root)

`list_commits` with `sha=ecd9022` returns only commits reachable from ecd9022, and the path-filtered queries above returned 8010626 for all six pages. Both confirm ancestry.

## How Build can re-check
- `get_commit 801062641f30d2acf45dbea4748323f20c5e30d8`: the six pages are `added`, with the blobs above.
- `list_commits sha=ecd902211abd202711838219b28a1e1b39ae47c4 path=mesh/roles/<page>` for each page.
- Compare blobs at ecd9022, e.g. `get_file_contents ref=ecd9022` then `git hash-object`.

## Addendum, 2026-10-05 16:31 CT: ancestry against the new main 979c35e
Main moved to **979c35e0be9a27ab143c7dcfc714d979b11e10a0** (Merge PR #8; parents ecd902211abd… first, cba4140d… second).
- 979c35e's first parent is ecd9022, and 8010626 is an ancestor of ecd9022 (chain above), so 8010626 is an ancestor of 979c35e.
- `list_commits sha=979c35e path=mesh/roles/<page>` returned the same results as at ecd9022 for all six pages:
  - who-tessera-is.md: f71e00a0 then 8010626
  - the other five: 8010626 only
- PR #8 did not touch any of the six pages (its 21 files are listed in apply-979c35e/pr8-979c35e-blobs.tsv). Their blobs at 979c35e are the ecd9022 blobs above.

The full SHA 801062641f30d2acf45dbea4748323f20c5e30d8 is still correct for all six notes on 979c35e.
