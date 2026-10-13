"""Cycle-2 quantum claims (numpy statevector/density sims). -> quantum2_results.json"""
import numpy as np, json, math, itertools
rng = np.random.default_rng(2); R = {}
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2); I = np.eye(2); X = np.array([[0, 1], [1, 0]]); Z = np.diag([1., -1])
def kron(*a):
    o = np.array([[1.]])
    for m in a: o = np.kron(o, m)
    return o
# Q6 Deutsch-Jozsa: one oracle query decides constant vs balanced for n=1..8, all sampled oracles; classical deterministic worst case needs 2^(n-1)+1
res = []
for n in range(1, 9):
    N = 2 ** n; Hn = kron(*[H] * n); okc = True
    fs = [np.zeros(N, int), np.ones(N, int)] + [rng.permutation(np.r_[np.zeros(N // 2, int), np.ones(N // 2, int)]) for _ in range(30)]
    for f in fs:
        psi = Hn @ ((-1.0) ** f * (Hn @ np.eye(N)[0]))  # phase-oracle form
        p0 = abs(psi[0]) ** 2; const = len(set(f)) == 1
        okc &= (abs(p0 - 1) < 1e-9) if const else (p0 < 1e-9)
    res.append(dict(n=n, quantum_queries=1, classical_worst=2 ** (n - 1) + 1, all_correct=bool(okc)))
R["Q6_deutsch_jozsa"] = dict(table=res, verdict="CONFIRMED" if all(r["all_correct"] for r in res) else "FAILED")
# Q7 Teleportation: ideal fidelity 1 for Haar states; with a Werner resource (singlet fraction F) fidelity = (2F+1)/3; beats classical 2/3 iff F>1/2
def teleport(psi, rho_pair):
    rho = np.kron(np.outer(psi, psi.conj()), rho_pair)  # q0=psi, q1 Alice half, q2 Bob
    bell = [np.array(v) / np.sqrt(2) for v in ([1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, -1], [0, 1, -1, 0])]
    cor = [I, X, Z, Z @ X]; out = np.zeros((2, 2), complex)
    for b, U in zip(bell, cor):
        P = np.kron(np.outer(b, b.conj()), I); r = P @ rho @ P
        rb = np.einsum('ijkilk->jl', r.reshape(4, 2, 4, 2).reshape(2, 2, 2, 2, 2, 2).transpose(0, 1, 2, 3, 4, 5)) if False else r.reshape(4, 2, 4, 2).trace(axis1=0, axis2=2)
        out += U @ rb @ U.conj().T
    return np.real(psi.conj() @ out @ psi)
phi = np.array([1, 0, 0, 1]) / np.sqrt(2); B = np.outer(phi, phi)
rows = []
for F in (1.0, 0.9, 0.75, 0.5, 0.4):
    p = (4 * F - 1) / 3; rp = p * B + (1 - p) * np.eye(4) / 4
    st = [(lambda v: v / np.linalg.norm(v))(rng.normal(size=2) + 1j * rng.normal(size=2)) for _ in range(300)]
    f = np.mean([teleport(s, rp) for s in st]); rows.append(dict(F=F, fidelity=round(float(f), 6), theory=round((2 * F + 1) / 3, 6)))
R["Q7_teleportation"] = dict(table=rows, classical_limit=2 / 3, verdict="CONFIRMED" if all(abs(r["fidelity"] - r["theory"]) < 1e-9 for r in rows) else "FAILED")
# Q8 Shor order finding N=15: 8-qubit counting register + modular-exp oracle (exact unitary); classical post-processing by continued fractions
def order_find(a, N=15, t=8):
    M = 2 ** t; vals = [pow(a, x, N) for x in range(M)]; amps = np.zeros((M, N), complex)
    for x in range(M): amps[x, vals[x]] = 1 / np.sqrt(M)
    # inverse QFT over the counting register
    F = np.exp(-2j * np.pi * np.outer(np.arange(M), np.arange(M)) / M) / np.sqrt(M); amps = F @ amps
    p = (abs(amps) ** 2).sum(1); shots = rng.choice(M, 200, p=p / p.sum()); rs = []
    from fractions import Fraction
    for y in shots:
        r = Fraction(int(y), M).limit_denominator(N).denominator
        if pow(a, r, N) == 1: rs.append(r)
    r = min(rs) if rs else None; succ = len(rs) / len(shots)
    fac = sorted({math.gcd(pow(a, r // 2) - 1, N), math.gcd(pow(a, r // 2) + 1, N)} - {1, N}) if r and r % 2 == 0 else []
    return dict(a=a, period=r, true_period=next(k for k in range(1, N) if pow(a, k, N) == 1), shot_success=round(succ, 3), factors=fac)
sh = [order_find(a) for a in (2, 7, 8, 11, 13)]
R["Q8_shor_15"] = dict(table=sh, verdict="CONFIRMED" if all(s["period"] == s["true_period"] for s in sh) and any(s["factors"] == [3, 5] for s in sh) else "FAILED")
# Q9 Decoherence: Ramsey on a qubit with Markovian dephasing rate gamma=1/T2 (+ T1). Fit coherence decay -> recovered T2, check 1/T2 = 1/(2T1) + 1/Tphi
rows = []
for T1, Tphi in ((100., 80.), (50., 1e9), (200., 40.)):
    T2 = 1 / (1 / (2 * T1) + 1 / Tphi); ts = np.linspace(0, 3 * T2, 40); coh = []
    for t in ts:  # Kraus composition: amplitude damping then pure dephasing on |+>
        g = 1 - np.exp(-t / T1); lam = 1 - np.exp(-t / Tphi) if Tphi < 1e8 else 0
        rho = np.array([[.5, .5], [.5, .5]], complex)
        K = [np.array([[1, 0], [0, np.sqrt(1 - g)]]), np.array([[0, np.sqrt(g)], [0, 0]])]; rho = sum(k @ rho @ k.T for k in K)
        K = [np.sqrt(1 - lam / 2) * I, np.sqrt(lam / 2) * Z]; rho = sum(k @ rho @ k.T for k in K)
        coh.append(2 * abs(rho[0, 1]))
    fit = -1 / np.polyfit(ts, np.log(coh), 1)[0]; rows.append(dict(T1=T1, Tphi=Tphi if Tphi < 1e8 else "inf", T2_theory=round(T2, 3), T2_fit=round(float(fit), 3)))
R["Q9_T2_scaling"] = dict(table=rows, verdict="CONFIRMED" if all(abs(r["T2_fit"] - r["T2_theory"]) / r["T2_theory"] < 1e-3 for r in rows) else "FAILED", note="T2 <= 2*T1 holds; Tphi=inf gives T2=2*T1")
# Q10 Repetition code threshold (bit-flip code capacity, majority decode): logical error falls with d iff p < 0.5; also phenomenological check that d=3 beats bare qubit iff p<0.5
rows = []
for p in (0.01, 0.05, 0.1, 0.2, 0.3, 0.45, 0.55):
    exact = {d: sum(math.comb(d, k) * p ** k * (1 - p) ** (d - k) for k in range(d // 2 + 1, d + 1)) for d in (1, 3, 5, 7, 9)}
    mc = {d: float(np.mean(rng.random((100000, d)).__lt__(p).sum(1) > d // 2)) for d in (3, 7)}
    rows.append(dict(p=p, **{f"PL_d{d}": float(f"{v:.3g}") for d, v in exact.items()}, mc_d3=mc[3], mc_d7=mc[7], d_helps=bool(exact[9] < exact[3] < exact[1])))
thr_ok = all(r["d_helps"] == (r["p"] < 0.5) for r in rows)
R["Q10_repetition_threshold"] = dict(table=rows, threshold="0.5 (code-capacity bit-flip)", verdict="CONFIRMED" if thr_ok else "FAILED", note="surface-code ~1% threshold not simulated here (needs a decoder); this is the repetition-code analogue")
json.dump(R, open("quantum2_results.json", "w"), indent=1, default=float)
for k, v in R.items(): print(k, v["verdict"])
print(sh); print(R["Q7_teleportation"]["table"]); print(rows[2], rows[-1])
