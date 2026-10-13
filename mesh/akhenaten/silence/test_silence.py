import unittest, json, os, datetime as dt, silence
TR = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "real-trace.json")))
class T(unittest.TestCase):
    def test_heartbeat_suppressed_after_recent_post(self):
        self.assertFalse(silence.should_heartbeat(100, 110))
        self.assertTrue(silence.should_heartbeat(100, 100 + silence.HB))
    def test_watchdog_flags_only_stale(self):
        now = dt.datetime.fromisoformat("2026-10-13T12:00:00-05:00")
        m = [{"agent": "a", "ts": "2026-10-13T11:50:00-05:00"}, {"agent": "b", "ts": "2026-10-13T11:30:00-05:00"}]
        self.assertEqual(silence.watch(m, now), ["b"])
    def test_real_replay_fewer_msgs_detect_le_30_no_false_alarms(self):
        r = silence.replay(TR)
        self.assertLess(r["msgs_after"], r["msgs_before"])
        self.assertLessEqual(r["worst_detect_min_after"], 30)
        self.assertEqual(r["false_alarms"], 0)
    def test_10min_hb_would_increase_msgs(self):
        r = silence.replay(TR, hb=10, deadline=25, tick=5)
        self.assertGreater(r["msgs_after"], r["msgs_before"])
if __name__ == "__main__": unittest.main()
