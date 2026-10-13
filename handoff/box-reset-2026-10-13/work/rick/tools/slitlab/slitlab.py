"""slitlab: 10 interference / 5D-crystal experiments (numpy only, reuses qlab.qsim)."""
import sys, json, zlib, sqlite3, time, numpy as np
sys.path.insert(0,'/workspace/rick/qlab'); from qsim import SV
R=np.random.default_rng(7)

def i1_double_slit():
    lam,d,a,L=500e-9,50e-6,10e-6,1.0; x=np.linspace(-0.03,0.03,4001)
    th=x/L; env=np.sinc(a*th/lam)**2; ph=2*np.pi*d*th/lam
    coh=env*(1+np.cos(ph)); which=env*1.0  # which-path: intensities add, no cross term
    c=np.abs(x)<lam*L/d*1.5; env_c=env  # visibility measured on envelope-normalised pattern
    V=lambda I:((I/env_c)[c].max()-(I/env_c)[c].min())/((I/env_c)[c].max()+(I/env_c)[c].min())
    # partial which-path: distinguishability D -> visibility sqrt(1-D^2)
    part={D:V(env*(1+np.sqrt(1-D**2)*np.cos(ph))) for D in (0,0.5,0.9,1)}
    return dict(V_coherent=V(coh),V_whichpath=V(which),V_vs_D={str(k):round(v,4) for k,v in part.items()})

def i2_phase_knob():
    phi=np.linspace(0,np.pi,7); I=np.cos(phi/2)**2   # MZI output port
    # analog dot product: encode a_i,b_i in [0,1] as phases, read intensities with shot noise
    n,errs=16,[]
    for t in range(200):
        a,b=R.random(n),R.random(n); exact=a@b
        # amplitude modulators: set phase so transmitted amp = sqrt(a), then sqrt(b): I=a*b
        pa=2*np.arccos(np.sqrt(a)); pb=2*np.arccos(np.sqrt(b))
        pa+=R.normal(0,0.02,n); pb+=R.normal(0,0.02,n)  # 0.02 rad phase jitter
        I=np.cos(pa/2)**2*np.cos(pb/2)**2
        photons=R.poisson(I*1e4)/1e4
        errs.append(abs(photons.sum()-exact)/exact)
    return dict(phase_to_I=[round(v,4) for v in I.tolist()] if False else [round(float(v),4) for v in np.cos(phi/2)**2],
                dot_rel_err_mean=float(np.mean(errs)),dot_rel_err_p95=float(np.percentile(errs,95)),
                effective_bits=float(-np.log2(np.mean(errs))))

def grover(nq,mark):
    s=SV(nq).run([('H',[q]) for q in range(nq)]); N=2**nq
    k=int(np.floor(np.pi/4*np.sqrt(N)))
    for _ in range(k):
        s.v[mark]*=-1; s.v=2*s.v.mean()-s.v
    return k,float(abs(s.v[mark])**2)

