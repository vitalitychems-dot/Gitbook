import os, tempfile, unittest, sqlite3, hashlib
import palace
class T(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp(); self.db = os.path.join(self.d, "p.db"); r = os.path.join(self.d, "corpus")
        os.makedirs(r + "/q"); os.makedirs(r + "/t")
        self.facts = {"aqft beats exact qft under noise": ("q/a.md", 40), "tesla coil patent resonance": ("t/b.md", 5),
                      "bhnmc baseline narma reservoir": ("q/c.txt", 70)}
        for i, (fact, (f, ln)) in enumerate(self.facts.items()):
            lines = [f"filler line {j} lorem ipsum{i}" for j in range(100)]; lines[ln - 1] = fact
            open(os.path.join(r, f), "w").write("\n".join(lines))
        self.root = r
    def run_q(self):
        palace.build([self.root], self.db); hits = 0
        for fact, (f, ln) in self.facts.items():
            res = palace.search(fact, 5, self.db)
            ok = any(p.endswith(f) and l0 <= ln <= l1 for p, l0, l1, *_ in res); hits += ok
        return hits / len(self.facts)
    def test_recall_and_citations(self): self.assertEqual(self.run_q(), 1.0)
    def test_bm25_fallback(self):
        orig = palace.fts_ok; palace.fts_ok = lambda c: False
        try: self.assertEqual(self.run_q(), 1.0)
        finally: palace.fts_ok = orig
    def test_idempotent(self):
        dump = lambda: hashlib.sha1(repr(sqlite3.connect(self.db).execute("select path,l0,l1,room,body from chunks order by id").fetchall()).encode()).hexdigest()
        palace.build([self.root], self.db); a = dump(); palace.build([self.root], self.db); self.assertEqual(a, dump())
if __name__ == "__main__": unittest.main()
