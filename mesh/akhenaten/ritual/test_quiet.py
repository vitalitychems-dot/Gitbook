import unittest, json, os
from common import load_round
D = os.path.dirname(os.path.abspath(__file__))
def rnd(n):
    q = json.load(open(f"{D}/questions{'' if n == 1 else '-2'}.json"))
    return q, load_round(f"{D}/live-round-{n}.jsonl", len(q))
class Quiet(unittest.TestCase):
    def test_saves_cost_matches_full(self):
        from quiet import quiet, full
        for n in (1, 2):
            q, a = rnd(n); f, fc = full(q, a); o, oc, _ = quiet(q, a)
            self.assertLess(oc, 0.4 * fc)
            for x, y, qq in zip(o, f, q):
                if qq["type"] == "num": self.assertAlmostEqual(float(x) / float(y), 1, delta=0.01)
                else: self.assertEqual(x, y)
    def test_escalates_on_disagreement(self):
        from quiet import quiet
        q = [{"id": 1, "q": "x", "type": "cat"}]
        a = {"a": ["A"], "b": ["B"], "c": ["A"], "d": ["B"], "e": ["B"]}
        o, cost, esc = quiet(q, a)
        self.assertEqual((o, cost, esc), (["B"], 5, [1]))
if __name__ == "__main__": unittest.main()
