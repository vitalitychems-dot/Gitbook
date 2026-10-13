#!/usr/bin/env python3
"""Experiment 2: self-consistency / majority vote on small GSM8K subset."""
from __future__ import annotations
import argparse, json, re, random, time, sys, collections
from pathlib import Path
sys.path.insert(0, "/workspace/knowledge-lab/scripts")
from ollama_client_seeded import generate, DEFAULT_MODEL

ANS_RE = re.compile(r"####\s*(-?[\d,\.]+)")
NUM_RE = re.compile(r"-?[\d,\.]+")

def extract_gold(answer: str) -> str:
    m = ANS_RE.search(answer)
    if m:
        return m.group(1).replace(",", "")
    nums = NUM_RE.findall(answer.replace(",", ""))
    return nums[-1] if nums else ""

def extract_pred(text: str) -> str:
    m = ANS_RE.search(text)
    if m:
        return m.group(1).replace(",", "")
    m2 = re.search(r"(?:final answer|answer)\s*[:=]\s*(-?[\d,\.]+)", text, re.I)
    if m2:
        return m2.group(1).replace(",", "")
    nums = NUM_RE.findall(text.replace(",", ""))
    return nums[-1] if nums else ""

def majority_vote(preds: list[str]) -> str:
    preds = [p for p in preds if p != ""]
    if not preds:
        return ""
    counts = collections.Counter(preds)
    best = max(counts.values())
    for p in preds:
        if counts[p] == best:
            return p
    return preds[0]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-items", type=int, default=10)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--ns", default="1,3,5")
    ap.add_argument("--data", default="/workspace/evals/data/gsm8k_test.jsonl")
    ap.add_argument("--out", default="/workspace/knowledge-lab/results/exp2_self_consistency.json")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--temperature", type=float, default=0.7)
    args = ap.parse_args()
    ns = [int(x) for x in args.ns.split(",")]

    rows = [json.loads(l) for l in open(args.data) if l.strip()]
    rng = random.Random(args.seed)
    indices = list(range(len(rows)))
    rng.shuffle(indices)
    indices = indices[: args.n_items]

    system = (
        "You are a careful math tutor. Solve the grade-school word problem. "
        "Show brief reasoning. End with a line exactly like: #### <number>"
    )

    max_n = max(ns)
    per_item = []
    t_all = time.time()
    total_calls = 0

    for rank, idx in enumerate(indices):
        row = rows[idx]
        gold = extract_gold(row["answer"])
        prompt = row["question"].strip() + "\n\nWrite #### <final numeric answer> on the last line."
        samples = []
        for s in range(max_n):
            out = generate(
                prompt, model=args.model, system=system,
                num_predict=128, num_ctx=2048, temperature=args.temperature,
                seed=args.seed + rank * 100 + s * 17,
            )
            pred_text = out.get("response") or ""
            pred = extract_pred(pred_text)
            samples.append({
                "sample_i": s,
                "pred": pred,
                "response": pred_text[:500],
                "wall_s": out.get("_wall_s"),
                "eval_count": out.get("eval_count"),
                "tok_s": out.get("_tok_s"),
                "seed": args.seed + rank * 100 + s * 17,
            })
            total_calls += 1
            print(f"[item {rank+1}/{args.n_items} sample {s+1}/{max_n}] idx={idx} pred={pred} gold={gold} wall={out.get('_wall_s'):.1f}s", flush=True)

        item_rec = {"index": idx, "gold": gold, "question": row["question"][:200], "samples": samples, "by_n": {}}
        for n in ns:
            preds = [samples[i]["pred"] for i in range(n)]
            voted = majority_vote(preds)
            try:
                ok = abs(float(voted) - float(gold)) < 1e-6
            except Exception:
                ok = voted == gold
            agree = sum(1 for p in preds if p == voted) / n if n else 0
            item_rec["by_n"][str(n)] = {
                "voted": voted,
                "correct": ok,
                "preds": preds,
                "agreement": agree,
                "wall_s_sum": sum(samples[i]["wall_s"] or 0 for i in range(n)),
            }
        per_item.append(item_rec)

    summary_by_n = {}
    for n in ns:
        correct = sum(1 for it in per_item if it["by_n"][str(n)]["correct"])
        wall = sum(it["by_n"][str(n)]["wall_s_sum"] for it in per_item)
        summary_by_n[str(n)] = {
            "N_samples": n,
            "n_items": args.n_items,
            "correct": correct,
            "accuracy": correct / args.n_items if args.n_items else None,
            "wall_s_total": wall,
            "mean_wall_s_per_item": wall / args.n_items if args.n_items else None,
        }
    base_wall = summary_by_n.get("1", {}).get("wall_s_total")
    for n in ns:
        if base_wall:
            summary_by_n[str(n)]["relative_cost_vs_N1"] = summary_by_n[str(n)]["wall_s_total"] / base_wall

    out = {
        "experiment": "self_consistency_majority_vote",
        "claim_label": "TESTED",
        "honest_framing": (
            "This is the honest version of 'multiplying agents to sway odds': "
            "self-consistency / majority vote over stochastic samples (Wang et al., arXiv:2203.11171). "
            "It can improve accuracy on some tasks when the model is noisy, at roughly linear compute cost. "
            "It does not grant agency, consciousness, or the ability to change physical odds outside the model."
        ),
        "model": args.model,
        "temperature": args.temperature,
        "seed_items": args.seed,
        "indices": indices,
        "summary_by_n": summary_by_n,
        "total_generate_calls": total_calls,
        "wall_s_all": time.time() - t_all,
        "items": per_item,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({"summary_by_n": summary_by_n, "wall_s_all": out["wall_s_all"]}, indent=2))

if __name__ == "__main__":
    main()
