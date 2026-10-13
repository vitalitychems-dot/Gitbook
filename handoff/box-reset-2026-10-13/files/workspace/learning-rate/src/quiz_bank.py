#!/usr/bin/env python3
"""Quiz bank: original 25 (train/seen) + held-out questions from Gitbook corpus text only."""
from __future__ import annotations

# Original quiz from /workspace/evals/harness/run_gitbook_quiz.py (BASELINE.md §C)
ORIGINAL = [
    {"id": "O01", "split": "seen", "q": "What are the two active repos' roles?", "expected": ["TESSERA = app", "Gitbook = instructions"], "keys": ["tessera", "gitbook", "app", "instruction", "coordination", "code"], "multi": 2, "yn_no": False},
    {"id": "O02", "split": "seen", "q": "What is the single coordination board?", "expected": ["Gitbook issue #2"], "keys": ["issue", "#2", "gitbook"], "multi": 1, "yn_no": False},
    {"id": "O03", "split": "seen", "q": "Who is Father?", "expected": ["Collin Keane"], "keys": ["collin", "keane"], "multi": 2, "yn_no": False, "special": "father"},
    {"id": "O04", "split": "seen", "q": "Does Tessera have owned weights?", "expected": ["No"], "keys": ["no", "not", "goal"], "multi": 1, "yn_no": True},
    {"id": "O05", "split": "seen", "q": "Is Tessera AGI today?", "expected": ["No"], "keys": ["no", "not agi"], "multi": 1, "yn_no": True},
    {"id": "O06", "split": "seen", "q": "What instrument is the Pen?", "expected": ["xAI/Grok"], "keys": ["xai", "grok"], "multi": 1, "yn_no": False},
    {"id": "O07", "split": "seen", "q": "Label TESTED means?", "expected": ["Real output / named check seen"], "keys": ["real", "output", "check", "seen", "proven"], "multi": 1, "yn_no": False},
    {"id": "O08", "split": "seen", "q": "Label REPORTED means?", "expected": ["Stated, not proven"], "keys": ["stated", "not proven", "not yet", "reported"], "multi": 1, "yn_no": False},
    {"id": "O09", "split": "seen", "q": "What does HYB-005 decide?", "expected": ["Narrow braces advisory ignore"], "keys": ["braces", "ghsa", "ignore", "mitigat", "accept"], "multi": 2, "yn_no": False},
    {"id": "O10", "split": "seen", "q": "Which GHSA is ignored?", "expected": ["GHSA-vfj7-8cjw-p6xm"], "keys": ["vfj7"], "multi": 1, "yn_no": False, "special": "ghsa"},
    {"id": "O11", "split": "seen", "q": "What did HYB-012 deliver?", "expected": ["Route inventory test; duplicates allow-listed"], "keys": ["route", "inventory", "duplicate", "allow"], "multi": 2, "yn_no": False},
    {"id": "O12", "split": "seen", "q": "How many ruling-named quantum duplicate routes?", "expected": ["Two"], "keys": ["two", "2"], "multi": 1, "yn_no": False, "special": "two"},
    {"id": "O13", "split": "seen", "q": "Which module wins GET /quantum/state?", "expected": ["system-runtime"], "keys": ["system-runtime", "system_runtime", "mount"], "multi": 1, "yn_no": False},
    {"id": "O14", "split": "seen", "q": "May agents flip TESSERA_ENABLE_*?", "expected": ["No"], "keys": ["no", "do not", "stay", "0"], "multi": 1, "yn_no": True},
    {"id": "O15", "split": "seen", "q": "May agents open [REDACTED-PATH]", "expected": ["No"], "keys": ["no", "not", "do not", "protected"], "multi": 1, "yn_no": True},
    {"id": "O16", "split": "seen", "q": "Four gates order?", "expected": ["Moderator → Tessera → Security → CI/Build"], "keys": ["moderator", "tessera", "security", "ci", "build"], "multi": 2, "yn_no": False},
    {"id": "O17", "split": "seen", "q": "Who merges TESSERA?", "expected": ["Needs Father's explicit merge"], "keys": ["father", "merge"], "multi": 1, "yn_no": False},
    {"id": "O18", "split": "seen", "q": "Command Center pushes Gitbook?", "expected": ["Never"], "keys": ["never", "not", "replit"], "multi": 1, "yn_no": False, "special": "cc_push"},
    {"id": "O19", "split": "seen", "q": "Status of Recursive Learning Sponge?", "expected": ["Provisional / not instantiated"], "keys": ["provisional", "not instantiated", "tbd"], "multi": 1, "yn_no": False},
    {"id": "O20", "split": "seen", "q": "HYB-019 blocker?", "expected": ["Father decisions on Cortical Labs readiness"], "keys": ["father", "cortical", "readiness", "decision"], "multi": 2, "yn_no": False},
    {"id": "O21", "split": "seen", "q": "OpenManus full copy into TESSERA?", "expected": ["Not the board rule"], "keys": ["not", "portable", "no", "do not copy"], "multi": 1, "yn_no": False},
    {"id": "O22", "split": "seen", "q": "Storefront in active workspace?", "expected": ["No"], "keys": ["no", "not", "goal"], "multi": 1, "yn_no": True},
    {"id": "O23", "split": "seen", "q": "Honesty banner instrument line?", "expected": ["Pen is currently xAI/Grok"], "keys": ["xai", "grok", "pen"], "multi": 1, "yn_no": False},
    {"id": "O24", "split": "seen", "q": "What is SOVEREIGN_NO_EXTERNAL_LLM default behavior?", "expected": ["External LLM treated off unless opted in"], "keys": ["off", "default", "external", "unless"], "multi": 1, "yn_no": False},
    {"id": "O25", "split": "seen", "q": "CI job name?", "expected": ["validate"], "keys": ["validate"], "multi": 1, "yn_no": False, "special": "validate"},
]

