// Read-only scientific connectivity counterexamples; no browser/dependencies.
import {backboneMesh} from '../../../web/molecular-structure.mjs';
import {mkdirSync,writeFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const atom=(index,position,segment=0)=>({index,position,chain:'A',segment,seq:index+1,secondary:'coil',icode:' ',carbonyl:100+2*index,nitrogen:101+2*index});
const disconnected={atoms:[],bonds:[],backbone:[atom(0,[0,0,0]),atom(1,[3.8,0,0])]};
const fragments={atoms:[],bonds:[{a:102,b:105,kind:'peptide'}],backbone:[atom(0,[100,100,100],0),atom(1,[0,0,0],1),atom(2,[3.8,0,0],1)]};
const patches=backboneMesh(disconnected),mixed=backboneMesh(fragments);
const centers=mixed.flatMap(p=>[p.vertices.slice(0,2),p.vertices.slice(2,4)]).map(pair=>pair[0].map((v,i)=>(v+pair[1][i])/2));
const perpendicularExcursion=Math.max(0,...centers.map(v=>Math.hypot(v[1],v[2])));
if(patches.length!==0||mixed.length!==10||perpendicularExcursion>1e-12)throw Error('Peptide connectivity or segment controls failed');
const result={passed:true,validConnectedFragmentPatches:mixed.length,disconnectedBackboneRibbonPatches:patches.length,
 differentTERSegmentControlInfluenceExcursion:perpendicularExcursion,
 expected:{disconnectedBackboneRibbonPatches:0,differentTERSegmentControlInfluenceExcursion:0},
 scope:'Connectivity/control-point counterexamples; not a full PDB/SDF parser test'};
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const out=path.join(root,'outputs/checks/2026-11-04-synthetic-training/review');mkdirSync(out,{recursive:true});
writeFileSync(path.join(out,'ribbon-review.json'),JSON.stringify(result,null,2)+'\n');console.log(result);
