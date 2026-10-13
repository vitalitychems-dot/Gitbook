#!/bin/bash
# usage: scan.sh repo_dir out_dir ; records file:line:type only (no values)
R=$1; O=$2; n=$(basename $R); mkdir -p $O
EX=(-g '!**/1T/**' -g '!**/*vault*' -g '!**/*vault*/**' -g '!**/node_modules/**' -g '!**/.git/**' -g '!*.lock' -g '!package-lock.json' -g '!*.min.js' --max-filesize 2M -uu)
declare -A P=(
 [github_token]='\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36}\b|github_pat_[A-Za-z0-9_]{60,}'
 [slack_token]='xox[bpars]-[A-Za-z0-9-]{10,}'
 [openai_like_sk]='\bsk-(proj-|ant-)?[A-Za-z0-9_-]{20,}'
 [aws_key]='\b(AKIA|ASIA)[A-Z0-9]{16}\b'
 [google_api_key]='AIza[0-9A-Za-z_-]{35}'
 [private_key]='-----BEGIN ([A-Z]+ )?PRIVATE KEY-----'
 [db_url_pw]='(postgres(ql)?|mysql|mongodb(\+srv)?|redis|amqp)://[^:/\s"'"'"']+:[^@\s"'"'"']+@'
 [stripe_live]='\b(sk|rk)_live_[A-Za-z0-9]{16,}'
 [xai_key]='\bxai-[A-Za-z0-9]{40,}'
 [pw_assign]='(?i)\b(password|passwd|secret|api_?key|token|client_secret)\s*[:=]\s*["'"'"'][^"'"'"'\s$\{<]{8,}["'"'"']'
)
for t in "${!P[@]}"; do rg -P -n -o "${EX[@]}" "${P[$t]}" $R 2>/dev/null | awk -F: -v t=$t -v n=$n '{print n"\t"$1":"$2"\t"t}' ; done > $O/$n.secrets
find $R -path '*/node_modules' -prune -o -path '*/.git' -prune -o \( -name '.env' -o -name '.env.*' -o -name '*.pem' -o -name 'id_rsa*' -o -name '*.key' \) -print 2>/dev/null | grep -viE 'vault|/1T/' | awk -v n=$n '{print n"\t"$0":0\tsecret_file"}' >> $O/$n.secrets
declare -A Q=(
 [wallet_seed]='(?i)\b(mnemonic|seed.?phrase|private.?key|secretKey)\b'
 [payments]='(?i)\b(stripe|paypal|square\.com|braintree|checkout\.session)\b'
 [web3]='(?i)\b(ethers|web3|@solana|solana/web3|wagmi|viem|metamask|walletconnect)\b'
 [auth]='(?i)\b(passport|next-auth|jsonwebtoken|bcrypt|/login|signIn\(|oauth)\b'
)
for t in "${!Q[@]}"; do rg -P -l "${EX[@]}" -g '*.{js,ts,tsx,jsx,py,go,rs,sol,mjs,cjs}' "${Q[$t]}" $R 2>/dev/null | awk -v t=$t -v n=$n '{print n"\t"$0"\t"t}'; done > $O/$n.risky
rg -P -n "${EX[@]}" 'IDENTITY:\s*Tessera' $R 2>/dev/null | awk -F: -v n=$n '{print n"\t"$1":"$2"\tidentity_text"}' > $O/$n.ident
if [ -d $R/.git ]; then git -C $R log --all --format='%H%x09%an%x09%cn%x09%G?%x09%ci%x09%s' 2>/dev/null > $O/$n.gitlog; fi
echo done > $O/$n.ok
