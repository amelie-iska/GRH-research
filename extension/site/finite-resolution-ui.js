/* Accessible numerical diagnostics. These panels do not issue Lean certificates. */
(function (root, factory) {
  "use strict";
  const api = factory(root, typeof module === "object" && module.exports ? require("./finite-resolution-core.js") : root.ResolutionMath);
  if (typeof module === "object" && module.exports) module.exports = api;
  else {
    root.ResolutionUI = api;
    if (root.document.readyState === "loading") root.document.addEventListener("DOMContentLoaded", () => api.mountAll());
    else api.mountAll();
  }
}(typeof globalThis !== "undefined" ? globalThis : this, function (root, R) {
  "use strict";
  let nextId = 0;
  const FAMILIES = {
    "taylor-green": {
      title: "Resolution audit: Taylor–Green sampling",
      description: "Sample the same analytic solution on three periodic grids. Central spatial differences estimate its curl and nonlinear equation residual; time differentiation remains analytic. These controls are independent of the animated view.",
      fields: [["start", "Starting grid n", 8, [8, 16, 32]], ["time", "Time t", 1.5, 0, 1000], ["nu", "Viscosity ν", 0.08, 0, 100]],
      assumptions: "The domain has side length 2π, h = 2π/n, and n ≥ 5 resolves both velocity frequency 1 and pressure frequency 2. The curl and componentwise nonlinear-residual bounds scale as h² for fixed t and ν. Uniform energy quadrature is exact in real arithmetic for this particular Fourier family. This is a derivative audit of an analytic solution, not a time-marching Navier–Stokes solver."
    },
    "heat-mode": {
      title: "Resolution audit: heat at fixed physical time",
      description: "Compare a smooth Fourier stripe at the same final time on three grids. The diagnostic refines its own time step with h²; it does not reinterpret the point or peak fixtures as a fixed smooth continuum field.",
      fields: [["start", "Starting grid n", 8, [8, 16, 32]], ["time", "Final time T", 1, 0, 1000], ["nu", "Viscosity ν", 0.08, 0, 100], ["modeX", "Integer frequency kₓ", 1, -63, 63, 1], ["modeY", "Integer frequency kᵧ", 0, -63, 63, 1]],
      assumptions: "The domain has side length 2π. Each frequency must be strictly below every grid's Nyquist frequency: |kₓ|, |kᵧ| < n/2. Automatic step counts keep νΔt/h² ≤ 1/5, within the channel's 1/4 positivity limit. The actual heatStep kernel is checked for one step; the final amplitude is evaluated from its exact discrete Fourier symbol. Spatial and time errors may cancel, so their observed total-error rate need not resemble 2 at each refinement."
    },
    "u1-plaquette": {
      title: "Resolution audit: a declared local U(1) family",
      description: "Use a centered cell of side h = 1/n inside a unit-square patch, with curvature B(x,y) = B₀ + κ(x² + y²). This new smooth family supplies the spacing absent from the original single-plaquette slider.",
      fields: [["start", "Starting refinement n", 1, [1, 2, 4, 8, 16, 256, 1024, 4096, 16384]], ["curvature", "Central curvature B₀", 1, -10000, 10000], ["quadratic", "Quadratic variation κ", 0, -10000, 10000]],
      assumptions: "The flux is the exact cell integral, Φ = h²(B₀ + κh²/6). The stable density is 4 sin²(Φ/2)/h⁴; the raw density reuses the existing product of four link phases and its subtraction 1 − Re W. Both represent 2(1 − cos Φ)/h⁴ in real arithmetic. The bound combines cell averaging with the small-angle error; it is O(h⁴) for κ = 0 and generally O(h²) otherwise. Large flux retains a 2π ambiguity, and a single shrinking cell supplies no global bundle or continuum mass-gap theorem."
    }
  };
  function formatNumber(value) {
    if (!Number.isFinite(value)) return "unavailable";
    if (value === 0) return "0";
    const a = Math.abs(value);
    return a < 0.001 || a >= 10000 ? value.toExponential(3) : Number(value.toPrecision(5)).toString();
  }
  function tableRows(report) {
    return report.rows.map(row => ({
      n: String(row.n), h: formatNumber(row.h), error: formatNumber(row.error), bound: formatNumber(row.bound),
      order: row.observedOrder === null ? (row.orderStatus === "needs-two-levels" ? "—" : "Unresolved") : row.observedOrder.toFixed(3),
      status: row.errorStatus === "reference-underflow" ? "Reference underflow" : row.errorStatus === "unresolved-at-rounding-scale" ? "At rounding scale" : "Numerically resolved"
    }));
  }
  function element(doc, tag, className, text) {
    const node = doc.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function installStyles(doc) {
    if (doc.getElementById("finite-resolution-style")) return;
    const style = element(doc, "style"); style.id = "finite-resolution-style";
    style.textContent = ".resolution-lab{margin:24px 0;padding:22px;border:1px solid var(--line,#d4ddd5);background:var(--soft,#edf1eb);color:var(--ink,#182b29);font-size:13px;line-height:1.7}.resolution-lab h4{font-size:17px;margin:0 0 10px}.resolution-lab p{margin:10px 0}.resolution-controls{display:flex;gap:14px 20px;flex-wrap:wrap;border:0;padding:0;margin:18px 0}.resolution-controls legend{font-weight:700;padding:0 0 9px}.resolution-control{display:flex;flex-direction:column;gap:5px;max-width:100%;font-size:12px}.resolution-control input,.resolution-control select{min-height:40px;width:145px;max-width:100%;border:1px solid var(--line,#d4ddd5);background:var(--white,#fff);color:inherit;padding:6px 9px}.resolution-status{font-weight:700}.resolution-alert{border-left:3px solid var(--ochre,#a65b19);padding-left:12px}.resolution-table-wrap{overflow-x:auto;margin:18px 0}.resolution-table{border-collapse:collapse;min-width:560px;width:100%;font-size:12px}.resolution-table th,.resolution-table td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--line,#d4ddd5)}.resolution-table th{font-weight:700}.resolution-table caption{text-align:left;margin-bottom:9px;color:var(--muted,#596b64)}.resolution-metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(155px,1fr));gap:14px;margin:18px 0}.resolution-metrics>div{min-width:0}.resolution-metrics dt{font-size:11px;color:var(--muted,#596b64)}.resolution-metrics dd{font-family:var(--mono,monospace);margin:4px 0 0;overflow-wrap:anywhere}.resolution-notes{margin:16px 0}.resolution-notes summary{cursor:pointer;font-weight:700}.resolution-links{display:flex;gap:12px 22px;flex-wrap:wrap}.resolution-lab [hidden]{display:none!important}@media(max-width:580px){.resolution-lab{padding:15px}.resolution-control{flex:1 1 120px}.resolution-control input,.resolution-control select{width:100%}.resolution-metrics{grid-template-columns:1fr 1fr}}";
    doc.head.appendChild(style);
  }
  function mount(container) {
    if (!container || !container.ownerDocument) throw new TypeError("A diagnostic container is required.");
    if (container.resolutionPanel) return container.resolutionPanel;
    const doc = container.ownerDocument, family = container.dataset.resolutionLab, spec = FAMILIES[family];
    if (!spec) throw new RangeError("Unknown finite-resolution panel family.");
    if (!R) throw new Error("Finite-resolution core is unavailable.");
    installStyles(doc); container.classList.add("resolution-lab");
    const prefix = "resolution-" + (++nextId), controls = Object.create(null);
    const heading = element(doc, "h4", "", spec.title), intro = element(doc, "p", "", spec.description);
    const scope = element(doc, "p", "", "Analytic bounds concern real arithmetic. The displayed numbers are floating-point evaluations; their rounding indicators are heuristic. This panel does not issue a Lean certificate.");
    const fields = element(doc, "fieldset", "resolution-controls"); fields.appendChild(element(doc, "legend", "", "Diagnostic family parameters"));
    for (const [key, label, value, min, max, step] of spec.fields) {
      const wrapper = element(doc, "label", "resolution-control", label), control = element(doc, Array.isArray(min) ? "select" : "input");
      control.id = prefix + "-" + key; wrapper.htmlFor = control.id;
      if (Array.isArray(min)) for (const number of min) { const option = element(doc, "option", "", String(number)); option.value = String(number); control.appendChild(option); }
      else { control.type = "number"; control.min = String(min); control.max = String(max); control.step = step === undefined ? "any" : String(step); control.required = true; }
      control.value = String(value); controls[key] = control; wrapper.appendChild(control); fields.appendChild(wrapper);
    }
    const button = element(doc, "button", "button secondary", "Recompute refinement"); button.type = "button";
    const status = element(doc, "p", "resolution-status"); status.setAttribute("role", "status"); status.setAttribute("aria-live", "polite");
    const alert = element(doc, "p", "resolution-alert"); alert.setAttribute("role", "alert"); alert.hidden = true;
    const result = element(doc, "div", "resolution-result");
    const notes = element(doc, "details", "resolution-notes"); notes.appendChild(element(doc, "summary", "", "Assumptions and interpretation")); notes.appendChild(element(doc, "p", "", spec.assumptions));
    notes.appendChild(element(doc, "p", "", "An observed rate is log(error on the coarser grid / error on the finer grid) divided by log of the refinement factor. It is withheld when either error is at the heuristic rounding scale or the reference underflows. A zero in floating arithmetic is not evidence of zero analytic truncation error. Model mismatch, uncertain parameters and an unproved continuum limit are separate from the listed truncation budget."));
    const links = element(doc, "p", "resolution-links");
    for (const [href, text] of [["verification/finite-resolution-node.json", "Numerical verification record"], ["verification/finite-resolution-20261113.md", "Derivations and source scope"], ["downloads/fluid-extension.pdf", "Fluid extension PDF"]]) {
      const link = element(doc, "a", "", text); link.href = href; links.appendChild(link);
    }
    container.replaceChildren(heading, intro, scope, fields, button, status, alert, result, notes, links);
    let report = null;
    function metric(parent, label, value) {
      const pair = element(doc, "div"); pair.appendChild(element(doc, "dt", "", label)); pair.appendChild(element(doc, "dd", "", typeof value === "string" ? value : formatNumber(value))); parent.appendChild(pair);
    }
    function refresh() {
      try {
        const parameters = {};
        for (const key of Object.keys(controls)) {
          if (!controls[key].value.trim()) throw new RangeError("Enter a value for every diagnostic parameter.");
          parameters[key] = Number(controls[key].value);
        }
        const start = parameters.start; delete parameters.start;
        report = R.convergenceStudy(family, parameters, [start, start * 2, start * 4]);
        const last = report.rows[report.rows.length - 1], tableWrap = element(doc, "div", "resolution-table-wrap"), table = element(doc, "table", "resolution-table");
        table.appendChild(element(doc, "caption", "", family === "taylor-green" ? "Maximum curl error at fixed time" : family === "heat-mode" ? "Fourier-amplitude error at fixed physical time" : "Stable action-density error relative to B₀²"));
        const thead = element(doc, "thead"), headRow = element(doc, "tr");
        for (const title of ["n", "Cell size h", "Observed error", "Analytic bound", "Observed rate", "Numerical status"]) { const cell = element(doc, "th", "", title); cell.scope = "col"; headRow.appendChild(cell); }
        thead.appendChild(headRow); table.appendChild(thead);
        const tbody = element(doc, "tbody");
        for (const row of tableRows(report)) { const tr = element(doc, "tr"); for (const key of ["n", "h", "error", "bound", "order", "status"]) tr.appendChild(element(doc, "td", "", row[key])); tbody.appendChild(tr); }
        table.appendChild(tbody); tableWrap.appendChild(table);
        const metrics = element(doc, "dl", "resolution-metrics"); metric(metrics, "Finest grid n", last.n); metric(metrics, "Heuristic rounding scale", last.roundingHeuristic);
        if (family === "taylor-green") {
          metric(metrics, "Nonlinear residual (max component)", last.pdeResidual); metric(metrics, "Nonlinear residual bound", last.pdeBound);
          metric(metrics, "Energy quadrature error", last.energyError); metric(metrics, "Divergence residual", last.divergence);
        } else if (family === "heat-mode") {
          metric(metrics, "Spatial amplitude error", last.spatialError); metric(metrics, "Spatial bound", last.spatialBound);
          metric(metrics, "Time amplitude error", last.timeError); metric(metrics, "Time bound", last.timeBound);
          metric(metrics, "Steps at fixed final time", last.steps); metric(metrics, "CFL νΔt/h²", last.r);
          metric(metrics, "One-step kernel residual", last.oneStepKernelResidual); metric(metrics, "Discrete amplitude", last.discreteAmplitude);
          metric(metrics, "Continuum generator gap (L = 2π)", last.continuumGeneratorGap); metric(metrics, "Grid generator gap (L = 2π)", last.discreteGeneratorGap);
        } else {
          metric(metrics, "Raw action density", last.rawDensity); metric(metrics, "Stable action density", last.stableDensity); metric(metrics, "Target B₀²", last.targetDensity);
          metric(metrics, "Raw density error", last.rawError); metric(metrics, "Cell-averaging bound", last.midpointBound); metric(metrics, "Small-angle bound", last.smallAngleBound);
          metric(metrics, "Raw rounding-scale heuristic", last.rawRoundingHeuristic); metric(metrics, "Cell flux Φ", last.flux);
        }
        const messages = [];
        if (report.rows.some(row => row.phaseAliased)) messages.push("At least one cell has |Φ| ≥ π: its principal phase does not determine an unwrapped curvature.");
        if (report.rows.some(row => row.cancellationDetected || row.rawActionNegative)) messages.push("The raw link-product action shows loss of significance; inspect the stable evaluation and the raw error separately.");
        if (report.rows.some(row => row.negativeModeMultiplier)) messages.push("A stable negative Fourier multiplier changes the mode's sign; positivity of the full channel is a different condition.");
        if (family === "heat-mode") messages.push("Spatial and time errors can cancel. The separate error budgets remain meaningful when the total-error rate is irregular.");
        if (report.rows.some(row => row.errorStatus !== "numerically-resolved")) messages.push("At least one error is unresolved at the rounding scale or its reference underflows; no rate is inferred there.");
        result.replaceChildren(tableWrap, metrics);
        if (messages.length) result.appendChild(element(doc, "p", "resolution-alert", messages.join(" ")));
        status.textContent = "Three-grid diagnostic evaluated. Analytic hypotheses and numerical checks remain separate.";
        status.dataset.state = "evaluated"; alert.textContent = ""; alert.hidden = true;
      } catch (error) {
        report = null; result.replaceChildren(); status.textContent = "No diagnostic displayed for these parameters."; status.dataset.state = "invalid";
        alert.textContent = error.message || String(error); alert.hidden = false;
      }
      return report;
    }
    for (const control of Object.values(controls)) control.addEventListener("change", refresh);
    button.addEventListener("click", refresh);
    const panel = {refresh, controls, getReport: () => report}; container.resolutionPanel = panel; refresh(); return panel;
  }
  function mountAll(doc = root.document) {
    const panels = [];
    for (const node of doc.querySelectorAll("[data-resolution-lab]")) {
      try { panels.push(mount(node)); }
      catch (error) { node.textContent = "Resolution diagnostic unavailable: " + (error.message || String(error)); node.setAttribute("role", "alert"); }
    }
    return panels;
  }
  return {mount, mountAll, formatNumber, tableRows};
}));
