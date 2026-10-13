import unittest
from quiet_backoff import due,seen,BASE
class T(unittest.TestCase):
    def test_new_etag_runs(self): a,s=seen({},200,"e1",0);self.assertEqual((a,s["iv"]),("RUN",BASE))
    def test_304_idles(self): _,s=seen({},200,"e1",0);self.assertEqual(seen(s,304,"e1",300)[0],"IDLE")
    def test_same_etag_200_idles(self): _,s=seen({},200,"e1",0);self.assertEqual(seen(s,200,"e1",300)[0],"IDLE")
    def test_default_no_backoff_latency_equals_base(self):
        _,s=seen({},200,"e1",0)
        for _ in range(10): a,s=seen(s,304,"e1",s["next"])
        self.assertEqual(s["iv"],BASE)
    def test_optional_backoff_caps(self):
        _,s=seen({},200,"e1",0,cap=30)
        for _ in range(10): a,s=seen(s,304,"e1",s["next"],cap=30)
        self.assertEqual(s["iv"],30)
    def test_change_resets(self):
        s={"etag":"e1","iv":30,"next":1800};a,s=seen(s,200,"e2",1800,cap=30);self.assertEqual((a,s["iv"]),("RUN",BASE))
    def test_not_due_skips(self): _,s=seen({},200,"e1",0);self.assertFalse(due(s,60));self.assertTrue(due(s,BASE*60))
    def test_replay_data_reproduces(self):
        import replay
        w,f,l=replay.sim(etag=True);w0,f0,l0=replay.sim()
        self.assertLess(f,0.2*f0);self.assertAlmostEqual(sum(l)/len(l),sum(l0)/len(l0),places=6)
if __name__=="__main__": unittest.main()
