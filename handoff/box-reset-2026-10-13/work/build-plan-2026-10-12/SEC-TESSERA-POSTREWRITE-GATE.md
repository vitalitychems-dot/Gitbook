# SEC — TESSERA post-rewrite gate (2026-10-12 ~7:15 PM CT) — VERDICT: FAIL (1 blocker)
Pinned: work.git main 89961129 (all 250+ refs: refs/heads only; 0 tags/notes/stash/pull/original/replace; packed-refs heads only) and tree 43d3d319. Read-only; no values recorded. Tools: gitleaks 8.21.2 --log-opts=--all --redact; streaming regex + literal pass over every object from `git rev-list --all --objects` (blobs AND commit objects).

## (1) gitleaks + regex
- gitleaks work.git: 2 hits, tree: 2 hits — both FIXTURE (colonial-secret-fail-closed.test.ts, compression-pipeline.test.ts). OK.
- Regex pass (gh tokens, github_pat, sk-or-v1, xai-, AIza, AKIA, xox*, JWT, glhf, KEY/SECRET=… assignments, DB URLs w/ password): 0 hits. PEM header: 2 files, both UI placeholder strings in CredentialsPage.tsx (form placeholder "-----BEGIN RSA PRIVATE KEY-----", no body). OK.
## (2) Paths (rev-list --all --objects, 20821 objects)
- 1T/, natal-vault*, .local-data/, Zz data/ingest/*.txt, secret-society.json, drive-rest share-*.html, collink1007-XXX/{,tess/,x/}.replit, Zz .replit files: ABSENT. OK.
- Remaining: root `.replit` (no env assignments with values) and `.replit-artifact/artifact.toml` files — no values. Other `data/ingest/manifest.json` (non-Zz archives) — manifests only.
## (3) Literal hash compare vs /workspace/sec-history/TESSERA
- Preview secret (sha256 prefix 69f433c5bff5): 0 occurrences in any object. OK.
- **BLOCKER — old TESSERACT_ADMIN_KEY (sha256 prefix 8517a2325160) survives in COMMIT MESSAGES** (line 3 of message) of 2f70b40206 and cb64a013ee ("Add a custom phrase to unlock the gate and start the zodiac binding process", 2026-04-17 7:10 PM CT, author trentvitality77), reachable only from branch `replit-agent`. filter-repo --replace-text does not touch messages.
  - Smallest fix: delete branch `replit-agent` from the rewrite (if not needed), OR `git filter-repo --replace-message <exprfile>` with the literal (local file only), then gc. Either way rotate the admin key (already required).
## (4) git-crypt coverage (43d3d319)
- .gitattributes: config/secrets/**, **/*.secret.json, **/*.secret.jsonl, .env, .env.local (+ README.md, .gitattributes exempt).
- Files matching the globs in the commit: only config/secrets/README.md (exempt, plaintext by design). No .env/.secret.json(l) files committed → 0 files require encryption; 0 unencrypted matches. PASS (vacuous).
- Gap (non-blocking): ".env*" was described, but only `.env` and `.env.local` at repo root are covered; `.env.production`, `.env.*.local`, and nested `**/.env` are NOT. Smallest fix: add `.env.*`/`**/.env*` lines with `!filter` for `.env.example`.
- Sensitive-named files outside globs reviewed by shape: collink1007-XXX/tess/server/{dimensional-secrets.json (lore text), saved-credentials.enc.json (2 bytes, empty), token-agency.json / token-factory-state.json (counters)} — no secrets. lib/db/drizzle/0003_natal_chart_schema.sql = schema only.
## (5) jsonl
- docs/v2/v2-memory.jsonl (467 lines): 0 secrets, 0 emails, 0 phones/SSN/cards/addresses; "natal" 1 (L163 = risk-entity naming the Gitbook natal-vault path, no data); dates 9 (L166–184, doc dates); handles 68 (vitalitychems 42, collink1007 21, "Father" 5; L2,21,26,28,55,…) — account/owner names already public via GitHub.
- data/school/{corrections,read-one,voice}.jsonl (5/15/3 lines): clean.
- Verdict: SAFE to leave unencrypted for public. Optional: genericize "Father" references.
## (6) Diff vs TESSERA-PUBLIC-SCAN.md
- Agree: gitleaks 2 FIXTURE hits; regex 0; paths gone; preview secret 0; git-crypt rules.
- Disagree: report says "Literal pass (all original secret values): 0 hits" — misses the admin key in 2 commit messages on `replit-agent` (its pass scanned diffs, not message bodies).
- Not in report: .env* glob gap; commit author/committer emails (gmail addr + others) become public — use GitHub noreply if undesired (non-blocking).
## Caveats
- GitHub server-side refs/pull/* and cached views/forks keep pre-rewrite objects (incl. natal-vault, keys): need GitHub Support purge after force-push, or accept risk. Rotate admin key, preview secret, and any real collink .replit keys regardless.
## Re-gate
After fix: rerun `python3 /tmp/sg/scan.py work.git` style literal pass incl. commit objects → expect 0 LIT hits; then PASS.

---
# RE-GATE (2026-10-12 ~8:05 PM CT) — work.git 0f5eab28: PASS | tree fdce23ea: FAIL (stale base) → overall FAIL
## work.git main 0f5eab28 (253 refs, heads only; no tags/notes/stash/pull/original)
- git fsck: clean (exit 0).
- gitleaks --all: 2 hits, FIXTURE only (compression-pipeline.test.ts, colonial-secret-fail-closed.test.ts @4de1eb94).
- Regex + literal pass over every object incl. commit objects/messages: admin key (8517a2325160) 0, preview secret (69f433c5bff5) 0, token-format regexes 0 (only PEM placeholder strings in 2 CredentialsPage.tsx).
- replit-agent: old 2f70b40206/cb64a013ee gone; rewritten as 316e3e99/e74ae41a. Message line 3 now holds a 13-char string (sha256 39af656422b0), which matches no baseline secret and appears in no blob. Treated as the replacement text.
- Paths: 13 scrub paths, 1T/, natal-vault*, .local-data/, Zz ingest, collink/Zz .replit: 0 objects. Root .replit: 0 valued key assignments.
- Emails (author+committer, all refs): only 332565808+vitalitychems-dot@users.noreply.github.com (3412), 206951365+cursor[bot]@users.noreply.github.com (21), manus@users.noreply.github.com (3). OK.
## tree fdce23ea — BLOCKER
- fdce23ea → 43d3d319 → 89961129 sit on the OLD pre-fix history; 0f5eab28 is not in this clone (origin refs stale). This history still has: the admin key in commit messages (literal hits 2), 630 gmail author emails plus ~25 other non-noreply/replit addresses, `evo@test` (2), and a malformed mailmap result `3.32565808e+08+vitalitychems-dot@users.noreply.github.com` (29, e.g. 673fbda7).
- Pushing fdce23ea as-is would reintroduce all of that.
- Smallest fix: `git fetch origin` in the tree, then cherry-pick/rebase 43d3d319+fdce23ea onto 0f5eab28 (as the noreply identity), then re-gate the new SHA. Also check the mailmap for the float-formatted entry (it is absent from work.git, so only the stale tree has it).
- .gitattributes (fdce23ea): covers .env, .env.local, .env.*, **/.env*, config/secrets/**, **/*.secret.json(l); exempts .env.example, **/.env.example, config/secrets/README.md. Matching files: only .env.example and config/secrets/README.md (both exempt, plaintext). 0 files needing encryption. Coverage OK.
## Caveat
GitHub-side refs/pull/* and caches still need a Support purge after the force-push. Rotate the admin key and the preview secret regardless.

---
# RE-GATE (2026-10-12 ~8:05 PM CT) — work.git main 0f5eab28 / tree fdce23ea — VERDICT: FAIL (1 blocker, tree only)
## work.git @ 0f5eab28, all 253 refs (heads only; no tags/notes/stash/pull/original/replace) — CLEAN
- git fsck: exit 0, no errors.
- gitleaks --all: 2 hits, FIXTURE only (compression-pipeline.test.ts, colonial-secret-fail-closed.test.ts @4de1eb94).
- Regex pass over every object incl. commit objects + `git log --all --format=%B`: 0 hits (PEM: 2 UI placeholders in CredentialsPage.tsx only).
- Literal hash compare, every object incl. commit messages: admin key 8517a2325160 = 0, preview secret 69f433c5bff5 = 0.
- replit-agent: branch still exists; 2f70b40206 / cb64a013ee no longer exist (rewritten), and the literal is absent → clean.
- Paths: 13 scrub paths, 1T/, natal-vault*, .local-data/, Zz ingest, secret-society, drive-rest shares: absent. Root `.replit`: 9 blob versions, 0 key/secret assignments with values.
- Emails (author+committer, all refs): only 332565808+vitalitychems-dot@users.noreply.github.com (3412), 206951365+cursor[bot]@users.noreply.github.com (21), manus@users.noreply.github.com (3). No gmail/other. PASS.
## tree @ fdce23ea — BLOCKER
- .gitattributes correct: .env.*, **/.env* encrypted; .env.example and **/.env.example exempt (plus prior rules). Matching files in commit: only .env.example (exempt, plaintext) and config/secrets/README.md (exempt). 0 files need encryption; 0 unencrypted matches. Coverage PASS.
- **BLOCKER: fdce23ea is built on the OLD rewrite 89961129, not on 0f5eab28.** `tree` origin refs were never re-fetched; 0f5eab28 is not in tree. Pushing fdce23ea would reintroduce the whole pre-fix history: admin-key commit messages (2f70b40206/cb64a013ee via origin/replit-agent) and 630 vitalitychems@gmail.com + replit/cursor/other emails (also 29 malformed "3.32565808e+08+vitalitychems-dot@…" and evo@test).
  - Smallest fix: in tree, `git fetch origin` then rebase/cherry-pick 43d3d319+fdce23ea onto 0f5eab28 (author = noreply), producing a new tip; re-gate that SHA. Do not push fdce23ea.
- Note: work.git main has no .gitattributes yet (git-crypt commits not in it), so the public main is not covered until the rebased commits land.
## Caveat (unchanged)
GitHub server-side refs/pull/* , caches and forks keep pre-rewrite objects → Support purge or accept risk; rotate admin key, preview secret, any real collink .replit keys.

---
# RE-GATE 2 (2026-10-12 ~8:17 PM CT) — tree branch `rebased` 4f354393 — VERDICT: PASS
- Chain: 4f354393 → fa9a92d8 → 0f5eab28. 89961129, 43d3d319, fdce23ea are NOT ancestors.
- New commits: author+committer 332565808+vitalitychems-dot@users.noreply.github.com.
- Diff vs 0f5eab28 (.gitattributes, learning-memory.test.ts:~L? token fixture, config/secrets/README.md): 1 regex hit = synthetic test fixture (concatenated "ghp_" + alphabet placeholder) restoring the scrubbed fixture; not a real secret.
- Hash compare over all commit messages in 4f354393 history + diff: admin key 8517a2325160 = 0, preview secret 69f433c5bff5 = 0.
- Emails (full history of 4f354393): vitalitychems-dot noreply 1136, cursor[bot] noreply 21, manus noreply 3. No others.
- .gitattributes: .env, .env.local, .env.*, **/.env* → git-crypt; .env.example, **/.env.example exempt. Matching tracked files: only .env.example (exempt, plaintext). No unencrypted .env files.
- Remaining (non-blocking): GitHub-side refs/pull/*, cache, forks purge via Support; rotate admin key, preview secret, collink .replit keys.

---
# RE-GATE 3 (2026-10-12 ~8:35 PM CT) — final.git main ae58a7e5 (f133605c + ae58a7e5 on 1e7453f7 #250) — VERDICT: OK
- Refs: 257, all refs/heads. fsck --full exit 0, no output.
- gitleaks --all: 2 hits, FIXTURE only (compression-pipeline.test.ts:10, colonial-secret-fail-closed.test.ts:39 @4de1eb94), same as before.
- Key-hash compare over all commit messages: 8517a2325160 = 0, 69f433c5bff5 = 0.
- Paths: natal-vault, /1T/, .local-data, z-app/data/ingest, secret-society.json, drive-rest share HTMLs, collink .replit = 0. (natal-chart*.ts source files and remaining collink/drive-rest content are the same as the PASSed work.git; not scrub targets.)
- Emails (all refs): vitalitychems-dot noreply 3438, cursor[bot] noreply 21, manus noreply 3. Nothing else.
- Top 2 commits: diff ae58a7e5~2..ae58a7e5 byte-identical to tree 0f5eab28..4f354393 (PASS at RE-GATE 2), so .gitattributes coverage is unchanged and OK.
- 8 new commits 0f5eab28..1e7453f7: noreply author+committer, diff regex 0 hits.
- prepush.log: only `git branch -d` cleanup lines, the f133605c commit, and the final line `error: No such remote 'origin'` (the push did not happen). No secrets/URLs with credentials.
- push-rewrite.sh line 31 fixed to `set-url ... || remote add origin ...` (same URL); backup push-rewrite.sh.bak3; bash -n OK; not run.
