#!/bin/sh
# Full-picture palace build (Tessera v3 step). Read-only over sources; writes palace.db only.
cd "$(dirname "$0")"
PALACE_SHALLOW=/workspace/rea-batch PALACE_ROOTS=/workspace/rick:/workspace/rick/src/Gitbook:/workspace/TESSERA-ro:/workspace/tess-opt:/workspace/tw:/workspace/rea-batch:/workspace/tessera-brain:/workspace/cloud-agent-transcripts:/workspace/full-picture:/workspace/gitbook-cordnation PALACE_EXT=.md:.txt:.json:.log PALACE_MAXF=65536 python3 palace.py build
