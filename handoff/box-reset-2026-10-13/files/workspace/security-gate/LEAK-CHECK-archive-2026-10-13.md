# Leak check: TESSERA public main archive paths, 2026-10-13 (read-only)

Main = 33ed9383cb9d63c96ba3fb7d49ff393a174ab84d. /workspace/ops/tree-TESSERA.json was stale (47983dda), so I refetched the tree (5004 entries, not truncated): /workspace/security-gate/tree-main-33ed938.json.
I fetched the files from public raw at that SHA into /workspace/security-gate/leakscan/f. I ran gitleaks twice, once with the default rules and once with pubscan/gl.toml, then a regex scan for PII, natal data, chat logs and Drive links. No secret values are recorded here.

## Present on main? YES, 1365 blobs, ~140 MB
| prefix | files |
|---|---|
| archive/from-gitbook/archive/moved/collink1007-* (XXX 906, amber-flame-tiger-sand 37, z 29) | 972 |
| archives/source-repositories/** (Zz 227, olive-giant-ever-glade, Grok-ready, 5t) | 276 |
| archives/migration-review/** (legacy-ui, archive-helpers) | 117 |
File types: ts 719, tsx 352, json 136, mjs 27, html 18, txt 13, yaml 12, mp3 12, py 12, sql 11, sh 8, md 7, toml 6, other 30, plus 1 zip (93.6 MB) and 1 png.
No 1T or natal-vault paths fall under these prefixes.

## Findings (severity)
- **MEDIUM**: archive/from-gitbook/archive/moved/collink1007-amber-flame-tiger-sand/artifacts/drive/1e3Vip.zip is a 93.6 MB **Drive export**. NOT OPENED: Auto-review blocked the download, so its contents are unknown. Treat it as possibly private.
- **MEDIUM**: archive/.../collink1007-amber-flame-tiger-sand/attachments/Pasted Text.txt:982, :5923-5929, :6316-6322 hold 15 **Google Drive file share links** (usp=drivesdk). They may expose Father's Drive files to anyone who has the link. The file is a pasted agent prompt/spec (6343 lines), not a chat transcript.
- **LOW**: archive/.../collink1007-XXX/tess/data/summit-51-state.json:2583-2742 holds 10 **proton.me addresses** in a synthetic agent-identity pattern. Probably generated, but check whether they are real mailboxes.
- **LOW**: archive/.../collink1007-amber-flame-tiger-sand/artifacts/.tmp/mcp-results/*.json are raw GitHub MCP outputs (repo trees and search). They reveal repo and file names from Father's other repos.
- **LOW**: 12 tessera-voice-*.mp3 files (collink1007-*). These look like TTS output; not reviewed by ear.
- **INFO (false positives)**:
  - private_key at archive/.../collink1007-XXX/tess/client/src/pages/CredentialsPage.tsx:71 is a form *placeholder*.
  - generic_secret, 8 hits: test fixtures and placeholders. They include archive/.../Pasted Text.txt:3097 (a placeholder), archives/migration-review/archive-helpers/simulation.test.mjs:13, archives/source-repositories/Zz/artifacts/api-server/src/__tests__/*.test.ts, and archives/source-repositories/5t/.agents/outputs/tx-t44-unique/.agents__agent_assets_metadata.toml:15 (looks like an asset token; low).
  - Emails are vendor or fake (tessera.sov, openai.com, mylife.com and epsilon.com opt-out addresses, domain.com, email.com).
  - "birth chart" (cheat-codes-conference.ts:206, :298) is generic text, not data.
  - The "chat_log" hits are LLM message-role code, not transcripts.
  - No phone numbers, street addresses, SSNs or birth dates found. The single phone hit at legacy-ui/KnowledgeSecretsPage.tsx:751 is a numeric false positive.
  - Real names: none found beyond Father's handle collink1007, which appears in path names and manifests. interdimensional-entities.ts names are fictional.
- gitleaks (default and gl.toml): **0 findings**.

## pubscan cross-check
pubscan/paths.txt and paths2.txt flagged 23 paths in this area. 21 are gone from main. Two remain and are now benign: collink1007-XXX/tess/server/saved-credentials.enc.json (2 bytes, empty) and dimensional-secrets.json (lore text, no keys). The keys pubscan listed (TESSERACT_ADMIN_KEY, preview secret, glhf.chat key, .replit keys) are not on main, but they still need rotating. The 1e3Vip.zip and the Drive links were not in pubscan's verdicts.

## Counts
Secrets 0 real (9 false positives). Emails 115 hits in 14 files, 0 personal. Phone/address/natal 0. Drive links 15, plus 1 Drive zip. Chat logs 0. Real names 0 beyond the handle.

## Smallest fix (needs Father's yes)
1. One PR on TESSERA that `git rm`s `archive/from-gitbook/archive/moved/collink1007-amber-flame-tiger-sand/` (the zip, Pasted Text.txt and .tmp/mcp-results). Better: remove all three prefixes, since they are dead archive code already kept in private Gitbook.
2. Add 1e3Vip.zip and both Pasted Text.txt to the pubscan purge list (history rewrite plus GitHub support purge), because they are already public in history.
3. Father checks the sharing on the 15 Drive links and sets them to restricted. That fixes the exposure even before history is purged.
