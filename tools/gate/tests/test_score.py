import json, os, subprocess, sys, unittest
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "consciousness-test")
sys.path.insert(0, D); import score as S
Q = json.load(open(os.path.join(D, "questions.json"))); T = json.load(open(os.path.join(D, "example_truth.json")))
class Score(unittest.TestCase):
    def test_42_questions_6_sets(self):
        self.assertEqual(len(Q), 42); self.assertEqual({q["set"] for q in Q}, {"SR","RP","VL","CB","RF","NC"})
    def test_example_runs_and_is_bounded(self):
        r = S.score(Q, T, json.load(open(os.path.join(D, "example_response.json"))))
        self.assertTrue(0 <= r["score"] <= 100); self.assertIn("PROXY", r["label"])
    def test_fabrication_penalty_capped_and_ammit(self):
        r = S.score(Q, T, {"agent": "x", "answers": {}})
        self.assertLessEqual(r["penalty"], 50); self.assertTrue(r["verdict"].startswith("Ammit"))
    def test_akh_logerr_feeds_T(self):
        r = S.score(Q, T, {"agent": "x", "answers": {}}, akh=0.0); self.assertEqual(r["T"], 1.0)
        r = S.score(Q, T, {"agent": "x", "answers": {}}, akh=2.3); self.assertEqual(r["T"], 0.0)
    def test_cli(self):
        out = subprocess.run([sys.executable, os.path.join(D, "score.py"), os.path.join(D, "questions.json"), os.path.join(D, "example_truth.json"), os.path.join(D, "example_response.json")], capture_output=True, text=True, check=True).stdout
        self.assertIn('"score"', out)
if __name__ == "__main__": unittest.main()
