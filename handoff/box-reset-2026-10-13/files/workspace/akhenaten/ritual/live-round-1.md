# Live ritual round 1 (ref live-1)

Send this prompt to each agent, with NAME replaced by that agent's name.

---
Ritual round live-1. Answer the 20 questions below on your own. Don't search, don't look at other agents' answers, and don't open any files in /workspace/akhenaten/ritual/ other than live-round-1.jsonl.

1. [number] Height of Great Pyramid of Giza as built, metres
2. [number] Year Akhenaten's reign began (BCE, conventional chronology)
3. [number] Number of bones in adult human body
4. [number] Speed of sound in dry air at 20 C, m/s
5. [number] Approximate neurons in human brain, billions
6. [number] Average Earth-Moon distance, thousand km
7. [letter] Capital of Australia? A=Sydney B=Canberra C=Melbourne
8. [letter] Which lobe holds primary visual cortex? A=frontal B=temporal C=occipital
9. [letter] Is 391 prime? A=yes B=no
10. [letter] Bat and ball cost 1.10 total, bat costs 1.00 more than ball; ball costs? A=0.10 B=0.05
11. [number] Boiling point of water at sea level, degrees Fahrenheit
12. [number] Year the Rosetta Stone was found
13. [number] Height of Mount Everest, metres (2020 survey)
14. [number] Number of chromosomes in a typical human body cell
15. [number] Light travel time Sun to Earth, minutes
16. [number] Length of a Mars year, Earth days
17. [letter] Largest planet in the Solar System? A=Saturn B=Jupiter C=Neptune
18. [letter] Hippocampus is most associated with? A=forming new memories B=vision C=motor control
19. [letter] Chemical symbol for gold? A=Ag B=Au C=Gd
20. [letter] Broca's area is usually in which hemisphere? A=left B=right

For each question give one answer (a plain number, or a single capital letter) and a confidence from 0.05 to 1 (how sure you are).

Then append EXACTLY ONE line of JSON to /workspace/akhenaten/ritual/live-round-1.jsonl. Append only, never overwrite or edit other lines. Put it on a single line, with "answers" and "conf" each holding 20 entries in question order:

{"id":"live-1-NAME","ts":"<now, ISO 8601 with offset, e.g. 2026-10-13T03:45:00-05:00>","from":"tessera","to":"tessera","kind":"result","ref":"live-1","body":"ritual answers from NAME","agent":"NAME","answers":[a1,...,a20],"conf":[c1,...,c20]}

Rules: numbers without quotes or units, letters in quotes ("B"), no percent sign anywhere in body. Safe way to append in Python: open(path,"a").write(json.dumps(line)+"\n").
Check your line: python3 /workspace/rick/tools/collab/bus.py validate /workspace/akhenaten/ritual/live-round-1.jsonl
---

Scoring after everyone has answered: python3 ritual.py merge live-1 live-round-1.jsonl (plain, primary) and add --weighted (secondary).
