# GB-017: content rebase onto feaeb558 (Tessera task 15:42 CT)

> **Base update (Tessera 15:46 CT):** the final base is **f4b2c41** (`f4b2c41ee458e54fc4f12cecd4cab941aa8e627c`), which is PR #5 merged on top of feaeb558. PR #5 landed GB-015, 019, 021 and 020.
> - A snapshot of feaeb558 with those 4 diffs applied matches every one of the 8 PR #5 blobs (`git hash-object`).
> - PR #5 did not touch flow.md, roles.md, command-center.md, agent-checkins.md, SUMMARY.md or the operating-mode page.
> - This package's diff regenerated on f4b2c41 is **byte-identical** to the feaeb558 version. It is saved as `*.f4b2c41.diff`, and `*.feaeb558.diff` is kept as an identical copy.
> - Copies are in `base-f4b2c41/` and `proposed-f4b2c41/`.
> - Apply checks on f4b2c41: solo OK, 0 offsets; stack 017 → 018 → 016 rev 3.2 OK, 0 offsets.


- **Main:** `feaeb558b88df9679a45b4a03a375f58e50bcb4d`, 0 open PRs (~15:44 CT).
- **Base:** feaeb558 + GB-015. GB-015 touches only grok-bot.md, so GB-017 also applies directly on feaeb558.
- **New diff:** `GB-017.feaeb558.diff`, 164 lines, sha256 `49028bee3aa3f9662ca7481c7c1dd370a2ab7e673ff9fa39d0e52801034c5fe0`. The old `GB-017.diff` (ca3ef700) is kept.
- **Copies:** `base-f4b2c41/` and `proposed-f4b2c41/` hold the 5 files.

**Verdict: CONTENT CHANGE.** It needs all four gates (Moderator, Tessera, Security, CI/Build) and a fresh Father yes.

## What feaeb558 changed under GB-017

- **flow.md:** front matter (published + new note), operating-model link, approval rule, pipeline, diagram, 3 standing rows, lane boundaries (Tessera Grok bot/CC, Tessera, **Tessera Pen — directs scoped work…**) and a related-pages link.
- **roles.md:** front matter (published + new note), new banner `> **Status: published — operating model aligned**`, CC/TESSERA rows, **Pen row → "Configured / live participation requires check-in | Directs scoped work and protects coherence"**, the path sentence, and the "See flow" note.
- **SUMMARY.md:** added an operating-model nav line, so the GB-017 hunk shifts by +1.

## Hunk decisions

| File | GB-017 (1e3) did | feaeb558 state | feaeb558 rebase does | Type |
|---|---|---|---|---|
| flow.md front matter | `status: corrected-pending-publish` → `published` | already `published` with a new note | nothing; feaeb558 front matter kept | redundant, dropped |
| flow.md Tessera identity row | added after Status truth | — | same row, same text, re-anchored | unchanged content |
| flow.md Security lane bullet | added after Build | — | same bullet, re-anchored | unchanged content |
| flow.md Tessera Pen lane bullet | (did not exist) | feaeb558 added "**Tessera Pen** — directs scoped work and protects coherence; does not push or merge." | becomes "**Tessera Pen** — not a lane: Tessera's own writing voice (see Tessera identity above); does not push or merge." | **NEW, content (Pen is not a lane)** |
| roles.md front matter + banner | `published`; removed the "corrected — pending" banner | already `published`; new banner "published — operating model aligned" | nothing; feaeb558 front matter and its 'Status: published' banner kept | redundant, dropped |
| roles.md Pen row | Provisional → **Not a lane** — Tessera's own writing voice | feaeb558 row "Configured / live participation requires check-in / Directs scoped work…" | replaced by GB-017's row (same text as before) | **content conflict, resolved for GB-017** (feaeb558 row text dropped) |
| roles.md Grok Bot row, Security row, identity Notes bullet | added/changed | unchanged by feaeb558 | same text, re-anchored | unchanged content |
| SUMMARY Grok Bot (Active) | changed | unchanged | same, offset +1 | unchanged content |
| security.md (new), tessera-pen.md | — | not touched by feaeb558 | **byte-identical** sections | unchanged |

Kept from feaeb558: everything except (a) the Pen roster row text and (b) the "directs scoped work and protects coherence" clause on the flow.md Pen bullet. Both conflict with GB-017's "Pen is not a lane". GB-017 does not touch `mesh/TESSERA-GITBOOK-OPERATING-MODE.md`. The same Pen wording there goes to the held GB-022 operating-mode sub-diff.

## Apply check (feaeb558 snapshot)

- Solo: OK, 0 offsets.
- In both stacks: OK, 0 offsets.
