import re,json,os
H=os.path.dirname(os.path.abspath(__file__))
d=json.loads(re.search(r"const D=(\{.*?\});\n",open(os.path.join(H,"..","v3","eye3.html")).read(),re.S).group(1))
D={"t0":d["t0"],"events":d["events"],"fires":d["fires"],"sources":d["sources"]}
html=open(os.path.join(H,"template4.html")).read().replace("__DATA__",json.dumps(D,separators=(",",":")))
open(os.path.join(H,"eye4.html"),"w").write(html);print(len(html),"bytes",len(D["events"]),"events")
