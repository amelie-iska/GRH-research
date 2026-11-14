(function () {
  "use strict";
  if (typeof document === "undefined") return;
  const M = window.FluidMath;
  const byId = id => document.getElementById(id);
  const state = M.stateFromSearch(window.location.search);
  const colors = {ink: "#182b29", teal: "#14695e", ochre: "#a65b19", muted: "#596b64", grid: "#d4ddd5", paper: "#fcfdf9"};
  const svgNS = "http://www.w3.org/2000/svg";
  let playing = false, lastFrame = 0, lastDraw = 0, currentHeat = null, saveTimer = null;
  const f = (value, digits = 4) => Number(value).toFixed(digits).replace("-", "−");
  const scientific = value => value === 0 ? "0" : Math.abs(value) >= 0.01 && Math.abs(value) < 10000 ? f(value, 4) : value.toExponential(3).replace("e-", "e−");
  const complexText = z => `${f(z[0], 5)} ${z[1] >= 0 ? "+" : "−"} ${f(Math.abs(z[1]), 5)}i`;
  const setText = (id, text) => { byId(id).textContent = text; };
  function svg(tag, attributes = {}, text = null) {
    const element = document.createElementNS(svgNS, tag);
    for (const [key, value] of Object.entries(attributes)) element.setAttribute(key, value);
    if (text !== null) element.textContent = text;
    return element;
  }
  function stext(parent, x, y, text, className = "f-chart-text", extra = {}) {
    const node = svg("text", {x, y, class: className, ...extra}, text); parent.appendChild(node); return node;
  }
  function fitCanvas(canvas) {
    const rect = canvas.getBoundingClientRect(), w = Math.max(1, rect.width), h = Math.max(1, rect.height), ratio = Math.min(window.devicePixelRatio || 1, 2);
    const bw = Math.round(w * ratio), bh = Math.round(h * ratio);
    if (canvas.width !== bw || canvas.height !== bh) { canvas.width = bw; canvas.height = bh; }
    const ctx = canvas.getContext("2d"); ctx.setTransform(ratio, 0, 0, ratio, 0, 0); ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = colors.paper; ctx.fillRect(0, 0, w, h);
    return {ctx, w, h};
  }
  function blend(from, to, amount) {
    amount = M.clamp(amount, 0, 1);
    return `rgb(${from.map((v, i) => Math.round(v * (1 - amount) + to[i] * amount)).join(",")})`;
  }
  function vortexColor(omega) { return blend([242, 245, 236], omega < 0 ? [20, 105, 94] : [166, 91, 25], Math.abs(omega) / 2 * 0.82); }
  function arrow(ctx, a, b, color = colors.ink, width = 1.2) {
    const dx = b[0] - a[0], dy = b[1] - a[1], length = Math.hypot(dx, dy);
    if (length < 1.2) return;
    const angle = Math.atan2(dy, dx), head = Math.min(4.5, length * 0.45);
    ctx.strokeStyle = color; ctx.lineWidth = width; ctx.beginPath(); ctx.moveTo(...a); ctx.lineTo(...b); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(b[0] - head * Math.cos(angle - 0.5), b[1] - head * Math.sin(angle - 0.5)); ctx.lineTo(...b);
    ctx.lineTo(b[0] - head * Math.cos(angle + 0.5), b[1] - head * Math.sin(angle + 0.5)); ctx.stroke();
  }
  function squareFrame(ctx, w, h, xLabel, yLabel, maxLabel = "1") {
    const side = Math.min(w - 64, h - 52), left = (w - side) / 2 + 7, top = (h - side) / 2 - 6;
    ctx.strokeStyle = colors.grid; ctx.lineWidth = 1; ctx.strokeRect(left, top, side, side);
    ctx.fillStyle = colors.muted; ctx.font = "11px Arial, sans-serif"; ctx.textAlign = "center";
    ctx.fillText("0", left, top + side + 17); ctx.fillText(maxLabel, left + side, top + side + 17);
    ctx.fillText(xLabel, left + side / 2, top + side + 33); ctx.textAlign = "right";
    ctx.fillText("0", left - 8, top + side + 4); ctx.fillText(maxLabel, left - 8, top + 4); ctx.fillText(yLabel, left - 9, top + side / 2);
    return {side, left, top, point: (x, y) => [left + x * side, top + (1 - y) * side]};
  }
  function drawFlow() {
    const {ctx, w, h} = fitCanvas(byId("flowCanvas"));
    if (state.view === "flat") {
      const box = squareFrame(ctx, w, h, "x", "y", "2π"), n = 40;
      for (let j = 0; j < n; j++) for (let i = 0; i < n; i++) {
        const field = M.taylorGreen((i + 0.5) * M.TAU / n, (j + 0.5) * M.TAU / n, state.time, state.nu);
        ctx.fillStyle = vortexColor(field.vorticity);
        ctx.fillRect(box.left + i * box.side / n, box.top + (n - 1 - j) * box.side / n, box.side / n + 0.4, box.side / n + 0.4);
      }
      for (let j = 0; j < 13; j++) for (let i = 0; i < 13; i++) {
        const x = (i + 0.5) / 13, y = (j + 0.5) / 13, field = M.taylorGreen(M.TAU * x, M.TAU * y, state.time, state.nu);
        const a = box.point(x, y), scale = box.side / 13 * 0.74;
        arrow(ctx, [a[0] - field.u * scale / 2, a[1] + field.v * scale / 2], [a[0] + field.u * scale / 2, a[1] - field.v * scale / 2]);
      }
      ctx.strokeStyle = colors.grid; ctx.strokeRect(box.left, box.top, box.side, box.side);
    } else {
      const cy = Math.cos(state.yaw * Math.PI / 180), sy = Math.sin(state.yaw * Math.PI / 180), cp = Math.cos(state.pitch * Math.PI / 180), sp = Math.sin(state.pitch * Math.PI / 180);
      const rotation = p => { const x = cy * p[0] - sy * p[1], y = sy * p[0] + cy * p[1]; return [x, cp * y - sp * p[2], sp * y + cp * p[2]]; };
      const scale = Math.min(w / 6.8, h / 5.7), project = p => [w / 2 + p[0] * scale, h / 2 - p[1] * scale];
      const point = (x, y) => rotation([(2.05 + 0.76 * Math.cos(y)) * Math.cos(x), (2.05 + 0.76 * Math.cos(y)) * Math.sin(x), 0.76 * Math.sin(y)]);
      const elements = [], nx = 56, ny = 24;
      for (let j = 0; j < ny; j++) for (let i = 0; i < nx; i++) {
        const x = i * M.TAU / nx, y = j * M.TAU / ny;
        const vertices = [point(x, y), point(x + M.TAU / nx, y), point(x + M.TAU / nx, y + M.TAU / ny), point(x, y + M.TAU / ny)];
        const field = M.taylorGreen(x + Math.PI / nx, y + Math.PI / ny, state.time, state.nu);
        elements.push({depth: vertices.reduce((a, p) => a + p[2], 0) / 4, vertices, color: vortexColor(field.vorticity)});
      }
      for (let j = 0; j < 12; j++) for (let i = 0; i < 24; i++) {
        const x = (i + 0.5) * M.TAU / 24, y = (j + 0.5) * M.TAU / 12;
        const normal = rotation([Math.cos(x) * Math.cos(y), Math.sin(x) * Math.cos(y), Math.sin(y)]);
        if (normal[2] < 0.1) continue;
        const field = M.taylorGreen(x, y, state.time, state.nu), a = point(x, y), b = point(x + field.u * 0.13, y + field.v * 0.13);
        elements.push({depth: a[2] + 0.04, arrow: [project(a), project(b)]});
      }
      elements.sort((a, b) => a.depth - b.depth);
      for (const item of elements) {
        if (item.arrow) arrow(ctx, ...item.arrow, colors.ink, 1.05);
        else {
          const points = item.vertices.map(project); ctx.beginPath(); ctx.moveTo(...points[0]); points.slice(1).forEach(p => ctx.lineTo(...p)); ctx.closePath();
          ctx.fillStyle = item.color; ctx.fill(); ctx.strokeStyle = "rgba(75,99,83,.12)"; ctx.lineWidth = 0.5; ctx.stroke();
        }
      }
      ctx.font = "11px Arial, sans-serif"; ctx.fillStyle = colors.muted; ctx.textAlign = "center";
      ctx.fillText("Periodic coordinates · flat intrinsic metric", w / 2, h - 17);
    }
    const sample = M.taylorGreen(Math.PI / 2, Math.PI / 2, state.time, state.nu);
    setText("flowEnergy", scientific(sample.energyAverage)); setText("flowVorticity", f(2 * sample.amplitude));
    setText("flowDissipation", scientific(sample.energyDerivative));
    setText("flowSummary", `At t = ${f(state.time, 2)}, ν = ${f(state.nu, 3)}, the amplitude is ${f(sample.amplitude, 4)}. ${state.nu === 0 ? "The inviscid member has constant energy." : "Viscosity decreases the exact mean kinetic energy."}`);
    byId("flowCanvas").setAttribute("aria-label", `Taylor–Green ${state.view} view at time ${f(state.time, 2)}; mean energy ${scientific(sample.energyAverage)}. Arrow keys rotate the torus display.`);
  }
  function drawCover() {
    const data = M.toralFibres(state.power, [state.x, state.y]), {ctx, w, h} = fitCanvas(byId("coverCanvas"));
    const box = squareFrame(ctx, w, h, "x₁", "x₂");
    ctx.strokeStyle = "#e7ece4"; ctx.lineWidth = 0.8;
    for (let k = 1; k < 4; k++) { ctx.beginPath(); ctx.moveTo(box.left + box.side * k / 4, box.top); ctx.lineTo(box.left + box.side * k / 4, box.top + box.side); ctx.stroke(); ctx.beginPath(); ctx.moveTo(box.left, box.top + box.side * k / 4); ctx.lineTo(box.left + box.side, box.top + box.side * k / 4); ctx.stroke(); }
    ctx.fillStyle = "#527d70";
    for (const p of data.points) { const z = box.point(...p); ctx.beginPath(); ctx.arc(...z, state.power === 3 ? 1.3 : state.power === 2 ? 2.1 : 3.4, 0, M.TAU); ctx.fill(); }
    const selected = box.point(...data.point), target = box.point(...data.target);
    ctx.strokeStyle = colors.ochre; ctx.lineWidth = 2.3; ctx.beginPath(); ctx.arc(...selected, 7, 0, M.TAU); ctx.stroke();
    ctx.strokeStyle = colors.teal; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(target[0] - 6, target[1]); ctx.lineTo(target[0] + 6, target[1]); ctx.moveTo(target[0], target[1] - 6); ctx.lineTo(target[0], target[1] + 6); ctx.stroke();
    byId("coverMatrix").replaceChildren(...data.matrix.map(row => { const span = document.createElement("span"); span.textContent = `[ ${row[0]}   ${row[1]} ]`; return span; }));
    setText("coverDegree", data.determinant.toLocaleString()); setText("coverCount", data.points.length.toLocaleString());
    setText("coverTarget", `(${f(data.target[0], 3)}, ${f(data.target[1], 3)})`);
    setText("coverFrequency", `(${data.lifted.join(", ")})`);
    setText("coverCharacter", `Both character evaluations give ${complexText(data.characterImage)}. Numerical difference: ${data.characterError.toExponential(2)}.`);
    byId("coverCanvas").setAttribute("aria-label", `All ${data.points.length} distinct preimages of the image (${f(data.target[0], 3)}, ${f(data.target[1], 3)}) under J to power ${state.power}.`);
  }
  function drawCircuit() {
    const node = byId("fluidCircuit"); node.replaceChildren(svg("title", {}, "Two-qubit diffusivity circuit"));
    const width = Math.max(300, node.getBoundingClientRect().width), compact = width < 620;
    const height = compact ? 180 : 170; node.setAttribute("viewBox", `0 0 ${width} ${height}`);
    const margin = compact ? 40 : 65, right = width - (compact ? 15 : 55), ys = [52, 118];
    const step = (right - margin) / 5, xs = [margin + step * 0.7, margin + step * 1.8, margin + step * 2.85, margin + step * 4];
    ys.forEach((y, i) => { node.appendChild(svg("line", {x1: margin, x2: right, y1: y, y2: y, stroke: colors.muted, "stroke-width": 1})); stext(node, margin - 10, y + 5, `q${i}`, "f-circuit-label", {"text-anchor": "end"}); });
    function gate(x, y, label, angle, fixed = false) {
      const gw = compact ? 39 : 62, gh = 34;
      node.appendChild(svg("rect", {x: x - gw / 2, y: y - gh / 2, width: gw, height: gh, fill: fixed ? "#f7e9d5" : "#e6efea", stroke: fixed ? colors.ochre : colors.teal, rx: 2}));
      stext(node, x, y + 4, label, "f-circuit-label", {"text-anchor": "middle", "font-size": compact ? 11 : 14});
      stext(node, x, y + 31, f(angle, 2), "f-circuit-small", {"text-anchor": "middle"});
    }
    gate(xs[0], ys[0], "Ry", state.angles[0]); gate(xs[1], ys[0], "Rz", state.angles[1]);
    gate(xs[0], ys[1], "Ry", state.angles[2]); gate(xs[1], ys[1], "Rz", state.angles[3]);
    node.appendChild(svg("line", {x1: xs[2], x2: xs[2], y1: ys[0], y2: ys[1], stroke: colors.teal, "stroke-width": 1.6}));
    node.appendChild(svg("circle", {cx: xs[2], cy: ys[0], r: 4, fill: colors.teal}));
    node.appendChild(svg("circle", {cx: xs[2], cy: ys[1], r: 10, fill: colors.paper, stroke: colors.teal, "stroke-width": 1.5}));
    node.appendChild(svg("path", {d: `M${xs[2] - 7} ${ys[1]}h14M${xs[2]} ${ys[1] - 7}v14`, stroke: colors.teal, fill: "none", "stroke-width": 1.5}));
    gate(xs[3], ys[0], "Ry", 0.4, true); gate(xs[3], ys[1], "Ry", -0.3, true);
  }
  function drawHeat() {
    const data = M.circuit(state.angles), gradient = M.circuitGradient(state.angles, 0);
    currentHeat = M.heatTrajectory(data.r, state.steps, state.initial);
    const {ctx, w, h} = fitCanvas(byId("heatCanvas")), box = squareFrame(ctx, w, h, "Periodic position x", "y", "2π");
    const max = Math.max(...currentHeat.initial);
    for (let y = 0; y < M.GRID; y++) for (let x = 0; x < M.GRID; x++) {
      const p = currentHeat.probabilities[y * M.GRID + x]; ctx.fillStyle = blend([242, 245, 236], [18, 83, 75], p / max);
      ctx.fillRect(box.left + x * box.side / M.GRID + 0.3, box.top + (M.GRID - 1 - y) * box.side / M.GRID + 0.3, box.side / M.GRID - 0.6, box.side / M.GRID - 0.6);
    }
    ctx.font = "10px Arial, sans-serif"; ctx.fillStyle = colors.muted; ctx.textAlign = "center";
    ctx.fillText(`Fixed colour range: probability 0 to ${max.toFixed(4)}`, w / 2, 14);
    const last = currentHeat.final, first = currentHeat.history[0];
    setText("fluidCircuitNorm", f(data.norm, 10)); setText("fluidCircuitNu", f(data.nu, 6)); setText("fluidHeatR", f(data.r, 6));
    setText("fluidCircuitGradient", f(gradient.nu, 6)); setText("fluidFeatures", `⟨Z₀⟩ = ${f(data.features[0], 5)} · ⟨Z₁⟩ = ${f(data.features[1], 5)} · ⟨X₀X₁⟩ = ${f(data.features[2], 5)}`);
    setText("heatMass", f(last.mass, 10)); setText("heatEntropy", f(last.entropy, 6)); setText("heatEntropyGain", f(last.entropy - first.entropy, 6)); setText("heatContrast", scientific(last.contrast));
    setText("heatSummary", `${state.steps} steps, elapsed channel time ${f(state.steps * M.STEP_TIME, 1)}. Minimum probability ${scientific(last.min)}. The maximum entropy is 8 bits; the color scale stays fixed to the initial peak.`);
    byId("fluidBasisRows").replaceChildren(...data.probabilities.map((p, i) => {
      const tr = document.createElement("tr"); [i.toString(2).padStart(2, "0"), f(p, 7), complexText(data.amplitudes[i])].forEach((value, j) => { const cell = document.createElement(j ? "td" : "th"); if (!j) cell.scope = "row"; cell.textContent = value; tr.appendChild(cell); }); return tr;
    }));
    byId("heatCanvas").setAttribute("aria-label", `Diagonal position distribution after ${state.steps} channel steps. Mass ${f(last.mass, 10)}, entropy ${f(last.entropy, 5)} bits, contrast ${scientific(last.contrast)}.`);
    drawCircuit(); drawHistory();
  }
  function drawHistory() {
    if (!currentHeat) return;
    const node = byId("heatHistory"), width = Math.max(300, node.getBoundingClientRect().width), narrow = width < 620, height = narrow ? 410 : 230;
    node.setAttribute("viewBox", `0 0 ${width} ${height}`); node.replaceChildren();
    const histories = [{key: "entropy", title: "Entropy (bits)", max: 8, color: colors.teal}, {key: "contrast", title: "Quadratic contrast", max: currentHeat.history[0].contrast * 1.05 || 1, color: colors.ochre}];
    histories.forEach((item, index) => {
      const panelWidth = narrow ? width : width / 2, offsetX = narrow ? 0 : index * panelWidth, offsetY = narrow ? index * 205 : 0;
      const left = offsetX + 57, right = offsetX + panelWidth - 15, top = offsetY + 36, bottom = offsetY + (narrow ? 165 : 180);
      stext(node, left, offsetY + 18, item.title, "f-chart-title");
      for (let i = 0; i < 3; i++) { const value = item.max * i / 2, y = bottom - (bottom - top) * i / 2; node.appendChild(svg("line", {x1: left, x2: right, y1: y, y2: y, stroke: colors.grid, "stroke-width": 0.7})); stext(node, left - 8, y + 4, item.key === "entropy" ? value.toFixed(0) : scientific(value), "f-chart-number", {"text-anchor": "end", "font-size": 10}); }
      const points = currentHeat.history.map((entry, i) => [left + i / Math.max(1, state.steps) * (right - left), bottom - entry[item.key] / item.max * (bottom - top)]);
      node.appendChild(svg("path", {d: points.map((p, i) => `${i ? "L" : "M"}${p[0]} ${p[1]}`).join(" "), fill: "none", stroke: item.color, "stroke-width": 2.1}));
      const last = points[points.length - 1]; node.appendChild(svg("circle", {cx: last[0], cy: last[1], r: 3.3, fill: item.color}));
      stext(node, left, bottom + 19, "0", "f-chart-number"); stext(node, right, bottom + 19, String(state.steps), "f-chart-number", {"text-anchor": "end"});
      stext(node, (left + right) / 2, bottom + 36, "Channel step", "f-chart-text", {"text-anchor": "middle"});
    });
  }
  function drawScaling() {
    const data = M.blowupScaling(state.logTau, state.h), node = byId("scalingPlot"), width = Math.max(300, node.getBoundingClientRect().width), narrow = width < 600, height = narrow ? 350 : 350;
    node.setAttribute("viewBox", `0 0 ${width} ${height}`); node.replaceChildren();
    const left = 48, right = width - 20, top = 42, bottom = 262, xx = log => left + (-log / 18) * (right - left), yy = log => bottom - (log + 10) / 20 * (bottom - top);
    stext(node, left, 19, "log₁₀ of normalized ratio", "f-chart-title");
    for (const tick of [-10, -5, 0, 5, 10]) { node.appendChild(svg("line", {x1: left, x2: right, y1: yy(tick), y2: yy(tick), stroke: tick === 0 ? "#aebeb3" : colors.grid, "stroke-width": tick === 0 ? 1.2 : 0.7})); stext(node, left - 9, yy(tick) + 4, String(tick).replace("-", "−"), "f-chart-number", {"text-anchor": "end"}); }
    for (const tick of [0, -6, -12, -18]) { const x = xx(tick); node.appendChild(svg("line", {x1: x, x2: x, y1: top, y2: bottom, stroke: colors.grid, "stroke-width": 0.6})); stext(node, x, bottom + 19, String(tick).replace("-", "−"), "f-chart-number", {"text-anchor": "middle"}); }
    const series = [{key: "velocity", label: "Velocity", color: colors.ochre, dash: ""}, {key: "radial", label: "Radial length", color: "#6f7d75", dash: "2 3"}, {key: "axial", label: "Axial length", color: "#4a76a1", dash: "7 4"}, {key: "energy", label: "Core energy", color: colors.teal, dash: ""}];
    for (const item of series) {
      node.appendChild(svg("line", {x1: xx(0), y1: yy(0), x2: xx(-18), y2: yy(-18 * data.exponents[item.key]), stroke: item.color, "stroke-width": item.key === "energy" ? 2.5 : 1.6, "stroke-dasharray": item.dash}));
      node.appendChild(svg("circle", {cx: xx(state.logTau), cy: yy(data.logs[item.key]), r: item.key === "velocity" || item.key === "energy" ? 3.5 : 2.5, fill: item.color}));
    }
    node.appendChild(svg("line", {x1: xx(state.logTau), x2: xx(state.logTau), y1: top, y2: bottom, stroke: colors.ink, "stroke-dasharray": "3 4", "stroke-width": 1}));
    stext(node, (left + right) / 2, bottom + 38, "log₁₀ τ  →  approach T", "f-chart-text", {"text-anchor": "middle"});
    series.forEach((item, i) => { const columns = narrow ? 2 : 4, x = left + (i % columns) * (right - left) / columns, y = 321 + Math.floor(i / columns) * 19; node.appendChild(svg("line", {x1: x, x2: x + 18, y1: y - 4, y2: y - 4, stroke: item.color, "stroke-width": 2, "stroke-dasharray": item.dash})); stext(node, x + 23, y, item.label, "f-chart-text", {"font-size": narrow ? 10 : 11}); });
    const rows = [{key: "radial", name: "Radial length", limit: "0"}, {key: "axial", name: "Axial length", limit: "0"}, {key: "velocity", name: "Velocity amplitude", limit: "∞"}, {key: "volume", name: "Core volume", limit: "0"}, {key: "energy", name: "Core energy product", limit: "0"}];
    byId("scalingRows").replaceChildren(...rows.map(item => { const tr = document.createElement("tr"); [item.name, f(data.exponents[item.key], 4), data.values[item.key].toExponential(4).replace("e-", "e−"), item.limit].forEach((text, j) => { const cell = document.createElement(j ? "td" : "th"); if (!j) cell.scope = "row"; cell.textContent = text; tr.appendChild(cell); }); return tr; }));
  }
  const bindings = [
    ["flowTime", "flowTimeOut", "time", 2, drawFlow], ["flowNu", "flowNuOut", "nu", 3, drawFlow],
    ["flowYaw", "flowYawOut", "yaw", 0, drawFlow, "°"], ["flowPitch", "flowPitchOut", "pitch", 0, drawFlow, "°"],
    ["coverPower", "coverPowerOut", "power", 0, drawCover], ["coverX", "coverXOut", "x", 2, drawCover], ["coverY", "coverYOut", "y", 2, drawCover],
    ["heatSteps", "heatStepsOut", "steps", 0, drawHeat], ["scalingTau", "scalingTauOut", "logTau", 1, drawScaling], ["scalingH", "scalingHOut", "h", 4, drawScaling]
  ];
  function updateControls() {
    for (const [id, out, key, digits, , suffix = ""] of bindings) { byId(id).value = state[key]; setText(out, f(state[key], digits) + suffix); }
    for (let i = 0; i < 4; i++) { byId("fluidTheta" + i).value = state.angles[i]; setText("fluidTheta" + i + "Out", f(state.angles[i], 2)); }
    byId("flowView").value = state.view; byId("heatInitial").value = state.initial;
    byId("flowYaw").disabled = state.view === "flat"; byId("flowPitch").disabled = state.view === "flat";
  }
  function saveState() { clearTimeout(saveTimer); saveTimer = setTimeout(() => { history.replaceState(null, "", M.stateToSearch(state) + window.location.hash); }, 200); }
  function all() { updateControls(); drawFlow(); drawCover(); drawHeat(); drawScaling(); }
  for (const [id, out, key, digits, render, suffix = ""] of bindings) {
    byId(id).addEventListener("input", () => { state[key] = Number(byId(id).value); setText(out, f(state[key], digits) + suffix); render(); saveState(); });
  }
  for (let i = 0; i < 4; i++) byId("fluidTheta" + i).addEventListener("input", () => { state.angles[i] = Number(byId("fluidTheta" + i).value); setText("fluidTheta" + i + "Out", f(state.angles[i], 2)); drawHeat(); saveState(); });
  byId("flowView").addEventListener("change", event => { state.view = event.target.value; updateControls(); drawFlow(); saveState(); });
  byId("heatInitial").addEventListener("change", event => { state.initial = event.target.value; drawHeat(); saveState(); });
  function stop() { playing = false; byId("playFlow").setAttribute("aria-pressed", "false"); setText("playFlow", "Animate time"); }
  byId("playFlow").addEventListener("click", () => {
    playing = !playing; byId("playFlow").setAttribute("aria-pressed", String(playing)); setText("playFlow", playing ? "Pause animation" : "Animate time");
    lastFrame = performance.now(); if (playing) requestAnimationFrame(animate); else saveState();
  });
  function animate(now) {
    if (!playing) return;
    const elapsed = Math.min((now - lastFrame) / 1000, 0.1); lastFrame = now;
    state.time = Math.min(12, state.time + elapsed * 0.65);
    if (now - lastDraw > 45) { updateControls(); drawFlow(); lastDraw = now; }
    if (state.time >= 12) { stop(); saveState(); } else requestAnimationFrame(animate);
  }
  byId("flowOrigin").addEventListener("click", () => { stop(); state.time = 0; updateControls(); drawFlow(); saveState(); });
  byId("heatStep").addEventListener("click", () => { state.steps = Math.min(128, state.steps + 1); updateControls(); drawHeat(); saveState(); });
  byId("heatReset").addEventListener("click", () => { state.steps = 0; updateControls(); drawHeat(); saveState(); });
  byId("resetFluid").addEventListener("click", () => { stop(); Object.assign(state, M.stateFromSearch("")); all(); saveState(); setText("fluidStatus", "All four laboratories reset to their documented defaults."); });
  byId("copyFluidLink").addEventListener("click", async () => {
    const url = new URL(window.location.href); url.search = M.stateToSearch(state); history.replaceState(null, "", url.search + url.hash);
    try { await navigator.clipboard.writeText(url.href); setText("fluidStatus", "Configuration link copied. It restores every displayed control."); }
    catch { setText("fluidStatus", "The address bar now contains this configuration; copy that address to share it."); }
  });
  const flowCanvas = byId("flowCanvas"); let drag = null;
  flowCanvas.addEventListener("pointerdown", event => { if (state.view !== "torus" || event.button !== 0) return; drag = {id: event.pointerId, x: event.clientX, y: event.clientY, yaw: state.yaw, pitch: state.pitch}; flowCanvas.setPointerCapture(event.pointerId); });
  flowCanvas.addEventListener("pointermove", event => { if (!drag || event.pointerId !== drag.id) return; state.yaw = M.clamp(drag.yaw + (event.clientX - drag.x) * 0.55, -180, 180); state.pitch = M.clamp(drag.pitch + (event.clientY - drag.y) * 0.35, -75, 75); updateControls(); drawFlow(); });
  for (const eventName of ["pointerup", "pointercancel", "lostpointercapture"]) flowCanvas.addEventListener(eventName, () => { if (drag) { drag = null; saveState(); } });
  flowCanvas.addEventListener("keydown", event => { if (state.view !== "torus" || !["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"].includes(event.key)) return; event.preventDefault(); if (event.key === "ArrowLeft") state.yaw = M.clamp(state.yaw - 5, -180, 180); if (event.key === "ArrowRight") state.yaw = M.clamp(state.yaw + 5, -180, 180); if (event.key === "ArrowUp") state.pitch = M.clamp(state.pitch + 5, -75, 75); if (event.key === "ArrowDown") state.pitch = M.clamp(state.pitch - 5, -75, 75); updateControls(); drawFlow(); saveState(); });
  document.addEventListener("visibilitychange", () => { if (document.hidden) stop(); });
  window.addEventListener("popstate", () => { stop(); Object.assign(state, M.stateFromSearch(window.location.search)); all(); });
  let resizeQueued = false;
  const observer = new ResizeObserver(() => { if (!resizeQueued) { resizeQueued = true; requestAnimationFrame(() => { resizeQueued = false; drawFlow(); drawCover(); drawCircuit(); drawHistory(); drawScaling(); if (currentHeat) drawHeat(); }); } });
  for (const id of ["flowCanvas", "coverCanvas", "heatCanvas", "fluidCircuit", "heatHistory", "scalingPlot"]) observer.observe(byId(id));
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)");
  reduced.addEventListener("change", event => { if (event.matches) stop(); });
  all();
  fetch("data/fluids-reference.json").then(response => { if (!response.ok) throw new Error("Reference file unavailable"); return response.json(); }).then(data => {
    if (data.schema !== "fluid-reference-v1") throw new Error("Reference schema mismatch");
    const summary = data.summary;
    setText("fluidVerificationSummary", `${summary.cochain_grids} periodic cochain grids; four symbolic flow residuals equal zero; ${summary.circuit_cases} independent complex128 circuit references. Maximum parameter-shift / finite-difference feature error ${summary.feature_gradient_error.toExponential(2)}. A separate ${summary.coherent_channel_dimension}-dimensional coherent density matrix checks the channel beyond diagonal states.`);
  }).catch(() => { setText("fluidVerificationSummary", "The live models remain available. Open the linked reference JSON to inspect the independently recorded checks; it could not be fetched in this browser context."); });
}());
