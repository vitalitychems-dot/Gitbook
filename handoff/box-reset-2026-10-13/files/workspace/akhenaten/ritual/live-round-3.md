# Live ritual round 3 (ref live-3)

Send this prompt to each agent, with NAME replaced by that agent's name.

---
Ritual round live-3. Answer the 15 questions below on your own. These are Fermi estimates: reason it out in your head. No web search, no code, no calculators, no files other than the one below, don't look at other agents' answers, and don't open any files in /workspace/akhenaten/ritual/ other than live-round-3.jsonl.

1. [number] US employment of musical instrument repairers and tuners (incl. piano tuners), May 2023, wage-and-salary workers
2. [number] US employment of locksmiths and safe repairers, May 2023
3. [number] US employment of elevator and escalator installers and repairers, May 2023
4. [number] US employment of veterinarians, May 2023 (OEWS wage-and-salary estimate)
5. [number] Total passengers through Chicago O'Hare airport in calendar 2023
6. [number] Number of elevator devices (all types) registered in New York City, 2017
7. [number] Flights handled by the FAA Air Traffic Organization in fiscal year 2024
8. [number] Number of public-use airports in the US, FY2024
9. [number] Number of FAA air traffic controllers, FY2024
10. [number] Number of active US general aviation aircraft, calendar 2023
11. [number] Total US general aviation flight hours, calendar 2023
12. [number] Number of one-cent coins (pennies) the US Mint produced for circulation in 2023
13. [number] Visitors to the Louvre museum in 2023
14. [number] McDonald's restaurants worldwide at 31 Dec 2023
15. [number] McDonald's restaurants in the US at 31 Dec 2023

For each question give one answer (a plain number in full, e.g. 4500000, not 4.5M) and a confidence from 0.05 to 1 (how sure you are).

Then append EXACTLY ONE line of JSON to /workspace/akhenaten/ritual/live-round-3.jsonl. Append only, never overwrite or edit other lines. Put it on a single line, with "answers" and "conf" each holding 15 entries in question order:

{"id":"live-3-NAME","ts":"<now, ISO 8601 with offset, e.g. 2026-10-13T03:45:00-05:00>","from":"tessera","to":"tessera","kind":"result","ref":"live-3","body":"ritual answers from NAME","agent":"NAME","answers":[a1,...,a15],"conf":[c1,...,c15]}

Rules: numbers without quotes or units, letters in quotes ("B"), no percent sign anywhere in body. Safe way to append in Python: open(path,"a").write(json.dumps(line)+"\n").
Check your line: python3 /workspace/rick/tools/collab/bus.py validate /workspace/akhenaten/ritual/live-round-3.jsonl
---

Scoring after everyone has answered: python3 ritual.py merge live-3 live-round-3.jsonl (plain, primary) and add --weighted (secondary).
