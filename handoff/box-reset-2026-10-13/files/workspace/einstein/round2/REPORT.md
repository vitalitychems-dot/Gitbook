# Einstein round 2 (2026-10-13). Base: TESSERA main f91ff82c (includes #263, #264, #265)
Overlap: TESSERA had 0 open PRs. Gitbook's open PRs #39 (archive pack) and #40 (docs) do not overlap.
1. Embedding cache key. File: artifacts/api-server/src/lib/neural-embeddings.ts (hashText).
   Wrong cached embeddings on REAL data (all 517 tracked TESSERA .md files, real generateEmbedding, compared with a fresh module instance): 6/517 (1.16%, Wilson 95% CI 0.53 to 2.51%) before, 0/517 after. All 6 discordant pairs favor the fix (exact McNemar p=0.031). KEEP.
   Tests: api-server vitest 464 to 465 passing (adds 1 regression test, which fails on the old code). The one failing file, invention-glb-upload, also fails on base. tsc shows no new errors.
   Branch: einstein/r2-01-embed-cache-key (local). Patch: patches/0001-fix-embeddings-key-the-embedding-cache-on-the-whole-.patch. Bench: bench/emb-cache-key.bench.test.ts, c1-before.json, c1-after.json
2-10. Not built in this pass.
Rick #3: see the final message.
