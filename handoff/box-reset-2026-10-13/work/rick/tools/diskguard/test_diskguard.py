import json, os, subprocess, tempfile, time, unittest
import diskguard as dg

class T(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.root = self.tmp.name
        now = time.time()
        for name, mb, age_h in (("big-fresh", 3, 0), ("small-old", 1, 48)):
            d = os.path.join(self.root, name); os.makedirs(d)
            fp = os.path.join(d, "f.bin")
            with open(fp, "wb") as f: f.write(os.urandom(mb * 1024 * 1024))
            t = now - age_h * 3600
            os.utime(fp, (t, t)); os.utime(d, (t, t))
    def tearDown(self): self.tmp.cleanup()

    def test_sizing_and_order(self):
        rows = dg.collect([self.root], 6, 10)
        self.assertEqual([r["path"].split("/")[-1] for r in rows], ["big-fresh", "small-old"])
        self.assertAlmostEqual(rows[0]["bytes"] / 2**20, 3, delta=0.1)
        self.assertAlmostEqual(rows[1]["bytes"] / 2**20, 1, delta=0.1)

    def test_staleness(self):
        rows = {r["path"].split("/")[-1]: r for r in dg.collect([self.root], 6, 10)}
        self.assertTrue(rows["small-old"]["finished"]); self.assertFalse(rows["big-fresh"]["finished"])

    def test_git_clean_pushed(self):
        d = os.path.join(self.root, "clone"); bare = os.path.join(self.root, "bare.git")
        g = lambda *a, c=d: subprocess.run(["git", "-C", c, *a], check=True, capture_output=True)
        subprocess.run(["git", "init", "-q", "--bare", bare], check=True)
        subprocess.run(["git", "init", "-q", d], check=True)
        open(os.path.join(d, "x"), "w").write("x")
        g("add", "x"); g("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "x")
        g("remote", "add", "origin", bare); g("push", "-q", "origin", "HEAD:main"); g("fetch", "-q")
        r = [r for r in dg.collect([self.root], 999, 10) if r["path"] == d][0]
        self.assertIn("git clone clean and fully pushed", r["reasons"])
        open(os.path.join(d, "y"), "w").write("y")
        r = [r for r in dg.collect([self.root], 999, 10) if r["path"] == d][0]
        self.assertFalse(r["finished"])

    def test_thresholds(self):
        for pct, want in ((50, None), (85, 85), (89.9, 85), (90, 90), (94, 90), (95, 95), (99, 95)):
            self.assertEqual(dg.warn_level(pct), want)

    def test_growth(self):
        e = [{"ts": 0, "used": 100, "total": 1100}, {"ts": 3600, "used": 200, "total": 1100}]
        rate, eta = dg.growth(e); self.assertEqual(rate, 100); self.assertEqual(eta, 9)
        self.assertEqual(dg.growth(e[:1]), (None, None))

    def test_never_deletes_and_json(self):
        before = sorted(os.listdir(self.root))
        rep = os.path.join(self.root, "R.md"); hist = os.path.join(self.root, "h.jsonl")
        out = subprocess.run(["python3", dg.__file__, "--json", "--roots", self.root, "--report", rep, "--history", hist],
                             capture_output=True, text=True)
        d = json.loads(out.stdout)
        self.assertIn("percent", d); self.assertTrue(os.path.exists(rep))
        self.assertIn("rm -rf -- ", open(rep).read())
        self.assertEqual(sorted(x for x in os.listdir(self.root) if x not in ("R.md", "h.jsonl")), before)

if __name__ == "__main__": unittest.main()
