# git72 — Gitbook #72 prototypes (Rick)
Local-only, zero-token prototypes for #72: git bundles as an offline web transport (gitweb/), a git-commit work queue run with no network and no LLM (offline_queue/), git-object dedup fix for /workspace/ops/autoclean.sh (disk/), and the cheapest way to read one file from a repo (speed/). Every bench builds tiny fixtures under /tmp/git72-*, prints JSON, and deletes them afterward. Python 3 stdlib + git/zstd/hardlink only.

Run all: `./run_all.sh` (writes last_result.json; baseline.json only if missing; aborts if / ≥95%).
Run one: `python3 gitweb/run_bench.py` · `python3 offline_queue/run_bench.py` · `python3 disk/run_bench.py` · `python3 speed/run_bench.py`.
Worker alone: `offline_queue/worker.sh <clone-dir>` (claims one job from queue/open; exit 3 = queue empty).
