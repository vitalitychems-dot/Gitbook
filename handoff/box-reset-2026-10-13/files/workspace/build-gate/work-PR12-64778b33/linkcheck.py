import json,re,posixpath,sys
files=json.load(open('meta/files.json'))
tree=json.load(open('meta/head-tree.json'))['tree']
paths={x['path'] for x in tree}
link_re=re.compile(r'(?<!\!)\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)|!\[[^\]]*\]\(([^)\s]+)\)')
checked=[];broken=[];external=0;anchors=0
for f in files:
    fn=f['filename']; d=posixpath.dirname(fn)
    for ln in f.get('patch','').split('\n'):
        if not ln.startswith('+') or ln.startswith('+++'): continue
        for m in link_re.finditer(ln[1:]):
            tgt=m.group(2) or m.group(3)
            if re.match(r'^[a-z]+:',tgt) or tgt.startswith('//'): external+=1; continue
            if tgt.startswith('#'): anchors+=1; continue
            p=tgt.split('#')[0].split('?')[0]
            from urllib.parse import unquote
            p=unquote(p)
            full=posixpath.normpath(posixpath.join(d,p)) if not p.startswith('/') else p.lstrip('/')
            ok = full in paths
            checked.append((fn,tgt,full,ok))
            if not ok: broken.append((fn,tgt,full))
print('added-line relative links checked:',len(checked),'broken:',len(broken),'external:',external,'anchor-only:',anchors)
for b in broken: print('BROKEN',b)
for c in checked: print(('OK ' if c[3] else 'BAD'),c[0],'->',c[1],'=>',c[2])
