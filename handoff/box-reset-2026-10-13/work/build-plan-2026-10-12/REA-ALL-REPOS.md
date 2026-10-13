# REA — all repos and what TESSERA actually got from them

Built 2026-10-13 ~1:15 AM CT, read-only from REPO-IMPACT.csv + REPO-IMPACT-part2.csv, V2-FEATURE-MAP.csv, CATEGORY-REPOS.md (+ /workspace/rea-categories/notes), OPTIMIZE-26.md, KEYLESS-SOURCES.md, REA-COVERAGE-V2.md, rea-shards/, and `gh pr view/diff` of TESSERA PRs #241 #242 #246 #247 #249 #250 (all MERGED 2026-10-12/13).

## Summary

- Inventory repos (names from Father's logs, mostly nicholasgasior/*): **315** — scanned/accessible 49, blocked (404/private) 228, excluded (hard-limit category) 38. Note: `gh repo list vitalitychems-dot` shows only 4 owned repos; for 'FOUND' rows a same-name public repo was read, not the original.
- Category research repos: **207** unique (226 table rows; some repos appear in 2 categories). All scanned with REA 6.4.0; joonspk-research/generative_agents timed out (partial).
- OPTIMIZE-26 repos: 10 (2 of them, dspy and langgraph, also in the category list; 8 extra). Unique repos in this file: 531 rows = 315 inventory + 205 category-only + 8 OPTIMIZE-only + three.js.
- **Repos that actually changed TESSERA: 11** — the 10 OPTIMIZE-26 repos (techniques re-implemented clean-room in PR #246) plus three.js (vendored in #241/#242). Every other repo is 'idea only, not built', 'nothing yet' (blocked) or excluded.
- PRs with no repo source: #247 (Rick's own 9 inventions), #249 (34 keyless live-data **services** like Wikipedia/USGS/NWS — data APIs, not code repos; built on #246 primitives), #250 (Rick gates from the internal Sanchez-vs-Gitbook audit).
- There are not 15 repos that changed TESSERA; the honest list is 11. Measured = local bench/tests on this box (CI is billing-blocked). All % in the 'estimate' column are ESTIMATES, never A/B-tested.

## Repos that actually changed TESSERA (11)

| # | repo | what landed | PR | MEASURED result |
|---|---|---|---|---|
| 1 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | LANDED: technique -> OPT-19, OPT-21 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | https://github.com/vitalitychems-dot/TESSERA/pull/246 | batch decisions 4->1 human round trips (-75%); single-owner claim 15->5 task runs (-66.7%) (local bench, artifacts/v2/src/opt/bench.mjs) |
| 2 | [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | LANDED: technique -> OPT-05, OPT-06, OPT-18 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | https://github.com/vitalitychems-dot/TESSERA/pull/246 | exact cache 100->60 model calls/100 tasks (-40%); normalized cache 60->20 (-66.7%); plan memo 10->2 pen calls (-80%) (local bench, artifacts/v2/src/opt/bench.mjs) |
| 3 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | LANDED: technique -> OPT-08 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | https://github.com/vitalitychems-dot/TESSERA/pull/246 | route-by-size 207.5->171.5 compute units/50 tasks (-17.3%) (local bench, artifacts/v2/src/opt/bench.mjs) |
| 4 | [huggingface/smolagents](https://github.com/huggingface/smolagents) | LANDED: technique -> OPT-10, OPT-13 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | https://github.com/vitalitychems-dot/TESSERA/pull/246 | clip tool output 12464->2021 tokens (-83.8%); capped retry 7->20 of 20 flaky tasks finished (local bench, artifacts/v2/src/opt/bench.mjs) |
| 5 | [apache/airflow](https://github.com/apache/airflow) | LANDED: technique -> OPT-12 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | https://github.com/vitalitychems-dot/TESSERA/pull/246 | parallel waves 10->4 sequential steps (-60%) (local bench, artifacts/v2/src/opt/bench.mjs) |
| 6 | [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | LANDED: technique -> OPT-13, OPT-14 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | https://github.com/vitalitychems-dot/TESSERA/pull/246 | capped retry 7->20/20; duplicate-done errors 1->0 (local bench, artifacts/v2/src/opt/bench.mjs) |
| 7 | [temporalio/temporal](https://github.com/temporalio/temporal) | LANDED: technique -> OPT-13, OPT-14, OPT-24 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | https://github.com/vitalitychems-dot/TESSERA/pull/246 | capped retry 7->20/20; duplicate-done 1->0; Retry-After violations 2->0 (local bench, artifacts/v2/src/opt/bench.mjs) |
| 8 | [openai/tiktoken](https://github.com/openai/tiktoken) | LANDED: technique -> OPT-07, OPT-11 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | https://github.com/vitalitychems-dot/TESSERA/pull/246 | fit-budget 20239->512 max tokens (-97.5%); pack-context 0% on V2-051 fixture, -2.9% on BUILD-LOG (local bench, artifacts/v2/src/opt/bench.mjs) |
| 9 | [zilliztech/GPTCache](https://github.com/zilliztech/GPTCache) | LANDED: technique -> OPT-05, OPT-06, OPT-09 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | https://github.com/vitalitychems-dot/TESSERA/pull/246 | cache -40% / -66.7% model calls; diff-only summary 21876->20518 tokens (-6.2%) (local bench, artifacts/v2/src/opt/bench.mjs) |
| 10 | [a2aproject/A2A](https://github.com/a2aproject/A2A) | LANDED: technique -> OPT-16, OPT-17 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | https://github.com/vitalitychems-dot/TESSERA/pull/246 | handoff envelope 85->39 tokens (-54.1%); capability route 15->1 messages (-93.3%) (local bench, artifacts/v2/src/opt/bench.mjs) |
| 11 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | LANDED: vendored library renders the 3D studio floor | https://github.com/vitalitychems-dot/TESSERA/pull/241; https://github.com/vitalitychems-dot/TESSERA/pull/242 | v2 tests 48/48 (#241), 53/53 (#242) pass locally; no perf number |

## Full table

'what we used' = landed feature/PR, or 'idea only, not built', or 'nothing yet'. 'estimate' column is unmeasured.

| repo | status | category | what we used | measured | estimate (ESTIMATE) | list |
|---|---|---|---|---|---|---|
| [collink1007/olive-giant-ever-glade](https://github.com/collink1007/olive-giant-ever-glade) | blocked | docs | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/ad-copy-generator](https://github.com/nicholasgasior/ad-copy-generator) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/GoLogin](https://github.com/nicholasgasior/GoLogin) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/CreepJS](https://github.com/nicholasgasior/CreepJS) | excluded | browser-fingerprint | nothing (excluded by hard-limit category) |  |  | inventory |
| [collink1007/Vitalitychems](https://github.com/collink1007/Vitalitychems) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/2captcha-python](https://github.com/nicholasgasior/2captcha-python) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/Multilogin](https://github.com/nicholasgasior/Multilogin) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/FingerprintJS](https://github.com/nicholasgasior/FingerprintJS) | excluded | browser-fingerprint | nothing (excluded by hard-limit category) |  |  | inventory |
| [collink1007/z](https://github.com/collink1007/z) | scanned | tessera-core | idea only, not built |  | -10% tokens/task ESTIMATE | inventory |
| [collink1007/fleet-moss-monarch-rapid](https://github.com/collink1007/fleet-moss-monarch-rapid) | scanned | commerce | idea only, not built |  | -5% build time ESTIMATE | inventory |
| [collink1007/XXX](https://github.com/collink1007/XXX) | scanned | offline-mesh | idea only, not built |  | +15% offline uptime; 1 HIGH finding (hard-coded admin key, already logged) ESTIMATE (finding MEASURED) | inventory |
| [collink1007/amber-flame-tiger-sand](https://github.com/collink1007/amber-flame-tiger-sand) | scanned | ui | idea only, not built |  | +10% offline uptime / +3 tests ESTIMATE | inventory |
| [nicholasgasior/ai-freelance-platform](https://github.com/nicholasgasior/ai-freelance-platform) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/affiliate-tracking](https://github.com/nicholasgasior/affiliate-tracking) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/age](https://github.com/nicholasgasior/age) | blocked | security-protocols | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/ai-agent-marketplace](https://github.com/nicholasgasior/ai-agent-marketplace) | blocked | agents-studio | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/ai-service-marketplace](https://github.com/nicholasgasior/ai-service-marketplace) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/ai-gig-economy](https://github.com/nicholasgasior/ai-gig-economy) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/alpha-vantage](https://github.com/nicholasgasior/alpha-vantage) | blocked | security-protocols | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/anticaptchaofficial](https://github.com/nicholasgasior/anticaptchaofficial) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/antidetect](https://github.com/nicholasgasior/antidetect) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/api-monetization](https://github.com/nicholasgasior/api-monetization) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/arbitrage-bot](https://github.com/nicholasgasior/arbitrage-bot) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/apify-sdk](https://github.com/nicholasgasior/apify-sdk) | blocked | adapters | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/beautifulsoup4](https://github.com/nicholasgasior/beautifulsoup4) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/backlink-checker](https://github.com/nicholasgasior/backlink-checker) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/audio-captcha-solver](https://github.com/nicholasgasior/audio-captcha-solver) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/bond-yield-tracker](https://github.com/nicholasgasior/bond-yield-tracker) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/bounty-hunter](https://github.com/nicholasgasior/bounty-hunter) | blocked | knowledge-memory | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/brain-js](https://github.com/nicholasgasior/brain-js) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/blog-generator](https://github.com/nicholasgasior/blog-generator) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/brightdata-sdk](https://github.com/nicholasgasior/brightdata-sdk) | blocked | adapters | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/browser-fingerprinting](https://github.com/nicholasgasior/browser-fingerprinting) | excluded | browser-fingerprint | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/capsolver-python](https://github.com/nicholasgasior/capsolver-python) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/captcha-harvester](https://github.com/nicholasgasior/captcha-harvester) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/case-study-builder](https://github.com/nicholasgasior/case-study-builder) | blocked | ui | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/cf-clearance](https://github.com/nicholasgasior/cf-clearance) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/censys-python](https://github.com/nicholasgasior/censys-python) | blocked | adapters | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/checkout-optimizer](https://github.com/nicholasgasior/checkout-optimizer) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/cloudflare-bypass](https://github.com/nicholasgasior/cloudflare-bypass) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/cloudflare-scrape](https://github.com/nicholasgasior/cloudflare-scrape) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/cfscrape](https://github.com/nicholasgasior/cfscrape) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/chromedp](https://github.com/nicholasgasior/chromedp) | blocked | security-protocols | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/cloudscraper](https://github.com/nicholasgasior/cloudscraper) | blocked | web-fetch | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/cf-workers](https://github.com/nicholasgasior/cf-workers) | blocked | compute-sandbox | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/code-marketplace](https://github.com/nicholasgasior/code-marketplace) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/colly](https://github.com/nicholasgasior/colly) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/commodity-tracker](https://github.com/nicholasgasior/commodity-tracker) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/compromise-nlp](https://github.com/nicholasgasior/compromise-nlp) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/competitor-analyzer](https://github.com/nicholasgasior/competitor-analyzer) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/content-optimizer](https://github.com/nicholasgasior/content-optimizer) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/customer-analytics](https://github.com/nicholasgasior/customer-analytics) | blocked | learning | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/decentralized-work](https://github.com/nicholasgasior/decentralized-work) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/creative-testing](https://github.com/nicholasgasior/creative-testing) | blocked | testing | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/conversion-optimizer](https://github.com/nicholasgasior/conversion-optimizer) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/dropshipping-automation](https://github.com/nicholasgasior/dropshipping-automation) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/dilithium](https://github.com/nicholasgasior/dilithium) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/defi-yield-farming](https://github.com/nicholasgasior/defi-yield-farming) | excluded | token-efficiency | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/email-marketing-engine](https://github.com/nicholasgasior/email-marketing-engine) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/ebook-creator](https://github.com/nicholasgasior/ebook-creator) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/email-sequence-builder](https://github.com/nicholasgasior/email-sequence-builder) | blocked | ui | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/facebook-ads-api](https://github.com/nicholasgasior/facebook-ads-api) | blocked | adapters | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/finnhub-python](https://github.com/nicholasgasior/finnhub-python) | blocked | adapters | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/forex-correlation](https://github.com/nicholasgasior/forex-correlation) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/flaresolverr](https://github.com/nicholasgasior/flaresolverr) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/fractal-analysis](https://github.com/nicholasgasior/fractal-analysis) | blocked | learning | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/funcaptcha-solver](https://github.com/nicholasgasior/funcaptcha-solver) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/freelance-api](https://github.com/nicholasgasior/freelance-api) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/futures-data](https://github.com/nicholasgasior/futures-data) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/funnel-builder](https://github.com/nicholasgasior/funnel-builder) | blocked | ui | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/gocolly](https://github.com/nicholasgasior/gocolly) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/google-ads-api](https://github.com/nicholasgasior/google-ads-api) | blocked | adapters | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/goquery](https://github.com/nicholasgasior/goquery) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/gpg4win](https://github.com/nicholasgasior/gpg4win) | blocked | docs | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/goscrapy](https://github.com/nicholasgasior/goscrapy) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/hcaptcha-solver](https://github.com/nicholasgasior/hcaptcha-solver) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/hashcat](https://github.com/nicholasgasior/hashcat) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/headless-chrome-crawler](https://github.com/nicholasgasior/headless-chrome-crawler) | blocked | web-fetch | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/gumroad-api](https://github.com/nicholasgasior/gumroad-api) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/human-ai-marketplace](https://github.com/nicholasgasior/human-ai-marketplace) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/grpcurl](https://github.com/nicholasgasior/grpcurl) | blocked | learning | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/httpie](https://github.com/nicholasgasior/httpie) | blocked | adapters | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/image-captcha-solver](https://github.com/nicholasgasior/image-captcha-solver) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/infographic-data](https://github.com/nicholasgasior/infographic-data) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/insomnia](https://github.com/nicholasgasior/insomnia) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/intermarket-analysis](https://github.com/nicholasgasior/intermarket-analysis) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/inventory-management](https://github.com/nicholasgasior/inventory-management) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/keyword-research-tool](https://github.com/nicholasgasior/keyword-research-tool) | blocked | search-index | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/lemon-squeezy-sdk](https://github.com/nicholasgasior/lemon-squeezy-sdk) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/lattigo](https://github.com/nicholasgasior/lattigo) | blocked | security-protocols | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/landing-page-builder](https://github.com/nicholasgasior/landing-page-builder) | blocked | ui | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/kyber](https://github.com/nicholasgasior/kyber) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/libsodium](https://github.com/nicholasgasior/libsodium) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/liquidity-mining](https://github.com/nicholasgasior/liquidity-mining) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/linkedin-ads-api](https://github.com/nicholasgasior/linkedin-ads-api) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/mailgun-js](https://github.com/nicholasgasior/mailgun-js) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/market-correlation](https://github.com/nicholasgasior/market-correlation) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/marketstack](https://github.com/nicholasgasior/marketstack) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/mechanize](https://github.com/nicholasgasior/mechanize) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/mercury-parser](https://github.com/nicholasgasior/mercury-parser) | blocked | security-protocols | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/mev-templates](https://github.com/nicholasgasior/mev-templates) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/meta-tag-generator](https://github.com/nicholasgasior/meta-tag-generator) | blocked | ui | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/micro-saas-template](https://github.com/nicholasgasior/micro-saas-template) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/microwork-platform](https://github.com/nicholasgasior/microwork-platform) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/moltbook-platform](https://github.com/nicholasgasior/moltbook-platform) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/natural-nlp](https://github.com/nicholasgasior/natural-nlp) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/ml5-js](https://github.com/nicholasgasior/ml5-js) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/newsletter-builder](https://github.com/nicholasgasior/newsletter-builder) | blocked | ui | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/nmap](https://github.com/nicholasgasior/nmap) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/nft-minter](https://github.com/nicholasgasior/nft-minter) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/newspaper3k](https://github.com/nicholasgasior/newspaper3k) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/onnxruntime-web](https://github.com/nicholasgasior/onnxruntime-web) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/nodriver](https://github.com/nicholasgasior/nodriver) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/options-flow](https://github.com/nicholasgasior/options-flow) | blocked | search-index | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/noise-protocol](https://github.com/nicholasgasior/noise-protocol) | blocked | security-protocols | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/openssl](https://github.com/nicholasgasior/openssl) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/order-fulfillment](https://github.com/nicholasgasior/order-fulfillment) | blocked | llm-runtime | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/oxylabs-sdk](https://github.com/nicholasgasior/oxylabs-sdk) | blocked | adapters | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/page-speed-analyzer](https://github.com/nicholasgasior/page-speed-analyzer) | blocked | security-protocols | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/paddle-sdk](https://github.com/nicholasgasior/paddle-sdk) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/passive-income-bot](https://github.com/nicholasgasior/passive-income-bot) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/pinterest-ads-api](https://github.com/nicholasgasior/pinterest-ads-api) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/plaid-node](https://github.com/nicholasgasior/plaid-node) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/playwright-python](https://github.com/nicholasgasior/playwright-python) | blocked | testing | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/playwright-stealth](https://github.com/nicholasgasior/playwright-stealth) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/podcast-outline-gen](https://github.com/nicholasgasior/podcast-outline-gen) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/playwright-cf-bypass](https://github.com/nicholasgasior/playwright-cf-bypass) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/postman-collection](https://github.com/nicholasgasior/postman-collection) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/price-comparison](https://github.com/nicholasgasior/price-comparison) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/press-release-writer](https://github.com/nicholasgasior/press-release-writer) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/product-description-ai](https://github.com/nicholasgasior/product-description-ai) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/product-sourcing-api](https://github.com/nicholasgasior/product-sourcing-api) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/programmatic-advertising](https://github.com/nicholasgasior/programmatic-advertising) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/puppeteer-core](https://github.com/nicholasgasior/puppeteer-core) | blocked | web-fetch | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/puppeteer-cf-bypass](https://github.com/nicholasgasior/puppeteer-cf-bypass) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/puppeteer-extra-plugin-stealth](https://github.com/nicholasgasior/puppeteer-extra-plugin-stealth) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/readability](https://github.com/nicholasgasior/readability) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/rank-tracker](https://github.com/nicholasgasior/rank-tracker) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/puppeteer-extra](https://github.com/nicholasgasior/puppeteer-extra) | blocked | web-fetch | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/quandl-python](https://github.com/nicholasgasior/quandl-python) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/requests-html](https://github.com/nicholasgasior/requests-html) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/residential-proxy](https://github.com/nicholasgasior/residential-proxy) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/rentahuman-ai](https://github.com/nicholasgasior/rentahuman-ai) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/recaptcha-solver](https://github.com/nicholasgasior/recaptcha-solver) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/retargeting-engine](https://github.com/nicholasgasior/retargeting-engine) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/ring](https://github.com/nicholasgasior/ring) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/review-management](https://github.com/nicholasgasior/review-management) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/rod](https://github.com/nicholasgasior/rod) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/saas-boilerplate](https://github.com/nicholasgasior/saas-boilerplate) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/sandwich-bot](https://github.com/nicholasgasior/sandwich-bot) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/scraperapi-sdk](https://github.com/nicholasgasior/scraperapi-sdk) | blocked | adapters | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/schema-markup](https://github.com/nicholasgasior/schema-markup) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/scrapy-redis](https://github.com/nicholasgasior/scrapy-redis) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/scrapy-splash](https://github.com/nicholasgasior/scrapy-splash) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/scrapingbee](https://github.com/nicholasgasior/scrapingbee) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/scrapydweb](https://github.com/nicholasgasior/scrapydweb) | blocked | docs | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/sector-rotation](https://github.com/nicholasgasior/sector-rotation) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/selenium-cf-bypass](https://github.com/nicholasgasior/selenium-cf-bypass) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/selenium-python](https://github.com/nicholasgasior/selenium-python) | scanned | docs | idea only, not built |  | +8% live-fetch jobs ESTIMATE | inventory |
| [nicholasgasior/sentiment-analysis](https://github.com/nicholasgasior/sentiment-analysis) | scanned | misc | idea only, not built |  | +5% ML curriculum tasks ESTIMATE | inventory |
| [nicholasgasior/sendgrid-nodejs](https://github.com/nicholasgasior/sendgrid-nodejs) | scanned | misc | idea only, not built |  | +5% publish/notify flows ESTIMATE | inventory |
| [nicholasgasior/selenium-wire](https://github.com/nicholasgasior/selenium-wire) | scanned | misc | idea only, not built |  | +8% live-fetch jobs ESTIMATE | inventory |
| [nicholasgasior/shipping-calculator](https://github.com/nicholasgasior/shipping-calculator) | scanned | excluded | idea only, not built |  | +2-5% widget/task glue ESTIMATE | inventory |
| [nicholasgasior/shodan-python](https://github.com/nicholasgasior/shodan-python) | excluded | misc | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/sitemap-generator](https://github.com/nicholasgasior/sitemap-generator) | scanned | misc | idea only, not built |  | +4% publish completeness ESTIMATE | inventory |
| [nicholasgasior/signal-protocol](https://github.com/nicholasgasior/signal-protocol) | scanned | security-protocols | idea only, not built |  | +10% mesh message integrity ESTIMATE | inventory |
| [nicholasgasior/seo-analyzer](https://github.com/nicholasgasior/seo-analyzer) | scanned | misc | idea only, not built |  | +4% publish completeness ESTIMATE | inventory |
| [nicholasgasior/smartproxy-sdk](https://github.com/nicholasgasior/smartproxy-sdk) | excluded | adapters | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/snapchat-ads-api](https://github.com/nicholasgasior/snapchat-ads-api) | blocked | comms | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/social-content-calendar](https://github.com/nicholasgasior/social-content-calendar) | scanned | misc | idea only, not built |  | -8% draft tokens ESTIMATE | inventory |
| [nicholasgasior/social-media-scheduler](https://github.com/nicholasgasior/social-media-scheduler) | scanned | misc | idea only, not built |  | -8% draft tokens ESTIMATE | inventory |
| [nicholasgasior/sphincs](https://github.com/nicholasgasior/sphincs) | scanned | misc | idea only, not built |  | +5% offline mesh trust ESTIMATE | inventory |
| [nicholasgasior/staking-contracts](https://github.com/nicholasgasior/staking-contracts) | excluded | misc | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/sniper-bot](https://github.com/nicholasgasior/sniper-bot) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/story-writer](https://github.com/nicholasgasior/story-writer) | scanned | token-efficiency | idea only, not built |  | -8% draft tokens ESTIMATE | inventory |
| [nicholasgasior/task-automation-platform](https://github.com/nicholasgasior/task-automation-platform) | scanned | misc | idea only, not built |  | +2-5% widget/task glue ESTIMATE | inventory |
| [nicholasgasior/tensorflow-js](https://github.com/nicholasgasior/tensorflow-js) | scanned | misc | idea only, not built |  | +5% ML curriculum tasks ESTIMATE | inventory |
| [nicholasgasior/tiingo-python](https://github.com/nicholasgasior/tiingo-python) | scanned | adapters | idea only, not built |  | +5% gateway data freshness ESTIMATE | inventory |
| [nicholasgasior/testimonial-generator](https://github.com/nicholasgasior/testimonial-generator) | scanned | testing | idea only, not built |  | -8% draft tokens ESTIMATE | inventory |
| [nicholasgasior/tiktok-ads-api](https://github.com/nicholasgasior/tiktok-ads-api) | scanned | misc | idea only, not built |  | +5% gateway data freshness ESTIMATE | inventory |
| [nicholasgasior/tink](https://github.com/nicholasgasior/tink) | scanned | security-protocols | idea only, not built |  | +8% crypto hygiene ESTIMATE | inventory |
| [nicholasgasior/trafilatura](https://github.com/nicholasgasior/trafilatura) | scanned | misc | idea only, not built |  | -15% tokens on scrape/summarize ESTIMATE | inventory |
| [nicholasgasior/token-creator](https://github.com/nicholasgasior/token-creator) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/turnstile-solver](https://github.com/nicholasgasior/turnstile-solver) | excluded | misc | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/twelve-data-python](https://github.com/nicholasgasior/twelve-data-python) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/twilio-node](https://github.com/nicholasgasior/twilio-node) | scanned | misc | idea only, not built |  | +5% publish/notify flows ESTIMATE | inventory |
| [nicholasgasior/vix-analysis](https://github.com/nicholasgasior/vix-analysis) | scanned | misc | idea only, not built |  | +5% gateway data freshness ESTIMATE | inventory |
| [nicholasgasior/undetected-chromedriver](https://github.com/nicholasgasior/undetected-chromedriver) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/twitter-ads-api](https://github.com/nicholasgasior/twitter-ads-api) | blocked | misc | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [nicholasgasior/video-script-writer](https://github.com/nicholasgasior/video-script-writer) | scanned | misc | idea only, not built |  | -8% draft tokens ESTIMATE | inventory |
| [nicholasgasior/web-unlocker](https://github.com/nicholasgasior/web-unlocker) | excluded | misc | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/whitepaper-generator](https://github.com/nicholasgasior/whitepaper-generator) | scanned | misc | idea only, not built |  | 0% ESTIMATE | inventory |
| [nicholasgasior/wink-nlp](https://github.com/nicholasgasior/wink-nlp) | scanned | misc | idea only, not built |  | -10% classify tokens; +5% task completion ESTIMATE | inventory |
| [nicholasgasior/wireguard-go](https://github.com/nicholasgasior/wireguard-go) | scanned | misc | idea only, not built |  | +5% offline mesh trust ESTIMATE | inventory |
| [sovereign-archive/T5](https://github.com/sovereign-archive/T5) | scanned | tessera-core | idea only, not built |  | 0% runtime ESTIMATE | inventory |
| [nicholasgasior/zenrows-scraper](https://github.com/nicholasgasior/zenrows-scraper) | excluded | web-fetch | nothing (excluded by hard-limit category) |  |  | inventory |
| [nicholasgasior/yahoo-finance-api](https://github.com/nicholasgasior/yahoo-finance-api) | scanned | adapters | idea only, not built |  | +5% gateway data freshness ESTIMATE | inventory |
| [sovereign-core/Doxiwehu-OmniMind-Public](https://github.com/sovereign-core/Doxiwehu-OmniMind-Public) | excluded | tessera-core | nothing (excluded by hard-limit category) |  |  | inventory |
| [sovereign-core/awesome-machine-learning](https://github.com/sovereign-core/awesome-machine-learning) | scanned | learning | idea only, not built |  | +5% ML curriculum tasks ESTIMATE | inventory |
| [sovereign-core/complete-digital-organism](https://github.com/sovereign-core/complete-digital-organism) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/TESSERACT-UNIFIED](https://github.com/sovereign-core/TESSERACT-UNIFIED) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/lexi-3.0-sovereign-consciousness](https://github.com/sovereign-core/lexi-3.0-sovereign-consciousness) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/lexi-2.0-sovereign-ultimate](https://github.com/sovereign-core/lexi-2.0-sovereign-ultimate) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/lexi-sovereign](https://github.com/sovereign-core/lexi-sovereign) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/mining](https://github.com/sovereign-core/mining) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [sovereign-core/nemo-sovereign-organism](https://github.com/sovereign-core/nemo-sovereign-organism) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/nexus-complete](https://github.com/sovereign-core/nexus-complete) | scanned | ui | idea only, not built |  | +2-5% widget/task glue ESTIMATE | inventory |
| [sovereign-core/nexus-omniscience](https://github.com/sovereign-core/nexus-omniscience) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/sovereign-ai-2025](https://github.com/sovereign-core/sovereign-ai-2025) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/openmunus](https://github.com/sovereign-core/openmunus) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/sovereign-tessera](https://github.com/sovereign-core/sovereign-tessera) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/sovereign-zenith](https://github.com/sovereign-core/sovereign-zenith) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tessera-aetherion-orion](https://github.com/sovereign-core/tessera-aetherion-orion) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tessera-ai-orchestration](https://github.com/sovereign-core/tessera-ai-orchestration) | blocked | agents-studio | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tessera-omniscience-complete](https://github.com/sovereign-core/tessera-omniscience-complete) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tessera-payment-processing](https://github.com/sovereign-core/tessera-payment-processing) | excluded | excluded | nothing (excluded by hard-limit category) |  |  | inventory |
| [sovereign-core/tessera-singularity-swarm](https://github.com/sovereign-core/tessera-singularity-swarm) | blocked | agents-studio | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tessera-sovereign-authority](https://github.com/sovereign-core/tessera-sovereign-authority) | blocked | auth | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tessera-sovereign-complete](https://github.com/sovereign-core/tessera-sovereign-complete) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tessera-sovereign-tumbler](https://github.com/sovereign-core/tessera-sovereign-tumbler) | excluded | tessera-core | nothing (excluded by hard-limit category) |  |  | inventory |
| [sovereign-core/tessera-sovereign-ultimate](https://github.com/sovereign-core/tessera-sovereign-ultimate) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tessera-sovereign-organism](https://github.com/sovereign-core/tessera-sovereign-organism) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tessera-super-hybrid-final-complete](https://github.com/sovereign-core/tessera-super-hybrid-final-complete) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-complete-final](https://github.com/sovereign-core/tesseract-complete-final) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tessera-ultimate-sovereign](https://github.com/sovereign-core/tessera-ultimate-sovereign) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-ecosystem](https://github.com/sovereign-core/tesseract-ecosystem) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-hybrid-unified](https://github.com/sovereign-core/tesseract-hybrid-unified) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tessera-tesseract-unified](https://github.com/sovereign-core/tessera-tesseract-unified) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-omniscience-v8](https://github.com/sovereign-core/tesseract-omniscience-v8) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-swarm-ultimate](https://github.com/sovereign-core/tesseract-swarm-ultimate) | blocked | agents-studio | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-quantum-agi](https://github.com/sovereign-core/tesseract-quantum-agi) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-omniversal](https://github.com/sovereign-core/tesseract-omniversal) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-ultimate](https://github.com/sovereign-core/tesseract-ultimate) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-unified-agi](https://github.com/sovereign-core/tesseract-unified-agi) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-unified-final](https://github.com/sovereign-core/tesseract-unified-final) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v10](https://github.com/sovereign-core/tesseract-v10) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v13](https://github.com/sovereign-core/tesseract-v13) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v11](https://github.com/sovereign-core/tesseract-v11) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v15](https://github.com/sovereign-core/tesseract-v15) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v14](https://github.com/sovereign-core/tesseract-v14) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v12](https://github.com/sovereign-core/tesseract-v12) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v17](https://github.com/sovereign-core/tesseract-v17) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v16](https://github.com/sovereign-core/tesseract-v16) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v18](https://github.com/sovereign-core/tesseract-v18) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v19](https://github.com/sovereign-core/tesseract-v19) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v20](https://github.com/sovereign-core/tesseract-v20) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v21](https://github.com/sovereign-core/tesseract-v21) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v22](https://github.com/sovereign-core/tesseract-v22) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v23](https://github.com/sovereign-core/tesseract-v23) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v3-trained](https://github.com/sovereign-core/tesseract-v3-trained) | blocked | learning | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v31](https://github.com/sovereign-core/tesseract-v31) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v30](https://github.com/sovereign-core/tesseract-v30) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v32-real](https://github.com/sovereign-core/tesseract-v32-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v36-real](https://github.com/sovereign-core/tesseract-v36-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v33-real](https://github.com/sovereign-core/tesseract-v33-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v38-real](https://github.com/sovereign-core/tesseract-v38-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v34-real](https://github.com/sovereign-core/tesseract-v34-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v35-real](https://github.com/sovereign-core/tesseract-v35-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v37-real](https://github.com/sovereign-core/tesseract-v37-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v39-real](https://github.com/sovereign-core/tesseract-v39-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v40-real](https://github.com/sovereign-core/tesseract-v40-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v4-ollama](https://github.com/sovereign-core/tesseract-v4-ollama) | blocked | llm-runtime | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v41-real](https://github.com/sovereign-core/tesseract-v41-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v42-real](https://github.com/sovereign-core/tesseract-v42-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v43-real](https://github.com/sovereign-core/tesseract-v43-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v47-real](https://github.com/sovereign-core/tesseract-v47-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v46-real](https://github.com/sovereign-core/tesseract-v46-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v45-real](https://github.com/sovereign-core/tesseract-v45-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v48-real](https://github.com/sovereign-core/tesseract-v48-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v49-real](https://github.com/sovereign-core/tesseract-v49-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v44-real](https://github.com/sovereign-core/tesseract-v44-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v51-real](https://github.com/sovereign-core/tesseract-v51-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v53-real](https://github.com/sovereign-core/tesseract-v53-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v52-real](https://github.com/sovereign-core/tesseract-v52-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v50-real](https://github.com/sovereign-core/tesseract-v50-real) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v8](https://github.com/sovereign-core/tesseract-v8) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract-v7](https://github.com/sovereign-core/tesseract-v7) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract2](https://github.com/sovereign-core/tesseract2) | scanned | tessera-core | idea only, not built |  | 0% ESTIMATE | inventory |
| [sovereign-core/tesseract-v9](https://github.com/sovereign-core/tesseract-v9) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract1](https://github.com/sovereign-core/tesseract1) | scanned | tessera-core | idea only, not built |  | 0-2% ESTIMATE | inventory |
| [sovereign-core/ultimate-tessera](https://github.com/sovereign-core/ultimate-tessera) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseractA1](https://github.com/sovereign-core/tesseractA1) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-core/tesseract3](https://github.com/sovereign-core/tesseract3) | scanned | tessera-core | idea only, not built |  | 0-2% ESTIMATE | inventory |
| [sovereign-origin/TessV1](https://github.com/sovereign-origin/TessV1) | scanned | misc | idea only, not built |  | 0-2% ESTIMATE | inventory |
| [sovereign-origin/tessera-sovereign-complete](https://github.com/sovereign-origin/tessera-sovereign-complete) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-origin/tessera-sovereign-ultimate](https://github.com/sovereign-origin/tessera-sovereign-ultimate) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-origin/tesseract-quantum-agi](https://github.com/sovereign-origin/tesseract-quantum-agi) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [sovereign-origin/tesseract-v4-ollama](https://github.com/sovereign-origin/tesseract-v4-ollama) | blocked | llm-runtime | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [thetesseractai/18](https://github.com/thetesseractai/18) | scanned | tessera-core | idea only, not built |  | +10% design reuse ESTIMATE | inventory |
| [thetesseractai/Tesseract-Sovereign-Moon-v2-Consolidated](https://github.com/thetesseractai/Tesseract-Sovereign-Moon-v2-Consolidated) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [thetesseractai/consolidated-project-all-in-one](https://github.com/thetesseractai/consolidated-project-all-in-one) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [thetesseractai/Tesseract2.0](https://github.com/thetesseractai/Tesseract2.0) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [thetesseractai/Tesseract-Unified-Ecosystem](https://github.com/thetesseractai/Tesseract-Unified-Ecosystem) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [thetesseractai/Tesseract-Sovereign-Moon-v3.0](https://github.com/thetesseractai/Tesseract-Sovereign-Moon-v3.0) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [thetesseractai/Tesseraxt-Sovereign-Brain](https://github.com/thetesseractai/Tesseraxt-Sovereign-Brain) | blocked | tessera-core | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [vitalitychems-dot/5t](https://github.com/vitalitychems-dot/5t) | blocked | docs | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [vitalitychems-dot/1T](https://github.com/vitalitychems-dot/1T) | excluded | docs | nothing (excluded by hard-limit category) |  |  | inventory |
| [vitalitychems-dot/Everything](https://github.com/vitalitychems-dot/Everything) | scanned | docs | idea only, not built |  | 0% ESTIMATE | inventory |
| [vitalitychems-dot/1](https://github.com/vitalitychems-dot/1) | scanned | docs | idea only, not built |  | 0% ESTIMATE | inventory |
| [vitalitychems-dot/GitbookAI](https://github.com/vitalitychems-dot/GitbookAI) | scanned | offline-mesh | idea only, not built |  | +20% offline drop UX ESTIMATE | inventory |
| [vitalitychems-dot/Grok-ready](https://github.com/vitalitychems-dot/Grok-ready) | blocked | docs | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [vitalitychems-dot/Gitbook](https://github.com/vitalitychems-dot/Gitbook) | scanned | docs | idea only, not built |  | +15% offline uptime ESTIMATE | inventory |
| [vitalitychems-dot/TX](https://github.com/vitalitychems-dot/TX) | scanned | docs | idea only, not built |  | 0% ESTIMATE | inventory |
| [vitalitychems-dot/Zz](https://github.com/vitalitychems-dot/Zz) | scanned | docs | idea only, not built |  | 0% ESTIMATE | inventory |
| [vitalitychems-dot/T44](https://github.com/vitalitychems-dot/T44) | blocked | docs | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [vitalitychems-dot/TESS](https://github.com/vitalitychems-dot/TESS) | scanned | docs | idea only, not built |  | 0-2% ESTIMATE | inventory |
| [vitalitychems-dot/tessera-complete-archives](https://github.com/vitalitychems-dot/tessera-complete-archives) | blocked | docs | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [vitalitychems-dot/tessera-coordination](https://github.com/vitalitychems-dot/tessera-coordination) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [vitalitychems-dot/tessera-grok-handoff-complete](https://github.com/vitalitychems-dot/tessera-grok-handoff-complete) | blocked | docs | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [vitalitychems-dot/tessera-grok-handoff](https://github.com/vitalitychems-dot/tessera-grok-handoff) | blocked | docs | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [vitalitychems-dot/TESSERA](https://github.com/vitalitychems-dot/TESSERA) | scanned | tessera-core | idea only, not built |  | 0% ESTIMATE | inventory |
| [vitalitychems-dot/tessera-unified](https://github.com/vitalitychems-dot/tessera-unified) | blocked | excluded | nothing yet (repo unreadable: 404/private) |  |  | inventory |
| [vitalitychems-dot/z](https://github.com/vitalitychems-dot/z) | scanned | excluded | idea only, not built |  | 0% ESTIMATE | inventory |
| [vitalitychems-dot/vitality](https://github.com/vitalitychems-dot/vitality) | scanned | commerce | idea only, not built |  | -5% flaky CI; +2 checks ESTIMATE | inventory |
| [collin-keane/Tessera](https://github.com/collin-keane/Tessera) | scanned | ui | idea only, not built |  | 0% ESTIMATE | inventory |
| [obra/superpowers](https://github.com/obra/superpowers) | scanned | agent-skills | idea only, not built |  | repeat-task tokens: -15-30% ESTIMATE | category |
| [anthropics/skills](https://github.com/anthropics/skills) | scanned | agent-skills | idea only, not built |  | repeat-task tokens: -15-30% ESTIMATE | category |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | scanned | agent-skills | idea only, not built |  | repeat-task tokens: -15-30% ESTIMATE | category |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | scanned | agent-skills | idea only, not built |  | repeat-task tokens: -15-30% ESTIMATE | category |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | scanned | agent-skills | idea only, not built |  | repeat-task tokens: -15-30% ESTIMATE | category |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | scanned | agent-skills | idea only, not built |  | repeat-task tokens: -15-30% ESTIMATE | category |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | scanned | agent-skills | idea only, not built |  | repeat-task tokens: -15-30% ESTIMATE | category |
| [google/skills](https://github.com/google/skills) | scanned | agent-skills | idea only, not built |  | repeat-task tokens: -15-30% ESTIMATE | category |
| [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | scanned | agi-frameworks | idea only, not built |  | task completion rate: +10-20% ESTIMATE | category |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | scanned | agi-frameworks | idea only, not built |  | task completion rate: +10-20% ESTIMATE | category |
| [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | scanned | agi-frameworks; sandboxed-code-exec | idea only, not built |  | task completion rate: +10-20% ESTIMATE | category |
| [reworkd/AgentGPT](https://github.com/reworkd/AgentGPT) | scanned | agi-frameworks | idea only, not built |  | task completion rate: +10-20% ESTIMATE | category |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | scanned | agi-frameworks | idea only, not built |  | task completion rate: +10-20% ESTIMATE | category |
| [microsoft/JARVIS](https://github.com/microsoft/JARVIS) | scanned | agi-frameworks | idea only, not built |  | task completion rate: +10-20% ESTIMATE | category |
| [yoheinakajima/babyagi](https://github.com/yoheinakajima/babyagi) | scanned | agi-frameworks | idea only, not built |  | task completion rate: +10-20% ESTIMATE | category |
| [openai/swarm](https://github.com/openai/swarm) | scanned | agi-frameworks | idea only, not built |  | task completion rate: +10-20% ESTIMATE | category |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | scanned | anti-hallucination-grounding; evals | idea only, not built |  | unsupported-claim rate: -20-50% ESTIMATE | category |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) | scanned | anti-hallucination-grounding; evals | idea only, not built |  | unsupported-claim rate: -20-50% ESTIMATE | category |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | scanned | anti-hallucination-grounding; evals | idea only, not built |  | unsupported-claim rate: -20-50% ESTIMATE | category |
| [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) | scanned | anti-hallucination-grounding | idea only, not built |  | unsupported-claim rate: -20-50% ESTIMATE | category |
| [NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | scanned | anti-hallucination-grounding | idea only, not built |  | unsupported-claim rate: -20-50% ESTIMATE | category |
| [truera/trulens](https://github.com/truera/trulens) | scanned | anti-hallucination-grounding | idea only, not built |  | unsupported-claim rate: -20-50% ESTIMATE | category |
| [vectara/hallucination-leaderboard](https://github.com/vectara/hallucination-leaderboard) | scanned | anti-hallucination-grounding | idea only, not built |  | unsupported-claim rate: -20-50% ESTIMATE | category |
| [stanford-oval/WikiChat](https://github.com/stanford-oval/WikiChat) | scanned | anti-hallucination-grounding | idea only, not built |  | unsupported-claim rate: -20-50% ESTIMATE | category |
| [mne-tools/mne-python](https://github.com/mne-tools/mne-python) | scanned | brain-scans-connectomics; k-neurology | idea only, not built |  | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) | category |
| [google/neuroglancer](https://github.com/google/neuroglancer) | scanned | brain-scans-connectomics | idea only, not built |  | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) | category |
| [ANTsX/ANTs](https://github.com/ANTsX/ANTs) | scanned | brain-scans-connectomics | idea only, not built |  | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) | category |
| [nilearn/nilearn](https://github.com/nilearn/nilearn) | scanned | brain-scans-connectomics | idea only, not built |  | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) | category |
| [freesurfer/freesurfer](https://github.com/freesurfer/freesurfer) | scanned | brain-scans-connectomics | idea only, not built |  | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) | category |
| [dipy/dipy](https://github.com/dipy/dipy) | scanned | brain-scans-connectomics | idea only, not built |  | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) | category |
| [nipy/nipype](https://github.com/nipy/nipype) | scanned | brain-scans-connectomics | idea only, not built |  | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) | category |
| [nipy/nibabel](https://github.com/nipy/nibabel) | scanned | brain-scans-connectomics; k-neurology | idea only, not built |  | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) | category |
| [fangwei123456/spikingjelly](https://github.com/fangwei123456/spikingjelly) | scanned | brain-synapse-simulation | idea only, not built |  | compute lab experiments available: n/a; research (ESTIMATE) | category |
| [jeshraghian/snntorch](https://github.com/jeshraghian/snntorch) | scanned | brain-synapse-simulation | idea only, not built |  | compute lab experiments available: n/a; research (ESTIMATE) | category |
| [BindsNET/bindsnet](https://github.com/BindsNET/bindsnet) | scanned | brain-synapse-simulation | idea only, not built |  | compute lab experiments available: n/a; research (ESTIMATE) | category |
| [brian-team/brian2](https://github.com/brian-team/brian2) | scanned | brain-synapse-simulation | idea only, not built |  | compute lab experiments available: n/a; research (ESTIMATE) | category |
| [nengo/nengo](https://github.com/nengo/nengo) | scanned | brain-synapse-simulation; consciousness-cognitive-arch | idea only, not built |  | compute lab experiments available: n/a; research (ESTIMATE) | category |
| [norse/norse](https://github.com/norse/norse) | scanned | brain-synapse-simulation | idea only, not built |  | compute lab experiments available: n/a; research (ESTIMATE) | category |
| [lava-nc/lava](https://github.com/lava-nc/lava) | scanned | brain-synapse-simulation | idea only, not built |  | compute lab experiments available: n/a; research (ESTIMATE) | category |
| [brainpy/BrainPy](https://github.com/brainpy/BrainPy) | scanned | brain-synapse-simulation; consciousness-cognitive-arch | idea only, not built |  | compute lab experiments available: n/a; research (ESTIMATE) | category |
| [opencog/opencog](https://github.com/opencog/opencog) | scanned | consciousness-cognitive-arch | idea only, not built |  | task completion rate: +5-10% ESTIMATE | category |
| [daveshap/ACE_Framework](https://github.com/daveshap/ACE_Framework) | scanned | consciousness-cognitive-arch | idea only, not built |  | task completion rate: +5-10% ESTIMATE | category |
| [opencog/atomspace](https://github.com/opencog/atomspace) | scanned | consciousness-cognitive-arch | idea only, not built |  | task completion rate: +5-10% ESTIMATE | category |
| [SoarGroup/Soar](https://github.com/SoarGroup/Soar) | scanned | consciousness-cognitive-arch | idea only, not built |  | task completion rate: +5-10% ESTIMATE | category |
| [cmekik/pyClarion](https://github.com/cmekik/pyClarion) | scanned | consciousness-cognitive-arch | idea only, not built |  | task completion rate: +5-10% ESTIMATE | category |
| [ccnlab/leabra](https://github.com/ccnlab/leabra) | scanned | consciousness-cognitive-arch | idea only, not built |  | task completion rate: +5-10% ESTIMATE | category |
| [ContinualAI/avalanche](https://github.com/ContinualAI/avalanche) | scanned | continual-learning | idea only, not built |  | retained skill after update: +10-30% ESTIMATE | category |
| [GMvandeVen/continual-learning](https://github.com/GMvandeVen/continual-learning) | scanned | continual-learning | idea only, not built |  | retained skill after update: +10-30% ESTIMATE | category |
| [aimagelab/mammoth](https://github.com/aimagelab/mammoth) | scanned | continual-learning | idea only, not built |  | retained skill after update: +10-30% ESTIMATE | category |
| [LAMDA-CL/LAMDA-PILOT](https://github.com/LAMDA-CL/LAMDA-PILOT) | scanned | continual-learning | idea only, not built |  | retained skill after update: +10-30% ESTIMATE | category |
| [GT-RIPL/Continual-Learning-Benchmark](https://github.com/GT-RIPL/Continual-Learning-Benchmark) | scanned | continual-learning | idea only, not built |  | retained skill after update: +10-30% ESTIMATE | category |
| [google-research/l2p](https://github.com/google-research/l2p) | scanned | continual-learning | idea only, not built |  | retained skill after update: +10-30% ESTIMATE | category |
| [Continvvm/continuum](https://github.com/Continvvm/continuum) | scanned | continual-learning | idea only, not built |  | retained skill after update: +10-30% ESTIMATE | category |
| [ContinualAI/continual-learning-baselines](https://github.com/ContinualAI/continual-learning-baselines) | scanned | continual-learning | idea only, not built |  | retained skill after update: +10-30% ESTIMATE | category |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | scanned | evals | idea only, not built |  | regressions caught pre-merge: +30-60% ESTIMATE | category |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | scanned | evals | idea only, not built |  | regressions caught pre-merge: +30-60% ESTIMATE | category |
| [comet-ml/opik](https://github.com/comet-ml/opik) | scanned | evals | idea only, not built |  | regressions caught pre-merge: +30-60% ESTIMATE | category |
| [openai/evals](https://github.com/openai/evals) | scanned | evals | idea only, not built |  | regressions caught pre-merge: +30-60% ESTIMATE | category |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | scanned | evals | idea only, not built |  | regressions caught pre-merge: +30-60% ESTIMATE | category |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | scanned | knowledge-graphs; rag | idea only, not built |  | retrieval precision: +10-30% ESTIMATE | category |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | scanned | knowledge-graphs; rag | idea only, not built |  | retrieval precision: +10-30% ESTIMATE | category |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | scanned | knowledge-graphs; memory-recall | idea only, not built |  | retrieval precision: +10-30% ESTIMATE | category |
| [getzep/graphiti](https://github.com/getzep/graphiti) | scanned | knowledge-graphs; memory-recall | idea only, not built |  | retrieval precision: +10-30% ESTIMATE | category |
| [neo4j/neo4j](https://github.com/neo4j/neo4j) | scanned | knowledge-graphs | idea only, not built |  | retrieval precision: +10-30% ESTIMATE | category |
| [reconurge/flowsint](https://github.com/reconurge/flowsint) | scanned | knowledge-graphs | idea only, not built |  | retrieval precision: +10-30% ESTIMATE | category |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | scanned | knowledge-graphs | idea only, not built |  | retrieval precision: +10-30% ESTIMATE | category |
| [neo4j-labs/llm-graph-builder](https://github.com/neo4j-labs/llm-graph-builder) | scanned | knowledge-graphs | idea only, not built |  | retrieval precision: +10-30% ESTIMATE | category |
| [huggingface/transformers](https://github.com/huggingface/transformers) | scanned | llms-open-inference | idea only, not built |  | cost per 1M tokens: -50-90% vs paid API ESTIMATE | category |
| [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | scanned | llms-open-inference | idea only, not built |  | cost per 1M tokens: -50-90% vs paid API ESTIMATE | category |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | scanned | llms-open-inference | idea only, not built |  | cost per 1M tokens: -50-90% vs paid API ESTIMATE | category |
| [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed) | scanned | llms-open-inference | idea only, not built |  | cost per 1M tokens: -50-90% vs paid API ESTIMATE | category |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | scanned | llms-open-inference | idea only, not built |  | cost per 1M tokens: -50-90% vs paid API ESTIMATE | category |
| [QwenLM/Qwen3](https://github.com/QwenLM/Qwen3) | scanned | llms-open-inference | idea only, not built |  | cost per 1M tokens: -50-90% vs paid API ESTIMATE | category |
| [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | scanned | llms-open-inference | idea only, not built |  | cost per 1M tokens: -50-90% vs paid API ESTIMATE | category |
| [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference) | scanned | llms-open-inference | idea only, not built |  | cost per 1M tokens: -50-90% vs paid API ESTIMATE | category |
| [ollama/ollama](https://github.com/ollama/ollama) | scanned | local-offline-inference | idea only, not built |  | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE | category |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | scanned | local-offline-inference | idea only, not built |  | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE | category |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | scanned | local-offline-inference; token-saving-compression | idea only, not built |  | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE | category |
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | scanned | local-offline-inference | idea only, not built |  | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE | category |
| [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | scanned | local-offline-inference | idea only, not built |  | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE | category |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | scanned | local-offline-inference | idea only, not built |  | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE | category |
| [exo-explore/exo](https://github.com/exo-explore/exo) | scanned | local-offline-inference | idea only, not built |  | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE | category |
| [janhq/jan](https://github.com/janhq/jan) | scanned | local-offline-inference | idea only, not built |  | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE | category |
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | scanned | machine-learning | idea only, not built |  | n/a until compute lab runs: ESTIMATE only | category |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | scanned | machine-learning | idea only, not built |  | n/a until compute lab runs: ESTIMATE only | category |
| [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | scanned | machine-learning | idea only, not built |  | n/a until compute lab runs: ESTIMATE only | category |
| [keras-team/keras](https://github.com/keras-team/keras) | scanned | machine-learning | idea only, not built |  | n/a until compute lab runs: ESTIMATE only | category |
| [jax-ml/jax](https://github.com/jax-ml/jax) | scanned | machine-learning | idea only, not built |  | n/a until compute lab runs: ESTIMATE only | category |
| [tinygrad/tinygrad](https://github.com/tinygrad/tinygrad) | scanned | machine-learning | idea only, not built |  | n/a until compute lab runs: ESTIMATE only | category |
| [dmlc/xgboost](https://github.com/dmlc/xgboost) | scanned | machine-learning | idea only, not built |  | n/a until compute lab runs: ESTIMATE only | category |
| [ml-explore/mlx](https://github.com/ml-explore/mlx) | scanned | machine-learning | idea only, not built |  | n/a until compute lab runs: ESTIMATE only | category |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | scanned | memory-recall; tool-use-mcp | idea only, not built |  | tokens per task (re-context): -20-40% ESTIMATE | category |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | scanned | memory-recall | idea only, not built |  | tokens per task (re-context): -20-40% ESTIMATE | category |
| [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | scanned | memory-recall | idea only, not built |  | tokens per task (re-context): -20-40% ESTIMATE | category |
| [letta-ai/letta](https://github.com/letta-ai/letta) | scanned | memory-recall | idea only, not built |  | tokens per task (re-context): -20-40% ESTIMATE | category |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | scanned | memory-recall | idea only, not built |  | tokens per task (re-context): -20-40% ESTIMATE | category |
| [getzep/zep](https://github.com/getzep/zep) | scanned | memory-recall | idea only, not built |  | tokens per task (re-context): -20-40% ESTIMATE | category |
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | scanned | multi-agent-orchestration; recursive-self-improvement | idea only, not built |  | parallel task throughput: +20-50% ESTIMATE | category |
| [microsoft/autogen](https://github.com/microsoft/autogen) | scanned | multi-agent-orchestration | idea only, not built |  | parallel task throughput: +20-50% ESTIMATE | category |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | scanned | multi-agent-orchestration | idea only, not built |  | parallel task throughput: +20-50% ESTIMATE | category |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | scanned | multi-agent-orchestration | LANDED: technique -> OPT-19, OPT-21 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | batch decisions 4->1 human round trips (-75%); single-owner claim 15->5 task runs (-66.7%) (local bench, artifacts/v2/src/opt/bench.mjs) | parallel task throughput: +20-50% ESTIMATE | category+optimize-26 |
| [agno-agi/agno](https://github.com/agno-agi/agno) | scanned | multi-agent-orchestration | idea only, not built |  | parallel task throughput: +20-50% ESTIMATE | category |
| [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | scanned | multi-agent-orchestration | idea only, not built |  | parallel task throughput: +20-50% ESTIMATE | category |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | scanned | multi-agent-orchestration | idea only, not built |  | parallel task throughput: +20-50% ESTIMATE | category |
| [camel-ai/camel](https://github.com/camel-ai/camel) | scanned | multi-agent-orchestration | idea only, not built |  | parallel task throughput: +20-50% ESTIMATE | category |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | scanned | rag | idea only, not built |  | answer grounding rate: +10-30% ESTIMATE | category |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | scanned | rag | idea only, not built |  | answer grounding rate: +10-30% ESTIMATE | category |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | scanned | rag | idea only, not built |  | answer grounding rate: +10-30% ESTIMATE | category |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | scanned | rag | idea only, not built |  | answer grounding rate: +10-30% ESTIMATE | category |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | scanned | rag | idea only, not built |  | answer grounding rate: +10-30% ESTIMATE | category |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | scanned | rag | idea only, not built |  | answer grounding rate: +10-30% ESTIMATE | category |
| [deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) | scanned | reasoning-thinking | idea only, not built |  | task accuracy: +5-15% ESTIMATE | category |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | scanned | reasoning-thinking; recursive-self-improvement | LANDED: technique -> OPT-05, OPT-06, OPT-18 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | exact cache 100->60 model calls/100 tasks (-40%); normalized cache 60->20 (-66.7%); plan memo 10->2 pen calls (-80%) (local bench, artifacts/v2/src/opt/bench.mjs) | task accuracy: +5-15% ESTIMATE | category+optimize-26 |
| [huggingface/open-r1](https://github.com/huggingface/open-r1) | scanned | reasoning-thinking | idea only, not built |  | task accuracy: +5-15% ESTIMATE | category |
| [verl-project/verl](https://github.com/verl-project/verl) | scanned | reasoning-thinking | idea only, not built |  | task accuracy: +5-15% ESTIMATE | category |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | scanned | reasoning-thinking; recursive-self-improvement | idea only, not built |  | task accuracy: +5-15% ESTIMATE | category |
| [Jiayi-Pan/TinyZero](https://github.com/Jiayi-Pan/TinyZero) | scanned | reasoning-thinking | idea only, not built |  | task accuracy: +5-15% ESTIMATE | category |
| [princeton-nlp/tree-of-thought-llm](https://github.com/princeton-nlp/tree-of-thought-llm) | scanned | reasoning-thinking | idea only, not built |  | task accuracy: +5-15% ESTIMATE | category |
| [hkust-nlp/simpleRL-reason](https://github.com/hkust-nlp/simpleRL-reason) | scanned | reasoning-thinking | idea only, not built |  | task accuracy: +5-15% ESTIMATE | category |
| [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve) | scanned | recursive-self-improvement | idea only, not built |  | benchmark score per iteration: +5-20% ESTIMATE | category |
| [MineDojo/Voyager](https://github.com/MineDojo/Voyager) | scanned | recursive-self-improvement | idea only, not built |  | benchmark score per iteration: +5-20% ESTIMATE | category |
| [zou-group/textgrad](https://github.com/zou-group/textgrad) | scanned | recursive-self-improvement | idea only, not built |  | benchmark score per iteration: +5-20% ESTIMATE | category |
| [noahshinn/reflexion](https://github.com/noahshinn/reflexion) | scanned | recursive-self-improvement | idea only, not built |  | benchmark score per iteration: +5-20% ESTIMATE | category |
| [jennyzzt/dgm](https://github.com/jennyzzt/dgm) | scanned | recursive-self-improvement | idea only, not built |  | benchmark score per iteration: +5-20% ESTIMATE | category |
| [openai/codex](https://github.com/openai/codex) | scanned | sandboxed-code-exec | idea only, not built |  | sandbox escape surface: large reduction ESTIMATE | category |
| [daytonaio/daytona](https://github.com/daytonaio/daytona) | scanned | sandboxed-code-exec | idea only, not built |  | sandbox escape surface: large reduction ESTIMATE | category |
| [firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker) | scanned | sandboxed-code-exec | idea only, not built |  | sandbox escape surface: large reduction ESTIMATE | category |
| [google/gvisor](https://github.com/google/gvisor) | scanned | sandboxed-code-exec | idea only, not built |  | sandbox escape surface: large reduction ESTIMATE | category |
| [e2b-dev/E2B](https://github.com/e2b-dev/E2B) | scanned | sandboxed-code-exec | idea only, not built |  | sandbox escape surface: large reduction ESTIMATE | category |
| [containers/bubblewrap](https://github.com/containers/bubblewrap) | scanned | sandboxed-code-exec | idea only, not built |  | sandbox escape surface: large reduction ESTIMATE | category |
| [superradcompany/microsandbox](https://github.com/superradcompany/microsandbox) | scanned | sandboxed-code-exec | idea only, not built |  | sandbox escape surface: large reduction ESTIMATE | category |
| [yamadashy/repomix](https://github.com/yamadashy/repomix) | scanned | token-saving-compression | idea only, not built |  | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) | category |
| [mit-han-lab/streaming-llm](https://github.com/mit-han-lab/streaming-llm) | scanned | token-saving-compression | idea only, not built |  | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) | category |
| [microsoft/LLMLingua](https://github.com/microsoft/LLMLingua) | scanned | token-saving-compression | idea only, not built |  | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) | category |
| [gptscript-ai/gptscript](https://github.com/gptscript-ai/gptscript) | scanned | token-saving-compression | idea only, not built |  | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) | category |
| [FasterDecoding/Medusa](https://github.com/FasterDecoding/Medusa) | scanned | token-saving-compression | idea only, not built |  | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) | category |
| [SafeAILab/EAGLE](https://github.com/SafeAILab/EAGLE) | scanned | token-saving-compression | idea only, not built |  | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) | category |
| [Zefan-Cai/KVCache-Factory](https://github.com/Zefan-Cai/KVCache-Factory) | scanned | token-saving-compression | idea only, not built |  | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) | category |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | scanned | tool-use-mcp | idea only, not built |  | new-tool integration time: -50-80% ESTIMATE | category |
| [upstash/context7](https://github.com/upstash/context7) | scanned | tool-use-mcp | idea only, not built |  | new-tool integration time: -50-80% ESTIMATE | category |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | scanned | tool-use-mcp | idea only, not built |  | new-tool integration time: -50-80% ESTIMATE | category |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | scanned | tool-use-mcp | idea only, not built |  | new-tool integration time: -50-80% ESTIMATE | category |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | scanned | tool-use-mcp | idea only, not built |  | new-tool integration time: -50-80% ESTIMATE | category |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | scanned | tool-use-mcp | idea only, not built |  | new-tool integration time: -50-80% ESTIMATE | category |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | scanned | tool-use-mcp | idea only, not built |  | new-tool integration time: -50-80% ESTIMATE | category |
| [Genesis-Embodied-AI/genesis-world](https://github.com/Genesis-Embodied-AI/genesis-world) | scanned | world-simulation | idea only, not built |  | studio realism / agent-life features: qualitative ESTIMATE | category |
| [joonspk-research/generative_agents](https://github.com/joonspk-research/generative_agents) | scanned (REA timed out, partial) | world-simulation | idea only, not built |  | studio realism / agent-life features: qualitative ESTIMATE | category |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | scanned | world-simulation | idea only, not built |  | studio realism / agent-life features: qualitative ESTIMATE | category |
| [Farama-Foundation/Gymnasium](https://github.com/Farama-Foundation/Gymnasium) | scanned | world-simulation | idea only, not built |  | studio realism / agent-life features: qualitative ESTIMATE | category |
| [a16z-infra/ai-town](https://github.com/a16z-infra/ai-town) | scanned | world-simulation | idea only, not built |  | studio realism / agent-life features: qualitative ESTIMATE | category |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | scanned | world-simulation | idea only, not built |  | studio realism / agent-life features: qualitative ESTIMATE | category |
| [microsoft/TinyTroupe](https://github.com/microsoft/TinyTroupe) | scanned | world-simulation | idea only, not built |  | studio realism / agent-life features: qualitative ESTIMATE | category |
| [OpenBMB/AgentVerse](https://github.com/OpenBMB/AgentVerse) | scanned | world-simulation | idea only, not built |  | studio realism / agent-life features: qualitative ESTIMATE | category |
| [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | scanned | llms-open-inference | idea only, not built |  | cost per 1M tokens: -50-90% vs paid API ESTIMATE | category |
| [TadasBaltrusaitis/OpenFace](https://github.com/TadasBaltrusaitis/OpenFace) | scanned | k-affective-computing | idea only, not built |  | empathy-label accuracy (needs eval): ESTIMATE only; consent-required data | category |
| [declare-lab/MELD](https://github.com/declare-lab/MELD) | scanned | k-affective-computing | idea only, not built |  | empathy-label accuracy (needs eval): ESTIMATE only; consent-required data | category |
| [audeering/opensmile](https://github.com/audeering/opensmile) | scanned | k-affective-computing | idea only, not built |  | empathy-label accuracy (needs eval): ESTIMATE only; consent-required data | category |
| [CheyneyComputerScience/CREMA-D](https://github.com/CheyneyComputerScience/CREMA-D) | scanned | k-affective-computing | idea only, not built |  | empathy-label accuracy (needs eval): ESTIMATE only; consent-required data | category |
| [google-deepmind/alphafold](https://github.com/google-deepmind/alphafold) | scanned | k-biology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [biopython/biopython](https://github.com/biopython/biopython) | scanned | k-biology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [aqlaboratory/openfold](https://github.com/aqlaboratory/openfold) | scanned | k-biology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [sokrypton/ColabFold](https://github.com/sokrypton/ColabFold) | scanned | k-biology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [scverse/scanpy](https://github.com/scverse/scanpy) | scanned | k-biology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | scanned | k-coding | idea only, not built |  | coding task success: +5-15% ESTIMATE | category |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | scanned | k-coding | idea only, not built |  | coding task success: +5-15% ESTIMATE | category |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | scanned | k-coding | idea only, not built |  | coding task success: +5-15% ESTIMATE | category |
| [tldr-pages/tldr](https://github.com/tldr-pages/tldr) | scanned | k-coding | idea only, not built |  | coding task success: +5-15% ESTIMATE | category |
| [freeCodeCamp/devdocs](https://github.com/freeCodeCamp/devdocs) | scanned | k-coding | idea only, not built |  | coding task success: +5-15% ESTIMATE | category |
| [bigcode-project/the-stack-v2](https://github.com/bigcode-project/the-stack-v2) | scanned | k-coding | idea only, not built |  | coding task success: +5-15% ESTIMATE | category |
| [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | scanned | k-engineering | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [openscad/openscad](https://github.com/openscad/openscad) | scanned | k-engineering | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [OpenFOAM/OpenFOAM-dev](https://github.com/OpenFOAM/OpenFOAM-dev) | scanned | k-engineering | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [python-control/python-control](https://github.com/python-control/python-control) | scanned | k-engineering | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [sympy/sympy](https://github.com/sympy/sympy) | scanned | k-geometry; k-sciences | idea only, not built |  | 3D floor mesh ops: curriculum ESTIMATE | category |
| [isl-org/Open3D](https://github.com/isl-org/Open3D) | scanned | k-geometry | idea only, not built |  | 3D floor mesh ops: curriculum ESTIMATE | category |
| [CGAL/cgal](https://github.com/CGAL/cgal) | scanned | k-geometry | idea only, not built |  | 3D floor mesh ops: curriculum ESTIMATE | category |
| [mikedh/trimesh](https://github.com/mikedh/trimesh) | scanned | k-geometry | idea only, not built |  | 3D floor mesh ops: curriculum ESTIMATE | category |
| [geogebra/geogebra](https://github.com/geogebra/geogebra) | scanned | k-geometry | idea only, not built |  | 3D floor mesh ops: curriculum ESTIMATE | category |
| [riscv/riscv-isa-manual](https://github.com/riscv/riscv-isa-manual) | scanned | k-hardware | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [YosysHQ/yosys](https://github.com/YosysHQ/yosys) | scanned | k-hardware | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [lowRISC/opentitan](https://github.com/lowRISC/opentitan) | scanned | k-hardware | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [openhwfoundation/cva6](https://github.com/openhwfoundation/cva6) | scanned | k-hardware | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [KiCad/kicad-source-mirror](https://github.com/KiCad/kicad-source-mirror) | scanned | k-hardware | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [adafruit/Adafruit_CircuitPython_Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle) | scanned | k-hardware | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe) | scanned | k-human-behavior | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) | scanned | k-human-behavior | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [MIT-LCP/mimic-code](https://github.com/MIT-LCP/mimic-code) | scanned | k-human-behavior; k-medicine | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [synthetichealth/synthea](https://github.com/synthetichealth/synthea) | scanned | k-medicine | idea only, not built |  | n/a: curriculum ESTIMATE; not medical advice | category |
| [openmedlab/Awesome-Medical-Dataset](https://github.com/openmedlab/Awesome-Medical-Dataset) | scanned | k-medicine | idea only, not built |  | n/a: curriculum ESTIMATE; not medical advice | category |
| [kiwix/kiwix-tools](https://github.com/kiwix/kiwix-tools) | scanned | k-medicine | idea only, not built |  | n/a: curriculum ESTIMATE; not medical advice | category |
| [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | scanned | k-medicine | idea only, not built |  | n/a: curriculum ESTIMATE; not medical advice | category |
| [AllenInstitute/AllenSDK](https://github.com/AllenInstitute/AllenSDK) | scanned | k-neurology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [bids-standard/bids-specification](https://github.com/bids-standard/bids-specification) | scanned | k-neurology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [OpenNeuroOrg/openneuro](https://github.com/OpenNeuroOrg/openneuro) | scanned | k-neurology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [neuropsychology/NeuroKit](https://github.com/neuropsychology/NeuroKit) | scanned | k-physiology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [MIT-LCP/wfdb-python](https://github.com/MIT-LCP/wfdb-python) | scanned | k-physiology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [PIA-Group/BioSPPy](https://github.com/PIA-Group/BioSPPy) | scanned | k-physiology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [physiozoo/physiozoo](https://github.com/physiozoo/physiozoo) | scanned | k-physiology | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [Qiskit/qiskit](https://github.com/Qiskit/qiskit) | scanned | k-quantum | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [quantumlib/Cirq](https://github.com/quantumlib/Cirq) | scanned | k-quantum | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [microsoft/QuantumKatas](https://github.com/microsoft/QuantumKatas) | scanned | k-quantum | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [PennyLaneAI/pennylane](https://github.com/PennyLaneAI/pennylane) | scanned | k-quantum | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [qutip/qutip](https://github.com/qutip/qutip) | scanned | k-quantum | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [astropy/astropy](https://github.com/astropy/astropy) | scanned | k-sciences | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [wikimedia/mediawiki](https://github.com/wikimedia/mediawiki) | scanned | k-sciences | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [rdkit/rdkit](https://github.com/rdkit/rdkit) | scanned | k-sciences | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [kiwix/kiwix-js](https://github.com/kiwix/kiwix-js) | scanned | k-sciences | idea only, not built |  | n/a: curriculum ESTIMATE | category |
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | scanned | agent/bot optimization | LANDED: technique -> OPT-08 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | route-by-size 207.5->171.5 compute units/50 tasks (-17.3%) (local bench, artifacts/v2/src/opt/bench.mjs) |  | optimize-26 |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | scanned | agent/bot optimization | LANDED: technique -> OPT-10, OPT-13 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | clip tool output 12464->2021 tokens (-83.8%); capped retry 7->20 of 20 flaky tasks finished (local bench, artifacts/v2/src/opt/bench.mjs) |  | optimize-26 |
| [apache/airflow](https://github.com/apache/airflow) | scanned | workflow orchestration | LANDED: technique -> OPT-12 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | parallel waves 10->4 sequential steps (-60%) (local bench, artifacts/v2/src/opt/bench.mjs) |  | optimize-26 |
| [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | scanned | workflow orchestration | LANDED: technique -> OPT-13, OPT-14 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | capped retry 7->20/20; duplicate-done errors 1->0 (local bench, artifacts/v2/src/opt/bench.mjs) |  | optimize-26 |
| [temporalio/temporal](https://github.com/temporalio/temporal) | scanned | workflow orchestration | LANDED: technique -> OPT-13, OPT-14, OPT-24 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | capped retry 7->20/20; duplicate-done 1->0; Retry-After violations 2->0 (local bench, artifacts/v2/src/opt/bench.mjs) |  | optimize-26 |
| [openai/tiktoken](https://github.com/openai/tiktoken) | scanned | token efficiency | LANDED: technique -> OPT-07, OPT-11 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | fit-budget 20239->512 max tokens (-97.5%); pack-context 0% on V2-051 fixture, -2.9% on BUILD-LOG (local bench, artifacts/v2/src/opt/bench.mjs) |  | optimize-26 |
| [zilliztech/GPTCache](https://github.com/zilliztech/GPTCache) | scanned | token efficiency | LANDED: technique -> OPT-05, OPT-06, OPT-09 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | cache -40% / -66.7% model calls; diff-only summary 21876->20518 tokens (-6.2%) (local bench, artifacts/v2/src/opt/bench.mjs) |  | optimize-26 |
| [a2aproject/A2A](https://github.com/a2aproject/A2A) | scanned | multi-agent collaboration | LANDED: technique -> OPT-16, OPT-17 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | handoff envelope 85->39 tokens (-54.1%); capability route 15->1 messages (-93.3%) (local bench, artifacts/v2/src/opt/bench.mjs) |  | optimize-26 |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | not REA-scanned (vendored dependency) | 3d-rendering | LANDED: vendored library renders the 3D studio floor (PR #241 https://github.com/vitalitychems-dot/TESSERA/pull/241) and agent-world homes (PR #242 https://github.com/vitalitychems-dot/TESSERA/pull/242) | v2 tests 48/48 (#241), 53/53 (#242) pass locally; no perf number |  | dependency (not in scan lists) |
