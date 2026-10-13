#!/usr/bin/env python3
"""Small tests for collatz_max_stopping.py — known values, not a proof.
Famous: starting at 27 takes 111 steps to reach 1.
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from collatz_max_stopping import max_stopping_time


def stopping_time(n: int) -> int:
    """Direct count of steps to 1 (no cache), for oracle checks."""
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


def test_stopping_time_1():
    assert stopping_time(1) == 0
    r = max_stopping_time(1)
    assert r["max_stopping_time"] == 0
    assert r["argmax_start"] == 1


def test_stopping_time_27_is_111():
    # Well-known Collatz fact: 27 → … → 1 in 111 steps.
    assert stopping_time(27) == 111


def test_max_up_to_10():
    # Manual: 1:0, 2:1, 3:7, 4:2, 5:5, 6:8, 7:16, 8:3, 9:19, 10:6
    # max is 19 at start 9
    r = max_stopping_time(10)
    assert r["max_stopping_time"] == 19
    assert r["argmax_start"] == 9


def test_max_up_to_27_includes_111():
    r = max_stopping_time(27)
    assert r["max_stopping_time"] == 111
    assert r["argmax_start"] == 27


def test_max_up_to_100():
    # Cross-check: argmax should match brute force
    brute_max, brute_arg = 0, 1
    for s in range(1, 101):
        st = stopping_time(s)
        if st > brute_max:
            brute_max, brute_arg = st, s
    r = max_stopping_time(100)
    assert r["max_stopping_time"] == brute_max
    assert r["argmax_start"] == brute_arg


def main() -> int:
    tests = [
        test_stopping_time_1,
        test_stopping_time_27_is_111,
        test_max_up_to_10,
        test_max_up_to_27_includes_111,
        test_max_up_to_100,
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
