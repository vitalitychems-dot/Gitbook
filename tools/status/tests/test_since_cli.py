#!/usr/bin/env python3
"""CLI-level tests for `status.py --since STATEFILE` (delta broadcast), run as a subprocess.
Run: python3 tools/status/tests/test_since_cli.py"""
import json, pathlib, shutil, subprocess, sys, tempfile, unittest
HERE = pathlib.Path(__file__).resolve().parent
SCRIPT = HERE.parent / "status.py"
FIX = HERE / "fixtures/status_min"
NOW = "2026-10-13T15:00-05:00"

class SinceCLI(unittest.TestCase):
    def setUp(self):
        self.root = pathlib.Path(tempfile.mkdtemp()); shutil.copytree(FIX, self.root, dirs_exist_ok=True)
        self.state = pathlib.Path(tempfile.mkdtemp()) / "agent.status-since.json"
    def tearDown(self):
        shutil.rmtree(self.root); shutil.rmtree(self.state.parent)
    def run_cli(self):
        r = subprocess.run([sys.executable, str(SCRIPT), "--since", str(self.state), "--now", NOW],
                           cwd=self.root, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr); return r.stdout.splitlines()
    def full(self):
        sys.path.insert(0, str(SCRIPT.parent)); import status, datetime as dt
        return status.build(self.root, dt.datetime.fromisoformat(NOW))[1]
    def test_first_second_and_planted(self):
        warn = self.full(); self.assertTrue(warn, "fixture must have needs-attention items")
        # 1) first wake, no state file: full list, file created
        self.assertFalse(self.state.exists())
        self.assertEqual(self.run_cli(), [f"- {w}" for w in warn])
        self.assertTrue(self.state.exists()); self.assertEqual(json.loads(self.state.read_text()), sorted(warn))
        # 2) second wake, nothing changed
        self.assertEqual(self.run_cli(), ["- no change"])
        # 3) planted change: only the new item
        p = self.root / "mesh/queue/TASKS.json"; q = json.loads(p.read_text())
        q["tasks"].append({"id": "Q-999", "lane": "Build", "status": "claimed", "claimed_by": "X",
                           "claimed_at": "garbage", "title": "planted"}); p.write_text(json.dumps(q))
        out = self.run_cli()
        self.assertEqual(len(out), 1, out); self.assertTrue(out[0].startswith("- Q-999"), out)
        self.assertEqual(self.run_cli(), ["- no change"])
    def test_help_documents_default_path(self):
        r = subprocess.run([sys.executable, str(SCRIPT), "--help"], capture_output=True, text=True)
        self.assertIn(".status-since.json", r.stdout.replace("\n", "").replace(" ", ""))

if __name__ == "__main__":
    unittest.main(verbosity=2)
