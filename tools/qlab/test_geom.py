import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import bhnmc_geometry as g; from geomcheck import *
E={n:(x,y) for n,x,y in g.E}; res=[]
seal=check_seal(E,21,23); res.append(('corner electrodes on O-ring 21-23mm',sorted(seal)==['E01','E08','E57','E64'],seal))
ps=check_seal(g.ports,21,23); res.append(('both fluid ports on seal',len(ps)==2,ps))
off=check_outside(g.M,25); res.append(('4 coils off 50mm board (centre r>25)',len(off)==4,off))
cov=mux_coverage(64,2,16); res.append(('dual 16:1 mux covers only 32/64',cov==(False,32),cov))
cov4=mux_coverage(64,4,16); res.append(('4x16:1 covers 64',cov4==(True,64),cov4))
mc=min_clearance(g.M,E); res.append(('coil-electrode min centre dist 3.18mm',abs(mc[0]-3.18)<0.01,tuple(round(x,2) if isinstance(x,float) else x for x in mc)))
for n,ok,i in res: print('PASS' if ok else 'FAIL',n,i)
