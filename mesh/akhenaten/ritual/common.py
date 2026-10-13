"""Shared helpers. No ground truth here: answers live only in a private file outside the repo."""
import json, statistics, collections, math
def load_round(path, n):
    out = {}
    for l in open(path):
        if l.strip():
            m = json.loads(l)
            if m.get("kind") == "result" and "agent" in m and len(m.get("answers", [])) == n:
                out[m["agent"]] = m["answers"]
    return out
def merge_one(q, vals):
    v = [x for x in vals if x is not None]
    if q["type"] == "num": return statistics.median(float(x) for x in v)
    return collections.Counter(v).most_common(1)[0][0]
def spread(q, vals):
    """num: median |log(x/median)|; cat: 1 - majority share. 0 = full agreement."""
    v = [x for x in vals if x is not None]
    if q["type"] == "num":
        v = [float(x) for x in v if float(x) > 0]
        med = statistics.median(v)
        return statistics.mean(abs(math.log(x / med)) for x in v)
    c = collections.Counter(v)
    return 1 - c.most_common(1)[0][1] / len(v)
