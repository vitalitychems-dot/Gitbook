# fullpicture: memory graph (Tessera v3 step 0)
1. `../palace/rebuild-full.sh` indexes every local clone, Gitbook, rick-audit text, the rea-batch summaries, logs and transcripts dir → palace.db (97MB)
2. `python3 graph.py` → graph.json (nodes, edges, coverage) + graph.mmd (top-80 edges, mermaid)
3. `python3 test_graph.py`
Edge types: mentions (a doc chunk owned by node A names node B), references (markdown link to a rule doc), imports (@workspace package deps).
