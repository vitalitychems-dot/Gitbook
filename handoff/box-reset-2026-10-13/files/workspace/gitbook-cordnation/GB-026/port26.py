import sys, os
os.chdir(sys.argv[1])
ISSUE2 = "[Gitbook issue #2](https://github.com/vitalitychems-dot/Gitbook/issues/2)"
BANNER_READY = "> **Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)**\n\n"
NOTE_READY_OLD = "status: approved\nnote: Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)\n"
NOTE_READY_NEW = "status: published\nnote: Published 2026-10-05 (commit 8010626); Father Yes 2026-10-05; testers WAIVED / not checked\n"
BANNER_98 = "> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**\n\n"

E = {}
def ed(path, old, new):
    E.setdefault(path, []).append((old, new))

# ---- Ruling 1
ed("mesh/roles/tessera-pen.md",
 "- vitalitychems-dot/tessera-coordination — PEN.md, COORDINATION.md, COMMAND.md, STATUS.md\n",
 "- `history/coordination/` (merged from the deleted tessera-coordination repo) — [PEN.md](../../history/coordination/tessera-pen-record.md), [COORDINATION.md](../../history/coordination/coordination-record.md), [COMMAND.md](../../history/coordination/command-center.md); STATUS.md is at [`history/recovered/coordination/STATUS.md`](../../history/recovered/coordination/STATUS.md)\n")

# ---- Ruling 2
ed("mesh/flow.md",
 "Never pushes GitBook or TESSERA; see issue **#2** / `COMMAND.md`.",
 "Never pushes GitBook or TESSERA. Coordination board: [Gitbook issue **#2**](https://github.com/vitalitychems-dot/Gitbook/issues/2); `COMMAND.md` is Command Center's command file.")
ed("mesh/roles/command-center.md",
 "- References: issue **#2** / `COMMAND.md`\n",
 "- References: [Gitbook issue **#2**](https://github.com/vitalitychems-dot/Gitbook/issues/2) (the coordination board); `COMMAND.md` (Command Center's command file)\n")

# ---- Ruling 3 (banners)
ed("mesh/roles.md", "> **Status: published — operating model aligned**\n\n", "")
ed("mesh/roles/command-center.md", "> **Status: published — authority wording aligned**\n\n", "")
ed("mesh/roles/gitbook-moderator.md", BANNER_98, "")
ed("mesh/roles/pen-tone-guide.md", BANNER_98, "")

# ---- Ruling 4
ed("review/moderator-handoff.md",
 "no with notes holds the items he names; a yes never carries over",
 "no with notes holds the items he names; revise returns the named items for the stated change; a yes never carries over")

# ---- Ruling 5: GB-004..014 pages
for p in ["mesh/roles/who-tessera-is.md","mesh/roles/board-world-chamber.md","mesh/roles/honesty-banner.md",
          "mesh/roles/pen-ability-set-framing.md","mesh/roles/pen-gate-refuse-companion.md","mesh/roles/refuse-and-offer.md"]:
    ed(p, NOTE_READY_OLD, NOTE_READY_NEW)
    ed(p, BANNER_READY, "")
ed("mesh/roles/gitbook-moderator.md",
 "- Decide on intake items: **approve**, **reject**, or **block**\n",
 "- Decide on intake items: **approve**, **reject**, or **changes needed**\n")
ed("mesh/roles/gitbook-moderator.md",
 "| Blocked | Held; does not proceed to digest/push until unblocked or resubmitted per Moderator note |\n",
 "| Changes needed | Held; does not proceed to digest/push until fixed and resubmitted per Moderator note |\n")
ed("mesh/roles/who-tessera-is.md",
 "| Command Center | Digests and relays the Ready handoff to Father; does not push |\n",
 "| Command Center | Digests and relays the Ready handoff to Father; pushes only the Replit app set (privately, after all four gates and Father's yes); never pushes GitBook or TESSERA |\n")
