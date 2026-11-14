/* Exact finite cosmology certificates. Conditional probability != empirical rank. */
(function (root) {
  'use strict';
  const Q = typeof module !== 'undefined' && module.exports ? require('./exact-rational.js') : root.ExactRational;
  if (!Q) throw new Error('Exact rational arithmetic must load first.');
  const ZERO = Q.make(0n), ONE = Q.make(1n);
  const PARAMETER_KEYS = ['alpha', 'center', 'order', 'snr', 'threshold', 'width'];
  const cache = new WeakMap();
  const floatView = new DataView(new ArrayBuffer(8));

  function natural(text, minimum, maximum) {
    if (typeof text !== 'string' || !/^(0|[1-9][0-9]*)$/.test(text) || text.length > 6)
      throw new TypeError('Use a canonical natural-number string.');
    const value = Number(text);
    if (value < minimum || value > maximum) throw new RangeError('Natural parameter outside the declared domain.');
    return value;
  }

  function parameters(p) {
    if (!p || typeof p !== 'object' || Array.isArray(p)
        || Object.keys(p).sort().join('|') !== PARAMETER_KEYS.join('|'))
      throw new TypeError('Unexpected cosmology certificate parameters.');
    const center = natural(p.center, 0, 95), width = natural(p.width, 0, 2), order = natural(p.order, 1, 16);
    for (const key of ['alpha', 'snr', 'threshold']) {
      if (typeof p[key] !== 'string' || p[key].length > 162
          || p[key].split('/').some(s => s.replace('-', '').length > 80))
        throw new RangeError('Scalar input exceeds the 80-digit component limit.');
    }
    const alpha = Q.parse(p.alpha), snr = Q.parse(p.snr), threshold = Q.parse(p.threshold);
    if (Q.cmp(alpha, ZERO) <= 0 || Q.cmp(alpha, ONE) > 0) throw new RangeError('The risk budget must be in (0,1].');
    if (Q.cmp(threshold, ZERO) <= 0 || Q.cmp(threshold, Q.make(100n)) > 0) throw new RangeError('The threshold must be in (0,100].');
    if (Q.cmp(snr, ZERO) < 0 || Q.cmp(snr, Q.make(6n)) > 0 || Q.mul(snr, Q.make(10n)).d !== 1n)
      throw new RangeError('SNR must be a multiple of 1/10 between zero and six.');
    return {center, width, order, alpha, snr, threshold};
  }

  // This conversion names the exact stored binary64 constant. It is never
  // used to pretend that a transcendental slider expression is rational.
  function binary64(value) {
    if (typeof value !== 'number' || !Number.isFinite(value)) throw new TypeError('Expected a finite stored binary64 coefficient.');
    floatView.setFloat64(0, value, false);
    const bits = floatView.getBigUint64(0, false), negative = (bits >> 63n) !== 0n;
    const exponent = Number((bits >> 52n) & 2047n);
    let significand = bits & ((1n << 52n) - 1n);
    if (exponent) significand += 1n << 52n;
    const power = (exponent ? exponent - 1023 : -1022) - 52;
    if (negative) significand = -significand;
    return power >= 0 ? Q.make(significand << BigInt(power)) : Q.make(significand, 1n << BigInt(-power));
  }

  function dot(a, b) {
    if (a.length !== b.length) throw new RangeError('Dot-product dimensions differ.');
    let sum = ZERO;
    for (let i = 0; i < a.length; i++) sum = Q.add(sum, Q.mul(a[i], b[i]));
    return sum;
  }

  function dyadicRow(values) {
    const row = values.map(binary64);
    const powers = row.map(q => q.d.toString(2).length - 1);
    const exponent = Math.max(...powers);
    return {integers: row.map((q, i) => q.n << BigInt(exponent - powers[i])), exponent};
  }

  function dyadicDot(a, b) {
    if (a.integers.length !== b.integers.length) throw new RangeError('Dyadic dimensions differ.');
    let numerator = 0n;
    for (let i = 0; i < a.integers.length; i++) numerator += a.integers[i] * b.integers[i];
    return Q.make(numerator, 1n << BigInt(a.exponent + b.exponent));
  }

  function exactCatalog(data) {
    if (cache.has(data)) return cache.get(data);
    if (!data || data.schema !== 'ccc-synthetic-browser-v1' || data.base_sky.length !== 96
        || data.filter_weights.length !== 288 || data.normalized_injection_templates.length !== 288
        || data.calibration_maxima_sorted.length !== 4095) throw new RangeError('Unexpected finite calibration catalog.');
    const weights = data.filter_weights.map(row => {
      if (row.length !== 96) throw new RangeError('Unexpected filter dimension.');
      return dyadicRow(row);
    });
    const base = dyadicRow(data.base_sky);
    const sorted = data.calibration_maxima_sorted.map(binary64);
    if (sorted.some((x, i) => i > 0 && Q.cmp(x, sorted[i - 1]) < 0)) throw new RangeError('Calibration must be sorted.');
    const result = {weights, baseScores: weights.map(row => dyadicDot(row, base)), sorted, responses: new Map()};
    cache.set(data, result);
    return result;
  }

  function exactScan(data, p) {
    const catalog = exactCatalog(data), injectionIndex = p.center * 3 + p.width;
    if (!catalog.responses.has(injectionIndex)) {
      const row = data.normalized_injection_templates[injectionIndex];
      if (row.length !== 96) throw new RangeError('Unexpected injection dimension.');
      const injection = dyadicRow(row);
      if (catalog.responses.size >= 8) catalog.responses.delete(catalog.responses.keys().next().value);
      catalog.responses.set(injectionIndex, catalog.weights.map(w => dyadicDot(w, injection)));
    }
    const response = catalog.responses.get(injectionIndex);
    const scores = catalog.baseScores.map((x, i) => Q.add(x, Q.mul(p.snr, response[i])));
    let winner = 0;
    for (let i = 1; i < scores.length; i++) if (Q.cmp(scores[i], scores[winner]) > 0) winner = i;
    const maximum = scores[winner];
    let low = 0, high = catalog.sorted.length;
    while (low < high) {
      const middle = Math.floor((low + high) / 2);
      if (Q.cmp(catalog.sorted[middle], maximum) < 0) low = middle + 1; else high = middle;
    }
    return {maximum, winner, exceedances: catalog.sorted.length - low, draws: catalog.sorted.length};
  }

  function momentBudget(model, p) {
    if (!model || model.schema !== 'grh-cosmology-moment-model-v1' || model.family_size !== '288'
        || model.dimension !== '96' || model.calibration_draws !== '4095') throw new RangeError('Unexpected moment model.');
    const variance = Q.parse(model.variance_upper_bound);
    if (Q.cmp(variance, ZERO) <= 0) throw new RangeError('The variance envelope must be positive.');
    let coefficient = 1n;
    for (let j = 1; j <= p.order; j++) coefficient *= BigInt(2 * j - 1);
    const moment = Q.mul(Q.make(coefficient), Q.pow(variance, p.order));
    const power = Q.pow(p.threshold, 2 * p.order);
    const rawBound = Q.div(Q.mul(Q.make(288n), moment), power);
    const bound = Q.cmp(rawBound, ONE) < 0 ? rawBound : ONE;
    return {variance, coefficient, moment, power, rawBound, bound};
  }

  function evaluate(data, model, rawParameters) {
    const p = parameters(rawParameters), scan = exactScan(data, p), risk = momentBudget(model, p);
    const rank = Q.make(BigInt(scan.exceedances + 1), BigInt(scan.draws + 1));
    return {
      family_size: '288', variance_upper_bound: Q.format(risk.variance),
      even_exponent: String(2 * p.order), gaussian_moment_coefficient: String(risk.coefficient),
      moment_upper_bound: Q.format(risk.moment), threshold_power: Q.format(risk.power),
      uncapped_family_bound: Q.format(risk.rawBound), family_bound: Q.format(risk.bound),
      within_budget: Q.cmp(risk.bound, p.alpha) <= 0,
      exact_scan_maximum: Q.format(scan.maximum), winner_index: String(scan.winner),
      threshold_crossed: Q.cmp(scan.maximum, p.threshold) >= 0,
      calibration_exceedances: String(scan.exceedances), calibration_draws: String(scan.draws),
      rank_value: Q.format(rank), rank_floor: Q.format(Q.make(1n, BigInt(scan.draws + 1))),
      rank_at_most_alpha: Q.cmp(rank, p.alpha) <= 0,
      probability_scope: 'conditional_even_moment_bound',
      rank_scope: 'exact_finite_rank_no_probability_law_asserted',
      score_scope: 'exact_real_arithmetic_on_stored_binary64_constants'
    };
  }

  const api = Object.freeze({PARAMETER_KEYS, parameters, binary64, dot, exactScan, momentBudget, evaluate});
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.CosmologyCalibration = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
