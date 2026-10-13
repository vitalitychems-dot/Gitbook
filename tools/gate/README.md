# tools/gate — Moderator gate tools

| file | what |
|---|---|
| `regate.sh OWNER/REPO PR OLD NEW` | Read-only interdiff re-gate helper. Prints the interdiff files, all PR commit authors/committers, CI check runs on NEW and locked-path hits. Posts nothing. **Fails closed** (exit 1 on a failed check, 2 on bad args, 3 on any API error): head must equal NEW, OLD..NEW must be a fast-forward, every email must be the noreply, CI must be completed/success with at least one run, and no locked-path hit. Exit 0 means the mechanical checks pass; a Moderator still reads the interdiff and posts the verdict. |
| `locked.py` | Locked-path matcher used by regate.sh: built-in defaults plus the repo's `mesh/policy/protected-paths.txt` / `gate/locked-paths.txt` from main. |
| `gate-check.sh DIFF SHA256 [BASE]` | Doc-package checker (hash, shape, red flags, apply). |
| `consciousness-test/` | Weighing-of-the-Heart **behavioural proxy** (`RUBRIC.md`, 42 `questions.json`, `score.py`). It cannot prove consciousness. The answer key `truth.json` is **private** and is not in git; it stays on the box. |

Tests: `bash tools/gate/tests/test_regate.sh && python3 -m unittest discover -s tools/gate/tests -p 'test_*.py'`
