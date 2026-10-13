import unittest, numpy as np, os, json, simons as S
class T(unittest.TestCase):
    def test_interference_bounds(self):
        g = np.random.default_rng(0).random((20, 648)); psi = S.amplitudes(g)
        self.assertTrue(np.allclose((psi**2).sum(1), 1)); f = S.interference(psi, 1)[1:]
        self.assertTrue(((f >= 0) & (f <= 1 + 1e-9)).all()); self.assertTrue(np.allclose(S.interference(np.vstack([psi[:1]]*3), 1)[1:], 1))
    def test_bh_and_bonferroni(self):
        p = np.array([1e-5, .01, .03, .2, .9]); self.assertEqual(S.bh(p, .05).tolist(), [True, True, True, False, False])
        rng = np.random.default_rng(1); X = rng.normal(size=(400, 200)); y = rng.normal(size=400)
        r, p = S.edge_pvalues(X, y); self.assertLessEqual((p < .05/200).sum(), 1)  # noise features must not survive
    def test_no_lookahead(self):
        x = np.arange(10.); self.assertTrue(np.isnan(S.lag(x, 1)[0])); self.assertEqual(S.lag(x, 1)[5], 4)
        self.assertEqual(S.roll(x, 3, np.mean)[2], 1)  # window ends at t, never t+1
    def test_png(self):
        p = "/tmp/_hm.png"; S.render(np.random.default_rng(2).poisson(1, (40, 18, 36)).astype(float), p, last=40)
        self.assertEqual(open(p, "rb").read(8), b"\x89PNG\r\n\x1a\n")
    def test_pipeline_feature_count_and_results(self):
        d = S.load(); names, X, y, g = S.features(*d); self.assertGreaterEqual(len(names), 200)
        self.assertEqual(X.shape, (len(d[0]), len(names))); self.assertTrue(np.isnan(y[-1]))
        r = json.load(open(os.path.join(S.H, "results.json")))["A_same_window_as_eye"]["models"]
        self.assertAlmostEqual(r["persistence"]["band_acc"], 0.505); self.assertAlmostEqual(r["mean7"]["band_acc"], 0.473)
if __name__ == "__main__": unittest.main()
