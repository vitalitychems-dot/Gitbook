"""Layout enumeration and SWAP routing on a coupling map."""
import itertools,collections
from calib import neighbors
from twin import esp
def connected_subsets(dev,n,limit=400):
    nb=neighbors(dev); seen=set(); out=[]
    frontier=[frozenset([q]) for q in nb]
    for size in range(1,n):
        nxt=set()
        for s in frontier:
            for q in s:
                for m in nb[q]-s: nxt.add(s|{m})
        frontier=list(nxt)
    return sorted(frontier,key=sorted)[:limit]
def path(nb,allowed,a,b):
    prev={a:None}; dq=collections.deque([a])
    while dq:
        x=dq.popleft()
        if x==b: break
        for y in nb[x]:
            if y in allowed and y not in prev: prev[y]=x; dq.append(y)
    p=[b]
    while prev[p[-1]] is not None: p.append(prev[p[-1]])
    return p[::-1]
def route(dev,layout,c):
    """layout[l]=physical qubit of logical l. Returns (circuit on positions 0..n-1, phys list, swaps).
    Positions are indices into phys=layout(initial); SWAP = 3 CNOT on coupled positions."""
    nb=neighbors(dev); phys=list(layout); pos={p:i for i,p in enumerate(phys)}
    l2p=dict(enumerate(layout)); out=[]; swaps=0; allowed=set(phys)
    for g in c:
        if len(g[1])==2:
            a,b=g[1]
            while frozenset((l2p[a],l2p[b])) not in dev['edges']:
                pth=path(nb,allowed,l2p[a],l2p[b]); x,y=pth[0],pth[1]
                i,j=pos[x],pos[y]; out+=[('CNOT',[i,j]),('CNOT',[j,i]),('CNOT',[i,j])]; swaps+=1
                inv={v:k for k,v in l2p.items()}; la,lb=inv.get(x),inv.get(y)
                if la is not None: l2p[la]=y
                if lb is not None: l2p[lb]=x
            out.append((g[0],[pos[l2p[q]] for q in g[1]])+tuple(g[2:]))
        else: out.append((g[0],[pos[l2p[g[1][0]]]])+tuple(g[2:]))
    final={l:pos[p] for l,p in l2p.items()}
    return out,phys,swaps,final
def best_layouts(dev,c,n,top=3,perm_limit=24):
    cands=[]
    for s in connected_subsets(dev,n):
        for perm in itertools.islice(itertools.permutations(sorted(s)),perm_limit):
            rc,phys,sw,fin=route(dev,perm,c); cands.append((esp(dev,phys,rc),perm,sw))
    cands.sort(key=lambda x:-x[0]); return cands[:top]
