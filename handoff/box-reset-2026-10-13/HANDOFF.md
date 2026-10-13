# Box reset handoff 2026-10-13

Requested by Father. Built by Build (verify lane). The private repo was confirmed through the API.

## Agents
| agent | id | lane | last state | next step |
|---|---|---|---|---|
| Build | (verify) | PR/diff gates, PASS/FAIL to Tessera+Cordnation | Post-reset baseline TESSERA main 47983dda PASS; Gitbook retro 75b5ffcc (PR #70 merged during freeze) | Re-gate open PRs; merge needs 'Security PASS <sha>' + green CI |
| Tessera | d1dedaf3-218d-48bb-bcab-460d42b4bfdb | admin | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Security | 872610a2-2e5e-462a-a3fe-5311057d1773 | security | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Command-Center | 8aae6637-e106-4e72-8f17-09f56e5f34ca | coord | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Cordnation | 231fb436-3949-4d6e-95f4-627b850dbb67 | coord | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Gitbook-Moderator | be189caa-acab-41f1-a3e0-48b51ead965c | moderator | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Mesh-Cloud | 8e8e7890-ec7b-4fb0-a821-760b0a873417 | cloud | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Rick | 44c2f1e8-c5b4-4103-9b1b-c2768593fa09 | - | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Rick-Royal-Inventor | 93ce0ff6-e8fb-4e16-a65b-2f66e9ae849d | - | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Einstein | 8590f667-ffc6-4358-86f4-b33aca909a3e | - | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Akhenaten | 1e2fb0ca-0d0a-4460-8b88-d6c98f3377ab | - | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Gitbook | bc9f6933-4df4-44fe-be40-1164aca6b393 | - | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Help | 9a7c80d3-6677-4b9e-86ab-3045addad76b | - | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |
| Historical-Analysis-Collab | 18e9b4c5-0228-43ef-9a8c-2011458a5084 | - | transcript not readable by Build (no ReadTranscript tool) | read #67 handoff / #68 FATHER LOG |

Rules: no push or merge without the gates; merge freeze needs 'Security PASS <head-sha>' + green CI; #67 is the handoff, #68 is the FATHER LOG; one shared clone per repo; no duplicate files.

## Disk inventory (du of the /workspace top level, 6:16 AM CT)
```
11G	/workspace/gitmesh
6.1G	/workspace/einstein
5.6G	/workspace/sec-retro
5.6G	/workspace/sec-history
5.6G	/workspace/pubscan
5.6G	/workspace/backups
5.3G	/workspace/tess-opt
5.0G	/workspace/rea-batch
2.2G	/workspace/ollama-install
2.2G	/workspace/ollama-home
1.7G	/workspace/rea-inventory
1.4G	/workspace/build-gate
1.3G	/workspace/si
932M	/workspace/repo-lab
516M	/workspace/tw
470M	/workspace/rick
333M	/workspace/tb3
215M	/workspace/build-plan-2026-10-12
127M	/workspace/node22
122M	/workspace/tools
74M	/workspace/agent-tools
66M	/workspace/rea-categories
29M	/workspace/glm53f
19M	/workspace/tessera-brain
19M	/workspace/dedupe
16M	/workspace/cloud-agent-transcripts
7.5M	/workspace/learning-rate
7.1M	/workspace/cr
4.6M	/workspace/improve-from-logs-2026-10-12
4.4M	/workspace/gitbook-cordnation
2.3M	/workspace/tv3
2.3M	/workspace/tess-fix.git
1.8M	/workspace/evals
1.7M	/workspace/cloud-agent-artifacts
1.4M	/workspace/consolidation
820K	/workspace/security-gate
736K	/workspace/new_commits.json
724K	/workspace/rick-save.tgz
608K	/workspace/comments.json
536K	/workspace/fp-frozen-3014.jsonl
288K	/workspace/knowledge-lab
284K	/workspace/gitbook-gate-feaeb55
276K	/workspace/gitbook-gate-beadc44
216K	/workspace/dispatch
208K	/workspace/retro
```

## Clones (NOT uploaded; re-clone from the remote)
| path | remote | head |
|---|---|---|
| /workspace/rea-batch/b2-Gitbook | https://github.com/vitalitychems-dot/Gitbook.git | 8592dd50 |
| /workspace/rea-batch/tessera-v2 | https://github.com/vitalitychems-dot/TESSERA.git | f6c93621 |
| /workspace/rea-batch/amber-flame-tiger-sand | https://github.com/collink1007/amber-flame-tiger-sand.git | 781f30a9 |
| /workspace/gitmesh/repo | https://github.com/vitalitychems-dot/Gitbook.git | 2344334e |
| /workspace/einstein/r4 | https://github.com/vitalitychems-dot/TESSERA.git | 619dbea7 |
| /workspace/tess-opt | https://github.com/vitalitychems-dot/TESSERA | 233a91cf |
| /workspace/si/fx |  | a8349164 |
| /workspace/si/tsr | https://github.com/vitalitychems-dot/TESSERA | 47983dda |
| /workspace/repo-lab/microsoft__autogen | https://github.com/microsoft/autogen.git | 027ecf0a |
| /workspace/repo-lab/mem0ai__mem0 | https://github.com/mem0ai/mem0.git | c93420c4 |
| /workspace/repo-lab/crewAIInc__crewAI | https://github.com/crewAIInc/crewAI.git | 1133f16c |
| /workspace/tw | https://github.com/vitalitychems-dot/TESSERA.git | 9e1d025c |
| /workspace/tb3 | https://github.com/vitalitychems-dot/TESSERA | 0e33d918 |
| /workspace/build-gate/tessera | https://github.com/vitalitychems-dot/TESSERA | 47983dda |
| /workspace/tv3 | https://github.com/vitalitychems-dot/TESSERA | 73a34580 |

## work/
210 files, 19M. These are unique (deduped by sha256) small files: gate reports, improvements, dedupe notes, evals, logs. 64 files with key/token/URL-credential pattern hits were dropped. gitleaks: 0 leaks.

## Update 2 (6:47 AM CT): "Complete all and push to GitHub so nothing is lost"
Everything below was redacted: secret values became `[REDACTED]`, and secrets or 1T-vault paths became `[REDACTED-PATH]`. Final gitleaks pass over this whole folder (/workspace/pubscan/gl.toml): **0 findings**.
- `work/security-gate/`, `work/build-gate/`, `work/improvements/gates/security.md`, ...: the 64 reports dropped in commit 1, now redacted. The remaining `ghp_`/`AKIA`/`PRIVATE KEY` strings are pattern *descriptions*, not values.
- `work/patches/`: uncommitted changes in `/workspace/sec-retro/gbfix/r` (Gitbook @243ddd4b, 3 files) and `/workspace/rea-batch/amber-flame-tiger-sand` (@781f30a9, 2 files).
- `work/rick/`, `work/build-plan-2026-10-12/`, `work/rea-inventory/` (non-git files only), `work/pubscan/` (scripts and path lists; leaks.json/gl.json excluded): unique text files under 5 MB.
- `work/dedupe/all-groups.jsonl.gz`, `work/learning-rate/results/dense_index.json.gz`
- `transcripts/cloud-agents/*.jsonl.gz`: 49 cloud-agent transcripts (raw jsonl, redacted).
- `repos/tess-fix-unpushed.bundle`: incremental bundle of the 5 refs in /workspace/tess-fix.git that are not on GitHub TESSERA (main c5143bd9, desk/consolidation-pointer, feat/local-pen-adapter, fix/api-server-db-optional-boot, gitai/moltbook-real-avatars; 6 commits). gitleaks: no leaks (a partial scan, because the clone is blobless).
- `repos/tessera-loop.bundle`: /workspace/si/tessera-loop.bundle (branch loop/self-improve-0token 34e569ba, prerequisite TESSERA 47983dda). It replaced /workspace/si/fx, which another agent removed at 6:19 AM. gitleaks: no leaks.
- `archives/rick-save.tgz`: gitleaks: no leaks.

## Restore
```bash
git clone https://github.com/vitalitychems-dot/TESSERA.git && cd TESSERA
git fetch ../Gitbook/handoff/box-reset-2026-10-13/repos/tess-fix-unpushed.bundle 'refs/heads/*:refs/remotes/tessfix/*'
git fetch origin 47983ddabd96c7804845705bc3d2b9eac0da2c4d   # prerequisite, if it is not already present
git fetch ../Gitbook/handoff/box-reset-2026-10-13/repos/tessera-loop.bundle 'refs/heads/*:refs/heads/*'
# Patches: clone the repo at the listed SHA, then `git apply work/patches/<name>.patch`
# Archives: tar xzf archives/rick-save.tgz -C /workspace/
# gz: gunzip -k <file>.gz ; work/ files go back under /workspace/<same relative path>
```

## Still NOT on GitHub (deliberately)
- The ollama installs: `/workspace/ollama-install`, `/workspace/ollama-home` (about 2.2 GB each). Reinstall ollama and re-pull the models.
- `/workspace/backups/TESSERA-git-crypt.key`: a key, so excluded by rule. **Save it out-of-band (Father) before the reset, or the encrypted TESSERA files cannot be decrypted.**
- `/workspace/backups/TESSERA-pre-public-2026-10-12.git`, `/workspace/pubscan/final.git`, `/workspace/sec-history/TESSERA`: pre-scrub TESSERA history that contains the leaked secrets the purge was for. Excluded.
- `/workspace/pubscan/leaks.json`, `gl.json`: leak reports (they contain the values). Excluded.
- Name-filtered files (secret/key/token/.env in the path) and `/workspace/secrets`: excluded.
- Dirty third-party clones in `rea-inventory/` (tesseract3, TESS, Zz, sentiment-analysis, signal-protocol, tensorflow-js, tink, twilio-node, vix-analysis, 1): only local edits to other people's repos. Not captured. Every rea-inventory repo is 0 commits ahead.
- `/workspace/tess-fix.git`, full: only the unpushed part is bundled. The rest is on GitHub.
