# IDEAS-BUILD-1 (Oct 13, 2026, 1:10–1:30 AM CT)

PR: https://github.com/vitalitychems-dot/TESSERA/pull/251 (branch `ideas-b1-brain` on the rewritten main `23999aa`). It is **open and not merged**: it waits until the chunked history push reaches its final SHA.

Each number below comes from a real run. "Held-out" means data the code was never tuned on.

1. **Synapse layer** (Hebbian co-activation, decay, connectome modules). On held-out link recall (87 queries), recall@5 went from 2 to 13 (2.3% to 14.9%) and recall@10 from 2 to 14. Ablation: text overlap alone scores 2 and the synapse layer alone scores 13. **PASS, real gain.**
2. **Empathy / affect + intent recognition** (local lexicon, no network, no people-OSINT). On a 30-line held-out set, intent macro-F1 went from 0.076 (majority baseline) to 0.902 (27/30) and affect F1 from 0.200 to 0.881 (28/30). **PASS.** Caveat: the held-out set is small and I wrote and labelled it.
3. **Recursive learning loop** (outcomes update topic weights and synapses). On a 10-seed sim, round robin took 227.9 mean steps and the adaptive loop 232.1. Feedback learning on a held-out split moved recall@5 from 11/43 to 11/43. **NO GAIN.** It shipped as wiring only and no gain is claimed.
4. **Gated self-improvement**, suggest-only, flag `TESSERA_BRAIN_SELFPATCH` defaulting to 0, with 8 gates. Of 12 proposals, 8 were unsafe. A naive gate accepts all 8 unsafe ones; this gate accepted 0 unsafe and rejected 0 safe. **PASS.** It never applies or merges anything.
5. **3D /brain view** (three.js): auto-rotates, has a brain selector, edge brightness follows weight (WebGL lines are 1 px, so thickness can't vary), and pulses come from live Hebbian steps. The memory brain has 1412 nodes and 2292 edges, and 159 real edges fired in about 5 s. **Built.** Files in `brain-view/`:
   - `brain-memory.mp4`, `brain-memory.gif`
   - `brain-memory.png`, `brain-human.png`, `brain-flywire.png`, `brain-hemibrain.png`, `brain-celegans.png`, `brain-gpt2.png`
6. **Real connectome templates.** Each is a separate layer labelled by species, and all are listed in ATTRIBUTION.md:
   - Human HCP-MMP1.0, 360 parcels (Rosen & Halgren 2021, CC BY 4.0): 2048 edges, the top 10 per parcel.
   - FlyWire FAFB v783 (CC BY 4.0): 16,847,997 neuron-pair rows aggregated into 3528 neuropil edges covering 54,464,482 synapses, with excitatory/inhibitory sign from the predicted neurotransmitter.
   - hemibrain v1.2: 1503 ROI edges.
   - C. elegans (Cook 2019): 6625 edges.
   - GPT-2 small: a block-0 MLP slice with the top 5000 weights (MIT).
7. **Template as wiring prior.** recall@5 out of 87 queries, against a same-density random null (5 seeds):

   | Template | Real | Random null | Verdict |
   |---|---|---|---|
   | none (synapse layer only) | 13 | – | baseline |
   | human HCP | 13 | 13–14 | no gain |
   | FlyWire | 14 | 12–13 | +1 query, within noise |
   | hemibrain | 13 | 12–14 | no gain |
   | C. elegans | 13 | 13 | no gain |

   **Final pick:** no template prior for recall, since none beat random meaningfully. Human is the default *view* layer, as Father decided.
8. **Not done** (with reasons):
   - TRIBE / Algonauts 2025 and TRIBE v2 are licensed CC-BY-NC-4.0 and need gated LLaMA 3.2, V-JEPA2 and Wav2Vec-BERT (many GB, GPU), with the disk at 96%. Not run.
   - H01, MICrONS, MANC, the Allen atlas and the HCP anatomical centroids aren't added yet; human parcels are placed by force layout, not anatomy.
   - Mapping Tessera's memory onto human parcels exists only as a rank mapping inside the template eval.
   - Rick round 2 was already merged (#247), so it wasn't rebuilt.
   - The other "idea only" REA rows were deprioritized per Father's 1:14 AM message.
