/* Replayable exact instances of named theorem contracts. This is not a Lean kernel. */
(function (root) {
  'use strict';
  const R = typeof module !== 'undefined' && module.exports ? require('./exact-rational.js') : root.ExactRational;
  const SCHEMA = 'grh-lab-certificate-v1', MAX_TEXT = 524288, INPUT_DIGITS = 80;
  const CONTRACTS = Object.freeze(['hodge-family-v1', 'quadratic-cover-v1', 'weighted-gain-v1', 'cosmology-calibration-v1']);
  const ZERO = R.make(0n), ONE = R.make(1n);
  let cosmologyAdapter = null;

  function object(value, label) {
    if (!value || Array.isArray(value) || typeof value !== 'object' || ![null, Object.prototype].includes(Object.getPrototypeOf(value)))
      throw new TypeError(`${label} must be a plain object.`);
    if (Object.values(Object.getOwnPropertyDescriptors(value)).some(d => !Object.hasOwn(d, 'value')))
      throw new TypeError(`${label} cannot contain accessors.`);
    return value;
  }
  function keys(value, expected, label) {
    object(value, label);
    const actual = Object.keys(value).sort(), wanted = [...expected].sort();
    if (actual.length !== wanted.length || actual.some((k, i) => k !== wanted[i])) throw new TypeError(`${label} has missing or unknown fields.`);
  }
  function stable(value) {
    if (Array.isArray(value)) return `[${value.map(stable).join(',')}]`;
    if (value && typeof value === 'object') return `{${Object.keys(value).sort().map(k => `${JSON.stringify(k)}:${stable(value[k])}`).join(',')}}`;
    return JSON.stringify(value);
  }
  function clone(value) { return JSON.parse(stable(value)); }
  function deepFreeze(value) {
    if (value && typeof value === 'object') { Object.values(value).forEach(deepFreeze); Object.freeze(value); }
    return value;
  }
  // JSON.parse alone silently accepts duplicate keys. This bounded parser does not.
  // No JSON numeric literals occur in this protocol: exact numbers are n/d strings.
  function parseJSON(text) {
    if (typeof text !== 'string' || text.length > MAX_TEXT || new TextEncoder().encode(text).length > MAX_TEXT) throw new RangeError('Certificate text exceeds the 512 KiB limit.');
    let p = 0, nodes = 0;
    const space = () => { while (/\s/.test(text[p] || '') && p < text.length) { if (!' \t\r\n'.includes(text[p])) throw new SyntaxError('Invalid JSON whitespace.'); p++; } };
    function string() {
      const start = p++;
      while (p < text.length) {
        const c = text[p++];
        if (c === '"') return JSON.parse(text.slice(start, p));
        if (c === '\\') p++;
      }
      throw new SyntaxError('Unterminated JSON string.');
    }
    function value(depth) {
      if (depth > 24 || ++nodes > 12000) throw new RangeError('Certificate JSON exceeds the nesting or node limit.');
      space(); const c = text[p];
      if (c === '"') return string();
      if (c === '{') {
        p++; const out = Object.create(null), seen = new Set(); space();
        if (text[p] === '}') { p++; return out; }
        for (;;) {
          space(); if (text[p] !== '"') throw new SyntaxError('Object keys must be strings.');
          const key = string();
          if (seen.has(key)) throw new SyntaxError(`Duplicate JSON key: ${key}`);
          seen.add(key); space(); if (text[p++] !== ':') throw new SyntaxError('Expected a colon.');
          out[key] = value(depth + 1); space(); const delimiter = text[p++];
          if (delimiter === '}') return out;
          if (delimiter !== ',') throw new SyntaxError('Expected a comma or closing brace.');
        }
      }
      if (c === '[') {
        p++; const out = []; space(); if (text[p] === ']') { p++; return out; }
        for (;;) { out.push(value(depth + 1)); space(); const delimiter = text[p++]; if (delimiter === ']') return out; if (delimiter !== ',') throw new SyntaxError('Expected a comma or closing bracket.'); }
      }
      for (const [token, v] of [['true', true], ['false', false], ['null', null]]) if (text.slice(p, p + token.length) === token) { p += token.length; return v; }
      if (c === '-' || /[0-9]/.test(c || '')) throw new TypeError('JSON numbers are forbidden; use canonical rational strings.');
      throw new SyntaxError('Invalid JSON value.');
    }
    const out = value(0); space(); if (p !== text.length) throw new SyntaxError('Trailing JSON data.'); return out;
  }
  function scalar(text, label) {
    const r = R.parse(text);
    if (text.split('/').some(s => s.replace('-', '').length > INPUT_DIGITS)) throw new RangeError(`${label} exceeds the 80-digit parameter limit.`);
    return r;
  }
  function interval(text, low, high, label) {
    const r = scalar(text, label);
    if (R.cmp(r, low) < 0 || R.cmp(r, high) > 0) throw new RangeError(`${label} is outside its domain.`);
    return r;
  }
  function integer(text, min, max, label) {
    const r = interval(text, R.make(BigInt(min)), R.make(BigInt(max)), label);
    if (r.d !== 1n) throw new TypeError(`${label} must be an integer rational.`);
    return Number(r.n);
  }
  function vector(raw, length, label) {
    if (!Array.isArray(raw) || raw.length !== length) throw new TypeError(`${label} must have ${length} entries.`);
    return raw.map((x, i) => scalar(x, `${label}[${i}]`));
  }
  function registryBinding(registry, contract) {
    if (!CONTRACTS.includes(contract)) throw new TypeError('Unknown theorem contract.');
    object(registry, 'Trusted contract registry');
    if (registry.schema !== 'grh-lab-contract-registry-v1' || registry.status !== 'verified') throw new TypeError('A verified local contract registry is required.');
    const b = registry.contracts && registry.contracts[contract];
    object(b, 'Trusted contract binding');
    return b;
  }
  function hodge(parameters) {
    keys(parameters, ['epsilon'], 'Hodge parameters');
    const e = interval(parameters.epsilon, ZERO, ONE, 'epsilon'), square = R.mul(e, e), zero = !e.n;
    return {diagonal: [R.format(square), '1/1'], least_eigenvalue: R.format(square), smallest_positive_eigenvalue: zero ? '1/1' : R.format(square), kernel_dimension: zero ? '1/1' : '0/1', euler_index: '0/1', positive_gap: !zero, coercivity_constant: R.format(square)};
  }
  function cover(parameters) {
    keys(parameters, ['power', 'x', 'y'], 'Cover parameters');
    const k = integer(parameters.power, 0, 3, 'power');
    const point = ['x', 'y'].map(key => {
      const r = interval(parameters[key], ZERO, ONE, key);
      if (R.mul(r, R.make(100n)).d !== 1n) throw new RangeError('The live cover controls use the exact hundredth grid.');
      return r;
    });
    let m = [[1n, 0n], [0n, 1n]];
    for (let i = 0; i < k; i++) m = m.map(row => [3n * row[0] + row[1], row[0] + 5n * row[1]]);
    const determinant = m[0][0] * m[1][1] - m[0][1] * m[1][0];
    const raw = m.map(row => R.add(R.mul(R.make(row[0]), point[0]), R.mul(R.make(row[1]), point[1])));
    return {matrix: m.map(row => row.map(v => R.format(R.make(v)))), determinant: R.format(R.make(determinant)), degree_nonzero: determinant !== 0n, target_mod_one: raw.map(v => R.format(R.sub(v, R.make(R.floor(v))))), lifted_frequency: m[0].map(v => R.format(R.make(v))), integer_degree_identity: determinant === 14n ** BigInt(k)};
  }
  function weighted(parameters) {
    keys(parameters, ['matrix', 'weights', 'rate'], 'Weighted-gain parameters');
    if (!Array.isArray(parameters.matrix) || parameters.matrix.length !== 2) throw new TypeError('The live gain lab uses a 2 by 2 matrix.');
    const G = parameters.matrix.map((row, i) => vector(row, 2, `matrix[${i}]`)), w = vector(parameters.weights, 2, 'weights'), q = scalar(parameters.rate, 'rate');
    if (G.flat().some(r => r.n < 0n) || q.n < 0n || w.some(r => r.n <= 0n)) throw new RangeError('G and q must be nonnegative; weights must be strictly positive.');
    const lhs = G.map(row => R.add(R.mul(row[0], w[0]), R.mul(row[1], w[1]))), rhs = w.map(v => R.mul(q, v));
    const ratios = lhs.map((v, i) => R.div(v, w[i])), max = R.cmp(ratios[0], ratios[1]) > 0 ? ratios[0] : ratios[1];
    const holding = lhs.every((v, i) => R.cmp(v, rhs[i]) <= 0);
    return {left_sides: lhs.map(R.format), right_sides: rhs.map(R.format), slacks: rhs.map((v, i) => R.format(R.sub(v, lhs[i]))), row_ratios: ratios.map(R.format), maximum_ratio: R.format(max), bound_holds: holding, certifies_contraction_of_supplied_gain: holding && R.cmp(q, ONE) < 0};
  }
  function evaluate(contract, parameters) {
    if (contract === 'hodge-family-v1') return hodge(parameters);
    if (contract === 'quadratic-cover-v1') return cover(parameters);
    if (contract === 'weighted-gain-v1') return weighted(parameters);
    if (contract === 'cosmology-calibration-v1' && cosmologyAdapter) return cosmologyAdapter(parameters);
    throw new TypeError('This contract has no available exact evaluator.');
  }
  function create(contract, parameters, registry) {
    const binding = registryBinding(registry, contract), result = evaluate(contract, parameters);
    return deepFreeze({schema: SCHEMA, contract, binding: clone(binding), parameters: clone(parameters), result});
  }
  function validate(input, registry, expectedContract = null) {
    const c = typeof input === 'string' ? parseJSON(input) : input;
    keys(c, ['schema', 'contract', 'binding', 'parameters', 'result'], 'Certificate');
    if (c.schema !== SCHEMA) throw new TypeError('Unsupported certificate schema.');
    if (expectedContract !== null && c.contract !== expectedContract) throw new TypeError('This certificate belongs to a different laboratory.');
    const expected = create(c.contract, c.parameters, registry);
    if (stable(c.binding) !== stable(expected.binding)) throw new TypeError('Stale or altered theorem/source binding. Use this release’s registry.');
    if (stable(c.result) !== stable(expected.result)) throw new TypeError('Derived certificate results do not match exact replay.');
    return expected;
  }
  function userRational(text) {
    if (typeof text !== 'string') throw new TypeError('Exact input must be text.');
    text = text.trim();
    let r;
    if (/^-?[0-9]+\/[0-9]+$/.test(text) && text.length <= 164) { const [n, d] = text.split('/'); r = R.make(BigInt(n), BigInt(d)); }
    else r = R.fromDecimal(text);
    return R.format(scalar(R.format(r), 'input'));
  }
  function leanSource(input, registry) {
    const c = validate(input, registry), p = c.parameters;
    const q = (v, field = 'ℚ') => {
      // Inputs have already been domain-checked; derived moment fractions may
      // legitimately be longer than the input parser's 256-digit boundary.
      if (typeof v !== 'string' || v.length > 8194 || !/^(0|-[1-9][0-9]*|[1-9][0-9]*)\/[1-9][0-9]*$/.test(v)) throw new TypeError('Invalid bounded rational Lean literal.');
      const [n, d] = v.split('/'), r = R.make(BigInt(n), BigInt(d));
      if (R.format(r) !== v) throw new TypeError('Noncanonical Lean literal.');
      return `((${r.n} : ${field}) / ${r.d})`;
    };
    const header = `-- Generated from validated ${SCHEMA}; no imported Lean code is executed.\n-- Contract: ${c.contract}\n-- Check with the pinned project: cd extension/lean && lake env lean -DwarningAsError=true LaboratoryInstance.lean\nimport BridgeTheorems\nimport FluidInterfaces\nimport WeightedGainContracts\nimport LaboratoryContracts\n${c.contract === 'cosmology-calibration-v1' ? 'import CosmologyCalibration\n' : ''}import Mathlib.Tactic.NormNum\nimport Mathlib.Tactic.FinCases\n\nopen Matrix\nopen scoped BigOperators\nnamespace LaboratoryInstance\n\n`;
    let body;
    if (c.contract === 'hodge-family-v1') {
      const e = q(p.epsilon, 'ℝ');
      body = `example : ResearchBridge.hodgeMatrix ${e} 0 0 1 = !![${e} ^ 2, 0; 0, 1] ∧\n    (∀ a b : ℝ, ${e} ^ 2 * (a ^ 2 + b ^ 2) ≤ ResearchBridge.hodgeEnergy ${e} 0 0 1 a b) ∧\n    (0 < ${e} ^ 2 ↔ ${e} ≠ 0) :=\n  LaboratoryContracts.hodge_family_certificate ${e} (by norm_num) (by norm_num)\n\nexample (a b : ℝ) : (ResearchBridge.hodgeMatrix ${e} 0 0 1 *ᵥ ![a, b] = 0) ↔\n    ((${e} = 0 ∨ a = 0) ∧ b = 0) :=\n  LaboratoryContracts.hodge_family_kernel ${e} a b\n\nexample : ${e} ^ 2 ${c.result.positive_gap ? '> 0' : '= 0'} := by norm_num\n\nexample : ${e} ^ 2 = ${q(c.result.least_eigenvalue, 'ℝ')} := by norm_num\n`;
    } else if (c.contract === 'quadratic-cover-v1') {
      const k = R.parse(p.power).n;
      body = `example : Matrix.det (FluidInterfaces.renormalizationMatrix ^ ${k}) = (14 : ℤ) ^ ${k} ∧\n    0 < Matrix.det (FluidInterfaces.renormalizationMatrix ^ ${k}) :=\n  LaboratoryContracts.quadratic_cover_certificate ${k}\n\nexample : Matrix.det (FluidInterfaces.renormalizationMatrix ^ ${k}) = ${R.parse(c.result.determinant).n} := by\n  rw [FluidInterfaces.renormalization_power_determinant]\n  norm_num\n`;
    } else if (c.contract === 'weighted-gain-v1') {
      const m = p.matrix.map(row => row.map(v => q(v))), w = p.weights.map(v => q(v));
      body = `def G : Matrix (Fin 2) (Fin 2) ℚ := !![${m[0][0]}, ${m[0][1]}; ${m[1][0]}, ${m[1][1]}]\ndef w : Fin 2 → ℚ := ![${w[0]}, ${w[1]}]\ndef q : ℚ := ${q(p.rate)}\n\ntheorem positive_weights : ∀ i, 0 < w i := by\n  intro i\n  fin_cases i <;> norm_num [w]\n\nexample : (∀ i, (G *ᵥ w) i / w i ≤ q) ↔ (∀ i, (G *ᵥ w) i ≤ q * w i) :=\n  WeightedGainContracts.row_ratio_iff G w q positive_weights\n\n`;
      if (c.result.bound_holds) body += `example : ∀ i, (G *ᵥ w) i ≤ q * w i := by\n  intro i\n  fin_cases i <;> norm_num [G, w, q, Matrix.mulVec, dotProduct, Fin.sum_univ_two]\n`;
      else {
        const i = c.result.slacks.findIndex(v => v.startsWith('-'));
        body += `-- This proposed bound fails; the exact violated row is certified instead.\nexample : q * w ${i} < (G *ᵥ w) ${i} := by\n  norm_num [G, w, q, Matrix.mulVec, dotProduct, Fin.sum_univ_two]\n`;
      }
    } else if (c.contract === 'cosmology-calibration-v1') {
      const natural = text => { if (typeof text !== 'string' || !/^(0|[1-9][0-9]*)$/.test(text) || text.length > 5) throw new TypeError('Invalid natural literal for Lean template.'); return text; };
      const k = natural(p.order), count = natural(c.result.calibration_exceedances), draws = natural(c.result.calibration_draws);
      const threshold = q(p.threshold, 'ℝ'), moment = q(c.result.moment_upper_bound, 'ℝ'), alpha = q(p.alpha, 'ℝ');
      const [rawN, rawD] = c.result.uncapped_family_bound.split('/');
      const scalarBudgetHolds = R.cmp(R.make(BigInt(rawN), BigInt(rawD)), R.parse(p.alpha)) <= 0;
      const conclusion = scalarBudgetHolds ? alpha : q(c.result.family_bound, 'ℝ');
      body = `open MeasureTheory\n\n-- Conditional on actual measurable scores, integrability and the stated true\n-- moment bound. No PRNG law, Gaussian moment identity or observational model\n-- is proved by these numerical literals. Choose the threshold before testing.\nexample {Ω : Type*} [MeasurableSpace Ω]\n    (μ : Measure Ω) [IsProbabilityMeasure μ] (score : Fin 288 → Ω → ℝ)\n    (hmeas : ∀ j, Measurable (score j))\n    (hint : ∀ j, Integrable (fun ω => |score j ω| ^ (2 * ${k})) μ)\n    (hmoment : ∀ j, (∫ ω, |score j ω| ^ (2 * ${k}) ∂μ) ≤ ${moment}) :\n    μ.real (CosmologyCalibration.scanEvent (Finset.univ : Finset (Fin 288)) score ${threshold}) ≤ ${conclusion} := by\n`;
      if (scalarBudgetHolds) body += `  have h := CosmologyCalibration.scan_even_moment_threshold μ\n    (Finset.univ : Finset (Fin 288)) score ${k} ${threshold} ${moment} ${alpha}\n    (by norm_num) (by intro j _; exact hmeas j)\n    (by intro j _; exact hint j) (by intro j _; exact hmoment j) (by norm_num)\n  exact h.2\n`;
      else body += `  have h := CosmologyCalibration.scan_uniform_even_moment_bound μ\n    (Finset.univ : Finset (Fin 288)) score ${k} ${threshold} ${moment}\n    (by norm_num) (by intro j _; exact hmeas j)\n    (by intro j _; exact hint j) (by intro j _; exact hmoment j)\n  have heval : min (1 : ℝ) (((Finset.univ : Finset (Fin 288)).card : ℝ) * ${moment} / ${threshold} ^ (2 * ${k})) = ${conclusion} := by norm_num\n  simpa only [heval] using h.2\n`;
      body += `\n-- Exact rank arithmetic only; no probability law for the stored rank is asserted.\nexample : CosmologyCalibration.rankFraction ${draws} ${count} = ${q(c.result.rank_value)} := by\n  norm_num [CosmologyCalibration.rankFraction]\n\nexample : 0 < CosmologyCalibration.rankFraction ${draws} ${count} ∧\n    1 / ((${draws} : ℚ) + 1) ≤ CosmologyCalibration.rankFraction ${draws} ${count} ∧\n    CosmologyCalibration.rankFraction ${draws} ${count} ≤ 1 :=\n  CosmologyCalibration.rank_fraction_bounds ${draws} ${count} (by norm_num)\n`;
    } else throw new TypeError('No Lean instantiation template is registered for this contract yet.');
    return header + body + '\nend LaboratoryInstance\n';
  }
  function setCosmologyAdapter(adapter) { if (typeof adapter !== 'function') throw new TypeError('An exact evaluator function is required.'); cosmologyAdapter = adapter; }
  const api = Object.freeze({SCHEMA, CONTRACTS, MAX_TEXT, R, parseJSON, stable, create, validate, evaluate, userRational, leanSource, setCosmologyAdapter});
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.LabCertificateBridge = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
