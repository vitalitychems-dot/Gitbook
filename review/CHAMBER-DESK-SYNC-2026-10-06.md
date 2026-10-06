---
status: in review
note: Filed 2026-10-06 from Father's order to push Tessera and update Gitbook. Not a merge receipt.
---

# Chamber desk sync — 2026-10-06

Intake GB-030 · Author lane: Tessera · Date (CT): 2026-10-05 10:29 PM · Source: Father's order in this sync, plus the two open TESSERA pulls · License: TBD · Suggested path: `review/CHAMBER-DESK-SYNC-2026-10-06.md`

**Label:** branch record. Not on TESSERA `main`. Not a claim that the pen is local weights as present fact.

## Where the code is

TESSERA `main` is `9c0fa1c` (`Merge PR #8: memory redaction patterns`). That commit was already on `origin/main`. This sync had nothing new to commit on `main`.

The chamber desk is already on GitHub, on two draft pulls. Pull #10 contains pull #9.

| Pull | Branch | Head | State |
| --- | --- | --- | --- |
| [TESSERA #9](https://github.com/vitalitychems-dot/TESSERA/pull/9) | `cursor/tessera-voice-chamber-22dd` | `c8c8295` | Draft. Open. Not merged. |
| [TESSERA #10](https://github.com/vitalitychems-dot/TESSERA/pull/10) | `cursor/chat-desk-training-22dd` | `aa4c294` | Draft. Open. Stacked on #9. Not merged. |

Father's order was "Push all to GitHub repo tessera and update GitHub repo Gitbook as well." It did not include the word `merge`. Origin and TESSERA merges still need that word. These pulls stay open.

## What the branch says it does

This is the pull text, labeled **REPORTED**. This sync did not re-run the suite.

- Identity questions answer as Tessera through the pen line. A Grok self-claim, a tile definition, or an untrusted search dump is replaced before it is shown or copied.
- The desk header is Tessera, with the pen line and the line that agents may change only Tessera and Gitbook. The placeholder is "Speak with Tessera". The tabs named in the pull are Chamber, World, Board, More. The chamber background is not the full-screen animation.
- A prompt can call a member or an agent only when that seat is free. Tessera's close leads. Unavailable seats are named unavailable. `@Grok` and other foreign model names are refused.
- `train:` stores a lesson on this process. `Tessera give final answer` returns the latest trained close, or the pen line when none is stored.
- A clock, a count, a unit conversion, or the moon is answered from the desk, with the source named. A what/who/where question may read one Wikipedia sentence only when that page shares the question's words. A user correction (`actually ...`) is kept as the user's words for the next matching question.

The published desk note still says the pen is xAI/Grok, and [who Tessera is](../mesh/roles/who-tessera-is.md) still says owned weights on Father's hardware remain a goal. Those pages stay as published. The branch UI says the pen is local open weights. That sentence was seen in a local preview. It is not a sealed proof that the weights are local.

## Checks

| Check | Label | Result |
| --- | --- | --- |
| TESSERA `main` already matches `origin/main` | **TESTED** this sync | `git status` clean. No unpushed commits. |
| Pull #9 CI `validate` on run `37403946170` | **TESTED** (the run exists and failed) | Failed at `pnpm audit`. Reported severity: 1 critical (`proxy-addr`), 2 high (1 ignored), 2 moderate, 1 low. |
| Pull #10 status checks | **REPORTED** | None recorded on the pull at sync time. |
| Implementing agent: vitest voice and eval, 6 passed; later chamber-learning, chat-collab, and tessera-voice, 20 passed | **REPORTED** | Written on the pulls. Not re-run here. |
| Implementing agent: headless Chrome, injected stream "I am Grok...", name / where / who showed the pen sentence | **REPORTED** | Written on pull #9. Not re-run here. |
| Separate retest, local preview `http://127.0.0.1:5174/c/1`, files not changed | **TESTED** by that retest, **REPORTED** here | Header three lines, placeholder, Learn pen sentence, and a flat background passed. Chamber was the visible active tab. Other tab labels were not readable. Live replies failed: EventSource got `application/json` instead of `text/event-stream`. Copy was not exercised. |

## Not done

- TESSERA `main` does not contain this chamber code.
- Do not mark the desk LIVE or DONE.
- Do not merge pull #9 or #10 until Father says `merge` and the audit failure is actually fixed or explicitly waived. This page does not waive it.
- Gitbook `main` does not contain this page until this pull is merged.
