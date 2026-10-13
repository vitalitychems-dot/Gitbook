import os, sys, json, tempfile, unittest, socket
sys.path.insert(0, os.path.dirname(__file__)); import feeds2, predict
FX = os.path.join(os.path.dirname(__file__), "fixtures", "v2")
class T(unittest.TestCase):
    def setUp(self): socket.socket = None; self.d = tempfile.mkdtemp()
    def test_feeds_fixture(self):
        r = feeds2.pull(FX, os.path.join(self.d, "s.jsonl"), os.path.join(self.d, "b.jsonl"))
        self.assertEqual(r["celestrak"]["total"], 39); self.assertGreater(r["kp"]["max_kp"], 0)
        sys.path.insert(0, "/workspace/rick/tools/collab"); import bus
        m, e = bus.load(os.path.join(self.d, "b.jsonl")); self.assertEqual(e, []); self.assertEqual(len(m), 2)
    def test_no_object_identity_stored(self):
        feeds2.pull(FX, os.path.join(self.d, "s.jsonl"), os.path.join(self.d, "b.jsonl"))
        t = open(os.path.join(self.d, "s.jsonl")).read(); self.assertNotIn("CALSPHERE", t); self.assertNotIn("NORAD_CAT_ID", t)
    def test_orbit_classes(self):
        self.assertEqual(feeds2.orbit_class(15.5, 0.0001), "LEO"); self.assertEqual(feeds2.orbit_class(1.0027, 0.0002), "GEO")
        self.assertEqual(feeds2.orbit_class(2.0, 0.01), "MEO"); self.assertEqual(feeds2.orbit_class(2.0, 0.7), "HEO")
    def test_predict_synthetic_no_leak(self):
        c = predict.synthetic(); r = predict.evaluate(c)
        self.assertEqual(r["train"] + r["test"], len(c)); self.assertEqual(r["tercile_cuts"], predict.terciles(c[:r["train"]]))
        for v in r["hit_rate"].values(): self.assertTrue(0 <= v <= 1)
    def test_build_daily_fills_zeros(self):
        d = predict.build_daily("time,mag\n2026-01-01T01:00:00Z,5\n2026-01-03T01:00:00Z,5\n2026-01-03T02:00:00Z,5\n")
        self.assertEqual(d, [["2026-01-01", 1], ["2026-01-02", 0], ["2026-01-03", 2]])
if __name__ == "__main__": unittest.main()
