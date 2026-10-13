#!/usr/bin/env python3
"""GSM8K subset baseline. Seed=42, first N after shuffle OR fixed indices."""
from __future__ import annotations
import argparse, json, re, random, time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ollama_client import generate, DEFAULT_MODEL

ANS_RE = re.compile(r"####\s*(-?[\d,\.]+)")
NUM_RE = re.compile(r"-?[\d,\.]+")

def extract_gold(answer: str) -> str:
    m = ANS_RE.search(answer)
    if m:
        return m.group(1).replace(",", "")
    # fallback last number
    nums = NUM_RE.findall(answer.replace(",", ""))
    return nums[-1] if nums else ""

def extract_pred(text: str) -> str:
    # Prefer #### or final "answer is" or last number
    m = ANS_RE.search(text)
    if m:
        return m.group(1).replace(",", "")
    m2 = re.search(r"(?:final answer|answer)\s*[:=]\s*(-?[\d,\.]+)", text, re.I)
    if m2:
        return m2.group(1).replace(",", "")
    nums = NUM_RE.findall(text.replace(",", ""))
    return nums[-1] if nums else ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=50)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--data", default="/workspace/evals/data/gsm8k_test.jsonl")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    args = ap.parse_args()

    rows = [json.loads(l) for l in open(args.data) if l.strip()]
    rng = random.Random(args.seed)
    indices = list(range(len(rows)))
    rng.shuffle(indices)
    indices = indices[: args.n]
    indices_sorted_record = sorted(indices)

    system = (
        "You are a careful math tutor. Solve the grade-school word problem. "
        "Show brief reasoning. End with a line exactly like: #### <number>"
    )
    results = []
    t0 = time.time()
    correct = 0
    for rank, idx in enumerate(indices):
        row = rows[idx]
        gold = extract_gold(row["answer"])
        prompt = row["question"].strip() + "\n\nWrite #### <final numeric answer> on the last line."
        out = generate(prompt, model=args.model, system=system, num_predict=128, num_ctx=2048, temperature=0.0)
        pred_text = out.get("response") or ""
        pred = extract_pred(pred_text)
        ok = False
        try:
            ok = abs(float(pred) - float(gold)) < 1e-6
        except Exception:
            ok = (pred == gold)
        correct += int(ok)
        results.append({
            "item_id": f"gsm8k_test_{idx}",
            "index": idx,
            "rank": rank,
            "question": row["question"],
            "gold": gold,
            "pred": pred,
            "correct": ok,
            "response": pred_text,
            "eval_count": out.get("eval_count"),
            "tok_s": out.get("_tok_s"),
            "wall_s": out.get("_wall_s"),
        })
        print(f"[{rank+1}/{args.n}] idx={idx} ok={ok} gold={gold} pred={pred} tok/s={out.get('_tok_s')}", flush=True)

    summary = {
        "benchmark": "GSM8K",
        "split": "test",
        "n": args.n,
        "seed": args.seed,
        "item_ids": [r["item_id"] for r in results],
        "indices": indices,
        "indices_sorted": indices_sorted_record,
        "correct": correct,
        "accuracy": correct / args.n if args.n else None,
        "model": args.model,
        "wall_s_total": time.time() - t0,
        "grading": "numeric equality after extracting #### or last number; commas stripped",
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as f:
        json.dump({"summary": summary, "results": results}, f, indent=2)
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
