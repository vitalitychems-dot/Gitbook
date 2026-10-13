import unittest, datetime as dt, silence
class T(unittest.TestCase):
    def test_post_only_on_change_or_keepalive(self):
        self.assertFalse(silence.should_post(1, 1, 0, 30))
        self.assertTrue(silence.should_post(2, 1, 0, 30))
        self.assertTrue(silence.should_post(1, 1, 0, silence.KEEPALIVE))
    def test_watchdog_flags_only_stale(self):
        now = dt.datetime.fromisoformat("2026-10-13T12:00:00-05:00")
        m = [{"agent": "a", "ts": "2026-10-13T11:50:00-05:00"}, {"agent": "b", "ts": "2026-10-13T09:00:00-05:00"}]
        self.assertEqual(silence.watch(m, now), ["b"])
    def test_sim_fewer_msgs_and_stall_caught(self):
        r = silence.sim(7)
        self.assertLess(r["msgs_after"], 0.4 * r["msgs_before"])
        self.assertTrue(r["stall_caught_after"]); self.assertLessEqual(r["detect_latency_min_after"], 90)
if __name__ == "__main__": unittest.main()
