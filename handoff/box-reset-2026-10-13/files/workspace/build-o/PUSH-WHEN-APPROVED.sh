#!/bin/bash
# NOT RUN. Each block is a separate externally visible action; run only with Father's explicit yes.
set -e
R=/workspace/rea-batch
# 1) GB-063 rev3 (Gitbook, base 56a7a48d, local commit 10c2531)
cd $R/b2-Gitbook && git push -u origin gb-063-rev3 && gh pr create -R vitalitychems-dot/Gitbook -H gb-063-rev3 -B main -t "GB-063 rev3: intake log update" -b "Diff sha256 f0b2eca5a7cd0ec3ff5258d064d7b45fe39be1e3a073de604c95366f8065d5e2, base 56a7a48d. Four gates passed on rev2; Father yes 5:08 PM CT bulk list."
#    then: gh pr merge <N> -R vitalitychems-dot/Gitbook --merge   (only if mergeable)
# 2) Rename + GitMesh refs
#    gh repo rename GitMesh -R vitalitychems-dot/GitbookAI --yes
#    cd $R/b2-GitbookAI && git remote set-url origin https://github.com/vitalitychems-dot/GitMesh.git && git push -u origin gitmesh-rename && gh pr create -R vitalitychems-dot/GitMesh -H gitmesh-rename -B main -t "Rename GitbookAI to GitMesh" -b "linkcheck: 3 files, 0 broken; mesh/index.json valid JSON"
#    cd $R/b2-Gitbook && git push -u origin gitmesh-rename-docs && gh pr create -R vitalitychems-dot/Gitbook -H gitmesh-rename-docs -B main -t "Docs: GitbookAI -> GitMesh" -b "4 files; archive/ untouched; linkcheck 0 broken"
# 3) Open-only PRs (do NOT merge)
#    TESSERA branches: o1-offline-index o2-offline-queue o3-service-worker o4-kiwix-optional o5-usb-bundle o6-lan-p2p o7-mesh-badge i12-hyb011-exclusions o10-node-per-install
#    Gitbook branches: o8-offline-internet-page o9-lora-research-note
#    for each: git push -u origin <br> && gh pr create -B main -H <br> --body "<receipt line from receipts.txt>"
