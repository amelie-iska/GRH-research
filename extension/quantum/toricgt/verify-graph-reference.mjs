import fs from 'node:fs';
import crypto from 'node:crypto';
import {runGraph} from './graph-reference.js';
const base=new URL('./',import.meta.url);
const read=p=>JSON.parse(fs.readFileSync(new URL(p,base),'utf8'));
const weights=read('results/browser-weights.json'),dataset=read('data/dataset-v1.json');
const run=read('results/training-v1/quantum-seed17/run.json');
const cases=[];let maximum=0;
for(const split of ['test','ood'])for(let i=0;i<2;i++){
  const graph=dataset.splits[split][i],expected=run.metrics[split].examples[i];
  if(graph.id!==expected.id)throw Error('Dataset identity mismatch');
  const actual=runGraph(graph,weights);
  const error=Math.max(...actual.predictedDistancesUnits.map((v,j)=>Math.abs(v-expected.predicted_distance_units[j])))/32;
  maximum=Math.max(maximum,error);
  if(error>2e-5)throw Error('Full forward mismatch '+error);
  if(JSON.stringify(actual.pathResult.proposed_path)!==JSON.stringify(expected.proposed_path))throw Error('Learned path mismatch');
  if(JSON.stringify(actual.pathResult.final_certificate)!==JSON.stringify(expected.final_certificate))throw Error('Certificate mismatch');
  cases.push({split,index:i,id:graph.id,text:graph.text,node_prediction_max_error:error,certificate_match:true});
}
const original=runGraph(dataset.splits.test[0],weights),theta=structuredClone(weights.state_dict.theta);
theta[0][0][0]+=.4;const changed=runGraph(dataset.splits.test[0],weights,theta);
const change=Math.max(...original.predictionsNormalized.map((x,i)=>Math.abs(x-changed.predictionsNormalized[i])));
if(change<1e-7)throw Error('Theta override did not change full model predictions');
const source_sha256=Object.fromEntries(['reference.js','graph-reference.js','results/browser-weights.json'].map(p=>[p,crypto.createHash('sha256').update(fs.readFileSync(new URL(p,base))).digest('hex')]));
const result={schema:'quantum-toricgt-browser-fullforward-verification-v1',passed:true,node:process.version,cases,max_node_prediction_error:maximum,theta_override_max_prediction_change:change,source_sha256,precision:'JavaScript float64 plus erf approximation versus PyTorch CUDA float32; tolerance2e-5 in normalized prediction.'};
fs.writeFileSync(new URL('results/browser-fullforward-verification.json',base),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));
