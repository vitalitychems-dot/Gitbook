"""Invention 5: compress TF-IDF chunk vectors. Pool = all chunks that BM25 (top-40) returns for any dev/test query
(leak-fixed: benchmark files removed). Retrieval = cosine(query tfidf, chunk vec) over the WHOLE pool -> files.
Baseline = exact sparse TF-IDF (CSR bytes: float32 vals + int32 idx + ptr). Compressed = rank-k SVD (low-rank,
a 2-core tensor train) with float16 / int8 factors. Rank k chosen on dev; kept only if test recall@5 drop < 2%."""
import json, math, collections, numpy as np, common as c, inv3_eval as e
qs = c.DEV + c.TEST; pool = {}
for x in qs:
    for r in e.clean(c.retrieve(x["q"], 40)): pool.setdefault(r[0], (r[1], r[2]))
ids = list(pool); paths = [pool[i][0] for i in ids]; docs = [collections.Counter(c.tok(pool[i][1])) for i in ids]
df = collections.Counter(w for d in docs for w in d); N = len(docs)
V = {w: j for j, (w, n) in enumerate(df.most_common()) if n >= 2}; idf = np.zeros(len(V), np.float32)
for w, j in V.items(): idf[j] = math.log(N / df[w])
rows, cols, vals = [], [], []
for i, d in enumerate(docs):
    v = [(V[w], (1 + math.log(n)) * idf[V[w]]) for w, n in d.items() if w in V]; nr = math.sqrt(sum(x * x for _, x in v)) or 1
    for j, x in v: rows.append(i); cols.append(j); vals.append(x / nr)
sparse_bytes = len(vals) * 8 + (N + 1) * 4
X = np.zeros((N, len(V)), np.float32); X[rows, cols] = vals
def qvec(q):
    v = np.zeros(len(V), np.float32)
    for w, n in collections.Counter(c.tok(q)).items():
        if w in V: v[V[w]] = (1 + math.log(n)) * idf[V[w]]
    return v / (np.linalg.norm(v) or 1)
def ev(score_fn, xs):
    h1 = h5 = 0
    for x in xs:
        s = score_fn(qvec(x["q"])); out = []
        for i in np.argsort(-s):
            if paths[i] not in out: out.append(paths[i])
            if len(out) == 5: break
        h1 += out[:1] == [x["file"]]; h5 += x["file"] in out
    return dict(top1=round(h1 / len(xs), 3), recall5=round(h5 / len(xs), 3))
R = dict(pool_chunks=N, vocab=len(V), sparse_bytes=sparse_bytes, exact={"dev": ev(lambda q: X @ q, c.DEV), "test": ev(lambda q: X @ q, c.TEST)})
# randomized SVD (numpy only)
rng = np.random.default_rng(0); K = 512
Y = X @ rng.standard_normal((X.shape[1], K + 16), dtype=np.float32)
for _ in range(2): Y = X @ (X.T @ Y)
Q, _ = np.linalg.qr(Y); Ub, S, Vt = np.linalg.svd(Q.T @ X, full_matrices=False); U = Q @ Ub
R["lowrank"] = {}
for k in (64, 128, 256, 512):
    D = (U[:, :k] * S[:k]); P = Vt[:k]
    for dt in ("f16", "i8"):
        if dt == "f16": Dq = D.astype(np.float16).astype(np.float32); by = (D.size + P.size) * 2
        else:
            sc = np.abs(D).max(1, keepdims=True) / 127 + 1e-12; Dq = np.round(D / sc).astype(np.int8).astype(np.float32) * sc; by = D.size + N * 4 + P.size * 2
        f = lambda q, Dq=Dq, P=P: Dq @ (P @ q)
        R["lowrank"][f"k{k}_{dt}"] = dict(bytes=int(by), ratio=round(by / sparse_bytes, 3), dev=ev(f, c.DEV), test=ev(f, c.TEST))
base = R["exact"]["dev"]["recall5"]
ok = {n: v for n, v in R["lowrank"].items() if v["dev"]["recall5"] >= base * 0.98}
pick = min(ok, key=lambda n: ok[n]["bytes"]) if ok else None
R["chosen_on_dev"] = pick
if pick: R["kept"] = R["lowrank"][pick]["test"]["recall5"] >= R["exact"]["test"]["recall5"] * 0.98 and R["lowrank"][pick]["bytes"] < sparse_bytes
print(json.dumps(R, indent=1)); json.dump(R, open("results/inv5.json", "w"), indent=1)
