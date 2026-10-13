import { fetchRepo, rank } from "/tmp/wt-fb/scripts/feedback/outcome-feedback.mjs";
const all=[];for(const r of ["vitalitychems-dot/TESSERA","vitalitychems-dot/Gitbook"]) all.push(...fetchRepo(r).finished);
all.sort((a,b)=>a.number-b.number); // approx chronological per repo
const cut=Math.floor(all.length*0.8), train=all.slice(0,cut), test=all.slice(cut);
const out=rank({finished:train,candidates:test.map(t=>({repo:t.repo,number:t.number,title:t.title,kind:"x"}))});
const lab=new Map(test.map(t=>[t.repo+t.number,t.merged]));
const s=out.tasks.map(t=>[t.score,lab.get(t.repo+t.number)]);
const pos=s.filter(x=>x[1]),neg=s.filter(x=>!x[1]);let w=0;for(const p of pos)for(const n of neg)w+=p[0]>n[0]?1:p[0]===n[0]?.5:0;
const k=Math.ceil(test.length/4), top=out.tasks.slice(0,k).filter(t=>lab.get(t.repo+t.number)).length;
console.log({test:test.length,merged:pos.length,closed:neg.length,auc:(w/(pos.length*neg.length)).toFixed(3),topQuartileMergeRate:(top/k).toFixed(3),baseRate:(pos.length/test.length).toFixed(3)});
