"""Invention 2: Grover-like amplitude reweighting. Candidate files get amplitudes a=sqrt(softmax(-bm25)).
Oracle phase-flips candidates 'supported' by the knowledge graph: a file whose graph node (longest path-prefix
node in fullpicture/graph.json, copied read-only) is a neighbor of, or the same as, nodes of other top candidates.
Diffusion = inversion about the mean; r iterations; final p=a^2. Tuned (r, oracle) on dev, scored on test.
Applied both to raw BM25 and on top of inv3 (leak-fixed MWPM dedup)."""
import json, math, collections, common as c, inv3_eval as e
G = json.load(open("/workspace/rick/tools/fullpicture/graph.json"))
NP = sorted([(n["path"], n["id"]) for n in G["nodes"] if n.get("path")], key=lambda x: -len(x[0]))
NB = collections.defaultdict(set)
for ed in G["edges"]: NB[ed["source"]].add(ed["target"]); NB[ed["target"]].add(ed["source"])
def node(p):
    for pre, i in NP:
        if p.startswith(pre): return i
def grover(rows, r=1, top=10):
    fs, best = [], {}
    for x in rows:
        if x[1] not in best: best[x[1]] = x[3]; fs.append(x[1])
    fs = fs[:top]
    if len(fs) < 2 or r == 0: return fs
    s = [-best[f] for f in fs]; mx = max(s); w = [math.exp(v - mx) for v in s]; Z = sum(w); a = [math.sqrt(v / Z) for v in w]
    nodes = [node(f) for f in fs]
    mark = [n is not None and sum(1 for m in nodes if m and (m == n or m in NB[n])) >= 2 for n in nodes]
    if not any(mark) or all(mark): return fs
    for _ in range(r):
        a = [-v if mk else v for v, mk in zip(a, mark)]; mu = sum(a) / len(a); a = [2 * mu - v for v in a]
    return [f for _, f in sorted(zip([-v * v for v in a], fs), key=lambda t: t[0])]
def on_raw(r): return lambda q: grover(c.retrieve(q), r)[:5]
def on_inv3(r):
    def f(q):
        base = e.rank(q, 10)
        if r == 0: return base[:5]
        rows = [x for x in e.clean(c.retrieve(q, 40)) if x[1] in base]
        g = grover(sorted(rows, key=lambda x: base.index(x[1])), r)
        return (g + [b for b in base if b not in g])[:5]
    return f
if __name__ == "__main__":
    R = {}
    for name, fn in (("raw", on_raw), ("on_inv3", on_inv3)):
        dev = {r: c.score(fn(r), c.DEV) for r in (0, 1, 2)}
        rb = max(dev, key=lambda r: (dev[r]["top1"] + dev[r]["recall5"], -r))
        R[name] = dict(dev=dev, chosen_r=rb, test_r0=c.score(fn(0)), test_chosen=c.score(fn(rb)), test_r1=c.score(fn(1)))
    R["mapped_files_note"] = "graph has %d path nodes" % len(NP)
    print(json.dumps(R, indent=1)); json.dump(R, open("results/inv2.json", "w"), indent=1)
