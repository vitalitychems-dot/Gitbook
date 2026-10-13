"""Space+time trail composite: synthetic moving objects, exponential-decay trail, depth shading. numpy+PIL."""
import numpy as np,time,json
from PIL import Image
H,W,T=360,640,48
yy,xx=np.mgrid[:H,:W]
def frame(t):
    img=np.zeros((H,W,3));dep=np.full((H,W),np.inf)
    for k,(z,col) in enumerate([(1.,(255,90,40)),(2.,(40,200,255)),(3.5,(180,255,80))]):
        cx=W/2+(W/2.6)*np.cos(t*.13+k*2)/z*1.5; cy=H/2+(H/3)*np.sin(t*.2+k)/z*1.2; r=40/z
        m=((xx-cx)**2+(yy-cy)**2<r*r)&(z<dep); img[m]=col; dep[m]=z
    return img,dep
def composite(decay=0.9,shade=True):
    acc=np.zeros((H,W,3));t0=time.time()
    for t in range(T):
        f,d=frame(t)
        if shade: f=f*np.where(np.isinf(d),0,1/(1+0.35*(d-1)))[...,None]
        w=decay**(T-1-t);acc=np.maximum(acc,f*w)   # max-blend keeps trails crisp, newest brightest
    return acc.clip(0,255).astype(np.uint8),time.time()-t0
def naive():
    t0=time.time();fs=[frame(t)[0] for t in range(T)];return np.mean(fs,0).astype(np.uint8),time.time()-t0
if __name__=='__main__':
    a,ta=composite();Image.fromarray(a).save('sample_trail_depth.png')
    b,tb=naive();Image.fromarray(b).save('baseline_mean.png')
    c=lambda x:float(x.astype(float).std())
    r={'frames':T,'res':f'{W}x{H}','trail_ms':round(ta*1000,1),'mean_baseline_ms':round(tb*1000,1),
       'contrast_std_trail':round(c(a),1),'contrast_std_mean':round(c(b),1)}
    print(json.dumps(r,indent=1));json.dump(r,open('results.json','w'),indent=1)
