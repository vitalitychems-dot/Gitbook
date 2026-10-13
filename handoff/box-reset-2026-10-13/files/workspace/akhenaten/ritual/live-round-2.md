# Live ritual round 2 (ref live-2)

Send this prompt to each agent, with NAME replaced by that agent's name.

---
Ritual round live-2. Answer the 20 questions below on your own. Don't search, don't run code or calculators (estimate or reason in your head), don't look at other agents' answers, and don't open any files in /workspace/akhenaten/ritual/ other than live-round-2.jsonl.

1. [number] Probability at least two of 30 people share a birthday (365 equally likely days, no leap years), 4 decimals
2. [number] Expected number of fair coin flips until you first see two heads in a row (HH)
3. [number] Expected number of fair coin flips until you first see the pattern HTH
4. [number] How many primes are there below 10,000?
5. [number] How many trailing zeros does 1000! (1000 factorial) have?
6. [number] How many derangements of 8 items (permutations with no item in its original place)?
7. [number] Monty Hall with 4 doors: you pick one, host opens one goat door, you switch to one of the 2 other closed doors at random. Probability you win the car?
8. [number] Number of ways to tile a 2x12 rectangle with 1x2 dominoes
9. [number] Sum of the decimal digits of 2^100
10. [number] Expected number of rolls of a fair six-sided die to see all six faces (2 decimals)
11. [number] How many positive divisors does 10! have?
12. [number] How many 5-card hands from a standard 52-card deck are a full house?
13. [number] Sum of the first 100 prime numbers
14. [letter] What weekday is 1 January 2100? A=Wednesday B=Thursday C=Friday D=Saturday
15. [letter] Which is larger? A=e^pi B=pi^e
16. [letter] Is 1,000,003 prime? A=yes B=no
17. [number] Total surface area of Earth, million square km
18. [number] Total mass of Earth's atmosphere, in units of 10^18 kg
19. [number] Time for light to travel 1 astronomical unit, seconds (1 decimal)
20. [letter] A family has two children and at least one is a boy born on a Tuesday. Probability both are boys? A=1/2 B=1/3 C=13/27

For each question give one answer (a plain number, or a single capital letter) and a confidence from 0.05 to 1 (how sure you are).

Then append EXACTLY ONE line of JSON to /workspace/akhenaten/ritual/live-round-2.jsonl. Append only, never overwrite or edit other lines. Put it on a single line, with "answers" and "conf" each holding 20 entries in question order:

{"id":"live-2-NAME","ts":"<now, ISO 8601 with offset, e.g. 2026-10-13T03:45:00-05:00>","from":"tessera","to":"tessera","kind":"result","ref":"live-2","body":"ritual answers from NAME","agent":"NAME","answers":[a1,...,a20],"conf":[c1,...,c20]}

Rules: numbers without quotes or units, letters in quotes ("B"), no percent sign anywhere in body. Safe way to append in Python: open(path,"a").write(json.dumps(line)+"\n").
Check your line: python3 /workspace/rick/tools/collab/bus.py validate /workspace/akhenaten/ritual/live-round-2.jsonl
---

Scoring after everyone has answered: python3 ritual.py merge live-2 live-round-2.jsonl (plain, primary) and add --weighted (secondary).
