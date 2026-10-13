import math,itertools,datetime,fractions,random
from fractions import Fraction as F
def isprime(n): return n>1 and all(n%p for p in range(2,int(n**.5)+1))
r={}
r[1]=round(1-math.prod((365-i)/365 for i in range(30)),4)
r[2]=6; r[3]=10  # Markov chain; checked below by simulation
r[4]=sum(isprime(n) for n in range(10000))
r[5]=sum(1000//5**k for k in range(1,6))
d=[1,0]; [d.append((n-1)*(d[-1]+d[-2])) for n in range(2,9)]; r[6]=d[8]
r[7]=float(F(3,4)*F(1,2))  # 4 doors, host opens 1 goat, switch to one of 2 random
a,b=1,1
for _ in range(11): a,b=b,a+b
r[8]=b
r[9]=sum(map(int,str(2**100)))
r[10]=round(6*sum(1/k for k in range(1,7)),2)
r[11]=sum(1 for k in range(1,math.factorial(10)+1) if math.factorial(10)%k==0)
r[12]=13*math.comb(4,3)*12*math.comb(4,2)
ps=[n for n in range(2,600) if isprime(n)][:100]; r[13]=sum(ps)
r[14]="F" if datetime.date(2100,1,1).weekday()==4 else "?"
r[15]="A" if math.e**math.pi>math.pi**math.e else "B"
r[16]="A" if isprime(1000003) else "B"
r[17]=510.1; r[18]=5.15
r[19]=round(149597870700/299792458,1)
# Tuesday boy: enumerate
kids=[(s,d) for s in "BG" for d in range(7)]
pairs=[(x,y) for x in kids for y in kids if ("B",1) in (x,y)]
p=F(sum(x[0]==y[0]=="B" for x,y in pairs),len(pairs)); r[20]="C" if p==F(13,27) else p
# sim checks for 2,3,7
rng=random.Random(1)
def flips(t):
    s="";
    while not s.endswith(t): s+=rng.choice("HT")
    return len(s)
print("sim HH",sum(flips("HH") for _ in range(20000))/20000,"HTH",sum(flips("HTH") for _ in range(20000))/20000)
w=0
for _ in range(100000):
    car=rng.randrange(4); pick=0; opn=rng.choice([x for x in range(1,4) if x!=car]); sw=rng.choice([x for x in range(1,4) if x!=opn]); w+=sw==car
print("sim monty4",w/100000)
for k,v in r.items(): print(k,v)
