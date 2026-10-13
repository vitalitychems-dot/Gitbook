#!/usr/bin/env python3
"""Unit + golden tests for tools/status/status.py. Run: python3 tools/status/tests/test_status.py"""
import datetime as dt, difflib, json, pathlib, shutil, sys, tempfile, unittest
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import status
FIX = HERE / "fixtures/status_min"
NOW = dt.datetime.fromisoformat("2026-10-13T15:00-05:00")

def copy_fix():
    t = pathlib.Path(tempfile.mkdtemp()); shutil.copytree(FIX, t, dirs_exist_ok=True); return t

def add_task(root, task):
    p = root / "mesh/queue/TASKS.json"; q = json.loads(p.read_text()); q["tasks"].append(task); p.write_text(json.dumps(q))

class T(unittest.TestCase):
    def test_golden(self):
        got, _ = status.build(FIX, NOW)
        exp = (FIX / "expected-STATUS.md").read_text()
        d = list(difflib.unified_diff(exp.splitlines(), got.splitlines(), "expected", "got", lineterm=""))
        self.assertEqual(d, [], "\n".join(d))
    def test_table_skips_separator(self):
        self.assertEqual(len(status.table("| Id | A |\n|---|---|\n| x | y |", "Id")), 1)
    def test_strip_links(self):
        self.assertEqual(status.strip_links("[PR #1](u) and [b](c)"), "PR #1 and b")
    def test_short_row_ignored(self):
        self.assertEqual(status.table("| Id | A |\n|---|---|\n| x |", "Id"), [])
    def test_bad_timestamps_do_not_crash(self):
        r = copy_fix()
        add_task(r, {"id": "C-NAIVE", "lane": "Build", "status": "claimed", "title": "x", "claimed_by": "Build", "claimed_at": "2026-10-13T08:00:00"})
        add_task(r, {"id": "C-BAD", "lane": "Build", "status": "claimed", "title": "x", "claimed_by": "Build", "claimed_at": "yesterday-ish"})
        _, w = status.build(r, NOW)
        self.assertTrue(any(x.startswith("C-NAIVE has an unreadable") for x in w))
        self.assertTrue(any(x.startswith("C-BAD has an unreadable") for x in w))
    def test_lease_boundary(self):
        r = copy_fix()
        for i, at in [("C-600", "2026-10-13T14:00:00Z"), ("C-601", "2026-10-13T13:59:00Z")]:
            add_task(r, {"id": i, "lane": "Build", "status": "claimed", "title": "x", "claimed_by": "Build", "claimed_at": at})
        _, w = status.build(r, NOW)
        self.assertTrue(any(x.startswith("C-601 claim") for x in w))
        self.assertFalse(any(x.startswith("C-600 claim") for x in w))

if __name__ == "__main__":
    unittest.main(verbosity=2)
