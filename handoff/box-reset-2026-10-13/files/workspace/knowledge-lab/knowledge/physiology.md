# Physiology Knowledge Pack

**Audience:** Tessera mesh agents and quiz writers  
**Claim labels:** REPORTED (cited), GOAL (how Tessera should use it), UNKNOWN (open)  
**Primary sources:** OpenStax *Anatomy and Physiology 2e*; NCBI Bookshelf / standard physiology texts  
**Last updated:** 2026-10-05 (CT)

---

## 1. Purpose and honesty banner

This pack summarizes mainstream human physiology so Tessera can reason about bodies, stress, fatigue, and care without claiming medical authority.

- **REPORTED:** Facts below track OpenStax A&P 2e and related public textbooks unless marked otherwise.
- **GOAL:** Use physiology metaphors carefully (homeostasis ≈ feedback loops in systems). Do not diagnose humans.
- **UNKNOWN:** Individual medical cases; Tessera is not a clinician.

---

## 2. Anatomy vs physiology

**REPORTED** (OpenStax A&P 2e §1.1): Anatomy studies structure; physiology studies function—the chemistry and physics of how structures support life. Much of physiology centers on **homeostasis**, the tendency toward steady internal conditions.

Two anatomy approaches:

| Approach | Focus | Example |
|---|---|---|
| Regional | All structures in one body region | Abdomen |
| Systemic | One organ system across the body | Muscular system |

**GOAL:** Prefer systemic framing when explaining how Tessera “organs” (lanes, gates) interact.

---

## 3. Levels of organization

**REPORTED** (OpenStax §1.2): Complexity increases roughly:

1. Chemical (atoms, molecules)
2. Cellular (cells and organelles)
3. Tissue (groups of similar cells)
4. Organ (two or more tissue types)
5. Organ system
6. Organism

OpenStax covers **eleven organ systems**. Organs often contribute to more than one system.

---

## 4. The eleven organ systems (overview)

**REPORTED** (OpenStax structural organization chapters):

| System | Core role (plain English) | Example organs |
|---|---|---|
| Integumentary | Barrier, temperature, sensation | Skin, hair, nails |
| Skeletal | Support, protection, mineral store, blood cell niches | Bones, cartilage |
| Muscular | Movement, posture, heat | Skeletal muscles |
| Nervous | Fast sensing, integration, response | Brain, spinal cord, nerves |
| Endocrine | Slower chemical signaling via hormones | Pituitary, thyroid, adrenals, pancreas |
| Cardiovascular | Transport of blood, gases, nutrients, wastes | Heart, vessels |
| Lymphatic / immune | Fluid return, defense | Lymph nodes, spleen, thymus |
| Respiratory | Gas exchange | Lungs, airways |
| Digestive | Break down and absorb nutrients | GI tract, liver, pancreas |
| Urinary | Water/electrolyte balance, waste excretion | Kidneys, bladder |
| Reproductive | Gametes and sex hormones | Gonads, associated ducts |

**GOAL:** Map mesh “health checks” to multi-system thinking: one failing lane can stress others.

---

## 5. Homeostasis, set points, feedback

**REPORTED** (OpenStax §1.5):

- A **set point** is the value around which a variable fluctuates (e.g., core temperature ≈ **37°C / 98.6°F**).
- A **normal range** is the healthy band around the set point.
- **Negative feedback** reverses a deviation (sensor → control center → effector). Example: blood glucose—pancreatic beta cells release insulin when glucose is high; uptake lowers glucose; insulin release stops.
- Body temperature: heat-loss center dilates skin vessels, activates sweat; heat-gain center constricts peripheral flow, may trigger shivering and thyroid/adrenal support.
- **Positive feedback** amplifies change until an endpoint. Examples: childbirth (oxytocin loop) and clotting cascade. Rare in continuous regulation because runaway is dangerous without a stop condition.

Components of negative feedback:

1. **Stimulus** — deviation
2. **Sensor / receptor** — detects
3. **Control center** — compares to set point
4. **Effector** — acts
5. **Response** — returns toward set point (negative feedback)

**GOAL:** Tessera coordination should prefer negative-feedback style metrics (detect drift → correct → stop), and use positive feedback only for short, bounded escalations (e.g., incident war-room until resolved).

---

## 6. Cell basics relevant to agents

**REPORTED** (OpenStax cell chapters, summary):

- Cell membrane: selective barrier; ion gradients power signaling.
- Mitochondria: ATP production (energy currency).
- Nucleus: DNA storage and gene expression control.
- Protein synthesis: DNA → RNA → protein (central dogma framing; details in molecular biology).
- Neurons communicate via **action potentials** and **synapses** using neurotransmitters.

