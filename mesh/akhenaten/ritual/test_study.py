import unittest, json, os
from common import load_round
D = os.path.dirname(os.path.abspath(__file__))
def rnd(n):
    q = json.load(open(f"{D}/questions{'' if n == 1 else '-2'}.json"))
    return q, load_round(f"{D}/live-round-{n}.jsonl", len(q))
class Study(unittest.TestCase):
    def test_queue_flags_only_spread(self):
        from study import study_queue
        q, a = rnd(2); s = study_queue(q, a)
        self.assertEqual([x["id"] for x in s], [16])
        self.assertNotIn("answer", json.dumps(s))
        q, a = rnd(1); self.assertEqual(study_queue(q, a), [])
if __name__ == "__main__": unittest.main()