ed("mesh/roles/pen-tone-guide.md",
 "6. Mesh path: GitBook draft → Moderator → digest → Father yes → private Replit.\n",
 "6. Mesh path: GitBook draft → Cordnation → Moderator → Tessera → Security → CI/Build → Ready → Command Center digest → Father yes/no/revise → Tessera pushes the approved package (PR, Build verifies, Tessera merges), or Father pushes himself. Replit is never a GitBook path.\n")
ed("mesh/roles/pen-tone-guide.md",
 "Pen → Cordnation (intake) → Moderator (gate) → digest → Father.",
 "Pen → Cordnation (intake) → Moderator → Tessera → Security → CI/Build → digest → Father.")
ed("history/coordination/AGENT-TRAINING-AUTHENTICITY.md",
 "- **Pen** is the coordination/editorial layer that frames tasks, protects boundaries, assigns work, and keeps the record coherent. Pen does not silently impersonate Tessera or other agents.\n",
 "- **Pen** is Tessera's own writing voice (her editorial layer), not a separate agent, lane, or gate. It frames text, protects boundaries, and keeps the record coherent. **Tessera**, not Pen, assigns work. Pen does not silently impersonate Tessera or other agents.\n")
ed("history/coordination/AGENT-TRAINING-AUTHENTICITY.md",
 "Pen assigns one task at a time and protects scope. Tessera reviews proposed behavior",
 "Tessera assigns one task at a time and protects scope (Pen is her writing voice, not the assigner). Tessera reviews proposed behavior")
ed("history/coordination/AGENT-TRAINING-AUTHENTICITY.md",
 "| Pen coordination is visible | Assignment, rationale, and status transitions are recorded |\n",
 "| Tessera's assignments are visible | Assignment, rationale, and status transitions are recorded |\n")
ed("README.md", "---\nstatus: staged\n---\n", "---\nstatus: published\n---\n")

# ---- Ruling 6: Tessera pushes after Father's yes
RULE = ("After Father's yes, **Tessera** pushes the approved GitBook packages: she opens a PR, Build verifies it, "
        "then Tessera merges and posts on " + ISSUE2 + " (Father's rule, 3:59 PM CT). Father may still push himself.")
OM = "mesh/TESSERA-GITBOOK-OPERATING-MODE.md"
ed(OM, "assigns tasks; second review gate (after Moderator) | Does not invent agent activity or bypass the review gates |",
       "assigns tasks; second review gate (after Moderator); after Father's yes, pushes the approved Gitbook packages (opens a PR, Build verifies, Tessera merges and posts on issue #2) | Does not invent agent activity or bypass the review gates; pushes and merges only what Father's yes lists |")
ed(OM, "| Build | Independent verification of proposed results (CI/Build, fourth gate) |",
       "| Build | Independent verification of proposed results (CI/Build, fourth gate); verifies Tessera's push PR before she merges |")
ed(OM, "| Father / human owner | Final bulk approval and GitHub publication authority |",
       "| Father / human owner | Final bulk approval; may still push approved Gitbook changes himself |")
ed(OM, "11. On `yes`, Father alone publishes the approved Gitbook changes to GitHub.",
       "11. " + RULE.replace("After Father's yes, **Tessera** pushes", "On `yes`, **Tessera** pushes"))
ed(OM, "12. A separate explicit `merge` is required for any Origin/main merge.",
       "12. A separate explicit `merge` is required for any Origin merge (`collin-keane/Tessera`).")

F = "mesh/flow.md"
ed(F, "After `yes`, **Father alone pushes GitBook → GitHub** on his authenticated connection.",
      "After `yes`, **Tessera pushes the approved GitBook packages**: she opens a PR, Build verifies it, then Tessera merges and posts on " + ISSUE2 + " (Father's rule, 3:59 PM CT). Father may still push himself on his authenticated connection.")
ed(F, "→ for listed docs items, **Father** alone pushes the approved GitBook changes → GitHub (Replit is never a GitBook publication path)",
      "→ for listed docs items, **Tessera** pushes the approved GitBook package: she opens a PR, **Build** verifies it, Tessera merges and posts on Gitbook issue #2; Father may still push himself (Replit is never a GitBook publication path)")
