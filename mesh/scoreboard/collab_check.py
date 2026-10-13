#!/usr/bin/env python3
import re,sys,json
H=re.compile(r"^HANDOFF [A-Za-z0-9_.-]+ (PASS|FAIL) (https://github\.com/\S+/pull/\d+|-) [\w.@%-]+=[-\d.]+->[-\d.]+ by=\S+$")
def check_handoff(l): return bool(H.match(l.strip()))
def check_prop(l):
    try: d=json.loads(l)
    except Exception: return False
    return {"id","by","goal","idea"}<=d.keys()
if __name__=="__main__":
    bad=0
    for p in sys.argv[1:]:
        f=check_prop if p.endswith(".jsonl") else check_handoff
        for i,l in enumerate(open(p),1):
            if l.strip() and not f(l): print(f"{p}:{i}: bad line");bad+=1
    sys.exit(1 if bad else 0)
