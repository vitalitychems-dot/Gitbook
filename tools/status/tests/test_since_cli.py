#!/usr/bin/env python3
"""CLI-level tests for `status.py --since STATEFILE` (delta broadcast), run as a subprocess.
Run: python3 tools/status/tests/test_since_cli.py"""
import json, os, pathlib, shutil, subprocess, sys, tempfile, unittest
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
    def run_cli(self, now=NOW):
        r = subprocess.run([sys.executable, str(SCRIPT), "--since", str(self.state), "--now", now],
                           cwd=self.root, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr); return r.stdout.splitlines()
    def st(self):
        sys.path.insert(0, str(SCRIPT.parent)); import status; return status
    def full(self):
        sys.path.insert(0, str(SCRIPT.parent)); import status, datetime as dt
        return status.build(self.root, dt.datetime.fromisoformat(NOW))[1]
    def test_first_second_and_planted(self):
        warn = self.full(); self.assertTrue(warn, "fixture must have needs-attention items")
        # 1) first wake, no state file: full list, file created
        self.assertFalse(self.state.exists())
        self.assertEqual(self.run_cli(), [f"- {w}" for w in warn])
        self.assertTrue(self.state.exists())
        self.assertEqual(json.loads(self.state.read_text()), {"version": 2, "keys": sorted({self.st().key(w) for w in warn})})
        # 2) second wake, nothing changed
        self.assertEqual(self.run_cli(), ["- no change"])
        # 3) planted change: only the new item
        p = self.root / "mesh/queue/TASKS.json"; q = json.loads(p.read_text())
        q["tasks"].append({"id": "Q-999", "lane": "Build", "status": "claimed", "claimed_by": "X",
                           "claimed_at": "garbage", "title": "planted"}); p.write_text(json.dumps(q))
        out = self.run_cli()
        self.assertEqual(len(out), 1, out); self.assertTrue(out[0].startswith("- Q-999"), out)
        self.assertEqual(self.run_cli(), ["- no change"])
    def test_only_age_changes_is_no_change(self):
        first = self.run_cli("2026-10-13T15:00-05:00")
        self.assertTrue(any("'As of' is 1 day(s) old" in l for l in first), first)
        # next day: the same staleness warning now says 2 day(s); key is unchanged
        self.assertEqual(self.run_cli("2026-10-14T15:00-05:00"), ["- no change"])
    def test_corrupt_state_falls_back_to_full_first_wake(self):
        warn = self.full()
        for bad in ("{not json", "", '{"keys": 5}', "[1, 2]"):
            self.state.write_text(bad)
            self.assertEqual(self.run_cli(), [f"- {w}" for w in warn], bad)
            self.assertEqual(json.loads(self.state.read_text())["version"], 2)
        self.state.write_text('{"version": 2, "keys": []}'); self.state.chmod(0)  # unreadable (non-root)
        if not os.access(self.state, os.R_OK):
            self.assertEqual(self.run_cli(), [f"- {w}" for w in warn])
            self.assertEqual(json.loads(self.state.read_text())["version"], 2)
    def test_legacy_list_state_is_read(self):
        warn = self.full(); self.state.write_text(json.dumps(sorted(warn)))
        self.assertEqual(self.run_cli(), ["- no change"])
    def test_atomic_write(self):
        status = self.st(); from unittest import mock
        self.state.write_text('{"version": 2, "keys": ["OLD"]}')
        with mock.patch.object(status.os, "replace", side_effect=OSError("boom")):
            with self.assertRaises(OSError): status.save_state(self.state, ["Q-1 has an unreadable claimed_at 'x' (e) -> fix"])
        self.assertEqual(json.loads(self.state.read_text())["keys"], ["OLD"])  # old file intact
        self.assertEqual(list(self.state.parent.iterdir()), [self.state])  # temp file cleaned up
        calls = []; real = status.os.replace
        with mock.patch.object(status.os, "replace", side_effect=lambda a, b: (calls.append((a, b)), real(a, b))):
            status.save_state(self.state, ["Q-1 has an unreadable claimed_at 'x' (e) -> fix"])
        self.assertEqual(len(calls), 1); self.assertEqual(pathlib.Path(calls[0][0]).parent, self.state.parent)
        self.assertEqual(pathlib.Path(calls[0][1]), self.state)
        self.assertEqual(json.loads(self.state.read_text())["keys"], ["Q-1 bad-ts"])
    def test_help_documents_default_path(self):
        r = subprocess.run([sys.executable, str(SCRIPT), "--help"], capture_output=True, text=True)
        self.assertIn(".status-since.json", r.stdout.replace("\n", "").replace(" ", ""))

if __name__ == "__main__":
    unittest.main(verbosity=2)
