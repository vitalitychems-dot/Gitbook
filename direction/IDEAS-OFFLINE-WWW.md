# Offline mesh + "our own www" ideas (Einstein, 2026-10-13)

**Status: PROPOSAL ONLY. All numbers are UNMEASURED estimates.** Nothing here is deployed; there are no Pages and no workflows.
Test standard for any adoption: real data, N>=7, bootstrap 95% CI, before/after, Moderator gate.

| # | Idea | Est. before -> after | How to test |
|---|---|---|---|
| 1 | **SHA-keyed shared scan cache**: key = (tool, version, tree SHA) -> JSON result; every bot checks the cache before scanning | tokens/scan ~100% -> ~10-20% on repeat SHAs; scan time ~minutes -> <1 s on a hit | Replay the last 50 PR scans; measure hit rate, wall time and tokens with vs without the cache |
| 2 | **Deterministic no-LLM cron jobs** (tests, benches, ledger refresh, lint) in place of agent turns | tokens/day for routine checks X -> ~0; works with billing off | Pick 5 routine agent tasks; port them to scripts; compare output equality + token use over 7 days |
| 3 | **Git bundles for sneakernet/LoRa sync** (`git bundle create --since`) | full clone ~repo size -> incremental bundle ~KB-MB; works with no internet | Bundle 1 day of commits; measure size; verify `git fetch bundle` on a fresh node; LoRa pages/day = 86400*rate/(8*bytes) |
| 4 | **Content-addressed dedup store** (sha256 blobs, shared across bots under /workspace/cas) | duplicate file storage -> 1 copy; disk -20-40% (est.) | Hash all files in the bot workspaces; count dupes; dry-run the savings report (no deletes) |
| 5 | **Delta-only sync** (send only changed blobs/ranges, rsync-style rolling hash) | bytes/sync full -> changed fraction (~5-15%) | Sync 7 daily snapshots; compare bytes full vs delta |
| 6 | **zstd + trained dictionary** for JSON/JSONL logs and pages | ratio gzip ~3x -> zstd-dict ~5-8x on small records | `zstd --train` on 1k samples; compare ratio + speed vs gzip on held-out set |
| 7 | **Kiwix/ZIM offline web** (Wikipedia, docs, our own site) served via kiwix-serve | web lookups need internet -> 0 internet; latency ~100s ms -> ~10 ms local | Answer 50 held-out factual queries online vs ZIM; measure hit rate + latency |
| 8 | **Our own www**: static site generated from Gitbook/TESSERA (markdown -> HTML), hostable later via GitHub Pages; offline mirror = git bundle + ZIM build (zimwriterfs) so any node serves it | site availability: internet-only -> any node offline; build = deterministic, 0 tokens | Build locally only; check link integrity, ZIM size and that a bundle restores an identical site hash on a 2nd node |
| 9 | **Peer mesh via git remotes** over LAN / Yggdrasil / Reticulum (nodes `git fetch` each other; GitHub just one remote) | single point (GitHub) -> N peers; sync works with GitHub down | 2-3 box/LAN nodes; drop internet; measure propagation time of 1 commit, verify SHA equality |
| 10 | **Shared ETag/PR-state cache** for GitHub API (304s) | API calls ~288 -> ~32/day per bot (cf. #88 −89%) | Replay 1 day of polls with/without the cache; count calls + rate-limit headers |

## Ranking rationale
1-2 are first: they save the most tokens right away while usage is at 90%. 3, 8 and 9 build the offline "own www". 4-7 and 10 are cheaper storage, bandwidth and lookups.

## Hard limits
Nothing is deployed and no Pages are enabled. Nothing is deleted, including in the dedup dry runs. No private data goes in public repos. Any workflow must be proposed as `.yml.txt` and reviewed by Father.
