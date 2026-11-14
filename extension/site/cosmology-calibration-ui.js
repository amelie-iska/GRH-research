/* Live exact finite-search budgets and a reversible certificate interface. */
(function (root) {
  'use strict';
  if (!root.document) return;
  const $ = id => document.getElementById(id), Q = root.ExactRational, C = root.CosmologyCalibration;
  const status = $('riskLoadStatus');
  if (!status) return;
  const controls = ['riskThreshold', 'riskOrder', 'riskAlpha'].map($);
  let data, model, panel;

  function computedNumber(text) {
    const [n, d] = text.split('/');
    return Q.toNumber(Q.make(BigInt(n), BigInt(d)));
  }
  function pretty(text) {
    const n = computedNumber(text);
    return n > 0 && n < 0.0001 ? n.toExponential(6) : n.toPrecision(7);
  }
  function readParameters() {
    const state = root.CCCLab.getState();
    return {center: String(state.center), width: String(state.width), snr: root.LabCertificateBridge.userRational(String(state.snr)),
      threshold: root.LabCertificateBridge.userRational($('riskThreshold').value),
      order: $('riskOrder').value, alpha: root.LabCertificateBridge.userRational($('riskAlpha').value)};
  }
  function summary(certificate) {
    const result = certificate.result;
    return result.within_budget
      ? 'The fixed-threshold probability bound meets the requested budget under the stated moment assumptions.'
      : 'This threshold does not meet the requested probability budget. The exact bound is retained.';
  }
  function refresh() {
    if (!data || !model) return;
    try {
      const result = C.evaluate(data, model, readParameters());
      $('riskFamilyBound').textContent = pretty(result.family_bound);
      $('riskExactRank').textContent = result.rank_value;
      $('riskScanMaximum').textContent = pretty(result.exact_scan_maximum);
      $('riskThresholdRelation').textContent = result.threshold_crossed ? 'At or above the declared threshold' : 'Below the declared threshold';
      $('riskDecision').textContent = summary({result});
      $('riskDecision').dataset.state = result.within_budget ? 'checked' : 'failed-bound';
      $('riskVariance').textContent = model.variance_upper_bound;
      $('riskExactScope').textContent = `Exact finite replay: ${result.calibration_exceedances} exceedances among ${result.calibration_draws} stored maxima; resolution ${result.rank_floor}. The certificate replays real arithmetic on stored binary64 coefficients. The original canvas readout rounds its arithmetic.`;
      status.textContent = 'Exact model bytes and coefficient provenance checked. Probability and finite-rank statements have separate scopes.';
      status.dataset.error = 'false';
    } catch (error) {
      status.textContent = error.message; status.dataset.error = 'true';
      for (const id of ['riskFamilyBound', 'riskExactRank', 'riskScanMaximum', 'riskThresholdRelation']) $(id).textContent = '—';
      $('riskDecision').textContent = 'No certificate is available for these inputs.';
    }
    if (panel) panel.refresh();
  }

  function prepareImport(parameters) {
    const previous = {state: root.CCCLab.getState(), threshold: controls[0].value, order: controls[1].value, alpha: controls[2].value};
    return {
      commit() {
        controls[0].value = parameters.threshold; controls[1].value = parameters.order; controls[2].value = parameters.alpha;
        root.CCCLab.setInjection({center: Number(parameters.center), width: Number(parameters.width), snr: computedNumber(parameters.snr)});
        refresh();
      },
      rollback() {
        controls[0].value = previous.threshold; controls[1].value = previous.order; controls[2].value = previous.alpha;
        root.CCCLab.setInjection(previous.state); refresh();
      }
    };
  }

  async function hash(bytes) {
    const value = await root.crypto.subtle.digest('SHA-256', bytes);
    return Array.from(new Uint8Array(value), x => x.toString(16).padStart(2, '0')).join('');
  }
  async function boundAsset(name, sources) {
    const rel = `extension/site/data/${name}`, expected = sources[rel];
    if (typeof expected !== 'string' || !/^[0-9a-f]{64}$/.test(expected)) throw new Error(`This release has no source binding for ${name}.`);
    const response = await root.fetch(`data/${name}`);
    if (!response.ok) throw new Error(`Exact model request returned HTTP ${response.status}.`);
    const bytes = await response.arrayBuffer(), actual = await hash(bytes);
    if (actual !== expected) throw new Error(`Stale or altered model bytes: ${name}.`);
    return {json: JSON.parse(new TextDecoder().decode(bytes)), sha256: actual};
  }
  async function waitForLab() {
    if (document.documentElement.dataset.cosmologyReady === 'true') return;
    if (document.documentElement.dataset.cosmologyReady === 'error') throw new Error('The synthetic lab is unavailable.');
    await new Promise((resolve, reject) => {
      const ready = () => { root.removeEventListener('grh:cosmology-error', failed); resolve(); };
      const failed = () => { root.removeEventListener('grh:cosmology-ready', ready); reject(new Error('The synthetic lab is unavailable.')); };
      root.addEventListener('grh:cosmology-ready', ready, {once: true});
      root.addEventListener('grh:cosmology-error', failed, {once: true});
    });
  }
  async function initialize() {
    await waitForLab();
    const registry = await root.LabCertificateUI.loadRegistry();
    const binding = registry.contracts && registry.contracts['cosmology-calibration-v1'];
    if (!binding) throw new Error('This release has no compiled cosmology contract.');
    const [dataset, momentModel, factor] = await Promise.all([
      boundAsset('cosmology-synthetic.json', binding.runtime_sources),
      boundAsset('cosmology-moment-model.json', binding.runtime_sources),
      boundAsset('cosmology-noise-factor.json', binding.runtime_sources)
    ]);
    data = dataset.json; model = momentModel.json;
    if (model.dataset_sha256 !== dataset.sha256 || model.factor_sha256 !== factor.sha256)
      throw new Error('The moment model is bound to a different coefficient catalog.');
    root.LabCertificateBridge.setCosmologyAdapter(parameters => C.evaluate(data, model, parameters));
    $('riskControls').disabled = false;
    panel = await root.LabCertificateUI.mount($('cosmologyCertificate'), {
      contract: 'cosmology-calibration-v1', registry, readParameters, prepareImport, summarize: summary
    });
    for (const control of controls) control.addEventListener('input', refresh);
    root.addEventListener('grh:cosmology-update', refresh);
    refresh();
    document.documentElement.dataset.calibrationContractReady = 'true';
  }
  initialize().catch(error => {
    status.textContent = `Exact certificate unavailable: ${error.message}`; status.dataset.error = 'true';
    document.documentElement.dataset.calibrationContractReady = 'error';
    console.error('Cosmology contract:', error);
  });
})(typeof globalThis !== 'undefined' ? globalThis : this);
