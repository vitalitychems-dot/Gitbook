import unittest, json, os, tempfile, sign
D = os.path.dirname(os.path.abspath(__file__))
L = [json.loads(l) for l in open(f"{D}/fixtures/live-round-3-forged.jsonl")]
class T(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp(); self.reg = {m["agent"]: sign.keygen(m["agent"], self.d) for m in L}
        self.kf = lambda a: sign.load_key(a, self.d)
    def test_before_all_9_accepted_by_old_collect(self):
        self.assertEqual(sum(m["kind"] == "result" and "agent" in m for m in L), 9)
    def test_forged_replay_0_accepted(self):
        self.assertEqual(sign.verify(L, self.reg, self.kf), [])
    def test_forger_signing_with_own_key_only_gets_own_line(self):
        k = self.kf("tessera")
        for mut in (lambda m: m, lambda m: dict(m, **{"from": m["agent"]})):
            ok = sign.verify([sign.sign(mut(m), k) for m in L], self.reg, self.kf)
            self.assertEqual([m["agent"] for m in ok], ["tessera"])
    def test_honest_lines_accepted_and_tamper_rejected(self):
        G = [sign.sign(dict(m, **{"from": m["agent"]}), self.kf(m["agent"])) for m in L]
        self.assertEqual(len(sign.verify(G, self.reg, self.kf)), 9)
        bad = dict(G[0]); bad["answers"] = [0] * 15
        self.assertFalse(sign.verify_line(bad, self.reg, self.kf))
    def test_unregistered_or_wrong_fingerprint_rejected(self):
        G = sign.sign(dict(L[0], **{"from": "tessera"}), self.kf("tessera"))
        self.assertFalse(sign.verify_line(G, {}, self.kf))
        self.assertFalse(sign.verify_line(G, {"tessera": "0" * 16}, self.kf))
if __name__ == "__main__": unittest.main()
