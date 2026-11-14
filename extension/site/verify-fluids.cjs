"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const crypto = require("node:crypto");
const F = require("./fluid-core.js");
const reference = JSON.parse(fs.readFileSync(path.join(__dirname, "data/fluids-reference.json"), "utf8"));
assert.equal(reference.schema, "fluid-reference-v1");
const maximum = {};
function close(actual, expected, tolerance, key) {
  const error = Math.abs(actual - expected);
  maximum[key] = Math.max(maximum[key] || 0, error);
  assert.ok(Number.isFinite(actual) && error <= tolerance, `${key}: ${actual} versus ${expected}; tolerance ${tolerance}`);
}
for (const row of reference.taylor_green) {
  const value = F.taylorGreen(...row.args);
  for (const key of ["u", "v", "pressure", "vorticity", "energyAverage", "energyDerivative"]) close(value[key], row[key], 2e-14, "taylor_green_reference");
}
// A manufactured-flow test using finite differences, independently of its symbolic reference.
let finiteDifferenceErrors = [];
for (const step of [0.004, 0.002, 0.001]) {
  let maxResidual = 0;
  for (const [x, y, time, nu] of [[0.7, 1.2, 0.5, 0.12], [2.2, 4.1, 1.7, 0.08], [3.8, 5.3, 2.3, 0.2]]) {
    const f = F.taylorGreen(x, y, time, nu), xp = F.taylorGreen(x + step, y, time, nu), xm = F.taylorGreen(x - step, y, time, nu), yp = F.taylorGreen(x, y + step, time, nu), ym = F.taylorGreen(x, y - step, time, nu), tp = F.taylorGreen(x, y, time + step, nu), tm = F.taylorGreen(x, y, time - step, nu);
    for (const key of ["u", "v"]) {
      const dx = (xp[key] - xm[key]) / (2 * step), dy = (yp[key] - ym[key]) / (2 * step), dt = (tp[key] - tm[key]) / (2 * step);
      const dp = key === "u" ? (xp.pressure - xm.pressure) / (2 * step) : (yp.pressure - ym.pressure) / (2 * step);
      const lap = (xp[key] + xm[key] + yp[key] + ym[key] - 4 * f[key]) / step ** 2;
      maxResidual = Math.max(maxResidual, Math.abs(dt + f.u * dx + f.v * dy + dp - nu * lap));
    }
  }
  finiteDifferenceErrors.push(maxResidual);
}
assert.ok(finiteDifferenceErrors[1] < finiteDifferenceErrors[0] / 3.5);
assert.ok(finiteDifferenceErrors[2] < finiteDifferenceErrors[1] / 3.5);

for (const row of reference.renormalization_powers) {
  const actual = F.renormalizationPower(row.k);
  assert.deepEqual(actual.matrix, row.matrix); assert.equal(actual.determinant, row.determinant);
  const [[a, b], [c, d]] = actual.matrix.map(r => r.map(BigInt));
  assert.equal(a * d - b * c, 14n ** BigInt(row.k));
}
let fibrePoints = 0;
for (const power of [0, 1, 2, 3]) for (const point of [[0, 0], [0.28, 0.63], [0.999, 0.001]]) {
  const data = F.toralFibres(power, point, [-2, 3]);
  assert.equal(data.points.length, 14 ** power);
  const unique = new Set(data.points.map(p => p.map(v => Math.round(v * 1e10) % 1e10).join(",")));
  assert.equal(unique.size, data.points.length);
  for (const x of data.points) {
    for (let j = 0; j < 2; j++) {
      const value = data.matrix[j][0] * x[0] + data.matrix[j][1] * x[1] - data.target[j];
      close(value - Math.round(value), 0, 2e-12, "fibre_cover_residual");
    }
    fibrePoints++;
  }
  close(data.characterError, 0, 2e-12, "character_pullback_residual");
}

