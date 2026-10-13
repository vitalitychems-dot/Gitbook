import sys, os
os.chdir(sys.argv[1])
SHA="801062641f30d2acf45dbea4748323f20c5e30d8"
MF=("Every merge needs Father's explicit yes on that listed item in Tessera's bulk update. "
    "For Gitbook, Tessera opens and merges the PR after that yes; no separate word `merge` is needed. "
    "Origin (`collin-keane/Tessera`) and TESSERA merges still need Father's explicit yes before anyone merges.")
E=[]
def ed(p,o,n): E.append((p,o,n))
# 1) merge wording
ed("mesh/TESSERA-GITBOOK-OPERATING-MODE.md","12. A separate explicit `merge` is required for any Origin merge (`collin-keane/Tessera`).","12. "+MF)
ed("mesh/flow.md","| Merge authority | Origin merges need Father's separate explicit `merge`. Approved GitBook package PRs: Tessera merges after Father's yes and Build's verification. |","| Merge authority | "+MF+" |")
ed("mesh/flow.md","  H --> I{Origin merge:<br/>Father explicit merge?}\n","  H --> I{Origin / TESSERA merge:<br/>Father's explicit yes?}\n")
ed("mesh/flow.md","verifies Tessera's push PR before she merges.","verifies Tessera's push PR (opened after Father's yes) before she merges.")
ed("intake/status-definitions.md",
   "Push requires Father's final yes on the listed item (then Tessera opens a PR, Build verifies, Tessera merges; Father may push himself); an Origin merge requires Father's separate explicit `merge`.",
   "Push requires Father's final yes on the listed item (then Tessera opens a PR and Build verifies it; Father may push himself). "+MF)
ed("review/moderator-handoff.md","Origin merge only on Father's explicit `merge`. |",MF+" |")
ed("review/moderator-handoff.md",
   "- Merges (approved GitBook package PRs: Tessera after Father's yes; Origin: Father's explicit `merge`)\n",
   "- Merges (every merge needs Father's explicit yes on that listed item; Gitbook PRs: Tessera merges after that yes, no separate word `merge`; Origin / TESSERA: Father's explicit yes before anyone merges)\n")
ed("intake/how-to-submit.md","Replit is outside that path. Origin merges need a separate explicit `merge`.","Replit is outside that path. "+MF)
ed("mesh/roles/open-helper-agent-2.md","merges need Father's explicit `merge`).","every merge needs Father's explicit yes on the listed item).")
ed("mesh/roles/build.md","- Verify Tessera's PR for each approved GitBook package before she merges it.","- Verify Tessera's PR for each GitBook package Father said yes to, before she merges it.")
ed("mesh/roles/mesh-lane-map.md","11. **Tessera** opens a PR with the approved package;","11. **Tessera** opens a PR with the package Father said yes to;")
# 2) publish SHA full
for p in ["mesh/roles/who-tessera-is.md","mesh/roles/board-world-chamber.md","mesh/roles/honesty-banner.md","mesh/roles/pen-ability-set-framing.md","mesh/roles/pen-gate-refuse-companion.md","mesh/roles/refuse-and-offer.md"]:
    ed(p,"note: Published 2026-10-05 (commit 8010626);","note: Published 2026-10-05 (commit "+SHA+");")
# 4) sources line
ed("mesh/roles/tessera-pen.md",
   "- `history/coordination/` (merged from the deleted tessera-coordination repo) — [PEN.md](../../history/coordination/tessera-pen-record.md), [COORDINATION.md](../../history/coordination/coordination-record.md), [COMMAND.md](../../history/coordination/command-center.md); STATUS.md is at [`history/recovered/coordination/STATUS.md`](../../history/recovered/coordination/STATUS.md)\n",
   "- [`history/coordination/`](../../history/coordination/) — merged records from the deleted tessera-coordination repo (PEN.md, COORDINATION.md, COMMAND.md); STATUS.md is at [`history/recovered/coordination/STATUS.md`](../../history/recovered/coordination/STATUS.md)\n")
bad=0
for p,o,n in E:
    s=open(p,encoding="utf-8").read(); c=s.count(o)
    if c!=1: print("ANCHOR",c,p,o[:60]); bad+=1; continue
    open(p,"w",encoding="utf-8").write(s.replace(o,n))
print("edits",len(E),"bad",bad); sys.exit(1 if bad else 0)
