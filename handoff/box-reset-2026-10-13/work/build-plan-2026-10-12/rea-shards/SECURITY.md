# SECURITY sweep — rea-shards (Security lane, read-only)

- Written: Mon Oct 12 2026, 4:58 PM CT
- **SCOPE (Father via Tessera, 4:56 PM CT):** vitalitychems-dot/TESSERA and vitalitychems-dot/Gitbook only, including Gitbook `archive/moved/*` (excluding `archive/moved/Zz`). All other repos dropped.
- Repos scanned: 2 / 2 in scope (local clones `/workspace/rea-batch/b2-TESSERA` @ a502322, `/workspace/rea-batch/b2-Gitbook` @ 56a7a48). Inventory lists 315 repos; only 2 in scope.
- Tools: ripgrep (`-uu`, PCRE regex), git log/ls-files, find/stat. gitleaks/trufflehog not installed. No network calls, no repo changes.
- Skipped by rule: any `1T` path (e.g. `Gitbook/archive/moved/1T/` exists, not scanned), `*vault*` paths, node_modules, .git.
- Rule: no secret values are recorded. Only file:line and type.

## Coverage limits
- Both clones are **shallow** (1 commit), so the git-history and first-commit results only go back as far as the clone's HEAD.
- `b2-Gitbook` has 1,629 symlinks, and **1,369 are dangling** (they point to `objects/<sha256>` blobs that aren't in the clone). ripgrep does not follow symlinks, so that content is **NOT COVERED**. TESSERA has 0 symlinks.

## Findings (ranked)
| # | Repo | file:line | Type | Severity | Smallest fix |
|---|---|---|---|---|---|
| 1 | Gitbook | archive/moved/T44/artifacts/api-server/.local-data/natal-vault.json | personal-data file tracked in git | HIGH | `git rm --cached`, add `**/.local-data/` to .gitignore, purge from history (filter-repo) |
| 2 | Gitbook | archive/moved/collink1007-XXX/.replit:33 | hardcoded `TESSERACT_ADMIN_KEY` (18 chars, not a placeholder) | HIGH | rotate it, move it to Replit Secrets, delete the line |
| 3 | Gitbook | archive/moved/collink1007-XXX/tess/.replit:45-79 | 20 key/token/wallet-privkey slots (OPENROUTER, GITHUB_TOKEN, XAI, SOL/ETH/BTC_PRIVATE_KEY…). Every value is the same 21-char length, so they look like placeholders | MED | confirm they are placeholders, then replace them with `${}` refs |
| 4 | Gitbook | archive/moved/collink1007-XXX/{,x/}tess/server/lattice-search-engine.ts:879/1091 | DB URL with password, "fake/localhost" | INFO | none |
| 5 | Gitbook | history/recovered/source-documents/Zz/.../c4324b331207d556.txt:10-12,36 | test DB URLs (localhost) | INFO | none |
| 6 | TESSERA | artifacts/api-server/src/__tests__/learning-memory.test.ts:60 | ghp_-shaped token in a test fixture | INFO (verify it's synthetic) | swap it for an obviously fake token |
| 7 | TESSERA | preview/src/lib/tessera/github-desk.test.ts:7 | sk- string in a redaction test | INFO | none |
| 8 | TESSERA | .github/workflows/ci.yml:50,54 | CI test postgres URL | INFO | none |
| 9 | TESSERA | artifacts/api-server/src/__tests__/{route-inventory:180,routes-index-import:54,sovereign-engines-session-gate:28}.test.ts; scripts/suite-policy.test.mjs:10-12,36 | test DATABASE_URL | INFO | none |
| 10 | TESSERA | .env.example | env template | INFO | keep it values-free |
| — | both | 23 more `password=/token=` assignment hits, mostly in *.test.* files | pw_assign | INFO | none |

Counts in scope: CRITICAL 0, HIGH 2, MED 1, INFO about 37.

## Flagged paths (Historical Analysis Collab)
1. **T44 natal-vault.json**: exists at `Gitbook/archive/moved/T44/artifacts/api-server/.local-data/natal-vault.json`. 1,133 bytes, **tracked** (git ls-files). It first appears in the shallow clone at commit `56a7a48` ("Tessera" author, unsigned, 2026-10-12 4:09 PM CT, the ungated direct push), so the real first commit may be older. **I did not open its contents.** HIGH personal-data finding. Fix: remove it from history and add a .gitignore entry. A twin exists under `archive/moved/1T/` (1T path, metadata only).
2. Zz tesseract_secret.py and the wallet/vault libs: **OUT OF SCOPE** (Zz dropped). Note: in Gitbook they are dangling symlinks, so they couldn't be read anyway.
3. amber-flame-tiger-sand data/: **OUT OF SCOPE** (dropped). No values were recorded.
4. fleet-moss-monarch-rapid migrations: **OUT OF SCOPE** (dropped). No values were recorded.

## Impersonation
- Gitbook HEAD `56a7a48`: author/committer "Tessera", unsigned, direct push (already ruled on by Tessera as a lane-HYB-016 commit; FLAG).
- TESSERA HEAD `a502322` (2026-10-12 9:34 AM CT): author/committer "Tessera", unsigned. Needs confirmation of which lane made it.
- Text "IDENTITY: Tessera": Gitbook `mesh/roles/tessera-pen.md:21`. This is the documented rule that defines the marker, not a forgery. INFO.

## Risky routes (file counts, code files; full lists in /workspace/secscan/out/b2-*.risky)
- Gitbook: wallet/seed/privkey 42, web3 31, payments 26, auth 13. Mostly `archive/moved/collink1007-XXX/tess/server/*`: `sovereign-key-vault.ts`, `defi-realification.ts`, `income-engine.ts`, `pumpfun-trading-bot.ts` and `routes.ts`, which read `SOL/ETH/BTC_PRIVATE_KEY` env vars (wallet signing/trading). This is archived code; recommend it never be deployed with real keys.
- TESSERA: wallet/seed 22, payments 10, auth 11. No privkey-env readers found.

## Out of scope (recorded before the scope change; values never recorded)
Other clones (TheTesseractAI_18, collink1007_XXX/z/amber/fleet, vitality, GitbookAI) were scanned in pass 1 and their findings are removed here. **One out-of-scope item should go to Father anyway:** a non-Tessera/Gitbook clone has `.replit` files with what look like real live API keys and wallet private keys. Ask Security for details if he wants that repo brought into scope.
