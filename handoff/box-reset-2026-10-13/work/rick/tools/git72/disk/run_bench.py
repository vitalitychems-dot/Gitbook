#!/usr/bin/env python3
"""Bench autoclean dedup scope + archive step on a tiny fixture. Mirrors the jdupes calls used in /workspace/ops/autoclean.sh."""
import sys,os,json,shutil; sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
gitenv(); D="/tmp/git72-disk"; shutil.rmtree(D,True); os.makedirs(D)
def real(p): return int(sh(f"du -sB1 {p}").split()[0])  # counts hardlinks once
def fixture():
    shutil.rmtree(f"{D}/fx",True); make_site(f"{D}/fx/r1",20)
    sh(f"git -C {D}/fx/r1 repack -q -d"); # mixed: a pack + new loose objects
    open(f"{D}/fx/r1/extra.md","w").write("x"*4000); sh("git add -A && git commit -qm extra",f"{D}/fx/r1")
    for i in (2,3): sh(f"cp -a {D}/fx/r1 {D}/fx/r{i}")   # independent copies (like separate network clones)
    return real(f"{D}/fx")
r={}
b=fixture(); sh(f"jdupes -L -q {D}/fx/r*/.git/objects/pack || true"); r["old_packs_only"]={"before":b,"after":real(f"{D}/fx")}
b=fixture(); sh(f"hardlink -q -f {D}/fx/r*/.git/objects || true"); r["new_hardlink_objects"]={"before":b,"after":real(f"{D}/fx")}
for k in r: r[k]["saved"]=r[k]["before"]-r[k]["after"]
ok=all(sh(f"git -C {D}/fx/r{i} fsck --no-progress 2>&1; echo $?").strip().endswith("0") for i in (1,2,3)); r["fsck_ok_after_new"]=ok
# archive step (unchanged): tar vs zstd -19 --long=27
os.makedirs(f"{D}/w"); make_site(f"{D}/w/site",20); shutil.rmtree(f"{D}/w/site/.git")
sh(f"tar -C {D}/w -cf {D}/a.tar site && zstd -q -19 --long=27 {D}/a.tar -o {D}/a.tar.zst")
r["archive"]={"dir_bytes":real(f"{D}/w"),"tar":du(f"{D}/a.tar"),"tar_zst19":du(f"{D}/a.tar.zst")}
shutil.rmtree(D); print(json.dumps(r))
