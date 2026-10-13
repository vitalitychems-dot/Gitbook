import json,sys,collections
p=sys.argv[1]; last=None
with open(p,'rb') as f:
    for line in f:
        if line.startswith(b'{"rea_progress"'): continue
        if line.strip(): last=line
out={"status":"no_result"}
if last:
    try:
        d=json.loads(last); n=d.get("normalized_result") or d
        g=n.get("graph",{}) or {}
        nodes=g.get("nodes",[]) or []; edges=g.get("edges",[]) or []
        kc=collections.Counter(x.get("kind","?") for x in nodes)
        st=n.get("statistics") or {}
        cov=(g.get("coverage") or {}).get("status")
        out={"status":"ok","statistics":st,"nodes":len(nodes),"edges":len(edges),"coverage":cov,"kinds":dict(kc.most_common(10))}
    except Exception as e: out={"status":"parse_error","err":str(e)[:200]}
print(json.dumps(out))
