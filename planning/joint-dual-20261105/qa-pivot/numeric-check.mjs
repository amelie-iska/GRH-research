import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {pivotState} from '../../../web/quadratic-pivot.mjs';
const expected=JSON.parse(readFileSync(new URL('./independent-expectations.json',import.meta.url)));
const near=(a,b,label)=>assert(Math.abs(a-b)<=3e-12*Math.max(1,Math.abs(b)),`${label}: ${a} versus ${b}`);
for(const c of expected.cases){
 const s=pivotState(c.a,c.dLog);
 for(const key of ['oldPower','quadPower','refinedPower','saving','targetGap','capacity','D','H','A','B','R','oldSum','quadSum','refinedSum'])near(s[key],c[key],`${c.a}/${c.dLog}/${key}`);
 for(const key of ['oldPowers','quadPowers','oldTerms','quadTerms','Aj'])s[key].forEach((v,i)=>near(v,c[key][i],`${key}[${i}]`));
 assert.equal(s.strictSaving,c.strictSaving);
 assert(s.refinedPower>.75,'No point attains target');
 near(s.A*s.B,s.H**(1/3),'AB=H^(1/3)');
 near(s.capacity,s.H,'Weighted row capacity, not R');
}
for(const [a,d] of [[-1,12],[.251,12],[NaN,12],[0,-1],[0,101],[0,NaN]])assert.throws(()=>pivotState(a,d),RangeError);
const report={passed:true,cases:expected.cases.length,checks:['exact Fraction exponents on the complete 1001-point slider lattice','independent Decimal monomials and sums at all five D scales','strict endpoint/crossover/one-step-neighbor sector checks','weighted capacity and AB identity','all refined powers strictly exceed target','invalid input refusal'],scope:'Independent algebraic evaluation checks; does not reprove the external analytic large sieve or certify arithmetic row energies.'};
writeFileSync(new URL('../../../outputs/checks/2026-11-05-joint-dual/qa-pivot/numeric.json',import.meta.url),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report));
