import json, os, sys, tempfile, unittest, socket
sys.path.insert(0, os.path.dirname(__file__)); import eye
FX = os.path.join(os.path.dirname(__file__), "fixtures")
sys.path.insert(0, "/workspace/rick/tools/collab")
class T(unittest.TestCase):
    def setUp(self):
        socket.socket = None  # no network
        self.d = tempfile.mkdtemp(); self.idx = os.path.join(self.d, "e.jsonl"); self.bus = os.path.join(self.d, "b.jsonl")
    def test_parse_all(self):
        r = eye.pull(FX, self.idx, self.bus)
        for s in eye.FEEDS: self.assertGreater(r[s]["events"], 0, s)
    def test_fields_and_citation(self):
        eye.pull(FX, self.idx, self.bus)
        for l in open(self.idx):
            e = json.loads(l)
            for k in ("id","source","license","cite","lat","lon","time"): self.assertIn(k, e)
            self.assertTrue(-90 <= e["lat"] <= 90 and -180 <= e["lon"] <= 180)
    def test_dedup(self):
        a = eye.pull(FX, self.idx, self.bus)["new_indexed"]; b = eye.pull(FX, self.idx, self.bus)["new_indexed"]
        self.assertGreater(a, 0); self.assertEqual(b, 0)
    def test_bus_valid(self):
        eye.pull(FX, self.idx, self.bus)
        import bus; msgs, errs = bus.load(self.bus); self.assertEqual(errs, []); self.assertEqual(len(msgs), 4)
    def test_no_person_fields(self):
        eye.pull(FX, self.idx, self.bus); t = open(self.idx).read().lower()
        for w in ("callsign", "icao24", "mmsi", "phone", "email", "face"): self.assertNotIn('"%s"' % w, t)
    def test_map_offline(self):
        eye.pull(FX, self.idx, self.bus); out = os.path.join(self.d, "m.html"); _, n = eye.make_map(self.idx, out)
        h = open(out).read(); self.assertGreater(n, 0); self.assertNotIn("http://cdn", h); self.assertNotIn("<script src", h)
if __name__ == "__main__": unittest.main()