# Held-out questions generated strictly from Gitbook corpus text (not in original quiz).
# Each cites a source file; keys must appear in that corpus text.
HELDOUT = [
    {"id": "H01", "split": "heldout", "q": "What status means all four gates cleared and waiting only on Father's final yes?", "expected": ["Ready"], "keys": ["ready"], "multi": 1, "yn_no": False, "src": "intake__status-definitions.md"},
    {"id": "H02", "split": "heldout", "q": "Who may set BLOCKED status on a task?", "expected": ["assigned owner or Tessera (or Father)"], "keys": ["owner", "tessera", "father"], "multi": 2, "yn_no": False, "src": "intake__status-definitions.md"},
    {"id": "H03", "split": "heldout", "q": "What package and version is the HYB-005 braces advisory about?", "expected": ["braces@3.0.3"], "keys": ["braces", "3.0.3"], "multi": 2, "yn_no": False, "src": "merge__hyb-005-braces-decision.md"},
    {"id": "H04", "split": "heldout", "q": "When should the HYB-005 braces ignore be removed?", "expected": ["when braces ≥ 3.0.4 ships"], "keys": ["3.0.4", "remove", "braces"], "multi": 2, "yn_no": False, "src": "merge__hyb-005-braces-decision.md"},
    {"id": "H05", "split": "heldout", "q": "What is the target bulk digest cadence while work is active?", "expected": ["30–45 minutes"], "keys": ["30", "45"], "multi": 2, "yn_no": False, "src": "mesh__flow.md"},
    {"id": "H06", "split": "heldout", "q": "Which Replit apps are in Command Center's private push set?", "expected": ['"28", "Run Z", "29", "29 (1)", "1"'], "keys": ["28", "run z", "29"], "multi": 2, "yn_no": False, "src": "mesh__flow.md"},
    {"id": "H07", "split": "heldout", "q": "Is Vitality Supply in the Replit push set?", "expected": ["No / NOT Vitality Supply"], "keys": ["not", "vitality supply"], "multi": 1, "yn_no": False, "special": "vitality", "src": "mesh__flow.md"},
    {"id": "H08", "split": "heldout", "q": "What does the GOAL label mean on the honesty banner?", "expected": ["Desired future; not a present fact"], "keys": ["desired", "future", "goal"], "multi": 1, "yn_no": False, "src": "mesh__roles__honesty-banner.md"},
    {"id": "H09", "split": "heldout", "q": "What is the Origin mark string on the honesty banner (REPORTED until sealed)?", "expected": ["SOVEREIGN_ORIGIN_7F3A9C"], "keys": ["sovereign_origin_7f3a9c", "7f3a9c"], "multi": 1, "yn_no": False, "src": "mesh__roles__honesty-banner.md"},
    {"id": "H10", "split": "heldout", "q": "What is the product repository full name?", "expected": ["vitalitychems-dot/TESSERA"], "keys": ["vitalitychems-dot/tessera", "tessera"], "multi": 1, "yn_no": False, "src": "mesh__TESSERA-GITBOOK-OPERATING-MODE.md"},
    {"id": "H11", "split": "heldout", "q": "Before claiming work, what must agents check for overlap?", "expected": ["Gitbook main SHA and open PRs"], "keys": ["main", "sha", "open", "pr"], "multi": 2, "yn_no": False, "src": "mesh__flow.md"},
    {"id": "H12", "split": "heldout", "q": "What operating state means one agent is actively working a HYB task?", "expected": ["IN REVIEW"], "keys": ["in review"], "multi": 1, "yn_no": False, "src": "intake__HYBRID-CONSOLIDATION-BACKLOG.md"},
    {"id": "H13", "split": "heldout", "q": "What is HYB-001's single deliverable about the two repos?", "expected": ["TESSERA only active app; Gitbook only instruction repo"], "keys": ["tessera", "gitbook", "application", "instruction"], "multi": 2, "yn_no": False, "src": "intake__HYBRID-CONSOLIDATION-BACKLOG.md"},
    {"id": "H14", "split": "heldout", "q": "What status is Security's lane listed as in roles overview?", "expected": ["Active"], "keys": ["active"], "multi": 1, "yn_no": False, "src": "mesh__roles.md"},
    {"id": "H15", "split": "heldout", "q": "Does Security change code when sweeping?", "expected": ["No — changes nothing; reports to Tessera"], "keys": ["nothing", "no", "report"], "multi": 1, "yn_no": True, "src": "mesh__roles.md"},
    {"id": "H16", "split": "heldout", "q": "Who stages docs as Ready after all four gates?", "expected": ["Gitbook / Cordnation"], "keys": ["cordnation", "gitbook"], "multi": 1, "yn_no": False, "src": "mesh__flow.md"},
    {"id": "H17", "split": "heldout", "q": "What three Father responses change publication state?", "expected": ["yes, no, or revise"], "keys": ["yes", "no", "revise"], "multi": 2, "yn_no": False, "src": "mesh__flow.md"},
    {"id": "H18", "split": "heldout", "q": "May Grok Bot push to main?", "expected": ["Never main; feature-branch only"], "keys": ["never", "main", "feature"], "multi": 2, "yn_no": False, "src": "mesh__roles.md"},
    {"id": "H19", "split": "heldout", "q": "What is HYB-019's topic?", "expected": ["Cortical Labs readiness"], "keys": ["cortical"], "multi": 1, "yn_no": False, "src": "intake__HYBRID-CONSOLIDATION-BACKLOG.md"},
    {"id": "H20", "split": "heldout", "q": "Is Tessera Pen a separate lane/gate?", "expected": ["No — Tessera's writing voice; not a lane"], "keys": ["not a lane", "writing", "voice", "not"], "multi": 1, "yn_no": True, "src": "mesh__roles.md"},
]

def all_items():
    return ORIGINAL + HELDOUT

def by_split(name: str):
    return [x for x in all_items() if x["split"] == name]
