"""Rotated surface code, code-capacity X noise, exact MWPM (bitmask DP) decoder. numpy+stdlib."""
import sys, json, numpy as np
from collections import deque
from functools import lru_cache
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gf2 import rank, nullspace
import vtk

def build(d):
    q = lambda i, j: i * d + j
    X, Z = [], []
    for r in range(d + 1):
        for c in range(d + 1):
            qs = [q(i, j) for i in (r - 1, r) for j in (c - 1, c) if 0 <= i < d and 0 <= j < d]
            bulk = 1 <= r <= d - 1 and 1 <= c <= d - 1
            t = 'Z' if (r + c) % 2 == 0 else 'X'
            if bulk: (Z if t == 'Z' else X).append(qs)
            elif r in (0, d) and 1 <= c <= d - 1 and t == 'X': X.append(qs)
            elif c in (0, d) and 1 <= r <= d - 1 and t == 'Z': Z.append(qs)
    n = d * d
    def mat(L):
        M = np.zeros((len(L), n), np.uint8)
        for k, s in enumerate(L): M[k, s] = 1
        return M
    Hx, Hz = mat(X), mat(Z)
    assert not ((Hx.astype(int) @ Hz.T.astype(int)) % 2).any(), "stabilizers anticommute"
    assert Hx.shape[0] + Hz.shape[0] == n - 1 and rank(Hx) + rank(Hz) == n - 1
    # Z logical: commutes with X checks (in ker Hx), not in rowspace(Hz)
    rz = rank(Hz)
    zL = next(v for v in nullspace(Hx) if rank(np.vstack([Hz, v])) > rz)
    return Hx, Hz, zL

class Decoder:
    def __init__(self, Hz, zL):
        m, n = Hz.shape; B = m
        adj = [[] for _ in range(m + 1)]
        for k in range(n):
            ch = list(np.nonzero(Hz[:, k])[0])
            a, b = (ch + [B])[:2]
            adj[a].append((b, int(zL[k]))); adj[b].append((a, int(zL[k])))
        self.D = np.full((m + 1, m + 1), 10**6, int); self.P = np.zeros((m + 1, m + 1), int)
        for s in range(m):
            dist = {s: 0}; par = {s: 0}; dq = deque([s])
            while dq:
                u = dq.popleft()
                if u == B: continue
                for v, w in adj[u]:
                    if v not in dist:
                        dist[v] = dist[u] + 1; par[v] = par[u] ^ w; dq.append(v)
            for v in dist: self.D[s, v] = dist[v]; self.P[s, v] = par[v]
        self.Hz, self.zL, self.B = Hz, zL, B

    def logical_flip(self, synd):
        """MWPM correction parity along zL."""
        dfx = list(np.nonzero(synd)[0]); k = len(dfx); B = self.B; D, P = self.D, self.P
        @lru_cache(None)
        def f(mask):
            if mask == 0: return (0, 0)
            i = (mask & -mask).bit_length() - 1; m2 = mask & ~(1 << i); a = dfx[i]
            c, p = f(m2); best = (c + D[a, B], p ^ P[a, B])
            j = m2
            while j:
                jb = (j & -j).bit_length() - 1; j &= j - 1
                c, p = f(m2 & ~(1 << jb)); b = dfx[jb]
                cand = (c + D[a, b], p ^ P[a, b])
                if cand[0] < best[0]: best = cand
            return best
        return f((1 << k) - 1)[1]

def logical_error_rate(d, p, shots, seed):
    Hx, Hz, zL = build(d); dec = Decoder(Hz, zL); r = vtk.rng(seed)
    E = (r.random((shots, d * d)) < p).astype(np.uint8)
    S = (E.astype(int) @ Hz.T.astype(int)) % 2
    L = (E.astype(int) @ zL.astype(int)) % 2
    fails = sum(int(L[t] ^ dec.logical_flip(S[t])) for t in range(shots))
    return fails

if __name__ == "__main__":
    shots = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    ps = [0.01, 0.02, 0.04, 0.06, 0.08, 0.09, 0.10, 0.11, 0.12, 0.14]
    out = {}
    for d in (3, 5, 7):
        out[d] = []
        for i, p in enumerate(ps):
            k = logical_error_rate(d, p, shots, 1000 * d + i)
            w = vtk.wilson(k, shots); out[d].append({"p": p, "fails": k, "shots": shots, "pL": w[0], "lo": w[1], "hi": w[2]})
            print(d, p, k, round(w[0], 5), flush=True)
    res = {"data": out}
    for a, b in ((3, 5), (5, 7), (3, 7)):
        res[f"cross_{a}_{b}"] = vtk.find_crossing(ps, [x["pL"] for x in out[a]], [x["pL"] for x in out[b]])
    lo = [x for x in out[3] if x["p"] <= 0.04]
    res["d3_slope_loglog_p<=0.04"] = float(np.polyfit(np.log([x["p"] for x in lo]), np.log([max(x["pL"],1e-9) for x in lo]), 1)[0])
    print({k: v for k, v in res.items() if k != "data"})
    json.dump(res, open(sys.argv[2] if len(sys.argv) > 2 else "surface_results.json", "w"), indent=1)
    vtk.svg_plot({f"d={d}": (ps, [x["pL"] for x in out[d]]) for d in out}, sys.argv[3] if len(sys.argv) > 3 else "surface_threshold.svg", "physical p", "logical error rate", True, "Rotated surface code, code capacity, MWPM")
