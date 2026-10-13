#!/usr/bin/env python3
"""HumanEval subset: generate completion, execute tests in subprocess with timeout."""
from __future__ import annotations
import argparse, json, random, re, time, sys, tempfile, subprocess, textwrap, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ollama_client import generate, DEFAULT_MODEL

CODE_FENCE = re.compile(r"```(?:python)?\n(.*?)```", re.S)

def extract_code(text: str, prompt: str) -> str:
    # Prefer fenced code; else take from first 'def ' or whole text
    m = CODE_FENCE.search(text)
    if m:
        code = m.group(1)
    else:
        code = text
    # If model repeated prompt, keep from last def matching
    if prompt.strip() in code:
        # completion only after prompt
        idx = code.find(prompt.strip())
        if idx >= 0:
            code = code[idx:]
    # If response looks like completion only (no def), prepend prompt
    if "def " not in code and "def " in prompt:
        code = prompt + code
    # Strip leading prose lines before first def/import/from/class
    lines = code.splitlines()
    start = 0
    for i, ln in enumerate(lines):
        if ln.startswith(("def ", "import ", "from ", "class ", "@")):
            start = i
            break
    return "\n".join(lines[start:]).strip() + "\n"

def run_tests(code: str, test: str, entry_point: str, timeout: float = 5.0) -> tuple[bool, str]:
    # Build a script: code + test + check(entry_point)
    script = code + "\n\n" + test + f"\n\ncheck({entry_point})\nprint('PASS')\n"
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "candidate.py"
        path.write_text(script)
        try:
            # sandbox-ish: no network needed; restrict via env
            env = os.environ.copy()
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            p = subprocess.run(
                [sys.executable, str(path)],
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=td,
                env=env,
            )
            ok = p.returncode == 0 and "PASS" in p.stdout
            detail = (p.stdout + "\n" + p.stderr)[-2000:]
            return ok, detail
        except subprocess.TimeoutExpired:
            return False, "TIMEOUT"
        except Exception as e:
            return False, repr(e)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--data", default="/workspace/evals/data/HumanEval.jsonl")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--timeout", type=float, default=5.0)
    args = ap.parse_args()

    rows = [json.loads(l) for l in open(args.data) if l.strip()]
    # Use first N in official order for HumanEval (common practice) but record seed policy
    # Task asks fix seed and record IDs — use first N to match common subset, seed noted for reproducibility of other benches
    selected = rows[: args.n]

    system = (
        "You are a Python coding assistant. Complete the function. "
        "Return only valid Python code that completes the given prompt. "
        "Do not explain. Prefer a single ```python code block."
    )
    results = []
    t0 = time.time()
    correct = 0
    for rank, row in enumerate(selected):
        prompt = row["prompt"]
        out = generate(
            "Complete this Python function. Output code only.\n\n" + prompt,
            model=args.model,
            system=system,
            num_predict=256,
            num_ctx=3072,
            temperature=0.0,
            timeout=240,
        )
        pred_text = out.get("response") or ""
        code = extract_code(pred_text, prompt)
        ok, detail = run_tests(code, row["test"], row["entry_point"], timeout=args.timeout)
        correct += int(ok)
        results.append({
            "item_id": row["task_id"],
            "rank": rank,
            "entry_point": row["entry_point"],
            "correct": ok,
            "detail": detail[:500],
            "code": code[:4000],
            "response": pred_text[:2000],
            "eval_count": out.get("eval_count"),
            "tok_s": out.get("_tok_s"),
            "wall_s": out.get("_wall_s"),
        })
        print(f"[{rank+1}/{args.n}] {row['task_id']} ok={ok} tok/s={out.get('_tok_s')}", flush=True)

    summary = {
        "benchmark": "HumanEval",
        "split": "official",
        "n": args.n,
        "seed_note": "first N problems in official HumanEval.jsonl order (not shuffled); seed=42 unused for selection",
        "seed": args.seed,
        "item_ids": [r["item_id"] for r in results],
        "correct": correct,
        "pass_at_1": correct / args.n if args.n else None,
        "model": args.model,
        "wall_s_total": time.time() - t0,
        "grading": f"execute HumanEval check() in sandboxed subprocess timeout={args.timeout}s",
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as f:
        json.dump({"summary": summary, "results": results}, f, indent=2)
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
