import assert from 'node:assert/strict';
import{readFileSync,writeFileSync}from'node:fs';
import{pivotState,obstructionState}from'../../../web/quadratic-pivot.mjs';
import{pivotState as preserved}from'../../../outputs/checks/2026-11-05-arithmetic-learning/ui-pivot/previous/quadratic-pivot.mjs';
const e=JSON.parse(readFileSync(new URL('./expectations.json',import.meta.url)));
const near=(a,b,label)=>assert(Math.abs(a-b)<3e-12*Math.max(1,Math.abs(b)),`${label}: ${a} vs ${b}`);
for(const c of e.face){const s=pivotState(c.a,c.d),before=preserved(c.a,c.d);for(const k of Object.keys(before))assert.deepEqual(s[k],before[k],`Historical field ${k}`);for(const[k,expected]of[['oldPowers',c.old],['quadPowers',c.quad],['ordinaryPowers',c.ordinary]])s[k].forEach((v,i)=>near(v,expected[i],k));near(s.refinedPower,c.historical,'historical minimum');near(s.currentPower,c.current,'current');near(s.ordinarySum,c.ordinarySum,'ordinary sum');near(s.currentSum,c.currentSum,'current sum');near(s.currentSaving,.25,'full-face gain');near(s.currentTargetGap,.25,'face target gap');near(s.globalPower,7/6,'global');}
for(const c of e.triangle){const s=obstructionState(c.x,c.y);for(const[k,expected]of[['oldPowers',c.old],['ordinaryPowers',c.ordinary]])s[k].forEach((v,i)=>near(v,expected[i],k));near(s.currentPower,c.best,'triangle best');near(s.capacityPower,c.capacity,'triangle capacity');assert(s.currentPower>.75);}
for(const[x,y]of[[5/12,1/6],[.75,0]])near(obstructionState(x,y).currentPower,7/6,'exact witness');
for(const[x,y]of[[-.1,0],[0,-.1],[.75,.01],[NaN,0]])assert.throws(()=>obstructionState(x,y),RangeError);
const report={passed:true,faceCases:e.face.length,triangleCases:e.triangle.length,historicalExportFields:'byte-value equal to preserved prior evaluator for every face case',independentMethod:'Fraction exponents and70-digit Decimal monomials; 91-level exact triangular lattice',witnesses:['(5/12,1/6) gives7/6','(3/4,0) gives7/6'],limits:'Upper-bound formula and bookkeeping checks only; does not prove the infinite analytic theorem or energy lower bounds.'};
writeFileSync(new URL('../../../outputs/checks/2026-11-05-arithmetic-learning/ui-pivot/numeric.json',import.meta.url),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
