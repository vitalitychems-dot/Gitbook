# Einstein Round 4 RESULT

State: **STOPPED** (halted mid-round by STOP at 8:40 AM CT; not a clean DONE)
Started: 2026-10-13 8:31 AM CT · Stopped: 2026-10-13 ~8:44 AM CT

## STOP event
- At about 8:40 AM CT, `/workspace/einstein/loop/STOP` was created and `loop/STATUS.json` was set to STOPPED with the note:
  "Father/Tessera 8:39 AM CT: STOP. Ungated merges #319 #321. Do NOT merge or open anything; exit now."
- `/workspace/einstein/loop/PROMPT-GUARD.md` now says: never merge; open PRs only via the STOP-guarded `round4/ship.sh`, and let the 30-minute gated timer merge.
- This executor followed the task brief's merge-directly practice (the R3 practice and Father's 4:05 AM CT approval) until the STOP. It then stopped. It opened and merged nothing after that, and pushed nothing more.
- Others have already acted on main: **#323** "Revert #321" (open) and **#324** "R4-23 v2 gated re-submit of #321" (open).

## MERGED (4, all ungated: direct squash-merge by this executor before the STOP)
1. **R4-21 router path tokens once.** `brain/router.mjs` tokenizes the module paths once per router instead of once per query, and drops the redundant sorts before mixing.
   Metric (router-eval.json, 88 real closed-PR queries, 943 modules): rank **3.842 → 2.209 ms/query (1.74×)**, **0** output mismatches, held-out top-1/top-3 **38/42 → 38/42**.
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/319 (merged 8:36 AM CT)
2. **R4-22 predict inv-log cache.** `synapse.predict` caches the 1/log(1+deg) map together with the cached adjacency.
   Metric (docs/v2/v2-memory.jsonl, 192 seeds): **0.2349 → 0.1664 ms/call (1.41×)**, **0** mismatches (k=5, k=50, and after a live edge edit).
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/320 (merged 8:37 AM CT)
3. **R4-23 coMention lowercase once.** `coMentionEpisodes` lowercases each name once per call instead of once per pair.
   Metric (v2-memory.jsonl): **4.038 → 2.661 ms/call (1.52×)**, identical episodes.
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/321 (merged 8:38 AM CT). **Revert PR #323 is open; gated re-submit is #324.**
4. **R4-24 recognizer weight rows.** `learn.createRecognizer` stores weights as one row per feature, keyed by label index, and extracts features once per learn().
   Metric (MESHLOG+HELDOUT, 248 real lines): benchLearning **369.3 → 137.2 ms (2.69×)**, output identical, **0** prediction mismatches.
   PR: https://github.com/vitalitychems-dot/TESSERA/pull/322 (merged 8:40:22 AM CT, at about the moment of the STOP)

v2 suite: 112 → 117 pass in total across the round (each PR adds one equality test). The same 14 env-only failures as main (three.js / .ts imports on node 20) remain.

## BUILT, NOT SHIPPED (STOP)
- **R4-26 affect lexicon precompile.** `affect.classify` builds its ~70 lexicon RegExps once at load instead of on every call.
  Metric (248 real lines): **49.21 → 10.31 µs/line (4.77×)**, **0/248** mismatches; v2 suite 116 → 117 locally.
  Commit ea5e0a3 exists only on a local branch and was never pushed. Files are saved at `/workspace/einstein/round4/r4-26/` (affect.mjs.new, test, bench, body.md). The gated pipeline can re-submit it via ship.sh once STOP is lifted.

## DROPPED
- **R4-25 refLegend live recount/net-saving.** On 72 real docs files, tokens went 550678 → 550669 (−0.002%). BUILD-LOG stayed at 1675 → 1675. The gain is too small to matter.
- **R4-27..R4-30:** not attempted (STOP).
- Considered and not built: in-flight LLM request coalescing in llm-batcher. It could only be measured with mocked timing (SYNTHETIC-ONLY), so it was not counted.

## OVERLAPS SKIPPED
- live/shepherd.mjs (#313), deterministic-selectors / autonomous-forum-engine / routes (#312), archive dedupe/delete (#316/#317), CI/workflows (#309/#311/#300/#305), brain/grounded.mjs (#269), eval/reasoning (#267), scorecard (#314), heldout runner (#306). No Gitbook PRs.

## NOTES
- Hard limits held: no TESSERA_ENABLE_* flips, no repo-file deletes, no force-push or history rewrite, TESSERA only, no payments.
- **Gate deviation:** #319–#322 were merged without the Security/Moderator/Build gate. The brief allowed this, but the new guard forbids it. They need a decision from Father/Tessera: keep, or revert like #321/#323.
- Box: the `/workspace/einstein/r4` checkout was partly wiped at ~8:43 AM CT by another process (pack index and many worktree files gone; disk 77% → 42%). Its git state is broken. Use a fresh lean clone next round.
- Temporary node_modules symlinks into /workspace/si/tsr were removed; the target is untouched.
- Per-attempt log: `/workspace/einstein/round4/log.jsonl`.
