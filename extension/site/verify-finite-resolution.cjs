"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const crypto = require("node:crypto");
const R = require("./finite-resolution-core.js");
const F = require("./fluid-core.js");
const M = require("./math.js");
const root = path.resolve(__dirname, "../..");
const referencePath = path.join(__dirname, "data/finite-resolution-reference.json");
const reference = JSON.parse(fs.readFileSync(referencePath, "utf8"));
assert.equal(reference.schema, "finite-resolution-reference-v1");
assert.equal(reference.reference_arithmetic.decimal_digits, 80);
const completed = [], maximum = {}, counts = {reference_cases: 0, grid_bound_cases: 0, heat_bound_cases: 0, invalid_inputs: 0};
function check(name, fn) { fn(); completed.push(name); }
function close(actual, expected, tolerance, name) {
  const error = Math.abs(actual - expected);
  maximum[name] = Math.max(maximum[name] || 0, error);
  assert.ok(Number.isFinite(actual) && error <= tolerance, name + ": " + actual + " versus " + expected);
}
function under(value, bound, allowance, name) {
  assert.ok(Number.isFinite(value) && Number.isFinite(bound) && value <= bound + allowance, name + ": " + value + " > " + bound);
}
check("independent 80-digit references", () => {
  const generator = fs.readFileSync(path.join(root, "extension/code/build_finite_resolution_reference.py"));
  assert.equal(crypto.createHash("sha256").update(generator).digest("hex"), reference.generator_sha256);
  for (const row of reference.taylor_green) {
    const q = R.taylorGreenDiagnostics(row.options);
    for (const [key, refKey] of [["amplitude","amplitude"],["curlMultiplier","curl_multiplier"],["laplacianMultiplier","laplacian_multiplier"],["curlError","curl_error"],["laplacianError","laplacian_error"],["pdeResidual","pde_residual"],["sampledEnergy","energy"]]) {
      close(q[key], row[refKey].value, 5e-13, "reference_taylor_green");
    }
    counts.reference_cases++;
  }
  for (const row of reference.heat_modes) {
    const q = R.heatModeDiagnostics(row.options);
    for (const [key, refKey] of [["r","r"],["discreteEigenvalue","discrete_eigenvalue"],["multiplier","multiplier"],["discreteAmplitude","discrete_amplitude"],["semiDiscreteAmplitude","semidiscrete_amplitude"],["continuumAmplitude","continuum_amplitude"],["spatialError","spatial_error"],["timeError","time_error"],["totalError","total_error"]]) {
      close(q[key], row[refKey].value, 8e-14, "reference_heat");
    }
    counts.reference_cases++;
  }
  for (const row of reference.u1_plaquettes) {
    const q = R.u1PlaquetteDiagnostics(row.options);
    for (const [key, refKey] of [["flux","flux"],["cellMean","cell_mean"],["stableDensity","stable_density"],["targetDensity","target_density"],["error","error"],["midpointBound","midpoint_bound"],["smallAngleBound","small_angle_bound"]]) {
      close(q[key], row[refKey].value, 2e-13 * Math.max(1, Math.abs(row[refKey].value)), "reference_u1");
    }
    counts.reference_cases++;
  }
});
check("Taylor-Green resolved-grid derivative, nonlinear residual and quadrature bounds", () => {
  for (const n of [5, 7, 8, 13, 16, 32, 64, 128]) for (const [time, nu] of [[0,0],[1.5,0.08],[12,0.3]]) {
    const q = R.taylorGreenDiagnostics({n,time,nu});
    under(q.curlError, q.curlBound, q.roundingHeuristic, "curl analytic bound with numerical allowance");
    under(q.laplacianError, q.laplacianBound, q.laplacianRoundingHeuristic, "Laplacian analytic bound with numerical allowance");
    under(q.pdeResidual, q.pdeBound, q.pdeRoundingHeuristic, "nonlinear PDE diagnostic bound with numerical allowance");
    under(q.energyError, 0, q.energyRoundingHeuristic, "resolved Fourier energy quadrature");
    under(q.divergence, 0, q.roundingHeuristic, "commuting centered derivative divergence");
    assert.equal(q.energyQuadratureExactRealArithmetic, true);
    assert.equal(q.boundStatus, R.BOUND_STATUS);
    assert.equal(q.roundingStatus, R.ROUNDING_STATUS);
    counts.grid_bound_cases++;
  }
});
check("heat spatial/time error budgets and actual one-step kernel", () => {
  for (const n of [8,16,32,64]) for (const [nu,time] of [[0,1],[0.08,1],[0.2,3]]) for (const [modeX,modeY] of [[0,0],[1,0],[1,2]]) {
    const q = R.heatModeDiagnostics({n,nu,time,modeX,modeY});
    assert.ok(q.r >= 0 && q.r <= 0.25);
    under(q.spatialError, q.spatialBound, 4e-14, "spatial heat bound");
    under(q.timeError, q.timeBound, q.roundingHeuristic, "Euler heat bound");
    under(q.totalError, q.totalBound, q.roundingHeuristic + 4e-14, "combined heat bound");
    assert.equal(q.continuumGeneratorGap, nu);
    assert.ok(q.generatorGapDeficit >= -4e-14);
    under(q.generatorGapDeficit, q.generatorGapBound, 4e-14, "finite-box generator gap discretization");
    if (modeX === 1 && modeY === 0) close(q.discreteGeneratorGap, nu*q.discreteEigenvalue, 4e-14, "fundamental_generator_mode");
    close(q.massAfterOneStep, 1, 8e-14, "one_step_mass");
    under(q.oneStepKernelResidual, 0, 64 * Number.EPSILON / (n*n), "independent heat kernel symbol");
    counts.heat_bound_cases++;
  }
});
check("repeated actual heatStep agrees with the spectral discrete trajectory", () => {
  for (const n of [8,16]) {
    const steps = 7, nu = 0.08, h = 2*Math.PI/n, time = steps*0.1*h*h/nu;
    const q = R.heatModeDiagnostics({n,nu,time,steps,modeX:1,modeY:2});
    let p = Float64Array.from({length:n*n}, (_,i)=>(1+0.5*Math.cos(h*(i%n+2*Math.floor(i/n))))/(n*n));
    for (let j=0;j<steps;j++) p=F.heatStep(p,q.r,n);
    for (let i=0;i<p.length;i++) {
      const expected=(1+0.5*q.discreteAmplitude*Math.cos(h*(i%n+2*Math.floor(i/n))))/(n*n);
      close(p[i],expected,2e-15,"repeated_heat_kernel");
    }
  }
});
check("admissible negative Fourier multiplier is not confused with unstable CFL", () => {
  const q=R.heatModeDiagnostics({n:8,nu:0.14,time:1,steps:1,modeX:3,modeY:3});
  assert.equal(q.negativeModeMultiplier,true); assert.ok(q.r<0.25);
  under(q.totalError,q.totalBound,1e-13,"oscillatory admissible mode");
});
check("U(1) smooth-cell and small-angle bounds", () => {
  for (const n of [1,2,4,8,16,64]) for (const curvature of [-1,0,1]) for (const quadratic of [-0.7,0,0.7]) {
    const q=R.u1PlaquetteDiagnostics({n,curvature,quadratic});
    under(q.error,q.bound,q.roundingHeuristic+1e-15,"U1 total real-arithmetic bound with numerical allowance");
    assert.ok(q.stableDensity>=0);
    close(q.rawDensity,2*M.gaugePlaquette(q.flux,0,0).action/(q.h**4),0,"existing_plaquette_reuse");
  }
});
const tgStudy=R.convergenceStudy("taylor-green");
const heatStudy=R.convergenceStudy("heat-mode");
const u1Study=R.convergenceStudy("u1-plaquette");
const variableStudy=R.convergenceStudy("u1-plaquette",{curvature:1,quadratic:0.7});
check("representative convergence, with no forced total-heat rate", () => {
  assert.ok(tgStudy.rows.at(-1).observedOrder>1.9 && tgStudy.rows.at(-1).observedOrder<2.1);
  assert.ok(u1Study.rows.at(-1).observedOrder>3.9 && u1Study.rows.at(-1).observedOrder<4.1);
  assert.ok(variableStudy.rows.at(-1).observedOrder>1.9 && variableStudy.rows.at(-1).observedOrder<2.1);
  const hs=heatStudy.rows;
  const spatialOrder=Math.log(hs.at(-2).spatialError/hs.at(-1).spatialError)/Math.log(2);
  assert.ok(spatialOrder>1.9 && spatialOrder<2.1);
  // Spatial under-diffusion and Euler over-diffusion can cancel.
  assert.ok(hs.some(r=>r.totalError<Math.min(r.spatialError,r.timeError)));
  assert.ok(hs.slice(1).every(r=>Number.isFinite(r.observedOrder)));
  const a=R.heatModeDiagnostics({n:16,nu:0.08,time:1,steps:32});
  const b=R.heatModeDiagnostics({n:16,nu:0.08,time:1,steps:64});
  const timeOrder=Math.log(a.timeError/b.timeError)/Math.log(2);
  assert.ok(timeOrder>0.9 && timeOrder<1.1);
});
const cancellation=R.u1PlaquetteDiagnostics({n:65536,curvature:1,quadratic:0});
const floorStudy=R.convergenceStudy("u1-plaquette",{curvature:1},[1024,4096,65536]);
check("loss of significance and rounding-scale rates are retained", () => {
  assert.equal(cancellation.cancellationDetected,true);
  assert.equal(cancellation.rawDensity,0);
  assert.equal(cancellation.stableDensity,1);
  assert.equal(cancellation.errorStatus,"unresolved-at-rounding-scale");
  assert.equal(floorStudy.rows.at(-1).observedOrder,null);
  assert.equal(floorStudy.rows.at(-1).orderStatus,"unresolved-at-rounding-scale");
  const high=reference.u1_plaquettes.find(r=>r.options.n===65536);
  assert.ok(Number(high.error.decimal)>0);
  assert.equal(high.stable_density.value,1);
});
const phaseAlias=R.u1PlaquetteDiagnostics({n:1,curvature:8});
check("phase aliasing remains distinct from a small-angle error bound", () => {
  assert.equal(phaseAlias.phaseAliased,true);
  close(phaseAlias.flux-phaseAlias.principalPhase,2*Math.PI,1e-14,"phase_alias_turn");
  const shifted=R.u1PlaquetteDiagnostics({n:1,curvature:8+2*Math.PI});
  close(shifted.stableDensity,phaseAlias.stableDensity,2e-14,"phase_alias_same_wilson_density");
  assert.notEqual(shifted.targetDensity,phaseAlias.targetDensity);
});
check("zero-time and zero-field cases do not fabricate an observed order", () => {
  assert.equal(R.heatModeDiagnostics({time:0,steps:0}).error,0);
  assert.equal(R.heatModeDiagnostics({nu:0,time:1}).error,0);
  assert.equal(R.convergenceStudy("u1-plaquette",{curvature:0,quadratic:0}).rows.at(-1).observedOrder,null);
  const q=R.taylorGreenDiagnostics({n:8,time:1000,nu:100});
  assert.equal(q.errorStatus,"reference-underflow");
  assert.equal(R.convergenceStudy("taylor-green",{time:1000,nu:100}).rows.at(-1).observedOrder,null);
});
check("invalid grids, Nyquist aliases, unstable steps and nonfinite inputs fail closed", () => {
  const invalid=[
    ()=>R.taylorGreenDiagnostics({n:4}), ()=>R.taylorGreenDiagnostics({n:129}),
    ()=>R.taylorGreenDiagnostics({n:NaN}), ()=>R.taylorGreenDiagnostics({time:-1}),
    ()=>R.taylorGreenDiagnostics({nu:Infinity}), ()=>R.taylorGreenDiagnostics(null),
    ()=>R.heatModeDiagnostics({n:8,modeX:4}), ()=>R.heatModeDiagnostics({n:8,modeY:5}),
    ()=>R.heatModeDiagnostics({modeX:1.5}), ()=>R.heatModeDiagnostics({nu:-1}),
    ()=>R.heatModeDiagnostics({n:16,nu:1,time:1,steps:1}),
    ()=>R.heatModeDiagnostics({time:1,steps:0}), ()=>R.heatModeDiagnostics({time:0,steps:1}),
    ()=>R.heatModeDiagnostics({time:NaN}), ()=>R.heatModeDiagnostics([]),
    ()=>R.u1PlaquetteDiagnostics({n:0}), ()=>R.u1PlaquetteDiagnostics({n:65537}),
    ()=>R.u1PlaquetteDiagnostics({curvature:Infinity}), ()=>R.u1PlaquetteDiagnostics({quadratic:NaN}),
    ()=>R.convergenceStudy("unknown"), ()=>R.convergenceStudy("heat-mode",{},[16,8]),
    ()=>R.convergenceStudy("taylor-green",{},[8,8]), ()=>R.convergenceStudy("u1-plaquette",null),
  ];
  for (const fn of invalid) { assert.throws(fn); counts.invalid_inputs++; }
});
const digest = file => crypto.createHash("sha256").update(fs.readFileSync(path.join(root,file))).digest("hex");
const sourceFiles=["extension/site/finite-resolution-core.js","extension/site/verify-finite-resolution.cjs",
  "extension/code/build_finite_resolution_reference.py","extension/site/data/finite-resolution-reference.json",
  "extension/site/fluid-core.js","extension/site/math.js"];
