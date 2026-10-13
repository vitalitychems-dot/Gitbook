import sys,subprocess,collections
# input: lines "mode sha\tpath"; output root tree sha built with git mktree --missing
ents=[l.rstrip('\n') for l in open(sys.argv[1]) if l.strip()]
tree=collections.defaultdict(list); dirs=set([''])
for l in ents:
    ms,p=l.split('\t'); m,s=ms.split()
    parts=p.split('/')
    for i in range(1,len(parts)): dirs.add('/'.join(parts[:i]))
    tree['/'.join(parts[:-1])].append((m,'blob',s,parts[-1]))
def build(d):
    items=list(tree[d])
    for sd in sorted(x for x in dirs if x and ('/'.join(x.split('/')[:-1]))==d):
        items.append(('040000','tree',build(sd),sd.split('/')[-1]))
    inp=''.join(f"{m} {t} {s}\t{n}\n" for m,t,s,n in items)
    return subprocess.run(['git','mktree','--missing'],input=inp,capture_output=True,text=True,check=True,cwd=sys.argv[2]).stdout.strip()
print(build(''))
