// Run with: node verify-math.cjs
// These finite calculations test the companion models, not the full paper.
const assert = require('node:assert/strict');
const M = require('./math.js');
const key = P => JSON.stringify(P);
const points = M.ecPoints(), keys = new Set(points.map(key));
assert.equal(points.length, 19);
const cyclic = Array.from({length: 19}, (_, k) => M.ecMultiply(k, [5, 1]));
assert.equal(new Set(cyclic.map(key)).size, 19);
assert.equal(M.ecMultiply(19, [5, 1]), null);
for (const P of points) for (const Q of points) {
  assert.ok(keys.has(key(M.ecAdd(P, Q))));
  assert.deepEqual(M.ecAdd(P, Q), M.ecAdd(Q, P));
  for (const R of points) assert.deepEqual(M.ecAdd(M.ecAdd(P, Q), R), M.ecAdd(P, M.ecAdd(Q, R)));
}
let maxConeResidual = 0;
for (let i = 0; i < 61; i++) for (let j = 0; j < 67; j++) {
  const p = M.conePoint(M.TAU * i / 61, M.TAU * j / 67, 1.3);
  const d = M.coneDiagnostics(p);
  maxConeResidual = Math.max(maxConeResidual, Math.abs(d.residual));
  assert.ok(Math.abs(d.residual) < 1e-14);
  assert.ok(Math.abs(d.squaredRadius - 1.69) < 1e-14);
  const rotated = M.rotatePlane(p, 0, 3, 0.37);
  assert.ok(Math.abs(M.norm(rotated) - M.norm(p)) < 1e-14);
}
assert.deepEqual(M.coneDiagnostics(M.conePoint(0, Math.PI)).ranks, [0, 1]);
assert.deepEqual(M.coneDiagnostics(M.conePoint(0, 0)).ranks, [1, 0]);
assert.deepEqual(M.coneDiagnostics(M.conePoint(0, 0, 0)).homology, [1, 2, 1]);
let maxLeak = 0;
for (let d = 0; d < 7; d++) {
  const f = M.fourierDistribution(d);
  assert.ok(Math.abs(f.total - 1) < 1e-14);
  assert.equal(f.cells.filter(c => c.supported).length, 7);
  for (const c of f.cells) assert.ok(Math.abs(c.probability - (c.supported ? 1 / 7 : 0)) < 1e-14);
  maxLeak = Math.max(maxLeak, f.offSupportMax);
}
assert.equal(M.hodge(0).least, 0);
assert.equal(M.hodge(0).smallestPositive, 1);
assert.equal(M.hodge(0).kernelDimension, 1);
assert.ok(Math.abs(M.hodge(0.1).least - 0.01) < 1e-15);
let maxGaugeResidual = 0;
for (const flux of [-3.14, -1.1, 0, 1.2, 3.14]) for (let v = 0; v < 4; v++) for (const lambda of [-3.14, -1.1, 0, 1.1, 3.14]) {
  const g = M.gaugePlaquette(flux, v, lambda);
  maxGaugeResidual = Math.max(maxGaugeResidual, g.residual);
  assert.ok(g.residual < 1e-14);
}
assert.ok(M.torusSeamResidual() < 1e-14);
console.log(JSON.stringify({status: 'passed', scope: 'finite companion models only', curvePoints: points.length,
  ellipticAssociativityTriples: points.length ** 3, maxConeResidual, maxFourierOffSupportProbability: maxLeak,
  maxGaugeResidual, torusSeamResidual: M.torusSeamResidual()}, null, 2));
