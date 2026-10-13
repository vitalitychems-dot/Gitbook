# Deletion list (PROPOSAL ONLY) — 2026-10-13

Nothing deleted. Every item waits for Father's explicit yes. 1T/vault paths excluded entirely. Disk: 98G/125G used (79%).

## (a) Box duplicate clones/worktrees
Checked: `git status --porcelain` (dirty) and `git log --branches --not --remotes` (unpushed). Keep-copy: TESSERA -> /workspace/build-gate/tessera; Gitbook -> /workspace/si/gb; amber-flame-tiger-sand -> rea-batch/amber-flame-tiger-sand; others unique.

### a1. Eligible (clean, nothing unpushed)
|path|repo|MB|
|-|-|-|
|/workspace/fatherlogin-fallback/TESSERA|TESSERA|4|
|/workspace/fatherlogin-fallback/Gitbook|Gitbook|3|
|/tmp/t299|TESSERA|1270|

Subtotal a1: 1277 MB

### a2. NOT eligible yet (dirty and/or unpushed): owner must push or confirm first
|path|repo|dirty files|unpushed commits|MB|
|-|-|-|-|-|
|/workspace/repo-lab/crewAIInc__crewAI|crewAI|1|0|316|
|/workspace/build-gate/tessera|TESSERA|3|4|6548|
|/workspace/rea-batch/b2-Gitbook|Gitbook|2|1|3413|
|/workspace/rea-batch/tessera-v2|TESSERA|2|0|1258|
|/workspace/rea-batch/amber-flame-tiger-sand|amber-flame-tiger-sand|2|0|240|
|/workspace/rea-batch/b3-collink1007_amber-flame-tiger-sand|amber-flame-tiger-sand|2|0|240|
|/workspace/rea-batch/b3-collink1007_z|z|10|0|265|
|/workspace/rea-batch/onnxruntime-web|onnxruntime|3|0|805|
|/workspace/tess-opt|TESSERA|2|14|6170|
|/workspace/tw|TESSERA|2|3|1264|
|/workspace/einstein/round3/tess|TESSERA|2|0|6423|
|/workspace/einstein/r4|TESSERA|2|6|1264|
|/workspace/tv3|TESSERA|2|14|753|
|/workspace/gitmesh/repo|Gitbook|7|0|11434|
|/workspace/tb3|TESSERA|1|1|870|
|/workspace/sec-retro/gbfix/r|Gitbook|3|0|3|
|/workspace/si/tsr|TESSERA|0|22|1994|
|/workspace/si/gb|Gitbook|1|7|11091|
|/workspace/si/wt-gb|Gitbook|0|7|1|
|/workspace/si/wt-fb|TESSERA|0|22|757|
|/workspace/codeowners-followup/TESSERA|TESSERA|0|1|2|
|/workspace/codeowners-followup/Gitbook|Gitbook|0|1|3|
|/workspace/fix-agent-login|TESSERA|0|1|10|
|/tmp/tess|TESSERA|2|0|1267|

Subtotal a2: 56391 MB (keep-copies are in this list and are NOT to be deleted)

**Section (a) total listed: 57668 MB**

## (b) Temp/cache dirs
|path|MB|
|-|-|
|/home/box/.cache (uv/pip/npm; regenerable)|740|
|/tmp/node-compile-cache, /tmp/fix, playwright profiles|~23|
|/workspace/si/node-v22.20.0-linux-x64 (dup; keep build-gate copy)|185|

**Section (b) total: ~948 MB**

## (c) Repo files: archive as tar.zst into private Gitbook FIRST, then delete via gated PR
|repo|item|bytes|note|
|-|-|-|-|
|Gitbook|duplicate archive trees (1843 groups)|18,428,248|keep one copy each|
|TESSERA|archive/from-gitbook/archive/moved/* duplicates of archives/source-repositories/* (86 groups)|3,473,145|keep archives/source-repositories|
|TESSERA|theme files (4, listed below)|6,904|REVIEW: may be live code, not confirmed old|
|Gitbook|theme files under archive/moved/Zz/ (2)|183|archive copies|

**Section (c) total: ~21.9 MB (21,908,480 bytes)**

TESSERA theme files:
- artifacts/tessera/src/lib/theme-constants.ts
- preview/src/components/tessera/theme-view.tsx
- preview/src/lib/tessera/themes.test.ts
- preview/src/lib/tessera/themes.ts
