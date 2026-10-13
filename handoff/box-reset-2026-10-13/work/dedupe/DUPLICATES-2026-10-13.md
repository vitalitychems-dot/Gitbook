# Duplicate file scan — 2026-10-13

**Mode:** read-only (no delete / move / hardlink).
**Tool:** custom Python size-then-SHA256 (`/workspace/dedupe/scan_dupes.py`); `jdupes`/`fdupes` not installable (no root).
**Roots:** `/workspace`, `/home/box`.
**Skipped dirs:** `.git` (entire tree, including `objects/`), `proc`, `sys`, `dev`. Symlinks skipped.
**Hardlinks:** same `(dev,ino)` counted once (not treated as reclaimable duplicates).

## Disk usage (at report time)

| Filesystem | Size | Used | Avail | Use% |
|---|---:|---:|---:|---:|
| `/` (`/dev/vdb`) | 125G | ~113G | ~13G | **90%** |

At scan start: 112G used / 14G avail (90%). Peaked at **99%** (~1.9G free) when a redundant Gitbook gate clone landed under `/tmp/build-gb070-*` (11G) beside existing `/tmp/gb70` (11G). Build removed only its own temp clone; box returned to ~90%.

- `/workspace` tree indexed content (excl `.git`): **66.84 GB** across **305,496** files
- Scan runtime: **107.8s**
- Files hashed (size collisions): **240,378**; hardlink skips: **53,773**
- `node_modules` (included in scan, reported separately): **54,400** files, **720.08 MB**

## Reclaimable duplicate bytes (content-identical, keep 1 copy)

| Metric | Bytes | Human |
|---|---:|---:|
| **Total reclaimable** `(n-1)*size` | 21,902,296,428 | **20.40 GB** |
| Excluding groups that are 100% under `node_modules` | 21,878,102,596 | 20.38 GB |
| Groups entirely inside `node_modules` | 24,193,832 | 23.07 MB |
| Duplicate groups | 19,582 | |

> Note: because `.git` was skipped, multi-gigabyte bare/mirror clones of TESSERA/Gitbook are **not** in this total. See leftover section — they dwarf content dupes.

## Top 30 duplicate groups by wasted space

### 1. wasted **1.40 GB** — file size 89.30 MB × 17 copies
- sha256 `b7a2b5e239f8064f…`
```
/workspace/build-gate/full-f76d/archive/from-gitbook/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/einstein/r4/archive/from-gitbook/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/einstein/round3/tess/archive/from-gitbook/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/gitmesh/repo/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/rea-batch/amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/rea-batch/amber-flame-tiger-sand/artifacts/drive/tesseract_consolidated.zip
/workspace/rea-batch/b3-collink1007_amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/rea-batch/b3-collink1007_amber-flame-tiger-sand/artifacts/drive/tesseract_consolidated.zip
/workspace/rea-batch/b3-collink1007_z/artifacts/drive/1e3Vip.zip
/workspace/rea-batch/b3-collink1007_z/artifacts/drive/tesseract_consolidated.zip
/workspace/rea-batch/tessera-v2/archive/from-gitbook/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/rick/src/Gitbook/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/tb3/archive/from-gitbook/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/tess-opt/archive/from-gitbook/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/tv3/archive/from-gitbook/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
/workspace/tw/archive/from-gitbook/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip
```

### 2. wasted **315.00 MB** — file size 45.00 MB × 8 copies
- sha256 `996102e83517161c…`
```
/workspace/build-gate/full-f76d/archive/sections/3_9_1776105526328/part-04
/workspace/einstein/r4/archive/sections/3_9_1776105526328/part-04
/workspace/einstein/round3/tess/archive/sections/3_9_1776105526328/part-04
/workspace/rea-batch/b2-TESSERA/archive/sections/3_9_1776105526328/part-04
/workspace/rea-batch/tessera-v2/archive/sections/3_9_1776105526328/part-04
/workspace/tess-opt/archive/sections/3_9_1776105526328/part-04
/workspace/tv3/archive/sections/3_9_1776105526328/part-04
/workspace/tw/archive/sections/3_9_1776105526328/part-04
```

