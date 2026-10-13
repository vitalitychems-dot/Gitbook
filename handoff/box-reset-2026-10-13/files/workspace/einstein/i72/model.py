import random,statistics as S
z=[int(l.split()[1]) for l in open('sizes.txt')];r=[int(l.split()[0]) for l in open('sizes.txt')]
random.seed(1)
def ci(x,f):
  b=sorted(f(random.choices(x,k=len(x))) for _ in range(10000));return f(x),b[250],b[9750]
for n,x in(('raw',r),('zstd19',z)):
  print(n,'mean %.0f [%.0f,%.0f]'%ci(x,S.mean),'median %.0f [%.0f,%.0f]'%ci(x,S.median))
eff=0.9  # 222B payload / ~13B LoRaWAN hdr
links={'LoRa SF12 EU 1%duty':293*.01,'LoRa SF7 EU 1%duty':5470*.01,'LoRa SF7 US915 no duty':5470,'APRS 1200':1200,'HF 300':300,'2G GPRS 40k':40000}
m=S.median(z)
for k,b in links.items():
  bps=b*eff; print('%-24s %8.1f bps  t/page(median) %9.0f s  pages/day %8.0f'%(k,bps,m*8/bps,86400*bps/8/m))
