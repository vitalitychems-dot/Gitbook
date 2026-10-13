# goodnight000/api-anything
- What it actually is: a **local website-to-operation recorder/replayer**. Headless Chromium watches a page make a request for two example inputs, templates it, then replays via Node fetch (tier 1) or in-browser fallback. Exposed via CLI, TS, MCP (list_sites, list_operations, call_operation, login). Not a gateway, not codegen, not a mock.
- License: MIT. ~780 stars, active. Not on npm; install = git clone + `npm ci && npm install -g $(npm pack)`. Node 22.13+, Chromium for learning.
- Ships 22 read ops across 9 sites (Google Flights, HN, X, Instagram, YouTube, Airbnb, Amazon, LinkedIn, Goodreads).
- "No longer need APIs": **marketing.** It only knows operations it was taught, breaks when sites change (repair can fail), no CAPTCHA, writes untested; it is still calling the sites' internal web endpoints. Our real APIs (GitHub, Gitbook, Gmail, etc.) are still needed and are the sanctioned path.
- Risks: imports cookies from signed-in browser profiles (~/.api-anything) — credential exposure; scraping may violate site ToS; conflicts with our rule against driving signed-in sessions / internal APIs when a sanctioned tool exists.
- **Verdict: SKIP** (free, but low value and credential/ToS risk). Re-evaluate only for a public, no-login read site with no official API, after Security review.
