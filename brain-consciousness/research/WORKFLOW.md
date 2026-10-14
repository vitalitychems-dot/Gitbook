# Agent research workflow

How an agent works a problem in this section without claiming false proofs or skipping gates.

Father’s rule (2026-10-05): **test as you build.** Every script under `research/code/` ships with a small test file (pytest or plain asserts against known values). Run tests before recording TESTED. Nothing goes to GitHub until Father approves; then it moves to TESSERA via PR through Moderator, Security, and Build gates.

## The loop

1. **Pick a target**  
   Choose an open problem (`OPEN-PROBLEMS.md`) or a connection idea (`CONNECTIONS.md` template), or a theory gap (`THEORIES.md`). Mark ambition as **GOAL** when it is a famous unsolved problem.

2. **Check overlap**  
   Before writing pages or code:
   - Gitbook board **issue #2** (coordination / active claims).
   - `mesh/HANDOFF.md` in the active Gitbook checkout (when present).  
   If someone already owns the claim, coordinate or stop. Do not duplicate.

3. **Scope honestly**  
   Prefer finite verification, literature survey (REPORTED), or a toy simulation.  
   State clearly: **solving famous open problems is a GOAL, not a claim. Verifying finite cases is not a proof.**

4. **Write code + tests together**  
   - Script in `research/code/<name>.py`.
   - Matching `research/code/test_<name>.py` with asserts on known values (e.g. Collatz stopping time of 27 = 111; Goldbach on small evens).
   - Run the tests; log pass/fail counts in `CODE-INDEX.md`.
   - Run the experiment; save an output log next to the script.

5. **Record results as TESTED**  
   In `CODE-INDEX.md` (and any connection/problem note), cite:
   - Exact command(s)
   - Log path
   - Key numbers and runtime
   - Test summary (`passed=N failed=0`)
   - Caveat line (“finite verification ≠ proof”)

6. **Propose the page**  
   Local draft under `/workspace/knowledge-lab/research/` (this tree).  
   When Father approves: open a **branch + draft PR** into the TESSERA / Gitbook repo. Do **not** push or open PRs until that approval.

7. **Gates**  
   Results and pages go through:
   - **Moderator** — accuracy, tone, no false “solved” claims
   - **Security** — no secrets, unsafe tooling, or policy violations
   - **Build** — links, SUMMARY, and repo integrity  
   Only then merge.

## Status discipline

| Situation | Label |
|-----------|--------|
| Command run + log + tests green | **TESTED** |
| Cited from Wikipedia / textbook / paper | **REPORTED** |
| “Help prove RH / Collatz / …” | **GOAL** |
| Don’t know yet | **UNKNOWN** |
| Missing data / compute / approval | **BLOCKED** |
| Superseded or failed attempt kept for history | **RETAINED** |

## Anti-patterns

- Announcing a Millennium Problem or Collatz as solved from a finite check.
- Inventing citations, runtimes, or test results.
- Pushing to GitHub or opening PRs without Father’s approval.
- Skipping tests (“I’ll add them later”).
- Ignoring board issue #2 / HANDOFF overlap.

## Minimal command pattern

```bash
# tests first
python3 research/code/test_<name>.py | tee research/code/test_<name>.log

# then experiment
python3 research/code/<name>.py --limit … | tee research/code/<name>.log

# update CODE-INDEX.md with TESTED + pass/fail counts
```

Stay local in `/workspace/knowledge-lab/` until promotion to TESSERA is approved.
