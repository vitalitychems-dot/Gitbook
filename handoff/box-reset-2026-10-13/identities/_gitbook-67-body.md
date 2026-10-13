Father ordered (5:25 AM CT): put every task and how to finish it in Gitbook so nothing is lost. The box disk is 100% full and its Shell is hanging. Written by Tessera.

## Global rules (Father, 2026-10-13)
- **Merges:** MERGE FREEZE. Nothing merges without `Security PASS <head-sha>` and green CI, plus a Build PASS for TESSERA and a Moderator PASS for Gitbook.
- **Measured wins only:** never lower any test score, and put before/after numbers in every PR.
- **Priority order:** token efficiency and speed first, then accuracy.
- **Saving tokens and disk:**
  - Read through the GitHub API instead of cloning. If a clone is needed, make it shallow and blobless and delete it after use.
  - No duplicate files, and clean /tmp after every task. Store results on GitHub.
- **Scope and privacy:**
  - Only TESSERA and Gitbook are edited. Other repos are read-only.
  - TESSERA is public, so private data never goes there.
- **Commits:** as `vitalitychems-dot <332565808+vitalitychems-dot@users.noreply.github.com>`, NEVER as user.name=Tessera.
- **Hard limits:** no wallets or payments, no repo or data deletes without Father's list approval, no TESSERA_ENABLE flips, no history rewrites.
- **1T vault:** Tessera only. Store encrypted files and read; never delete or move. Other agents don't touch it.
- **Agent caps:** 12 running, 4 children each, depth 3. Agents take their next task on finishing, under Father's auto-approval and within these rules.

