/* Shared import/export controls. Imported text never contains executable code. */
(function (root) {
  'use strict';
  const B = typeof module !== 'undefined' && module.exports ? require('./certificate-bridge.js') : root.LabCertificateBridge;
  let registryPromise = null, nextId = 0;
  function transactionalApply(text, registry, contract, adapter) {
    const certificate = B.validate(text, registry, contract);
    const transaction = adapter.prepareImport(certificate.parameters);
    if (!transaction || typeof transaction.commit !== 'function' || typeof transaction.rollback !== 'function')
      throw new TypeError('A reversible prepared control transaction is required.');
    try {
      transaction.commit();
      if (B.stable(adapter.readParameters()) !== B.stable(certificate.parameters))
        throw new Error('The live controls could not restore these exact parameters.');
    } catch (error) {
      transaction.rollback();
      throw error;
    }
    return certificate;
  }
  function loadRegistry() {
    if (!registryPromise) registryPromise = root.fetch('data/certificate-contracts.json', {cache: 'no-cache'}).then(response => {
      if (!response.ok) throw new Error(`Compiled contract registry unavailable (HTTP ${response.status}).`);
      return response.json();
    });
    return registryPromise;
  }
  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function download(name, text, type) {
    const url = URL.createObjectURL(new Blob([text], {type})), link = document.createElement('a');
    link.href = url; link.download = name; link.click();
    root.setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  function defaultSummary(certificate) {
    const result = certificate.result;
    if (certificate.contract === 'hodge-family-v1') return result.positive_gap ? `Positive exact coercivity constant: ${result.coercivity_constant}.` : 'Exact zero boundary: the first coordinate is in the kernel; the positive eigenvalue is 1.';
    if (certificate.contract === 'quadratic-cover-v1') return `Nonzero integer determinant ${result.determinant}; selected point maps exactly to (${result.target_mod_one.join(', ')}).`;
    if (certificate.contract === 'weighted-gain-v1') return result.bound_holds ? (result.certifies_contraction_of_supplied_gain ? 'The supplied gain matrix satisfies the strict contraction bound.' : 'The supplied gain bound holds; its rate does not certify contraction.') : 'The proposed gain bound fails. The replay records its exact negative slack.';
    return 'Exact theorem-contract arithmetic replayed for the displayed inputs.';
  }
  async function mount(container, options) {
    if (!container) throw new TypeError('A certificate panel container is required.');
    const id = `certificate-panel-${++nextId}`;
    container.classList.add('certificate-panel');
    const heading = element('h4', '', 'Live state ↔ exact certificate');
    const explanation = element('p', 'certificate-scope', 'Export the exact parameters, independently replay the evidence, or import a validated instance back into these controls. The browser checks arithmetic against named theorem contracts; it does not run the Lean kernel.');
    const status = element('p', 'certificate-status', 'Loading the compiled theorem bindings…'); status.setAttribute('role', 'status'); status.setAttribute('aria-live', 'polite');
    const result = element('pre', 'certificate-result'); result.setAttribute('aria-label', 'Exact recomputed certificate result');
    const actions = element('div', 'certificate-actions');
    const exportButton = element('button', 'button secondary', 'Export current state');
    const downloadButton = element('button', 'button secondary', 'Download certificate');
    const leanButton = element('button', 'button secondary', 'Download Lean instance');
    for (const button of [exportButton, downloadButton, leanButton]) { button.type = 'button'; button.disabled = true; actions.appendChild(button); }
    const label = element('label', 'certificate-label', 'Certificate JSON to inspect or import'); label.htmlFor = id;
    const input = element('textarea', 'certificate-text'); input.id = id; input.rows = 7; input.spellcheck = false; input.maxLength = B.MAX_TEXT;
    const importButton = element('button', 'button primary', 'Validate and restore controls'); importButton.type = 'button'; importButton.disabled = true;
    const details = element('details', 'certificate-bindings'); details.appendChild(element('summary', '', 'Compiled interfaces and independent replay'));
    const sourceList = element('ul'); details.appendChild(sourceList);
    const command = element('pre', 'certificate-command', 'python3 extension/code/verify_lab_certificate.py certificate.json\ncd extension/lean\nlake build\nlake env lean -DwarningAsError=true LaboratoryInstance.lean'); details.appendChild(command);
    details.appendChild(element('p', 'certificate-scope', 'Source and printed-type hashes identify the reviewed interface. They are provenance, not proof authentication. Save the downloaded LaboratoryInstance.lean in extension/lean, build the pinned project, then run the compiler command above. The source contains fixed templates and validated rational literals only. Numerical canvas residuals and unsupported physical/statistical hypotheses are outside this certificate.'));
    container.replaceChildren(heading, explanation, status, result, actions, label, input, importButton, details);
    let registry, current = null;
    const error = issue => { status.textContent = issue.message || String(issue); status.dataset.state = 'error'; };
    function refresh() {
      if (!registry) return;
      try {
        current = B.create(options.contract, options.readParameters(), registry);
        result.textContent = JSON.stringify(current.result, null, 2);
        status.textContent = (options.summarize || defaultSummary)(current);
        status.dataset.state = current.result.bound_holds === false || current.result.within_budget === false ? 'failed-bound' : 'checked';
        exportButton.disabled = downloadButton.disabled = false;
        try { B.leanSource(current, registry); leanButton.disabled = false; } catch (_) { leanButton.disabled = true; }
      } catch (issue) {
        current = null; exportButton.disabled = downloadButton.disabled = leanButton.disabled = true;
        result.textContent = ''; error(issue);
      }
    }
    function exportText() {
      const certificate = B.create(options.contract, options.readParameters(), registry);
      return JSON.stringify(certificate, null, 2) + '\n';
    }
    function importText(text) {
      const certificate = transactionalApply(text, registry, options.contract, options);
      refresh(); input.value = JSON.stringify(certificate, null, 2) + '\n';
      status.textContent = `Validated and restored exact live parameters. ${(options.summarize || defaultSummary)(certificate)}`;
      return certificate;
    }
    exportButton.addEventListener('click', () => { try { input.value = exportText(); status.textContent = 'Current exact state exported. Changing the controls requires a fresh export.'; } catch (issue) { error(issue); } });
    downloadButton.addEventListener('click', () => { try { download(`${options.contract}.json`, exportText(), 'application/json'); } catch (issue) { error(issue); } });
    leanButton.addEventListener('click', () => { try { download('LaboratoryInstance.lean', B.leanSource(exportText(), registry), 'text/plain'); } catch (issue) { error(issue); } });
    importButton.addEventListener('click', () => { try { importText(input.value); } catch (issue) { error(issue); } });
    try {
      registry = options.registry || await loadRegistry();
      const binding = registry.contracts[options.contract];
      if (!binding) throw new Error('This release has no compiled binding for this contract.');
      for (const theorem of binding.theorems) {
        const item = element('li'), link = element('a', '', theorem.name);
        link.href = theorem.source_url;
        item.append(link, document.createTextNode(` · source ${theorem.source_sha256.slice(0, 12)} · type ${theorem.type_sha256.slice(0, 12)}`));
        sourceList.appendChild(item);
      }
      const lab = element('a', '', 'Open the associated live laboratory'); lab.href = binding.lab_url; details.appendChild(lab);
      details.appendChild(element('p', 'certificate-scope', 'Source links open the current repository branch. The recorded source hash identifies the checked content; a branch URL alone does not authenticate that content.'));
      for (const control of options.watch || []) for (const event of ['input', 'change']) control.addEventListener(event, refresh);
      importButton.disabled = false; refresh();
    } catch (issue) { error(issue); }
    return Object.freeze({refresh, exportText, importText, get registry() { return registry; }});
  }
  const api = Object.freeze({mount, transactionalApply, loadRegistry});
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.LabCertificateUI = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
