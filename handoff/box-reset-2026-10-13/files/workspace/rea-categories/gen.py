import json,csv,os,glob,re
BP='/workspace/build-plan-2026-10-12'
info=json.load(open('catinfo.json'))
rows=[l.rstrip('\n').split('\t') for f in ['picks.tsv','kpicks.tsv'] for l in open(f) if l.strip()]
def rea(r):
    p='rea/'+r.replace('/','__')+'.json'
    return json.load(open(p)) if os.path.exists(p) else {"status":"pending"}
def rea_str(d):
    if d.get('status')=='pending': return 'REA pending'
    if d.get('status')=='clone_failed': return 'clone failed'
    s=d.get('statistics',{})
    t=f"REA exit {d.get('exit')}: {s.get('parsed_javascript_files',0)} JS parsed, {s.get('findings',0)} findings, graph {d.get('nodes',0)}n/{d.get('edges',0)}e ({d.get('coverage')})"
    if d.get('exit')==124: t='REA timeout 420s (partial/none); '+t
    return t+f"; files {d.get('files_total','?')}, js/ts {d.get('js_ts_files','?')}, py {d.get('py_files','?')}"
# notes
os.makedirs('notes',exist_ok=True)
for c,r,st,lic,size,lang,arch,desc in rows:
    d=rea(r); i=info[c]
    open('notes/'+r.replace('/','__')+'.md','a' if False else 'w').write(f"# {r}\n\n- URL: https://github.com/{r}\n- Stars: {st} (GitHub API, 2026-10-12)\n- License: {lic}{' (archived)' if arch=='true' else ''}\n- Language: {lang}\n- Category: {c}\n- Description: {desc}\n- REA (MEASURED): {rea_str(d)}\n- Note: REA 6.4.0 analyses JS/TS only; non-JS repos show near-empty graphs — that is a tool limit, not repo quality.\n- Maps to TESSERA module: {i[0]}\n- Improves: {i[1]}\n- Metric: {i[2]} — {i[3]}\n")
# table
L=["# CATEGORY-REPOS — research for TESSERA next upgrade","","As of 2026-10-12 CT. Stars/licenses via GitHub API. **REA = MEASURED** (rea-agents@6.4.0 static JS/TS analysis on shallow clones). **All % are ESTIMATE** — no repo has been A/B tested against TESSERA's baseline yet; vendor claims labeled. Permissive = MIT/Apache/BSD/ISC/CC-BY/CC0; copyleft/NOASSERTION/NONE flagged for license review.",""]
L+=["| category | repo | stars | license | what it improves | metric + % | REA (MEASURED) |","|---|---|---:|---|---|---|---|"]
perm={'MIT','Apache-2.0','BSD-3-Clause','ISC','CC-BY-4.0','CC0-1.0','MPL-2.0'}
for c,r,st,lic,size,lang,arch,desc in rows:
    i=info[c]; d=rea(r)
    lf=lic if lic in perm else f"{lic} ⚠review"
    L.append(f"| {c} | [{r}](https://github.com/{r}) | {int(st):,} | {lf}{' (archived)' if arch=='true' else ''} | {i[1]} | {i[2]}: {i[3]} | {rea_str(d)} |")
open(BP+'/CATEGORY-REPOS.md','w').write('\n'.join(L)+'\n')
# graph
ents={};rels=set()
def E(n,t,obs):
    e=ents.setdefault(n,{"type":"entity","name":n,"entityType":t,"observations":[]})
    for o in obs:
        if o not in e["observations"]: e["observations"].append(o)
def R(a,t,b): rels.add((a,t,b))
for l in open(BP+'/v2-memory.jsonl'):
    o=json.loads(l)
    if o['type']=='entity': E(o['name'],o['entityType'],o.get('observations',[]))
    else: R(o['from'],o['relationType'],o['to'])
E('TESSERA_v2','project',['Full-picture graph built 2026-10-12: categories+knowledge+shepherd relay merged','Rule: Tessera reviews whole graph before any v3/v4 self-upgrade'])
mods=set()
for c,(m,imp,met,pct) in info.items():
    E('category:'+c,'category',[imp,f'metric {met}: {pct}'])
    for mm in re.split(r' \+ | / ',m):
        mm='module:'+mm.strip(); mods.add(mm); E(mm,'tessera_module',[]); R('category:'+c,'feeds',mm); R(mm,'part_of','TESSERA_v2')
