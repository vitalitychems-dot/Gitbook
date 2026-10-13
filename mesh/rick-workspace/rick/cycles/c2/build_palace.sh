#!/bin/sh
# c2 coverage fix: same roots as rebuild-full.sh, but large files are chunked instead of skipped (cap 64KB -> 256KB). Writes c2/palace.db only.
cd "$(dirname "$0")"; R=/workspace/rick/tools/palace
PALACE_DB=$PWD/palace.db PALACE_SHALLOW=/workspace/rea-batch PALACE_ROOTS=/workspace/rick:/workspace/rick/src/Gitbook:/workspace/TESSERA-ro:/workspace/tess-opt:/workspace/tw:/workspace/rea-batch:/workspace/tessera-brain:/workspace/cloud-agent-transcripts:/workspace/full-picture:/workspace/gitbook-cordnation PALACE_EXT=.md:.txt:.json:.log PALACE_MAXF=262144 python3 $R/palace.py build
