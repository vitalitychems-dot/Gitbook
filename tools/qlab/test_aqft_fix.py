"""Pytest invariants for the AQFT cleanup rerun (old test_aqft_fix.py).

The old script averaged phase-estimation success and noisy fidelity and
exited 0 even when the numbers were nonsense. These tests check probability
normalization, the ideal-vs-noisy ordering visible in RESULTS.md §7b, fixed
seeds, and the frozen baseline.
"""
import json, os, sys
import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from baselines.measure_aqft import noisy_sweep, phase_estimation, spec_aqft
from aqft import aqft

BASELINE = os.path.join(HERE, 'baselines', 'aqft.json')
# RESULTS.md §7, 4-input seed-11 noisy means, printed to 4 digits.
PUBLISHED_NOISY = {(3, 3): 0.8676, (4, 3): 0.7609, (4, 4): 0.7578, (5, 3): 0.7012, (5, 5): 0.6686}
# RESULTS.md §7b, PE t=5, seed 55, 10 phases.
PUBLISHED_PE = {
    '5': dict(ideal_mean=0.7860, ideal_std=0.1656, noisy_mean=0.4403, noisy_std=0.0888),
    '3': dict(ideal_mean=0.7488, ideal_std=0.1729, noisy_mean=0.4581, noisy_std=0.1028),
}


def load_baseline():
    with open(BASELINE) as f:
        return json.load(f)


def test_pe_normalization_and_bounds():
    """Phase-estimation probabilities are normalized and each P(correct) lies in [0, 1]."""
    pe = phase_estimation()
    base = load_baseline()['pe5_seed55']
    assert pe['phis'] == pytest.approx(base['phis'], abs=1e-15)
    for m, arm in pe['arms'].items():
        assert aqft(pe['t'], int(m)) == spec_aqft(pe['t'], int(m))
        for p, s in zip(arm['ideal'], arm['prob_sums']):
            assert -1e-9 <= p <= 1 + 1e-9
            assert abs(s - 1) < 1e-8
        for p in arm['noisy']:
            assert -1e-9 <= p <= 1 + 1e-9
        assert arm['ideal'] == pytest.approx(base['arms'][m]['ideal'], abs=1e-12)
        assert arm['noisy'] == pytest.approx(base['arms'][m]['noisy'], abs=1e-12)


def test_pe_ideal_ordered_noise_bounded():
    """On the seed-55 sample, truncating m lowers ideal P(correct) and the exact circuit is hurt more by noise.

    RESULTS.md §7b: exact ideal 0.7860 > m=3 ideal 0.7488, while noisy m=3 0.4581
    beats noisy exact 0.4403. Both noisy means stay inside (0, 1).
    """
    pe = phase_estimation()
    exact, mid, low = pe['arms']['5'], pe['arms']['3'], pe['arms']['2']
    assert exact['ideal_mean'] + 1e-12 >= mid['ideal_mean'] >= low['ideal_mean'] - 1e-12
    assert 0 < exact['noisy_mean'] < exact['ideal_mean']
    assert 0 < mid['noisy_mean'] < mid['ideal_mean']
    assert 0 < low['noisy_mean'] < 1
    # Visible in the published rerun: m=3 wins under this noise, by a small margin.
    assert mid['noisy_mean'] > exact['noisy_mean']
    for key, published in PUBLISHED_PE.items():
        arm = pe['arms'][key]
        for field, digits in published.items():
            assert round(arm[field], 4) == digits
    base = load_baseline()['pe5_seed55']['arms']
    for key in ('5', '3', '2'):
        for field in ('ideal_mean', 'ideal_std', 'noisy_mean', 'noisy_std'):
            assert pe['arms'][key][field] == pytest.approx(base[key][field], abs=1e-12)


def test_noisy_fidelity_bounded():
    """Noisy fidelity stays in [0, 1]. On the published 4-input sample, m=3 beats the exact QFT for n=4 and n=5."""
    sweep = noisy_sweep()
    base = load_baseline()['noisy_seed11']
    for n_s, block in sweep.items():
        n = int(n_s)
        assert block['inputs'] == base[n_s]['inputs']
        assert aqft(n, n) == spec_aqft(n, n)
        means = []
        for row, brow in zip(block['by_m'], base[n_s]['by_m']):
            assert all(-1e-9 <= f <= 1 + 1e-9 for f in row['fidelities'])
            assert -1e-9 <= row['mean'] <= 1 + 1e-9
            assert row['fidelities'] == pytest.approx(brow['fidelities'], abs=1e-12)
            assert row['mean'] == pytest.approx(brow['mean'], abs=1e-12)
            assert row['std'] == pytest.approx(brow['std'], abs=1e-12)
            means.append(row['mean'])
            published = PUBLISHED_NOISY.get((n, row['m']))
            if published is not None:
                assert round(row['mean'], 4) == published
        # m=n is exact, so its ideal fidelity is 1 and noise pulls the recorded mean strictly below 1.
        assert means[-1] < 1 - 1e-3
        if n >= 4:
            m3 = next(r['mean'] for r in block['by_m'] if r['m'] == 3)
            assert m3 > means[-1]
            assert max(means) == m3


def test_deterministic_pe_and_noisy_avg():
    """Repeating the fixed seeds rebuilds the same probabilities and the same noisy fidelities."""
    a, b = phase_estimation(), phase_estimation()
    assert a['phis'] == b['phis']
    for m in a['arms']:
        assert a['arms'][m]['ideal'] == b['arms'][m]['ideal']
        assert a['arms'][m]['noisy'] == b['arms'][m]['noisy']
        assert aqft(5, int(m)) == spec_aqft(5, int(m))
    n1, n2 = noisy_sweep(), noisy_sweep()
    for n_s in n1:
        assert n1[n_s]['inputs'] == n2[n_s]['inputs']
        for r1, r2 in zip(n1[n_s]['by_m'], n2[n_s]['by_m']):
            assert r1['fidelities'] == r2['fidelities']


def test_matches_fix_baseline():
    """The cleanup-rerun aggregates stay on the frozen baseline, including the m=2 arm."""
    pe = phase_estimation()
    noisy = noisy_sweep()
    base = load_baseline()
    for m, arm in pe['arms'].items():
        b = base['pe5_seed55']['arms'][m]
        assert arm['ideal_mean'] == pytest.approx(b['ideal_mean'], abs=1e-12)
        assert arm['noisy_mean'] == pytest.approx(b['noisy_mean'], abs=1e-12)
        assert arm['ideal'] == pytest.approx(b['ideal'], abs=1e-12)
    for n_s, block in noisy.items():
        for row, brow in zip(block['by_m'], base['noisy_seed11'][n_s]['by_m']):
            assert row['mean'] == pytest.approx(brow['mean'], abs=1e-12)
            assert row['std'] == pytest.approx(brow['std'], abs=1e-12)
    # Production note is part of the baseline contract.
    assert 'measure_aqft.py' in base['produced_by']['command']
    assert base['produced_by']['noise'] == {'p1': 1e-3, 'p2': 1e-2, 'gamma': 1e-3}


if __name__ == '__main__':
    raise SystemExit(pytest.main([__file__, '-q', '--tb=short', '-p', 'no:cacheprovider']))