def i3_grover():
    out=[]
    for nq in range(2,13):
        N=2**nq; k,p=grover(nq,N//3)
        out.append(dict(N=N,grover_queries=k,p_success=round(p,4),classical_queries_same_p=int(np.ceil(p*N)),classical_avg=(N+1)/2))
    return dict(table=out)

def mzi(phi): # 2x2: BS * phase * BS
    B=np.array([[1,1j],[1j,1]])/np.sqrt(2); return B@np.diag([np.exp(1j*phi),1])@B
def i4_mzi_gates():
    # logic: inputs x,y in {0,1} set phases phi = pi*(x+y)/k + bias; read port intensity, threshold 0.5
    def gate(f,bias,scale):
        ok=0
        for x in (0,1):
            for y in (0,1):
                out=abs((mzi(bias+scale*(x+y))@[1,0])[0])**2; ok+=(out>0.5)==f(x,y)
        return ok
    # |out0|^2 = sin^2(phi/2)
    res=dict(NOT=all((abs((mzi(np.pi*(1-x))@[1,0])[0])**2>0.5)==(1-x) for x in (0,1)),
             XOR=gate(lambda x,y:x^y,0,np.pi)==4, AND=gate(lambda x,y:x&y,0,0.4*np.pi)==4,
             OR=gate(lambda x,y:x|y,np.pi/3,np.pi/3)==4)
    # robustness: max phase error with all gates still correct
    tol=0
    for e in np.linspace(0,np.pi/2,91):
        good=all(gate(f,b+e,s)==4 and gate(f,b-e,s)==4 for f,b,s in [(lambda x,y:x^y,0,np.pi),(lambda x,y:x&y,0,0.4*np.pi),(lambda x,y:x|y,np.pi/3,np.pi/3)])
        if good: tol=e
        else: break
    res['phase_tolerance_rad']=round(float(tol),4); return res

def i5_nosignal():
    # Bell pair; Alice chooses measurement basis angle (her "slit setting"); Bob's marginal
    psi=np.array([1,0,0,1])/np.sqrt(2); rho=np.outer(psi,psi.conj()); bob=[]
    for th in np.linspace(0,np.pi,9):
        U=np.array([[np.cos(th/2),-np.sin(th/2)],[np.sin(th/2),np.cos(th/2)]])
        r=np.kron(U,np.eye(2))@rho@np.kron(U,np.eye(2)).T.conj()
        rB=r.reshape(2,2,2,2).trace(axis1=0,axis2=2); bob.append(float(rB[0,0].real))
    # mutual information between Alice's choice bit and Bob's outcome, sampled
    shots=200000; choice=R.integers(0,2,shots); pB0=np.array(bob)[[0,4]]
    out=(R.random(shots)>pB0[choice]).astype(int)
    def H(p): p=p[p>0]; return -(p*np.log2(p)).sum()
    joint=np.histogram2d(choice,out,bins=2)[0]/shots
    MI=H(joint.sum(1))+H(joint.sum(0))-H(joint.ravel())
    return dict(bob_P0_over_settings=[round(b,6) for b in bob],max_dev=float(np.ptp(bob)),MI_bits_sampled=float(MI))

def i6_grating():
    out=[]
    for N in (2,4,8,16,32):
        x=np.linspace(-0.5,0.5,8192); ph=2*np.pi*x
        I=np.abs(np.exp(1j*np.outer(np.arange(N),ph)).sum(0))**2
        peak_w=1/N  # main-lobe width in order units
        # capacity: N slits with phase settings -> N complex amplitudes; with M distinguishable phase levels -> N*log2 M bits/shot (classical), log2 N qubit-equivalent dims
        out.append(dict(N=N,peak_to_N2=round(float(I.max()/N**2),4),fwhm_orders=round(peak_w,4),bits_classical_8lvl=N*3,hilbert_dim=N,qubits_equiv=float(np.log2(N))))
    return dict(table=out)

def i7_optimizer():
    # cost: Max-Cut on random 8-node graph; "optical" = phase vector, intensity-based energy, annealed by phase noise
    n=8; W=np.triu((R.random((n,n))<0.5).astype(float),1); W=W+W.T
    cut=lambda s:0.25*np.sum(W*(1-np.outer(s,s)))
    best=max(cut(np.array([1 if (b>>i)&1 else -1 for i in range(n)])) for b in range(2**n))
    def optical(evals,seed):
        g=np.random.default_rng(seed); phi=g.uniform(0,2*np.pi,n); E=lambda p:-0.25*np.sum(W*(1-np.cos(p[:,None]-p[None,:])))
        e=E(phi); T=1.0; bestc=0
        for t in range(evals):
            q=phi+g.normal(0,0.5,n); eq=E(q)
            if eq<e or g.random()<np.exp((e-eq)/T): phi,e=q,eq
            T*=0.99; bestc=max(bestc,cut(np.sign(np.cos(phi))+(np.cos(phi)==0)))
        return bestc
    def rnd(evals,seed):
        g=np.random.default_rng(seed); return max(cut(g.choice([-1,1],n)) for _ in range(evals))
    res={}
    for ev in (10,30,100):
        o=[optical(ev,s)==best for s in range(200)]; r=[rnd(ev,s)==best for s in range(200)]
        res[str(ev)]=dict(optical_hit=float(np.mean(o)),random_hit=float(np.mean(r)))
    return dict(optimum=best,hit_rate_by_evals=res)

def i8_crystal():
    # published: Zhang et al. PRL 112,033901 (2014): 5D, ~360 TB per disc theoretical.
    # Project Silica (Anderson et al., SOSP 2023): voxel-based glass, ~7 TB in a 75x75x2 mm platter era.
    out=[]
    for no,nr in [(2,2),(4,4),(8,4),(8,8)]:
        bits=np.log2(no*nr); errs=0; trials=20000
        o=R.integers(0,no,trials); r=R.integers(0,nr,trials)
        ang=o*np.pi/no+R.normal(0,np.deg2rad(4),trials)   # slow axis in [0,pi)
        ret=(r+0.5)/nr+R.normal(0,0.04,trials)
        od=np.round(ang/(np.pi/no)).astype(int)%no; rd=np.clip(np.floor(ret*nr),0,nr-1).astype(int)
        ser=float(np.mean((od!=o)|(rd!=r)))
        # density at 0.5um x 0.5um x 2um voxel pitch (assumed)
        vox_cm3=1/(0.5e-4*0.5e-4*2e-4)
        out.append(dict(orient=no,retard=nr,bits_per_voxel=bits,symbol_err=round(ser,5),raw_TB_per_cm3=round(vox_cm3*bits/8/1e12,2)))
    return dict(table=out,assumptions="sigma 4deg orientation, 0.04 retardance; voxel pitch 0.5x0.5x2 um (assumed, not published value)")

H74G=np.array([[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
H74H=np.array([[1,0,1,0,1,0,1],[0,1,1,0,0,1,1],[0,0,0,1,1,1,1]])
def ham_enc(b): b=b.reshape(-1,4); return (b@H74G.T%2).ravel()
def ham_dec(c):
    c=c.reshape(-1,7).copy(); s=(c@H74H.T%2)@[1,2,4]
    for i,v in enumerate(s):
        if v: c[i,v-1]^=1
    return c[:,[2,4,5,6]].ravel()
GRAY=[0,1,3,2]
def i9_tessera_memory():
    db=sqlite3.connect('/workspace/rick/tools/palace/palace.db')
    txt="\n".join(r[0] for r in db.execute("select body from chunks order by id limit 200")).encode()
    comp=zlib.compress(txt,9); bits=np.unpackbits(np.frombuffer(comp,np.uint8))
    def store(b,sig_deg,sig_r):
        b=np.concatenate([b,np.zeros((-len(b))%4,np.uint8)]); s=b.reshape(-1,4)
        o=GRAY.index(0) if False else np.array([GRAY[v] for v in (s[:,0]*2+s[:,1])]); r=np.array([GRAY[v] for v in (s[:,2]*2+s[:,3])])
        ang=o*np.pi/4+R.normal(0,np.deg2rad(sig_deg),len(o)); ret=(r+0.5)/4+R.normal(0,sig_r,len(r))
        od=np.round(ang/(np.pi/4)).astype(int)%4; rd=np.clip(np.floor(ret*4),0,3).astype(int)
        inv=lambda v:np.array([GRAY.index(x) for x in v])
        oo,rr=inv(od),inv(rd); return np.stack([oo>>1,oo&1,rr>>1,rr&1],1).ravel().astype(np.uint8)
    res={}
    for sd,sr in [(4,0.04),(8,0.07),(10,0.09)]:
        raw=store(bits,sd,sr)[:len(bits)]; ber_raw=float(np.mean(raw!=bits))
        b4=np.concatenate([bits,np.zeros((-len(bits))%4,np.uint8)]); enc=ham_enc(b4)
        # interleave so voxel errors spread across codewords
        perm=R.permutation(len(enc)); rec=store(enc[perm],sd,sr)[:len(enc)]; unp=np.empty_like(rec); unp[perm]=rec
        dec=ham_dec(unp)[:len(bits)]; ber_ecc=float(np.mean(dec!=bits))
        try: ok=zlib.decompress(np.packbits(dec).tobytes())==txt
        except Exception: ok=False
        # block mode: 2 KB text blocks compressed independently -> errors stay local
        blocks=[txt[i:i+2048] for i in range(0,len(txt),2048)]; good=0
        for bl in blocks:
            cb=np.unpackbits(np.frombuffer(zlib.compress(bl,9),np.uint8)); cb4=np.concatenate([cb,np.zeros((-len(cb))%4,np.uint8)])
            e=ham_enc(cb4); pm=R.permutation(len(e)); rc=store(e[pm],sd,sr)[:len(e)]; u=np.empty_like(rc); u[pm]=rc
            try: good+=zlib.decompress(np.packbits(ham_dec(u)[:len(cb)]).tobytes())==bl
            except Exception: pass
        res[f"sig{sd}deg_{sr}"]=dict(ber_raw=ber_raw,ber_hamming74=ber_ecc,whole_archive_exact=ok,blocks_2KB_recovered=round(good/len(blocks),4))
    return dict(text_bytes=len(txt),compressed_bytes=len(comp),ratio=round(len(txt)/len(comp),2),voxels_raw=int(np.ceil(len(bits)/4)),voxels_ecc=int(np.ceil(len(bits)/4*7/4)),noise=res)

def i10_palace_grover():
    db=sqlite3.connect('/workspace/rick/tools/palace/palace.db')
    rows=[r[0] for r in db.execute("select path from chunks order by id limit 1024")]
    N=len(rows); nq=int(np.log2(N)); N=2**nq; rows=rows[:N]
    target=next(i for i,p in enumerate(rows) if 'qlab' in p or 'INVENTIONS' in p)
    k,p=grover(nq,target)
    # classical: oracle checks one path per query; expected queries over random targets
    return dict(N=N,target_path=rows[target],grover_queries=k,grover_p=round(p,4),classical_expected=(N+1)/2,classical_worst=N,
                note="simulated amplitudes; real wall-clock here is classical (statevector costs O(N) per step)")

ALL=[i1_double_slit,i2_phase_knob,i3_grover,i4_mzi_gates,i5_nosignal,i6_grating,i7_optimizer,i8_crystal,i9_tessera_memory,i10_palace_grover]
if __name__=='__main__':
    out={}
    for f in ALL:
        t=time.time(); out[f.__name__]=f(); out[f.__name__]['sec']=round(time.time()-t,3)
    json.dump(out,open('results.json','w'),indent=1,default=float); print(json.dumps(out,indent=1,default=float))
