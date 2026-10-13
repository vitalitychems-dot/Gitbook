# REA of Father's photos (2026-10-13)
I looked at 18 images (the Flux ad was excluded). They show 8 GitHub repos, 3 other public projects, 5 of our own screenshots and 2 claims/posts. GitHub stats were fetched on 2026-10-13. No repos were cloned (the GitHub API was enough), nothing outside was modified, and nothing was pushed.

| # | Photo shows | GitHub / URL | Stars | License | What it really does | Safety | Would help |
|---|---|---|---|---|---|---|---|
| 1 | FreeLLMAPI | github.com/tashfeenahmed/freellmapi | 34.3k | MIT | One OpenAI-style /v1 endpoint over free tiers of 34 LLM providers. A router picks a model, fails over when one is rate-limited, and tracks usage per key | OK. Each provider's ToS still applies; we use only our own keys | collab (router prototyped) |
| 2 | camofox-browser | github.com/jo-inc/camofox-browser | 11.6k | MIT | Stealth headless browser that spoofs fingerprints to "bypass Cloudflare, bot detection, anti-scraping" | **EXCLUDED**: it is built to evade sites' access controls and scrape against their terms | none |
| 3 | Open WebUI | github.com/open-webui/open-webui | 155k | Open WebUI License (BSD-3 + branding clause) | Self-hosted ChatGPT-style UI for Ollama/OpenAI APIs, with RAG and hybrid search | OK | palace/allsee (hybrid search tested, rejected) |
| 4 | Supabase | github.com/supabase/supabase | 111k | Apache-2.0 | Postgres plus auth, storage and realtime APIs (open Firebase alternative) | OK | mesh bus/collab later (not prototyped; heavy) |
| 5 | Stirling PDF | github.com/Stirling-Tools/Stirling-PDF | 94k | MIT core + proprietary parts | Local PDF toolkit: merge, split, OCR, redact | OK | palace (OCR PDFs into the index; not prototyped) |
| 6 | Coolify | github.com/coollabsio/coolify | 62.9k | Apache-2.0 | Self-hosted Heroku/Vercel alternative | OK, but it needs Docker, which Security says not to use on port 2375 | not adopted on this box |
| 7 | Open-Gen-AI | github.com/Anil-matcha/Open-Generative-AI | 30.2k | MIT | Image/video generation studio that calls hosted models; markets itself as "unrestricted" | Caution: "unrestricted" generation means deepfake/NSFW risk. Not adopted | none |
| 8 | Vibe-Trading | github.com/HKUDS/Vibe-Trading | 35.4k | MIT | LLM trading agent: backtests, multi-agent debate | Trading is off-limits for us. Only the debate/ensemble idea was taken, for science forecasts | simons (prototyped) |
| 9 | Argos Atlas | argosatlas.com (website, not a repo; tab title "Mapa de 175.000 cámaras") | – | proprietary | Global map of ~172k public cameras, flights, ships, satellites | **Camera layer EXCLUDED** (it watches people). Flight/ship/satellite layers already exist in Eye v3/v4 | tessera-eye (nothing new) |
| 10 | Perchance | perchance.org (site) | – | – | Free text-to-image generator with no login | OK to use by hand; no repo to study | none |
| 11 | moltbook post "I can modify my own source code" | moltbook.com (AI-agent social site) | – | – | Discussion post about the risks of self-modifying agents | Supports our gates: self-changes need tests and review | V-plan gates (no change) |
| 12 | BHNMC-X infographic | concept art, no repo | – | – | Bio-hybrid computer concept | Specs like 10^30 OPS are not physical claims | already in bhnmc/ |
| 13 | "TV that never needs plugging in" (Maxwell Chikumbutso, Accra Metropolitan Univ. post) | Instagram post | – | – | Claimed free-energy TV | Hoax-class claim. Ambient RF gives microwatts, and a TV needs about 50–100 W | none |
| 14–18 | Our own screenshots: Tesseract 5D, Eye v4 Bean zoom, Eye v3 globe, Mesh City, Simons heat map | /workspace/rick/tools/... | – | ours | – | – | – |

## Adaptations (prototypes in /workspace/rick/src/rea/proto, `python3 -m unittest test_proto` passes 2/2)
1. **KEPT: skill-weighted "debate" ensemble → simons** (`debate_ensemble.py`), from Vibe-Trading's multi-agent debate. Each forecaster (mean7, mean30, ridge_all, ridge_survivors) votes, weighted by 1/MAE² over the last 30 days it has already seen. A test confirms there is no lookahead. One-year holdout (365 days): MAE 5.736 → **5.701 (−0.6%)**. Bootstrap 95% CI of the gain is +0.015 to +0.055. Small but real. Note that W=30, p=2 was picked from 6 settings tried on the same holdout, so the true gain may be smaller. Not merged into simons.py yet.
2. **KEPT (simulation only): free-tier router with failover → collab** (`router.py`), from FreeLLMAPI. 4 simulated backends with per-minute quotas against about 50 requests/min, 20 seeds: one backend serves 39.2%, round-robin 77.3%, **router 98.5%**. Calls per served request drop 2.55 → 1.03. Mean quality is 0.794, versus 0.900 for the single best backend. This is a model, not real providers.
3. **REJECTED: Open WebUI-style hybrid search (BM25 + path ranker, RRF) → palace** (`hybrid_palace.py`). Real 10-query benchmark: 7 → 9/10. But on 40 held-out queries it scored 24 → 18 (path-boost 0.5: 21). It overfits, so under Father's rule it is not kept. Dedupe-only changed nothing (24/24).


## Eye Shield anti-surveillance study (2026-10-13)
Public signatures from Argos / Flock_SCAN / Camofox / Red Sparrow were catalogued for **defense only** under `tools/eye-shield/signatures/`. See `tools/eye-shield/RESULTS.md`. Not installed, not run, no camera feeds, no firewall changes.
