"""Invention 3: MWPM-style near-duplicate matching. Candidate chunks for a query form a graph; edge weight =
5-shingle Jaccard (>= TAU). Repeated max-weight matching (networkx blossom = MWPM analogue, as in surface-code
decoding) pairs mirrors; matched pairs are merged (union-find) until no edges remain. Each cluster is represented
by its 'original' = the copy whose root has the highest prior, where root priors are learned ONLY on the dev split."""
import collections, json, networkx as nx, common as c
TAU = 0.6
def sh(s): w = c.tok(s); return frozenset(" ".join(w[i:i+5]) for i in range(max(1, len(w)-4)))
def jac(a, b): return len(a & b) / (len(a | b) or 1)
# root priors from dev gold files (no test peeking)
PRIOR = collections.Counter(c.ROOT(x["file"]) for x in c.DEV)
def prior(p): return PRIOR.get(c.ROOT(p), 0) - 0.5 * ("/archive" in p or "/history/" in p or "/recovered/" in p)
def clusters(rows):
    S = [sh(r[2]) for r in rows]; par = list(range(len(rows)))
    def find(i):
        while par[i] != i: par[i] = par[par[i]]; i = par[i]
        return i
    G = nx.Graph()
    for i in range(len(rows)):
        for j in range(i+1, len(rows)):
            w = jac(S[i], S[j])
            if w >= TAU: G.add_edge(i, j, weight=w)
    rounds = 0
    while G.number_of_edges():
        rounds += 1
        for i, j in nx.max_weight_matching(G):
            par[find(i)] = find(j)
        # contract: keep only edges between different clusters
        G.remove_edges_from([(i, j) for i, j in list(G.edges) if find(i) == find(j)])
    return [find(i) for i in range(len(rows))], rounds
def rank(q, k=5):
    rows = c.retrieve(q)
    if not rows: return []
    lab, _ = clusters(rows)
    groups = collections.OrderedDict()
    for i, r in enumerate(rows): groups.setdefault(lab[i], []).append(r)
    out = []
    for g in groups.values():  # cluster order = best BM25 member; rep = original copy
        rep = max(g, key=lambda r: (prior(r[1]), -g.index(r)))[1]
        if rep not in out: out.append(rep)
    for r in rows:
        if r[1] not in out: out.append(r[1])
    return out[:k]
if __name__ == "__main__":
    base = c.score(lambda q: c.files(c.retrieve(q), 5)); new = c.score(rank)
    # ablation: prior-only rerank without matching (is the matching doing the work?)
    abl = c.score(lambda q: sorted(c.files(c.retrieve(q), 30), key=lambda p: -prior(p))[:5])
    dev = c.score(rank, c.DEV)
    R = dict(baseline=base, mwpm_dedup=new, ablation_prior_only=abl, dev=dev, tau=TAU, priors=dict(PRIOR))
    print(json.dumps(R, indent=1)); json.dump(R, open("results/inv3.json", "w"), indent=1)
