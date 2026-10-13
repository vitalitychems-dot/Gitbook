import numpy as np,time,json
from perceive import *
rng=np.random.default_rng(0)
def blur(x,k=7):
    for _ in range(k): x=conv3(x,[[1/9]*3]*3)
    return x
res={m:{'tp':0,'fp':0,'fn':0} for m in ['laplacian','combined']}
for trial in range(20):
    img=blur(rng.normal(128,40,(256,256)),1)+rng.normal(0,8,(256,256)); truth=np.zeros((16,16),bool)
    for kind in ['blur','flat','warp']*2:
        i,j=rng.integers(0,15,2)*16; p=img[i:i+32,j:j+32]
        if kind=='blur': img[i:i+32,j:j+32]=blur(p.copy(),6)
        elif kind=='flat': img[i:i+32,j:j+32]=p.mean()+rng.normal(0,1,p.shape)
        else: img[i:i+32,j:j+32]=128+60*np.sin(np.arange(32)/2.0)[None,:]+rng.normal(0,8,p.shape)  # stretched/smeared stripes
        truth[i//16:i//16+2,j//16:j//16+2]=True
    for m in res:
        d=detect(img,m);r=res[m];r['tp']+=int((d&truth).sum());r['fp']+=int((d&~truth).sum());r['fn']+=int((~d&truth).sum())
for m,r in res.items():
    r['precision']=round(r['tp']/max(1,r['tp']+r['fp']),3);r['recall']=round(r['tp']/max(1,r['tp']+r['fn']),3)
    r['f1']=round(2*r['precision']*r['recall']/max(1e-9,r['precision']+r['recall']),3)
t=time.time();detect(img);res['ms_per_256px']=round((time.time()-t)*1000,1)
print(json.dumps(res,indent=1));json.dump(res,open('synth_results.json','w'),indent=1)
