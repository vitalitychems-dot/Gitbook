#!/usr/bin/env python3
import sys,os,json,shutil,time; sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
gitenv(); B="/tmp/git72-q"; N=20; H=os.path.dirname(os.path.abspath(__file__))
shutil.rmtree(B,True); os.makedirs(f"{B}/seed/queue/open")
for i in range(N): json.dump({"file":f"f{i%4}.txt","line":f"fix {i}"},open(f"{B}/seed/queue/open/{i}.json","w"))
for i in range(4): open(f"{B}/seed/f{i}.txt","w").write("base\n")
sh("git init -q -b main && git add -A && git commit -qm seed",f"{B}/seed")
sh(f"git clone -q --bare {B}/seed {B}/hub.git && git clone -q {B}/hub.git {B}/w")
t=time.perf_counter(); done=0
while True:
    r=subprocess.run([f"{H}/worker.sh",f"{B}/w"],capture_output=True)
    if r.returncode==3: break
    r.check_returncode(); done+=1
off=time.perf_counter()-t
sh(f"git clone -q {B}/hub.git {B}/v"); res=len(os.listdir(f"{B}/v/results"))
lines=sum(open(f"{B}/v/f{i}.txt").read().count("fix") for i in range(4))
# online stub: 0.5s simulated API/LLM latency + 500 tokens/job (sleep scaled: 3 jobs measured, extrapolated)
t=time.perf_counter(); [time.sleep(0.5) for _ in range(3)]; on=(time.perf_counter()-t)/3*N
r={"jobs":N,"completed":done,"verified_results":res,"verified_lines":lines,"offline_s":round(off,2),
 "offline_jobs_per_s":round(done/off,1),"offline_tokens":0,"online_stub_s":round(on,2),"online_stub_tokens":500*N,
 "online_assumption":"0.5s + 500 tok per job (stub, not measured LLM)"}
shutil.rmtree(B); print(json.dumps(r))
