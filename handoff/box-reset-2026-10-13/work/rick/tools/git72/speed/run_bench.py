#!/usr/bin/env python3
import sys,os,json,shutil; sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
gitenv(); S="/tmp/git72-sp/src"; O="/tmp/git72-sp"; F="page07.md"
make_site(S,20); sh("git config uploadpack.allowFilter true && git config uploadpack.allowAnySHA1InWant true",S)
want=open(f"{S}/{F}").read(); res={}
def run(name,fn,land):
    ms=timed(lambda:(shutil.rmtree(land,True),fn()),5); ok=open(f"{land}/{F}").read()==want if os.path.isdir(land) else False
    res[name]={"ms":ms,"bytes_landed":du(land),"ok":ok,"tokens":0}
run("A_full_clone",lambda:sh(f"git clone -q file://{S} {O}/A"),f"{O}/A")
run("B_blobless_sparse",lambda:sh(f"git clone -q --filter=blob:none --no-checkout file://{S} {O}/B && git -C {O}/B sparse-checkout set --no-cone /{F} && git -C {O}/B checkout -q main"),f"{O}/B")
run("C_git_archive_path",lambda:(os.makedirs(f"{O}/C"),sh(f"git archive main {F} | tar -x -C {O}/C",S)),f"{O}/C")
run("C2_cat_file",lambda:(os.makedirs(f"{O}/C2"),sh(f"git -C {S} cat-file -p main:{F} > {O}/C2/{F}")),f"{O}/C2")
ms=timed(lambda:open(f"{S}/{F}").read(),5); res["D_cat_worktree"]={"ms":ms,"bytes_landed":0,"ok":True,"tokens":0}
shutil.rmtree(O); print(json.dumps(res))
