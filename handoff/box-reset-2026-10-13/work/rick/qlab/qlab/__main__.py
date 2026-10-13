"""python3 -m qlab optimize <circuit.json> --device <calib.json> [--out out.json] [--no-twin]
   python3 -m qlab test [--full]
circuit.json: {"n":3,"gates":[["H",[0]],["CNOT",[0,1]],["CP",[1,2],0.785]]}  (also "QFT"/"AQFT" macro: ["AQFT",[n,m]])"""
import sys,os,json,argparse,subprocess,time
import qlab  # noqa: path setup
import numpy as np
def load_circ(p):
    d=json.load(open(p)); n=d['n']; c=[]
    from aqft import aqft
    for g in d['gates']:
        if g[0] in ('QFT','AQFT'): c+=aqft(g[1][0],g[1][1] if g[0]=='AQFT' else g[1][0])
        else: c.append((g[0],list(g[1]))+tuple(g[2:]))
    return n,c
def optimize(args):
    from calib import load; from route import route,best_layouts; from twin import run,esp
    from qopt import optimize as v1; from qopt2 import lower; from qopt3 import optimize3; import qnoise2
    from qsim import SV
    t0=time.time(); n,c=load_circ(args.circuit); dev=load(args.device); L=lower(c)
    if n<=8:
        psi=SV(n).run(L).v; sc=lambda x:qnoise2.fidelity(n,x,psi)
        o,_=optimize3(lower(v1(L)),sc)
    else: o=lower(v1(L))
    o=[g if g[0]!='CZ' else g for g in o]
    def stats(x): return dict(gates=len(x),twoq=sum(len(g[1])==2 for g in x))
    from route import connected_subsets
    naive=tuple(sorted(connected_subsets(dev,n,limit=1)[0]))
    def pred(lay):
        rc,ph,sw,fin=route(dev,lay,o); out=dict(layout=list(lay),swaps=sw,esp=float(esp(dev,ph,rc)),routed=stats(rc),final_positions=fin)
        if n<=8 and not args.no_twin:
            p=SV(n).run(rc).v; out['twin_fidelity']=float(np.real(p.conj()@run(dev,ph,rc,n)@p))
        return out,rc
    nv,_=pred(naive); cands=[pred(l[1]) for l in best_layouts(dev,o,n,top=3)]
    key='twin_fidelity' if 'twin_fidelity' in nv else 'esp'
    best,brc=max(cands,key=lambda z:z[0][key])
    res=dict(device=dev['name'],calibration_source=dev['source'],n=n,input=stats(L),optimized=stats(o),
             naive_layout=nv,best_layout=best,optimized_circuit=[list(g[:2])+list(g[2:]) for g in o],
             routed_circuit=[list(g[:2])+list(g[2:]) for g in brc],seconds=round(time.time()-t0,2),
             note='twin_fidelity = state fidelity from |0..0> under the calibrated twin (no readout). Predicted, not measured on hardware.')
    s=json.dumps(res,default=lambda x:list(x) if isinstance(x,tuple) else float(x),indent=1)
    (open(args.out,'w').write(s) if args.out else print(s))
    print(f"[qlab] {dev['name']}: gates {res['input']['gates']}->{res['optimized']['gates']}, 2q {res['input']['twoq']}->{res['optimized']['twoq']}; "
          f"{key} naive {nv[key]:.4f} -> best layout {best['layout']} {best[key]:.4f} (swaps {nv['swaps']}->{best['swaps']})",file=sys.stderr)
def test(args):
    here=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tests=['test_sim.py','test_opt.py','test_noise.py','test_geom.py','test_opt2.py','test_opt3.py','qlab/selftest_twin.py','qlab/selftest_cli.py']
    if args.full: tests+=['test_aqft_avg.py']
    env=dict(os.environ,OMP_NUM_THREADS='1'); bad=0
    for t in tests:
        t0=time.time(); r=subprocess.run([sys.executable,t],cwd=here,env=env,capture_output=True,text=True)
        fails=r.stdout.count('FAIL')+r.stdout.count('pass=False'); ok=r.returncode==0 and fails==0; bad+=not ok
        print(f"{'OK  ' if ok else 'FAIL'} {t} ({time.time()-t0:.1f}s){'' if ok else ' :: '+(r.stderr or r.stdout)[-400:]}")
    print('ALL PASS' if not bad else f'{bad} FAILED'); sys.exit(1 if bad else 0)
ap=argparse.ArgumentParser(prog='qlab'); sp=ap.add_subparsers(dest='cmd',required=True)
o=sp.add_parser('optimize'); o.add_argument('circuit'); o.add_argument('--device',required=True); o.add_argument('--out'); o.add_argument('--no-twin',action='store_true'); o.set_defaults(f=optimize)
t=sp.add_parser('test'); t.add_argument('--full',action='store_true'); t.set_defaults(f=test)
a=ap.parse_args(); a.f(a)
