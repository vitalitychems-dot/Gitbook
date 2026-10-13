"""W vs GHZ: entanglement left after losing 1 qubit (trace out). numpy only."""
import numpy as np,json
def ghz(n): v=np.zeros(2**n);v[0]=v[-1]=2**-.5;return v
def w(n): v=np.zeros(2**n);[v.__setitem__(1<<k,n**-.5) for k in range(n)];return v
def ptrace_last(v,n):
    t=v.reshape(2**(n-1),2);return t@t.conj().T
def ptranspose(r,n,k):  # transpose qubit block: first k qubits vs rest
    d=2**k;e=r.shape[0]//d;return r.reshape(d,e,d,e).transpose(2,1,0,3).reshape(r.shape)
def negativity(r,n,k): ev=np.linalg.eigvalsh(ptranspose(r,n,k));return float(-ev[ev<0].sum())
def trace_to_two(r,n):  # keep first 2 qubits
    m=2**(n-2);t=r.reshape(4,m,4,m);return np.einsum('aibi->ab',t)
def concurrence(r):
    Y=np.array([[0,0,0,-1],[0,0,1,0],[0,1,0,0],[-1,0,0,0]]);R=r@Y@r.conj()@Y
    l=np.sqrt(np.abs(np.sort(np.linalg.eigvals(R).real)[::-1]));return float(max(0,l[0]-l[1]-l[2]-l[3]))
out={}
for n in (3,4,5):
    for name,f in (('W',w),('GHZ',ghz)):
        r=ptrace_last(f(n),n);m=n-1
        out[f'{name}{n}']={'negativity_1|rest_after_loss':round(negativity(r,m,1),4),
          'pair_concurrence_after_loss':round(concurrence(trace_to_two(r,m)) if m>2 else concurrence(r),4),
          'surviving_qubits':m}
print(json.dumps(out,indent=1));json.dump(out,open('results.json','w'),indent=1)
