"""Inventions 1-5: token efficiency on real allsee briefs (c1 test split). Hits cached once; transforms only change bodies/k."""
import json, re, math, random, collections, time
from harness import *
c = con()
def hits_for(xs, k=8):
    return [allsee.search(x["q"], k, c, {}) for x in xs]
def evalb(xs, briefs):  # briefs: list of hit-lists (bodies possibly pruned)
    r = a = tk = 0
    for x, hs in zip(xs, briefs):
        r += recall(hs, x); a += answer(x["q"], hs) == x["a"]; tk += sum(T(h["body"]) for h in hs)
    n = len(xs); return dict(recall5=round(r/n,4), acc=round(a/n,4), tokens_brief=round(tk/n,1))
def sents(b): return [s for s in re.split(r"(?<=[.!?])\s+|\n", b) if s.strip()]
# 1 valvular one-way line filter (keep only query-bearing lines)
def valve(q, hs):
    qs = set(tok(q)); out = []
    for h in hs:
        b = "\n".join(l for l in h["body"].splitlines() if qs & set(tok(l))) or h["body"][:300]
        out.append({**h, "body": b})
    return out
# 2 free-energy sentence budget: keep sentence s iff marginal info dE (new query-term coverage, idf-weighted) > T*cost(s)
def free_energy(q, hs, Temp):
    qs = set(tok(q)); w = {t: allsee.idf(c, t) for t in qs}; covered = set(); out = []
    for h in hs:
        keep = []
        for s in sents(h["body"]):
            st = set(tok(s)); gain = sum(w[t] for t in (st & qs) - covered); hasnum = bool(re.search(NUM, s))
            info = gain + (0.5 * sum(w[t] for t in st & qs) if hasnum else 0)
            if info > Temp * T(s) ** 0.5: keep.append(s); covered |= st & qs
        out.append({**h, "body": "\n".join(keep) or h["body"][:120]})
    return out
# 3 Landauer adaptive k: bit-cost = entropy of softmax(scores); low entropy (confident) -> fewer hits
def landauer(q, hs8, hi, lo):
    s = [h["score"] for h in hs8[:5]]
    if not s: return hs8[:5]
    m = max(s); p = [math.exp((v - m) / max(1e-6, abs(m) * 0.1)) for v in s]; Z = sum(p); p = [v/Z for v in p]
    H = -sum(v * math.log2(v) for v in p if v > 0)
    k = lo if H < hi else 5
    return hs8[:k]
# 4 annealed context pruning: SA over sentence subset maximizing coverage - lam*tokens (vs greedy #2)
def anneal(q, hs, lam, iters=300, seed=0):
    rnd = random.Random(seed); qs = set(tok(q)); w = {t: allsee.idf(c, t) for t in qs}
    S = [(i, s, set(tok(s)) & qs, T(s), bool(re.search(NUM, s))) for i, h in enumerate(hs) for s in sents(h["body"])]
    if not S: return hs
    def E(x):
        cov = set().union(*[S[j][2] for j in range(len(S)) if x[j]]) if any(x) else set()
        num = sum(1 for j in range(len(S)) if x[j] and S[j][4] and S[j][2])
        return -(sum(w[t] for t in cov) + 0.5 * min(num, 3)) + lam * sum(S[j][3] for j in range(len(S)) if x[j])
    x = [bool(s[2]) for s in S]; e = E(x); best = (e, x[:])
    for it in range(iters):
        Tt = 2.0 * (1 - it / iters) + 1e-3; j = rnd.randrange(len(S)); x[j] = not x[j]; e2 = E(x)
        if e2 <= e or rnd.random() < math.exp((e - e2) / Tt): e = e2
        else: x[j] = not x[j]
        if e < best[0]: best = (e, x[:])
    x = best[1]; out = []
    for i, h in enumerate(hs):
        b = "\n".join(S[j][1] for j in range(len(S)) if x[j] and S[j][0] == i)
        out.append({**h, "body": b or h["body"][:120]})
    return out
