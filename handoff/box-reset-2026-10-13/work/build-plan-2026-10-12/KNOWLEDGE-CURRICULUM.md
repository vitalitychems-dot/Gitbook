# TESSERA Knowledge Curriculum (open knowledge to load offline)

As of 2026-10-12, 6:40 PM CT. These are **sizes as published by the source (ESTIMATE)**. I did not download them. The rule: prefer community or nonprofit sources, and note license and gatekeeper. Formats should work offline: Kiwix **ZIM**, JSONL, Parquet, SQLite or git.
P1 = load first (small, high value). P2 = next. P3 = large or specialist.

| # | Domain | Source | License | Gatekeeper | Format | Size (approx) | Priority |
|---|---|---|---|---|---|---|---|
| 1 | General | Wikipedia EN (Kiwix ZIM, nopic / maxi) | CC BY-SA 4.0 | Wikimedia (nonprofit) | ZIM | ~50 GB nopic / ~110 GB maxi | P1 (nopic) |
| 2 | Sciences | Wikibooks, Wikiversity, Wiktionary ZIM | CC BY-SA | Wikimedia | ZIM | 1–8 GB each | P1 |
| 3 | Medicine | WikiMed (Kiwix medicine ZIM) | CC BY-SA | Wikimedia/Kiwix | ZIM | ~2–10 GB | P1 |
| 4 | Medicine | MedlinePlus health topics XML | Public domain (US NLM). Govt-run, but no non-gov equivalent of the same quality, so kept | US NLM | XML→ZIM | <1 GB | P1 |
| 5 | Medicine/Biology | PubMed Central **Open Access subset** (commercial-use CC0/CC BY files only) | CC0/CC BY (per-article) | NIH (govt; only OA subset used) | XML/text bulk | ~100s GB full; take CC BY subset by field | P2 |
| 6 | Medicine | Europe PMC OA (mirror alternative to PMC) | per-article CC | EMBL-EBI (intergov. nonprofit) | XML | similar | P2 (alt to 5) |
| 7 | Medicine | Synthea synthetic patients | Apache-2.0 | MITRE (nonprofit) | CSV/FHIR | generated, any size | P1 |
| 8 | Medicine | Mondo disease ontology / HPO | CC BY 4.0 | Monarch Initiative | OBO/OWL/JSON | <500 MB | P1 |
| 9 | Physiology | PhysioNet **open-access** databases (e.g., MIT-BIH, not credentialed ones) | ODC-By / CC BY | MIT LCP | WFDB | 0.1–50 GB each | P2 |
| 10 | Neurology | OpenNeuro BIDS datasets (CC0) | CC0 | Stanford CRN (academic) | BIDS/NIfTI | GB–TB per set; pick 2–3 | P3 |
| 11 | Neurology | Allen Brain Atlas / connectivity | Allen terms (free, attribution) | Allen Institute (nonprofit) | API/NWB | large | P3 |
| 12 | Affective | CREMA-D (emotional speech) | ODbL | academic | wav+csv | ~2 GB | P2 (consent-sourced, research only) |
| 13 | Affective | MELD (multimodal emotion in dialogue) | GPL-3.0 | academic | csv+mp4 | ~10 GB | P3 |
| 14 | Affective | GoEmotions (text emotion) | Apache-2.0 | Google Research (big tech; no comparable-size alt) | TSV | <50 MB | P1 |
| 15 | Behavior | OpenStax Psychology / Sociology textbooks | CC BY 4.0 | Rice Univ. (nonprofit) | PDF/HTML→ZIM | <1 GB | P1 |
| 16 | Sciences | OpenStax full library (physics, chem, bio, A&P, calculus) | CC BY 4.0 | Rice Univ. | HTML/ZIM | ~5 GB | P1 |
| 17 | Sciences | arXiv metadata + CC-licensed full texts | per-paper (many CC BY) | Cornell (nonprofit) | JSONL / PDF | metadata ~4 GB | P2 |
| 18 | Sciences | LibreTexts ZIM | CC BY-NC-SA mostly (non-commercial: check use) | UC Davis | ZIM | ~10–20 GB | P2 |
| 19 | Coding | freeCodeCamp curriculum, free-programming-books, TheAlgorithms | BSD-3 / CC BY / MIT | community | git | <2 GB | P1 |
| 20 | Coding | DevDocs offline + tldr pages + Stack Exchange ZIM | MPL-2.0 / CC BY / CC BY-SA | community | JSON/ZIM | ~1 GB / ~80 GB SO | P1 (DevDocs, tldr) / P3 (SO) |
| 21 | Coding | The Stack v2 (permissive subset) | per-file permissive; ToU | BigCode/HF | Parquet | TBs | P3 |
| 22 | Hardware | RISC-V ISA manual, OpenTitan, Yosys, KiCad libs | CC BY 4.0 / Apache / ISC / CC BY-SA | community/foundations | git | <5 GB | P2 |
| 23 | Engineering | FreeCAD docs, OpenFOAM tutorials, python-control | LGPL / GPL / BSD | community | git/HTML | <3 GB | P2 |
| 24 | Quantum | Qiskit textbook, QuantumKatas, PennyLane demos, QuTiP | Apache / MIT / BSD | mixed (IBM/Microsoft repos are open-licensed; PennyLane and QuTiP are the non-big-tech alternatives) | notebooks | <2 GB | P2 |
| 25 | Geometry | CGAL manual, sympy geometry, trimesh, Open3D | GPL/LGPL / BSD / MIT | community | git/HTML | <3 GB | P2 |
| 26 | Biology | UniProt Swiss-Prot, PDB, Biopython tutorial, OpenFold weights | CC BY 4.0 / CC0 / BSD / Apache | EMBL-EBI / wwPDB / community | FASTA/mmCIF | Swiss-Prot ~0.3 GB; PDB ~250 GB | P1 (Swiss-Prot) / P3 (PDB) |
| 27 | All | Project Gutenberg ZIM | Public domain (US) | nonprofit | ZIM | ~60 GB | P3 |

**Load plan:**
- **P1 (~70 GB):** Wikipedia nopic, WikiMed, MedlinePlus, OpenStax, coding sets, Mondo, Synthea, Swiss-Prot, GoEmotions.
- Ingest each source into the knowledge-graph memory as *source entities* with license observations. Index chunks with the RAG layer (local embeddings), not the LLM.

**Rules:**
- Store attribution files.
- NC-licensed sources (LibreTexts) stay marked non-commercial.
- Medical content is reference only, not diagnosis.
- Affective and behavior data must be consent-sourced research sets. Never profile real people (people-OSINT stays excluded).
