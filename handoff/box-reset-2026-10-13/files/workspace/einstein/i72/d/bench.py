import json,random,math,zlib,hashlib,difflib,statistics as S,collections as C
from datetime import datetime as D,timedelta as TD
import zstandard as Z
random.seed(7)
def ci(x,f=S.mean,n=5000):
  b=sorted(f(random.choices(x,k=len(x))) for _ in range(n));return "%.3g [%.3g,%.3g]"%(f(x),b[n//40],b[-n//40])
R={}
# 2 page diff + dict
W=json.load(open('wiki2.json'));pairs=[(v[1][1],v[0][1]) for v in W.values() if len(v)==2]
full=[len(Z.ZstdCompressor(level=19).compress(n.encode())) for o,n in pairs]
def delta(o,n):
  d=''.join(difflib.unified_diff(o.splitlines(1),n.splitlines(1),n=0));return len(Z.ZstdCompressor(level=19).compress(d.encode()))
dl=[delta(o,n) for o,n in pairs]
# dict trained leave-one-out on other old pages (fair: receiver has old corpus)
dd=[]
for i,(o,n) in enumerate(pairs):
  samp=[x[0].encode()[j:j+4096] for k,x in enumerate(pairs) if k!=i for j in range(0,len(x[0]),4096)]
  dic=Z.train_dictionary(16384,samp);dd.append(len(Z.ZstdCompressor(level=19,dict_data=dic).compress(n.encode())))
R['2_full_zstd_B']=ci(full,S.median);R['2_delta_zstd_B']=ci(dl,S.median);R['2_dict_full_B']=ci(dd,S.median)
R['2_ratio_full/delta']=ci([f/d for f,d in zip(full,dl)],S.median)
# 3 hash-only: msg sent as 32B hash if exact body seen before, else zstd body
M=[json.loads(l) or '' for l in open('comments.jsonl')];seen=set();b0=[];b1=[]
for m in M:
  h=hashlib.sha256(m.encode()).digest();z=len(Z.ZstdCompressor(level=19).compress(m.encode()))
  b0.append(z);b1.append(32 if h in seen else z);seen.add(h)
R['3_hits']="%d/%d"%(sum(a!=b for a,b in zip(b0,b1)),len(M));R['3_mean_B_before']=ci(b0);R['3_mean_B_after']=ci(b1)
# 4 residual entropy on CI conclusions (chronological)
seq=[l.split('\t')[2] or 'running' for l in reversed(open('runs.tsv').read().splitlines())]
def H(x):
  c=C.Counter(x);n=len(x);return -sum(v/n*math.log2(v/n) for v in c.values())
res=['0' if a==b else b for a,b in zip(seq,seq[1:])]
R['4_H_raw_bits']=H(seq[1:]);R['4_H_resid_bits']=H(res)
blk=[(seq[i:i+50]) for i in range(0,len(seq)-51,50)]
R['4_ratio']=ci([H(b[1:])/max(H(['0' if a==c else c for a,c in zip(b,b[1:])]),1e-9) for b in blk],S.median)
# 1 heartbeat: polling every 5 min (60B msg) vs send only on state change + absence alarm
ch=sum(a!=b for a,b in zip(seq,seq[1:]));t=[D.fromisoformat(l.split('\t')[0][:-1]) for l in open('runs.tsv')]
days=(max(t)-min(t)).total_seconds()/86400
R['1_bytes_day_poll']=86400/300*60;R['1_bytes_day_absence']=round(ch/days*60,1);R['1_days']=round(days,2)
# 5 quiet backoff: fixed 5-min cron vs backoff 5->cap 30, reset on push
P=sorted(D.fromisoformat(l.strip()[:-1]) for l in open('pushes.txt'));s,e=P[0],P[-1]
def sim(cap):
  ticks=0;lat=[];now=s;iv=5;pi=0
  while now<e:
    now+=TD(minutes=iv);ticks+=1;new=[p for p in P[pi:] if p<=now]
    if new: lat+= [(now-p).total_seconds()/60 for p in new];pi+=len(new);iv=5
    else: iv=min(iv*2,cap)
  return ticks/((e-s).total_seconds()/86400),lat
f,lf=sim(5);b,lb=sim(30)
R['5_runs_day_fixed']=round(f,1);R['5_runs_day_backoff']=round(b,1);R['5_lat_fixed_min']=ci(lf);R['5_lat_backoff_min']=ci(lb);R['5_lat_backoff_max']=max(lb)
print(json.dumps(R,indent=0))
