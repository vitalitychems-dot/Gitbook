#!/usr/bin/env python3
"""Verify Goldbach's conjecture for all even n in [4, LIMIT]:
each even n = p + q for primes p, q.
Uses a sieve of Eratosthenes. Stdlib only.
"""
from __future__ import annotations
import argparse
import time
from pathlib import Path


def sieve(limit: int) -> list[bool]:
    """is_prime[i] True iff i is prime. Length limit+1."""
    is_prime = [False, False] + [True] * (limit - 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            step = p
            start = p * p
            is_prime[start : limit + 1 : step] = [False] * (((limit - start) // step) + 1)
        p += 1
    return is_prime


def verify_goldbach(limit: int) -> dict:
    t0 = time.perf_counter()
    is_prime = sieve(limit)
    primes = [i for i, ok in enumerate(is_prime) if ok]
    prime_set = set(primes)
    t_sieve = time.perf_counter() - t0

    t1 = time.perf_counter()
    failures: list[int] = []
    checked = 0
    hardest = None  # (n, min_p) — even with largest smallest-prime partner
    max_min_p = 0
    for n in range(4, limit + 1, 2):
        checked += 1
        found = False
        min_p = None
        for p in primes:
            if p > n // 2:
                break
            if (n - p) in prime_set:
                found = True
                min_p = p
                break
        if not found:
            failures.append(n)
        elif min_p is not None and min_p >= max_min_p:
            max_min_p = min_p
            hardest = (n, min_p, n - min_p)
    t_check = time.perf_counter() - t1
    elapsed = time.perf_counter() - t0

    return {
        "limit": limit,
        "even_numbers_checked": checked,
        "failures": failures,
        "all_verified": len(failures) == 0,
        "prime_count_up_to_limit": len(primes),
        "hardest_example": hardest,
        "sieve_seconds": round(t_sieve, 4),
        "check_seconds": round(t_check, 4),
        "total_seconds": round(elapsed, 4),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=1_000_000)
    ap.add_argument(
        "--log",
        type=Path,
        default=Path(__file__).resolve().parent / "goldbach_verify.log",
    )
    args = ap.parse_args()

    result = verify_goldbach(args.limit)
    lines = [
        "Goldbach conjecture verification",
        f"limit={result['limit']}",
        f"even_numbers_checked={result['even_numbers_checked']}",
        f"all_verified={result['all_verified']}",
        f"failures={result['failures']}",
        f"prime_count_up_to_limit={result['prime_count_up_to_limit']}",
        f"hardest_example(n, min_p, n-min_p)={result['hardest_example']}",
        f"sieve_seconds={result['sieve_seconds']}",
        f"check_seconds={result['check_seconds']}",
        f"total_seconds={result['total_seconds']}",
        "NOTE: finite verification is not a proof.",
    ]
    text = "\n".join(lines) + "\n"
    print(text, end="")
    args.log.write_text(text)
    print(f"Wrote log: {args.log}")


if __name__ == "__main__":
    main()
