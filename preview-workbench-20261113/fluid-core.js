/* Finite numerical kernels for the fluid companion. No external libraries. */
(function (root, factory) {
  "use strict";
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.FluidMath = api;
}(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";
  const TAU = 2 * Math.PI;
  const GRID = 16;
  const STEP_TIME = 0.1;
  const NU_MIN = 0.02;
  const NU_MAX = 0.30;
  const DEFAULT_ANGLES = [0.72, -0.45, 1.1, 0.38];
  const mod1 = x => x - Math.floor(x);
  const clamp = (x, a, b) => Math.max(a, Math.min(b, x));

  function taylorGreen(x, y, time, nu) {
    if (![x, y, time, nu].every(Number.isFinite) || time < 0 || nu < 0) throw new RangeError("Finite coordinates, nonnegative time and viscosity required.");
    const a = Math.exp(-2 * nu * time);
    return {u: Math.sin(x) * Math.cos(y) * a, v: -Math.cos(x) * Math.sin(y) * a,
      pressure: (Math.cos(2 * x) + Math.cos(2 * y)) * a * a / 4,
      vorticity: 2 * Math.sin(x) * Math.sin(y) * a,
      energyAverage: a * a / 4, amplitude: a, energyDerivative: -nu * a * a};
  }

  function matrixMultiply(a, b) {
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
      [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]];
  }
  function renormalizationPower(k) {
    if (!Number.isInteger(k) || k < 0 || k > 10) throw new RangeError("Use an integer power from 0 to 10.");
    let m = [[1, 0], [0, 1]];
    for (let j = 0; j < k; j++) m = matrixMultiply(m, [[3, 1], [1, 5]]);
    return {matrix: m, determinant: 14 ** k};
  }
  function gcd(a, b) { while (b) { const r = a % b; a = b; b = r; } return Math.abs(a); }
  function toralFibres(k, point, frequency = [1, 0]) {
    if (!Number.isInteger(k) || k < 0 || k > 3) throw new RangeError("The complete fibre view uses powers 0–3.");
    const {matrix: m, determinant: det} = renormalizationPower(k);
    const x = point.map(mod1);
    const raw = [m[0][0] * x[0] + m[0][1] * x[1], m[1][0] * x[0] + m[1][1] * x[1]];
    const target = raw.map(mod1);
    // The column-Hermite diagonal is (det/g, g), g=gcd(bottom row).
    // The integer rectangle is a complete set of quotient representatives.
    const g = gcd(m[1][0], m[1][1]), width = det / g;
    const points = [];
    for (let j = 0; j < g; j++) for (let i = 0; i < width; i++) {
      const v = [target[0] + i, target[1] + j];
      points.push([mod1((m[1][1] * v[0] - m[0][1] * v[1]) / det),
        mod1((-m[1][0] * v[0] + m[0][0] * v[1]) / det)]);
    }
    const lifted = [m[0][0] * frequency[0] + m[1][0] * frequency[1],
      m[0][1] * frequency[0] + m[1][1] * frequency[1]];
    const a = TAU * (frequency[0] * target[0] + frequency[1] * target[1]);
    const b = TAU * (lifted[0] * x[0] + lifted[1] * x[1]);
    const characterImage = [Math.cos(a), Math.sin(a)], characterPullback = [Math.cos(b), Math.sin(b)];
    return {matrix: m, determinant: det, point: x, target, points, frequency, lifted,
      characterImage, characterPullback, characterError: Math.hypot(characterImage[0] - characterPullback[0], characterImage[1] - characterPullback[1])};
  }

  function ry(re, im, qubit, angle) {
    const mask = 1 << (1 - qubit), c = Math.cos(angle / 2), s = Math.sin(angle / 2);
    for (let j = 0; j < 4; j++) if (!(j & mask)) {
      const k = j | mask, ar = re[j], ai = im[j], br = re[k], bi = im[k];
      re[j] = c * ar - s * br; im[j] = c * ai - s * bi;
      re[k] = s * ar + c * br; im[k] = s * ai + c * bi;
    }
  }
  function rz(re, im, qubit, angle) {
    const mask = 1 << (1 - qubit);
    for (let j = 0; j < 4; j++) {
      const phase = (j & mask ? 1 : -1) * angle / 2, c = Math.cos(phase), s = Math.sin(phase), a = re[j], b = im[j];
      re[j] = c * a - s * b; im[j] = s * a + c * b;
    }
  }
  function circuit(angles) {
    if (angles.length !== 4 || !angles.every(Number.isFinite)) throw new RangeError("Four finite rotation angles required.");
    const re = new Float64Array([1, 0, 0, 0]), im = new Float64Array(4);
    ry(re, im, 0, angles[0]); rz(re, im, 0, angles[1]);
    ry(re, im, 1, angles[2]); rz(re, im, 1, angles[3]);
    [re[2], re[3]] = [re[3], re[2]]; [im[2], im[3]] = [im[3], im[2]];
    ry(re, im, 0, 0.4); ry(re, im, 1, -0.3);
    const probabilities = Array.from(re, (a, j) => a * a + im[j] * im[j]);
    const features = [0, 0, 0];
    for (let j = 0; j < 4; j++) {
      features[0] += (j & 2 ? -1 : 1) * probabilities[j];
      features[1] += (j & 1 ? -1 : 1) * probabilities[j];
      features[2] += re[j] * re[j ^ 3] + im[j] * im[j ^ 3];
    }
    const logit = 1.4 * features[0] - 0.8 * features[1] + 0.6 * features[2];
    const sigmoid = 1 / (1 + Math.exp(-logit));
    const nu = NU_MIN + (NU_MAX - NU_MIN) * sigmoid;
    const r = nu * STEP_TIME / (TAU / GRID) ** 2;
    return {amplitudes: Array.from(re, (a, j) => [a, im[j]]), probabilities, features,
      norm: probabilities.reduce((a, b) => a + b, 0), logit, sigmoid, nu, r};
  }
  function circuitGradient(angles, parameter) {
    if (!Number.isInteger(parameter) || parameter < 0 || parameter > 3) throw new RangeError("Parameter must be 0–3.");
    const plus = [...angles], minus = [...angles]; plus[parameter] += Math.PI / 2; minus[parameter] -= Math.PI / 2;
    const p = circuit(plus), m = circuit(minus), center = circuit(angles);
    const features = p.features.map((v, i) => (v - m.features[i]) / 2);
    const logit = 1.4 * features[0] - 0.8 * features[1] + 0.6 * features[2];
    return {features, nu: (NU_MAX - NU_MIN) * center.sigmoid * (1 - center.sigmoid) * logit};
  }
  function initialDistribution(n = GRID, kind = "peaks") {
    const p = new Float64Array(n * n), wrap = a => Math.min(Math.abs(a), n - Math.abs(a));
    for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) {
      const a = wrap(x - n / 4) ** 2 + wrap(y - n / 2) ** 2;
      const b = wrap(x - 11 * n / 16) ** 2 + wrap(y - 5 * n / 16) ** 2;
      p[y * n + x] = kind === "point" ? Number(x === Math.floor(n / 4) && y === Math.floor(n / 2)) :
        kind === "stripe" ? 1 + 0.85 * Math.cos(TAU * x / n) : Math.exp(-a / 2.2) + 0.55 * Math.exp(-b / 2.2);
    }
    const mass = p.reduce((a, b) => a + b, 0);
    return Float64Array.from(p, v => v / mass);
  }
  function heatStep(p, r, n = GRID) {
    if (!Number.isFinite(r) || r < 0 || r > 0.25 || p.length !== n * n || !Number.isInteger(n) || n < 2) throw new RangeError("A square grid and 0 ≤ r ≤ 1/4 are required.");
    const q = new Float64Array(p.length);
    for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) {
      const index = y * n + x;
      q[index] = (1 - 4 * r) * p[index] + r * (p[y * n + (x + 1) % n] + p[y * n + (x + n - 1) % n] +
        p[((y + 1) % n) * n + x] + p[((y + n - 1) % n) * n + x]);
    }
    return q;
  }
  function distributionStats(p) {
    const uniform = 1 / p.length;
    return {mass: p.reduce((a, b) => a + b, 0), min: Math.min(...p), max: Math.max(...p),
      entropy: p.reduce((a, b) => a - (b > 0 ? b * Math.log2(b) : 0), 0),
      contrast: p.reduce((a, b) => a + (b - uniform) ** 2, 0) / 2};
  }
  function heatTrajectory(r, steps, kind = "peaks", n = GRID) {
    if (!Number.isInteger(steps) || steps < 0 || steps > 512) throw new RangeError("Use 0–512 steps.");
    let p = initialDistribution(n, kind);
    const initial = Array.from(p), history = [distributionStats(p)];
    for (let j = 0; j < steps; j++) { p = heatStep(p, r, n); history.push(distributionStats(p)); }
    return {initial, probabilities: Array.from(p), history, final: history[history.length - 1], steps, r, kind};
  }
  function blowupScaling(logTau, h) {
    if (!Number.isFinite(logTau) || logTau < -30 || logTau > 0 || h < 0.002 || h > 0.009) throw new RangeError("Use log10(tau) in [-30,0] and h in [0.002,0.009].");
    const exponents = {radial: 0.5, axial: 0.5 - h, velocity: -0.5 - h, volume: 1.5 - h, energy: 0.5 - 3 * h};
    const values = {}, logs = {};
    for (const [key, exponent] of Object.entries(exponents)) { logs[key] = exponent * logTau; values[key] = 10 ** logs[key]; }
    return {logTau, tau: 10 ** logTau, h, exponents, values, logs,
      energyProduct: values.velocity ** 2 * values.volume};
  }
  function stateFromSearch(search) {
    const q = new URLSearchParams(search);
    const num = (name, fallback, low, high) => { const value = Number(q.get(name)); return q.has(name) && Number.isFinite(value) ? clamp(value, low, high) : fallback; };
    return {time: num("time", 1.5, 0, 12), nu: num("nu", 0.08, 0, 0.3),
      view: q.get("view") === "flat" ? "flat" : "torus", yaw: num("yaw", -30, -180, 180), pitch: num("pitch", 36, -75, 75),
      power: Math.round(num("power", 1, 0, 3)), x: num("x", 0.28, 0, 1), y: num("y", 0.63, 0, 1),
      angles: DEFAULT_ANGLES.map((a, i) => num("a" + i, a, -Math.PI, Math.PI)),
      steps: Math.round(num("steps", 30, 0, 128)), initial: ["peaks", "point", "stripe"].includes(q.get("initial")) ? q.get("initial") : "peaks",
      logTau: num("logTau", -8, -18, 0), h: num("h", 0.006, 0.002, 0.009)};
  }
  function stateToSearch(s) {
    const q = new URLSearchParams();
    for (const name of ["time", "nu", "view", "yaw", "pitch", "power", "x", "y", "steps", "initial", "logTau", "h"]) q.set(name, String(s[name]));
    s.angles.forEach((a, i) => q.set("a" + i, String(a)));
    return "?" + q.toString();
  }
  return {TAU, GRID, STEP_TIME, NU_MIN, NU_MAX, DEFAULT_ANGLES, mod1, clamp, taylorGreen,
    matrixMultiply, renormalizationPower, toralFibres, circuit, circuitGradient,
    initialDistribution, heatStep, distributionStats, heatTrajectory, blowupScaling, stateFromSearch, stateToSearch};
}));
