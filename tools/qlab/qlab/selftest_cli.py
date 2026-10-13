import subprocess,sys,json,os,tempfile
here=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); out=os.path.join(here,'cli_example_output.json')
r=subprocess.run([sys.executable,'-m','qlab','optimize','examples/aqft5.json','--device','qlab/devices/props_nairobi.json','--out',out],cwd=here,capture_output=True,text=True)
print(r.stderr.strip()); d=json.load(open(out))
ok=r.returncode==0 and d['best_layout']['twin_fidelity']>=d['naive_layout']['twin_fidelity']
print(('PASS' if ok else 'FAIL'),'CLI optimize aqft5 on nairobi', d['best_layout']['twin_fidelity'], d['naive_layout']['twin_fidelity'])
