import unittest, json, os, tempfile, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bus, sched, conflict
H = os.path.dirname(os.path.abspath(__file__))
class T(unittest.TestCase):
    def test_bus_rules(self):
        msgs, errs = bus.load(os.path.join(H, "sample-bus.jsonl")); bad = dict(errs)
        self.assertNotIn(1, bad); self.assertNotIn(2, bad)
        self.assertIn("only tessera messages father", bad[3])
        self.assertTrue(any("zone" in e for e in bad[4]) and any("%" in e for e in bad[4]) and any("block" in e for e in bad[4]))
        self.assertNotIn(5, bad)
    def test_digest(self):
        msgs, _ = bus.load(os.path.join(H, "sample-bus.jsonl")); d = "\n".join(bus.digest(msgs))
        self.assertIn("collab-bus: owner=rick next_gate=tessera", d)
    def test_sched_respects_deps_and_gates(self):
        d = json.load(open(os.path.join(H, "sample-tasks.json"))); st = sched.expand(d["tasks"], d["gate_cost"])
        m, fin, _ = sched.simulate(st, "cp")
        for s, v in st.items():
            for dep in v["deps"]: self.assertLessEqual(fin[dep], fin[s] - v["cost"])
        self.assertLess(fin["PR55-qlab:moderator"], fin["PR55-qlab:father"])
        self.assertLessEqual(m, sched.simulate(st, "fifo")[0])
    def test_sched_cycle(self):
        st = {"a": {"lane": "x", "cost": 1, "deps": ["b"], "prio": 0}, "b": {"lane": "x", "cost": 1, "deps": ["a"], "prio": 0}}
        self.assertRaises(ValueError, sched.simulate, st, "cp")
    def test_conflict(self):
        L = [("a.md", 1, "Tessera claimed HYB-012 today"), ("b.md", 2, "Replit claims HYB-012 too"), ("c.md", 3, "Rick owns GB-001")]
        r = conflict.scan_lines(L); self.assertEqual(list(r), ["HYB-012"]); self.assertEqual(r["HYB-012"]["lanes"], ["replit", "tessera"])
        pc = conflict.path_conflicts([{"from": "rick", "paths": ["tools/collab"]}, {"from": "build", "paths": ["tools/collab/bus.py"]}, {"from": "rick", "paths": ["mesh/x.md"]}])
        self.assertEqual(len(pc), 1)
if __name__ == "__main__": unittest.main()
