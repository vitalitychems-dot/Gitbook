import json, tesseract as T
def test_store_5d():
    c = T.sqlite3.connect(T.DB); s = dict(c.execute("select scenario,count(*) from e group by 1"))
    assert s["observed"] > 400 and s["forecast:p50"] == 7
def test_query_all_stores():
    r = T.query("earthquake"); assert r["world+bus+forecast"] and r["palace"] and r["_ms"]["total"] < 2000
def test_cone_ordered():
    c = T.cones(); v = {x[0]: x[10] for x in c}; d = c[0][0].split(":")[1]
    assert v[f"cone:{d}:p10"] <= v[f"cone:{d}:p50"] <= v[f"cone:{d}:p90"]
def test_anomaly_spike():
    xs = [20] * 40 + [21, 19] * 10; xs[50] = 80; assert 50 in T.anomalies(xs)
def test_brief_budget():
    assert T.toks(T.brief()) < 2000
