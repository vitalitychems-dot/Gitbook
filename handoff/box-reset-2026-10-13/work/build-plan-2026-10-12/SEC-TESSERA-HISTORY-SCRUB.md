# SEC — TESSERA full-history secrets scan + scrub list (2026-10-12 ~6:50 PM CT)
Read-only. Mirror clone: /workspace/sec-history/TESSERA (1802 commits, 495 refs, all branches). Tools: gitleaks 8.21.2 (--log-opts=--all, redacted) + custom regex pass over `git log -p --all`. No values recorded. 1T contents not opened.
Cross-check: /workspace/build-plan-2026-10-12/TESSERA-PUBLIC-SCAN.md DID NOT EXIST at scan time -> cross-check pending.

## Findings (type | path | first | last | at HEAD | class)
- generic-api-key | archive/from-gitbook/archive/moved/collink1007-XXX/.replit (TESSERACT_ADMIN_KEY, len 18, not placeholder-shaped) | c535df98 | c535df98 | HEAD | REAL? -> ROTATE
- 20 key/wallet vars (OPENROUTER, XAI, GROK, GEMINI, GITHUB_TOKEN, GITHUB_MODELS_TOKEN, SOL/ETH/BTC_PRIVATE_KEY, SOL_PRIVATE_KEY_ECONOMY, SHOPIFY_*, HUBSPOT, KLAVIYO, COHERE, DEEPSEEK, ELEVENLABS, HUGGINGFACE, APIFY, PUTER) | archive/from-gitbook/archive/moved/collink1007-XXX/tess/.replit | c535df98 | b84e4abc | HEAD | all len 21 -> likely PLACEHOLDER; scrub anyway
- generic-api-key x30 | .../collink1007-XXX/tess/data/secret-society.json | c535df98 | HEAD | review
- generic-api-key | .../collink1007-XXX/{tess,x/tess}/server/{agi-implementations,realification-conference,summit-37-parallel-universes}.ts | c535df98 | HEAD | likely code literals
- generic-api-key | .../Zz/artifacts/z-app/data/ingest/{1e44d8b943c4248f,e7ee9a19bfd44fc4}.txt | c535df98 | 763ed988 | gone
- generic-api-key | preview/src/lib/auth/preview.ts (34556936), archives/source-repositories/Zz/.../auth/preview.ts (9538b364), archive/from-gitbook/.../Zz/.../auth/preview.ts (gone) | preview secret -> ROTATE preview secret
- jwt | archive/drive-rest/share-2c60.html, share-3ad6.html | f5cc6af5 | gone | Google Drive share tokens (likely expired)
- jwt | .../collink1007-XXX/tess/server/sovereign-security-tester.ts | c535df98 | 763ed988 | HEAD
- privkey-block | .../collink1007-XXX/tess/client/src/pages/CredentialsPage.tsx (c535df98..763ed988), artifacts/tessera/src/pages/CredentialsPage.tsx (67784aed) | HEAD | likely UI placeholder; verify
- FIXTURE: github-pat learning-memory.test.ts (06c64e65); privkey pen-local.test.ts (3630e96c, gone); generic colonial-secret-fail-closed.test.ts, compression-pipeline.test.ts (0a69be53); db-url tessera_test@127.0.0.1 in ci.yml (216e4e89) and route-inventory/routes-index-import/sovereign-engines-session-gate/system-runtime-admin-gate tests
- No hits: AWS AKIA, xoxb/xoxp, sk-or-v1, xai-, AIza, gh*_ real tokens (outside fixture), mnemonics.

