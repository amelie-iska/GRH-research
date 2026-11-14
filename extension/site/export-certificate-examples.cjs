/* Reproduce the eleven source-bound examples used by the Lean return-path audit. */
'use strict';
const fs = require('node:fs'), path = require('node:path'), crypto = require('node:crypto');
const B = require('./certificate-bridge.js'), C = require('./cosmology-calibration-core.js');
const repo = path.resolve(__dirname, '../..');
const registryPath = path.join(__dirname, 'data/certificate-contracts.json');
const registry = JSON.parse(fs.readFileSync(registryPath, 'utf8'));
const data = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/cosmology-synthetic.json'), 'utf8'));
const model = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/cosmology-moment-model.json'), 'utf8'));
B.setCosmologyAdapter(parameters => C.evaluate(data, model, parameters));
const out = path.resolve(process.argv[2] || path.join(repo, 'extension/review/final-pass/lab-certificates'));
fs.mkdirSync(out, {recursive: true});
const sha = file => crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const cases = [
  ['hodge-zero', 'hodge-family-v1', {epsilon: '0/1'}],
  ['hodge-third', 'hodge-family-v1', {epsilon: '1/3'}],
  ['hodge-one', 'hodge-family-v1', {epsilon: '1/1'}],
  ['cover-zero', 'quadratic-cover-v1', {power: '0/1', x: '7/25', y: '63/100'}],
  ['cover-three', 'quadratic-cover-v1', {power: '3/1', x: '7/25', y: '63/100'}],
  ...['5/8', '3/5', '2/1'].map((rate, i) => ['gain-' + i, 'weighted-gain-v1', {matrix: [['1/4', '3/2'], ['3/32', '1/4']], weights: ['4/1', '1/1'], rate}]),
  ...[['cosmology-budget-passes', '6/1', '1/20'], ['cosmology-budget-fails', '2/1', '1/20'], ['cosmology-capped-one', '2/1', '1/1']].map(([name, threshold, alpha]) => [name, 'cosmology-calibration-v1', {alpha, center: '0', order: '8', snr: '0/1', threshold, width: '1'}])
];
const manifest = {schema: 'grh-lab-certificate-export-evidence-v1', registry_sha256: sha(registryPath), emitter_sha256: sha(path.join(__dirname, 'certificate-bridge.js')), source_bound_instances: []};
for (const [name, contract, parameters] of cases) {
  const certificate = B.create(contract, parameters, registry), json = path.join(out, name + '.json'), lean = path.join(out, name + '.lean');
  fs.writeFileSync(json, JSON.stringify(certificate, null, 2) + '\n');
  fs.writeFileSync(lean, B.leanSource(certificate, registry));
  manifest.source_bound_instances.push({name, contract, certificate: name + '.json', certificate_sha256: sha(json), lean: name + '.lean', lean_sha256: sha(lean)});
}
fs.writeFileSync(path.join(out, 'export-manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
console.log(JSON.stringify({status: 'exported', instances: cases.length, output_directory: out, registry_sha256: manifest.registry_sha256}));
