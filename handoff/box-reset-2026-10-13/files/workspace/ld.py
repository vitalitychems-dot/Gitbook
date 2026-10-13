import json,sys
def load(f):
    t=open(f).read()
    for s in range(len(t)):
        if t[s] in '[{':
            try: return json.JSONDecoder().raw_decode(t[s:])[0]
            except Exception: continue
