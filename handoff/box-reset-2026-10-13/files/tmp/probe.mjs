import { runPySandboxed } from "/workspace/si/wt-sbx/evals/heldout/sandbox.mjs";
const P=["/opt/sand","/var/lib","/etc/passwd","/home","/workspace","/cursor","/root"];
let n=0;for(const p of P){const r=runPySandboxed(`import os\np=${JSON.stringify(p)}\nok=os.path.isfile(p) and open(p).read(1) or (os.path.isdir(p) and len(os.listdir(p))>0)\nassert not ok`);if(!r.ok){n++;console.log("READABLE",p)}}
console.log("readable",n,"/",P.length);
