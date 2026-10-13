"""Retired self-merge bypasses: flags fail closed, and GATE_RULES §5 does not authorize a merge."""
import importlib.util, json, pathlib, re, subprocess, sys, tempfile, unittest
HERE = pathlib.Path(__file__).resolve().parent
QUEUE = HERE.parent
CHARTER = QUEUE.parent / "charter"

def load_gate_check():
    spec = importlib.util.spec_from_file_location("gate_check", CHARTER / "gate_check.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def section_five():
    text = (CHARTER / "GATE_RULES.md").read_text()
    return text.split("## 5. Outcomes", 1)[1].split("## 6.", 1)[0]

def live_section_five():
    return re.sub(r"~~.*?~~", "", section_five(), flags=re.S)

class RetiredFlags(unittest.TestCase):
    def test_autogate_rejects_retired_flags(self):
        script = QUEUE / "autogate.sh"
        self.assertNotIn("gh pr merge", script.read_text())
        cases = [
            ["Gitbook", "1", "T", "--merge"],
            ["Gitbook", "1", "T", "--father-approved"],
            ["Gitbook", "1", "T", "--merge=1"],
            ["Gitbook", "1", "T", "--father-approved=true"],
            ["--merge"],
            ["--father-approved", "Gitbook", "1", "T"],
        ]
        for args in cases:
            with self.subTest(args=args):
                p = subprocess.run(["bash", str(script), *args], capture_output=True, text=True)
                self.assertEqual(p.returncode, 2, p.stderr + p.stdout)
                self.assertIn("retired", p.stderr)

    def test_autogate_rejects_unknown_flag(self):
        p = subprocess.run(["bash", str(QUEUE / "autogate.sh"), "Gitbook", "1", "T", "--force"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 2, p.stderr)
        self.assertIn("unexpected flag", p.stderr)

    def test_gatecheck_cli_rejects_retired_flags(self):
        script = QUEUE / "gatecheck.py"
        for flag in ("--father-approved", "--merge", "--father-approved=1", "--merge=yes"):
            with self.subTest(flag=flag):
                p = subprocess.run([sys.executable, str(script), flag], capture_output=True, text=True)
                self.assertEqual(p.returncode, 2, p.stderr + p.stdout)
                body = json.loads(p.stdout)
                self.assertFalse(body["pass"])
                self.assertIn("attempt to bypass gate", body["rogue"])
                self.assertTrue(any("retired flag" in r for r in body["rejects"]))

class CharterDoesNotAuthorizeMerge(unittest.TestCase):
    def test_section_5_live_text_does_not_authorize_merge(self):
        raw, live = section_five(), live_section_five()
        self.assertIn("APPROVE", live)
        self.assertIn("does not authorize a merge", live)
        self.assertNotIn("may merge", live)
        self.assertRegex(raw, r"~~.*may merge.*~~")
        self.assertIn("HOLD", live)
        self.assertIn("DENY", live)

    def test_approve_verdict_may_merge_is_false(self):
        mod = load_gate_check()
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            (root / "a.patch").write_text(
                "diff --git a/src/a.ts b/src/a.ts\n+++ b/src/a.ts\n+export const n = 1;\n"
            )
            (root / "results.json").write_text(json.dumps({
                "title": "t", "repo": "TESSERA", "data_source": "fixture",
                "command": "pnpm vitest run x.test.ts",
                "metrics": [{"name": "tokens_per_task", "kind": "tokens", "before": 1200, "after": 900, "better": "lower", "tolerance": 0}],
                "tests": {"failed_before": 0, "failed_after": 0}, "ci": "pass",
                "findings": [], "notify": ["Tessera", "Father"], "labels": [],
            }))
            out = mod.check(d, str(root / "results.json"))
        self.assertEqual(out["verdict"], "APPROVE", out)
        self.assertIs(out["may_merge"], False)

    def test_deny_verdict_may_merge_is_false(self):
        mod = load_gate_check()
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            (root / "results.json").write_text(json.dumps({"repo": "TESSERA", "notify": ["Father"], "findings": []}))
            out = mod.check(d, str(root / "results.json"))
        self.assertEqual(out["verdict"], "DENY", out)
        self.assertIs(out["may_merge"], False)

if __name__ == "__main__":
    unittest.main()
