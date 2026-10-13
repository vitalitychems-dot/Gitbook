import os, subprocess, time, json, shutil, statistics
def sh(c, cwd=None): return subprocess.run(c, shell=True, cwd=cwd, check=True, capture_output=True, text=True).stdout
def du(p):
    t=0
    for r,_,fs in os.walk(p):
        for f in fs:
            fp=os.path.join(r,f)
            if not os.path.islink(fp): t+=os.path.getsize(fp)
    return t if os.path.isdir(p) else os.path.getsize(p)
def timed(fn, n=5):
    ts=[]
    for _ in range(n):
        t=time.perf_counter(); fn(); ts.append((time.perf_counter()-t)*1000)
    return round(statistics.median(ts),2)
def gitenv():
    os.environ.update(GIT_AUTHOR_NAME="b",GIT_AUTHOR_EMAIL="b@x",GIT_COMMITTER_NAME="b",GIT_COMMITTER_EMAIL="b@x")
def make_site(d, pages=20):
    shutil.rmtree(d, ignore_errors=True); os.makedirs(d); sh("git init -q -b main", d)
    for i in range(pages):
        ext="md" if i%2 else "html"
        open(f"{d}/page{i:02}.{ext}","w").write(f"# Page {i}\n\n"+("Gitbook mesh note line %d. "%i)*30+"\n[next](page%02d)\n"%(i+1))
        if i%5==4: sh(f"git add -A && git commit -qm 'pages to {i}'", d)
    open(f"{d}/data.csv","w").write("id,node,latency_ms\n"+"".join(f"{i},n{i%7},{i*3%97}\n" for i in range(300)))
    sh("git add -A && git commit -qm data", d)
