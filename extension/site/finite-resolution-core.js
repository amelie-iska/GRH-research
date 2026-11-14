/* Resolution diagnostics for declared analytic families, not a new fluid solver.
 * Bounds concern real arithmetic; evaluated doubles are not outward-rounded
 * interval certificates. Rounding indicators below are explicitly heuristic.
 */
(function (root, factory) {
  "use strict";
  if (typeof module === "object" && module.exports) {
    module.exports = factory(require("./fluid-core.js"), require("./math.js"));
  } else root.ResolutionMath = factory(root.FluidMath, root.ResearchMath);
}(typeof globalThis !== "undefined" ? globalThis : this, function (F, M) {
  "use strict";
  const TAU = 2 * Math.PI, EPS = Number.EPSILON;
  const BOUND_STATUS = "analytic-real-arithmetic-not-an-interval-certificate";
  const ROUNDING_STATUS = "heuristic-not-a-certified-roundoff-bound";
  function optionsObject(value) {
    if (!value || typeof value !== "object" || Array.isArray(value)) throw new TypeError("Diagnostic options must be an object.");
  }
  function integer(x, lo, hi, name) {
    if (!Number.isSafeInteger(x) || x < lo || x > hi) throw new RangeError(name + " must be an integer in [" + lo + ", " + hi + "].");
    return x;
  }
  function finite(x, lo, hi, name) {
    if (!Number.isFinite(x) || x < lo || x > hi) throw new RangeError(name + " must be finite and in [" + lo + ", " + hi + "].");
    return x;
  }
  function dependency(value, name) { if (!value) throw new Error(name + " must be loaded before this diagnostic is used."); }
  function sum(values) {
    let total = 0, correction = 0;
    for (const value of values) { const y = value - correction, next = total + y; correction = (next - total) - y; total = next; }
    return total;
  }
  function sinc(x) { return x === 0 ? 1 : Math.sin(x) / x; }
  function metadata(family, n, h, error, bound, roundingHeuristic, underflow) {
    return {family, n, h, error, bound, boundStatus: BOUND_STATUS,
      roundingHeuristic, roundingStatus: ROUNDING_STATUS, underflow,
      errorStatus: underflow ? "reference-underflow" : error <= roundingHeuristic ? "unresolved-at-rounding-scale" : "numerically-resolved"};
  }

  function taylorGreenDiagnostics(options = {}) {
    optionsObject(options);
    dependency(F, "FluidMath");
    const n = integer(options.n === undefined ? 16 : options.n, 5, 128, "n");
    const time = finite(options.time === undefined ? 1.5 : options.time, 0, 1000, "time");
    const nu = finite(options.nu === undefined ? 0.08 : options.nu, 0, 100, "nu");
    // n >= 5 resolves both velocity frequency 1 and pressure frequency 2
    // strictly below Nyquist; it does not certify an arbitrary flow's spectrum.
    const h = TAU / n, grid = new Array(n * n);
    const at = (x, y) => grid[((y + n) % n) * n + (x + n) % n];
    const energies = new Float64Array(n * n);
    for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) {
      const value = F.taylorGreen(x * h, y * h, time, nu);
      grid[y * n + x] = value;
      energies[y * n + x] = (value.u * value.u + value.v * value.v) / 2;
    }
    const a = grid[0].amplitude;
    let curlError = 0, laplacianError = 0, divergence = 0, pdeResidual = 0, curlSquare = 0;
    for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) {
      const c = at(x, y), xp = at(x + 1, y), xm = at(x - 1, y), yp = at(x, y + 1), ym = at(x, y - 1);
      const dxu = (xp.u - xm.u) / (2 * h), dyu = (yp.u - ym.u) / (2 * h);
      const dxv = (xp.v - xm.v) / (2 * h), dyv = (yp.v - ym.v) / (2 * h);
      const lu = (xp.u + xm.u + yp.u + ym.u - 4 * c.u) / (h * h);
      const lv = (xp.v + xm.v + yp.v + ym.v - 4 * c.v) / (h * h);
      const ce = Math.abs(dxv - dyu - c.vorticity);
      curlError = Math.max(curlError, ce); curlSquare += ce * ce;
      laplacianError = Math.max(laplacianError, Math.abs(lu + 2 * c.u), Math.abs(lv + 2 * c.v));
      divergence = Math.max(divergence, Math.abs(dxu + dyv));
      const rx = -2 * nu * c.u + c.u * dxu + c.v * dyu + (xp.pressure - xm.pressure) / (2 * h) - nu * lu;
      const ry = -2 * nu * c.v + c.u * dxv + c.v * dyv + (yp.pressure - ym.pressure) / (2 * h) - nu * lv;
      pdeResidual = Math.max(pdeResidual, Math.abs(rx), Math.abs(ry));
    }
    const curlBound = a * h * h / 3, laplacianBound = a * h * h / 6;
    const pdeBound = nu * a * h * h / 6 + a * a * h * h / 4;
    const roundingHeuristic = 64 * EPS * a / h;
    const sampledEnergy = sum(energies) / (n * n), exactEnergy = a * a / 4;
    return Object.assign(metadata("taylor-green", n, h, curlError, curlBound, roundingHeuristic, a === 0), {
      time, nu, amplitude: a, nominalBoundOrder: 2,
      curlError, curlRmsError: Math.sqrt(curlSquare / (n * n)), curlBound,
      curlMultiplier: sinc(h), curlSymbolEnvelope: 2 * a * Math.abs(1 - sinc(h)),
      laplacianError, laplacianBound, laplacianMultiplier: 8 * Math.sin(h / 2) ** 2 / (h * h),
      laplacianRoundingHeuristic: 128 * EPS * a / (h * h),
      divergence, divergenceExactRealArithmetic: 0,
      pdeResidual, pdeBound, pdeRoundingHeuristic: 128 * EPS * (nu * a / (h * h) + a * a / h),
      sampledEnergy, exactEnergy, energyError: Math.abs(sampledEnergy - exactEnergy),
      energyQuadratureExactRealArithmetic: true, energyRoundingHeuristic: 64 * EPS * a * a,
      scope: "Periodic samples of the existing analytic Taylor-Green solution. Central spatial differences are diagnostic; the time derivative is analytic. Energy quadrature is exact for this resolved Fourier family in real arithmetic. No numerical Navier-Stokes evolution or continuum theorem is inferred."
    });
  }

  function heatModeDiagnostics(options = {}) {
    optionsObject(options);
    dependency(F, "FluidMath");
    const n = integer(options.n === undefined ? 16 : options.n, 4, 128, "n");
    const nu = finite(options.nu === undefined ? 0.08 : options.nu, 0, 100, "nu");
    const time = finite(options.time === undefined ? 1 : options.time, 0, 1000, "time");
    const limit = Math.floor((n - 1) / 2);
    const modeX = integer(options.modeX === undefined ? 1 : options.modeX, -limit, limit, "modeX (strictly below Nyquist)");
    const modeY = integer(options.modeY === undefined ? 0 : options.modeY, -limit, limit, "modeY (strictly below Nyquist)");
    const h = TAU / n;
    const suggested = time === 0 ? 0 : Math.max(1, Math.ceil(5 * nu * time / (h * h)));
    const steps = integer(options.steps === undefined ? suggested : options.steps, 0, 10000000, "steps");
    if ((time === 0) !== (steps === 0)) throw new RangeError("Zero time requires zero steps; positive time requires positive steps.");
    const dt = steps ? time / steps : 0, r = nu * dt / (h * h);
    if (!(r >= 0 && r <= 0.25)) throw new RangeError("The existing heat channel requires CFL ratio 0 <= nu*dt/h^2 <= 1/4.");
    const continuumEigenvalue = modeX * modeX + modeY * modeY;
    const discreteEigenvalue = 4 * (Math.sin(modeX * h / 2) ** 2 + Math.sin(modeY * h / 2) ** 2) / (h * h);
    const x = nu * dt * discreteEigenvalue, multiplier = 1 - x;
    if (Math.abs(multiplier) > 1) throw new RangeError("Computed mode multiplier is outside the stable interval.");
    const discreteAmplitude = steps ? multiplier ** steps : 1;
    const semiDiscreteAmplitude = Math.exp(-nu * discreteEigenvalue * time);
    const continuumAmplitude = Math.exp(-nu * continuumEigenvalue * time);
    const spatialError = Math.abs(semiDiscreteAmplitude - continuumAmplitude);
    const timeError = Math.abs(discreteAmplitude - semiDiscreteAmplitude);
    const totalError = Math.abs(discreteAmplitude - continuumAmplitude);
    const spatialBound = Math.min(1, nu * time * h * h * (modeX ** 4 + modeY ** 4) / 12);
    // |a^m-b^m| <= m|a-b| for |a|,|b|<=1; |1-x-exp(-x)| <= x^2/2.
    // This remains valid for an admissible negative mode multiplier.
    const timeBound = Math.min(2, steps * x * x / 2), totalBound = Math.min(2, spatialBound + timeBound);
    // This is the smallest nonzero generator eigenvalue on the fixed 2pi box,
    // not an absolute mixing gap of a possibly periodic discrete-time channel.
    const continuumGeneratorGap = nu;
    const discreteGeneratorGap = 4 * nu * Math.sin(h / 2) ** 2 / (h * h);
    const initial = new Float64Array(n * n), cosine = new Float64Array(n * n);
    for (let yy = 0; yy < n; yy++) for (let xx = 0; xx < n; xx++) {
      const i = yy * n + xx;
      cosine[i] = Math.cos(h * (modeX * xx + modeY * yy));
      initial[i] = continuumEigenvalue === 0 ? 1 / (n * n) : (1 + 0.5 * cosine[i]) / (n * n);
    }
    const once = F.heatStep(initial, r, n);
    let oneStepKernelResidual = 0;
    for (let i = 0; i < once.length; i++) {
      const expected = continuumEigenvalue === 0 ? 1 / (n * n) : (1 + 0.5 * multiplier * cosine[i]) / (n * n);
      oneStepKernelResidual = Math.max(oneStepKernelResidual, Math.abs(once[i] - expected));
    }
    const underflow = continuumEigenvalue > 0 && continuumAmplitude === 0;
    const roundingHeuristic = 64 * EPS * (steps + 1) * Math.max(Math.abs(discreteAmplitude), semiDiscreteAmplitude, continuumAmplitude);
    return Object.assign(metadata("heat-mode", n, h, totalError, totalBound, roundingHeuristic, underflow), {
      nu, time, modeX, modeY, steps, dt, r, nominalBoundOrder: options.steps === undefined ? 2 : null,
      continuumEigenvalue, discreteEigenvalue, multiplier, negativeModeMultiplier: multiplier < 0,
      discreteAmplitude, semiDiscreteAmplitude, continuumAmplitude,
      spatialError, spatialBound, timeError, timeBound, totalError, totalBound,
      boxSide: TAU, continuumGeneratorGap, discreteGeneratorGap,
      generatorGapDeficit: continuumGeneratorGap - discreteGeneratorGap, generatorGapBound: nu * h * h / 12,
      oneStepKernelResidual, massAfterOneStep: sum(once),
      scope: "A fixed Fourier mode on the 2pi-periodic torus, evolved by the actual five-point heatStep kernel. Final discrete amplitude is evaluated by its exact real-arithmetic symbol. Default time steps refine with h^2 at fixed physical time. Grid-dependent point/peaks initial data are not claimed to be samples of this smooth family."
    });
  }

  function u1PlaquetteDiagnostics(options = {}) {
    optionsObject(options);
    dependency(M, "ResearchMath");
    const n = integer(options.n === undefined ? 1 : options.n, 1, 65536, "n");
    const curvature = finite(options.curvature === undefined ? 1 : options.curvature, -10000, 10000, "curvature");
    const quadratic = finite(options.quadratic === undefined ? 0 : options.quadratic, -10000, 10000, "quadratic");
    const h = 1 / n, h2 = h * h;
    // Declared local smooth field B(x,y)=B0+kappa(x^2+y^2) on a centered cell.
    // The exact cell mean is B0+kappa*h^2/6; no edge quadrature is used.
    const cellMean = curvature + quadratic * h2 / 6, flux = h2 * cellMean;
    const plaquette = M.gaugePlaquette(flux, 0, 0);
    const rawDensity = 2 * plaquette.action / (h2 * h2);
    const stableDensity = 4 * Math.sin(flux / 2) ** 2 / (h2 * h2);
    const targetDensity = curvature * curvature;
    const midpointRadius = Math.abs(quadratic) * h2 / 6;
    const midpointBound = midpointRadius * (2 * Math.abs(curvature) + midpointRadius);
    const smallAngleBound = h2 * h2 * (Math.abs(curvature) + midpointRadius) ** 4 / 12;
    const bound = midpointBound + smallAngleBound;
    const error = Math.abs(stableDensity - targetDensity);
    const roundingHeuristic = 128 * EPS * Math.max(stableDensity, targetDensity, cellMean * cellMean);
    const rawRoundingHeuristic = 128 * EPS / (h2 * h2);
    return Object.assign(metadata("u1-plaquette", n, h, error, bound, roundingHeuristic, false), {
      curvature, quadratic, cellMean, flux, targetDensity, stableDensity, rawDensity,
      nominalBoundOrder: quadratic === 0 ? 4 : 2, midpointRadius, midpointBound, smallAngleBound,
      rawError: Math.abs(rawDensity - targetDensity), rawVsStable: Math.abs(rawDensity - stableDensity),
      rawRoundingHeuristic, rawActionNegative: plaquette.action < 0,
      cancellationDetected: flux !== 0 && plaquette.action === 0,
      principalPhase: Math.atan2(plaquette.W[1], plaquette.W[0]),
      phaseAliased: Math.abs(flux) >= Math.PI,
      unitModulusResidual: Math.abs(Math.hypot(...plaquette.W) - 1),
      scope: "A new local plaquette family inside a unit-square patch, h=1/n, with physical curvature B0 and quadratic variation kappa. Flux is its exact centered-cell integral. The old single-plaquette slider has no continuum spacing. The small-angle estimate does not remove 2pi phase aliasing or supply a Yang-Mills continuum limit."
    });
  }

  const evaluators = Object.freeze({"taylor-green": taylorGreenDiagnostics, "heat-mode": heatModeDiagnostics, "u1-plaquette": u1PlaquetteDiagnostics});
  function convergenceStudy(family, options = {}, levels) {
    optionsObject(options);
    if (!Object.prototype.hasOwnProperty.call(evaluators, family)) throw new RangeError("Unknown resolution family.");
    const selected = levels === undefined ? (family === "u1-plaquette" ? [1, 2, 4, 8, 16, 32] : [8, 16, 32, 64]) : levels;
    if (!Array.isArray(selected) || selected.length < 2 || selected.length > 12 || selected.some((x, i) => !Number.isSafeInteger(x) || (i > 0 && x <= selected[i - 1]))) throw new RangeError("Use 2-12 strictly increasing integer refinement levels.");
    const rows = selected.map(n => evaluators[family](Object.assign({}, options, {n})));
    for (let i = 0; i < rows.length; i++) {
      const row = rows[i], previous = rows[i - 1];
      row.observedOrder = null;
      row.orderStatus = i === 0 ? "needs-two-levels" : "unresolved-at-rounding-scale";
      if (previous && row.errorStatus === "numerically-resolved" && previous.errorStatus === "numerically-resolved") {
        row.observedOrder = Math.log(previous.error / row.error) / Math.log(previous.h / row.h);
        row.orderStatus = "observed-not-certified";
      } else if (row.underflow || (previous && previous.underflow)) row.orderStatus = "reference-underflow";
    }
    return {family, rows, levels: selected.slice(), boundStatus: BOUND_STATUS, roundingStatus: ROUNDING_STATUS,
      scope: "Rates are observations between the specified grids, not a proof of a continuum limit. The analytic bound and model assumptions are reported separately."};
  }
  return Object.freeze({TAU, BOUND_STATUS, ROUNDING_STATUS, taylorGreenDiagnostics, heatModeDiagnostics, u1PlaquetteDiagnostics, convergenceStudy});
}));
