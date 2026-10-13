#!/usr/bin/env python3
"""GB-027 edits on 979c35e + GB-026 rev3 + six unchanged 979c35e role pages. Each old string must match exactly once."""
import sys, os, shutil
root = sys.argv[1]
OS = "Origin (`collin-keane/Tessera`) and TESSERA merges still need Father's explicit yes (the word 'merge') before anyone merges."
OS_OLD = "Origin (`collin-keane/Tessera`) and TESSERA merges still need Father's explicit yes before anyone merges."
BANNER = "> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**\n\n"
E = {
"mesh/TESSERA-GITBOOK-OPERATING-MODE.md": [
 ("| Tessera Grok bot / Command Center | Collects completed check-ins and prepares the periodic bulk digest | May ask the owner for `yes`, `no`, or `revise`; never auto-pushes or auto-merges |",
  "| Tessera Grok bot / Command Center | Collects completed check-ins and feeds Tessera's periodic bulk update (Tessera sends it to Father) | Does not send the update or ask Father for `yes`, `no`, or `revise` (Tessera does); never auto-pushes or auto-merges |"),
 ("Must explicitly approve the exact digest; Origin merge requires separate `merge` |",
  "Must explicitly approve the exact digest (`yes`, `no`, or `revise`); Origin and TESSERA merges need Father's explicit yes (the word 'merge') |"),
 ("9. Tessera Grok bot / Command Center collects only items that cleared all four gates (Ready) into a **bulk digest**.",
  "9. Tessera Grok bot / Command Center collects only items that cleared all four gates (Ready) and feeds them into **Tessera's bulk digest**; Tessera sends it to Father."),
 (OS_OLD, OS),
],
"mesh/flow.md": [
 ("the Tessera Grok bot prepares a 30–45 minute bulk digest and Father gives final approval.",
  "Tessera sends a 30–45 minute bulk update (Command Center feeds it) and Father gives final approval."),
 ("The Tessera Grok bot / Command Center prepares one evidence-linked bulk digest every 30–45 minutes while work is active. It asks Father for `yes`, `no`, or `revise`; it does not publish or merge.",
  "Tessera sends Father one evidence-linked bulk update every 30–45 minutes while work is active; the Tessera Grok bot / Command Center feeds it and does not publish or merge. The update asks Father for `yes`, `no`, or `revise`."),
 ("A separate explicit `merge` is still required for Origin merges.", OS),
 ("→ Tessera Grok bot / **Command Center** one bulk digest to Father every 30–45 min with each push as its own numbered digest item",
  "→ **Command Center** (Tessera Grok bot) feeds **Tessera's** one bulk update to Father every 30–45 min, with each push as its own numbered digest item"),
 ("→ Father separately says `merge` for an Origin merge (no merge without Father's explicit yes).",
  "→ Origin (`collin-keane/Tessera`) and TESSERA merges need Father's explicit yes (the word 'merge') before anyone merges."),
 ("S --> F[Command Center digest<br/>numbered items 30–45 min]",
  "S --> F[Tessera bulk update — CC feeds it<br/>numbered items 30–45 min]"),
 ("H --> I{Origin / TESSERA merge:<br/>Father's explicit yes?}",
  "H --> I{\"Origin / TESSERA merge:<br/>Father's explicit yes (the word 'merge')?\"}"),
 ("| Command Center | Digests, status, and handoff coordination;",
  "| Command Center | Feeds Tessera's bulk update; status and handoff coordination;"),
 (OS_OLD, OS),
 ("prepares the evidence-linked bulk digest every 30–45 minutes while active (each push its own numbered item) and asks Father for `yes` / `no` / `revise`;",
  "feeds Tessera's evidence-linked bulk update (Tessera sends it to Father every 30–45 minutes while active and asks `yes` / `no` / `revise`; each push its own numbered item);"),
],
"mesh/roles.md": [
 ("Prepares 30–45 minute bulk digests (numbered push items) and asks Father for yes/no/revise;",
  "Feeds Tessera's 30–45 minute bulk update (numbered push items; Tessera sends it and asks Father for yes/no/revise);"),
 ("→ Tessera Grok bot / Command Center bulk digest (30–45 min; one numbered item per push) →",
  "→ Tessera's bulk update to Father, fed by Tessera Grok bot / Command Center (30–45 min; one numbered item per push) →"),
 ("→ Father separately authorizes an Origin merge with `merge`.",
  "→ Origin (`collin-keane/Tessera`) and TESSERA merges need Father's explicit yes (the word 'merge')."),
 ("Command Center coordinates and digests and never pushes GitBook or TESSERA;",
  "Command Center coordinates and feeds Tessera's bulk update and never pushes GitBook or TESSERA;"),
 ("Agents do not merge Origin without Father's explicit `merge`.",
  "Agents do not merge Origin (`collin-keane/Tessera`) or TESSERA without Father's explicit yes (the word 'merge')."),
],
"mesh/roles/command-center.md": [
 ("note: Command Center and the Tessera Grok bot prepare bulk digests only;",
  "note: Command Center and the Tessera Grok bot feed Tessera's bulk update only (Tessera sends it to Father);"),
 ("- Evidence-linked bulk digests to Father every **30–45 minutes while work is active**",
  "- Feeding Tessera's evidence-linked bulk update (Tessera sends it to Father every **30–45 minutes while work is active**)"),
 ("- Ready-state digest and handoff to Father",
  "- Ready-state input to Tessera's bulk update, and handoff coordination"),
 ("(1) merges awaiting Father's `merge`,",
  "(1) Origin / TESSERA merges awaiting Father's explicit yes (the word 'merge'),"),
 ("- Merge without Father's separate explicit `merge`",
  "- Merge anything (Tessera merges Gitbook PRs after Father's yes; Origin and TESSERA merges need Father's explicit yes, the word 'merge')"),
 ("The Tessera Grok bot may prepare and deliver the digest, but it cannot publish or merge.",
  "The Tessera Grok bot / Command Center feeds Tessera's bulk update but does not send it, publish, or merge; Tessera sends it to Father and, after his yes, pushes and merges the approved Gitbook packages."),
],
"mesh/roles/mesh-lane-map.md": [
 ("| Digest / final push coordination | Command Center |",
  "| Bulk update to Father (30–45 min) | **Tessera** sends it; Command Center feeds it |"),
 ("→ CI/Build → one Command Center digest.",
  "→ CI/Build → one Tessera bulk update (Command Center feeds it)."),
 ("9. Command Center lists each docs push as its own numbered digest item (30–45 min digest);",
  "9. Command Center feeds each docs push into Tessera's bulk update as its own numbered item (Tessera sends it every 30–45 min);"),
 ("/ no with notes (holds the items he names). A yes never",
  "/ no with notes (holds the items he names) / revise (returns the named items for the stated change). A yes never"),
 ("Origin main still needs Father’s word `merge`.", OS),
 ("**no** with notes holds the items he names. A yes never carries over",
  "**no** with notes holds the items he names. **revise** returns the named items for the stated change. A yes never carries over"),
 ("`collin-keane/Tessera` main stays put until Father’s own word **`merge`**.",
  "`collin-keane/Tessera` main stays put until Father's explicit yes (the word 'merge'). TESSERA merges need the same."),
],
"intake/how-to-submit.md": [
 ("Command Center lists it as its own numbered item in the bulk digest to Father (every 30–45 min).",
  "Command Center feeds it as its own numbered item into Tessera's bulk update to Father (Tessera sends it every 30–45 min)."),
 (OS_OLD, OS),
],
"intake/status-definitions.md": [(OS_OLD, OS)],
"review/moderator-handoff.md": [
 ("Command Center may then include Ready items in the 30–45 min digest as numbered items.",
  "Command Center may then feed Ready items into Tessera's 30–45 min bulk update as numbered items."),
 (OS_OLD, OS),
 ("- Digests to Father (Command Center; each push its own numbered digest item)",
  "- Bulk updates to Father (Tessera sends them; Command Center feeds them; each push its own numbered item)"),
 ("Origin / TESSERA: Father's explicit yes before anyone merges)",
  "Origin / TESSERA: Father's explicit yes (the word 'merge') before anyone merges)"),
],
"mesh/roles/gitbook-cordnation.md": [
 ("- Moderation (approve / reject / block)", "- Moderation (approve / reject / changes needed)"),
 ("| Command Center digest (numbered docs-push item) → Father final yes →",
  "| Tessera's bulk update, fed by Command Center (numbered docs-push item) → Father final yes →"),
],
"mesh/roles/gitbook-moderator.md": [
 ("| Approved | Eligible for Command Center digest / later Father-gated push |",
  "| Approved | Goes to Tessera → Security → CI/Build; once all four gates clear, Gitbook / Cordnation stages it Ready for Tessera's bulk update to Father (Command Center feeds it) |"),
],
"mesh/roles/build.md": [
 ("- Merge without Father's word 'merge', or push or publish before Father approves.",
  "- Merge anything (Tessera merges Gitbook PRs after Father's yes; Origin and TESSERA merges need Father's explicit yes, the word 'merge'), or push or publish before Father approves."),
],
"mesh/roles/who-tessera-is.md": [
 ("- Not a lane that merges to main without Father’s word `merge`.",
  "- Not a lane that merges without Father's explicit yes. Tessera merges Gitbook PRs after that yes; Origin and TESSERA merges need Father's explicit yes (the word 'merge')."),
 ("| Father | Orders, yes/no, merge |",
  "| Father | Orders; yes/no/revise; the word 'merge' for Origin / TESSERA merges |"),
 ("| Command Center | Digests and relays the Ready handoff to Father;",
  "| Command Center | Feeds Ready items into Tessera's bulk update to Father (Tessera sends it);"),
],
"mesh/roles/board-world-chamber.md": [
 ("The shared work surface (coordination / Command Center digest path). Lanes post as themselves. Father opens issues and says yes/no / merge.",
  "The shared work surface (coordination / Tessera's bulk-update path, fed by Command Center). Lanes post as themselves. Father opens issues and says yes/no/revise, plus the word 'merge' for Origin / TESSERA merges."),
 ("**Waiting on:** Father’s GitHub push of this Ready pack (GitBook→GitHub via his connection). No Replit.",
  "**Waiting on:** nothing for this page (published in 8010626). New docs follow the gated path: after Father's yes, Tessera pushes (Father may push himself). No Replit."),
 ("| Board | See lane work; yes/no; merge | Push merge without his word |",
  "| Board | See lane work; yes/no/revise; the word 'merge' for Origin / TESSERA | Push or merge without his yes |"),
 ("- Father has not digest-approved this note",
  "- Father's yes covered publishing this note, not the tabs' live state"),
],
"mesh/roles/pen-tone-guide.md": [
 ("no merge to Tessera main without Father’s word `merge`.",
  "no merge to Tessera main without Father's explicit yes (the word 'merge')."),
 ("→ Ready → Command Center digest → Father yes/no/revise →",
  "→ Ready → Tessera's bulk update (Command Center feeds it) → Father yes/no/revise →"),
 ("- Father has not said `merge` for that branch to Tessera main",
  "- Father has not given his explicit yes (the word 'merge') for that branch to Tessera main"),
],
"mesh/roles/grok-bot.md": [
 ("- Digests (Command Center sends them).",
  "- Bulk updates to Father (Tessera sends them; Command Center feeds them)."),
],
}
for r in ["tessera","mesh-cloud","github-scraper","open-helper-agent","recursive-learning-sponge","tessera-brain-consciousness"]:
    E[f"mesh/roles/{r}.md"] = [(BANNER, "")]
bad = 0
for f, reps in E.items():
    p = os.path.join(root, f); s = open(p, encoding="utf-8").read()
    for old, new in reps:
        n = s.count(old)
        if n != 1:
            print(f"FAIL {f}: count={n}: {old[:70]!r}"); bad += 1; continue
        s = s.replace(old, new)
    open(p, "w", encoding="utf-8").write(s)
# item 1: restore command-center record (262 bytes, no trailing newline)
shutil.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "command-center.restored.md"),
                os.path.join(root, "history/coordination/command-center.md"))
print("edits:", sum(len(v) for v in E.values()), "files:", len(E) + 1, "failures:", bad)
sys.exit(1 if bad else 0)
