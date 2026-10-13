# Keyless live data sources for the mesh gateway node (2026-10-12 CT)

What this is: free sources that need no API key and no login. A gateway node fetches them, signs each packet, and relays it to offline nodes.
How they were found: a grep of the local clones (TESSERA f6c9362, Gitbook, XXX, z, amber, fleet-moss, TheTesseractAI/18). "Hits" is how many times the URL shows up there. Rows marked "well-known" were added from public docs.
Rules for every source: send a real User-Agent with contact info, cache, back off on 429, and keep the license note on each relayed packet. Nothing on this list needs scraping behind a login or getting past bot protection.
The rate limits come from each provider's published docs as I remember them. They can change, so re-check a source's ToS before turning it on.

| Source | Endpoint | Data type | License / ToS | Rate limit | Hits |
|---|---|---|---|---|---:|
| Wikipedia REST/Action API | en.wikipedia.org/api/rest_v1, /w/api.php | Encyclopedia text, summaries | CC BY-SA 4.0 (credit + share-alike) | No hard cap; ~200 req/s guideline, UA required | 11536 |
| Wikidata | www.wikidata.org/w/api.php, query.wikidata.org/sparql | Structured facts (entities) | CC0 | SPARQL 60 s query time/min per IP | 7 |
| arXiv API + RSS | export.arxiv.org/api/query, rss.arxiv.org | Paper metadata, abstracts | Metadata CC0; PDFs per-paper license | 1 req / 3 s | 9733 |
| GitHub REST (unauth) | api.github.com | Public repo/issue/release data | GitHub ToS | 60 req/h per IP without token | 3345 |
| npm registry | registry.npmjs.org | Package metadata | npm ToS | Generous; cache | 12648 |
| PyPI JSON | pypi.org/pypi/<pkg>/json | Package metadata | PSF ToS | Generous; cache | 16 |
| NASA EONET | eonet.gsfc.nasa.gov/api/v3 | Live natural events (fires, storms) | US Gov public domain | Not published; be polite | 803 |
| NASA Image Library | images-api.nasa.gov | Images + metadata | Mostly public domain (check per item) | Not published | 1889 |
| NASA SSCWeb | sscweb.gsfc.nasa.gov | Spacecraft positions | Public domain | Not published | 802 |
| CelesTrak | celestrak.org/NORAD/elements/gp.php | Satellite orbit elements | Free use, credit CelesTrak | Data updates ~every 2 h; don't poll faster | 802 |
| USGS Earthquakes | earthquake.usgs.gov/earthquakes/feed/v1.0 (GeoJSON) | Live quakes | Public domain | Feeds refresh each minute; no key | 292 |
| NOAA/NWS | api.weather.gov | US forecasts, alerts | Public domain; UA required | Unpublished, ~a few req/s | 152 |
| NOAA SWPC (well-known) | services.swpc.noaa.gov/json | Space weather | Public domain | Static JSON; poll ≥1 min | 0 |
| Open-Meteo | api.open-meteo.com, geocoding-, archive-, air-quality- | Weather, history, air quality, geocoding | CC BY 4.0; free for non-commercial | 10k/day, 5k/h, 600/min | 57 |
| OpenStreetMap Nominatim | nominatim.openstreetmap.org | Geocoding | ODbL; usage policy: max 1 req/s, no bulk, UA required | 1 req/s | 24 |
| OSM Overpass (well-known) | overpass-api.de/api/interpreter | Map features | ODbL | ~10k queries/day, fair use | 0 |
| OSM tiles | tile.openstreetmap.org | Map tiles | ODbL; tile policy bans heavy/offline bulk download (use own tile server for offline packs) | Light use only | 8 |
| Hacker News | hacker-news.firebaseio.com/v0 | Stories, comments | Public; YC ToS | No limit stated | 167 |
| HN Algolia (well-known) | hn.algolia.com/api/v1 | HN search | Public | ~10k/h per IP | 0 |
| GDELT (well-known) | api.gdeltproject.org/api/v2/doc | Global news events | Free, credit GDELT | ~1 req / 5 s | 0 |
| Semantic Scholar | api.semanticscholar.org/graph/v1 | Paper graph | S2 API license; non-key shared pool | ~1 req/s shared, 429s common | 402 |
| OpenAlex (well-known) | api.openalex.org | Scholarly works graph | CC0 | 100k/day, 10 req/s (add mailto=) | 0 |
| Crossref (well-known) | api.crossref.org | DOI metadata | Metadata mostly CC0 | Polite pool with mailto | 0 |
| NCBI E-utilities | eutils.ncbi.nlm.nih.gov | PubMed metadata | Public; NLM terms | 3 req/s without key | 291 |
| Europe PMC (well-known) | www.ebi.ac.uk/europepmc/webservices/rest | Biomedical literature | Open; per-article license | Fair use | 0 |
| data.gov CKAN | catalog.data.gov/api/3 | US gov dataset catalog | Public domain mostly | Fair use | 390 |
| World Bank | api.worldbank.org/v2 | Development indicators | CC BY 4.0 | Fair use | 128 |
| Internet Archive | archive.org/advancedsearch.php, /wayback/available | Archived pages, media metadata | Per-item rights; IA ToS | Fair use, back off on 429 | 287 |
| Open Library | openlibrary.org/*.json | Books metadata | CC0 metadata | ~1 req/s guideline | 51 |
| Gutendex | gutendex.com/books | Project Gutenberg catalog | Public-domain texts | Fair use | 44 |
| Frankfurter | api.frankfurter.app | ECB reference FX rates (daily, info only; not for trading) | Free, ECB data | Fair use | 84 |
| REST Countries | restcountries.com/v3.1 | Country facts | MPL-2.0 | Fair use | 12 |
| PokeAPI | pokeapi.co/api/v2 | Fixture/demo data | Fair use, cache required | ~100/min | 488 |
| Wikimedia EventStreams (well-known) | stream.wikimedia.org/v2/stream/recentchange | Live edit stream (SSE) | CC BY-SA / CC0 | One connection per client | 0 |

## Seen in the repos but left out
- api.coingecko.com, coingecko.com: crypto prices. The crypto category is excluded.
- ip-api.com, ipapi.co: geolocation by IP. That's close to people-OSINT, and ip-api's free tier is HTTP-only and non-commercial.
- www.reddit.com, oauth.reddit.com: the API needs OAuth and app registration now.
- api.nasa.gov: needs a key (DEMO_KEY is capped at 30/h). Use the keyless NASA hosts listed above instead.
- openexchangerates.org, api.exchangerate.host: these need keys now.
- numbersapi, catfact, quotable, worldtimeapi, jsonplaceholder: toy or unreliable sources (quotable and worldtimeapi have had outages). Use them only as test fixtures.

## Gateway notes
- The gateway is the only node that touches the internet. Offline nodes only get signed packets (source, URL, fetched_at, sha256, license, and the gateway's ed25519 signature).
- Each source keeps its own budget, set to the limits above. Packets carry a TTL so stale data shows up marked as stale.
