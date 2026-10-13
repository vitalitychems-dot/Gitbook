# Live ritual round 4 (ref live-4)
Send to each agent, with NAME replaced by that agent's own name. Each agent must write its own line.
---
Ritual round live-4. The 12 items below were generated just now from a secret random seed, so nobody can recall them. Estimate each one by eye in a single pass: no counting tools, no code, no calculator, no web, no other files. Rough is fine; we are measuring estimation.

1. How many times does the digit 6 appear in this 300-digit block?
263285348045634022244153881914573578593579358167505684847994338953507348887915229285513292974814555978018454357148180604903703874746377564643792911426370540402610302502646075284205047842706453659142771155425429280241900315943107698793643738941480009772987702680288024021353982587660375447307245798698

2. How many times does the digit 2 appear in this 300-digit block?
814442619032423815353481574308656624070799203160111094002866767844172998933946791044496812390539656101743700754872925894427430702828498434550617508915403067424856574485759253867086413829128754746681404517954856059471167760325917891948297409416431879334147201407873224481187518922594028896100572916657

3. How many times does the digit 9 appear in this 300-digit block?
535988182739776440705461791147210972141328202416402326693434471150420902319434392246608535264124921575448134597779365051021411426762591507126478661510965213819737961117950143924904127231051430815656975021038967559534852459239181267514365955857378674228478940211330922053516697791564261634350818789495

4. Estimate the mean of these 40 numbers (1 decimal).
512 413 970 635 289 746 973 615 442 198 757 705 701 598 915 668 891 591 249 580 949 400 370 86 194 82 210 390 395 895 238 826 652 867 150 951 309 3 658 472

5. Estimate the mean of these 40 numbers (1 decimal).
303 83 495 635 194 921 118 609 869 514 881 490 190 182 163 250 991 239 506 276 473 671 54 443 555 782 624 242 516 870 542 560 830 929 413 299 917 892 60 591

6. Estimate the mean of these 40 numbers (1 decimal).
425 35 10 865 527 142 875 276 7 522 657 646 36 869 613 975 828 297 735 178 886 689 785 897 758 629 805 81 439 646 525 55 304 363 869 35 337 416 196 289

7. How many of these 120 words start with the letter 'k'?
zero do do suze ka ze taveno ze mifero re mi rene sutoli do ve ro rone kano tota fetami wikane nosuka su feja nedo dopa mi tareta ve do ka litata buga bufeve jaga mi do fepano wi japa ja su toja ro ne sulisu jaho negafe pa pasu ga nomisu limi re taho vero subune jafepa romi hoga ro hozebu notato bu buzeka romi re roline re ta paho bu to jaroro tabure zeka tofeja ze ve vemi no ja feli ho ganoga sure witosu toto wi pali ro ka veja repa resuno rezesu re lito roze vefeja nokaga vega pa li rehosu no ka tore buga tozene ja bu no doze pa hono ze nokano suga to

8. How many of these 120 words start with the letter 'n'?
felija fega fe zerodo liwiwi bupare bu ne fere ho re mifega nomi feka honewi suno gapado butata fe hobu to wiro gazeno mi ne ho reho hoka fe mito dobuka gaja zemimi ze gawiwi kasuno wili hoga fe mino mimi ne tomive to to mi pa suno re ga nomipa tagave feto ve ka topaze ze vefe wiwino jaka ze tawido su hota tami kahomi kave jahopa ga fekano fe wireka jajare vekasu mili su wiho toroho jasuja su neta garega togaho kata vekafe lipa wijami no bufe bu gawi ho jare gamisu liwita lihore ne ta lilipa ronosu tone kapa vetami ka felibu bune surota paveho re vefene jazedo gado sunopa mi feta ze jazeja roga doli ne

9. How many of these 120 words start with the letter 't'?
do to kanepa pami vere ja zeta fe kataka papa pa hoto ze vegasu dota re wine buve su wino vepato veremi noro ro ta jarere li liwi rota gasuta su ta su ro katapa taroho wijare jadoli sunere limika neta ro sune domi misupa su suzeho nowi li nevesu to paka suze su nero jata gasuto ga do vepa mi ze paze mibu vejaze mihodo sujasu roneli dohono togave to ne torere jakabu nemi su nesu veno hojano hoja mi buga pa wisuja zeno roja susu ve to bu ga tota zeja ho su kaja zehore bubuze noze re minoka honoze buho pa rero dofe rofeho li remi ze mika gaho li fenore jami veroja dove lilibu tata zeli

10. Estimate the sum of these 25 numbers.
98 97 91 59 92 96 18 10 39 33 10 62 75 70 57 50 21 74 93 81 69 62 73 70 73

11. Estimate the sum of these 25 numbers.
79 76 27 84 82 70 71 39 26 85 72 57 81 99 86 65 62 30 55 75 79 20 14 72 35

12. Estimate the sum of these 25 numbers.
18 98 64 94 28 96 36 89 86 91 97 67 47 38 40 70 51 79 65 65 22 70 51 13 24

For each item give a number and a confidence from 0.05 to 1. Then append EXACTLY ONE line (one line per agent, written by you) to /workspace/akhenaten/ritual/live-round-4.jsonl:
{"id":"live-4-NAME","ts":"<ISO 8601 with offset>","from":"NAME","to":"tessera","kind":"result","ref":"live-4","body":"ritual answers from NAME","agent":"NAME","answers":[a1,...,a12],"conf":[c1,...,c12]}
"from" and "agent" must both be your own name. A round with a mismatched line, or with two lines from one sender, is rejected. Append with open(path,"a").write(json.dumps(line)+"\n").
---
Score: python3 ritual.py merge live-4 live-round-4.jsonl   (add --weighted for the secondary score)
