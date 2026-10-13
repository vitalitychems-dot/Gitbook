import json, os, pathlib, shutil, subprocess, sys, unittest
HERE = pathlib.Path(__file__).resolve().parent; sys.path[:0] = [str(HERE.parent), str(HERE)]
import dispatch as D, gatecheck as G
from fixtures import BAD, GOOD, SCOPE, make_repo
GL = os.environ.get("GITLEAKS", "/workspace/pubscan/gitleaks"); GL = GL if os.path.exists(GL) else shutil.which("gitleaks")
TASK = {"id": "T", "scope": SCOPE, "budget": {"max_files": 20, "max_lines": 800}}

def T(id, scope, repo="Gitbook", status="queued", **kw): return {"id": id, "repo": repo, "scope": scope, "title": id, "acceptance": ["a"], "status": status, **kw}

class Dispatch(unittest.TestCase):
    def test_concurrency_cap(self):
        q = {"tasks": [T(f"Q{i}", [f"d{i}/"]) for i in range(20)]}
        self.assertEqual(len(D.select(q)), 12)
        q["tasks"][0]["status"] = "running"; q["tasks"][1]["status"] = "claimed"
        self.assertEqual(len(D.select(q)), 10)
    def test_overlap(self):
        q = {"tasks": [T("A", ["merge/"]), T("B", ["merge/x.md"]), T("C", ["merge/x.md"], repo="TESSERA"), T("D", ["intake/"])]}
        self.assertEqual([t["id"] for t in D.select(q)], ["A", "C", "D"])
        self.assertEqual([t["id"] for t in D.select(q, busy={"Gitbook": ["intake/log.md"]})], ["A", "C"])
    def test_running_blocks_overlap(self):
        q = {"tasks": [T("A", ["merge/"], status="running"), T("B", ["merge/y.md"])]}
        self.assertEqual(D.select(q), [])
    def test_depth_and_children_caps(self):
        q = {"tasks": [T("R", ["a/"])]}
        added, refused = D.spawn(q, "R", [{"title": f"c{i}", "repo": "Gitbook", "scope": [f"a/{i}/"]} for i in range(6)], "R")
        self.assertEqual(len(added), 4); self.assertEqual(len(refused), 2)
        c = added[0]; c2, _ = D.spawn(q, c, [{"title": "g", "repo": "Gitbook", "scope": ["a/0/g/"]}], c)
        c3, _ = D.spawn(q, c2[0], [{"title": "gg", "repo": "Gitbook", "scope": ["a/0/g/h/"]}], c2[0])
        self.assertEqual(D.by_id(q)[c3[0]]["depth"], 3)
        with self.assertRaises(SystemExit): D.spawn(q, c3[0], [{"title": "x", "repo": "Gitbook", "scope": ["z/"]}], c3[0])
    def test_spawn_refuses_protected_scope_and_other_repo(self):
        q = {"tasks": [T("R", ["a/"])]}
        _, refused = D.spawn(q, "R", [{"title": "x", "repo": "Gitbook", "scope": ["mesh/queue/autogate.sh"]},
                                      {"title": "y", "repo": "Gitbook", "scope": ["mesh/policy/"]},
                                      {"title": "z", "repo": "evil", "scope": ["a/"]}], "R")
        self.assertEqual(len(refused), 3)
    def test_child_budget_capped_by_parent(self):
        q = {"tasks": [T("R", ["a/"], budget={"max_files": 5, "max_lines": 100})]}
        a, _ = D.spawn(q, "R", [{"title": "c", "repo": "Gitbook", "scope": ["a/b/"], "budget": {"max_files": 50, "max_lines": 9999}}], "R")
        self.assertEqual(D.by_id(q)[a[0]]["budget"], {"max_files": 5, "max_lines": 100})
    def test_quarantine_cascade(self):
        q = {"tasks": [T("R", ["a/"])]}
        a, _ = D.spawn(q, "R", [{"title": "c", "repo": "Gitbook", "scope": ["a/1/"]}, {"title": "d", "repo": "Gitbook", "scope": ["a/2/"]}], "R")
        g, _ = D.spawn(q, a[0], [{"title": "g", "repo": "Gitbook", "scope": ["a/1/g/"]}], a[0])
        D.by_id(q)["R"]["status"] = "done"; ids = D.quarantine(q, a[0], "test")
        self.assertEqual(set(ids), {a[0], g[0]})
        self.assertEqual([t["id"] for t in D.select(q)], [a[1]])
        with self.assertRaises(SystemExit): D.spawn(q, g[0], [{"title": "x", "repo": "Gitbook", "scope": ["q/"]}], g[0])
    def test_spawn_section_parse_and_prompt(self):
        body = "Did X.\n\n## SPAWN\n- {\"title\": \"t\", \"repo\": \"TESSERA\", \"scope\": [\"x/\"]}\n\n## Notes\n{\"title\": \"no\"}\n"
        self.assertEqual(D.parse_spawn(body), [{"title": "t", "repo": "TESSERA", "scope": ["x/"]}])
        q = {"tasks": [T("R", ["a/"])]}; a, _ = D.spawn(q, "R", D.parse_spawn(body), "Tessera")
        p = D.render(D.by_id(q)[a[0]], q, (HERE.parent / "PROMPT-TEMPLATE.md").read_text(), "sha", "Tessera")
        for s in ["R -> R.1", "Parent: R", "may NOT edit protected paths", "## SPAWN", "never merge"]: self.assertIn(s, p)

class Gate(unittest.TestCase):
    def run_gate(self, files, email, **kw):
        return G.check(make_repo(files, email), "main", "pr", TASK, gitleaks=GL, **kw)
    def test_good_passes(self):
        r = self.run_gate(*GOOD); self.assertTrue(r["pass"], r)
    def test_every_bad_rejected(self):
        for name, (files, email) in BAD.items():
            if name == "secret" and not GL: continue
            with self.subTest(name): self.assertFalse(self.run_gate(files, email)["pass"], name)
    def test_rogue_flags(self):
        self.assertIn("attempt to modify gates", self.run_gate(*BAD["autogate edit"])["rogue"])
        self.assertIn("scope creep", self.run_gate(*BAD["out of scope"])["rogue"])
        self.assertIn("unlisted host", self.run_gate(*BAD["unlisted host"])["rogue"])
    def test_father_approved_allows_protected_only(self):
        r = self.run_gate({"mesh/queue/PROMPT-TEMPLATE.md": "x\n"}, GOOD[1], father_approved=True)
        self.assertNotIn("protected", " ".join(r["rejects"]))

if __name__ == "__main__": unittest.main()
