# Build state — 2026-10-13

## Role
Verify-only gate. Mark **TESTED** only if Build ran it; otherwise **REPORTED**. Never merge. Post only labeled **Build** verdicts, and only with Father's yes in Build's chat.

## Current work
Gitbook #96 @ `77c387f1` and #97 @ `41be7616` gated (both PASS TESTED). Waiting to post verdicts.

## Where left off
Verdicts not yet posted on PRs — waiting for Father's yes in Build's chat (Tessera reports "I approve" at 9:01 CT in her chat; Build still needs yes here).

### PASS (TESTED)
| PR | Head | Notes |
|---|---|---|
| TESSERA #310 | `a64e5521` | |
| TESSERA #312 | `1f0cbf05` | merged 8:57 CT (Security ungated — Tessera investigating) |
| TESSERA #313 | `54b8a84c` | |
| TESSERA #314 | `62ec1d53` | Moderator PASS prior |
| TESSERA #315 | `791ef5da` | |
| TESSERA #316 | `cbc1f911` | deletes collink1007-* from tree (history kept); Father 7:54 |
| TESSERA #317 | `f9b2d7a4` | |
| TESSERA #318 | `dda57c2c` | |
| Gitbook #90 | `e99398f8` | |
| Gitbook #91 | `eedc736c` | |
| Gitbook #92 | `7ed7edb0` | re-gate after .pyc strip |
| Gitbook #96 | `77c387f1` | r2 after Security HIGH fixes; prior `d4a8bb66` superseded |
| Gitbook #97 | `41be7616` | state handoff docs only |

### Retro PASS
TESSERA #319–#322 ungated merges: all PASS. #320 claimed ~40% predict speedup; Build measured 5–12% — ask Tessera to correct note. #321/#322 claims matched.

## Wipe incident
Father approved wipe 8:40–8:43 CT. Freed ~60 GB (85%→41%). **Bug:** 45 live files deleted (moderator-tools incl. `score.py`, akhenaten/ritual/*, ops/deletion-list*, autoclean.sh). `/workspace/si/gb` broken; ~7 unpushed commits under recovery audit. Restoration in progress.

**Lesson:** exclude `ops/`, `moderator-tools/`, `akhenaten/`; confirm each file by **git hash**, not inventory size. Freeze further deletes until Tessera's file-loss report.

## Next
1. On Father's yes in Build chat: post labeled Build PASS/FAIL on waiting PRs (never for Security; never merge).
2. Finish restore + report lost vs recovered to Tessera/Father.
3. Spec suite-cache-per-main-SHA + one-command JSON runner (Rick/Mesh build; Build gates).

Gate detail: `state/build/GATE-2026-10-13-*.md` and `state/build/build.md`.