ed(F, "  G -->|yes — listed docs item| H[Father pushes<br/>GitBook → GitHub<br/>Replit outside that path]\n",
      "  G -->|yes — listed docs item| H[Tessera opens PR → Build verifies<br/>→ Tessera merges + posts on issue #2<br/>Father may push himself; Replit outside]\n")
ed(F, "  H --> I{Father explicit merge?}\n", "  H --> I{Origin merge:<br/>Father explicit merge?}\n")
ed(F, "(1) GitBook docs: **Father** alone pushes GitBook → GitHub after Ready yes on the listed digest item — Replit outside that path.",
      "(1) GitBook docs: after Father's yes on the listed digest item, **Tessera** pushes the approved package (opens a PR, Build verifies, Tessera merges and posts on Gitbook issue #2); Father may still push himself — Replit outside that path.")
ed(F, "| Merge authority | Origin merges need Father's separate explicit `merge`. |",
      "| Merge authority | Origin merges need Father's separate explicit `merge`. Approved GitBook package PRs: Tessera merges after Father's yes and Build's verification. |")
ed(F, "- **Tessera** — admin/product-truth voice and implementation target; does not fabricate agent activity or bypass approval.\n",
      "- **Tessera** — admin/product-truth voice and implementation target; does not fabricate agent activity or bypass approval. After Father's yes, pushes the approved GitBook packages (PR → Build verifies → Tessera merges → posts on Gitbook issue #2).\n")
ed(F, "- **Build** — verify-only; report TESTED versus REPORTED.\n",
      "- **Build** — verify-only; report TESTED versus REPORTED; verifies Tessera's push PR before she merges.\n")

R = "mesh/roles.md"
ed(R, "note: TESSERA is the product repository; Gitbook is the agent workspace; Father retains final bulk approval and push authority.\n",
      "note: TESSERA is the product repository; Gitbook is the agent workspace; Father retains final bulk approval; after his yes Tessera pushes approved Gitbook packages (Father may push himself).\n")
ed(R, "**GitBook docs track** (the single canonical GitBook path; Father pushes)",
      "**GitBook docs track** (the single canonical GitBook path; Tessera pushes after Father's yes)")
ed(R, "→ **Father alone pushes the approved Gitbook changes to GitHub** on his authenticated connection (docs items) →",
      "→ **Tessera pushes the approved Gitbook packages** (docs items): she opens a PR, Build verifies it, then Tessera merges and posts on Gitbook issue #2; Father may still push himself →")

CC = "mesh/roles/command-center.md"
ed(CC, "note: Command Center and the Tessera Grok bot prepare bulk digests only; Father is sole GitBook → GitHub push authority.\n",
       "note: Command Center and the Tessera Grok bot prepare bulk digests only; after Father's yes, Tessera pushes approved GitBook packages (Father may push himself).\n")
ed(CC, "- Push GitBook → GitHub (Father alone performs that push after Ready yes on the listed docs item;",
       "- Push GitBook → GitHub (after Father's yes on the listed docs item, Tessera pushes it via PR, Build verifies, Tessera merges; Father may still push himself;")
ed(CC, "is never a GitBook publication path; Father alone pushes GitBook → GitHub. The Tessera Grok bot",
       "is never a GitBook publication path; after Father's yes, Tessera pushes approved GitBook packages (Father may still push himself). The Tessera Grok bot")
ed(CC, "Replit is never a GitBook publication path, and Father alone pushes GitBook → GitHub.\n",
       "Replit is never a GitBook publication path, and after Father's yes Tessera pushes approved GitBook packages (Father may still push himself).\n")

ML = "mesh/roles/mesh-lane-map.md"
ed(ML, "note: Father is sole GitBook → GitHub push authority; Command Center coordinates only.\n",
       "note: After Father's yes, Tessera pushes approved GitBook packages (Father may push himself); Command Center coordinates only.\n")