for c,r,st,lic,size,lang,arch,desc in rows:
    d=rea(r)
    E('repo:'+r,'external_repo',[f'https://github.com/{r}',f'stars {st}',f'license {lic}',desc[:200],'REA: '+rea_str(d)])
    R('repo:'+r,'in_category','category:'+c)
for f in glob.glob(BP+'/rea-shards/*.md')+[BP+'/REA-COVERAGE-V2.md',BP+'/REA-RUN-LOG.md']:
    n='doc:'+os.path.basename(f); E(n,'document',[f]); R(n,'informs','TESSERA_v2')
for p in glob.glob(BP+'/REPO-IMPACT*')+glob.glob(BP+'/GLM-FLASH-REA.md'):
    n='doc:'+os.path.basename(p); E(n,'document',[p]); R(n,'informs','TESSERA_v2')
with open(BP+'/V2-FEATURE-MAP.csv') as fh:
    for row in csv.DictReader(fh):
        n='inventory:'+row['repo']; E(n,'inventory_repo',[f"include={row['include']}",f"license={row['license']}",f"category={row['capability_category']}",row['reason'][:150]])
        R(n,'mapped_by','doc:V2-FEATURE-MAP.csv')
E('doc:V2-FEATURE-MAP.csv','document',[BP+'/V2-FEATURE-MAP.csv']); R('doc:V2-FEATURE-MAP.csv','informs','TESSERA_v2')
for n,o in [('doc:KNOWLEDGE-CURRICULUM.md','Open knowledge load plan P1-P3 (ZIM/JSONL)'),('doc:SHEPHERD-RELAY.md','Design: gateway shepherds pull keyless open data, sign+encrypt, publish to Gitbook/GitMesh, sync via LAN/USB/LoRa'),('doc:CATEGORY-REPOS.md','Category research table'),('doc:FULL-PICTURE.md','Mermaid map')]:
    E(n,'document',[o]); R(n,'informs','TESSERA_v2')
E('module:Shepherd relay','tessera_module',['design only']); R('module:Shepherd relay','part_of','TESSERA_v2'); R('doc:SHEPHERD-RELAY.md','specifies','module:Shepherd relay')
R('module:Shepherd relay','publishes_to','module:Docs / GitMesh'); E('module:Docs / GitMesh','tessera_module',[])
for c in info:
    if c.startswith('k-'): R('doc:KNOWLEDGE-CURRICULUM.md','covers','category:'+c)
with open(BP+'/full-picture-memory.jsonl','w') as fh:
    for e in ents.values(): fh.write(json.dumps(e)+'\n')
    for a,t,b in sorted(rels): fh.write(json.dumps({"type":"relation","from":a,"to":b,"relationType":t})+'\n')
# mermaid
M=["# FULL-PICTURE — categories → TESSERA modules","","Source graph: `full-picture-memory.jsonl` (memory-MCP format). Rule: Tessera loads the whole graph before any v3/v4 self-upgrade.","","```mermaid","flowchart LR"]
ids={}
def nid(s): return ids.setdefault(s,'n%d'%len(ids))
for c,(m,_,_,_) in info.items():
    for mm in re.split(r' \+ | / ',m):
        M.append(f'  {nid("c"+c)}["{c}"] --> {nid("m"+mm.strip())}("{mm.strip()}")')
