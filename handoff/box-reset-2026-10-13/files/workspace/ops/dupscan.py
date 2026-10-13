import os,hashlib,json,sys
roots=['/workspace','/home/box']
EXD={'.git','node_modules'}
def skip(p):
    l=p.lower()
    return ('1t' in p.split('/') or '/1T' in p or 'natal-vault' in l or p.startswith('/home/box/agent-data') or p.startswith('/cursor/stores')
            or any(x in l for x in ['chrome','chromium','mozilla','firefox','browser-profile','.cache/ms-playwright']))
by={}
for r in roots:
  for d,ds,fs in os.walk(r):
    if skip(d): ds[:]=[];continue
    ds[:]=[x for x in ds if x not in EXD and not skip(os.path.join(d,x))]
    for f in fs:
      p=os.path.join(d,f)
      try:
        if os.path.islink(p) or not os.path.isfile(p):continue
        s=os.path.getsize(p)
      except: continue
      if s>0: by.setdefault(s,[]).append(p)
groups=[]
for s,ps in by.items():
  if len(ps)<2:continue
  h={}
  for p in ps:
    try:
      m=hashlib.sha256()
      with open(p,'rb') as fh:
        for c in iter(lambda:fh.read(1<<20),b''):m.update(c)
      h.setdefault(m.hexdigest(),[]).append(p)
    except: pass
  for k,v in h.items():
    if len(v)>1:
      v=sorted(set(v))
      if len(v)>1: groups.append((s,k,v))
def rank(p):
  pr=0 if p.startswith('/workspace/improvements') or p.startswith('/workspace/ops') else 1
  try:mt=-os.path.getmtime(p)
  except:mt=0
  return (pr,mt,len(p))
out=[]
for s,k,v in groups:
  v=sorted(v,key=rank); out.append({'size':s,'sha':k,'keep':v[0],'remove':v[1:],'free':s*(len(v)-1)})
out.sort(key=lambda g:-g['free'])
json.dump(out,open('/workspace/ops/box-dups.json','w'))
print(len(out),sum(len(g['remove'])+1 for g in out),sum(g['free'] for g in out))
