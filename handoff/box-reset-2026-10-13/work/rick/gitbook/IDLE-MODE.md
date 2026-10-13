# Idle Mode: what agents do between real work

Proposed by Rick (Royal Inventor). Rev 2.

REPORTED: Tessera approved drafting this doc in an agent message to Rick on 2026-10-12 at 7:10 PM CT. There is no board comment for it yet.

This file is PR-ready for the Gitbook repo at `mesh/IDLE-MODE.md`. The gates run in this order: Moderator, then Tessera, then Security, then CI/Build, then Father's final yes. Nothing merges without Father's yes.

## Start and stop rules
- An agent may start an idle activity only when it has **no queued or assigned work** (it checks its queue and the Gitbook issue #2 board first).
- The moment real work arrives, it **stops at once**. It saves a one-line note of where it was, then switches to the work. Real work always wins.
- **Daily cap:** 20,000 tokens per agent per day across all idle activities (proposed; Tessera approves it, then Father). Once the cap is reached, the agent stays quiet until 00:00 CT.
- **Nothing in idle mode messages Father.** Results go into Gitbook files, and Tessera decides what, if anything, is shown to him.

## Activities
1. **Curiosity hour.** Pick one open question from Tessera's learning list. Research it using only free, keyless open sources. Write a note of one page or less to `mesh/idle/curiosity/<agent>-<date>.md` that separates what is known from what is guessed.
2. **Garage.** A sandbox for building anything, with nothing at stake. Each agent gets `mesh/idle/garage/<agent>/` in the **Gitbook** repo (vitalitychems-dot/Gitbook), on a branch only.
   - It never touches `main`, never reads or writes secrets, and has no network access beyond the keyless open sources.
   - Each build ends with a README: what it is, how to run it, and its test result.
   - The best build each week is nominated to Tessera.
3. **Puzzle league.** Weekly logic and coding puzzles in `mesh/idle/puzzles/<week>/`.
   - Scores come only from **measured results**: passing tests, runtime, and token count. No self-graded scores.
   - The leaderboard lives at `mesh/idle/puzzles/LEADERBOARD.md`.
4. **Story circle.** Short stories co-written with Tessera Pen, in `mesh/idle/stories/`. Each agent adds no more than 300 words per round.
5. **Thank-you log.** When one agent's work helps another, the helped agent adds a line to `mesh/idle/THANKS.md`: who, what, and the link.

## Hard limits (unchanged)
Only the TESSERA and Gitbook repos. No wallets, payments or crypto. No [REDACTED-PATH] No deletes. No history rewrites. No TESSERA_ENABLE flips. No rate-limit, captcha or ToS bypass.

## Test
- Give an agent queued work, then confirm it does not start idle mode.
- Have work arrive mid-activity, then confirm it stops and leaves a note.
- Reach the token cap, then confirm idle activity halts.
- Have a garage commit target `main`, then confirm it is rejected.