const report={
  schema:"finite-resolution-checks-v1",status:"passed",checked_at_utc:new Date().toISOString(),node_version:process.version,
  reference_arithmetic:reference.reference_arithmetic,checks:completed,counts,maximum_reference_errors:maximum,
  observed_studies:{taylor_green:tgStudy,heat:heatStudy,u1_constant:u1Study,u1_variable:variableStudy},
  negative_controls:{cancellation,rounding_floor_study:floorStudy,phase_alias:phaseAlias,
    unstable_cfl:"rejected",nyquist_alias:"rejected",pressure_underresolution:"rejected"},
  source_sha256:Object.fromEntries(sourceFiles.map(p=>[p,digest(p)])),
  scope:"Independent high-precision references, actual existing numerical kernels and declared analytic-family bounds. Floating evaluations use explicit numerical allowances; rounding scales are heuristic, not interval certificates. No continuum PDE theorem, arbitrary-field convergence, or Yang-Mills mass-gap claim."
};
const target=path.join(root,"extension/verification/finite-resolution-node.json");
fs.mkdirSync(path.dirname(target),{recursive:true}); fs.writeFileSync(target,JSON.stringify(report,null,2)+"\n");
console.log(JSON.stringify({status:report.status,checks:completed.length,counts,maximum_reference_errors:maximum,output:path.relative(root,target)},null,2));
