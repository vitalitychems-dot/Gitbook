#!/usr/bin/env python3
"""Rigorous held-out bench harness for Tessera inventions.

  python3 bench.py run --baseline raw --candidate stack25
  python3 bench.py run --baseline path.py:fn --candidate path.py:fn
  python3 bench.py freeze --system raw          # write baseline.json regression guard
  python3 bench.py check                       # compare last result to baseline.json

Rules (Father 2026-10-13):
  - Fixed held-out TEST from cycles/c1/qa_set.json (split=='test').
  - Leak guard: qa_set / cycles / fraction / bench paths excluded from hits.
  - Keep only if candidate improves ≥1 metric AND no significant regression on any other
    (BH-corrected α=0.05). Priority order for reporting: tokens → speed → accuracy.
"""
from __future__ import annotations
import argparse
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from leak import LEAK_PATTERNS  # noqa: E402
from metrics import evaluate_system  # noqa: E402
from stats import (  # noqa: E402
    benjamini_hochberg,
    bootstrap_paired_diff,
    mcnemar,
    wilcoxon_signed_rank,
)
from systems import BUILTINS, clear_cache, load_system  # noqa: E402

QA_PATH = "/workspace/rick/cycles/c1/qa_set.json"
BASELINE_JSON = os.path.join(HERE, "baseline.json")
LAST_JSON = os.path.join(HERE, "last_result.json")

# Metric families for paired tests
BINARY_METRICS = {
    "hit@1": "hit1",
    "hit@5": "hit5",
    "accuracy": "correct",
}
CONTINUOUS_METRICS = {
    "tokens/query": ("tokens", False),   # (per_query key, higher_better)
    # latency compared on per-query mean ms
    "latency_mean_ms": ("lat_ms", False),
}


def load_test(qa_path=QA_PATH):
    qa = json.load(open(qa_path))
    test = [x for x in qa if x.get("split") == "test"]
    if not test:
        raise SystemExit(f"No split=='test' rows in {qa_path}")
    return test


