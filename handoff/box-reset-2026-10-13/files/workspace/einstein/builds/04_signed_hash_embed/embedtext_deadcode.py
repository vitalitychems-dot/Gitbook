"""Signed feature hashing (random +/-1 projection, the JL / 'dequantized' sketch) for embedText.
Target: vector-memory.ts embedText: 256 buckets, unsigned counts -> collisions only ADD similarity,
so unrelated texts look alike (positive bias). Candidate: same 256 buckets and same JS hash, plus a sign
bit, which makes the inner product an unbiased estimate of the exact bag-of-words cosine.
Data: real paragraphs of TESSERA docs/*.md. Metrics: mean |hashed cos - exact cos| over random pairs
(lower better); top-1 retrieval hit rate for 8-word queries cut from a paragraph (higher better)."""
import sys; sys.path.insert(0, "..")
from common import *
from collections import Counter
def jshash(w):
    h = 0
    for ch in w:
        h = ((h << 5) - h + ord(ch)) & 0xFFFFFFFF
    return h - (1 << 32) if h >= 1 << 31 else h
def embed(text, signed):
    t = tok(text); v = np.zeros(256)
    for w in t:
        h = jshash(w); a = abs(h); s = (1 if (a >> 16) & 1 else -1) if signed else 1
        v[a % 256] += s / len(t)
    n = np.linalg.norm(v); return v / n if n else v
def exact_cos(a, b):
    A, B = Counter(tok(a)), Counter(tok(b)); num = sum(A[k] * B[k] for k in A)
    return num / (np.sqrt(sum(x * x for x in A.values())) * np.sqrt(sum(x * x for x in B.values())))
P = paragraphs()
def pair_err(signed):
    def f(seed):
        r = vtk.rng(seed); idx = r.integers(0, len(P), (300, 2)); E = []
        for i, j in idx:
            if i == j: continue
            E.append(abs(embed(P[i], signed) @ embed(P[j], signed) - exact_cos(P[i], P[j])))
        return float(np.mean(E))
    return f
EMB = {s: np.array([embed(p, s) for p in P]) for s in (False, True)}
def hit(signed):
    def f(seed):
        r = vtk.rng(seed); ok = 0
        for i in r.integers(0, len(P), 200):
            t = tok(P[i]); st = r.integers(0, len(t) - 8); q = " ".join(t[st:st + 8])
            ok += int(np.argmax(EMB[signed] @ embed(q, signed)) == i)
        return ok / 200
    return f
if __name__ == "__main__":
    report([vtk.bench("04 signed hash: cosine error vs exact", pair_err(False), pair_err(True), 20, False, "mean |cos err|"),
            vtk.bench("04 signed hash: top-1 retrieval", hit(False), hit(True), 20, True, "top-1 hit rate")], "results_embedtext_deadcode.json")
