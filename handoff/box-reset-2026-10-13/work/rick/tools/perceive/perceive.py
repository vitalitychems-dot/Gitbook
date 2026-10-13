"""Classical CV anomaly detector: flags blurry / low-detail / warped blocks. numpy+PIL only."""
import numpy as np, json, sys
from PIL import Image
B=16
def gray(a): return a[...,:3].astype(float)@[.299,.587,.114] if a.ndim==3 else a.astype(float)
def conv3(g,k):
    p=np.pad(g,1,mode='edge');o=np.zeros_like(g)
    for i in range(3):
        for j in range(3): o+=k[i][j]*p[i:i+g.shape[0],j:j+g.shape[1]]
    return o
def blocks(x,f):
    H,W=x.shape[0]//B,x.shape[1]//B
    return f(x[:H*B,:W*B].reshape(H,B,W,B).swapaxes(1,2).reshape(H,W,B*B),-1)
def features(g):
    lap=conv3(g,[[0,1,0],[1,-4,1],[0,1,0]])
    gx=conv3(g,[[-1,0,1],[-2,0,2],[-1,0,1]]);gy=conv3(g,[[-1,-2,-1],[0,0,0],[1,2,1]])
    mag=np.hypot(gx,gy); edge=(mag>np.percentile(mag,75)).astype(float)
    lv=blocks(lap,np.var); ed=blocks(edge,np.mean)
    jxx=blocks(gx*gx,np.mean);jyy=blocks(gy*gy,np.mean);jxy=blocks(gx*gy,np.mean)
    coh=np.sqrt((jxx-jyy)**2+4*jxy**2)/(jxx+jyy+1e-9)
    return lv,ed,coh
def rz(x):
    m=np.median(x);s=np.median(abs(x-m))*1.4826+1e-9;return (x-m)/s
def score(g,mode='combined'):
    lv,ed,coh=features(g); l=np.log(lv+1e-6)
    if mode=='laplacian': return -rz(l)
    return np.maximum.reduce([-rz(l),-rz(ed),rz(coh)])
def detect(g,mode='combined',t=3.0): return score(g,mode)>t
def inpaint(a,mask,iters=300):
    a=a.astype(float).copy();m=np.kron(mask,np.ones((B,B)))>0
    m=np.pad(m,((0,a.shape[0]-m.shape[0]),(0,a.shape[1]-m.shape[1])))
    for _ in range(iters):
        p=np.pad(a,((1,1),(1,1))+((0,0),)*(a.ndim-2),mode='edge')
        avg=(p[:-2,1:-1]+p[2:,1:-1]+p[1:-1,:-2]+p[1:-1,2:])/4; a[m]=avg[m]
    return a.clip(0,255).astype(np.uint8)
def annotate(a,s,mask,out):
    rgb=a[...,:3] if a.ndim==3 else np.stack([a]*3,-1)
    h=np.kron(np.clip(s/6,0,1),np.ones((B,B)));h=np.pad(h,((0,rgb.shape[0]-h.shape[0]),(0,rgb.shape[1]-h.shape[1])))
    o=rgb.astype(float);o[...,0]=o[...,0]*(1-h*.6)+255*h*.6;o[...,1]*=1-h*.4;o[...,2]*=1-h*.4
    for (i,j) in zip(*np.nonzero(mask)):
        o[i*B,j*B:(j+1)*B]=o[(i+1)*B-1,j*B:(j+1)*B]=[255,255,0];o[i*B:(i+1)*B,j*B]=o[i*B:(i+1)*B,(j+1)*B-1]=[255,255,0]
    Image.fromarray(o.astype(np.uint8)).save(out)
if __name__=='__main__':
    src,pre=sys.argv[1],sys.argv[2]
    a=np.array(Image.open(src).convert('RGB'));g=gray(a);s=score(g);m=s>3
    annotate(a,s,m,pre+'_heatmap.png');Image.fromarray(inpaint(a,m)).save(pre+'_inpaint.png')
    json.dump({'image':src,'block':B,'shape':a.shape[:2],'flagged_blocks':int(m.sum()),'total_blocks':int(m.size),
      'regions':[{'x':int(j*B),'y':int(i*B),'w':B,'h':B,'score':round(float(s[i,j]),2)} for i,j in zip(*np.nonzero(m))][:500]},open(pre+'.json','w'),indent=1)
    print(int(m.sum()),'/',m.size,'blocks flagged')
