#!/usr/bin/env python3
"""Find the maximum Collatz stopping time for starting values in [1, LIMIT].
Stopping time = number of steps to reach 1 under n -> n/2 (even) or 3n+1 (odd).
Uses memoization. Stdlib only.
"""
from __future__ import annotations
import argparse
import time
from pathlib import Path


def max_stopping_time(limit: int) -> dict:
    t0 = time.perf_counter()
    # cache[n] = stopping time of n (steps to 1). cache[1] = 0
    cache: dict[int, int] = {1: 0}
    max_steps = 0
    argmax = 1

    for start in range(1, limit + 1):
        n = start
        path: list[int] = []
        while n not in cache:
            path.append(n)
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        # n is now in cache; backfill path
        steps_from_known = cache[n]
        for i, v in enumerate(reversed(path)):
            cache[v] = steps_from_known + i + 1
        steps = cache[start]
        if steps > max_steps:
            max_steps = steps
            argmax = start

    elapsed = time.perf_counter() - t0
    return {
        "limit": limit,
        "max_stopping_time": max_steps,
        "argmax_start": argmax,
        "cache_size": len(cache),
        "total_seconds": round(elapsed, 4),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=1_000_000)
    ap.add_argument(
        "--log",
        type=Path,
        default=Path(__file__).resolve().parent / "collatz_max_stopping.log",
    )
    args = ap.parse_args()

    result = max_stopping_time(args.limit)
    lines = [
        "Collatz maximum stopping time",
        f"limit={result['limit']}",
        f"max_stopping_time={result['max_stopping_time']}",
        f"argmax_start={result['argmax_start']}",
        f"cache_size={result['cache_size']}",
        f"total_seconds={result['total_seconds']}",
        "NOTE: finite search is not a proof of the Collatz conjecture.",
    ]
    text = "\n".join(lines) + "\n"
    print(text, end="")
    args.log.write_text(text)
    print(f"Wrote log: {args.log}")


if __name__ == "__main__":
    main()
