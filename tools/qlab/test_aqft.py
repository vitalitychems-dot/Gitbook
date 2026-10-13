"""Pytest invariants for aqft.py (replaces the assertion-free n=3..10 sweep).

The old script only printed and wrote aqft_results.json, so a crash-free run
was a pass. These tests check normalization and unitarity, monotone ideal
fidelity and gate counts, fixed-seed determinism, and examples/aqft5.json.
Numbers are locked to tools/qlab/baselines/aqft.json.
"""
import json, os, sys
import numpy as np
import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from baselines.measure_aqft import (
    AQFT5, ideal_fidelities, ideal_sweep, serialize, spec_aqft, unitarity_report,
)
from qsim import SV, qft
from qopt2 import lower
from aqft import aqft, inverse

BASELINE = os.path.join(HERE, 'baselines', 'aqft.json')
# RESULTS.md §7, seed-5 8-input ideal sweep (printed digits). Not recomputed from a new sample.
PUBLISHED_IDEAL_MEAN = {(4, 3): 0.990485, (5, 3): 0.959550, (6, 3): 0.906327}
PUBLISHED_IDEAL_MIN = {(5, 1): 0.000027}
# RESULTS.md §7 "2q best/exact" and the aqft5 lowering (n=5, m=4 → 24).
PUBLISHED_TWOQ = {(3, 3): 9, (4, 3): 16, (4, 4): 18, (5, 3): 20, (5, 4): 24, (5, 5): 26, (6, 3): 27, (6, 6): 39}


def load_baseline():
    with open(BASELINE) as f:
        return json.load(f)


def test_normalization_and_unitarity():
    """Every AQFT is unitary: U†U = I, states stay normalized, inverse returns |x>, and m=n is the QFT."""
    report = unitarity_report(n_max=4)
    tol = 1e-9
    assert report['max_abs_UtU_minus_I'] < tol
    assert report['max_norm_err'] < tol
    assert report['max_roundtrip_err'] < tol
    assert report['max_aqft_n_minus_qft'] < tol
    base = load_baseline()['unitarity']
    # Recorded errors are numerical noise. A broken circuit jumps by many orders.
    assert report['max_abs_UtU_minus_I'] <= max(base['max_abs_UtU_minus_I'] * 100, 1e-12)
    assert report['max_roundtrip_err'] <= max(base['max_roundtrip_err'] * 100, 1e-12)
    for n in range(2, 6):
        for m in range(1, n + 1):
            for x0 in (0, 2**n - 1):
                s = SV(n)
                s.v[:] = 0
                s.v[x0] = 1
                probs = s.run(aqft(n, m)).probs()
                assert abs(float(probs.sum()) - 1) < 1e-9
                assert abs(float(np.linalg.norm(s.v)) - 1) < 1e-9
            back = SV(n)
            back.v[:] = 0
            back.v[1] = 1
            back.run(aqft(n, m)).run(inverse(aqft(n, m)))
            phase = np.angle(back.v[1])
            restored = back.v * np.exp(-1j * phase)
            assert abs(float(np.linalg.norm(back.v)) - 1) < 1e-9
            assert abs(restored[1] - 1) < 1e-9
            assert float(np.max(np.abs(np.delete(restored, 1)))) < 1e-9


def test_ideal_fidelity_monotonic_and_bounded():
    """Ideal fidelity vs exact QFT lies in [0, 1], is non-decreasing in m, and is 1 at m=n.

    Checked on every computational-basis input for n=2..5, and on the seed-5
    sample whose means are the RESULTS.md §7 figures.
    """
    for n in range(2, 6):
        prev = None
        for m in range(1, n + 1):
            f = np.array(ideal_fidelities(n, m, range(2**n)))
            assert np.all(f >= -1e-12) and np.all(f <= 1 + 1e-12)
            if prev is not None:
                assert np.all(f + 1e-9 >= prev)
            prev = f
        assert float(prev.min()) > 1 - 1e-9

    sweep = ideal_sweep()
    base = load_baseline()['ideal_seed5']
    for n_s, block in sweep.items():
        assert block['inputs'] == base[n_s]['inputs']
        prev_mean = -1.0
        prev_f = None
        for row, brow in zip(block['by_m'], base[n_s]['by_m']):
            assert row['m'] == brow['m']
            assert 0 <= row['min'] <= row['mean'] <= 1
            assert row['mean'] + 1e-12 >= prev_mean
            if prev_f is not None:
                assert all(a + 1e-12 >= b for a, b in zip(row['fidelities'], prev_f))
            prev_mean = row['mean']
            prev_f = row['fidelities']
            assert row['fidelities'] == pytest.approx(brow['fidelities'], abs=1e-12)
            assert row['mean'] == pytest.approx(brow['mean'], abs=1e-12)
            assert row['min'] == pytest.approx(brow['min'], abs=1e-12)
        assert block['by_m'][-1]['mean'] == pytest.approx(1.0, abs=1e-9)
        n = int(n_s)
        for (nn, m), published in PUBLISHED_IDEAL_MEAN.items():
            if nn == n:
                got = next(r['mean'] for r in block['by_m'] if r['m'] == m)
                assert round(got, 6) == published
        for (nn, m), published in PUBLISHED_IDEAL_MIN.items():
            if nn == n:
                got = next(r['min'] for r in block['by_m'] if r['m'] == m)
                assert round(got, 6) == published


