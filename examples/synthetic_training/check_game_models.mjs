import assert from 'node:assert/strict';import {readFileSync,writeFileSync} from 'node:fs';
import {bellStrategy,magicStrategy,hermitianSpectrum} from '../../web/quantum-game-model.mjs';
const games=JSON.parse(readFileSync('web/data/synthetic-training/games-v1/games.json')).games;
let maxScore=0,maxNormalization=0,maxSignal=0,minProbability=1,minMoment=0,cases=0;
for(const game of games)for(const checkpoint of [game.history[0],game.history.at(-1)])for(const visibility of [0,.37,1]){
 const S=game.kind==='magic'?magicStrategy(checkpoint.parameters,visibility):bellStrategy(checkpoint.parameters,game.alpha,visibility),qs=game.kind==='magic'?3:2;
 if(visibility===1){const e=Math.abs(S.score-checkpoint.score);maxScore=Math.max(maxScore,e);assert(e<2e-12);}
 assert(S.score<=S.quantum+2e-11);minMoment=Math.min(minMoment,...hermitianSpectrum(S.moment));
 const table=[];for(let x=0;x<qs;x++){table[x]=[];for(let y=0;y<qs;y++){const q=S.joint(x,y),p=game.kind==='magic'?q.probability:q;table[x][y]=p;
  minProbability=Math.min(minProbability,...p.flat());const normal=Math.abs(p.flat().reduce((a,b)=>a+b,0)-1);maxNormalization=Math.max(maxNormalization,normal);assert(normal<1e-11);}}
 for(let x=0;x<qs;x++)for(let y=0;y<qs;y++)for(let a=0;a<table[x][y].length;a++){
  maxSignal=Math.max(maxSignal,Math.abs(table[x][y][a].reduce((a,b)=>a+b,0)-table[x][0][a].reduce((a,b)=>a+b,0)));
  maxSignal=Math.max(maxSignal,Math.abs(table[x][y].reduce((v,row)=>v+row[a],0)-table[0][y].reduce((v,row)=>v+row[a],0)));}
 cases++;
}
assert(minProbability>-1e-12&&minMoment>-1e-9&&maxSignal<1e-11);
const stalled=games.find(g=>g.kind!=='magic'&&g.alpha===1.5&&g.seed===43);assert(Math.abs(stalled.history.at(-1).score-3.5)<1e-8);
const report={passed:true,strategies:games.length,cases,maxScore,maxNormalization,maxSignal,minProbability,minMoment,retained_stalled_seed:43};writeFileSync('outputs/checks/2026-11-04-synthetic-training/games-models.json',JSON.stringify(report,null,2)+'\n');console.log(report);