def compare(base_eval, cand_eval, n_boot=1000, alpha=0.05):
    """Paired significance across metrics; BH correction; KEEP/DROP decision."""
    bp, cp = base_eval["per_query"], cand_eval["per_query"]
    comparisons = []

    # Binary: McNemar + paired bootstrap on rates
    for mname, key in BINARY_METRICS.items():
        mc = mcnemar(bp[key], cp[key])
        boot = bootstrap_paired_diff(bp[key].astype(float), cp[key].astype(float),
                                     n_boot=n_boot, higher_better=True)
        base_v = base_eval["metrics"][mname]["value"]
        cand_v = cand_eval["metrics"][mname]["value"]
        comparisons.append(dict(
            metric=mname,
            higher_better=True,
            baseline=base_v,
            candidate=cand_v,
            delta=cand_v - base_v,
            delta_ci=(boot["lo"], boot["hi"]),
            p_raw=mc["p"],
            test="mcnemar",
            detail=mc,
        ))

    # Continuous: Wilcoxon + paired bootstrap
    for mname, (key, hb) in CONTINUOUS_METRICS.items():
        wx = wilcoxon_signed_rank(bp[key], cp[key], higher_better=hb)
        boot = bootstrap_paired_diff(bp[key], cp[key], n_boot=n_boot, higher_better=hb)
        base_v = float(np.mean(bp[key]))
        cand_v = float(np.mean(cp[key]))
        delta = (cand_v - base_v) if hb else (base_v - cand_v)  # + => cand better
        comparisons.append(dict(
            metric=mname,
            higher_better=hb,
            baseline=base_v,
            candidate=cand_v,
            delta=delta,
            delta_ci=(boot["lo"], boot["hi"]),
            p_raw=wx["p"],
            test="wilcoxon",
            detail=wx,
        ))

    # Latency percentiles: compare via bootstrap on the per-query lat arrays' percentile delta
    for pname, pct in (("latency_p50_ms", 50), ("latency_p95_ms", 95)):
        base_v = base_eval["metrics"][pname]["value"]
        cand_v = cand_eval["metrics"][pname]["value"]
        # paired bootstrap of percentile difference (lower better)
        rng = np.random.default_rng(7)
        n = len(bp["lat_ms"])
        idx = rng.integers(0, n, size=(n_boot, n))
        samples = np.percentile(bp["lat_ms"][idx], pct, axis=1) - np.percentile(cp["lat_ms"][idx], pct, axis=1)
        lo, hi = np.quantile(samples, [0.025, 0.975])
        p_lo = (samples <= 0).mean()
        p_hi = (samples >= 0).mean()
        p = float(min(1.0, 2 * min(p_lo, p_hi)))
        comparisons.append(dict(
            metric=pname,
            higher_better=False,
            baseline=base_v,
            candidate=cand_v,
            delta=base_v - cand_v,  # + => cand faster
            delta_ci=(float(lo), float(hi)),
            p_raw=p,
            test="bootstrap_percentile",
            detail={},
        ))

    # Disk bytes: deterministic; treat as regression if cand > base * 1.0 and relative increase > 1%
    bd = base_eval["metrics"]["disk_bytes"]["value"]
    cd = cand_eval["metrics"]["disk_bytes"]["value"]
    disk_delta = bd - cd  # + => cand smaller
    # No paired test; use a simple relative threshold as "significant" if |rel| > 1%
    disk_p = 0.0 if abs(disk_delta) / max(bd, 1) > 0.01 else 1.0
    comparisons.append(dict(
        metric="disk_bytes",
        higher_better=False,
        baseline=bd,
        candidate=cd,
        delta=disk_delta,
        delta_ci=(disk_delta, disk_delta),
        p_raw=disk_p,
        test="relative_threshold_1pct",
        detail={"rel": (cd - bd) / max(bd, 1)},
    ))

    # BH correction
    pvals = [c["p_raw"] for c in comparisons]
    bh = benjamini_hochberg(pvals, alpha=alpha)
    for c, (reject, q) in zip(comparisons, bh):
        c["p_bh"] = q
        c["significant"] = bool(reject)
        # direction of point estimate
        c["improved"] = c["delta"] > 0
        c["regressed"] = c["delta"] < 0 and c["significant"]
        c["sig_improved"] = c["delta"] > 0 and c["significant"]

    sig_improvements = [c["metric"] for c in comparisons if c["sig_improved"]]
    point_improvements = [c["metric"] for c in comparisons if c["improved"]]
    regressions = [c["metric"] for c in comparisons if c["regressed"]]

    # KEEP rule: improve ≥1 metric (significant preferred; else any point improvement
    # with no significant regression). Father asked for true amounts with significance,
    # so require ≥1 significant improvement AND zero significant regressions.
    keep = bool(sig_improvements) and not regressions
    # Soft note if only point improvements (no sig)
    soft_keep = (not keep) and bool(point_improvements) and not regressions

    verdict = "KEPT" if keep else ("SOFT_KEEP_NS" if soft_keep else "DROPPED")
    return dict(
        comparisons=comparisons,
        sig_improvements=sig_improvements,
        point_improvements=point_improvements,
        regressions=regressions,
        verdict=verdict,
        alpha=alpha,
        n_boot=n_boot,
        rule="KEPT iff ≥1 BH-significant improvement and 0 BH-significant regressions",
    )


def regression_guard(cand_metrics, baseline_path=BASELINE_JSON, alpha=0.05):
    """Fail if candidate is significantly worse than frozen baseline.json on any metric.
    Uses CI non-overlap / value comparison against stored point+CI.
    """
    if not os.path.exists(baseline_path):
        return dict(ok=True, note="no baseline.json yet; run `bench.py freeze` first")
    frozen = json.load(open(baseline_path))
    fm = frozen.get("metrics", {})
    problems = []
    for name, cm in cand_metrics.items():
        if name not in fm:
            continue
        fb = fm[name]
        hb = cm.get("higher_better", True)
        # Regression if candidate CI is entirely on the worse side of frozen point
        if hb:
            # cand worse if cand.hi < frozen.value (clearly below)
            if cm["hi"] < fb["value"] and cm["value"] < fb["value"]:
                # only flag if relative drop > 1%
                if (fb["value"] - cm["value"]) / max(abs(fb["value"]), 1e-9) > 0.01:
                    problems.append(dict(metric=name, frozen=fb["value"], candidate=cm["value"], dir="lower"))
        else:
            if cm["lo"] > fb["value"] and cm["value"] > fb["value"]:
                if (cm["value"] - fb["value"]) / max(abs(fb["value"]), 1e-9) > 0.01:
                    problems.append(dict(metric=name, frozen=fb["value"], candidate=cm["value"], dir="higher"))
    return dict(ok=not problems, problems=problems, frozen_system=frozen.get("system"), frozen_at=frozen.get("ts"))


