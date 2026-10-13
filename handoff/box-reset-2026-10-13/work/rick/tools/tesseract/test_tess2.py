import json, os, time, subprocess, tempfile, sqlite3, tess2 as X, tesseract as T
def test_13_calibration(): r = X.calibrate(); assert abs(r["holdout_cov"] - .8) < .08 and r["holdout_cov"] > r["holdout_cov_k1"]
def test_rank_fix(): assert X.query2("earthquake alaska tessera")[0][0] == "world" and X.rank_eval(X.query2) > X.rank_eval(X.query1)
def test_20_lint(): assert X.lint("- a claim with no source") and not X.lint("- M 6.7 quake [usgs]") and X.lint(T.brief()) == []
def test_17_health():
    now = time.time(); ev = [{"source": "usgs", "time": "2020-01-01T00:00:00+00:00"}, {"source": "eonet", "time": dt_now()}]
    h = X.health(now, ev); assert h["usgs"]["stale"] and not h["eonet"]["stale"]
def dt_now(): import datetime as d; return d.datetime.now(d.timezone.utc).isoformat()
def test_11_delta():
    p = tempfile.mktemp(); a = X.delta(snap=p); b = X.delta(snap=p); assert a["new"] > 400 and b["new"] == 0
def test_9_salience(): s = X.salience(); assert s[0][0] >= s[-1][0] and len(s) == 463
def test_10_links(): assert any(l["palace"] for l in X.links())
def test_14_grid(): c = sqlite3.connect(T.DB).execute("select count(*) from e where lat is not null").fetchone()[0]; assert sum(X.grid().values()) == c
def test_16_compact():
    r = X.compact(out=tempfile.mktemp(suffix=".gz")); assert r["total"] == 463 and r["compact_bytes"] < r["raw_bytes"] / 5
def test_18_budget():
    for n in (200, 400): assert T.toks(X.budget_brief(n)) <= n
def test_8_replay(): r = X.replay(); assert sum(map(len, r["frames"].values())) == r["n"] and "id=ts" in open(os.path.join(X.HERE, "tesseract.html")).read()
def test_12_whatif():
    db = tempfile.mktemp(); open(db, "wb").write(open(T.DB, "rb").read())
    r = X.whatif(db, drop="usgs"); assert r["rows"] == r["observed"] - 245
    r2 = X.whatif(db, scale=("earthquake", 2)); c = sqlite3.connect(db)
    assert c.execute("select sum(sev) from e where scenario=? and kind='earthquake'", (r2["scenario"],)).fetchone()[0] > c.execute("select sum(sev) from e where scenario='observed' and kind='earthquake'").fetchone()[0]
    os.remove(db)
def test_15_flow(): f = X.flow(); assert f["rick"] and any(k.startswith("verdict:") for l in f.values() for k in l)
def test_19_overlay(): c = X.overlay(tempfile.mktemp()); assert all("salience" in b for b in c["buildings"]) and any(b["salience"] > 0 for b in c["buildings"])
def test_7_runner():
    d = os.path.join(X.HERE, "state"); now = str(int(time.time()))
    for f in ("eye", "feeds2"): open(f"{d}/{f}.stamp", "w").write(now)  # not due: no network, no data writes
    if os.path.exists(f"{d}/store.stamp"): os.remove(f"{d}/store.stamp")
    out = subprocess.run([os.path.join(X.HERE, "run_feeds.sh")], capture_output=True, text=True)
    log = open(f"{d}/runner.log").read().splitlines(); assert log[-1].endswith("ran store") and "ran eye" not in log[-1]
    n = len(log); subprocess.run([os.path.join(X.HERE, "run_feeds.sh")]); assert len(open(f"{d}/runner.log").read().splitlines()) == n  # interval gating
