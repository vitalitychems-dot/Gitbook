import sys, os
os.chdir(sys.argv[1])
E = [
("mesh/roles/who-tessera-is.md", "**Status:** REPORTED — in Moderator/digest path under Father YES TO ALL. Not sealed as live canon until Father completes the GitBook → GitHub push and separately authorizes any Origin merge. Origin mark below stays **REPORTED** until sealed.\n\n", ""),
("mesh/roles/board-world-chamber.md", "**Status:** REPORTED — Moderator APPROVED; Ready — awaiting Father GitHub push. Not sealed until Ready → GitHub.\n\n", ""),
("mesh/roles/honesty-banner.md", "**Status:** REPORTED — Moderator APPROVED; Ready — awaiting Father GitHub push. Not sealed until Ready → GitHub.\n\n", ""),
("mesh/roles/pen-ability-set-framing.md", "**Status:** draft for GitBook — not shippable until Moderator pass and Father’s digest yes.\n\n", ""),
("mesh/roles/pen-gate-refuse-companion.md", "**Status:** REPORTED — Moderator APPROVED; Ready — awaiting Father GitHub push. Not sealed until Ready → GitHub. Must match tone guide / refuse-and-offer IDs.", "Must match tone guide / refuse-and-offer IDs."),
("mesh/roles/refuse-and-offer.md", "**Status:** REPORTED — Moderator APPROVED; Ready — awaiting Father GitHub push. Rule IDs must match pen-gate when that branch lands. Not sealed until Ready → GitHub.\n", "Rule IDs must match pen-gate when that branch lands.\n"),
]
bad=0
for p,o,n in E:
    s=open(p,encoding="utf-8").read(); c=s.count(o)
    if c!=1: print("ANCHOR",c,p); bad+=1; continue
    open(p,"w",encoding="utf-8").write(s.replace(o,n))
print("edits",len(E),"bad",bad); sys.exit(1 if bad else 0)
