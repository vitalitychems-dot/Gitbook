#!/usr/bin/env python3
"""Small tests for goldbach_verify.py — known finite cases, not a proof."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from goldbach_verify import sieve, verify_goldbach


def test_sieve_small_primes():
    is_prime = sieve(30)
    expected = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
    got = {i for i, ok in enumerate(is_prime) if ok}
    assert got == expected, f"sieve(30) primes={got}"


def test_goldbach_small_evens():
    # Classic small checks: 4=2+2, 6=3+3, 8=3+5, 10=3+7=5+5, ...
    result = verify_goldbach(100)
    assert result["all_verified"] is True
    assert result["failures"] == []
    assert result["even_numbers_checked"] == 49  # 4,6,...,100


def test_goldbach_known_partition():
    is_prime = sieve(20)
    primes = [i for i, ok in enumerate(is_prime) if ok]
    prime_set = set(primes)
    n = 28
    assert any((n - p) in prime_set for p in primes if p <= n // 2)


def test_goldbach_limit_1000():
    result = verify_goldbach(1000)
    assert result["all_verified"] is True
    assert result["even_numbers_checked"] == 499


def main() -> int:
    tests = [
        test_sieve_small_primes,
        test_goldbach_small_evens,
        test_goldbach_known_partition,
        test_goldbach_limit_1000,
    ]
    passed = failed = 0
    for t in tests:
        try:
            t()
            print(f"PASS {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL {t.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"FAIL {t.__name__}: {type(e).__name__}: {e}")
            failed += 1
    print(f"SUMMARY passed={passed} failed={failed} total={len(tests)}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
