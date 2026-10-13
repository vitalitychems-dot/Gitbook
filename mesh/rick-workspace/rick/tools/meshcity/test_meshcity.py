import json, os, re, unittest, html.parser, gen
D = os.path.dirname(os.path.abspath(__file__))
DISK = {"percent": 96.5, "free": 1, "generated": "x"}
ROOMS = "  10 a/b\n   3 c/d\n"
class T(unittest.TestCase):
    def test_schema(self):
        c = json.load(open(f"{D}/city.json"))
        self.assertEqual(c["schema"], "meshcity/1")
        self.assertIn(c["ground"]["level"], ("green", "amber", "red", "unknown"))
        names = {b["name"] for b in c["buildings"] if b["kind"] == "agent"}
        self.assertEqual(names, set(gen.AGENTS))
        for b in c["buildings"]:
            for k in ("id", "kind", "name", "height", "x", "z"): self.assertIn(k, b)
            self.assertGreater(b["height"], 0)
        self.assertEqual(len({b["id"] for b in c["buildings"]}), len(c["buildings"]))
    def test_determinism(self):
        a = gen.dumps(gen.build(DISK, ROOMS)); b = gen.dumps(gen.build(DISK, ROOMS))
        self.assertEqual(a, b)
        self.assertEqual(json.loads(a)["ground"]["level"], "red")
    def test_html(self):
        t = open(f"{D}/index.html").read()
        p = html.parser.HTMLParser(); p.feed(t); p.close()
        self.assertIsNone(re.search(r"(https?:)?//[a-z0-9.-]+\.[a-z]{2,}/", t, re.I))
        self.assertNotRegex(t, r"\bsrc\s*=|\bhref\s*=|@import")
        m = re.search(r'<script id="city" type="application/json">(.*?)</script>', t, re.S)
        json.loads(m.group(1))
if __name__ == "__main__": unittest.main()
