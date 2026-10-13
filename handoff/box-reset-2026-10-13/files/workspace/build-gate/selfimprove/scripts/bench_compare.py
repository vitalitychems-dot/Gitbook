#!/usr/bin/env python3
"""Compare bench results (JSON from scripts/bench-latency.mjs, any nested numeric 'p50' values).
--before / --after take one or more JSON files (5 runs each). Uses the median across runs of each
path's p50. Exit 1 if any path is >THRESHOLD (default 5%) slower. The caller reruns up to 3 times
before treating a failure as real."""
import argparse, json, statistics, sys

def p50s(obj, prefix=""):
    out = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "p50" and isinstance(v, (int, float)): out[prefix or "root"] = v
            else: out.update(p50s(v, f"{prefix}.{k}" if prefix else k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            key = v.get("name", str(i)) if isinstance(v, dict) else str(i)
            out.update(p50s(v, f"{prefix}.{key}" if prefix else key))
    return out

def medians(files):
    runs = [p50s(json.load(open(f))) for f in files]
    keys = set().union(*runs) if runs else set()
    return {k: statistics.median([r[k] for r in runs if k in r]) for k in keys}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--before", nargs="+", required=True); ap.add_argument("--after", nargs="+", required=True)
    ap.add_argument("--threshold", type=float, default=0.05); ap.add_argument("--summary")
    a = ap.parse_args()
    b, f = medians(a.before), medians(a.after)
    rows, bad = ["| path | p50 before (ms) | p50 after (ms) | change |", "|---|---|---|---|"], []
    for k in sorted(set(b) & set(f)):
        ch = (f[k] - b[k]) / b[k] if b[k] else 0.0
        if ch > a.threshold: bad.append(k)
        rows.append(f"| {k} | {b[k]:.3f} | {f[k]:.3f} | {ch:+.1%}{' ❌' if ch > a.threshold else ''} |")
    rep = "### Bench (median of runs)\n" + "\n".join(rows) + "\n"
    print(rep)
    if a.summary: open(a.summary, "a").write(rep)
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
