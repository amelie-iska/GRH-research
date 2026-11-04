// Independent all-cell replay of the new inspector calculation branches.
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {validateTrace} from '../../../web/architecture-model.mjs';
import {cellDependencies} from '../../../web/architecture-layout.mjs';
import {surfaceProfile,selectionMapping} from '../../../web/surface-bridge-model.mjs';
import {thetaTree,depolarize,tropical,pantsAmplitude,chsh} from '../../../web/learned-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const read=p=>JSON.parse(readFileSync(path.join(root,p),'utf8'));
const manifest=read('web/data/learned-frontier/manifest.json'),results=[];
for(const entry of manifest.traces){
 const raw=readFileSync(path.join(root,'web/data/learned-frontier',entry.file));
 if(createHash('sha256').update(raw).digest('hex')!==entry.sha256)throw Error('Manifest checksum mismatch');
 const trace=validateTrace(JSON.parse(raw));let checked=0,maxError=0;
 for(const node of trace.nodes){
  if(node.id.startsWith('weight.'))continue;
  const shape=node.tensor.shape,total=shape.reduce((a,b)=>a*b,1);
  for(let j=0;j<total;j++){
   let index=j;const indices=shape.map(()=>0);
   for(let k=shape.length-1;k>=0;k--){indices[k]=index%shape[k];index=Math.floor(index/shape[k]);}
   const result=cellDependencies(trace,node,indices);
   if(result.verified){checked++;maxError=Math.max(maxError,result.error);if(result.error>3e-6)throw Error(`${trace.id} ${node.id} ${indices} error ${result.error}`);}
   const mapping=selectionMapping(trace,node,indices);
   if(!mapping)throw Error('Missing mapping');
  }
 }
 const surface=surfaceProfile(trace);
 if(surface.d.genus!==2)throw Error('Wrong actual genus');
 results.push({id:entry.id,nodes:trace.nodes.length,verifiedCells:checked,maxError,genus:surface.d.genus});
}
for(const [valence,radius] of [[3,8],[5,5],[9,3]]){
 const tree=thetaTree(radius,valence),expected=1+valence*((valence-1)**radius-1)/(valence-2);
 if(tree.nodes.length!==expected||tree.edges.length!==expected-1)throw Error('Tree count');
}
const rho=read('web/data/learned-frontier/lab.json').teacher.reduced_density;
const a=depolarize(depolarize(rho,.3),.7),b=depolarize(rho,1);
if(Math.max(...a.flat().map((x,i)=>Math.abs(x-b.flat()[i])))>1e-14)throw Error('Semigroup');
for(const tau of [.01,.1,1]){const t=tropical([-.3,.2,1],tau);if(t.gap<0||t.gap>t.bound+1e-14)throw Error('Tropical bound');}
if(pantsAmplitude(1)!==2||pantsAmplitude(1,2)!==0||pantsAmplitude(2)!==0)throw Error('Pants values');
if(Math.abs(chsh(1).quantum-(2+Math.sqrt(2))/4)>1e-14)throw Error('CHSH');
const output=path.join(root,'outputs/checks/2026-11-04-learned-frontier/review');mkdirSync(output,{recursive:true});
writeFileSync(path.join(output,'integrated-node.json'),JSON.stringify({passed:true,traces:results,treeChannelTropicalPantsGameChecks:true},null,2)+'\n');
console.log(JSON.stringify(results,null,2));