def test_gate_counts_monotone_and_bounded_by_qft():
    """Raising m only adds controlled-phase gates. m>=n is exactly qft(n). Counts match the baseline and RESULTS.md."""
    sweep = ideal_sweep()
    base = load_baseline()['ideal_seed5']
    for n in range(1, 11):
        prev_gates = prev_cp = prev_twoq = -1
        exact = qft(n)
        for m in range(1, n + 1):
            c = aqft(n, m)
            assert c == spec_aqft(n, m)
            assert _subsequence(c, exact)
            assert len(c) <= len(exact)
            assert len(c) >= prev_gates
            assert sum(g[0] == 'CP' for g in c) >= prev_cp
            tq = sum(len(g[1]) == 2 for g in lower(c))
            assert tq >= prev_twoq
            assert tq <= sum(len(g[1]) == 2 for g in lower(exact))
            prev_gates = len(c)
            prev_cp = sum(g[0] == 'CP' for g in c)
            prev_twoq = tq
        assert aqft(n, n) == exact
        assert aqft(n, n + 2) == exact
        if n >= 3:
            assert sum(g[0] == 'CP' for g in aqft(n, 1)) < sum(g[0] == 'CP' for g in exact)
    for n_s, block in sweep.items():
        for row, brow in zip(block['by_m'], base[n_s]['by_m']):
            assert (row['gates'], row['cp'], row['twoq']) == (brow['gates'], brow['cp'], brow['twoq'])
            key = (int(n_s), row['m'])
            if key in PUBLISHED_TWOQ:
                assert row['twoq'] == PUBLISHED_TWOQ[key]


def test_deterministic_with_fixed_seed():
    """The same seed and the same (n, m) rebuild the same circuit and the same fidelities."""
    first = ideal_sweep()
    second = ideal_sweep()
    assert first.keys() == second.keys()
    for n_s in first:
        assert first[n_s]['inputs'] == second[n_s]['inputs']
        for a, b in zip(first[n_s]['by_m'], second[n_s]['by_m']):
            assert a['fidelities'] == b['fidelities']
            assert a['gates'] == b['gates']
    for n in range(3, 9):
        for m in range(1, n + 1):
            assert serialize(aqft(n, m)) == serialize(aqft(n, m))
            assert aqft(n, m) == spec_aqft(n, m)
    # Statevector itself, not only the fidelity scalar.
    for _ in range(2):
        s = SV(5)
        s.v[:] = 0
        s.v[7] = 1
        s.run(aqft(5, 3))
        if _ == 0:
            saved = s.v.copy()
        else:
            assert np.array_equal(saved, s.v)


def test_matches_aqft5_reference():
    """examples/aqft5.json is the macro AQFT[5, 4] and expands to the drop-rule circuit."""
    with open(AQFT5) as f:
        doc = json.load(f)
    assert doc == {'n': 5, 'gates': [['AQFT', [5, 4]]]}
    c = aqft(5, 4)
    assert c == spec_aqft(5, 4)
    base = load_baseline()['aqft5']
    assert doc == base['document']
    assert serialize(c) == base['circuit']
    assert len(c) == base['gates'] == 16
    assert sum(g[0] == 'CP' for g in c) == base['cp'] == 9
    thr = 2 * np.pi / 2**4 - 1e-15
    assert all(g[2] >= thr for g in c if g[0] == 'CP')
    # Angles the full QFT would have used, and that m=4 must drop.
    dropped = [g for g in qft(5) if g[0] == 'CP' and g[2] < thr]
    assert dropped and all(g not in c for g in dropped)
    zero = ideal_fidelities(5, 4, [0])[0]
    assert zero == pytest.approx(base['zero_fidelity'], abs=1e-12)
    assert zero > 1 - 1e-9
    seed5 = next(r for r in load_baseline()['ideal_seed5']['5']['by_m'] if r['m'] == 4)
    again = ideal_fidelities(5, 4, load_baseline()['ideal_seed5']['5']['inputs'])
    assert float(np.mean(again)) == pytest.approx(base['seed5_mean'], abs=1e-12)
    assert float(np.min(again)) == pytest.approx(base['seed5_min'], abs=1e-12)
    assert float(np.mean(again)) == pytest.approx(seed5['mean'], abs=1e-12)


def _subsequence(small, big):
    i = 0
    for g in big:
        if i < len(small) and g == small[i]:
            i += 1
    return i == len(small)


if __name__ == '__main__':
    raise SystemExit(pytest.main([__file__, '-q', '--tb=short', '-p', 'no:cacheprovider']))
