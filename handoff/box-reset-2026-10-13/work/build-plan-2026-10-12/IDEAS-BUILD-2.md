# IDEAS-BUILD-2: brain round 2 (Oct 13, 2026, about 2:00–2:40 AM CT)

PR https://github.com/vitalitychems-dot/TESSERA/pull/256 is **MERGED** as `e6a0aa2f` (squash, author-email is the no-reply address), on base `e0e5f64`. It ran on Node 22.23.3.

1. **Learning loop.** Outcome-driven recognizer: an averaged perceptron with error-prioritized replay and Leitner spaced repetition. The schedule was picked by 5-fold CV on 198 dev lines, then scored once on a fresh hidden split of 50 lines.
   - Intent: accuracy 0.74 → **0.86**, F1 0.591 → 0.667. **GAIN.**
   - Affect: accuracy 0.72 → 0.72, F1 0.496 → 0.509. **No meaningful gain.**
2. **Anatomical human layout.** 0/360 → **360/360** parcels sit at real HCP-MMP1 centroids (MNI152 centre of gravity, attributed). Spearman of distance vs tract strength is −0.15. Render: `brain-view/brain-human-r2.png`. **DONE.**
3. **Real self-scan.** Tessera parsed the real main test log into 6 suggest-only proposals: 4 slow browser tests over 5 s, 1 failing test, and 1 slow brain test.
   - 0 of 6 passed the gates. All 6 failed has-test-ref, tests-passed and no-self-approve.
   - The slow brain test became a real patch: B1-06 went from 1256 ms to **85 ms** (−93%). It passed 7 of 8 gates, and the 8th (a non-Tessera approver) was the PR merge.
   - Nothing was applied automatically.
4. **Empathy set.** **218** real mesh/agent transcript sentences, PII stripped and hand-labelled. The lexicon scores intent accuracy 0.67 (F1 0.45) and affect accuracy 0.743 (F1 0.216). The learned model is item 1.
5. **Embedding recall.** **NOT DONE.** `ollama pull all-minilm` was refused (the redirect goes to a non-public address under network policy), and the disk hit 100% at one point. recall@5 stays at 13/87 from round 1.

Renders: `brain-view/brain-human-r2.png`, `brain-memory-r2.png`, `brain-memory-r2.mp4`, `brain-memory-r2.gif` (432 real Hebbian edge firings in the clip).

Tests: v2 115/116. The one failure (v2-062) is a sparse-checkout artifact: the file wasn't checked out locally.

Leftover: branch `ideas-b2-brain` is stale (it was pushed before the rebase and has no PR). I didn't delete it because deletions need approval.