def fmt_ci(m):
    return f"{m['value']:.4g} [{m['lo']:.4g}, {m['hi']:.4g}]"


def print_report(base_name, cand_name, base_eval, cand_eval, decision, guard):
    print("=" * 72)
    print(f"BENCH  baseline={base_name}  candidate={cand_name}")
    print(f"TEST n={base_eval['n']}  timing_repeats={base_eval['timing_repeats']}  "
          f"n_boot={base_eval['n_boot']}  leak={LEAK_PATTERNS}")
    print("=" * 72)
    print(f"{'metric':<18} {'baseline':>28} {'candidate':>28}")
    for name in base_eval["metrics"]:
        print(f"{name:<18} {fmt_ci(base_eval['metrics'][name]):>28} {fmt_ci(cand_eval['metrics'][name]):>28}")
    print("-" * 72)
    print(f"{'metric':<18} {'Δ (cand better+)':>16} {'Δ 95% CI':>24} {'p_raw':>10} {'p_BH':>10} {'sig':>5}")
    for c in decision["comparisons"]:
        lo, hi = c["delta_ci"]
        flag = ""
        if c["sig_improved"]:
            flag = "WIN"
        elif c["regressed"]:
            flag = "REG"
        elif c["significant"]:
            flag = "SIG"
        print(f"{c['metric']:<18} {c['delta']:+16.4g} [{lo:+.4g}, {hi:+.4g}]{'':>2} "
              f"{c['p_raw']:10.4g} {c['p_bh']:10.4g} {flag:>5}")
    print("-" * 72)
    print(f"sig_improvements: {decision['sig_improvements']}")
    print(f"regressions:      {decision['regressions']}")
    print(f"VERDICT: {decision['verdict']}  ({decision['rule']})")
    if not guard.get("ok", True):
        print(f"REGRESSION GUARD FAIL vs baseline.json: {guard['problems']}")
    else:
        print(f"regression guard: OK ({guard.get('note') or 'no problems vs '+str(guard.get('frozen_system'))})")
    print("=" * 72)