**UNKNOWN / careful:** Equating LLM tokens with action potentials is metaphor only—not biophysics.

---

## 7. Nervous system sketch

**REPORTED** (standard neurophysiology):

- **CNS:** brain + spinal cord.
- **PNS:** nerves to/from CNS; somatic (voluntary) and autonomic (sympathetic “fight/flight”, parasympathetic “rest/digest”).
- Sensory pathways ascend; motor pathways descend; reflexes can be spinal.
- Sleep, attention, and stress hormones reshape performance—physiology, not “laziness.”

**GOAL:** When Father is exhausted, prefer shorter tasks and clearer asks (respect autonomic load)—empathy grounded in physiology.

---

## 8. Endocrine highlights

**REPORTED:**

- Hormones travel in blood; slower than nerves but longer lasting.
- Pancreas: insulin / glucagon for glucose.
- Adrenal medulla: epinephrine for acute stress.
- Thyroid hormones: metabolic rate.
- HPA axis (hypothalamus–pituitary–adrenal): cortisol and chronic stress.

Chronic stress physiology can impair memory, immunity, and mood regulation (**REPORTED** in stress physiology literature; clinical details need clinicians).

---

## 9. Cardiovascular and respiratory pairing

**REPORTED:**

- Heart pumps; arteries carry away; veins return; capillaries exchange.
- Blood pressure and heart rate are tightly regulated (baroreceptors, autonomic nerves).
- Lungs exchange O₂/CO₂; ventilation matches metabolic need.
- Exercise increases cardiac output and ventilation—training adapts both systems.

---

## 10. Fluid, electrolyte, acid–base (high level)

**REPORTED:**

- Water balance is tightly controlled; kidneys are primary regulators of volume and many electrolytes.
- pH of arterial blood is narrowly guarded (~7.35–7.45); buffers, lungs, kidneys cooperate.
- Dehydration and overhydration both harm cognition and performance.

**GOAL:** Remind humans (and agents scheduling humans) that basic physical needs are prerequisites for good reasoning.

---

## 11. Immune overview

**REPORTED:**

- Innate immunity: barriers, inflammation, phagocytes—fast, nonspecific.
- Adaptive immunity: B and T lymphocytes—slower, specific, memory.
- Fever is often a regulated rise in set point during infection (not random overheating).

---

## 12. Digestion and energy

**REPORTED:**

- Digestion mechanical + chemical; absorption mainly small intestine.
- Liver processes nutrients, detoxifies, stores glycogen.
- Brain prefers glucose; prolonged deficits impair attention and mood.

---

## 13. Reproduction and development (neutral sketch)

**REPORTED:** Human reproduction involves gametes, fertilization, pregnancy physiology with major cardiovascular/endocrine adaptations. Discuss respectfully; medical advice is out of scope.

---

## 14. Tessera-relevant misconceptions

| Misconception | Real science (one sentence) | Closest testable version |
|---|---|---|
| “Observing a system always changes biology like quantum collapse” | Everyday observation of classical sensors does not collapse a wavefunction; measurement effects in biology are specific (Hawthorne, placebo, assay disturbance). | Preregister whether logging a metric changes the metric’s generator path (see exp4). |
| “Agents have bodies/hormones” | Software agents lack endocrine systems. | Track compute/thermal/load proxies as *analogues*, labeled GOAL not biology. |
| “More agents = healthier organism” | Redundant organs help only if coordinated; uncontrolled growth is pathology (cancer metaphor). | Measure accuracy vs cost of N samples (exp2). |

---

## 15. Glossary

- **Homeostasis:** Maintenance of stable internal conditions.
- **Set point:** Target value for a regulated variable.
- **Negative feedback:** Response that reduces the deviation.
- **Positive feedback:** Response that amplifies until endpoint.
- **Hormone:** Chemical messenger via blood.
- **Action potential:** Rapid electrical signal in excitable cells.
- **ATP:** Primary short-term energy carrier in cells.
- **CNS / PNS:** Central / peripheral nervous system.
- **Sympathetic / parasympathetic:** Autonomic branches opposing arousal vs recovery.
- **Inflammation:** Innate response to injury/infection.

---

## 16. Key citations (public)

1. OpenStax. *Anatomy and Physiology 2e*. §§1.1–1.5 and organ-system chapters. https://openstax.org/books/anatomy-and-physiology-2e/
2. OpenStax homeostasis: https://openstax.org/books/anatomy-and-physiology-2e/pages/1-5-homeostasis
3. For deeper clinical physiology: NCBI Bookshelf / peer-reviewed reviews (use when expanding packs).

