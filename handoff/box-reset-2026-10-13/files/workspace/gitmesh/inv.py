import subprocess,os,re,collections
R='.';out=[]
head=subprocess.check_output(['git','rev-parse','HEAD']).decode().strip()
files=subprocess.check_output(['git','ls-files']).decode().splitlines()
fs=set(files)
last={}
log=subprocess.check_output(['git','log','--format=@@%h %cs','--name-only']).decode(errors='replace')
cur=None
for l in log.splitlines():
    if l.startswith('@@'): cur=l[2:]
    elif l and l not in last: last[l]=cur
def cat(p):
    t=p.split('/')[0];pl=p.lower()
    if 'handoff' in pl: return 'handoff'
    if re.search(r'(^|/)(log|.*-log|.*_log)\.(md|txt|jsonl)$',pl) or pl.endswith('.jsonl') or '/logs/' in pl: return 'log'
    return {'intake':'intake','review':'review','merge':'merge','mesh':'mesh','history':'log' if pl.endswith('.md') and 'coordination' in pl else 'other',
            'posts':'page','forum':'page','brain':'page','brain-consciousness':'research','operations':'page','state':'other'}.get(t, 'page' if p.endswith('.md') and '/' not in p else 'other')
def purpose(p):
    if p.endswith(('.md','.txt')):
        try:
            for l in open(p,errors='replace'):
                l=l.strip().lstrip('#').strip()
                if l and l!='---': return l[:90].replace('|','/')
        except: pass
    ext=os.path.splitext(p)[1] or 'file'
    return f'{ext} asset in {os.path.dirname(p) or "root"}'
summ=open('SUMMARY.md').read()
linkre=re.compile(r'\]\(([^)#\s]+)')
broken=[];refs=collections.defaultdict(set)
extre=re.compile(r'(?:github\.com/)?\b(collin-keane/[\w.-]+|vitalitychems-dot/[\w.-]+)|\b(TESSERA|REA-[\w-]+|HYB-\d+|GB-\d+)\b')
mds=[f for f in files if f.endswith('.md')]
for f in mds:
    try: t=open(f,errors='replace').read()
    except: continue
    for m in extre.finditer(t): refs[f].add(m.group(1) or m.group(2))
    for l in linkre.findall(t):
        if re.match(r'^[a-z]+:',l): continue
        tgt=os.path.normpath(os.path.join(os.path.dirname(f),l.split('?')[0]))
        if tgt not in fs and not any(x.startswith(tgt+'/') for x in ()) and not os.path.isdir(tgt): broken.append((f,l))
summlinks={os.path.normpath(l) for l in linkre.findall(summ)}
nonarch=[f for f in mds if not f.startswith(('archive/','history/'))]
orph=[f for f in nonarch if f not in summlinks and f!='SUMMARY.md']
ho=[f for f in files if re.search(r'handoff|(^|/)log\.md$|-log\.md$|^history/coordination/|^intake/',f,re.I)]
cc=collections.Counter(cat(f) for f in files)
import datetime
w=open('../memory-graph-inventory.md','w')
w.write(f"# Gitbook memory-graph inventory (READ-ONLY)\n\n- Repo: vitalitychems-dot/Gitbook, main @ `{head}`\n- Generated: {datetime.datetime.now():%Y-%m-%d %H:%M} CT\n- Files: {len(files)}; categories: {dict(cc)}\n\n")
w.write("## 5. Gaps (summary first)\n\n")
w.write(f"### Orphan pages (non-archive/history .md not in SUMMARY.md): {len(orph)}\n"+''.join(f"- {o}\n" for o in orph)+"\n")
w.write(f"### Broken internal links: {len(broken)}\n"+''.join(f"- {a} -> `{b}`\n" for a,b in broken)+"\n")
w.write(f"## 3. Handoff and log files ({len(ho)})\n\n"+''.join(f"- {h}\n" for h in ho)+"\n")
allr=collections.Counter(r for s in refs.values() for r in s)
w.write("## 4. External repos / REA / item references\n\n### Totals\n"+''.join(f"- {k}: {v} files\n" for k,v in allr.most_common())+"\n### Per file\n"+''.join(f"- {f}: {', '.join(sorted(s))}\n" for f,s in sorted(refs.items()) if s)+"\n")
w.write("## 2. File table\n\n|path|category|size|last commit|date|purpose|\n|---|---|---|---|---|---|\n")
for f in files:
    sh,dt=(last.get(f) or '? ?').split()
    w.write(f"|{f}|{cat(f)}|{os.path.getsize(f) if os.path.exists(f) else '?'}|{sh}|{dt}|{purpose(f)}|\n")
print(len(files),len(orph),len(broken),len(ho),allr.most_common(12))
print(broken[:15]);print(orph[:20])