## Sensitive files ever committed (path only)
- artifacts/api-server/.local-data/natal-vault.json | 4ba3fe04..3f16ae15 | gone (still in history)
- archive/from-gitbook/archive/moved/T44/artifacts/api-server/.local-data/natal-vault.json | c535df98 | HEAD
- archive/from-gitbook/archive/moved/1T/ (incl. .local-data/natal-vault.json, .agents/memory/*) | c535df98..571cef4b | gone (in history) — not opened
- .replit files: .replit (HEAD), .../Zz/.replit (gone), .../Zz/.../imports/trees/{shared-lfs-zip/3,tessera-unified-main}/.replit, .../collink1007-XXX/{,tess/,x/}.replit
- No *.pem, no real .env (only .env.example).

## Scrub: paths for `git filter-repo --invert-paths`
archive/from-gitbook/archive/moved/1T/
archive/from-gitbook/archive/moved/T44/artifacts/api-server/.local-data/
artifacts/api-server/.local-data/natal-vault.json
archive/from-gitbook/archive/moved/collink1007-XXX/.replit
archive/from-gitbook/archive/moved/collink1007-XXX/tess/.replit
archive/from-gitbook/archive/moved/collink1007-XXX/x/.replit
archive/from-gitbook/archive/moved/Zz/.replit
archive/from-gitbook/archive/moved/Zz/artifacts/z-app/imports/trees/shared-lfs-zip/3/.replit
archive/from-gitbook/archive/moved/Zz/artifacts/z-app/imports/trees/tessera-unified-main/.replit
archive/from-gitbook/archive/moved/Zz/artifacts/z-app/data/ingest/
archive/from-gitbook/archive/moved/collink1007-XXX/tess/data/secret-society.json
archive/drive-rest/share-2c60.html
archive/drive-rest/share-3ad6.html
(optional: path-glob `**/.local-data/**`, `**/natal-vault*`)

## Scrub: --replace-text patterns (regex:, -> ***REMOVED***)
regex:(?m)^(\s*[A-Z0-9_]*(KEY|SECRET|TOKEN|PRIVATE|PASSWORD|MNEMONIC|SEED)[A-Z0-9_]*\s*=\s*)"[^"$]{8,}"==>\1"***REMOVED***"
regex:gh[pousr]_[A-Za-z0-9]{36}
regex:github_pat_[A-Za-z0-9_]{50,}
regex:sk-or-v1-[0-9a-f]{40,}
regex:xai-[A-Za-z0-9]{40,}
regex:AIza[0-9A-Za-z_-]{35}
regex:AKIA[0-9A-Z]{16}
regex:xox[bpas]-[0-9A-Za-z-]{10,}
regex:eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}
regex:(?s)-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----
regex:((postgres(ql)?|mysql|mongodb(\+srv)?)://[^:@/\s]+:)[^@\s]+@==>\1***@
(Last two will also hit fixtures; acceptable.) Plus the preview secret literal in */auth/preview.ts: supply its literal in a local expressions file only, never committed.

## Keys to rotate
- TESSERACT_ADMIN_KEY (collink1007-XXX/.replit) — looks real.
- Preview secret (preview/src/lib/auth/preview.ts) — in history, rotate.
- Confirm placeholders for the 20 len-21 vars in collink1007-XXX/tess/.replit; if any real, rotate (esp. SOL/ETH/BTC keys).
- Out of scope but urgent (prior sweep): TheTesseractAI_18 .replit keys + wallets.

## Post-rewrite PASS criteria (gates 2/3)
Re-run gitleaks --log-opts=--all + the regex pass on rewritten mirror: zero non-FIXTURE hits; none of the paths above present in any ref; all PR refs (refs/pull/*) — note GitHub keeps PR refs/caches server-side; contact GitHub support or accept residual risk before public.

## a502322 attribution
- SHA a5023224412c535e969d2aecc0c2f4d02be7b972, 2026-10-12 9:34 AM CT, "Refresh the name lists to the current trees." (body: TESSERA 4158 names at af3e52e, Gitbook 10405 at fa02977; "preview secret was not" copied).
- Author = committer = "Tessera <vitalitychems@gmail.com>", unsigned (N). On main; also contained by cursor/v2-0xx-*-3a81 branches. No associated PR (API returned none) -> direct push to main.
- Pattern: matches 203 commits of "Tessera|Tessera" local-git pushes (vs 227 "Tessera|GitHub" web merges, and Cursor Agent using cursoragent@cursor.com). Its parents af3e52eb/4a5e67f8 are same pattern (Oct 11). The "name lists"/tree-inventory wording + 3a81 branch suffix family points to the Cursor box lane(s) using a local git config user.name=Tessera (same mechanism as HYB-016's 56a7a48d), not Tessera admin. Attribution: a box/Cursor lane with git identity set to Tessera; exact lane unconfirmed — check which agent's git config on the box sets user.name=Tessera.