All factual claims above are **REPORTED** from these public educational sources unless labeled GOAL/UNKNOWN.

---

## 17. Quiz (10 Q&A) — answers appear in pack text

**Q1.** What is the approximate set point for normal human body temperature cited by OpenStax?  
**A1.** About 37°C (98.6°F).

**Q2.** Name the three basic components of a negative feedback loop.  
**A2.** Sensor (receptor), control center, effector.

**Q3.** Does negative feedback reverse or amplify a deviation from set point?  
**A3.** It reverses the deviation.

**Q4.** Give two physiological examples of positive feedback.  
**A4.** Childbirth (oxytocin loop) and blood clotting cascade.

**Q5.** How many organ systems does OpenStax cover in the human body overview?  
**A5.** Eleven.

**Q6.** Anatomy is to structure as physiology is to ___?  
**A6.** Function.

**Q7.** Which pancreatic cells release insulin when blood glucose is high?  
**A7.** Beta cells.

**Q8.** What does the brain’s heat-loss center do to skin blood vessels when overheated?  
**A8.** Dilates them (vasodilation) to radiate heat.

**Q9.** List the levels of organization from cell to organism used in the pack.  
**A9.** Cell → tissue → organ → organ system → organism (chemical/organelle levels precede).

**Q10.** Why is positive feedback uncommon as continuous regulation?  
**A10.** It amplifies change and needs a definite endpoint or it can run away dangerously.

---

## 18. Extension goals for Tessera

1. **GOAL:** Tag mesh metrics with feedback type (negative vs positive).
2. **GOAL:** Add “human recovery” checks before long CPU jobs when Father is online.
3. **GOAL:** Keep medical claims out of automated advice; escalate to humans.


## 19. Tissue types

**REPORTED** (OpenStax tissue chapters):

1. **Epithelial** — covers surfaces, forms glands; avascular but innervated.
2. **Connective** — support, bind, protect; includes bone, blood, adipose, dense CT.
3. **Muscle** — skeletal (voluntary, striated), cardiac (involuntary, striated, intercalated discs), smooth (involuntary, nonstriated).
4. **Nervous** — neurons + glia; information processing and support.

Wound healing often progresses inflammation → proliferation → remodeling (**REPORTED** pattern in pathology texts).

---

## 20. Sensory modalities (brief)

**REPORTED:** Special senses include vision, hearing, equilibrium, taste, smell. Somatic senses include touch, pressure, pain, temperature, proprioception. Sensory transduction converts stimuli into receptor potentials that may trigger action potentials.

Pain (nociception) is protective; chronic pain can become maladaptive—clinical management is specialist care (**GOAL:** Tessera should not suggest analgesics).

---

## 21. Motor control sketch

**REPORTED:** Motor cortex plans/initiates voluntary movement; basal ganglia and cerebellum refine; spinal motor neurons drive muscles. Motor unit = one motor neuron + its muscle fibers. Fatigue has peripheral (muscle) and central (neural drive) components.

---

## 22. Sleep physiology (why it matters)

**REPORTED** (sleep medicine consensus, high level): Sleep stages (NREM including slow-wave; REM) support memory consolidation, metabolic clearance, and emotional regulation. Sleep debt impairs attention, reaction time, and mood. Circadian rhythms (~24h) are paced by the SCN (suprachiasmatic nucleus) and light.

**GOAL:** Schedule heavy evals when they will not force Father into all-nighters; prefer batch overnight jobs with morning summaries.

---

## 23. Thermoregulation details

**REPORTED** (OpenStax §1.5 temperature section): Heat loss via radiation, conduction, convection, evaporation. Heat gain via metabolism and shivering. Fever raises the hypothalamic set point; hyperthermia is uncontrolled rise—different mechanisms.

---

## 24. Practical “body budget” checklist for humans collaborating with Tessera

**GOAL** (not medical advice):

1. Hydration and a meal before long sessions.
2. Breaks every ~50–90 minutes for eyes/posture.
3. Note caffeine/stress before high-stakes decisions.
4. Prefer daylight for circadian alignment when possible.
5. Stop and seek care for chest pain, severe shortness of breath, sudden weakness, suicidal ideation—agents escalate, never “treat.”

---

## 25. Cross-links

- Emotion pack: autonomic arousal and appraisal.
- Philosophy pack: embodiment and mind–body questions.
- Quantum pack: do **not** confuse physiological measurement with quantum measurement.