### 3. wasted **315.00 MB** — file size 45.00 MB × 8 copies
- sha256 `0f5a4962a0d37372…`
```
/workspace/build-gate/full-f76d/archive/sections/3_9_1776105526328/part-03
/workspace/einstein/r4/archive/sections/3_9_1776105526328/part-03
/workspace/einstein/round3/tess/archive/sections/3_9_1776105526328/part-03
/workspace/rea-batch/b2-TESSERA/archive/sections/3_9_1776105526328/part-03
/workspace/rea-batch/tessera-v2/archive/sections/3_9_1776105526328/part-03
/workspace/tess-opt/archive/sections/3_9_1776105526328/part-03
/workspace/tv3/archive/sections/3_9_1776105526328/part-03
/workspace/tw/archive/sections/3_9_1776105526328/part-03
```

### 4. wasted **315.00 MB** — file size 45.00 MB × 8 copies
- sha256 `b2cfd889f271df96…`
```
/workspace/build-gate/full-f76d/archive/sections/3_9_1776105526328/part-01
/workspace/einstein/r4/archive/sections/3_9_1776105526328/part-01
/workspace/einstein/round3/tess/archive/sections/3_9_1776105526328/part-01
/workspace/rea-batch/b2-TESSERA/archive/sections/3_9_1776105526328/part-01
/workspace/rea-batch/tessera-v2/archive/sections/3_9_1776105526328/part-01
/workspace/tess-opt/archive/sections/3_9_1776105526328/part-01
/workspace/tv3/archive/sections/3_9_1776105526328/part-01
/workspace/tw/archive/sections/3_9_1776105526328/part-01
```

### 5. wasted **315.00 MB** — file size 45.00 MB × 8 copies
- sha256 `467e9d54015e0a0a…`
```
/workspace/build-gate/full-f76d/archive/sections/3_9_1776105526328/part-02
/workspace/einstein/r4/archive/sections/3_9_1776105526328/part-02
/workspace/einstein/round3/tess/archive/sections/3_9_1776105526328/part-02
/workspace/rea-batch/b2-TESSERA/archive/sections/3_9_1776105526328/part-02
/workspace/rea-batch/tessera-v2/archive/sections/3_9_1776105526328/part-02
/workspace/tess-opt/archive/sections/3_9_1776105526328/part-02
/workspace/tv3/archive/sections/3_9_1776105526328/part-02
/workspace/tw/archive/sections/3_9_1776105526328/part-02
```

### 6. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `e8f4e8daefbce456…`
```
/workspace/gitmesh/repo/archive/drive-rest/8-2/part-01
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/8-2/part-01
/workspace/rick/src/Gitbook/archive/drive-rest/8-2/part-01
```

### 7. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `23ca5f12d07f2340…`
```
/workspace/gitmesh/repo/archive/drive-rest/8-2/part-03
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/8-2/part-03
/workspace/rick/src/Gitbook/archive/drive-rest/8-2/part-03
```

### 8. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `aa64566a90f2e017…`
```
/workspace/gitmesh/repo/archive/drive-rest/8-2/part-02
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/8-2/part-02
/workspace/rick/src/Gitbook/archive/drive-rest/8-2/part-02
```

### 9. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `a19ac8f99768e958…`
```
/workspace/gitmesh/repo/archive/drive-rest/8-2/part-06
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/8-2/part-06
/workspace/rick/src/Gitbook/archive/drive-rest/8-2/part-06
```

### 10. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `04161576c76f5acd…`
```
/workspace/gitmesh/repo/archive/drive-rest/8-2/part-05
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/8-2/part-05
/workspace/rick/src/Gitbook/archive/drive-rest/8-2/part-05
```

### 11. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `8d1bfb4ef584fc5d…`
```
/workspace/gitmesh/repo/archive/drive-rest/8-2/part-07
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/8-2/part-07
/workspace/rick/src/Gitbook/archive/drive-rest/8-2/part-07
```

### 12. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `aeb6f85c3d08ef8a…`
```
/workspace/gitmesh/repo/archive/drive-rest/8-2/part-04
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/8-2/part-04
/workspace/rick/src/Gitbook/archive/drive-rest/8-2/part-04
```

