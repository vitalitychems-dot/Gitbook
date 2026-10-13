import sys,re,html
t=sys.stdin.read();t=re.sub(r'(?is)<(script|style).*?</\1>','',t);t=re.sub(r'<[^>]+>',' ',t);t=html.unescape(t)
t=re.sub(r'[ \t]+',' ',t);t=re.sub(r'\s*\n\s*','\n',t);print(t.strip())