# 5 cross-hit line dedup (exact+normalized) - "entropy" of repeated lines is zero
def dedup_lines(hs):
    seen = set(); out = []
    for h in hs:
        keep = []
        for l in h["body"].splitlines():
            k = " ".join(tok(l))
            if k and k in seen: continue
            seen.add(k); keep.append(l)
        out.append({**h, "body": "\n".join(keep)})
    return out
if __name__ == "__main__":
    R = {}; t0 = time.time()
    HD = hits_for(DEV); HT = hits_for(TEST); print("cached", round(time.time()-t0,1), "s")
    k5 = lambda H: [h[:5] for h in H]
    R["baseline"] = {"dev": evalb(DEV, k5(HD)), "test": evalb(TEST, k5(HT))}
    R["1_valve"] = {"dev": evalb(DEV, [valve(x["q"], h[:5]) for x, h in zip(DEV, HD)]), "test": evalb(TEST, [valve(x["q"], h[:5]) for x, h in zip(TEST, HT)])}
    # 2 tune Temp on dev (on top of valve), pick max token cut with acc>=base dev acc & recall same
    sweep = {}
    for Tp in (0, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0):
        sweep[Tp] = evalb(DEV, [free_energy(x["q"], valve(x["q"], h[:5]), Tp) for x, h in zip(DEV, HD)])
    ok = [Tp for Tp, m in sweep.items() if m["acc"] >= R["1_valve"]["dev"]["acc"] - 0.005 and m["recall5"] >= R["1_valve"]["dev"]["recall5"]]
    Tb = min(ok, key=lambda Tp: sweep[Tp]["tokens_brief"]) if ok else 0
    R["2_free_energy"] = {"dev_sweep": sweep, "T": Tb, "test": evalb(TEST, [free_energy(x["q"], valve(x["q"], h[:5]), Tb) for x, h in zip(TEST, HT)])}
    sweep = {}
    for hi in (0.5, 1.0, 1.5, 2.0):
        for lo in (2, 3, 4):
            sweep[f"{hi}/{lo}"] = evalb(DEV, [valve(x["q"], landauer(x["q"], h, hi, lo)) for x, h in zip(DEV, HD)])
    base = R["1_valve"]["dev"]; ok = [k for k, m in sweep.items() if m["recall5"] >= base["recall5"] - 0.005 and m["acc"] >= base["acc"] - 0.005]
    kb = min(ok, key=lambda k: sweep[k]["tokens_brief"]) if ok else "9/5"; hi, lo = map(float, kb.split("/"))
    R["3_landauer_k"] = {"dev_sweep": sweep, "pick": kb, "test": evalb(TEST, [valve(x["q"], landauer(x["q"], h, hi, int(lo))) for x, h in zip(TEST, HT)])}
    sweep = {}
    for lam in (0.0, 0.02, 0.05, 0.1):
        sweep[lam] = evalb(DEV, [anneal(x["q"], valve(x["q"], h[:5]), lam) for x, h in zip(DEV, HD)])
    ok = [l for l, m in sweep.items() if m["acc"] >= base["acc"] - 0.005 and m["recall5"] >= base["recall5"]]
    lb = min(ok, key=lambda l: sweep[l]["tokens_brief"]) if ok else 0.0
    R["4_anneal_prune"] = {"dev_sweep": sweep, "lam": lb, "test": evalb(TEST, [anneal(x["q"], valve(x["q"], h[:5]), lb) for x, h in zip(TEST, HT)])}
    R["5_dedup_lines"] = {"dev": evalb(DEV, [dedup_lines(valve(x["q"], h[:5])) for x, h in zip(DEV, HD)]), "test": evalb(TEST, [dedup_lines(valve(x["q"], h[:5])) for x, h in zip(TEST, HT)])}
    json.dump(R, open("results/tokens.json", "w"), indent=1, default=str)
    for k, v in R.items(): print(k, json.dumps(v.get("test")), {kk: v[kk] for kk in ("T", "pick", "lam") if kk in v})