M.append(f'  {nid("mShepherd relay")}("Shepherd relay") --> {nid("mDocs / GitMesh")}')
for mm in sorted({x[1:] for x in ids if x.startswith("m")}): M.append(f'  {nid("m"+mm)} --> T[(TESSERA v2)]')
M+=['  V2[v2-memory + V2-FEATURE-MAP + REA shards] --> T','  T --> U{{v3 / v4 self-upgrade — only after full-graph review}}',"```"]
open(BP+'/FULL-PICTURE.md','w').write('\n'.join(M)+'\n')
print(len(ents),'entities',len(rels),'relations',len(rows),'rows')
# Gitbook ingest (excl archive/, history/, vault/1T/natal/token)
import subprocess
G='/workspace/gitmesh/repo'
files=subprocess.run(['git','-C',G,'ls-files','*.md'],capture_output=True,text=True).stdout.split()
bad=re.compile(r'vault|(^|[/_-])1t([/_.-]|$)|natal|token',re.I)
import fnmatch
EXC=['archive/moved/1T/*','*natal-vault.json','*/.local-data/*','*.replit','*/.env*','.env*','archive/moved/Zz/artifacts/z-app/data/ingest/*','history/recovered/source-documents/Zz/artifacts/z-app/data/ingest/*','archive/moved/Zz/artifacts/z-app/imports/objects/*','archive/moved/collink1007-XXX/tess/server/sol-wallet.ts','archive/moved/collink1007-XXX/tess/server/arbitrage-engine.ts','archive/moved/collink1007-XXX/tess/server/autonomous-trading-bots.ts','archive/moved/collink1007-XXX/tess/server/defi-realification.ts','archive/moved/collink1007-XXX/tess/server/pumpfun-trading-bot.ts','archive/moved/collink1007-XXX/x/tess/server/defi-realification.ts','*CredentialsPage.tsx','archive/moved/*/.vercel/*','archive/moved/collink1007-amber-flame-tiger-sand/artifacts/.tmp/*','*attached_assets/*','*pnpm-lock.yaml','*package-lock.json','*yarn.lock']
links=set(l.split('\t')[1] for l in subprocess.run(['git','-C',G,'ls-files','-s'],capture_output=True,text=True).stdout.splitlines() if l.startswith('120000'))
def excluded(f): return f in links or bad.search(f) or any(fnmatch.fnmatch(f,p) for p in EXC)
keep=[f for f in files if not excluded(f)]
EMAIL=re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
NATAL=re.compile(r'(natal|birth|born|dob|zodiac|ascendant)',re.I)
excl=len([f for f in subprocess.run(['git','-C',G,'ls-files'],capture_output=True,text=True).stdout.split() if excluded(f)])
E('Gitbook','repo',['vitalitychems-dot/Gitbook; pages ingested per memory-graph-inventory.md'])
R('Gitbook','informs','TESSERA_v2')
for f in keep:
    t=''
    try:
        for line in open(os.path.join(G,f),errors='ignore'):
            if line.startswith('#'): t=line.strip('# \n')[:120]; break
        t=EMAIL.sub('[email-redacted]',t)
        if NATAL.search(t): t='[natal-field-redacted]'
    except Exception: pass
    n='gitbook:'+f; E(n,'gitbook_page',[t or f]); R(n,'page_of','Gitbook')
    top=f.split('/')[0] if '/' in f else 'root'
    if top in ('mesh',): R(n,'informs','module:Offline mesh O1-O11')
E('Gitbook excluded paths (Security gate)','placeholder',[f'{excl} files excluded per GATE-GB-PR39-PR50-ARCHIVE-2026-10-12 EXCLUDE list + vault/1T/natal/token filter + symlinks; archive/ and history/ .md pages ingested (titles only, emails/natal redacted)'])
R('Gitbook excluded paths (Security gate)','part_of','Gitbook')
with open(BP+'/full-picture-memory.jsonl','w') as fh:
    for e in ents.values(): fh.write(json.dumps(e)+'\n')
    for a,t,b in sorted(rels): fh.write(json.dumps({"type":"relation","from":a,"to":b,"relationType":t})+'\n')
print('gitbook md pages',len(keep),'archive/history pages',len([f for f in keep if re.match(r'(archive|history)/',f)]),'excluded',excl,'| total',len(ents),'entities',len(rels),'relations')
E('model:zai-org/GLM-5.3-Flash','open_model',['https://huggingface.co/zai-org/GLM-5.3-Flash','MIT license (weights); released 2026-08-25','321.3B total / 18B active MoE, multimodal, FP8 ~328 GB; BF16 variant ~643 GB','Runs offline locally after download via vLLM/SGLang/KTransformers/llama.cpp GGUF (unsloth/GLM-5.3-Flash-GGUF community quant)','TESSERA fit: gateway/server node only (multi-GPU or large-RAM KTransformers); not edge nodes. For small offline nodes use zai-org/GLM-4.7-Flash (31.2B, MIT)'])
R('model:zai-org/GLM-5.3-Flash','code_repo','repo:zai-org/GLM-5'); R('model:zai-org/GLM-5.3-Flash','in_category','category:llms-open-inference'); R('model:zai-org/GLM-5.3-Flash','feeds','module:Compute lab')
E('model:zai-org/GLM-4.7-Flash','open_model',['https://huggingface.co/zai-org/GLM-4.7-Flash','MIT; 31.2B params; closest smaller GLM Flash for local nodes'])
R('model:zai-org/GLM-4.7-Flash','in_category','category:llms-open-inference')
with open(BP+'/full-picture-memory.jsonl','w') as fh:
    for e in ents.values(): fh.write(json.dumps(e)+'\n')
    for a,t,b in sorted(rels): fh.write(json.dumps({"type":"relation","from":a,"to":b,"relationType":t})+'\n')
print('final',len(ents),'entities',len(rels),'relations')
