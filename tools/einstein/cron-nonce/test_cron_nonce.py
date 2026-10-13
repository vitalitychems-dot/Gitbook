import unittest,secrets,math,time,collections
from cron_nonce import *
N=600;K=10000
class Rand(unittest.TestCase):
    d=[jitter(N,1800) for _ in range(K)]
    def test_range(self): self.assertTrue(0<=min(self.d) and max(self.d)<N)
    def test_cap_below_timeout(self): self.assertTrue(all(jitter(10**6,300)<240 for _ in range(1000)));self.assertRaises(ValueError,jitter,10,30)
    def test_chi2_uniform(self):  # 20 bins, df=19, p=0.001 crit 43.82
        c=collections.Counter(x*20//N for x in self.d);e=K/20
        self.assertLess(sum((c[i]-e)**2/e for i in range(20)),43.82)
    def test_serial_corr(self):
        x=self.d;m=sum(x)/K;v=sum((a-m)**2 for a in x)
        r=sum((x[i]-m)*(x[i+1]-m) for i in range(K-1))/v;self.assertLess(abs(r),4/math.sqrt(K))
    def test_unpredictable(self):  # predict next bin (of 20) as the bin that most often followed the previous bin; must not beat chance
        b=[x*20//N for x in self.d];T=collections.defaultdict(collections.Counter);hit=0
        for i in range(1,K):
            if T[b[i-1]]: hit+=T[b[i-1]].most_common(1)[0][0]==b[i]
            T[b[i-1]][b[i]]+=1
        p=1/20;sd=math.sqrt(K*p*(1-p));self.assertLess(hit,K*p+4*sd)
    def test_nonce_128bit_unique(self):
        s={nonce() for _ in range(K)};self.assertEqual(len(s),K);self.assertTrue(all(len(n)==32 for n in s))
class Pass(unittest.TestCase):
    def setUp(self): self.sk=Ed25519PrivateKey.generate();self.v=Verifier([self.sk.public_key()]);self.sha="a"*40
    def test_valid(self): m,s=sign(self.sk,self.sha);self.assertEqual(self.v.check(m,s,self.sha),"ACCEPT")
    def test_replay(self): m,s=sign(self.sk,self.sha);self.v.check(m,s,self.sha);self.assertEqual(self.v.check(m,s,self.sha),"REJECT replay")
    def test_wrong_sha(self): m,s=sign(self.sk,self.sha);self.assertEqual(self.v.check(m,s,"b"*40),"REJECT sha")
    def test_forged_key(self): m,s=sign(Ed25519PrivateKey.generate(),self.sha);self.assertEqual(self.v.check(m,s,self.sha),"REJECT sig")
    def test_tampered(self):
        m,s=sign(self.sk,self.sha);m2=m.replace(m.split(b" ")[2],nonce().encode());self.assertEqual(self.v.check(m2,s,self.sha),"REJECT sig")
    def test_stale(self):
        n=nonce();ts=int(time.time())-7200;m=pass_msg(self.sha,n,ts);self.assertEqual(self.v.check(m,self.sk.sign(m),self.sha),"REJECT stale")
    def test_ttl_expiry_frees_memory(self):
        m,s=sign(self.sk,self.sha);self.v.check(m,s,self.sha);self.v.check(b"x",b"",self.sha,now=int(time.time())+7200);self.assertEqual(len(self.v.seen),0)
unittest.main()