def cmd_run(args):
    test = load_test(args.qa)
    clear_cache()
    base_fn = load_system(args.baseline)
    cand_fn = load_system(args.candidate)
    print(f"Evaluating baseline={args.baseline} on n={len(test)} …", flush=True)
    t0 = time.time()
    base_eval = evaluate_system(base_fn, test, k=args.k, timing_repeats=args.repeats, n_boot=args.n_boot)
    print(f"  baseline done in {time.time()-t0:.1f}s", flush=True)
    print(f"Evaluating candidate={args.candidate} …", flush=True)
    t1 = time.time()
    cand_eval = evaluate_system(cand_fn, test, k=args.k, timing_repeats=args.repeats, n_boot=args.n_boot)
    print(f"  candidate done in {time.time()-t1:.1f}s", flush=True)

    decision = compare(base_eval, cand_eval, n_boot=args.n_boot, alpha=args.alpha)
    guard = regression_guard(cand_eval["metrics"], BASELINE_JSON)

    # If regression guard fails, force DROP
    if not guard.get("ok", True):
        decision["verdict"] = "DROPPED"
        decision["regressions"] = list(decision["regressions"]) + [
            f"guard:{p['metric']}" for p in guard.get("problems", [])
        ]

    print_report(args.baseline, args.candidate, base_eval, cand_eval, decision, guard)

    # Serialize (convert numpy)
    def ser_eval(e):
        return dict(
            n=e["n"],
            timing_repeats=e["timing_repeats"],
            n_boot=e["n_boot"],
            metrics=e["metrics"],
            # store per-query as lists for re-analysis
            per_query={k: (v.tolist() if hasattr(v, "tolist") else v) for k, v in e["per_query"].items()},
        )

    out = dict(
        ts=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        baseline=args.baseline,
        candidate=args.candidate,
        qa=args.qa,
        k=args.k,
        leak=list(LEAK_PATTERNS),
        baseline_eval=ser_eval(base_eval),
        candidate_eval=ser_eval(cand_eval),
        decision=decision,
        regression_guard=guard,
    )
    # Make decision JSON-safe (detail may have numpy)
    for c in out["decision"]["comparisons"]:
        c["delta_ci"] = list(c["delta_ci"])
        if "detail" in c:
            c["detail"] = {kk: (float(vv) if hasattr(vv, "item") else vv) for kk, vv in c["detail"].items()}

    with open(LAST_JSON, "w") as f:
        json.dump(out, f, indent=1)
    if args.out:
        with open(args.out, "w") as f:
            json.dump(out, f, indent=1)
        print(f"wrote {args.out}")
    print(f"wrote {LAST_JSON}")
    return 0 if decision["verdict"] == "KEPT" else 1


def cmd_freeze(args):
    """Run a system and freeze its metrics as the regression baseline."""
    test = load_test(args.qa)
    clear_cache()
    fn = load_system(args.system)
    ev = evaluate_system(fn, test, k=args.k, timing_repeats=args.repeats, n_boot=args.n_boot)
    payload = dict(
        ts=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        system=args.system,
        qa=args.qa,
        k=args.k,
        n=ev["n"],
        timing_repeats=ev["timing_repeats"],
        n_boot=ev["n_boot"],
        leak=list(LEAK_PATTERNS),
        metrics=ev["metrics"],
        note="Regression guard reference. Candidates must not significantly regress vs these values.",
    )
    with open(BASELINE_JSON, "w") as f:
        json.dump(payload, f, indent=1)
    print(f"Froze baseline.json from system={args.system} n={ev['n']}")
    for name, m in ev["metrics"].items():
        print(f"  {name}: {fmt_ci(m)}")
    return 0


def cmd_check(args):
    if not os.path.exists(LAST_JSON):
        print("No last_result.json; run `bench.py run` first")
        return 2
    last = json.load(open(LAST_JSON))
    guard = regression_guard(last["candidate_eval"]["metrics"], BASELINE_JSON)
    print(json.dumps(guard, indent=1))
    return 0 if guard.get("ok") else 1


def main(argv=None):
    p = argparse.ArgumentParser(description="Rigorous Tessera invention bench")
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="Compare baseline vs candidate; KEEP/DROP")
    r.add_argument("--baseline", required=True, help=f"builtin {list(BUILTINS)} or path.py:fn")
    r.add_argument("--candidate", required=True, help=f"builtin {list(BUILTINS)} or path.py:fn")
    r.add_argument("--qa", default=QA_PATH)
    r.add_argument("--k", type=int, default=5)
    r.add_argument("--repeats", type=int, default=5, help="timing repeats per query")
    r.add_argument("--n-boot", type=int, default=1000, dest="n_boot")
    r.add_argument("--alpha", type=float, default=0.05)
    r.add_argument("--out", default="", help="optional extra JSON path")
    r.set_defaults(func=cmd_run)

    f = sub.add_parser("freeze", help="Freeze a system as baseline.json regression guard")
    f.add_argument("--system", default="raw")
    f.add_argument("--qa", default=QA_PATH)
    f.add_argument("--k", type=int, default=5)
    f.add_argument("--repeats", type=int, default=3)
    f.add_argument("--n-boot", type=int, default=1000, dest="n_boot")
    f.set_defaults(func=cmd_freeze)

    c = sub.add_parser("check", help="Re-check last_result.json against baseline.json")
    c.set_defaults(func=cmd_check)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
