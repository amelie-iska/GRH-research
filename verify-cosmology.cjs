"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const math = require("./cosmology.js");
const data = JSON.parse(fs.readFileSync(path.join(__dirname, "data/cosmology-synthetic.json"), "utf8"));
assert.equal(math.validateDataset(data), true);
const close = (actual, expected, tolerance, label) => assert.ok(Math.abs(actual - expected) <= tolerance, `${label}: ${actual} != ${expected}`);

for (const record of data.benchmark.experiments) {
  const result = math.evaluate(data, {center: 0, width: 1, snr: record.injected_matched_snr});
  close(result.maximum, record.scan_maximum, 2e-12, "Python/JS scan maximum");
  close(result.fixedScore, record.fixed_injection_template_score, 2e-12, "Python/JS fixed score");
  close(result.selectedLocalP, record.selected_template_uncorrected_one_sided_p,
    Math.max(1e-23, record.selected_template_uncorrected_one_sided_p * 2e-12), "Python erfc / JS gamma tail");
  assert.equal(result.winner, record.selected_template_index);
  assert.equal(result.exceedances, record.calibration_exceedances);
  assert.equal(result.globalP, record.global_rank_p);
}

let maximumPairingError = 0;
for (let i = 0; i < 288; i += 1) {
  maximumPairingError = Math.max(maximumPairingError, Math.abs(math.dot(data.filter_weights[i], data.normalized_injection_templates[i]) - 1));
}
assert.ok(maximumPairingError < 1e-12, "Every declared injection must raise its own filter by one per unit SNR.");

assert.deepEqual(math.rankProbability([1, 2, 2, 4], 2), {exceedances: 3, p: 0.8});
assert.deepEqual(math.rankProbability([1, 2, 2, 4], 2.1), {exceedances: 1, p: 0.4});
assert.deepEqual(math.rankProbability([1, 2, 2, 4], 5), {exceedances: 0, p: 0.2});
assert.deepEqual(math.rankProbability([1, 2, 2, 4], 0), {exceedances: 4, p: 1});
close(math.normalUpperTail(0), 0.5, 0, "Zero normal score");
close(math.normalUpperTail(1), 0.15865525393145707, 1e-15, "Normal score 1");
close(math.normalUpperTail(8), 6.220960574271819e-16, 2e-29, "Normal score 8");
close(math.normalUpperTail(-1), 0.8413447460685429, 1e-15, "Negative score symmetry");

for (const point of data.points) {
  for (const [yaw, pitch] of [[0, 0], [-180, -90], [34, 67], [180, 90]]) {
    const rotated = math.rotatePoint(point, yaw, pitch);
    close(math.dot(rotated, rotated), 1, 2e-15, "Rotation preserves unit radius");
  }
  const orientation = math.facePoint(point);
  const facing = math.rotatePoint(point, orientation.yaw, orientation.pitch);
  close(facing[2], 1, 1e-15, "Face-injection orientation");
}

const view = {center: 17, width: 2, snr: 3.2, view: "flat", yaw: 55, pitch: -22};
assert.deepEqual(math.stateFromSearch(math.stateToSearch(view)), view);
assert.deepEqual(math.stateFromSearch("?center=garbage&width=99&snr=-8&view=unknown&pitch=300"),
  {center: 0, width: 2, snr: 0, view: "sphere", yaw: -25, pitch: 90});
const bins = math.histogram(data.calibration_maxima_sorted, 32, 0, 8);
assert.equal(bins.outside, 0);
assert.equal(bins.counts.reduce((a, b) => a + b, 0), 4095);

console.log(JSON.stringify({status: "passed", recorded_python_cases: 4, template_pairings_checked: 288,
  maximum_pairing_error: maximumPairingError, unit_directions_checked: 96,
  checks: ["exact global ranks and ties", "normal tails against Python", "projection geometry", "URL bounds and round trip", "histogram count preservation"]}, null, 2));