## P0 — disk (owner: every lane)
- **Where it stopped:** the box disk filled to 100%. The big clones are /tmp/gb (7.4G, Tessera's executor), /tmp/gb70 (11G, Tessera's; it was pushed as PR #65, so it's safe to delete) and /tmp/tchk (5.5G, a bare TESSERA clone, owner unknown).
- **To finish:** delete your own pushed or reproducible clones, report the GB freed to Command Center, and keep the disk under 80%.

## Fixes approved by Father ('Fix all', 4:46 AM; Moderator's chat 4:49 AM) — owner: Tessera
All are NOT started; the box stalled before anything was pushed.
1. **autogate gate-bypass fix (Security HIGH on #56/#62).**
   - Apply /workspace/security-gate/autogate-fix.patch (made on 243ddd4) to the current main (past efcca74).
   - Remove `--merge`. `--father-approved` must require a `FATHER APPROVED <sha>` comment by vitalitychems-dot, or Father's label.
   - Open the PR, then gate it with Security and Moderator.
2. **PR #65 (GB-070 rev3), branch gb-070-rev3, head 7a893548:**
   - Add the missing mesh/ledger/ledger-15.md from /workspace/gitbook-cordnation/GB-070/GB-070-rev3.diff.
   - Relabel #55 as 'partial record'. Then gate it with Security.
3. **Moderator retro fixes:** /workspace/retro/moderator-retro-fixes.patch (commit 2cd026f).
   - Labels #62's numbers SYNTHETIC-ONLY, fixes the #60 handoff line, marks #63's gains REPORTED and the token figure as an ESTIMATE, and adds the HANDOFF lines.
   - Moderator is waiting for the PR number and head SHA.
4. **TESSERA LOW fixes:**
   - .gitignore rules `**/creator/*.jsonl` and `**/father-msgs*.jsonl`.
   - Run the redactor in pack.mjs packV3; packer recall must stay 21/87.
5. **TESSERA V3-P3 regression:** repeat calls to the v3 crystal `/brain/snapshot` take 5.8 ms vs v2's 0.7 ms.
   - Cache the snapshot by t and prev. If it can't reach 0.7 ms or better, route repeat calls back to v2.

## Tesseract (Father 4:47–5:01 AM) — owner: Tessera
NOT started (disk).
- **Planned output files:** in /workspace/tesseract/ (move to GitHub storage): TESSERACT-DESIGN.md, AUDIT.md, CLEANUP-CANDIDATES.md, FATHER-LOG-INSTRUCTIONS.md and REA-DEPTH2.md, plus /workspace/dispatch/prompts-tesseract.json.
- **Location:** artifacts/tesseract/ in TESSERA, behind TESSERA_TESSERACT=0. v2 and v3 stay live until Tesseract wins every benchmark.
- **Scope:**
  - (a) One combined app with chat and a new theme, after reading ALL past theme files.
  - (b) A 5D brain view of the real memory graph that can be pulled apart and zoomed.
  - (c) A live clickable flow chart.
  - (d) A live voxel world of the agents, real actions only, nothing simulated.
  - (e) Sovereignty: list external dependencies and how to self-host or replace each.
  - (f) REA on every repo mentioned anywhere, to depth 2 (owned repos, then the repos they reference, then theirs). Cap level 2 at the 500 most-referenced. Licenses must check out. Reuse REA-UNUSED-PARTS.md.
  - (g) A cleanup inventory. Delete NOTHING without Father's approval. Known candidates: archive/from-gitbook/archive (1805 files), archives/source-repositories/Zz (235), archives/migration-review/legacy-ui (111), .agents/skills (400+).
  - (h) List every instruction Father pasted in logs, with its status.
  - Also catalogue: private repos, languages, compression methods, old authors and ideas, and the AI apps referenced.
- **Then:** 10 build-test rounds. Each round builds the next version and tests it, plus mixed combinations, against the previous one; only versions that beat it are kept. Last step: combine the agents into Tesseract 'fractions'.
- **Known facts:** TESSERA main is c80e5f9e (#293). Baselines are in /workspace/full-picture/BASELINE.md, and the prompt template rules are in /workspace/dispatch/prompts-wave3.json.

## Creator profile (Father 5:05–5:06 AM) — owner: Tessera ONLY (private)
- Read all TESSERA files (via the API) plus past chats and convos, and build a sourced profile of Father: strengths, weaknesses, vulnerabilities, what to improve, and metacognition practice.
- No IQ or EQ number unless measured (the ICAR test is offered).
- PRIVATE: store encrypted in the 1T vault or /workspace/secrets/creator. NEVER commit it to TESSERA.
- Existing work: TESSERA #281 (style fingerprint, AUC 0.996). The next-ask predictor was dropped because it didn't beat the baseline.

## Prompts ready to launch after the freeze lifts — owner: Tessera
- /workspace/dispatch/prompts-father-undone.json:
  - FU-01: real tokens per PR in the scoreboard.
  - FU-02: weakest-skill curriculum, kept only if it beats round-robin.
  - FU-03: a new PR to replace #39.
- /workspace/build-plan-2026-10-12/prompts-v3.json:
  - V3-P1: wire the packer into the live prompts and check with a real tokenizer.
  - V3-P2: 16-word cutoff fact check.
  - V3-P3: same as fix 5 above.

## Waiting on other lanes
- **Security:** retro gate for #274 and #281 is done (content PASS, provenance FAIL). Security gates every new PR head.
- **Cordnation:** log PR #65 as 'open, incomplete'; can't open PRs (read-only).
- **Rick:** charter approved by Father ('yes to all bots'), with Security PASS still required. Rick drafts the charter PR.
- **Command Center:** enforces the merge freeze and names violators.
- **Build:** duplicate scan at /workspace/dedupe/DUPLICATES-2026-10-13.md. Deletes need Father's yes.

## Needs Father
- Gitbook #40 (close or merge).
- Key rotations and the GitHub Support purge.
- Moltbook claim via X (he has no X account).
- The cleanup delete list, once written.

## Merged earlier today (for the record)
- **TESSERA:** #260–#266, #268, #270–#272, #274 and #281. Most were self-merged with no gate (Security PROV-FAIL).
- **Gitbook:** #55, #57–#63. #62 still has a HIGH, fixed by fix 1 above.
