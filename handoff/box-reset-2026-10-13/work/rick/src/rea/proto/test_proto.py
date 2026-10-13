import unittest, numpy as np, router, debate_ensemble as D
class T(unittest.TestCase):
    def test_router_beats_baselines(self):
        r = lambda p: sum(router.run(p, seed=s)[0] for s in range(10))
        self.assertGreater(r("router"), r("roundrobin")); self.assertGreater(r("roundrobin"), r("single"))
    def test_debate_no_lookahead_and_better(self):
        P, t, off = D.preds(); d = D.debate(P, t, 30, 2); eq = np.mean([P[k] for k in P], 0)
        t2 = t.copy(); t2[-1] += 1000; self.assertTrue(np.allclose(D.debate(P, t2, 30, 2)[:-1], d[:-1]) and D.debate(P, t2, 30, 2)[-1] == d[-1])
        self.assertLess(np.abs(d - t)[off-1:].mean(), np.abs(eq - t)[off-1:].mean())
if __name__ == "__main__": unittest.main()
