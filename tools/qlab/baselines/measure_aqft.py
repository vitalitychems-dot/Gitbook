"""Reproduce tools/qlab/baselines/aqft.json from the current aqft.py.

Run from anywhere:

  OMP_NUM_THREADS=1 python3 tools/qlab/baselines/measure_aqft.py

The protocol is the assertion-free sweeps this baseline replaces, cut to the
sizes that finish in well under a minute:

- ideal fidelity: seed 5, 8 basis inputs, n=3..6, m=1..n
  (the start of the old test_aqft.py sweep)
- noisy fidelity: seed 11, 4 basis inputs, n=3..5, m=1..n,
  noise p1=1e-3, p2=1e-2, gamma=1e-3 on lower(aqft)
  (the start of test_aqft_avg.py / the 4-input column in RESULTS.md §7)
- phase estimation: seed 55, 10 phases, t=5, m in {5, 3, 2}
  (test_aqft_fix.py, plus the m=2 arm from test_aqft.py)
- examples/aqft5.json macro AQFT[5, 4], gate list and |0> overlap
- unitarity / norm / inverse round-trip for n=2..4

The n=7..10 noisy rows in RESULTS.md §7 and §7b are not recomputed
(the original scripts took 484 s and 327 s).
"""
import json, os, sys, time
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from qsim import SV, qft, unitary
from aqft import aqft, inverse
from qopt2 import lower
import qnoise2

NK = dict(p1=1e-3, p2=1e-2, gamma=1e-3)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aqft.json')
AQFT5 = os.path.join(ROOT, 'examples', 'aqft5.json')


def spec_aqft(n, m):
    """Oracle for aqft.py: drop CP whose angle is below 2π/2^m."""
    thr = 2 * np.pi / 2**m - 1e-15
    return [g for g in qft(n) if not (g[0] == 'CP' and g[2] < thr)]


def cp_count(c):
    return sum(g[0] == 'CP' for g in c)


def twoq_lowered(c):
    return sum(len(g[1]) == 2 for g in lower(c))


def serialize(c):
    out = []
    for g in c:
        row = [g[0], [int(q) for q in g[1]]]
        if len(g) > 2:
            row.append(float(g[2]))
        out.append(row)
    return out


def ideal_fidelities(n, m, xs):
    fids = []
    for x in xs:
        ref = SV(n)
        ref.v[:] = 0
        ref.v[int(x)] = 1
        ref.run(qft(n))
        got = SV(n)
        got.v[:] = 0
        got.v[int(x)] = 1
        got.run(aqft(n, m))
        fids.append(float(abs(np.vdot(ref.v, got.v)) ** 2))
    return fids


def ideal_sweep(n0=3, n1=6, seed=5, k=8):
    rng = np.random.default_rng(seed)
    rows = {}
    for n in range(n0, n1 + 1):
        xs = [int(x) for x in rng.integers(0, 2**n, k)]
        by_m = []
        for m in range(1, n + 1):
            f = ideal_fidelities(n, m, xs)
            c = aqft(n, m)
            by_m.append(dict(
                m=m,
                mean=float(np.mean(f)),
                min=float(np.min(f)),
                fidelities=f,
                gates=len(c),
                cp=int(cp_count(c)),
                twoq=int(twoq_lowered(c)),
            ))
        rows[str(n)] = dict(inputs=xs, by_m=by_m)
    return rows


def noisy_sweep(n0=3, n1=5, seed=11, k=4):
    rng = np.random.default_rng(seed)
    rows = {}
    for n in range(n0, n1 + 1):
        xs = [int(x) for x in rng.integers(0, 2**n, k)]
        refs = []
        for x in xs:
            s = SV(n)
            s.v[:] = 0
            s.v[x] = 1
            refs.append(s.run(qft(n)).v.copy())
        by_m = []
        for m in range(1, n + 1):
            L = lower(aqft(n, m))
            f = [float(np.real(p.conj() @ qnoise2.run(n, L, init=x, **NK) @ p))
                 for x, p in zip(xs, refs)]
            by_m.append(dict(m=m, mean=float(np.mean(f)), std=float(np.std(f)), fidelities=f))
        rows[str(n)] = dict(inputs=xs, by_m=by_m)
    return rows


def phase_estimation(t=5, seed=55, nphi=10, ms=(5, 3, 2)):
    rng = np.random.default_rng(seed)
    phis = [float(p) for p in rng.random(nphi)]
    arms = {}
    for m in ms:
        ideal, noisy, sums = [], [], []
        for phi in phis:
            c = ([('X', [t])]
                 + [('H', [k]) for k in range(t)]
                 + [('CP', [k, t], 2 * np.pi * phi * 2**k) for k in range(t)]
                 + inverse(aqft(t, m)))
            y = int(round(phi * 2**t)) % 2**t
            probs = SV(t + 1).run(c).probs()
            sums.append(float(probs.sum()))
            ideal.append(float(probs[y + 2**t]))
            rho = qnoise2.run(t + 1, lower(c), **NK)
            noisy.append(float(np.real(rho[y + 2**t, y + 2**t])))
        arms[str(m)] = dict(
            m=m,
            ideal_mean=float(np.mean(ideal)),
            ideal_std=float(np.std(ideal)),
            noisy_mean=float(np.mean(noisy)),
            noisy_std=float(np.std(noisy)),
            ideal=ideal,
            noisy=noisy,
            prob_sums=sums,
        )
    return dict(t=t, seed=seed, nphi=nphi, phis=phis, arms=arms)


