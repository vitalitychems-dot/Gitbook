# Gitbook #72 — Rick results (2026-10-13, all local, tokens=0)
1. **Git as web** (20 pages + CSV): bytes/page tar 2,048 → bundle 192 → bundle.zst 148 (**13.8× smaller**). Full sync: untar 2–8 ms, clone from bundle 12–27 ms, zst+clone 14–36 ms. 1-page update as a delta bundle = 374 B, fetch 8–16 ms, verified. KEPT: plain bundle + delta bundles. zstd gives only −23% more for +~30% time, so keep it optional.
2. Actions local-model: Tessera's loop owns it (not built here).
3. **Offline git queue**: 20/20 jobs claimed→fixed→results committed to a local bare hub, verified (20 results, 20 lines). 2.1–4.5 s (4.5–9.6 jobs/s), **0 tokens**, vs. online stub 10.0 s / 10,000 tokens (the stub assumes 0.5 s + 500 tok/job). KEPT.
4. Identity (#71 gap): Tessera owns it.
5. **Disk / autoclean**: the dedup step was a silent no-op (jdupes skips read-only git objects). Switched to `hardlink -f` on .git/objects. Fixture saved 0 → 57,344 B (6.5%). Box dry run: 786 KiB. KEPT (small). See disk/RESULTS.md.
6. **Read one file**: full clone 17–44 ms/53.8 KB · blobless+sparse 27–68 ms/34.0 KB · git archive path 2.6–7.6 ms/806 B · `git cat-file -p rev:path` 2.1–4.0 ms/806 B · cat worktree 0.01 ms/0 B. All 0 tokens. Winner: cat from an existing worktree. With no worktree: `cat-file`/`archive` beats a full clone by ~10× time and ~67× disk. Blobless clone is slower than a full clone at this size, so DROPPED for small repos.
Ranges = two runs (quiet box vs. loaded). Machine-readable: baseline.json, last_result.json.
