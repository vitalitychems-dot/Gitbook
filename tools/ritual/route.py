"""Calibration routing: per question, ask the agent with the best leave-one-out track record on that
question's category; escalate to all agents (median) only if that agent's confidence < conf_min."""
import statistics as st, math
def err(a, t):
    if isinstance(t, str) or isinstance(a, str): return float(str(a) != str(t))
    return abs(math.log(max(float(a), 1e-9) / float(t)))
def agg(v):
    if any(isinstance(x, str) for x in v): import collections; return collections.Counter(v).most_common(1)[0][0]
    return st.median(float(x) for x in v)
def route(cats, ans, conf, truth, conf_min=0.0):
    """cats[i]=category; ans/conf: {agent:[...]}; truth used only for PAST items (leave-one-out)."""
    out, asks = [], 0
    for i, c in enumerate(cats):
        past = [j for j, cj in enumerate(cats) if cj == c and j != i]
        if not past: best = None
        else: best = min(ans, key=lambda a: (st.mean(err(ans[a][j], truth[j]) for j in past), a))
        if best is not None and conf[best][i] >= conf_min:
            out.append(ans[best][i]); asks += 1
        else:
            out.append(agg([ans[a][i] for a in ans])); asks += (len(ans) if best is None else len(ans))
    return out, asks
def poll_all(ans):
    n = len(next(iter(ans.values())))
    return [agg([ans[a][i] for a in ans]) for i in range(n)], n * len(ans)
