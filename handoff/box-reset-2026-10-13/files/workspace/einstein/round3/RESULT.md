# Einstein Round 3 RESULT

State: DONE
Finished: 2026-10-13 ~4:33 AM CT

## MERGED (10/10 attempts — all KEEPs)

1. **R3-01 emb-cache-key** — embedding cache keyed on whole text (two FNV-1a + length), not 32-bit hash of first 500 chars.  
   Metric: cache collision wrong count **517→0** on n=517 prefix-sharing pairs; neural-embeddings tests 2→3.  
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/278

2. **R3-02 semantic-cache sysfp** — fingerprint whole system context, not first 500 chars.  
   Metric: distinct fingerprints **1→4 of 4** codex-wrapped DOMAIN_SYSTEM_PROMPTS.  
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/276

3. **R3-03 signed embedText** — signed feature hashing in `vector-memory.embedText`.  
   Metric: mean |cos err| **0.09549→0.04430**; top-1 **0.6450→0.6675** (docs paragraphs).  
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/284

4. **R3-04 hybrid batch rerank** — `generateEmbeddingsBatch` for chunk rerank.  
   Metric: chunk embed calls **8→1**; wall **sequentialMs=16.9 → batchMs=2.2**.  
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/279

5. **R3-05 batch accessCount** — single `inArray` update in `searchMemory`.  
   Metric: ACCESS_COUNT_UPDATES **10→1** (default topK).  
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/277

6. **R3-06 prompt head+tail trim** — `trimToBudget` keeps head+tail.  
   Metric: end-needle retention **0/20→20/20** under 30% budget.  
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/280

7. **R3-07 ranker PPR cache** — precompute outTot + invLog in `createRanker`.  
   Metric: context.createRanker p50 **0.483→0.420 ms**; **0** ranking mismatches on 192 seeds.  
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/285

8. **R3-08 hybrid BM25 df** — single-pass df instead of per-term `includes` scan.  
   Metric: BM25_DF **184.0→67.5 ms** (speedup **2.72×**); scores equal within 1e-12.  
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/287

9. **R3-09 recall adj cache** — `recall` uses `cachedAdjacency` like `predict`.  
   Metric: BRAIN_RECALL p50/p95 **0.1619/0.3085 → 0.1009/0.1587**; 0 mismatches.  
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/282

10. **R3-10 compressPrompt tokens** — strip MD link/image URL tokens + HTML comments.  
    Metric: docs/v2/OPTIMIZE-26.md tokens **2396→1894** (saved **502**, 20.95%).  
    PR: https://github.com/vitalitychems-dot/TESSERA/pull/283

## DROPPED
- None of the 10 R3 attempts were dropped (all measured wins and merged).
- Closed as duplicate/conflict (not counted as attempts): #273 (dup of #276), #275 (conflicted r2 branch, superseded by #278).

## OVERLAPS SKIPPED
- #269 grounded answering (`artifacts/v2/src/brain/grounded.mjs`, v2-079)
- #267 GSM8K eval draft (`artifacts/v2/eval/reasoning/*`, v2-077)
- #272 REA registry (draft) / W3-01 paths
- #271 BM25 file router (already merged) — avoided overlapping v2 brain router paths
- #286 Einstein R4-01 (revalidate coalesce) — out of Round 3 scope; left open

## NOTES
- GitHub Actions `validate` fails on main itself (pre-existing db-optional-boot / invention-glb env). Merges followed the same practice as #268/#270/#271: merge on measured local wins.
- No TESSERA_ENABLE_* flips, no deletes, no history rewrites, TESSERA-only.
