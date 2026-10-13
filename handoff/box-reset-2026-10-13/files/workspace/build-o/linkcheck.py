import re,sys,os
bad=0
for f in sys.argv[1:]:
  for m in re.finditer(r'\]\(([^)#\s]+)(#[^)]*)?\)', open(f).read()):
    u=m.group(1)
    if re.match(r'[a-z]+:',u): continue
    p=os.path.normpath(os.path.join(os.path.dirname(f),u))
    if not os.path.exists(p): print("BROKEN",f,u); bad+=1
print("linkcheck files=%d broken=%d"%(len(sys.argv)-1,bad)); sys.exit(1 if bad else 0)
