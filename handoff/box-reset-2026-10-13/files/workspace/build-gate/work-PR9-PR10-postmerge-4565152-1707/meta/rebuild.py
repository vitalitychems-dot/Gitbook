import sys,subprocess,collections
repo=sys.argv[1]; listing=sys.argv[2]
ents={}
for l in open(listing):
    l=l.rstrip('\n')
    if not l: continue
    mb,p=l.split('\t',1); m,b=mb.split()
    ents[p]=(m,b)
def mk(lines):
    return subprocess.run(['git','-C',repo,'mktree','--missing'],input=''.join(lines),capture_output=True,text=True,check=True).stdout.strip()
tree=lambda: collections.defaultdict(tree)
root={}
for p,(m,b) in ents.items():
    parts=p.split('/'); d=root
    for x in parts[:-1]: d=d.setdefault(x,{})
    d[parts[-1]]=(m,b)
out={}
def build(d,prefix):
    lines=[]
    for k,v in d.items():
        if isinstance(v,dict):
            s=build(v,prefix+k+'/'); lines.append(f"040000 tree {s}\t{k}\n")
        else: lines.append(f"{v[0]} blob {v[1]}\t{k}\n")
    s=mk(lines); out[prefix.rstrip('/') or '<root>']=s; return s
build(root,'')
for k in sorted(out): print(out[k],k)
