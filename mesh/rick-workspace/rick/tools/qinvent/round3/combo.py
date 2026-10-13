import json
from tokens import *
HD=hits_for(DEV);HT=hits_for(TEST)
f=lambda xs,H:evalb(xs,[free_energy(x["q"],dedup_lines(valve(x["q"],h[:5])),1.5) for x,h in zip(xs,H)])
R={"dev":f(DEV,HD),"test":f(TEST,HT)};json.dump(R,open("results/combo_2_5.json","w"));print(R)
