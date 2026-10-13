# Security gate: Gitbook PR #39, PR #50, archive/+history/ @ 2344334e — 2026-10-12 ~6:50 PM CT
Read-only. No values recorded (path:line + type only). 1T/vault contents not opened (metadata only).

## (A) PR #39 GB-061 rev2 — FAIL (verification incomplete), pinned to head 71a8c78f11ebd290438ba7066c887114ada8f643
- Head verified: 71a8c78f…f643; base 8bbf7c20…6de766 = merge-base. Open, not merged, mergeable clean.
- Files: 70 added, 0 modified/deleted, +6589, all under archive/preserved/ (README.md + 28 olive-giant-ever-glade + 41 origin-tessera). Matches README counts.
- Checksums: the PR body lists 4 pack checksums (COPIED.tsv 5e211a65…, SKIPPED.tsv 1803b2d3…, apply-add.sh c4831c24…, SHA256SUMS.txt 98b9dd04…). NONE of these 4 files is in the head tree, and none exists anywhere on the box (searched whole fs). README.md also cites SKIPPED.tsv, which is not committed. => checksums UNVERIFIABLE; per-file blob checks against SHA256SUMS impossible. Origin Tessera source commit af2001fa not present in any local clone, so byte-exact claim also unverified.
- Recomputed sha256 of all 70 head blobs: /workspace/security-gate/PR39-71a8c78f-SHA256-recomputed.txt (for comparison once SHA256SUMS.txt is supplied).
- Content scan of diff: no secrets. 4 hits origin-tessera/archives/drive-export/Vitalitychems/.agents/agent_assets_metadata.toml:15,29,43,57 storage_version_token = [REDACTED] numeric version stamps (not credentials). "birth mark"/"VAULT" hits in olive-giant-ever-glade (prompt.ts, store.ts, opening.ts, council-room.tsx, self-view.tsx) are app lore/UI identifiers, no dates/places/natal data. README mentions natal-vault by name only. No 1T content, no emails/phones.
- To flip to PASS: commit (or place on box) COPIED.tsv, SKIPPED.tsv, apply-add.sh, SHA256SUMS.txt at a new head; I recompute and compare; re-gate at that new head.

## (B) PR #50 O11 mesh/secure-mesh.md, merged 2344334e — content PASS / provenance FAIL
- Head 8592dd50 (author vitalitychems-dot noreply, unsigned, 5:18:10 PM CT). PR opened 5:18:15 PM CT, merged 5:18:17 PM CT by vitalitychems-dot via GitHub web; merge commit author string "Tessera". 0 reviews, 0 reviewers; no Mod/Security/Build gate recorded (GB-066 log confirms). Body claims "Link check clean" only.
- Content: 22-line doc, no secrets, keys, PII, IPs, 1T. Describes design only (AES-GCM/Ed25519, group key shared out-of-band).
- Same pattern as TESSERA PR #146: open→merge in ~2 s, "Tessera" merge author.

## (C) archive/ + history/ @ 2344334e — FAIL as-is; PASS-with-excludes if EXCLUDE list applied
- HEAD /workspace/gitmesh/repo = 2344334e689ad8fdfc9b5c7848aa8f1fdeac6afb (matches). 10,236 tracked files; 1,629 symlinks (skipped; some loop).
- Raw scan output (path:line:type only): /workspace/security-gate/archive-history-scan-2344334e.txt
### Findings
- HIGH NEW: [REDACTED-PATH] material is tracked in Gitbook main: archive/moved/1T/ (11 files incl. .local-data/natal-vault.json 1133 B, .agents/memory/*, attached_assets/*.png/pdf). Added by e6ae7e9 (Oct 7 10:53 PM CT, author "Tessera"). Not opened.
- HIGH: archive/moved/T44/artifacts/api-server/.local-data/natal-vault.json (1133 B, tracked; same size as 1T copy). Not opened.
- HIGH NEW: real-format glhf.chat API key (OPENAI_API_KEY var, glhf_ prefix, 37 chars): archive/moved/Zz/artifacts/z-app/data/ingest/e7ee9a19bfd44fc4.txt:59 and duplicate history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/e7ee9a19bfd44fc4.txt:59. Rotate.
- HIGH (known): archive/moved/collink1007-XXX/.replit:33 TESSERACT_ADMIN_KEY (18 chars, real-looking).
- MED (known): archive/moved/collink1007-XXX/tess/.replit:45-79 (uniform-length, likely placeholders; confirm).
- MED wallet-signing/trading code: archive/moved/collink1007-XXX/tess/server/{sol-wallet,arbitrage-engine,autonomous-trading-bots,defi-realification,pumpfun-trading-bot,routes}.ts; archive/moved/collink1007-XXX/x/tess/server/{defi-realification,routes}.ts. Reads keys from env; no inline keys found.
- LOW PII: 86 consumer-domain email hits (Zz 50, history/source-documents 25, collink1007-XXX 10, olive 1). Natal/birth-field refs concentrated in Zz ingest + history/recovered/source-documents/Zz.
- False positives cleared: 45 "sk-" hits = "taskId":"task-…" (task-progress.json); BEGIN PRIVATE KEY in CredentialsPage.tsx:71 = form placeholder; JWT in sovereign-security-tester.ts:69 = attack-test payload; db URLs = fake/honeypot/test creds; base58 "WIF" hits = pnpm-lock integrity hashes; storage_version_token = numeric stamps; most generic token= hits are variable names/LLM token counts.
### t9_admin_token broken link
- Not a file link. Inventory lines 53/66/74 come from the markdown parser reading `[REDACTED]("t9_admin_token")` as a link: archive/moved/5t/.agents/outputs/tx-snapshot-diffs-frontend.md:804, history/recovered/source-documents/5t/.agents/outputs/tx-snapshot-diffs-frontend.md:804, history/recovered/source-documents/5t/.agents/outputs/tx-snapshot-diffs.md:3615. Target "t9_admin_token" is a browser localStorage key name; no file of that name exists in the repo or anywhere on the box. No token value present. Mark as false-positive link; no action.

## EXCLUDE list (must not enter memory graph)
```
archive/moved/1T/**
**/natal-vault.json
**/.local-data/**
**/.replit
**/.env*
archive/moved/Zz/artifacts/z-app/data/ingest/**
history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/**
archive/moved/Zz/artifacts/z-app/imports/objects/**
archive/moved/collink1007-XXX/tess/server/{sol-wallet,arbitrage-engine,autonomous-trading-bots,defi-realification,pumpfun-trading-bot}.ts
archive/moved/collink1007-XXX/x/tess/server/defi-realification.ts
archive/moved/collink1007-XXX/tess/client/src/pages/CredentialsPage.tsx
archive/moved/*/.vercel/**
archive/moved/collink1007-amber-flame-tiger-sand/artifacts/.tmp/**
**/attached_assets/**
**/pnpm-lock.yaml
symlinks (mode 120000) — do not follow
```
Plus: redact/skip email addresses and birth/natal fields at ingest time.
