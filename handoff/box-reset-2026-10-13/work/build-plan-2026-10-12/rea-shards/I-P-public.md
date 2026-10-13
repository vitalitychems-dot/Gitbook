# I-P shard — public upstream pass (2026-10-12 ~7:15 PM CT, read-only)

**Counts:** 65 repos — TESTED 19 · BLOCKED 26 · SKIPPED-EXCLUDED 20.
Method: gh search repos (exact name, sorted by stars, non-forks) plus well-known canonical upstreams; shallow clones in /workspace/rea-batch/<name>; rea-agents@6.4.0 (Node 22) on JS/TS repos, rg/LOC counts on the rest. No repo code executed; nothing written to GitHub. A fuzzy-only match (unrelated author/purpose) = BLOCKED.

**Top candidates:** 1) postlight/parser (mercury-parser), content ingest · 2) postmanlabs/postman-collection, API docs schema · 3) NaturalNode/natural, text tagging · 4) mailgun/mailgun.js, notifications · 5) Kong/insomnia, auth/request modules only. onnxruntime/puppeteer: depend via npm, don't absorb.

**Risk flags (paths only, no values printed):** key-pattern hits are test fixtures: mechanize/test/data/server.key, mechanize/test/data/server.pem; insomnia/packages/insomnia/src/network/__tests__/authentication.test.ts; mailgun-js/tests/module/domainKeys.test.ts. nmap/scripts/*brute*.nse = credential brute-force scripts, so don't absorb. passive-income-bot: the closest public match is a DyDx liquidator (crypto), so it's left BLOCKED and wasn't cloned. Sovereign-core/collink repos have no public copies.

**Note:** all % changes are ESTIMATEs (judgement); only the files/LOC/REA columns are MEASURED.

| repo | status | url | what it improves in TESSERA | metrics | % change | MEASURED/ESTIMATE + reason |
|---|---|---|---|---|---|---|
| collink1007/olive-giant-ever-glade | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/Multilogin | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/image-captcha-solver | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/infographic-data | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/insomnia | TESTED | https://github.com/Kong/insomnia | API client/request-collection model + auth helpers for TESSERA tools/api-client | files=2291, code LOC=381865, risk-keyword files=17, REA jsfiles=1660 findings=13236 parsefail=27 | +10% API-debug coverage | metrics MEASURED (static count/REA); improvement ESTIMATE: Electron app; only data/auth modules reusable |
| nicholasgasior/intermarket-analysis | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/inventory-management | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/keyword-research-tool | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/lemon-squeezy-sdk | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/lattigo | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/landing-page-builder | TESTED | https://github.com/withpulp/landing-page-builder | Tiny static landing template | files=62, code LOC=714, risk-keyword files=0, REA jsfiles=22 findings=9 parsefail=0 | ~1% | metrics MEASURED (static count/REA); improvement ESTIMATE: 714 LOC, 14★ |
| nicholasgasior/kyber | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/libsodium | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/liquidity-mining | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/linkedin-ads-api | TESTED | https://github.com/Smietje77/linkedin-ads-api | Small ads API wrapper (0★, unknown author) | files=7, code LOC=1136, risk-keyword files=0 | ~1% | metrics MEASURED (static count/REA); improvement ESTIMATE: unvetted |
| nicholasgasior/mailgun-js | TESTED | https://github.com/mailgun/mailgun.js | Typed email-send client for notifications | files=551, code LOC=35381, risk-keyword files=0, REA jsfiles=459 findings=2581 parsefail=1 | +5% notify reliability | metrics MEASURED (static count/REA); improvement ESTIMATE: small, TS, drop-in |
| nicholasgasior/market-correlation | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/marketstack | TESTED | https://github.com/apilayer/marketstack | Single-file README only | files=1, code LOC=0, risk-keyword files=0 | 0% | metrics MEASURED (static count/REA); improvement ESTIMATE: no code |
| nicholasgasior/mechanize | TESTED | https://github.com/sparklemotion/mechanize | Ruby stateful HTTP/form agent — reference only, wrong stack | files=212, code LOC=18681, risk-keyword files=4 | ~0% | metrics MEASURED (static count/REA); improvement ESTIMATE: Ruby, TESSERA is JS/TS |
| nicholasgasior/mercury-parser | TESTED | https://github.com/postlight/parser | Article/content extraction for TESSERA ingest (Historical Analysis) | files=719, code LOC=51195, risk-keyword files=9, REA jsfiles=516 findings=1993 parsefail=0 | +15% ingest quality | metrics MEASURED (static count/REA); improvement ESTIMATE: mature extractor, JS-native |
| nicholasgasior/mev-templates | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/meta-tag-generator | TESTED | https://github.com/PragatiVerma18/Meta-Tag-Generator | SEO meta-tag helper for Gitbook pages | files=25, code LOC=678, risk-keyword files=0, REA jsfiles=11 findings=62 parsefail=0 | ~2% | metrics MEASURED (static count/REA); improvement ESTIMATE: 678 LOC demo |
| nicholasgasior/micro-saas-template | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/microwork-platform | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/moltbook-platform | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/natural-nlp | TESTED | https://github.com/NaturalNode/natural | Tokenize/stem/classify for tagging docs | files=378, code LOC=32402, risk-keyword files=2, REA jsfiles=293 findings=914 parsefail=0 | +10% tagging | metrics MEASURED (static count/REA); improvement ESTIMATE: pure JS, no model download |
| nicholasgasior/ml5-js | TESTED | https://github.com/ml5js/ml5-next-gen | Browser ML wrappers — low fit | files=186, code LOC=15748, risk-keyword files=1, REA jsfiles=107 findings=602 parsefail=0 | ~2% | metrics MEASURED (static count/REA); improvement ESTIMATE: browser/demo oriented |
| nicholasgasior/newsletter-builder | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/nmap | TESTED | https://github.com/nmap/nmap | Network scanner — not an absorb target | files=2611, code LOC=594713, risk-keyword files=13 | 0% | metrics MEASURED (static count/REA); improvement ESTIMATE: C security tool; NSE brute-force scripts present |
| nicholasgasior/nft-minter | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/newspaper3k | TESTED | https://github.com/codelucas/newspaper | Python article extraction (alt to mercury-parser) | files=419, code LOC=6125, risk-keyword files=9 | +5% | metrics MEASURED (static count/REA); improvement ESTIMATE: Python, duplicates mercury-parser |
| nicholasgasior/onnxruntime-web | TESTED | https://github.com/microsoft/onnxruntime | Local inference runtime (use npm onnxruntime-web pkg, not source) | files=11412, code LOC=3387362, risk-keyword files=20 | +10% if local models needed | metrics MEASURED (static count/REA); improvement ESTIMATE: 3.4M LOC monorepo; depend, don't absorb |
| nicholasgasior/nodriver | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/options-flow | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/noise-protocol | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/openssl | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/order-fulfillment | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/oxylabs-sdk | TESTED | https://github.com/oxylabs/oxylabs-sdk-python | Paid proxy/scraper SDK client | files=220, code LOC=19650, risk-keyword files=0 | ~0% | metrics MEASURED (static count/REA); improvement ESTIMATE: vendor-locked, Python |
| nicholasgasior/page-speed-analyzer | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/paddle-sdk | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/passive-income-bot | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/pinterest-ads-api | TESTED | https://github.com/kayr-jpg/pinterest-ads-api | Small ads API wrapper (0★) | files=5, code LOC=931, risk-keyword files=0 | ~1% | metrics MEASURED (static count/REA); improvement ESTIMATE: unvetted |
| nicholasgasior/plaid-node | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/playwright-python | TESTED | https://github.com/microsoft/playwright-python | Browser automation (Python); TESSERA should use JS Playwright pkg | files=435, code LOC=111398, risk-keyword files=2 | ~2% | metrics MEASURED (static count/REA); improvement ESTIMATE: wrong language |
| nicholasgasior/playwright-stealth | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/podcast-outline-gen | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/playwright-cf-bypass | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/postman-collection | TESTED | https://github.com/postmanlabs/postman-collection | Collection schema/SDK for API docs in Gitbook | files=126, code LOC=30206, risk-keyword files=0, REA jsfiles=94 findings=801 parsefail=0 | +10% API-doc structure | metrics MEASURED (static count/REA); improvement ESTIMATE: small, JS, schema-driven |
| nicholasgasior/price-comparison | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/press-release-writer | TESTED | https://github.com/741955148-cell/press-release-writer | No source code (docs/prompts only) | files=18, code LOC=0, risk-keyword files=0 | 0% | metrics MEASURED (static count/REA); improvement ESTIMATE: 0 code LOC |
| nicholasgasior/product-description-ai | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/product-sourcing-api | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/programmatic-advertising | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| nicholasgasior/puppeteer-core | TESTED | https://github.com/puppeteer/puppeteer | Headless browser automation (depend via npm) | files=1566, code LOC=106611, risk-keyword files=0, REA jsfiles=496 findings=3330 parsefail=6 | +5% QA automation | metrics MEASURED (static count/REA); improvement ESTIMATE: depend, don't vendor |
| nicholasgasior/puppeteer-cf-bypass | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/puppeteer-extra-plugin-stealth | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| nicholasgasior/puppeteer-extra | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| sovereign-core/lexi-3.0-sovereign-consciousness | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| sovereign-core/lexi-2.0-sovereign-ultimate | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| sovereign-core/lexi-sovereign | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| sovereign-core/mining | SKIPPED-EXCLUDED | — | — (excluded: wallet/payment/crypto or bot-bypass category) | — | — | n/a |
| sovereign-core/nemo-sovereign-organism | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| sovereign-core/nexus-complete | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| sovereign-core/nexus-omniscience | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
| sovereign-core/openmunus | BLOCKED | — | — (no public canonical match; contents not guessed) | — | — | n/a |