### 13. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `8f59b59d4cd90039…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseract-AI-5/part-03
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseract-AI-5/part-03
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseract-AI-5/part-03
```

### 14. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `3d32b2b05f81b4d5…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseract-AI-5/part-02
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseract-AI-5/part-02
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseract-AI-5/part-02
```

### 15. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `dee619454812e8fe…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseract-AI-5/part-06
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseract-AI-5/part-06
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseract-AI-5/part-06
```

### 16. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `704df7df7b78b4da…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseract-AI-5/part-05
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseract-AI-5/part-05
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseract-AI-5/part-05
```

### 17. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `672ca32fef89c738…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseract-AI-5/part-08
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseract-AI-5/part-08
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseract-AI-5/part-08
```

### 18. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `b1d9e0ecff333ed6…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseract-AI-5/part-04
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseract-AI-5/part-04
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseract-AI-5/part-04
```

### 19. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `aeb83d2a01bc8e26…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseract-AI-5/part-01
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseract-AI-5/part-01
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseract-AI-5/part-01
```

### 20. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `25e816c5df5b249e…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseract-AI-5/part-07
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseract-AI-5/part-07
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseract-AI-5/part-07
```

### 21. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `ef3a3663ca8c47fc…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseracxt9/part-05
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseracxt9/part-05
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseracxt9/part-05
```

### 22. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `0e1883912533d958…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseracxt9/part-04
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseracxt9/part-04
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseracxt9/part-04
```

### 23. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `fd3f0b939f628c20…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseracxt9/part-08
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseracxt9/part-08
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseracxt9/part-08
```

### 24. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `09316d05d244f0b7…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseracxt9/part-10
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseracxt9/part-10
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseracxt9/part-10
```

### 25. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `a18a2bcbde91627b…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseracxt9/part-12
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseracxt9/part-12
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseracxt9/part-12
```

### 26. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `798e6a8aceb59a1b…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseracxt9/part-03
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseracxt9/part-03
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseracxt9/part-03
```

### 27. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `00e4c849c3831d00…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseracxt9/part-09
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseracxt9/part-09
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseracxt9/part-09
```

### 28. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `ead74048798ea513…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseracxt9/part-02
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseracxt9/part-02
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseracxt9/part-02
```

### 29. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `6c63ae6186f89331…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseracxt9/part-07
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseracxt9/part-07
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseracxt9/part-07
```

### 30. wasted **90.00 MB** — file size 45.00 MB × 3 copies
- sha256 `33c26fce2a5bf7bf…`
```
/workspace/gitmesh/repo/archive/drive-rest/Tesseracxt9/part-11
/workspace/rea-batch/v2-rea/Gitbook-novault/archive/drive-rest/Tesseracxt9/part-11
/workspace/rick/src/Gitbook/archive/drive-rest/Tesseracxt9/part-11
```

## Breakdown by top-level folder (wasted bytes attributed to extra copies)

Waste is attributed to every path in a group except the lexicographically first (kept).

| Folder | Wasted (extra copies) | All dup-bytes residing here |
|---|---:|---:|
| `/workspace/rea-batch` | 9.02 GB | 9.97 GB |
| `/workspace/rick` | 5.88 GB | 5.88 GB |
| `/workspace/einstein` | 1.47 GB | 1.47 GB |
| `/workspace/tv3` | 744.95 MB | 744.95 MB |
| `/workspace/tw` | 744.15 MB | 744.15 MB |
| `/workspace/tess-opt` | 743.75 MB | 743.75 MB |
| `/workspace/gitmesh` | 558.07 MB | 5.83 GB |
| `/workspace/tb3` | 532.40 MB | 532.40 MB |
| `/workspace/repo-lab` | 292.14 MB | 305.87 MB |
| `/workspace/rea-inventory` | 241.51 MB | 248.91 MB |
| `/workspace/build-gate` | 63.94 MB | 799.43 MB |
| `/workspace/node22` | 53.03 MB | 54.87 MB |
| `/workspace/tools` | 46.30 MB | 47.60 MB |
| `/workspace/agent-tools` | 37.07 MB | 60.90 MB |
| `/home/box/.local` | 23.36 MB | 35.21 MB |
| `/workspace/pubscan` | 13.74 MB | 13.74 MB |
| `/workspace/build-plan-2026-10-12` | 10.89 MB | 10.92 MB |
| `/workspace/consolidation` | 8.82 MB | 8.82 MB |
| `/home/box/.corepack` | 3.34 MB | 22.69 MB |
| `/workspace/gitbook-cordnation` | 1.40 MB | 1.98 MB |
| `/workspace/cloud-agent-artifacts` | 1.15 MB | 1.15 MB |
| `/home/box/chrome-profile` | 1.05 MB | 2.06 MB |
| `/workspace/tessera-brain` | 366.04 KB | 732.01 KB |
| `/workspace/improve-from-logs-2026-10-12` | 274.66 KB | 290.32 KB |
| `/home/box/.npm` | 258.46 KB | 14.61 MB |
| `/workspace/security-gate` | 186.97 KB | 186.97 KB |
| `/home/box/.cache` | 144.16 KB | 54.14 MB |
| `/workspace/evals` | 96.46 KB | 131.26 KB |
| `/home/box/.cursor` | 77.77 KB | 155.55 KB |
| `/workspace/gitbook-gate-feaeb55` | 66.89 KB | 66.89 KB |
| `/workspace/rea-categories` | 66.39 KB | 68.60 KB |
| `/workspace/gitbook-gate-feaeb558` | 61.92 KB | 61.92 KB |
| `/workspace/gitbook-gate-beadc44` | 61.87 KB | 61.87 KB |
| `/workspace/gitbook-gate-e73fb185` | 54.48 KB | 54.48 KB |
| `/workspace/gitbook-gate-fb984ad` | 53.96 KB | 53.96 KB |
| `/workspace/gitbook-gate-1e3bb50` | 49.64 KB | 53.96 KB |
| `/workspace/build-o` | 40.23 KB | 40.23 KB |
| `/home/box/sand-data` | 29.34 KB | 16.20 MB |
| `/workspace/sec-retro` | 26.12 KB | 26.25 KB |
| `/workspace/tess-fix.git` | 25.73 KB | 25.73 KB |
| *(other folders)* | 140.34 KB | |

### node_modules note

- Indexed under `node_modules`: 720.08 MB
- Reclaimable if entire duplicate group is only `node_modules` paths: 23.07 MB
- Largest `node_modules` tree observed: `/workspace/einstein/round3/tess/node_modules` (~724 MB).

## Obvious safe reclaim candidates (NOT counted as content-duplicates)

These were **excluded from hashing** (`.git`) or are large unique leftovers. **Do not delete without owner confirmation.** Listed for triage only.

### A. Stale / parallel git packs & bare clones (`.git` skipped by scan)

| Size | Path |
|---:|---|
| 5.53 GB | `/workspace/einstein/round3/tess/.git/objects/pack/pack-3771bc3cad12d4181995ad3175dd42bca8407cc6.pack` |
| 5.53 GB | `/workspace/sec-history/TESSERA/objects/pack/pack-4347c62a3dcc1b35046116e671d937112241aae8.pack` |
| 5.53 GB | `/workspace/backups/TESSERA-pre-public-2026-10-12.git/objects/pack/pack-c91dc3d0f1700c99b911b0d9949fe95852cc3d7d.pack` |
| 5.53 GB | `/workspace/pubscan/final.git/objects/pack/pack-719892dff20d88d66fb6d46f3df1a7c721de37bf.pack` |
| 5.53 GB | `/workspace/sec-retro/TESSERA/objects/pack/pack-ee3591da5678917b7c77dad00a33ae4bd161e82b.pack` |
| 5.33 GB | `/workspace/gitmesh/repo/.git/objects/pack/pack-d6655ef7eda4b140d30850f38b3957a7c14d77bb.pack` |
| 4.97 GB | `/workspace/rick/src/Gitbook/.git/objects/pack/pack-1c9ffe52533801881646d26146f8fe193b0c95db.pack` |
| 4.97 GB | `/workspace/rea-batch/v2-rea/Gitbook-novault/.git/objects/pack/pack-3ef1806fc7f633ec09ada89d8a01b0d439911e0b.pack` |
| 4.79 GB | `/workspace/tess-opt/.git/objects/pack/pack-b04c9e2b2eabb4b3113202a78b4a75b5bf4eaecf.pack` |
| 509.00 MB | `/workspace/einstein/r4/.git/objects/pack/pack-248d3ae160f33612264a11dc7846030959b50417.pack` |
| 508.81 MB | `/workspace/tw/.git/objects/pack/pack-2b3fb412f6712f4c227603a9e56335242045c48d.pack` |
| 508.05 MB | `/workspace/tess-opt/.git/objects/pack/pack-dfe7503ec6a9634df3dac11a3eb8282355cad3c0.pack` |
| 507.92 MB | `/workspace/rea-batch/tessera-v2/.git/objects/pack/pack-cd74ece976311358c7801ed2eed91e4d6f3c6c31.pack` |
| 507.47 MB | `/workspace/build-gate/full-f76d/.git/objects/pack/pack-45a48ea67c553f25b50def6f07768acaac5f3ff0.pack` |
| 465.63 MB | `/workspace/rea-batch/vitality/.git/objects/pack/pack-8aefd9f1a07317e1d724e6b967d215bf423fa4f3.pack` |
| 465.63 MB | `/workspace/rea-batch/b2-vitality/.git/objects/pack/pack-8aefd9f1a07317e1d724e6b967d215bf423fa4f3.pack` |

Sum of packs ≥400 MB: **51.11 GB** across 16 files.

Head/tail fingerprints of four ~5.6G TESSERA-related packs differ (not byte-identical), but they are redundant *purpose* clones (sec-retro, sec-history, pubscan, backups, einstein/round3, gitmesh, tess-opt, rick/src/Gitbook, rea-batch mirrors). Keeping **one** canonical clone + the intentional backup would free tens of GB.

Same pack filename appearing in multiple trees (likely identical mirrors):

- `pack-8aefd9f1a07317e1d724e6b967d215bf423fa4f3.pack` (465.63 MB) × 2
  - `/workspace/rea-batch/vitality/.git/objects/pack/pack-8aefd9f1a07317e1d724e6b967d215bf423fa4f3.pack`
  - `/workspace/rea-batch/b2-vitality/.git/objects/pack/pack-8aefd9f1a07317e1d724e6b967d215bf423fa4f3.pack`

### B. `/tmp` leftovers ≥10 MB

| Size | Path |
|---:|---|
| 10.81 GB | `/tmp/gb70` |
| 10.81 GB | `/tmp/build-gb070-210571` |
| 238.40 MB | `/tmp/pv` |
| 56.69 MB | `/tmp/eye5-chrome` |
| 38.63 MB | `/tmp/g70` |

Notable: `/tmp/gb70` (~2.1G) looks like an in-progress Gitbook gate clone at tip `243ddd4b`.

### C. `/workspace/build-gate` stale worktrees / Node tarball

| Size | Path | Notes |
|---:|---|---|
| 1.22 GB | `/workspace/build-gate/full-f76d` | stale gate clone / toolchain |
| 176.30 MB | `/workspace/build-gate/node-v22.20.0-linux-x64` | stale gate clone / toolchain |
| (many small) | `/workspace/build-gate/work-*` | old per-PR work dirs |

### D. Duplicate Node 22 binaries (~118–120 MB each)

- 119.05 MB `/workspace/node22/bin/node`
- 117.48 MB `/workspace/build-gate/node-v22.20.0-linux-x64/bin/node`
- 116.04 MB `/workspace/tools/node22/bin/node`

### E. Ollama install + models (unique content, large)

- 3.49 GB `/workspace/ollama-install`
- 2.11 GB `/workspace/ollama-home`

## Policy recommendation (from Father: never save duplicates)

1. Before cloning a repo for a gate, check for an existing checkout at the needed SHA under `/tmp` or `/workspace/build-gate` and reuse it.
2. Prefer one shared `node` toolchain path; do not unpack Node into every gate dir.
3. Archive/zip artifacts under `archive/` and `artifacts/drive/` are the top content-dupe offenders — store once, reference by hash.
4. Bare mirrors for secret-scan (`sec-*`, `pubscan`) should be a single shared bare repo with worktrees, not full copies.
5. Auto-detect: run this scanner (or `jdupes -r -S`) before large writes; refuse to save a file whose sha256 already exists elsewhere on the box.

## Artifacts

- `/workspace/dedupe/DUPLICATES-2026-10-13.md` (this file)
- `/workspace/dedupe/scan-summary.json`
- `/workspace/dedupe/all-groups.jsonl` (all groups)
- `/workspace/dedupe/scan_dupes.py`

Generated: 2026-10-13 04:32:35 CDT