ed(ML, "| GitBook → GitHub push | **Father** on his GitHub connection (after Ready yes on the listed digest item). Replit outside that path. |",
       "| GitBook → GitHub push | **Tessera** after Father's yes on the listed digest item: opens a PR, Build verifies, Tessera merges and posts on Gitbook issue #2. Father may still push himself on his GitHub connection. Replit outside that path. |")
ed(ML, "11. **Father** pushes GitBook → GitHub on his GitHub connection\n",
       "11. **Tessera** opens a PR with the approved package; **Build** verifies it; Tessera merges and posts on Gitbook issue #2 (Father may still push himself on his GitHub connection)\n")
ed(ML, "Replit is never a GitBook publication path, and Father alone pushes GitBook → GitHub.\n",
       "Replit is never a GitBook publication path, and after Father's yes Tessera pushes approved GitBook packages (Father may still push himself).\n")

ed("mesh/roles/open-helper-agent-2.md",
 "(Father alone pushes GitBook → GitHub after Ready yes on the listed docs item;",
 "(after Father's yes on the listed docs item, Tessera pushes it via PR, Build verifies, Tessera merges; Father may still push himself;")
ed("mesh/roles/build.md",
 "- Mark TESTED only from output Build ran itself; otherwise REPORTED.\n",
 "- Mark TESTED only from output Build ran itself; otherwise REPORTED.\n- Verify Tessera's PR for each approved GitBook package before she merges it.\n")
ed("mesh/roles/build.md",
 "Father alone pushes GitBook→GitHub via his connection; Replit outside that path.",
 "After Father's yes, Tessera pushes approved GitBook packages via PR (Build verifies; Tessera merges); Father may still push himself via his connection; Replit outside that path.")
ed("mesh/roles/grok-bot.md", "- Never to main (Father alone pushes main).",
   "- Never to main (after Father's yes, Tessera merges approved packages to main; Father may push himself).")
ed("mesh/roles/grok-bot.md", "pushes to main (Father only).", "pushes to main (Tessera after Father's yes, or Father).")
ed("mesh/roles/gitbook-cordnation.md", "→ Father final yes → Father push |",
   "→ Father final yes → Tessera push (PR, Build verifies, Tessera merges) or Father's own push |")
ed("intake/how-to-submit.md",
 "4. After Father approves, **Father alone** pushes GitBook → GitHub on his authenticated connection; Replit is outside that path.",
 "4. After Father approves, **Tessera** pushes the approved package: she opens a PR, Build verifies it, then she merges and posts on Gitbook issue #2. Father may still push himself on his authenticated connection. Replit is outside that path.")
ed("intake/status-definitions.md",
 "Push requires Father's final yes on the listed item; merge requires Father's separate explicit `merge`.",
 "Push requires Father's final yes on the listed item (then Tessera opens a PR, Build verifies, Tessera merges; Father may push himself); an Origin merge requires Father's separate explicit `merge`.")
MH = "review/moderator-handoff.md"
ed(MH, "GitBook docs: Father alone pushes after Father's final yes on the listed digest item (Replit",
       "GitBook docs: after Father's final yes on the listed digest item, Tessera pushes (opens a PR, Build verifies, Tessera merges and posts on Gitbook issue #2); Father may still push himself (Replit")
ed(MH, "Merge only on Father's explicit `merge`. |", "Origin merge only on Father's explicit `merge`. |")
ed(MH, "- GitBook docs push (Father only, after Ready yes on the listed item;",
       "- GitBook docs push (Tessera after Father's yes on the listed item, via a PR Build verifies; or Father himself;")
ed(MH, "- Merges (Father only)\n",
       "- Merges (approved GitBook package PRs: Tessera after Father's yes; Origin: Father's explicit `merge`)\n")

bad = 0
for p, lst in E.items():
    s = open(p, encoding="utf-8").read()
    for old, new in lst:
        n = s.count(old)
        if n != 1:
            print("ANCHOR", n, p, old[:70]); bad += 1; continue
        s = s.replace(old, new)
    open(p, "w", encoding="utf-8").write(s)
print("files", len(E), "edits", sum(len(v) for v in E.values()), "bad", bad)
sys.exit(1 if bad else 0)
