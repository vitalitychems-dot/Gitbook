#!/usr/bin/env python3
"""Memory graph: nodes (repos, agents, modules, results, rules) linked by mentions, imports, references.
Reads the palace db (text) + package.json/TS imports in TESSERA-ro. Writes graph.json + graph.mmd. stdlib only."""
import os, re, json, sqlite3, glob, collections, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("PALACE_DB", os.path.join(HERE, "..", "palace", "palace.db"))
T = "/workspace/TESSERA-ro"; GB = os.environ.get("RICK_GITBOOK", "/workspace/rick/src/Gitbook")
AGENTS = {"tessera": r"\btessera\b", "command-center": r"command center", "mesh-cloud": r"mesh cloud", "security": r"\bsecurity (lane|gate|pass|agent)\b",
  "build": r"\bbuild (lane|gate|pass|agent)\b", "gitbook-moderator": r"\bmoderator\b", "gitbook-cordnation": r"cordnation", "rick": r"\brick\b",
  "replit": r"\breplit\b", "cursor-project": r"cursor project", "grok-bot": r"grok bot", "father": r"\bfather\b"}
def nodes():
    N = {}
    def add(i, kind, path=None, pat=None): N[i] = {"id": i, "kind": kind, "path": path, "pat": pat}
    for r in ["TESSERA", "Gitbook", "rea-batch", "tess-opt", "tw", "rick", "tessera-brain", "cloud-agent-transcripts", "gitbook-cordnation"]:
        add("repo:" + r, "repo", pat=r"\b" + re.escape(r) + r"\b")
    for c in ["amber-flame-tiger-sand", "fleet-moss-monarch-rapid", "XXX", "z"]:
        add("repo:collink1007/" + c, "repo", pat=re.escape("collink1007/" + c) + r"\b")
    for a, p in AGENTS.items(): add("agent:" + a, "agent", pat=p)
    for d in sorted(glob.glob(T + "/artifacts/*/") + glob.glob(T + "/lib/*/")):
        m = os.path.basename(d.rstrip("/")); add("module:" + m, "module", d, r"\b" + re.escape(m) + r"\b")
    for d in sorted(glob.glob("/workspace/rick/tools/*/")) + [p for p in glob.glob("/workspace/rick/*/") if "tools" not in p]:
        m = os.path.basename(d.rstrip("/")); add("module:rick/" + m, "module", d, r"\b" + re.escape(m) + r"\b")
    for p in sorted(glob.glob(GB + "/mesh/*.md") + glob.glob(GB + "/mesh/roles/*.md") + glob.glob(GB + "/intake/status-definitions.md")):
        b = os.path.basename(p); add("rule:" + b, "rule", p, re.escape(b))
    for p in sorted(glob.glob("/workspace/rick/**/RESULTS.md", recursive=True) + glob.glob("/workspace/rick/*.md") + glob.glob("/workspace/rea-batch/*/*.md")):
        if re.search(r"(?i)result|summary|report|invent|survey|round", p): add("result:" + os.path.relpath(p, "/workspace"), "result", p, None)
    return N
def owner(path, N):
    best = None
    for i, n in N.items():
        if n["path"] and path.startswith(n["path"].rstrip("/")) and (best is None or len(n["path"]) > len(N[best]["path"])): best = i
    if best: return best
    for r in ["rea-batch", "tess-opt", "tw", "tessera-brain", "cloud-agent-transcripts", "gitbook-cordnation"]:
        if path.startswith("/workspace/" + r): return "repo:" + r
    if path.startswith("/workspace/TESSERA-ro") or "/rick-audit/TESSERA" in path or "/rick/src/TESSERA" in path: return "repo:TESSERA"
    if "Gitbook" in path: return "repo:Gitbook"
    return "repo:rick"
def build():
    N = nodes(); E = collections.Counter(); c = sqlite3.connect(DB)
    pats = [(i, re.compile(n["pat"], re.I)) for i, n in N.items() if n["pat"]]
    seen = 0
    for path, body in c.execute("select path, body from chunks"):
        seen += 1; src = owner(path, N)
        for i, rx in pats:
            if i != src and rx.search(body): E[(src, i, "mentions")] += 1
        for l in re.findall(r"\]\(([^)#\s]+\.md)", body):  # markdown references
            t = "rule:" + os.path.basename(l)
            if t in N and t != src: E[(src, t, "references")] += 1
    for pj in glob.glob(T + "/artifacts/*/package.json") + glob.glob(T + "/lib/*/package.json"):  # imports
        src = "module:" + os.path.basename(os.path.dirname(pj)); deps = json.load(open(pj))
        for k in list(deps.get("dependencies", {})) + list(deps.get("devDependencies", {})):
            if k.startswith("@workspace/"):
                t = "module:" + k.split("/")[1]
                if t in N: E[(src, t, "imports")] += 1
    edges = [{"source": s, "target": t, "type": k, "weight": w} for (s, t, k), w in sorted(E.items())]
    deg = collections.Counter(); [deg.update([e["source"], e["target"]]) for e in edges]
    out = {"nodes": [{k: v for k, v in n.items() if k != "pat"} | {"degree": deg[i]} for i, n in N.items()], "edges": edges,
           "coverage": {"chunks_scanned": seen, "docs": c.execute("select count(distinct path) from chunks").fetchone()[0], "isolated": [i for i in N if not deg[i]]}}
    json.dump(out, open(os.path.join(HERE, "graph.json"), "w"), indent=1)
    # mermaid: aggregate to top edges for readability
    top = sorted([e for e in edges if not e["source"].startswith("result:") or e["weight"] > 3], key=lambda e: -e["weight"])[:80]
    sid = lambda x: re.sub(r"\W", "_", x)
    L = ["flowchart LR"] + [f'  {sid(e["source"])}["{e["source"]}"] -->|{e["type"][0]}{e["weight"]}| {sid(e["target"])}["{e["target"]}"]' for e in top]
    open(os.path.join(HERE, "graph.mmd"), "w").write("\n".join(L) + "\n")
    return out
if __name__ == "__main__":
    o = build(); k = collections.Counter(n["kind"] for n in o["nodes"]); t = collections.Counter(e["type"] for e in o["edges"])
    print(json.dumps({"nodes": len(o["nodes"]), "by_kind": k, "edges": len(o["edges"]), "by_type": t, **{x: o["coverage"][x] for x in ("chunks_scanned", "docs")}, "isolated": len(o["coverage"]["isolated"])}))
