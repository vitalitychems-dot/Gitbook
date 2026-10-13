#!/usr/bin/env python3
"""Eye Shield: defensive, read-only log watcher + threat-intel attribution (stdlib only).
Patterns modeled on fail2ban filters (GPL-2) and SigmaHQ rules (Detection Rule License 1.1); cited per rule."""
import re, os, sys, json, gzip, bisect, ipaddress, subprocess, time, math, collections
H=os.path.dirname(os.path.abspath(__file__)); F=os.path.join(H,'feeds')
IP=r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
RULES=[ # (id, kind, regex, source)
 ('ssh_fail','brute_force',r'sshd\[\d+\]: (?:Failed (?:password|publickey) for (?:invalid user )?\S+|Invalid user \S+) from '+IP,'fail2ban filter.d/sshd.conf; Sigma linux auth failures'),
 ('ssh_preauth','brute_force',r'sshd\[\d+\]: (?:Connection closed by|Disconnected from) (?:authenticating|invalid) user \S+ '+IP+r'.*preauth','fail2ban sshd.conf (aggressive)'),
 ('pam_fail','brute_force',r'pam_unix\(\S+:auth\): authentication failure;.*rhost='+IP,'fail2ban common pam'),
 ('fw_block','scan',r'(?:UFW BLOCK|IPTABLES|DROP).*SRC='+IP+r'.*DPT=(?P<port>\d+)','fail2ban portscan.conf style'),
 ('web_scan','web_attack',IP+r' \S+ \S+ \[[^\]]+\] "(?:GET|POST|HEAD) [^"]*(?:\.\./|/etc/passwd|wp-login\.php|/\.env|/\.git/|phpmyadmin|cgi-bin|\$\{jndi:|union(?:\s|%20)+select|<script)','Sigma web/webserver_generic (path traversal, log4shell, sqli); fail2ban apache-badbots'),
 ('web_404','scan',IP+r' \S+ \S+ \[[^\]]+\] "[A-Z]+ \S+ [^"]*" 404 ','fail2ban nginx-botsearch'),
]
SUSP=[ # suspicious commands seen in logs (sudo/audit/web payloads), Sigma linux process_creation
 (r'(?:curl|wget)\s+\S+\
