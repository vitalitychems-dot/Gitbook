"""Headless Chrome input-event tests for eye4.html (CDP). Run: python3 test_v4.py [--offline]"""
import sys,os,json,time,subprocess,socket,urllib.request,http.server,threading,re
H=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(H,"vendor"));import websocket
ONLINE="--offline" not in sys.argv
def port():
    s=socket.socket();s.bind(("127.0.0.1",0));p=s.getsockname()[1];s.close();return p
hp=port();os.chdir(os.path.dirname(H))
srv=http.server.ThreadingHTTPServer(("127.0.0.1",hp),lambda *a:http.server.SimpleHTTPRequestHandler(*a,directory=os.path.dirname(H)) if False else type("Q",(http.server.SimpleHTTPRequestHandler,),{"log_message":lambda *x:None})(*a))
threading.Thread(target=srv.serve_forever,daemon=True).start()
cp=port();prof="/tmp/eye4-chrome"
ch=subprocess.Popen(["google-chrome","--headless=new","--no-sandbox","--disable-gpu",f"--remote-debugging-port={cp}",f"--user-data-dir={prof}","--window-size=1280,800","about:blank"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
for _ in range(150):
    try: tabs=json.load(urllib.request.urlopen(f"http://127.0.0.1:{cp}/json"));break
    except Exception: time.sleep(.2)
ws=websocket.create_connection([t for t in tabs if t["type"]=="page"][0]["webSocketDebuggerUrl"],timeout=60,suppress_origin=True);i=0
def cdp(m,**p):
    global i;i+=1;ws.send(json.dumps({"id":i,"method":m,"params":p}))
    while True:
        r=json.loads(ws.recv())
        if r.get("id")==i: return r.get("result",{})
def ev(x): return cdp("Runtime.evaluate",expression=x,returnByValue=True,awaitPromise=True)["result"].get("value")
def mouse(t,x,y,**k): cdp("Input.dispatchMouseEvent",type=t,x=x,y=y,**k)
def wait_tiles(n0,timeout=20):
    t=time.time()
    while time.time()-t<timeout:
        if ev("document.querySelectorAll('#m img.t').length && [...document.querySelectorAll('#m img.t')].filter(i=>i.style.display!='none').every(i=>i.complete)")and ev("T4.loads.length")>n0: break
        time.sleep(.2)
    return time.time()-t
R={};ok=[]
def check(name,cond,val): ok.append((name,bool(cond),val));print(("PASS" if cond else "FAIL"),name,val)
cdp("Page.enable");cdp("Emulation.setDeviceMetricsOverride",width=1280,height=800,deviceScaleFactor=1,mobile=False)
lat,lon=41.8827,-87.6233  # Chicago Loop (Millennium Park)
cdp("Page.navigate",url=f"http://127.0.0.1:{hp}/v4/eye4.html?lat={lat}&lon={lon}&z=4"+("&online=1" if ONLINE else ""));time.sleep(2)
# DRAG: 300px right, 200px down in 10 steps
c0=ev("T4.center()");mouse("mousePressed",640,400,button="left",clickCount=1)
for k in range(1,11): mouse("mouseMoved",640+30*k,400+20*k,button="left",buttons=1)
mouse("mouseReleased",940,600,button="left",clickCount=1);c1=ev("T4.center()")
dpx=ev(f"(()=>{{const a=ll2p({c0[0]},{c0[1]},T4.z),b=ll2p({c1[0]},{c1[1]},T4.z);return[a[0]-b[0],a[1]-b[1]]}})()")
check("drag moves map by exactly the pointer delta (300,200 px)",abs(dpx[0]-300)<1 and abs(dpx[1]-200)<1,dpx)
ev(f"T4.setView({lat},{lon},4)")
# WHEEL ZOOM at center 4->19 via 15 wheel events
z=[]
for k in range(15): mouse("mouseWheel",640,400,deltaX=0,deltaY=-100);z.append(ev("T4.z"))
cc=ev("T4.center()");check("wheel zooms 4->19 in 15 events, keeps point under cursor",z[-1]==19 and abs(cc[0]-lat)<1e-4 and abs(cc[1]-lon)<1e-4,{"z":z[-1],"center":cc})
mpp=ev("T4.mpp()");R["z19_m_per_px"]=mpp
# zoom-out reversibility
for k in range(2): mouse("mouseWheel",640,400,deltaX=0,deltaY=100)
check("wheel out",ev("T4.z")==17,ev("T4.z"));
for k in range(2): mouse("mouseWheel",640,400,deltaX=0,deltaY=-100)
# CLICK an event marker: put a quake under the cursor
ev(f"T4.setView(T4.events[0].la,T4.events[0].lo,6)");mouse("mousePressed",640,400,button="left",clickCount=1);mouse("mouseReleased",640,400,button="left",clickCount=1)
cl=ev("T4.clicks.at(-1)");txt=ev("info.textContent")
check("click on marker opens its details",cl and cl["hit"] and cl["hit"] in txt,cl)
mouse("mousePressed",100,700,button="left",clickCount=1);mouse("mouseReleased",100,700,button="left",clickCount=1)
check("click on empty map reports coordinates",ev("T4.clicks.at(-1).hit")is None and re.match(r"-?\d+\.\d{5}, ",ev("info.textContent")),ev("info.textContent")[:40])
check("refresh interval is 5 minutes",ev("T4.REFRESH_MS")==300000,ev("T4.REFRESH_MS"))
if ONLINE:
    # TILE LOAD TIMING at city zoom (fresh cache: unique zooms)
    for name,zz in (("esri",19),("usgs",16),("gibs",8)):
        ev(f"T4.base='{name}';T4.loads=[];T4.fail=0;T4.setView({lat},{lon},{zz})");t=wait_tiles(0)
        L=ev(f"T4.loads.filter(l=>l.z=={zz}&&l.k.startsWith('{name}/')).map(l=>l.ms)");L.sort()
        R[f"{name}_z{zz}"]={"tiles":len(L),"fail":ev("T4.fail"),"median_ms":round(L[len(L)//2]) if L else None,"p95_ms":round(L[int(len(L)*.95)-1]) if L else None,"screen_full_s":round(t,2)}
        check(f"{name} z{zz} tiles stream with no failures",L and ev("T4.fail")==0,R[f"{name}_z{zz}"])
    ev(f"T4.base='esri';T4.loads=[];T4.setView({lat},{lon},18)");wait_tiles(0);ev(f"T4.setView({lat},{lon},19)");wait_tiles(0)
    for _ in range(40):
        if ev("T4.refreshes.length"): break
        time.sleep(.5)
    rf=ev("T4.refreshes[0]");R["refresh"]=rf;check("live feed refresh pulled USGS+EONET",rf and rf["n"]>50,rf)
    cdp("Emulation.setDefaultBackgroundColorOverride");shot=cdp("Page.captureScreenshot",format="png")["data"]
    import base64;open(os.path.join(H,"shot4.png"),"wb").write(base64.b64decode(shot));R["shot_bytes"]=os.path.getsize(os.path.join(H,"shot4.png"))
    # STREET: KartaView via click
    ev("document.getElementById('street').checked=true");mouse("mousePressed",640,400,button="left",clickCount=1);mouse("mouseReleased",640,400,button="left",clickCount=1)
    for _ in range(90):
        if ev("T4.streetMs!==undefined"): break
        time.sleep(.5)
    R["kartaview"]={"photos":ev("T4.street.length"),"ms":ev("T4.streetMs"),"fields":ev("T4.street[0]?Object.keys(T4.street[0]):[]")}
    check("KartaView keyless photos near click, only position/date/image fields",R["kartaview"]["photos"]>0 and set(R["kartaview"]["fields"])<={"la","lo","dt","th","img"},R["kartaview"])
h=open(os.path.join(H,"eye4.html")).read()
code=open(os.path.join(H,"template4.html")).read();bad=re.findall(r"\b(flights?|ships?|ais|adsb|cctv|license|plates?|faces?|recogni\w+)\b",code.split("<script>")[1],re.I)
check("no remote scripts; no tracking terms in page code",not re.search(r"<script[^>]+src=",h) and not bad,bad)
ch.terminate();json.dump({"checks":ok,"metrics":R},open(os.path.join(H,"test_results.json"),"w"),indent=1)
print(f"{sum(o[1] for o in ok)}/{len(ok)} pass");print(json.dumps(R,indent=1));sys.exit(0 if all(o[1] for o in ok) else 1)
