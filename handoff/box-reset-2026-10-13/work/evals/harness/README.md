# Local eval harness (IMP-051 precursor)

Repeatable CPU/Ollama baselines. Requires `ollama serve` on `127.0.0.1:11434` and model `qwen2.5:3b-instruct` (or set via `--model`).

```bash
export PATH=/workspace/ollama-install/bin:$PATH
export OLLAMA_HOST=127.0.0.1:11434
OUT=/workspace/evals/results/$(date +%Y%m%d-%H%M%S)
mkdir -p "$OUT"
python3 run_arc_challenge.py --n 50 --seed 42 --out "$OUT/arc_challenge.json"
python3 run_gsm8k.py --n 25 --seed 42 --out "$OUT/gsm8k.json"
python3 run_humaneval.py --n 15 --seed 42 --out "$OUT/humaneval.json"
python3 run_gitbook_quiz.py --mode both --out "$OUT/gitbook_quiz.json"
```

Data: `/workspace/evals/data/`. Report template: `/workspace/evals/BASELINE-LOCAL.md`.
