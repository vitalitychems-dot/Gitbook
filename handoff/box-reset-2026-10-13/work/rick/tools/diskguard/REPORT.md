# Disk guardian report
Generated 2026-10-13 02:14 (box time, CT). Read-only: nothing was deleted.

**Disk:** 109.5G used of 125.9G (87.0%), 9.9G free.

> ⚠️ **WARNING: disk at or above 85%.**

**Growth:** 28.1G/hour shrinking; **hours until full:** n/a (not growing or no data).

## Top folders

| Size | Path | Last write | Owner (guess) | Lane (guess) | Finished? |
|---|---|---|---|---|---|
| 23.4G | `/workspace/rea-batch` | 2026-10-13 01:59 | REA scan | rea-batch | — |
| 12.1G | `/workspace/rick-audit` | 2026-10-13 02:12 | Rick | rick-audit | — |
| 11.2G | `/workspace/gitmesh` | 2026-10-12 19:42 | GitMesh | gitmesh | no writes for 6.5h |
| 10.3G | `/tmp/gb066` | 2026-10-13 02:03 | GB work | Gitbook | — |
| 7.5G | `/workspace/build-gate` | 2026-10-13 02:12 | Build | build-gate | — |
| 6.9G | `/tmp/gb` | 2026-10-13 02:03 | unknown | Gitbook | — |
| 6.3G | `/workspace/TESSERA-ro` | 2026-10-13 02:06 | Tessera | TESSERA | git clone clean and fully pushed |
| 5.5G | `/workspace/pubscan` | 2026-10-13 02:06 | public-repo scan | pubscan | — |
| 5.5G | `/workspace/backups` | 2026-10-12 20:18 | backups | backups | — |
| 5.5G | `/workspace/sec-history` | 2026-10-13 02:08 | Security | sec-history | — |
| 2.1G | `/workspace/ollama-home` | 2026-10-13 02:00 | local model | ollama-home | — |
| 2.1G | `/workspace/ollama-install` | 2026-10-12 12:05 | local model | ollama-install | PROTECTED (toolchain/backup), no writes for 14.1h |
| 1.7G | `/workspace/rea-inventory` | 2026-10-12 20:34 | REA scan | rea-inventory | — |
| 1.2G | `/workspace/tw` | 2026-10-13 02:08 | unknown | TESSERA | — |
| 1.2G | `/workspace/tess-opt` | 2026-10-13 02:03 | Tessera | TESSERA | — |
| 1.2G | `/workspace/repo-lab` | 2026-10-12 15:57 | unknown | repo-lab | no writes for 10.3h |
| 418.0M | `/tmp/rea` | 2026-10-12 18:44 | REA scan | rea | no writes for 7.5h |
| 215.0M | `/workspace/build-plan-2026-10-12` | 2026-10-13 02:04 | Build | build-plan-2026-10-12 | — |
| 198.4M | `/workspace/node22` | 2026-10-13 02:01 | unknown | node22 | — |
| 197.6M | `/workspace/rea-opt` | 2026-10-12 18:53 | REA scan | rea-opt | no writes for 7.3h |

## Suggested cleanup (owners only, after confirming)

Diskguard never deletes. Owners: check the folder is yours and finished, then run:

- 11.2G — `rm -rf -- '/workspace/gitmesh'`  (no writes for 6.5h)
- 6.3G — `rm -rf -- '/workspace/TESSERA-ro'`  (git clone clean and fully pushed)
- 1.2G — `rm -rf -- '/workspace/repo-lab'`  (no writes for 10.3h)
- 418.0M — `rm -rf -- '/tmp/rea'`  (no writes for 7.5h)
- 197.6M — `rm -rf -- '/workspace/rea-opt'`  (no writes for 7.3h)
