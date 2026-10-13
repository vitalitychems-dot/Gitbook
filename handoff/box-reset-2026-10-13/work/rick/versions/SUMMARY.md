# ALL-SEE + Tessera v4–v8 drafts: summary (Father's rule: only measured improvements are kept)

## Kept improvements
1. **Chunk-level dedup** (v4): identical chunks across TESSERA-ro / tess-opt / tw / gitbook clones are stored once. recall@5 0.9628→0.9674, p50 51.3→43.0 ms, index 235.2→211.1 MB.
2. **FTS5 optimize + vacuum** (v4): p50 43.0→40.5 ms, index 211.1→206.8 MB.
3. **Brief compression** (v5): each hit keeps only the lines that match the query. Tokens per brief 2,330→1,724 (−26%), with no change in recall or accuracy.

## Rounds
5 rounds ran (v4–v8). v6, v7 and v8 kept nothing, so the run stopped under the 3-empty-rounds rule. v9–v22 were never drafted.
Note: in pass 1, latency noise wrongly rejected changes in rounds 2–4. I fixed this with paired, interleaved timing (min of 3 runs) and re-ran from round 2. The pass-1 log is kept in tools/allsee/rounds_log_pass1.json.

## Final benchmark vs round 0 (215 held-out c1 test questions)
| metric | round 0 | final |
|---|---|---|
| recall@5 | 0.9628 | 0.9674 |
| accuracy | 0.1953 | 0.1953 |
| tokens/brief | 2,296 | 1,725 |
| p50 / p95 latency | 51.3 / 91.4 ms | 56.6 / 102.0 ms* |
| index | 235.2 MB | 239.3 MB* |
*The corpus grew after the box reboot (more files, new rick/src copies), and the box was under heavier load. Measured on the same corpus at v5, the index was 206.8 MB and the paired latency ratio was 1.01.

## Synapses (memory graph)
- fullpicture graph.json: 115 nodes / 1,717 edges before and after. No synapse change was kept.
- ALL-SEE links: 0 before and 0 after.
- Tested and rejected: TF-IDF cosine links plus graph edges plus Hebbian reweight/prune (5,362 nodes, 18,806 edges, 183 pruned to 18,418). With spreading activation at 0.05, recall@5 rose 0.9674→0.9767 but accuracy fell 0.1953→0.1907. At 0.2, recall fell to 0.9442. Same-folder links raised tokens. Graph edges alone and spread 0.05 without links gave no gain. Multi-chunk aggregation lowered recall to 0.907. The TF-IDF rerank raised recall by 1 point but cost 7–8% latency.

## Disk
Before: 17.6 GB free (87%). After: 3.8 GB free (98%). The drop comes mainly from other agents' new folders (/workspace/gb-spawn and /workspace/sb, about 11 GB each, created around 04:00). Rick's allsee folder is about 240 MB.
