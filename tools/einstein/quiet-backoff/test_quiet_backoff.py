import unittest
from quiet_backoff import due,seen,BASE,CAP
class T(unittest.TestCase):
    def test_new_sha_runs(self): a,s=seen({},"x",0);self.assertEqual((a,s["iv"]),("RUN",BASE))
    def test_not_due_skips(self): _,s=seen({},"x",0);self.assertFalse(due(s,60))
    def test_backoff_caps(self):
        _,s=seen({},"x",0)
        for _ in range(10): self.assertTrue(due(s,s["next"]));a,s=seen(s,"x",s["next"])
        self.assertEqual((a,s["iv"]),("IDLE",CAP))
    def test_push_resets(self):
        s={"sha":"x","iv":CAP,"next":CAP*60};a,s=seen(s,"y",CAP*60);self.assertEqual((a,s["iv"]),("RUN",BASE))
    def test_latency_bounded(self):  # push right after a check is seen at most CAP min later
        s={"sha":"x","iv":CAP,"next":CAP*60};self.assertFalse(due(s,CAP*60-1));self.assertTrue(due(s,CAP*60))
unittest.main()
