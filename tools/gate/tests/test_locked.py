import os, subprocess, sys, tempfile, unittest
L = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "locked.py")
def hits(paths, extra=""):
    with tempfile.NamedTemporaryFile("w", delete=False) as f: f.write(extra)
    return subprocess.run([sys.executable, L, f.name], input="\n".join(paths), capture_output=True, text=True, check=True).stdout.split()
class Locked(unittest.TestCase):
    def test_defaults_without_repo_list(self):
        self.assertEqual(hits([".github/workflows/ci.yml", "CODEOWNERS", "mesh/charter/GATE_RULES.md", "tools/gate/regate.sh", "a/b/AGENTS.md"]),
                         [".github/workflows/ci.yml", "CODEOWNERS", "mesh/charter/GATE_RULES.md", "a/b/AGENTS.md"])
    def test_repo_list_and_dir_patterns(self):
        self.assertEqual(hits(["x/y.md", "foo/bar/z"], "# c\n/foo/bar/ @o\n"), ["foo/bar/z"])
if __name__ == "__main__": unittest.main()
