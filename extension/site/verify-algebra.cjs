'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const a = require('./algebra.js');
function tuples(length, values, visit, prefix = []) {
  if (!length) return visit(prefix);
  for (const value of values) tuples(length - 1, values, visit, prefix.concat(value));
}
let matrices = 0;
tuples(8, [-1, 0, 1], t => {
  const r = a.plucker([t.slice(0, 4), t.slice(4)]);
  assert.equal(r.residual, 0n);
  if (r.rank < 2) assert(Object.values(r.minors).every(x => x === 0n));
  matrices++;
});
assert.deepEqual(a.plucker([[1, 0, 2, -1], [0, 1, 3, 2]]).minors,
  { '12': 1n, '13': 3n, '14': 2n, '23': -2n, '24': 1n, '34': 7n });
assert.equal(a.plucker([[0, 0, 0, 0], [0, 0, 0, 0]]).rank, 0);
assert.equal(a.plucker([[1, 2, -1, 3], [2, 4, -2, 6]]).rank, 1);
const tableaux = a.enumerateTableaux();
assert.equal(tableaux.length, 15); assert.equal(new Set(tableaux.map(t => t.join(','))).size, 15);
const byColumns = [];
for (const [x, y] of [[1, 2], [1, 3], [2, 3]]) for (const [z, w] of [[1, 2], [1, 3], [2, 3]]) for (let v = 1; v <= 3; v++) {
  if (x <= z && z <= v && y <= w) byColumns.push([x, z, v, y, w].join(','));
}
assert.deepEqual(tableaux.map(t => t.join(',')).sort(), byColumns.sort());
assert.equal(a.hookContent().dimension, 15n); assert.equal(a.hookContent().numerator, 360n);
assert.equal(a.hookContent().denominator, 24n);
assert.equal(a.tableauRules([1, 1, 2, 1, 3]).valid, false);
// Independent modular row elimination, including characteristic two.
function rankMod(matrix, columns, prime) {
  const m = matrix.map(row => row.map(x => Number(x % BigInt(prime)))); let rank = 0;
  for (let col = 0; col < columns && rank < m.length; col++) {
    let pivot = rank; while (pivot < m.length && !m[pivot][col]) pivot++;
    if (pivot === m.length) continue;
    [m[pivot], m[rank]] = [m[rank], m[pivot]];
    let inverse = 1; while (m[rank][col] * inverse % prime !== 1) inverse++;
    m[rank] = m[rank].map(x => x * inverse % prime);
    for (let i = 0; i < m.length; i++) if (i !== rank) {
      const factor = m[i][col]; m[i] = m[i].map((x, j) => ((x - factor * m[rank][j]) % prime + prime) % prime);
    }
    rank++;
  }
  return rank;
}
let complexes = 0;
for (let p = 0; p <= 6; p++) for (let q = 0; q <= 6; q++) for (let r = 0; r <= 6; r++) {
  for (const [u, v] of a.allowablePairs(p, q, r)) {
    const c = a.a3(p, q, r, u, v);
    assert(c.VU.flat().every(x => x === 0n));
    for (const prime of [2, 7]) { assert.equal(rankMod(c.U, p, prime), u); assert.equal(rankMod(c.V, q, prime), v); }
    const [m12, m23, s1, s2, s3] = c.multiplicities;
    assert.deepEqual([m12 + s1, m12 + m23 + s2, m23 + s3], [p, q, r]);
    complexes++;
  }
}
assert.deepEqual(a.allowablePairs(1, 1, 1), [[0, 0], [0, 1], [1, 0]]);
assert.equal(a.allowablePairs(1, 2, 1).length, 4);
const normalForms = new Map(); let monomials = 0;
tuples(8, [0, 1, 2], e => {
  const r = a.matchingNormalForm(e);
  assert(r.preserved); assert(r.balance.every(eq => eq.residual === 0n));
  assert(r.normal[2] === 0n || r.normal[3] === 0n); assert(r.normal[4] === 0n || r.normal[5] === 0n);
  assert.deepEqual(a.matchingNormalForm(r.normal).normal, r.normal);
  const key = r.before.join(','), reduced = r.normal.join(',');
  if (normalForms.has(key)) assert.equal(normalForms.get(key), reduced);
  normalForms.set(key, reduced);
  assert.equal(r.degree, e.reduce((sum, x, i) => sum + BigInt(x) * BigInt([2, 2, 4, 4, 3, 3, 4, 2][i]), 0n));
  monomials++;
});
assert.deepEqual(a.matchingVector([0,0,1,1,0,0,0,0]), a.matchingVector([1,1,0,0,0,0,1,0]));
assert.notDeepEqual(a.matchingVector([0,0,1,1,0,0,0,0]), a.matchingVector([1,1,0,0,0,0,0,1]));
assert.deepEqual(a.matchingVector([0,0,0,0,1,1,0,0]), a.matchingVector([0,0,0,0,0,0,1,1]));
assert.throws(() => a.a3(1, 1, 1, 1, 1)); assert.throws(() => a.matchingNormalForm([-1,0,0,0,0,0,0,0]));
assert.throws(() => a.plucker([[0.5,0,0,0],[0,0,0,0]]));
const html = fs.readFileSync(path.join(__dirname, 'algebra.html'), 'utf8');
const script = fs.readFileSync(path.join(__dirname, 'algebra.js'), 'utf8');
const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(match => match[1]);
assert.equal(ids.length, new Set(ids).size, 'Duplicate HTML IDs');
for (const [, id] of script.matchAll(/\$\('([^']+)'\)/g)) assert(ids.includes(id), `Missing DOM ID ${id}`);
console.log(JSON.stringify({ passed: true, plucker_matrices: matrices, tableaux: tableaux.length,
  complexes_over_two_fields: complexes, matching_monomials: monomials,
  distinct_matching_vectors: normalForms.size, dom_ids: ids.length }, null, 2));
