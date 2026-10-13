# Tessera (admin)
Instructions: decides and assigns all lanes. Moderator gates everything, then Security and Build; merge only after all PASS on the head SHA and CI is green. Hard limits: no wallets or crypto; no deletes without a list and Father's explicit yes; no history rewrites; no TESSERA_ENABLE_* flips; only edit TESSERA and Gitbook; noreply commit identity; no private data in public TESSERA; never touch the 1T vault; free tier only. Locked paths need Father's collink1007 review.
Left off (9:03 AM CT 2026-10-13):
- Father approved (9:01) Security and Build each posting their own verdicts. Both say they'll post only after Father says yes in their own chats.
- PRs with full PASSes that aren't posted yet: TESSERA #316, #317, #318, #314, #310; Gitbook #90, #92 @7ed7edb0, #96 @77c387f1, #97.
- #312 and #313 were merged by Mesh Cloud. Their content is clean, but they got a process FAIL: the squash author shows as "Tessera" (Father has to fix his GitHub profile name), and CI was still running at merge time.
- Gitbook #91 has Moderator FAIL because CI never ran on its head.
- The new-UI cloud agent bc-2a272c39 is running.
- Pending Father's answer: deleting /tmp/gb-scan (stray natal copy), and the 44 gitleaks hits in the Gitbook archive.
Next: post the gate verdicts, let the hourly timer merge, run the UI's 3 version rounds, and install the selfbuild Apps (Father).