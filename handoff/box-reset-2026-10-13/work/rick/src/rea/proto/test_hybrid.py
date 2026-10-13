import sys, time; sys.path.insert(0, "/workspace/rick/tools/palace"); import palace, hybrid_palace as H
exec(open("/workspace/rick/tools/palace/evalreal.py").read().split("h = 0")[0].split("\n",1)[1])  # reuse Q
def ev(fn):
    h = 0; ts = []
    for q, exp in Q:
        t = time.perf_counter(); r = fn(q, 5); ts.append((time.perf_counter()-t)*1000); h += any(exp in x[0] for x in r)
    ts.sort(); return h, ts[5]
b, bl = ev(palace.search); n, nl = ev(H.search)
print(f"baseline recall@5={b}/10 median {bl:.1f}ms | hybrid recall@5={n}/10 median {nl:.1f}ms")
assert n >= b
