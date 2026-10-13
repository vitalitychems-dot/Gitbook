# diskguard — disk guardian (read-only)

Reports disk use on the shared box and suggests cleanup. **It never deletes anything.**

```
python3 diskguard.py              # markdown report to stdout + REPORT.md
python3 diskguard.py --json       # machine-readable output
python3 diskguard.py --stale-hours 12 --top 30 --roots /workspace /tmp
python3 -m unittest -v test_diskguard
```

- Overall use of the disk holding `/workspace`; warns at 85/90/95% (exit code 2 when warning).
- Top folders under each root: size (allocated blocks), newest write time, guessed owner (path keywords) and lane (git remote repo name or folder name).
- "Finished" flag: no writes for `--stale-hours` (default 6) **or** a git clone that is clean with no unpushed commits. Toolchains/backups (`ollama*`, `node22`, `backups`) are marked PROTECTED and never suggested.
- Each run appends `{ts, used, total}` to `history.jsonl`; growth rate (bytes/hour over the last 24h) and hours-until-full are computed from it.
- Cleanup suggestions are exact `rm -rf -- '<path>'` commands for **owners** to run after confirming. Guesses can be wrong.
- Stdlib only (Python 3.9+), plus `git` if present.
