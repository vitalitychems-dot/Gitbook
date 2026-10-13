"""Invention 1: simulated annealing over step priority orders for the collab list scheduler (sched.py, imported
read-only). State = priority permutation of all expanded steps; energy = makespan (+tiny sum of finish times);
moves = swap two steps; Metropolis acceptance, geometric cooling, 5 seeds. Also computes a lower bound
(max(critical path, busiest lane load)) to know if the result is optimal."""
import sys, json, math, random
sys.path.insert(0, "/workspace/rick/tools/collab"); import sched
d = json.load(open("/workspace/rick/tools/collab/sample-tasks.json")); ST = sched.expand(d["tasks"], d["gate_cost"])
def sim_order(order):
    st = {s: ST[s] for s in order}  # simulate's fifo uses insertion order as priority
    m, fin, _ = sched.simulate(st, "fifo"); return m + 1e-3 * sum(fin.values()), m
def anneal(seed, iters=4000, T0=3.0, T1=0.01):
    r = random.Random(seed); cur = list(ST); r.shuffle(cur); e, m = sim_order(cur); best = (e, m, cur[:])
    for k in range(iters):
        T = T0 * (T1 / T0) ** (k / iters); i, j = r.sample(range(len(cur)), 2); nxt = cur[:]; nxt[i], nxt[j] = nxt[j], nxt[i]
        e2, m2 = sim_order(nxt)
        if e2 <= e or r.random() < math.exp((e - e2) / T): cur, e, m = nxt, e2, m2
        if e < best[0]: best = (e, m, cur[:])
    return best
if __name__ == "__main__":
    fifo = sched.simulate(ST, "fifo")[0]; cp = sched.simulate(ST, "cp")[0]
    lanes = {}
    for s, v in ST.items(): lanes[v["lane"]] = lanes.get(v["lane"], 0) + v["cost"]
    lb = max(max(sched.cpl(ST).values()), max(lanes.values()))
    runs = [anneal(s)[1] for s in range(5)]
    R = dict(steps=len(ST), fifo=fifo, longest_chain=cp, anneal_runs=runs, anneal_best=min(runs), lower_bound=lb, busiest_lane=max(lanes, key=lanes.get))
    print(json.dumps(R, indent=1)); json.dump(R, open("results/inv1.json", "w"), indent=1)
