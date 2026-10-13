// Faithful copy of assertFileWrite + findLane from PR #6 @ d9c4f1e0 (service.ts / routing.ts)
const lanes=[{id:"tessera",name:"Tessera",mode:"admin",fileWrites:true},{id:"security",name:"Security",mode:"read-only",fileWrites:false},{id:"build",name:"Build",mode:"verify-only",fileWrites:false}];
const findLane=(l,id)=>{if(!id)return undefined;return l.find(x=>x.id===id)};
function make(agentLane){return function assertFileWrite(explicitLane){const laneId=explicitLane?.trim()||agentLane;const lane=findLane(lanes,laneId);if(lane&&lane.fileWrites===false)throw new Error(`${lane.name} is ${lane.mode} and cannot open draft pull requests`);}}
const cases=[["security",undefined],["security","tessera"],["security","Security"],["build","nonexistent"],["Security",undefined],[undefined,undefined]];
for(const [env,arg] of cases){let r;try{make(env)(arg);r="ALLOWED"}catch(e){r="BLOCKED"}console.log(`env GITBOOK_AGENT_LANE=${env} lane arg=${arg} -> ${r}`)}
