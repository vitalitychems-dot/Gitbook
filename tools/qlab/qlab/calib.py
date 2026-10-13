"""Load device calibration. Accepts IBM backend-properties JSON (qiskit-ibm-runtime fake_provider props_*.json) or qlab's own simple format:
{"name":..,"qubits":[{"T1":us,"T2":us,"readout_p01":..,"readout_p10":..,"e1q":..,"t1q":ns}], "edges":[[a,b,e2q,t2q_ns],...]}"""
import json
def load(path):
    d=json.load(open(path))
    if 'backend_name' in d: return from_ibm(d)
    q=d['qubits']; edges={}
    for a,b,e,t in d['edges']: edges[frozenset((a,b))]=(e,t)
    return dict(name=d.get('name',path),qubits=q,edges=edges,source=d.get('source','user file'))
def from_ibm(d):
    qs=[]
    for plist in d['qubits']:
        p={x['name']:x['value'] for x in plist}
        qs.append(dict(T1=p['T1'],T2=min(p['T2'],2*p['T1']),readout_p01=p.get('prob_meas1_prep0',p['readout_error']),
                       readout_p10=p.get('prob_meas0_prep1',p['readout_error']),e1q=None,t1q=None,ex=None))
    edges={}
    for g in d['gates']:
        par={x['name']:x['value'] for x in g['parameters']}
        if g['gate']=='sx': qs[g['qubits'][0]]['e1q']=par['gate_error']; qs[g['qubits'][0]]['t1q']=par['gate_length']
        if g['gate']=='x': qs[g['qubits'][0]]['ex']=par['gate_error']
        if g['gate']=='cx':
            k=frozenset(g['qubits']); e,t=par['gate_error'],par['gate_length']
            if e>=1: continue  # IBM marks broken couplers with error 1
            if k not in edges or e<edges[k][0]: edges[k]=(e,t)
    return dict(name=d['backend_name'],qubits=qs,edges=edges,source='IBM backend properties '+d.get('last_update_date',''))
def neighbors(dev):
    nb={i:set() for i in range(len(dev['qubits']))}
    for k in dev['edges']: a,b=tuple(k); nb[a].add(b); nb[b].add(a)
    return nb
