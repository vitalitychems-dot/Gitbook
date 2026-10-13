#!/usr/bin/env python3
"""Fetch public USGS M4.5+ events (5y, compact: date,lat,lon,mag) and GFZ Kp daily history. Small files only."""
import urllib.request, csv, io, os, datetime, json
H=os.path.dirname(os.path.abspath(__file__)); D=os.path.join(H,"data")
U="https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime={s}&endtime={e}&minmagnitude=4.5&orderby=time-asc"
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"tessera-simons/1"}),timeout=180).read().decode()
def quakes(end="2026-10-13", years=5):
    e=datetime.date.fromisoformat(end); rows=[]
    for y in range(years*2,0,-1):  # half-year chunks (<20k limit)
        s=e-datetime.timedelta(days=183*y); t=e-datetime.timedelta(days=183*(y-1))
        for r in csv.DictReader(io.StringIO(get(U.format(s=s,e=t)))):
            rows.append((r["time"][:10],round(float(r["latitude"]),2),round(float(r["longitude"]),2),float(r["mag"] or 4.5)))
    rows=sorted(set(rows))
    with open(os.path.join(D,"quakes.csv"),"w") as f:
        f.write("date,lat,lon,mag\n"); f.writelines(f"{a},{b},{c},{d}\n" for a,b,c,d in rows)
    return len(rows)
def kp():
    t=get("https://kp.gfz-potsdam.de/app/files/Kp_ap_Ap_SN_F107_since_1932.txt"); out={}
    for l in t.splitlines():
        if l.startswith("#") or not l.strip(): continue
        p=l.split()
        if int(p[0])<2021: continue
        d=f"{p[0]}-{int(p[1]):02d}-{int(p[2]):02d}"; k=[float(x) for x in p[7:15]]
        if min(k)<0: continue
        out[d]=[round(sum(k),3), float(p[23]) if len(p)>23 else -1]  # daily Kp sum, Ap
    json.dump(out,open(os.path.join(D,"kp_daily.json"),"w")); return len(out)
if __name__=="__main__": print(quakes(), kp())
