import json, os, unittest
H = os.path.dirname(os.path.abspath(__file__))
class T(unittest.TestCase):
    def test_graph(self):
        g = json.load(open(os.path.join(H, "graph.json"))); ids = {n["id"] for n in g["nodes"]}
        self.assertTrue(all(e["source"] in ids and e["target"] in ids for e in g["edges"]))
        self.assertTrue({"repo", "agent", "module", "rule", "result"} <= {n["kind"] for n in g["nodes"]})
        self.assertIn(("module:api-server", "module:db", "imports"), {(e["source"], e["target"], e["type"]) for e in g["edges"]})
    def test_mermaid(self):
        m = open(os.path.join(H, "graph.mmd")).read().splitlines(); self.assertEqual(m[0], "flowchart LR"); self.assertGreater(len(m), 10)
if __name__ == "__main__": unittest.main()
