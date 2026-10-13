import os,glob,time,gzip,lzma,hashlib,io,base64,json,zstandard as Z
from PIL import Image
G='/workspace/einstein/charter/gb'
md=[p for p in glob.glob(G+'/**/*.md',recursive=True) if os.path.isfile(p) and not os.path.islink(p)]
docs_files=[open(p,'rb').read() for p in md]
docs=b''.join(docs_files)[:40_000_000]
jl=sorted(set(glob.glob('/workspace/rick/src/Gitbook/**/*.jsonl',recursive=True)))
jl=[p for p in jl if os.path.isfile(p)]
logs=b''.join(open(p,'rb').read() for p in jl)[:20_000_000]
graph=open('/workspace/rick/tools/fullpicture/graph.json','rb').read()
def t(f,d):
    s=time.perf_counter();o=f(d);return len(o),time.perf_counter()-s
algs={'gzip-6':lambda d:gzip.compress(d,6),'xz-6':lambda d:lzma.compress(d,preset=6),
 'zstd-3':lambda d:Z.ZstdCompressor(level=3).compress(d),'zstd-19':lambda d:Z.ZstdCompressor(level=19).compress(d),
 'zstd-3-long':lambda d:Z.ZstdCompressor(compression_params=Z.ZstdCompressionParameters.from_level(3,enable_ldm=True,window_log=27)).compress(d)}
def png(d):
    n=(len(d)+2)//3; w=1024; h=(n+w-1)//w; buf=d+b'\0'*(w*h*3-len(d))
    b=io.BytesIO(); Image.frombytes('RGB',(w,h),buf).save(b,'PNG',optimize=False,compress_level=9); return b.getvalue()
algs['png-pixels']=png
def delta(d):  # store only change vs previous line: (shared prefix len, shared suffix len, middle)
    out=[];prev=b''
    for ln in d.split(b'\n'):
        p=0;m=min(len(ln),len(prev))
        while p<m and ln[p]==prev[p]: p+=1
        s=0
        while s<m-p and ln[-1-s]==prev[-1-s]: s+=1
        out.append(b'%d,%d,'%(p,s)+ln[p:len(ln)-s]);prev=ln
    return Z.ZstdCompressor(level=19).compress(b'\n'.join(out))
def rle(d):
    out=bytearray();i=0
    while i<len(d):
        j=i
        while j<len(d) and j-i<255 and d[j]==d[i]: j+=1
        out+=bytes((j-i,d[i]));i=j
    return bytes(out)
rows=[]
for name,d in [('docs-md',docs),('jsonl-logs',logs),('graph.json',graph)]:
    for a,f in list(algs.items())+[('delta-lines+zstd19',delta),('RLE-only',rle),('RLE+zstd19',lambda d:Z.ZstdCompressor(level=19).compress(rle(d)))]:
        if a=='RLE-only' and len(d)>5e6: d2=d[:5_000_000]
        else: d2=d
        n,s=t(f,d2); rows.append((name,a,len(d2),n,len(d2)/n,len(d2)/1e6/s))
# content-addressed dedup on whole files
u={hashlib.sha256(b).digest():b for b in docs_files}
tot=sum(map(len,docs_files));uniq=sum(map(len,u.values()))
cz=Z.ZstdCompressor(compression_params=Z.ZstdCompressionParameters.from_level(3,enable_ldm=True,window_log=27))
uz=len(cz.compress(b''.join(u.values())[:400_000_000]))
rows.append(('docs-md(all %d files)'%len(docs_files),'CAS-dedup',tot,uniq,tot/uniq,0))
rows.append(('docs-md(all files)','CAS-dedup+zstd3-long',tot,uz,tot/uz,0))
# base-N encodings: size of representing the zstd output
z=Z.ZstdCompressor(level=19).compress(graph)
for nm,enc in [('base64',base64.b64encode(z)),('base85',base64.b85encode(z)),('base3-trits(ASCII)',None),('base256(raw)',z)]:
    if enc is None:
        n=int.from_bytes(z,'big');tr=[];
        import math; L=math.ceil(len(z)*8/math.log2(3)); rows.append(('graph.json zstd19 out',nm,len(z),L,len(z)/L,0)); continue
    rows.append(('graph.json zstd19 out',nm,len(z),len(enc),len(z)/len(enc),0))
print('| data | method | in bytes | out bytes | ratio | MB/s |\n|-|-|-|-|-|-|')
for r in rows: print('| %s | %s | %d | %d | %.2fx | %s |'%(r[0],r[1],r[2],r[3],r[4],('%.1f'%r[5]) if r[5] else '-'))
print('files',len(md),'jsonl',len(jl))
