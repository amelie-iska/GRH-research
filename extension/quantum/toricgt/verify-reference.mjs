import fs from 'node:fs';
import {simulateWeylToken,parameterShiftJacobian} from './reference.js';
const input = process.argv[2];
if (!input) throw new Error('Supply the independent Python verification JSON.');
const fixtures=JSON.parse(fs.readFileSync(input,'utf8')).reference_cases;
let featureError=0,stateError=0,jacobianError=0,normError=0;
for (const item of fixtures) {
  const actual=simulateWeylToken(item.angles,item.theta,true);
  const jac=parameterShiftJacobian(item.angles,item.theta);
  normError=Math.max(normError,Math.abs(actual.norm-1));
  for(let j=0;j<6;j++) {
    featureError=Math.max(featureError,Math.abs(actual.features[j]-item.features[j]));
    for(let p=0;p<12;p++) jacobianError=Math.max(jacobianError,Math.abs(jac[j][p]-item.jacobian[j][p]));
  }
  for(let j=0;j<8;j++) for(const part of ['real','imag'])
    stateError=Math.max(stateError,Math.abs(actual.state[part][j]-item.state[part][j]));
  if(actual.gateTrace.length!==16) throw new Error('Circuit trace has the wrong gate count.');
}
if(Math.max(featureError,stateError,jacobianError,normError)>2e-12) throw new Error('Independent JavaScript comparison failed.');
console.log(JSON.stringify({passed:true,cases:fixtures.length,featureError,stateError,jacobianError,normError},null,2));