def aqft5_record():
    doc = json.load(open(AQFT5))
    c = aqft(5, 4)
    fids = ideal_fidelities(5, 4, [0])
    return dict(
        document=doc,
        gates=len(c),
        cp=int(cp_count(c)),
        twoq=int(twoq_lowered(c)),
        circuit=serialize(c),
        zero_fidelity=fids[0],
    )


def unitarity_report(n_max=4):
    rng = np.random.default_rng(7)
    max_u = 0.0
    max_norm = 0.0
    max_round = 0.0
    max_qft = 0.0
    for n in range(2, n_max + 1):
        for m in range(1, n + 1):
            U = unitary(n, aqft(n, m))
            max_u = max(max_u, float(np.max(np.abs(U.conj().T @ U - np.eye(2**n)))))
            x = rng.normal(size=2**n) + 1j * rng.normal(size=2**n)
            x /= np.linalg.norm(x)
            s = SV(n)
            s.v = x.copy()
            s.run(aqft(n, m))
            max_norm = max(max_norm, float(abs(np.linalg.norm(s.v) - 1)))
            for x0 in (0, 1, 2**n - 1):
                s = SV(n)
                s.v[:] = 0
                s.v[x0] = 1
                s.run(aqft(n, m))
                s.run(inverse(aqft(n, m)))
                phase = np.angle(s.v[x0])
                expect = np.zeros(2**n, complex)
                expect[x0] = 1
                max_round = max(max_round, float(np.max(np.abs(s.v * np.exp(-1j * phase) - expect))))
        Uq = unitary(n, qft(n))
        Ua = unitary(n, aqft(n, n))
        max_qft = max(max_qft, float(np.max(np.abs(Uq - Ua))))
    return dict(
        n_max=n_max,
        max_abs_UtU_minus_I=max_u,
        max_norm_err=max_norm,
        max_roundtrip_err=max_round,
        max_aqft_n_minus_qft=max_qft,
    )


def build():
    t0 = time.time()
    ideal = ideal_sweep()
    noisy = noisy_sweep()
    pe = phase_estimation()
    ref = aqft5_record()
    uni = unitarity_report()
    # seed-5 mean at n=5, m=4 is the aqft5 operating point on the sweep inputs
    seed5_m4 = next(r for r in ideal['5']['by_m'] if r['m'] == 4)
    ref['seed5_mean'] = seed5_m4['mean']
    ref['seed5_min'] = seed5_m4['min']
    return dict(
        schema='qlab-aqft-baseline/v1',
        produced_by=dict(
            date='2026-10-13',
            command='OMP_NUM_THREADS=1 python3 tools/qlab/baselines/measure_aqft.py',
            cwd='repository root (the script locates tools/qlab itself)',
            script='tools/qlab/baselines/measure_aqft.py',
            numpy=np.__version__,
            threads='OMP_NUM_THREADS=1',
            noise=NK,
            seconds=None,
            notes=(
                'Frozen outputs of the current aqft.py, using the seeds of the old '
                'assertion-free sweeps. ideal_seed5 follows the old test_aqft.py draw '
                'for n=3..6 (8 basis inputs, np.random.default_rng(5)). '
                'noisy_seed11 follows test_aqft_avg.py and the RESULTS.md section 7 '
                '4-input column for n=3..5 (rng 11; p1=1e-3, p2=1e-2, gamma=1e-3; '
                'fidelity of lower(aqft) against the exact QFT state). '
                'pe5_seed55 follows the old test_aqft_fix.py (rng 55, 10 phases, t=5) '
                'and adds the m=2 arm from the old sweep. '
                'aqft5 expands examples/aqft5.json with the drop rule '
                'controlled-phase angle < 2*pi/2^m. '
                'unitarity records max |U dagger U - I|, statevector norm error, '
                'inverse(aqft) round-trip error, and aqft(n,n)-qft(n) for n=2..4. '
                'These rows match RESULTS.md section 7 and 7b to the printed digits '
                '(ideal n=4 m=3 0.990485, n=5 m=3 0.959550, n=6 m=3 0.906327; '
                'noisy n=4 m=3 0.7609 vs exact 0.7578, n=5 m=3 0.7012 vs 0.6686; '
                'PE t=5 exact ideal 0.7860+/-0.1656 noisy 0.4403+/-0.0888, '
                'm=3 ideal 0.7488+/-0.1729 noisy 0.4581+/-0.1028). '
                'The original n<=10 sweep (484 s) and the n=9,10 fix rerun (part of 327 s) '
                'are not recomputed; those published rows stay in RESULTS.md.'
            ),
        ),
        tolerances=dict(fidelity=1e-12, probability=1e-9, unitary=1e-9),
        ideal_seed5=ideal,
        noisy_seed11=noisy,
        pe5_seed55=pe,
        aqft5=ref,
        unitarity=uni,
    ), time.time() - t0


def main():
    doc, seconds = build()
    doc['produced_by']['seconds'] = round(seconds, 3)
    with open(OUT, 'w') as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f'wrote {OUT} in {seconds:.2f}s')


if __name__ == '__main__':
    main()