for (const row of reference.circuit_cases) {
  const actual = F.circuit(row.angles);
  for (let j = 0; j < 4; j++) {
    for (let part = 0; part < 2; part++) close(actual.amplitudes[j][part], row.amplitudes[j][part], 2e-15, "complex_amplitude_reference");
    close(actual.probabilities[j], row.probabilities[j], 2e-15, "probability_reference");
  }
  actual.features.forEach((value, j) => close(value, row.features[j], 3e-15, "pauli_feature_reference"));
  close(actual.norm, 1, 2e-15, "circuit_norm"); close(actual.nu, row.nu, 2e-15, "diffusivity_reference");
  assert.ok(actual.nu > F.NU_MIN && actual.nu < F.NU_MAX && actual.r > 0 && actual.r < 0.25);
  for (let parameter = 0; parameter < 4; parameter++) {
    const gradient = F.circuitGradient(row.angles, parameter);
    gradient.features.forEach((value, j) => close(value, row.feature_gradients[parameter][j], 3e-15, "parameter_shift_reference"));
    close(gradient.nu, row.nu_gradients[parameter], 2e-15, "nonlinear_chain_reference");
  }
}
for (const row of reference.heat_trajectories) {
  const actual = F.heatTrajectory(row.r, row.steps, row.kind);
  actual.probabilities.forEach((value, i) => close(value, row.probabilities[i], 2e-15, "heat_probability_reference"));
  close(actual.final.entropy, row.entropy, 3e-14, "heat_entropy_reference");
  close(actual.final.contrast, row.contrast, 2e-15, "heat_contrast_reference");
  for (let j = 0; j < actual.history.length; j++) {
    const now = actual.history[j]; close(now.mass, 1, 3e-14, "heat_mass"); assert.ok(now.min >= 0);
    if (j) { assert.ok(now.entropy + 3e-14 >= actual.history[j - 1].entropy); assert.ok(now.contrast <= actual.history[j - 1].contrast + 1e-15); }
  }
}
// An independent Fourier eigenmode detects indexing or periodic-boundary mistakes.
const n = 16, rate = 0.21, mode = new Float64Array(n * n), kx = 2, ky = 3;
for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) mode[y * n + x] = (1 + 0.4 * Math.cos(2 * Math.PI * (kx * x + ky * y) / n)) / (n * n);
const eigenvalue = 1 - 4 * rate + 2 * rate * (Math.cos(2 * Math.PI * kx / n) + Math.cos(2 * Math.PI * ky / n));
const evolved = F.heatStep(mode, rate, n);
evolved.forEach((value, i) => close(value, 1 / (n * n) + eigenvalue * (mode[i] - 1 / (n * n)), 1e-17, "heat_fourier_eigenmode"));
assert.throws(() => F.heatStep(mode, 0.25001), RangeError);
assert.throws(() => F.heatStep(mode, -0.01), RangeError);
assert.throws(() => F.toralFibres(4, [0, 0]), RangeError);
// Endpoint r=1/4 need not mix strictly: a checkerboard swaps parity.
const checker = Float64Array.from({length: n * n}, (_, i) => ((i % n + Math.floor(i / n)) % 2 ? 0 : 2 / (n * n)));
const twice = F.heatStep(F.heatStep(checker, 0.25, n), 0.25, n);
assert.deepEqual(Array.from(twice), Array.from(checker));

for (const h of [0.002, 0.006, 0.009]) for (const logTau of [0, -3, -8, -18]) {
  const value = F.blowupScaling(logTau, h);
  close(value.logs.energy, 2 * value.logs.velocity + value.logs.volume, 5e-15, "scaling_exponent");
  close(value.energyProduct / value.values.energy, 1, 7e-15, "scaling_energy_product");
  assert.ok(value.exponents.energy > 0 && value.exponents.velocity < 0);
}
const saved = F.stateFromSearch(""); assert.deepEqual(F.stateFromSearch(F.stateToSearch(saved)), saved);
const bounded = F.stateFromSearch("?time=-20&nu=1&power=99&h=NaN&steps=banana&logTau=-100&view=bad");
assert.equal(bounded.time, 0); assert.equal(bounded.nu, 0.3); assert.equal(bounded.power, 3);
assert.equal(bounded.h, 0.006); assert.equal(bounded.steps, 30); assert.equal(bounded.logTau, -18); assert.equal(bounded.view, "torus");

const digest = filename => crypto.createHash("sha256").update(fs.readFileSync(path.join(__dirname, filename))).digest("hex");
const report = {status: "passed", checked_at_utc: new Date().toISOString(), node_version: process.version,
  independent_reference: "Python symbolic expressions, dense complex128 matrices, and exact integer arithmetic",
  circuit_cases: reference.circuit_cases.length, feature_gradient_cases: reference.circuit_cases.length * 4,
  complete_fibre_points_checked: fibrePoints, finite_difference_momentum_residuals: finiteDifferenceErrors,
  maximum_errors: maximum, checks: ["independent Python reference comparison", "manufactured PDE residual second-order convergence", "exact BigInt determinant powers", "complete toral fibres and character pullback", "actual complex circuit and chain-rule gradient", "heat positivity, normalization, entropy, contrast", "Fourier eigenmode", "periodic endpoint obstruction to strict mixing", "scale-energy product", "URL state and bounds"],
  hashes: {core: digest("fluid-core.js"), reference: digest("data/fluids-reference.json"), verification_script: digest("verify-fluids.cjs")},
  scope: "Finite mathematical and numerical interfaces; not verification of the upstream continuum singularity proof or quantum advantage."};
const output = path.join(__dirname, "../verification/fluids-node.json");
fs.mkdirSync(path.dirname(output), {recursive: true}); fs.writeFileSync(output, JSON.stringify(report, null, 2) + "\n");
console.log(JSON.stringify(report, null, 2));
