#!/usr/bin/env python3
"""locked.py PATTERN_FILE < paths  -> prints paths that hit a locked pattern.
Built-in defaults always apply (fail closed even if the repo lists are missing)."""
import fnmatch, sys
DEFAULT = [".github/**", "CODEOWNERS", "**/CODEOWNERS", "gate/**", "SETUP-FATHER.md", "scripts/loop/**",
           "mesh/charter/**", "mesh/policy/**", "mesh/roles/**", "mesh/roles.md", "mesh/queue/autogate.sh",
           "mesh/queue/gatecheck.py", "mesh/queue/dispatch.py", "mesh/queue/PROMPT-TEMPLATE.md", "mesh/queue/tests/**",
           "evals/heldout/**", "AGENTS.md", "**/AGENTS.md", ".cursor/**", "**/*persona*", "**/prompts/**",
           "**/*.prompt.md", "**/system-prompt*", "**/routines/**", "**/secrets/**", "**/credentials*", "**/.env", "**/.env.*"]
def match(p, pat):
    pat = pat.strip().lstrip("/")
    if pat.endswith("/"): pat += "**"
    if fnmatch.fnmatchcase(p, pat): return True
    if pat.startswith("**/") and fnmatch.fnmatchcase(p, pat[3:]): return True
    return pat.endswith("/**") and p.startswith(pat[:-3] + "/")
pats = DEFAULT + [l.split()[0] for l in open(sys.argv[1]) if l.strip() and not l.lstrip().startswith("#")]
for p in (l.strip() for l in sys.stdin):
    if p and any(match(p, q) for q in pats): print(p)
