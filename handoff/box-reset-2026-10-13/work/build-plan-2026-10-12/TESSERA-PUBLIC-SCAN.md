# TESSERA public-readiness scan + scrub (2026-10-12, CT). Values redacted; file/commit/type only.

## Backup (never delete)
- /workspace/backups/TESSERA-pre-public-2026-10-12.git (mirror, all 495+ refs incl refs/pull/*, refreshed to main 6a64396b at ~6:50 PM CT)
- git-crypt key: /workspace/backups/TESSERA-git-crypt.key (chmod 600, not printed)

## Pre-scrub findings (gitleaks 8.21.2, --all, 50 hits)
1 - generic-api-key | archive/from-gitbook/archive/moved/Zz/artifacts/z-app/data/ingest/1e44d8b943c4248f.txt | c535df98
1 - generic-api-key | archive/from-gitbook/archive/moved/Zz/artifacts/z-app/data/ingest/e7ee9a19bfd44fc4.txt | 763ed988
1 - generic-api-key | archive/from-gitbook/archive/moved/Zz/artifacts/z-app/data/ingest/e7ee9a19bfd44fc4.txt | c535df98
1 - generic-api-key | archive/from-gitbook/archive/moved/Zz/artifacts/z-app/src/lib/auth/preview.ts | c535df98
1 - generic-api-key | archive/from-gitbook/archive/moved/collink1007-XXX/.replit | c535df98
30 - generic-api-key | archive/from-gitbook/archive/moved/collink1007-XXX/tess/data/secret-society.json | c535df98
1 - generic-api-key | archive/from-gitbook/archive/moved/collink1007-XXX/tess/server/agi-implementations.ts | c535df98
1 - generic-api-key | archive/from-gitbook/archive/moved/collink1007-XXX/tess/server/realification-conference.ts | c535df98
1 - generic-api-key | archive/from-gitbook/archive/moved/collink1007-XXX/tess/server/summit-37-parallel-universes.ts | c535df98
1 - generic-api-key | archive/from-gitbook/archive/moved/collink1007-XXX/x/tess/server/agi-implementations.ts | c535df98
1 - generic-api-key | archive/from-gitbook/archive/moved/collink1007-XXX/x/tess/server/realification-conference.ts | c535df98
1 - generic-api-key | archives/source-repositories/Zz/artifacts/z-app/src/lib/auth/preview.ts | 9538b364
1 - generic-api-key | artifacts/api-server/src/__tests__/colonial-secret-fail-closed.test.ts | 0a69be53
1 - generic-api-key | artifacts/api-server/src/__tests__/compression-pipeline.test.ts | 0a69be53
1 - generic-api-key | preview/src/lib/auth/preview.ts | 34556936
1 - github-pat | artifacts/api-server/src/__tests__/learning-memory.test.ts | 06c64e65
1 - jwt | archive/drive-rest/share-2c60.html | f5cc6af5
1 - jwt | archive/drive-rest/share-3ad6.html | f5cc6af5
1 - jwt | archive/from-gitbook/archive/moved/collink1007-XXX/tess/server/sovereign-security-tester.ts | 763ed988
1 - jwt | archive/from-gitbook/archive/moved/collink1007-XXX/tess/server/sovereign-security-tester.ts | c535df98
1 - private-key | artifacts/api-server/src/__tests__/pen-local.test.ts | 3630e96c
Plus sensitive paths: natal-vault.json (T44 + artifacts/api-server/.local-data), 1T/ tree, archive .replit files, secret-society.json, drive-rest share html (Google share JWTs), Zz data/ingest.
Matches Security SEC-TESSERA-HISTORY-SCRUB.md.

## Scrub applied (git filter-repo, local mirror /workspace/pubscan/work.git, refs/pull/* dropped locally)
- --invert-paths: exact PATHS list from SEC doc + globs **/.local-data/**, **/natal-vault* (file: /workspace/pubscan/paths2.txt)
- --replace-text: all 11 SEC regex PATTERNS (-> ***REMOVED***) + preview secret literal + 37 other gitleaks literals (non-test). Expressions file is local only, umask 077: /workspace/pubscan/priv/expr.txt (uncommitted, contains secrets — delete after Father rotates).
- Rewritten main (scrub only): 89961129. Plus commit 43d3d319 (vitalitychems-dot): git-crypt init, .gitattributes for config/secrets/**, **/*.secret.json(l), .env, .env.local; restores learning-memory.test.ts ghp fixture as string concat (regex had blanked it).
- NOT encrypted: docs/v2/v2-memory.jsonl, data/school/*.jsonl — v2 tests read them (CI would break); no emails/keys found in them.

## Post-scrub re-scan (all local refs)
- gitleaks --all: 2 hits, both FIXTURE (colonial-secret-fail-closed.test.ts, compression-pipeline.test.ts).
- SEC regex pass over git log -p --all: 0 hits.  Literal pass (all original secret values): 0 hits.
- Sensitive path presence in any ref: 0.

## Caveats
- GitHub keeps refs/pull/* (PR heads, read-only) and cached commit views server-side after force-push; old SHAs stay fetchable by SHA until GitHub Support purges. Need Support request or accept residual risk before public.
- Remote main keeps moving (cloud agent bc-26260d7a: 6a64396b -> 960a62ff during scrub). Rewrite must be redone against latest remote right before force-push, with the agent paused, or its old-history branches will reintroduce scrubbed commits.

## Rotate (types only)
TESSERACT_ADMIN_KEY (collink1007-XXX/.replit, looks real); preview client secret (preview.ts); confirm placeholders for ~20 vars in collink1007-XXX/tess/.replit (OpenRouter/xAI/Gemini/GitHub/SOL/ETH/BTC private keys etc.); Drive share JWTs (likely expired).

## Open PRs needing rebase after rewrite
#194 desk/consolidation-pointer, #110 cursor/site-002-diagnostics-gate-7ea3, #87 security/gate-system-runtime-and-shadow-winners, #82 fix/api-server-db-optional-boot, #80 feat/local-pen-adapter. (PR heads on old history; GitHub refs/pull/* for all closed PRs keep old history too.)
