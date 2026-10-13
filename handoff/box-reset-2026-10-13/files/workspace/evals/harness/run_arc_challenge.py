#!/usr/bin/env python3
"""ARC-Challenge subset (multiple choice)."""
from __future__ import annotations
import argparse, json, random, re, time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ollama_client import generate, DEFAULT_MODEL

LETTER_RE = re.compile(r"\b([A-D])\b")

def extract_letter(text: str) -> str:
    m = re.search(r"(?:answer|choice|option)\s*[:=]\s*([A-D])\b", text, re.I)
    if m:
        return m.group(1).upper()
    # last standalone A-D
    letters = LETTER_RE.findall(text.upper())
    return letters[-1] if letters else ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=50)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--data", default="/workspace/evals/data/ARC-Challenge-Test.jsonl")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    args = ap.parse_args()

    rows = [json.loads(l) for l in open(args.data) if l.strip()]
    rng = random.Random(args.seed)
    indices = list(range(len(rows)))
    rng.shuffle(indices)
    indices = indices[: args.n]

    system = (
        "You answer science multiple-choice questions. "
        "Reply with the single letter of the best choice (A, B, C, or D). "
        "End with: Answer: <LETTER>"
    )
    results = []
    t0 = time.time()
    correct = 0
    for rank, idx in enumerate(indices):
        row = rows[idx]
        q = row["question"]
        stem = q["stem"]
        choices = q["choices"]
        choice_lines = "\n".join(f"{c['label']}. {c['text']}" for c in choices)
        prompt = f"{stem}\n\n{choice_lines}\n\nAnswer with one letter."
        out = generate(prompt, model=args.model, system=system, num_predict=32, num_ctx=2048, temperature=0.0)
        pred_text = out.get("response") or ""
        pred = extract_letter(pred_text)
        gold = row["answerKey"]
        ok = pred == gold
        correct += int(ok)
        results.append({
            "item_id": row["id"],
            "index": idx,
            "rank": rank,
            "gold": gold,
            "pred": pred,
            "correct": ok,
            "response": pred_text,
            "eval_count": out.get("eval_count"),
            "tok_s": out.get("_tok_s"),
            "wall_s": out.get("_wall_s"),
        })
        print(f"[{rank+1}/{args.n}] id={row['id']} ok={ok} gold={gold} pred={pred}", flush=True)

    summary = {
        "benchmark": "ARC-Challenge",
        "split": "test",
        "n": args.n,
        "seed": args.seed,
        "item_ids": [r["item_id"] for r in results],
        "indices": indices,
        "correct": correct,
        "accuracy": correct / args.n if args.n else None,
        "model": args.model,
        "wall_s_total": time.time() - t0,
        "grading": "exact letter match A-D extracted from model response",
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as f:
        json.dump({"summary": summary, "results": results}, f, indent=2)
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
