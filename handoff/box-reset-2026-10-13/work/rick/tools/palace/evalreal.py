import time, palace
Q = [("AQFT approximate QFT beats exact under noise", "qlab/RESULTS.md"), ("BHNMC baseline results", "bhnmc/RESULTS.md"),
 ("Tesla patents principles", "knowledge/tesla.md"), ("U3 fusion peephole optimizer fidelity", "qlab/"),
 ("calibrated layout manila nairobi guadalupe", "qlab/"), ("Sanchez vs Gitbook conflicts autoloop", "sanchez-vs-gitbook.md"),
 ("reservoir NARMA memory capacity", "rick/"), ("round 2 inventions measured", "ROUND-2.md"),
 ("qlab PR plan tools/qlab branch", "qlab/PR-PLAN.md"), ("TESSERA Rick layers", "tessera-rick.md")]
h = 0; ts = []
for q, exp in Q:
    t = time.perf_counter(); r = palace.search(q, 5); ts.append((time.perf_counter() - t) * 1000)
    ok = any(exp in p for p, *_ in r); h += ok; print(int(ok), q, "->", r[0][0] if r else None)
ts.sort(); print(f"recall@5={h}/10 latency median={ts[5]:.1f}ms max={ts[-1]:.1f}ms")
