import numpy as np
P=[-15.75+4.5*i for i in range(8)]
E=[(f"E{r*8+c+1:02d}",P[c],P[7-r]) for r in range(8) for c in range(8)]
M={"M1":(-18,18),"M2":(0,20),"M3":(18,18),"M4":(20,0),"M5":(18,-18),"M6":(0,-20),"M7":(-18,-18),"M8":(-20,0)}
ports={"inlet":(-22,0),"outlet":(22,0)}
if __name__=="__main__":
    print("|ID|X mm|Y mm|r mm|"); print("|-|-|-|-|")
    for n,x,y in E: print(f"|{n}|{x:+.2f}|{y:+.2f}|{np.hypot(x,y):.2f}|")
    rs=[np.hypot(x,y) for _,x,y in E]
    print("\nmax electrode r",round(max(rs),2),"; electrodes with r>21 (O-ring inner):",sum(r>21 for r in rs))
    for m,(x,y) in M.items():
        d=min(np.hypot(x-ex,y-ey) for _,ex,ey in E); print(m,"r=%.2f"%np.hypot(x,y),"nearest electrode center %.2f mm"%d)
    for p,(x,y) in ports.items():
        d=min(np.hypot(x-ex,y-ey) for _,ex,ey in E); print(p,"r=22 (O-ring 21-23 => on seal) nearest electrode %.2f"%d)
    print("Z stack",1.5+2+4+2+3)
