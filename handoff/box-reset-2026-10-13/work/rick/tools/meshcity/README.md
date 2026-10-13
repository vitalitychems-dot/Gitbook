# Mesh City (invention #13)
Offline 3D city of the mesh. `python3 gen.py` reads local data only and writes city.json, then embeds it in index.html. Open index.html in a browser (no network, canvas 3D by hand). Drag to orbit, scroll to zoom, click a building to see its stats.
- Blue = agents. Height = f(files in the dirs it owns, files mentioning it in TESSERA-ro, gitbook-gate-1e3bb50 and rick). A null `files` value plus an `unknown` note means no owned dir was found.
- Orange = workshops (rick/tools/*, qlab). Height comes from the file count.
- Purple = library district (palace.py rooms). Height comes from the doc count.
- Ground = diskguard --json: green <90%, amber 90-95%, red >=95%.
Tests: `python3 test_meshcity.py` (schema, determinism, the HTML parses, no external URLs). shot.png is a headless Chrome render.
Caveat: the ownership mapping is a heuristic guess by dir name, and the mention counts are capped at 3000 files per agent.
