"""Headless Chrome tests for eye5.html. Run: python3 test_v5.py [--offline]"""
import sys, os, json, time, subprocess, socket, urllib.request, http.server, threading, re, base64
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, "..", "v4", "vendor"))
import websocket
ONLINE = "--offline" not in sys.argv

def port():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); p = s.getsockname()[1]; s.close(); return p

hp = port()
os.chdir(os.path.dirname(H))
Handler = type("Q", (http.server.SimpleHTTPRequestHandler,), {"log_message": lambda *x: None})
srv = http.server.ThreadingHTTPServer(("127.0.0.1", hp), Handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()
cp = port(); prof = "/tmp/eye5-chrome"
ch = subprocess.Popen(
    ["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu",
     f"--remote-debugging-port={cp}", f"--user-data-dir={prof}", "--window-size=1280,800", "about:blank"],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
for _ in range(150):
    try:
        tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{cp}/json")); break
    except Exception:
        time.sleep(0.2)
ws = websocket.create_connection([t for t in tabs if t["type"] == "page"][0]["webSocketDebuggerUrl"], timeout=60, suppress_origin=True)
i = 0
def cdp(m, **p):
    global i; i += 1; ws.send(json.dumps({"id": i, "method": m, "params": p}))
    while True:
        r = json.loads(ws.recv())
        if r.get("id") == i: return r.get("result", {})
def ev(x):
    return cdp("Runtime.evaluate", expression=x, returnByValue=True, awaitPromise=True)["result"].get("value")
def mouse(t, x, y, **k):
    cdp("Input.dispatchMouseEvent", type=t, x=x, y=y, **k)
def wait_tiles(n0, timeout=20):
    t = time.time()
    while time.time() - t < timeout:
        if ev("document.querySelectorAll('#m img.t').length && [...document.querySelectorAll('#m img.t')].filter(i=>i.style.display!='none').every(i=>i.complete)") and ev("T5.loads.length") > n0:
            break
        time.sleep(0.2)
    return time.time() - t

R = {}; ok = []
def check(name, cond, val):
    ok.append((name, bool(cond), val)); print(("PASS" if cond else "FAIL"), name, val)

# ensure built
if not os.path.exists(os.path.join(H, "eye5.html")):
    subprocess.check_call([sys.executable, os.path.join(H, "build5.py"), "--offline"])

cdp("Page.enable")
cdp("Emulation.setDeviceMetricsOverride", width=1280, height=800, deviceScaleFactor=1, mobile=False)
lat, lon = 41.8827, -87.6233
cdp("Page.navigate", url=f"http://127.0.0.1:{hp}/v5/eye5.html?lat={lat}&lon={lon}&z=4" + ("&online=1" if ONLINE else ""))
time.sleep(2)

# layers present
layers = ev("({events:T5.events.length,fires:D.fires.length,heat:D.heat.length,sats:T5.sats.length,probes:T5.probes.length,kp:T5.kp.length,cones:D.cones.length,census:D.sat_census})")
R["layers"] = layers
check("all safe layers embedded (events/fires/heat/sats/probes/kp/cones)",
      layers and layers["events"] > 50 and layers["fires"] > 100 and layers["heat"] == 18
      and layers["sats"] > 1000 and layers["probes"] > 0 and layers["kp"] > 0 and layers["cones"] > 0,
      layers)

# drag
c0 = ev("T5.center()"); mouse("mousePressed", 640, 400, button="left", clickCount=1)
for k in range(1, 11): mouse("mouseMoved", 640 + 30 * k, 400 + 20 * k, button="left", buttons=1)
mouse("mouseReleased", 940, 600, button="left", clickCount=1); c1 = ev("T5.center()")
dpx = ev(f"(()=>{{const a=ll2p({c0[0]},{c0[1]},T5.z),b=ll2p({c1[0]},{c1[1]},T5.z);return[a[0]-b[0],a[1]-b[1]]}})()")
check("drag moves map by pointer delta (300,200)", abs(dpx[0] - 300) < 1 and abs(dpx[1] - 200) < 1, dpx)
ev(f"T5.setView({lat},{lon},4)")

# wheel zoom + cursor lock
z = []
for k in range(15):
    mouse("mouseWheel", 640, 400, deltaX=0, deltaY=-100); z.append(ev("T5.z"))
cc = ev("T5.center()")
check("wheel zooms 4->19, keeps cursor point", z[-1] == 19 and abs(cc[0] - lat) < 1e-4 and abs(cc[1] - lon) < 1e-4, {"z": z[-1], "center": cc})
R["z19_m_per_px"] = ev("T5.mpp()")

# click-to-expand
ev("T5.setView(T5.events[0].la,T5.events[0].lo,6)")
mouse("mousePressed", 640, 400, button="left", clickCount=1); mouse("mouseReleased", 640, 400, button="left", clickCount=1)
cl = ev("T5.clicks.at(-1)"); txt = ev("info.textContent")
check("click marker expands details", cl and cl["hit"] and (cl["hit"] in txt or "source:" in txt), cl)
ev("T5.expandTo(T5.expand.la,T5.expand.lo,4)")
check("click-to-zoom expand raises zoom by ~4", ev("T5.z") >= 9, ev("T5.z"))

# empty click
mouse("mousePressed", 100, 700, button="left", clickCount=1); mouse("mouseReleased", 100, 700, button="left", clickCount=1)
check("empty click reports coordinates", ev("T5.clicks.at(-1).hit") is None and re.match(r"-?\d+\.\d{5}", ev("info.textContent")), ev("info.textContent")[:40])

# probe click
ev("T5.LAY.probes=true;T5.setView(T5.probes[0].la,T5.probes[0].lo,5)")
mouse("mousePressed", 640, 400, button="left", clickCount=1); mouse("mouseReleased", 640, 400, button="left", clickCount=1)
ptxt = ev("info.textContent")
check("probe click shows Eye Shield defensive info (no people)", "Eye Shield" in ptxt and "No people" in ptxt, ptxt[:120])

check("refresh interval 5 min", ev("T5.REFRESH_MS") == 300000, ev("T5.REFRESH_MS"))

# exclusion scan
code = open(os.path.join(H, "template5.html")).read().split("<script>")[1]
bad = re.findall(r"\b(adsb|ais\b|cctv|alpr|license.?plate|face.?recog|red.?sparrow|camoufox|camofox|argos.?atlas)\b", code, re.I)
h = open(os.path.join(H, "eye5.html")).read()
check("no remote scripts; no excluded tracking/malware terms in page code", not re.search(r"<script[^>]+src=", h) and not bad, bad)
check("EXCLUDED.md exists for Father", os.path.isfile(os.path.join(H, "..", "EXCLUDED.md")), os.path.join(H, "..", "EXCLUDED.md"))

if ONLINE:
    for name, zz in (("esri", 19), ("usgs", 16), ("gibs", 8)):
        ev(f"T5.base='{name}';T5.loads=[];T5.fail=0;T5.setView({lat},{lon},{zz})")
        t = wait_tiles(0)
        L = ev(f"T5.loads.filter(l=>l.z=={zz}&&l.k.startsWith('{name}/')).map(l=>l.ms)"); L.sort()
        R[f"{name}_z{zz}"] = {"tiles": len(L), "fail": ev("T5.fail"),
                              "median_ms": round(L[len(L) // 2]) if L else None,
                              "p95_ms": round(L[int(len(L) * 0.95) - 1]) if L else None,
                              "screen_full_s": round(t, 2)}
        check(f"{name} z{zz} tiles stream", L and ev("T5.fail") == 0, R[f"{name}_z{zz}"])
    ev(f"T5.base='esri';T5.loads=[];T5.setView({lat},{lon},18)"); wait_tiles(0)
    ev(f"T5.setView({lat},{lon},19)"); wait_tiles(0)
    for _ in range(60):
        if ev("T5.refreshes.length"): break
        time.sleep(0.5)
    rf = ev("T5.refreshes[0]"); R["refresh"] = rf
    check("live refresh pulled multi-source events", rf and rf["n"] > 50, rf)
    shot = cdp("Page.captureScreenshot", format="png")["data"]
    open(os.path.join(H, "shot5.png"), "wb").write(base64.b64decode(shot))
    R["shot_bytes"] = os.path.getsize(os.path.join(H, "shot5.png"))
    # street
    ev(f"T5.setView({lat},{lon},17);document.getElementById('street').checked=true")
    mouse("mousePressed", 640, 400, button="left", clickCount=1); mouse("mouseReleased", 640, 400, button="left", clickCount=1)
    for _ in range(90):
        if ev("T5.streetMs!==undefined"): break
        time.sleep(0.5)
    R["kartaview"] = {"photos": ev("T5.street.length"), "ms": ev("T5.streetMs"),
                     "fields": ev("T5.street[0]?Object.keys(T5.street[0]):[]")}
    check("KartaView keyless near click", R["kartaview"]["photos"] is not None and set(R["kartaview"].get("fields") or []) <= {"la", "lo", "dt", "th", "img"}, R["kartaview"])

ch.terminate()
json.dump({"checks": ok, "metrics": R}, open(os.path.join(H, "test_results.json"), "w"), indent=1)
print(f"{sum(o[1] for o in ok)}/{len(ok)} pass")
print(json.dumps(R, indent=1))
sys.exit(0 if all(o[1] for o in ok) else 1)
