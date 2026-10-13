"""Per-query metrics and aggregations for the rigorous harness."""
from __future__ import annotations
import os
import re
import time
from typing import Callable, Iterable

import numpy as np

from leak import filter_hits
from stats import bootstrap_ci, percentile

NUM = r"\b\d+(?:\.\d+)?%?"
TOK = re.compile(r"[a-z0-9]+", re.I)


def tok(s: str):
    return TOK.findall((s or "").lower())


def token_count(s: str) -> int:
    """Same proxy as allsee/rounds.py and qinvent: len//4."""
    return max(1, len(s or "") // 4) if s else 0


def extract_answer(q: str, hits) -> str | None:
    """Extractive number answerer (matches qinvent/round3 harness)."""
    best = None
    qt = set(tok(q))
    for rank, h in enumerate(hits):
        body = h.get("body", "") if isinstance(h, dict) else str(h)
        for s in re.split(r"(?<=[.!?])\s+|\n", body):
            ov = len(qt & set(tok(s))) / max(1, len(qt))
            for n in re.findall(NUM, s):
                score = ov / (1 + rank)
                if best is None or score > best[0]:
                    best = (score, n)
    return best[1] if best else None


def hit_at_k(x, hits, k: int) -> bool:
    """True if gold file appears in top-k (path or aliases)."""
    for h in hits[:k]:
        if not isinstance(h, dict):
            continue
        if x["file"] == h.get("path") or x["file"] in h.get("aliases", []):
            return True
    return False


def brief_tokens(hits) -> int:
    return sum(token_count(h.get("body", "") if isinstance(h, dict) else str(h)) for h in hits)


def brief_bytes(hits) -> int:
    return sum(len((h.get("body", "") if isinstance(h, dict) else str(h)).encode("utf-8", "replace")) for h in hits)


def dir_bytes(path: str) -> int:
    if not path or not os.path.exists(path):
        return 0
    total = 0
    if os.path.isfile(path):
        return os.path.getsize(path)
    for root, _ds, fs in os.walk(path):
        for f in fs:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total


def evaluate_system(
    system: Callable,
    qa: list,
    k: int = 5,
    timing_repeats: int = 5,
    n_boot: int = 1000,
    artifact_path: str | None = None,
):
    """Run system on each query. system(q) -> list[hit-dict].

    Timing: for each query, run `timing_repeats` times; take mean latency.
    Leak filter applied to every hit list.
    Returns per-query arrays + aggregate metrics with bootstrap CIs.
    """
    n = len(qa)
    hit1 = np.zeros(n, dtype=bool)
    hit5 = np.zeros(n, dtype=bool)
    correct = np.zeros(n, dtype=bool)
    tokens = np.zeros(n, dtype=float)
    bytes_ = np.zeros(n, dtype=float)
    lat_ms = np.zeros(n, dtype=float)
    # Warm once so first-query cold start doesn't dominate
    if qa:
        try:
            system(qa[0]["q"])
        except Exception:
            pass

    for i, x in enumerate(qa):
        times = []
        hits = None
        for _ in range(max(1, timing_repeats)):
            t0 = time.perf_counter()
            hits = filter_hits(system(x["q"]) or [])
            times.append((time.perf_counter() - t0) * 1000.0)
        lat_ms[i] = float(np.mean(times))
        hit1[i] = hit_at_k(x, hits, 1)
        hit5[i] = hit_at_k(x, hits, k)
        ans = extract_answer(x["q"], hits[:k])
        correct[i] = ans == x["a"]
        tokens[i] = brief_tokens(hits[:k])
        bytes_[i] = brief_bytes(hits[:k])

    disk = float(bytes_.sum())
    if artifact_path:
        disk += dir_bytes(artifact_path)

    def agg(arr, higher_better=True, as_rate=False):
        point, lo, hi = bootstrap_ci(arr, n_boot=n_boot, statistic=np.mean)
        return dict(
            value=point,
            lo=lo,
            hi=hi,
            higher_better=higher_better,
            n=int(len(arr)),
        )

    # Latency percentiles across queries (of per-query mean latencies)
    p50, p50_lo, p50_hi = bootstrap_ci(lat_ms, n_boot=n_boot, statistic=lambda a, axis=None: np.percentile(a, 50, axis=axis))
    p95, p95_lo, p95_hi = bootstrap_ci(lat_ms, n_boot=n_boot, statistic=lambda a, axis=None: np.percentile(a, 95, axis=axis))

    metrics = {
        "hit@1": agg(hit1.astype(float), higher_better=True),
        "hit@5": agg(hit5.astype(float), higher_better=True),
        "accuracy": agg(correct.astype(float), higher_better=True),
        "tokens/query": agg(tokens, higher_better=False),
        "latency_p50_ms": dict(value=p50, lo=p50_lo, hi=p50_hi, higher_better=False, n=n),
        "latency_p95_ms": dict(value=p95, lo=p95_lo, hi=p95_hi, higher_better=False, n=n),
        "disk_bytes": dict(
            value=disk,
            lo=disk,  # deterministic for a given run (no resample of file sizes)
            hi=disk,
            higher_better=False,
            n=1,
            note="sum of brief UTF-8 bytes (+ artifact dir if set); CI degenerate",
        ),
    }
    per_query = dict(
        hit1=hit1,
        hit5=hit5,
        correct=correct,
        tokens=tokens,
        bytes=bytes_,
        lat_ms=lat_ms,
    )
    return dict(metrics=metrics, per_query=per_query, n=n, timing_repeats=timing_repeats, n_boot=n_boot)
