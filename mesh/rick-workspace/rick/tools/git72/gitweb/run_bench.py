#!/usr/bin/env python3
import sys,os,json,shutil; sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
gitenv(); S="/tmp/git72-site"; O="/tmp/git72-out"; P=20
make_site(S,P); shutil.rmtree(O,ignore_errors=True); os.makedirs(O)
sh(f"tar --exclude=.git -cf {O}/site.tar -C {S} ."); sh(f"git bundle create -q {O}/site.bundle --all",S)
sh(f"zstd -q -19 {O}/site.bundle -o {O}/site.bundle.zst")
sz={k:du(f"{O}/{k}") for k in ["site.tar","site.bundle","site.bundle.zst"]}
def untar(): shutil.rmtree(f"{O}/a",True); os.makedirs(f"{O}/a"); sh(f"tar -xf {O}/site.tar -C {O}/a")
def clone(): shutil.rmtree(f"{O}/b",True); sh(f"git clone -q {O}/site.bundle {O}/b")
def zclone(): shutil.rmtree(f"{O}/c",True); sh(f"zstd -dqf {O}/site.bundle.zst -o {O}/u.bundle && git clone -q {O}/u.bundle {O}/c")
t={"site.tar":timed(untar),"site.bundle":timed(clone),"site.bundle.zst":timed(zclone)}
# incremental: 1 new page -> delta bundle fetched into existing clone
open(f"{S}/page20.md","w").write("# new\n"); sh("git add -A && git commit -qm new",S)
sh(f"git bundle create -q {O}/delta.bundle main ^HEAD~1",S)
dt=timed(lambda: sh(f"git fetch -q {O}/delta.bundle main:refs/remotes/usb/main",f"{O}/b"),3)
ok=sh(f"git -C {O}/b rev-parse refs/remotes/usb/main").strip()==sh("git rev-parse HEAD",S).strip()
r={"pages":P,"bytes":sz,"bytes_per_page":{k:round(v/P) for k,v in sz.items()},"sync_ms":t,
   "delta_bundle_bytes":du(f"{O}/delta.bundle"),"delta_fetch_ms":dt,"delta_ok":ok,"tokens":0}
shutil.rmtree(S); shutil.rmtree(O); print(json.dumps(r))
