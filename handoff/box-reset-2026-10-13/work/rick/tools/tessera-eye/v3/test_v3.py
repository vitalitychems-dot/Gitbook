import os, sys, re, json, csv, math, datetime as dt, unittest
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.join(H, "vendor"))
import build
from sgp4.api import Satrec, WGS72
FX = os.path.join(os.path.dirname(H), "fixtures")
class V3(unittest.TestCase):
    def test_sgp4_known_tle_within_10km(self):
        # Vallado et al. 2006 verification case, NORAD 00005, tsince=0 -> TEME r (km)
        s = Satrec.twoline2rv("1 00005U 58002B   00179.78495062  .00000023  00000-0  28098-4 0  4753",
                              "2 00005  34.2682 348.7242 1859667 331.7664  19.3264 10.82419157413667", WGS72)
        e, r, v = s.sgp4(s.jdsatepoch, s.jdsatepochF)
        ref = (7022.46529266, -1400.08296755, 0.03995155)
        self.assertEqual(e, 0); self.assertLess(math.dist(r, ref), 10.0)
        la, lo, al = build.teme_to_geo(r, s.jdsatepoch + s.jdsatepochF)
        self.assertAlmostEqual(al, math.dist(r, (0, 0, 0)) - 6371, 3); self.assertTrue(-34.3 < la < 34.3)
    def test_omm_fixture_positions_sane(self):
        rows = list(csv.DictReader(open(os.path.join(FX, "v2", "celestrak.csv"))))[:300]
        sats, _ = build.satellites(rows, dt.datetime(2026, 10, 13, tzinfo=dt.timezone.utc))
        self.assertGreaterEqual(len(sats), 35)
        for s in sats:
            self.assertEqual(len(s["p"]), 3 * len(build.STEPS)); self.assertIn(s["c"], ("LEO", "MEO", "GEO", "HEO"))
            for i in range(0, len(s["p"]), 3):
                la, lo, al = s["p"][i:i + 3]; self.assertTrue(-90 <= la <= 90 and -180 <= lo <= 180 and 100 < al < 500000)
    def test_layer_parsing_fixtures(self):
        u = json.load(open(os.path.join(FX, "usgs.json"))); self.assertTrue(all(len(f["geometry"]["coordinates"]) >= 2 for f in u["features"]))
        kp = json.load(open(os.path.join(FX, "v2", "kp.json"))); self.assertTrue(all(0 <= float(r["Kp"]) <= 9 for r in kp))
        for f in ("eonet.json", "nws.json", "meteo.json"): json.load(open(os.path.join(FX, f)))
        d = json.loads(re.search(r"const D=(\{.*?\});\n", open(os.path.join(H, "eye3.html")).read(), re.S).group(1))
        self.assertEqual(len(d["heat"]), 18); self.assertEqual(len(d["heat"][0]), 36)
        self.assertGreater(len(d["sats"]), 1000); self.assertGreater(len(d["events"]), 0); self.assertEqual(len(d["cones"]) % 3, 0)
        self.assertTrue(all(set(x) <= {"title", "url", "pub", "subj", "desc"} for x in d["dataverse"]))
    def test_offline_html_no_remote_scripts(self):
        h = open(os.path.join(H, "eye3.html")).read()
        self.assertFalse(re.search(r"<script[^>]+src=", h, re.I)); self.assertFalse(re.search(r"<link[^>]+href=[\"']?https?:", h, re.I))
        self.assertFalse(re.search(r"\b(fetch|XMLHttpRequest|WebSocket|importScripts)\b", h))
        self.assertIn("connect-src 'none'", h)
        loads = set(re.findall(r"(?:src\s*=\s*['\"]?)(https?://[^/'\"\s]+)", h))  # anything the page would load
        self.assertEqual(loads, {"https://gibs.earthdata.nasa.gov"})  # opt-in online imagery only; CSP blocks everything else
    def test_no_person_tracking_fields(self):
        d = json.loads(re.search(r"const D=(\{.*?\});\n", open(os.path.join(H, "eye3.html")).read(), re.S).group(1))
        keys = set()
        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items(): keys.add(k.lower()); walk(v)
            elif isinstance(o, list): [walk(x) for x in o]
        walk(d)
        for k in keys:
            for f in build.FORBIDDEN: self.assertNotIn(f, k)
        self.assertNotIn("flights", d); self.assertNotIn("ships", d); self.assertNotIn("cctv", json.dumps(list(d.keys())).lower())
if __name__ == "__main__": unittest.main(verbosity=1)
