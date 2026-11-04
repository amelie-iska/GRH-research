// Read-only actual browser-model fixtures for independent Python matrix checks.
import {bellStrategy,magicStrategy,hermitianSpectrum} from '../../../web/quantum-game-model.mjs';
import {dessinCellModel} from '../../../web/hubs-spokes-model.mjs';
import {mkdirSync,writeFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';import path from 'node:path';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const fixtures=[];
const magicParameters=[Array.from({length:2},(_,l)=>Array.from({length:2},(_,q)=>[.17+l*.3,.41+q*.2,-.23+l*.1])),Array.from({length:2},(_,l)=>Array.from({length:2},(_,q)=>[-.31+l*.1,.23+q*.3,.52-l*.1]))];
for(const visibility of [0,.37,1])for(const spec of [
 {kind:'bell',alpha:0,parameters:[Math.PI/4,0,Math.PI/2,Math.PI/4,-Math.PI/4]},
 {kind:'bell',alpha:1.5,parameters:[.31,.17,1.23,.41,-.79]},
 {kind:'magic',parameters:magicParameters},
 {kind:'magic',parameters:magicParameters.map(p=>p.map(l=>l.map(q=>q.map(()=>0))))}
]){
 const S=spec.kind==='magic'?magicStrategy(spec.parameters,visibility):bellStrategy(spec.parameters,spec.alpha,visibility),n=spec.kind==='magic'?3:2;
 fixtures.push({...spec,visibility,score:S.score,joints:Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>S.joint(i,j))),moment:S.moment,spectrum:hermitianSpectrum(S.moment)});
}
const out=path.join(root,'outputs/checks/2026-11-04-synthetic-training/review');mkdirSync(out,{recursive:true});
writeFileSync(path.join(out,'games-browser-fixtures.json'),JSON.stringify({fixtures,drawings:[3,5,9].flatMap(m=>[false,true].map(f=>dessinCellModel(m,f)))},null,2)+'\n');
console.log('12 browser probability/moment fixtures and6 dessin fixtures exported for independent review');
