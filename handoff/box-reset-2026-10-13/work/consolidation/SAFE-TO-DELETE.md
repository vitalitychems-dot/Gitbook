# SAFE-TO-DELETE — repo checklist for Father

As-of: 2026-10-05 ~6:00 PM CT. Tessera does **not** delete repos. Father deletes them himself, one exact name at a time.
Inclusion rule: only repos classed **DUPLICATE** or **EMPTY/TRIVIAL** with evidence. **PROTECTED** and **UNKNOWN** repos are excluded.

## ✅ Safe to delete today: **NONE** (TESTED)

The fresh blob-SHA scan (`scan_coverage.py`, `raw/uncovered.json`) found that **every remaining source repo still has files that are not in TESSERA or Gitbook**. The 8 repos that did qualify (empty or 100% covered) were already deleted earlier today: Everything, TX, Tessera-main, tessera-coordination, tessera-gitbook, tessera-replit, tessera-unified, z (REPORTED, Gitbook `merge/DELETION-MANIFEST.md`). This agrees with Gitbook `merge/CURRENT-REPOSITORY-STATUS.md`.

## Near-candidates: what flips each one to DUPLICATE (do not delete yet)

| Repo | Gap today (TESTED) | Becomes safe after | Where the content would then live |
|---|---|---|---|
| `Grok-ready` | 5 unique blobs (3 migration-review JSONs, README, .gitignore) + 3 open PRs | CONS-010 (copy the redacted JSONs/README) + CONS-011 (Father closes #3/#4/#5) + rescan = 0 | TESSERA (code, per HYB-006) + Gitbook `history/recovered/chronology/Grok-ready/` |
| `TESS` | 2 audit logs + the shared 212 MB `attached_assets` set (also in 1/5t/T44) | CONS-014 (log summary) + CONS-016 (media retained in Father's offline zip / one repo) + CONS-015 (declarations data decision) | TESSERA/Gitbook + Father's offline media backup |
| `1` (main only) | 0 unique vs siblings, but the `subrepl-nftoz8d7` branch is live and holds natal-vault | Stays PROTECTED until CONS-018/019 and the Replit agent is detached | — |
| `T44` | `natal-vault.json` + an old `opengraph.jpg` | Stays PROTECTED until CONS-018 (Father keeps the vault privately) and CONS-017 (reject the jpg), then rescan | TESSERA/Gitbook + Father's private copy |
| archive repos ×3 | Opaque ZIP parts, 0 overlap | Stay UNKNOWN until CONS-022 (offline reassembly + sha256 check + Father's verdict) | Father's offline backup + Gitbook manifest |

Never on this list: `TESSERA`, `Gitbook` (destinations), `1T` (PROTECTED vault), `olive-giant-ever-glade` (PROTECTED), `Zz` and `5t` (live Replit use).

## Checklist template (use for each repo once it qualifies)
- [ ] Exact repo name: `vitalitychems-dot/<name>`. Father types it himself.
- [ ] Head SHA frozen, and no pushes since the scan (`list_commits` top SHA == the scan SHA).
- [ ] Rescan shows **0 uncovered blobs** vs TESSERA+Gitbook (or every remaining blob is listed and accepted in Gitbook `merge/`).
- [ ] 0 open PRs and 0 open issues worth keeping.
- [ ] No secrets, personal data, or wallet material remains in the repo, or Father holds it privately.
- [ ] **Backup:** download the zip (GitHub → Code → Download ZIP for each branch, or `git clone --mirror`) to Father's offline storage. Record its sha256 in Gitbook `merge/DELETION-MANIFEST.md`.
- [ ] Gitbook `merge/DELETION-MANIFEST.md` row added (repo, head SHA, coverage %, backup hash, date CT).
- [ ] Father deletes it in GitHub Settings → Danger Zone.
