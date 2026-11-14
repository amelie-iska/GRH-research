/* Focused protocol, exact arithmetic, hostile-input and transaction tests. */
'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {execFileSync} = require('node:child_process');
const B = require('./certificate-bridge.js'), R = require('./exact-rational.js'), UI = require('./certificate-bridge-ui.js');
const C = require('./cosmology-calibration-core.js');
const registry = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/certificate-contracts.json'), 'utf8'));
const data = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/cosmology-synthetic.json'), 'utf8'));
const model = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/cosmology-moment-model.json'), 'utf8'));
B.setCosmologyAdapter(p => C.evaluate(data, model, p));
const copy = x => JSON.parse(JSON.stringify(x));
const gain = rate => ({matrix: [['1/4', '3/2'], ['3/32', '1/4']], weights: ['4/1', '1/1'], rate});
const cosmology = (threshold = '6/1', alpha = '1/20') => ({alpha, center: '0', order: '8', snr: '0/1', threshold, width: '1'});
const certificate = (contract, params) => B.create(contract, params, registry);

test('canonical rational parser rejects coercion, noncanonical strings and resource overflow', () => {
  for (const value of [0, 0.5, true, false, null, NaN, Infinity, 1n, {}, 'NaN', 'Infinity', '1', '01/2', '-0/1', '0/2', '2/4', '1/-2', '1/0', '+1/2', '1.0/2', ' 1/2', '1/' + '9'.repeat(257)]) assert.throws(() => R.parse(value));
  assert.equal(R.format(R.parse('-7/13')), '-7/13');
  assert.throws(() => R.make(1, 2));
});
test('exact decimal text and sign normalization do not pass through Number', () => {
  assert.equal(R.format(R.fromDecimal('0.080')), '2/25');
  assert.equal(R.format(R.fromDecimal('-0.125')), '-1/8');
  assert.equal(R.format(R.fromDecimal('123456789012345678901.2')), '617283945061728394506/5');
  assert.equal(B.userRational(' 2/6 '), '1/3');
  assert.equal(R.format(R.fromDecimal('5e-324'.replace('324', '256'))), '1/' + (2n * 10n ** 255n));
  assert.throws(() => R.fromDecimal('1e999999'));
});
test('display-only rational conversion avoids Infinity/Infinity and premature underflow', () => {
  assert.equal(R.toNumber(R.make(10n ** 500n + 1n, 10n ** 500n)), 1);
  assert.equal(R.toNumber(R.make(10n ** 400n, 10n ** 399n)), 10);
  assert.equal(R.toNumber(R.make(10n ** 500n)), Infinity);
  assert.equal(R.toNumber(R.make(1n, 10n ** 500n)), 0);
  assert.equal(R.toNumber(R.make(5n, 10n ** 324n)), Number.MIN_VALUE);
  assert.equal(R.toNumber(R.make(-5n, 10n ** 324n)), -Number.MIN_VALUE);
});
test('strict JSON rejects duplicate/escaped duplicate keys, numbers, invalid syntax and oversized UTF8', () => {
  for (const text of ['{"x":"1/1","x":"2/1"}', '{"x":"1/1","\\u0078":"2/1"}', '{"x":0}', '{"x":0.0}', '{"x":1e2}', '{"x":NaN}', '{"x":Infinity}', '{"x":"a",}', 'true false', '"bad\nstring"', '['.repeat(30) + 'true' + ']'.repeat(30), '"' + 'λ'.repeat(270000) + '"']) assert.throws(() => B.parseJSON(text));
  assert.equal(B.parseJSON('{"x":"\\u03bb"}').x, 'λ');
});
test('Hodge positive and zero boundaries preserve the two different gap quantities', () => {
  const zero = certificate('hodge-family-v1', {epsilon: '0/1'}), third = certificate('hodge-family-v1', {epsilon: '1/3'});
  assert.equal(zero.result.least_eigenvalue, '0/1'); assert.equal(zero.result.smallest_positive_eigenvalue, '1/1'); assert.equal(zero.result.kernel_dimension, '1/1'); assert.equal(zero.result.positive_gap, false);
  assert.deepEqual(third.result.diagonal, ['1/9', '1/1']); assert.equal(third.result.positive_gap, true);
  for (const epsilon of ['-1/3', '4/3', '2/6', true, 0.1, '1/' + '9'.repeat(81)]) assert.throws(() => certificate('hodge-family-v1', {epsilon}));
});
test('toral powers and exact point map agree with independent integer oracles', () => {
  const determinants = ['1/1', '14/1', '196/1', '2744/1'];
  for (let k = 0; k < 4; k++) assert.equal(certificate('quadratic-cover-v1', {power: `${k}/1`, x: '7/25', y: '63/100'}).result.determinant, determinants[k]);
  const one = certificate('quadratic-cover-v1', {power: '1/1', x: '7/25', y: '63/100'});
  assert.deepEqual(one.result.target_mod_one, ['47/100', '43/100']);
  const three = certificate('quadratic-cover-v1', {power: '3/1', x: '7/25', y: '63/100'});
  assert.deepEqual(three.result.matrix, [['38/1', '50/1'], ['50/1', '138/1']]); assert.deepEqual(three.result.target_mod_one, ['7/50', '47/50']);
  for (const p of [{power: '4/1', x: '0/1', y: '0/1'}, {power: '1/1', x: '1/3', y: '0/1'}, {power: '1/2', x: '0/1', y: '0/1'}]) assert.throws(() => certificate('quadratic-cover-v1', p));
});
test('weighted replay distinguishes a holding contraction, failed bound and noncontracting bound', () => {
  const accepted = certificate('weighted-gain-v1', gain('5/8'));
  assert.deepEqual(accepted.result.slacks, ['0/1', '0/1']); assert.equal(accepted.result.maximum_ratio, '5/8'); assert.equal(accepted.result.certifies_contraction_of_supplied_gain, true);
  const failed = certificate('weighted-gain-v1', gain('3/5')); assert.equal(failed.result.bound_holds, false); assert.deepEqual(failed.result.slacks, ['-1/10', '-1/40']);
  const noncontracting = certificate('weighted-gain-v1', gain('2/1')); assert.equal(noncontracting.result.bound_holds, true); assert.equal(noncontracting.result.certifies_contraction_of_supplied_gain, false);
  const invalid = gain('5/8'); invalid.weights[1] = '0/1'; assert.throws(() => certificate('weighted-gain-v1', invalid));
});
test('80-digit parameter domain remains exact for weights far beyond binary64 precision', () => {
  const n = 10n ** 79n + 7n, w = R.format(R.make(n));
  const c = certificate('weighted-gain-v1', {matrix: [['1/2', '0/1'], ['0/1', '1/2']], weights: [w, w], rate: '1/2'});
  assert.deepEqual(c.result.slacks, ['0/1', '0/1']); assert.equal(c.result.maximum_ratio, '1/2');
});
test('tampered derived results, unknown fields, wrong lab and stale bindings fail closed', () => {
  const original = certificate('hodge-family-v1', {epsilon: '1/3'});
  const mutations = [c => {c.result.least_eigenvalue = '1/8';}, c => {c.result.positive_gap = false;}, c => {c.parameters.extra = '1/1';}, c => {delete c.result.diagonal;}, c => {c.schema = 'v2';}, c => {c.binding.theorems[0].source_sha256 = '0'.repeat(64);}, c => {c.binding.theorems[0].printed_type += ' altered';}, c => {c.binding.runtime_sources['extension/site/exact-rational.js'] = 'f'.repeat(64);}, c => {c.code = 'unsafe';}];
  for (const mutate of mutations) {const c = copy(original); mutate(c); assert.throws(() => B.validate(JSON.stringify(c), registry));}
  assert.throws(() => B.validate(JSON.stringify(original), registry, 'weighted-gain-v1'));
  assert.equal(B.validate(JSON.stringify(original), registry).parameters.epsilon, '1/3');
});
test('validated round-trip restores exact parameters and invalid import never prepares or mutates controls', () => {
  let state = {epsilon: '2/3'}, prepared = 0, committed = 0;
  const adapter = {readParameters: () => copy(state), prepareImport: p => {prepared++; const before = copy(state); return {commit: () => {committed++; state = copy(p);}, rollback: () => {state = before;}};}};
  const original = certificate('hodge-family-v1', {epsilon: '1/3'});
  UI.transactionalApply(JSON.stringify(original), registry, original.contract, adapter); assert.deepEqual(state, {epsilon: '1/3'}); assert.equal(committed, 1);
  const bad = copy(original); bad.result.positive_gap = false;
  assert.throws(() => UI.transactionalApply(JSON.stringify(bad), registry, original.contract, adapter)); assert.equal(prepared, 1); assert.equal(committed, 1); assert.deepEqual(state, {epsilon: '1/3'});
});
test('a control that cannot restore exact state rolls back without accepting a rounded import', () => {
  let state = {epsilon: '2/3'}, rolledBack = false;
  const adapter = {readParameters: () => state, prepareImport: () => {const before = state; return {commit: () => {state = {epsilon: '33/100'};}, rollback: () => {state = before; rolledBack = true;}};}};
  assert.throws(() => UI.transactionalApply(JSON.stringify(certificate('hodge-family-v1', {epsilon: '1/3'})), registry, 'hodge-family-v1', adapter));
  assert.equal(rolledBack, true); assert.equal(state.epsilon, '2/3');
});
test('cosmology certificate retains conditional moment scope and exact finite rank arithmetic', () => {
  const positive = certificate('cosmology-calibration-v1', cosmology()), failed = certificate('cosmology-calibration-v1', cosmology('2/1'));
  assert.equal(positive.result.within_budget, true); assert.equal(failed.result.within_budget, false); assert.equal(positive.result.rank_floor, '1/4096');
  assert.equal(positive.result.probability_scope, 'conditional_even_moment_bound'); assert.equal(positive.result.rank_scope, 'exact_finite_rank_no_probability_law_asserted');
  const tampered = copy(positive); tampered.result.calibration_exceedances = '0'; assert.throws(() => B.validate(tampered, registry));
});
test('Lean return path contains fixed theorem applications and rejects source injection', () => {
  for (const c of [certificate('hodge-family-v1', {epsilon: '1/3'}), certificate('quadratic-cover-v1', {power: '3/1', x: '1/2', y: '1/4'}), certificate('weighted-gain-v1', gain('5/8')), certificate('weighted-gain-v1', gain('3/5')), certificate('cosmology-calibration-v1', cosmology()), certificate('cosmology-calibration-v1', cosmology('2/1', '1/1'))]) {
    const text = B.leanSource(c, registry); assert.doesNotMatch(text, /\b(sorry|admit|native_decide)\b/); assert.match(text, /namespace LaboratoryInstance/);
  }
  const uncappedFails = B.leanSource(certificate('cosmology-calibration-v1', cosmology('2/1', '1/1')), registry);
  assert.match(uncappedFails, /scan_uniform_even_moment_bound/); assert.doesNotMatch(uncappedFails, /scan_even_moment_threshold/); assert.match(uncappedFails, /hmeas/); assert.match(uncappedFails, /hmoment/);
  assert.throws(() => certificate('hodge-family-v1', {epsilon: '1/1\naxiom bad : False'}));
});
test('independent Python replay agrees on 128 rational gain instances and edge contracts', () => {
  const cases = [certificate('hodge-family-v1', {epsilon: '0/1'}), certificate('hodge-family-v1', {epsilon: '37/101'}), certificate('quadratic-cover-v1', {power: '3/1', x: '99/100', y: '1/100'}), certificate('cosmology-calibration-v1', cosmology())];
  for (let i = 0; i < 128; i++) {
    const r = (n, d) => R.format(R.make(BigInt(n), BigInt(d)));
    cases.push(certificate('weighted-gain-v1', {matrix: [[r(i % 7, 11), r((i * 5) % 13, 17)], [r((i * 3) % 11, 19), r(i % 5, 7)]], weights: [r(i + 1, 13), r(i + 3, 11)], rate: r(i % 17, 9)}));
  }
  const script = 'import sys,json;sys.path.insert(0,sys.argv[1]);from verify_lab_certificate import replay;v=json.load(sys.stdin);out=[replay(c,v["registry"]) for c in v["certificates"]];print(json.dumps({"checked":len(out),"all_valid":all(x["status"]=="valid-instance" for x in out)}))';
  const result = JSON.parse(execFileSync('python3', ['-c', script, path.resolve(__dirname, '../code')], {input: JSON.stringify({registry, certificates: cases}), encoding: 'utf8', maxBuffer: 1024 * 1024}));
  assert.equal(result.checked, 132); assert.equal(result.all_valid, true);
});
