/* Mathematical models for the research companion.
 * Exact modular calculations use small integers; geometric/Fourier displays
 * use IEEE-754 doubles. Numerical diagnostics are not formal certificates.
 */
(function (root) {
  'use strict';
  const TAU = 2 * Math.PI;
  const mod = (x, p) => ((x % p) + p) % p;
  const radians = d => d * Math.PI / 180;
  const norm = x => Math.hypot(...x);
  const dot = (x, y) => x.reduce((s, t, i) => s + t * y[i], 0);

  function inverse(a, p) {
    a = mod(a, p);
    if (!a) throw new RangeError('Zero has no multiplicative inverse.');
    let t = 0, newT = 1, r = p, newR = a;
    while (newR) {
      const q = Math.floor(r / newR);
      [t, newT] = [newT, t - q * newT];
      [r, newR] = [newR, r - q * newR];
    }
    if (r !== 1) throw new RangeError('Element is not invertible.');
    return mod(t, p);
  }

  // null is the point at infinity. These formulas are for a short
  // Weierstrass curve in characteristic other than two and three.
  function ecAdd(P, Q, p = 17, a = 2) {
    if (P === null) return Q === null ? null : [...Q];
    if (Q === null) return [...P];
    const [x1, y1] = P, [x2, y2] = Q;
    if (x1 === x2 && mod(y1 + y2, p) === 0) return null;
    const slope = x1 === x2
      ? mod((3 * x1 * x1 + a) * inverse(2 * y1, p), p)
      : mod((y2 - y1) * inverse(x2 - x1, p), p);
    const x3 = mod(slope * slope - x1 - x2, p);
    const y3 = mod(slope * (x1 - x3) - y1, p);
    return [x3, y3];
  }
  function ecMultiply(n, P, p = 17, a = 2) {
    if (!Number.isSafeInteger(n)) throw new TypeError('Scalar must be a safe integer.');
    if (n < 0) return ecMultiply(-n, P === null ? null : [P[0], mod(-P[1], p)], p, a);
    let Q = null, R = P;
    while (n > 0) {
      if (n % 2) Q = ecAdd(Q, R, p, a);
      R = ecAdd(R, R, p, a);
      n = Math.floor(n / 2);
    }
    return Q;
  }
  function ecPoints(p = 17, a = 2, b = 2) {
    const out = [null];
    for (let x = 0; x < p; x++) for (let y = 0; y < p; y++) {
      if (mod(y * y - x * x * x - a * x - b, p) === 0) out.push([x, y]);
    }
    return out;
  }
  const pointText = P => P === null ? '𝒪' : `(${P[0]}, ${P[1]})`;

  function torusPoint(u, v, R = 2, r = 0.7) {
    const radial = R + r * Math.cos(TAU * v);
    return [radial * Math.cos(TAU * u), radial * Math.sin(TAU * u), r * Math.sin(TAU * v)];
  }
  function torusSeamResidual(samples = 64) {
    let maximum = 0;
    for (let j = 0; j <= samples; j++) {
      const t = j / samples;
      const a = torusPoint(0, t), b = torusPoint(1, t);
      const c = torusPoint(t, 0), d = torusPoint(t, 1);
      maximum = Math.max(maximum, norm(a.map((x, i) => x - b[i])), norm(c.map((x, i) => x - d[i])));
    }
    return maximum;
  }
  function conePoint(alpha, beta, radius = 1) {
    // u,v each have length 1/sqrt(2); the second orthogonal change
    // contributes another 1/sqrt(2), hence the factor 1/2 below.
    const ca = Math.cos(alpha), sa = Math.sin(alpha);
    const cb = Math.cos(beta), sb = Math.sin(beta);
    return [radius * (ca + cb) / 2, radius * (sa + sb) / 2,
      radius * (ca - cb) / 2, radius * (sa - sb) / 2];
  }
  function rotatePlane(point, i, j, angle) {
    const out = [...point], c = Math.cos(angle), s = Math.sin(angle);
    out[i] = c * point[i] - s * point[j];
    out[j] = s * point[i] + c * point[j];
    return out;
  }
  function coneProjection(point, xw, yz, kind = 'perspective') {
    const r = rotatePlane(rotatePlane(point, 0, 3, xw), 1, 2, yz);
    // UI radius <=1.5 ensures |r[3]|<=1.5 < viewing distance 3.
    const factor = kind === 'orthographic' ? 1 : 3 / (3 - r[3]);
    return r.slice(0, 3).map(x => x * factor);
  }
  function coneDiagnostics(point, tolerance = 1e-10) {
    const x = point.slice(0, 2), y = point.slice(2, 4);
    const ranks = [norm(x) > tolerance ? 1 : 0, norm(y) > tolerance ? 1 : 0];
    return {x, y, residual: dot(x, y), squaredRadius: dot(point, point), ranks,
      homology: [1 - ranks[0], 2 - ranks[0] - ranks[1], 1 - ranks[1]]};
  }
  function fourierDistribution(d, q = 7) {
    const cells = [], normalization = q * Math.sqrt(q);
    let total = 0, offSupportMax = 0;
    for (let u = 0; u < q; u++) for (let v = 0; v < q; v++) {
      let real = 0, imag = 0;
      for (let t = 0; t < q; t++) {
        const angle = TAU * mod((v - d * u) * t, q) / q;
        real += Math.cos(angle);
        imag += Math.sin(angle);
      }
      real /= normalization; imag /= normalization;
      const probability = real * real + imag * imag;
      const supported = mod(v - d * u, q) === 0;
      cells.push({u, v, real, imag, probability, supported});
      total += probability;
      if (!supported) offSupportMax = Math.max(offSupportMax, probability);
    }
    return {q, d, cells, total, offSupportMax};
  }
  function hodge(epsilon) {
    if (!(epsilon >= 0 && epsilon <= 1)) throw new RangeError('epsilon must lie in [0,1].');
    const eigenvalues = [epsilon * epsilon, 1];
    return {epsilon, eigenvalues, least: eigenvalues[0],
      smallestPositive: epsilon === 0 ? 1 : eigenvalues[0],
      kernelDimension: epsilon === 0 ? 1 : 0,
      homology: epsilon === 0 ? [1, 1, 0] : [0, 0, 0], index: 0};
  }
  function gaugePlaquette(flux, vertex, lambda) {
    const original = [0.4, 0.3, 0.2, 0.1].map(w => flux * w);
    const gauge = [0, 0, 0, 0]; gauge[vertex] = lambda;
    const transformed = original.map((a, i) => a + gauge[i] - gauge[(i + 1) % 4]);
    const complexProduct = phases => phases.reduce(([a, b], p) =>
      [a * Math.cos(p) - b * Math.sin(p), a * Math.sin(p) + b * Math.cos(p)], [1, 0]);
    const W = complexProduct(original), Wprime = complexProduct(transformed);
    return {original, transformed, gauge, W, Wprime,
      residual: Math.hypot(W[0] - Wprime[0], W[1] - Wprime[1]), action: 1 - W[0]};
  }
  const api = Object.freeze({TAU, mod, radians, norm, dot, inverse, ecAdd, ecMultiply, ecPoints, pointText,
    torusPoint, torusSeamResidual, conePoint, rotatePlane, coneProjection, coneDiagnostics,
    fourierDistribution, hodge, gaugePlaquette});
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.ResearchMath = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
