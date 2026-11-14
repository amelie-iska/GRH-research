(function (global) {
  "use strict";

  const DEFAULT_STATE = Object.freeze({center: 0, width: 1, snr: 0, view: "sphere", yaw: -25, pitch: 15});
  const WIDTHS = Object.freeze([0.18, 0.30, 0.45]);
  const SVG_NS = "http://www.w3.org/2000/svg";
  const RAD = Math.PI / 180;

  function dot(a, b) {
    let value = 0;
    for (let i = 0; i < a.length; i += 1) value += a[i] * b[i];
    return value;
  }

  // Q(x) = Gamma(1/2,x^2/2)/(2 Gamma(1/2)). Use the convergent
  // lower-gamma series at small argument and the upper-gamma continued
  // fraction at larger argument. This avoids subtracting tiny upper tails.
  function normalUpperTail(x) {
    if (Number.isNaN(x)) throw new TypeError("A normal score must be a number.");
    if (x === Infinity) return 0;
    if (x === -Infinity) return 1;
    if (x < 0) return 1 - normalUpperTail(-x);
    if (x === 0) return 0.5;
    const z = x * x / 2;
    const a = 0.5;
    const factor = Math.exp(-z + a * Math.log(z) - 0.5 * Math.log(Math.PI));
    if (z < 1.5) {
      let term = 1 / a;
      let sum = term;
      for (let n = 1; n < 300; n += 1) {
        term *= z / (a + n);
        sum += term;
        if (Math.abs(term) <= Math.abs(sum) * 2e-16) break;
      }
      return Math.max(0, Math.min(1, 0.5 * (1 - factor * sum)));
    }
    const tiny = 1e-300;
    let b = z + 1 - a;
    let c = 1 / tiny;
    let d = 1 / b;
    let h = d;
    for (let n = 1; n < 500; n += 1) {
      const coefficient = -n * (n - a);
      b += 2;
      d = coefficient * d + b;
      if (Math.abs(d) < tiny) d = tiny;
      c = b + coefficient / c;
      if (Math.abs(c) < tiny) c = tiny;
      d = 1 / d;
      const change = d * c;
      h *= change;
      if (Math.abs(change - 1) < 4e-16) break;
    }
    return Math.max(0, Math.min(1, 0.5 * factor * h));
  }

  function rankProbability(sortedCalibration, value) {
    if (!Number.isFinite(value) || !sortedCalibration.length) throw new RangeError("A finite score and a nonempty calibration are required.");
    let low = 0;
    let high = sortedCalibration.length;
    while (low < high) {
      const middle = (low + high) >>> 1;
      if (sortedCalibration[middle] < value) low = middle + 1;
      else high = middle;
    }
    const exceedances = sortedCalibration.length - low;
    return {exceedances, p: (1 + exceedances) / (sortedCalibration.length + 1)};
  }

  function bounded(value, minimum, maximum, fallback, integer) {
    if (value === null || value === undefined || value === "") return fallback;
    const number = Number(value);
    if (!Number.isFinite(number)) return fallback;
    const clipped = Math.min(maximum, Math.max(minimum, number));
    return integer ? Math.round(clipped) : clipped;
  }

  function normalizeState(raw) {
    return {
      center: bounded(raw.center, 0, 95, DEFAULT_STATE.center, true),
      width: bounded(raw.width, 0, 2, DEFAULT_STATE.width, true),
      snr: Math.round(10 * bounded(raw.snr, 0, 6, DEFAULT_STATE.snr, false)) / 10,
      view: raw.view === "flat" ? "flat" : "sphere",
      yaw: bounded(raw.yaw, -180, 180, DEFAULT_STATE.yaw, true),
      pitch: bounded(raw.pitch, -90, 90, DEFAULT_STATE.pitch, true)
    };
  }

  function stateFromSearch(search) {
    const parameters = new URLSearchParams(search);
    return normalizeState({center: parameters.get("center"), width: parameters.get("width"),
      snr: parameters.get("snr"), view: parameters.get("view"), yaw: parameters.get("yaw"), pitch: parameters.get("pitch")});
  }

  function stateToSearch(state) {
    const s = normalizeState(state);
    const parameters = new URLSearchParams();
    for (const key of ["center", "width", "snr", "view", "yaw", "pitch"]) parameters.set(key, String(s[key]));
    return parameters.toString();
  }

  function validateDataset(data) {
    if (data.schema !== "ccc-synthetic-browser-v1") throw new Error("Unsupported synthetic-data schema.");
    const configuration = data.benchmark && data.benchmark.configuration;
    if (!configuration || configuration.points !== 96 || configuration.template_count !== 288 || configuration.calibration_draws !== 4095) {
      throw new Error("The dataset does not match the declared finite model.");
    }
    const vector = (v, n) => Array.isArray(v) && v.length === n && v.every(Number.isFinite);
    if (!Array.isArray(data.points) || data.points.length !== 96 || !data.points.every(p => vector(p, 3) && Math.abs(dot(p, p) - 1) < 1e-12)) {
      throw new Error("Invalid sphere directions.");
    }
    if (!vector(data.base_sky, 96)) throw new Error("Invalid base sky.");
    for (const name of ["normalized_injection_templates", "filter_weights"]) {
      if (!Array.isArray(data[name]) || data[name].length !== 288 || !data[name].every(v => vector(v, 96))) throw new Error("Invalid template or filter matrix.");
    }
    if (!Array.isArray(data.labels) || data.labels.length !== 288 || !data.labels.every((label, i) => label.center_index === Math.floor(i / 3) && label.width_rad === WIDTHS[i % 3])) {
      throw new Error("Unexpected template ordering.");
    }
    const calibration = data.calibration_maxima_sorted;
    if (!vector(calibration, 4095) || calibration.some((x, i) => i > 0 && x < calibration[i - 1])) throw new Error("Invalid sorted calibration record.");
    if (!Array.isArray(data.benchmark.experiments) || data.benchmark.experiments.length !== 4) throw new Error("Missing fixed benchmark.");
    return true;
  }

  function evaluate(data, rawState) {
    const state = normalizeState(rawState);
    const injectionIndex = state.center * 3 + state.width;
    const injection = data.normalized_injection_templates[injectionIndex];
    const sky = data.base_sky.map((x, i) => x + state.snr * injection[i]);
    const scores = data.filter_weights.map(filter => dot(filter, sky));
    let winner = 0;
    for (let j = 1; j < scores.length; j += 1) if (scores[j] > scores[winner]) winner = j;
    const maximum = scores[winner];
    const calibration = rankProbability(data.calibration_maxima_sorted, maximum);
    return {state, sky, scores, injectionIndex, winner, maximum,
      fixedScore: scores[injectionIndex], fixedLocalP: normalUpperTail(scores[injectionIndex]),
      selectedLocalP: normalUpperTail(maximum), globalP: calibration.p, exceedances: calibration.exceedances};
  }

  function rotatePoint(point, yawDegrees, pitchDegrees) {
    const yaw = yawDegrees * RAD;
    const pitch = pitchDegrees * RAD;
    const x = Math.cos(yaw) * point[0] + Math.sin(yaw) * point[2];
    const z = -Math.sin(yaw) * point[0] + Math.cos(yaw) * point[2];
    return [x, Math.cos(pitch) * point[1] - Math.sin(pitch) * z,
      Math.sin(pitch) * point[1] + Math.cos(pitch) * z];
  }

  function facePoint(point) {
    const yaw = Math.atan2(-point[0], point[2]) / RAD;
    const pitch = Math.atan2(point[1], Math.hypot(point[0], point[2])) / RAD;
    return {yaw, pitch};
  }

  function longitudeLatitude(point) {
    return [Math.atan2(point[1], point[0]) / RAD, Math.asin(Math.max(-1, Math.min(1, point[2]))) / RAD];
  }

  function histogram(values, binCount, minimum, maximum) {
    const counts = Array(binCount).fill(0);
    const step = (maximum - minimum) / binCount;
    if (!(step > 0)) throw new RangeError("Histogram domain must be increasing.");
    let outside = 0;
    for (const value of values) {
      if (value < minimum || value > maximum) {outside += 1; continue;}
      counts[Math.min(binCount - 1, Math.floor((value - minimum) / step))] += 1;
    }
    return {counts, step, outside};
  }

  function formatP(p) {
    return p < 0.0001 ? p.toExponential(3) : p.toFixed(6);
  }

  function sampleColor(value) {
    const neutral = [237, 241, 235];
    const target = value < 0 ? [20, 105, 94] : [166, 91, 25];
    const weight = Math.min(1, Math.abs(value) / 6);
    return "rgb(" + neutral.map((v, i) => Math.round(v + weight * (target[i] - v))).join(",") + ")";
  }

  const api = {DEFAULT_STATE, WIDTHS, dot, normalUpperTail, rankProbability, normalizeState,
    stateFromSearch, stateToSearch, validateDataset, evaluate, rotatePoint, facePoint, longitudeLatitude, histogram, formatP};
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  global.CCCMath = api;
  if (!global.document) return;

  const $ = id => document.getElementById(id);
  function svgElement(name, attributes, text) {
    const element = document.createElementNS(SVG_NS, name);
    for (const [key, value] of Object.entries(attributes || {})) element.setAttribute(key, String(value));
    if (text !== undefined) element.textContent = text;
    return element;
  }
  function add(parent, name, attributes, text) {
    const element = svgElement(name, attributes, text);
    parent.appendChild(element);
    return element;
  }
  function line(parent, x1, y1, x2, y2, extra) {
    return add(parent, "line", {x1, y1, x2, y2, stroke: "#d9e3da", "stroke-width": 1, ...extra});
  }
  function setSVG(svg, width, height, titleId, descriptionId, title, description) {
    svg.replaceChildren();
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    svg.style.height = `${height}px`;
    add(svg, "title", {id: titleId}, title);
    add(svg, "desc", {id: descriptionId}, description);
  }

  let data = null;
  let state = stateFromSearch(global.location.search);
  let current = null;

  function drawMap() {
    if (!current) return;
    const svg = $("skyMap");
    const width = Math.max(260, svg.parentElement.clientWidth);
    const height = state.view === "sphere" ? Math.min(430, Math.max(290, width * 0.76)) : Math.min(330, Math.max(240, width * 0.53));
    setSVG(svg, width, height, "skyMapTitle", "skyMapDescription", "96 synthetic Gaussian-sky samples",
      `Synthetic data, not observed CMB. Injected center ${state.center}, width ${WIDTHS[state.width]} radians, matched SNR ${state.snr}. Winning filter center ${data.labels[current.winner].center_index}.`);
    const projected = [];
    if (state.view === "sphere") {
      const cx = width / 2;
      const cy = height / 2 - 3;
      const radius = Math.min(width * 0.43, height * 0.44);
      add(svg, "circle", {cx, cy, r: radius, fill: "#f0f5ed", stroke: "#afc3b7", "stroke-width": 1});
      const curve = points => {
        let path = "";
        let connected = false;
        for (const point of points) {
          const p = rotatePoint(point, state.yaw, state.pitch);
          if (p[2] < 0) {connected = false; continue;}
          path += `${connected ? "L" : "M"}${(cx + radius * p[0]).toFixed(2)},${(cy - radius * p[1]).toFixed(2)} `;
          connected = true;
        }
        add(svg, "path", {d: path, fill: "none", stroke: "#d4e0d5", "stroke-width": 0.8});
      };
      for (const latitude of [-60, -30, 0, 30, 60]) {
        const lat = latitude * RAD;
        curve(Array.from({length: 181}, (_, j) => {const lon = 2 * Math.PI * j / 180; return [Math.cos(lat) * Math.cos(lon), Math.cos(lat) * Math.sin(lon), Math.sin(lat)];}));
      }
      for (const longitude of [0, 45, 90, 135, 180, 225, 270, 315]) {
        const lon = longitude * RAD;
        curve(Array.from({length: 91}, (_, j) => {const lat = -Math.PI / 2 + Math.PI * j / 90; return [Math.cos(lat) * Math.cos(lon), Math.cos(lat) * Math.sin(lon), Math.sin(lat)];}));
      }
      data.points.forEach((point, i) => {
        const p = rotatePoint(point, state.yaw, state.pitch);
        if (p[2] >= -1e-12) projected.push({index: i, x: cx + radius * p[0], y: cy - radius * p[1], depth: p[2]});
      });
      projected.sort((a, b) => a.depth - b.depth);
    } else {
      const left = 38;
      const right = width - 18;
      const plotWidth = right - left;
      const plotHeight = plotWidth / 2;
      const top = (height - plotHeight) / 2 - 8;
      const bottom = top + plotHeight;
      add(svg, "rect", {x: left, y: top, width: plotWidth, height: plotHeight, fill: "#f7faf3", stroke: "#c5d3c9", "stroke-width": 1});
      for (const lon of [-180, -90, 0, 90, 180]) {
        const x = left + (lon + 180) / 360 * plotWidth;
        line(svg, x, top, x, bottom);
        add(svg, "text", {x, y: bottom + 19, "text-anchor": "middle", class: "c-chart-label"}, `${lon}°`);
      }
      for (const lat of [-90, -45, 0, 45, 90]) {
        const y = top + (90 - lat) / 180 * plotHeight;
        line(svg, left, y, right, y);
        if (lat % 90 === 0) add(svg, "text", {x: left - 6, y: y + 4, "text-anchor": "end", class: "c-chart-label"}, `${lat}°`);
      }
      add(svg, "text", {x: (left + right) / 2, y: bottom + 39, "text-anchor": "middle", class: "c-chart-note"}, "synthetic longitude");
      data.points.forEach((point, i) => {const [lon, lat] = longitudeLatitude(point); projected.push({index: i, x: left + (lon + 180) / 360 * plotWidth, y: top + (90 - lat) / 180 * plotHeight, depth: 1});});
    }
    const pointRadius = width < 400 ? 4.5 : 5.5;
    for (const p of projected) {
      const group = add(svg, "g", {class: "c-map-point", "data-index": p.index});
      add(group, "circle", {cx: p.x, cy: p.y, r: pointRadius + 7, fill: "transparent"});
      add(group, "circle", {cx: p.x, cy: p.y, r: pointRadius, fill: sampleColor(current.sky[p.index]), stroke: "#81988b", "stroke-width": 0.7});
      add(group, "title", {}, `Sample ${p.index}: ${current.sky[p.index].toFixed(5)} arbitrary units. Select to move the injection center.`);
      group.addEventListener("click", () => {state = normalizeState({...state, center: p.index}); syncControls(); update();});
    }
    const winningCenter = data.labels[current.winner].center_index;
    for (const p of projected) {
      if (p.index === winningCenter) add(svg, "rect", {x: p.x - 9, y: p.y - 9, width: 18, height: 18, fill: "none", stroke: "#a65b19", "stroke-width": 1.8, "pointer-events": "none"});
      if (p.index === state.center) add(svg, "path", {d: `M${p.x},${p.y - 13} L${p.x + 13},${p.y} L${p.x},${p.y + 13} L${p.x - 13},${p.y} Z`, fill: "none", stroke: "#182b29", "stroke-width": 1.5, "pointer-events": "none"});
    }
    const clipped = current.sky.filter(value => Math.abs(value) > 6).length;
    const injectionVisible = projected.some(p => p.index === state.center);
    const viewText = state.view === "sphere"
      ? `${projected.length} facing samples shown in orthographic projection. Switch to the flat map for all 96.${injectionVisible ? "" : " The injection center is on the far hemisphere; use Face injection."}`
      : "All 96 samples shown in a longitude–latitude projection. Positions and color values are simulated.";
    $("skyViewCaption").textContent = viewText + (clipped ? ` ${clipped} values exceed the ±6 color limits; their exact values remain in the table.` : "");
  }

  function drawHistogram() {
    if (!current) return;
    const svg = $("scanHistogram");
    const width = Math.max(260, svg.parentElement.clientWidth);
    const height = width < 380 ? 230 : 250;
    setSVG(svg, width, height, "histogramTitle", "histogramDescription", "Full-search null maxima and current synthetic result",
      `${current.exceedances} of 4095 null maxima are at least ${current.maximum.toFixed(6)}. The Monte Carlo rank probability is ${current.globalP}.`);
    const margin = {left: 39, right: 15, top: 29, bottom: 42};
    const plotWidth = width - margin.left - margin.right;
    const plotHeight = height - margin.top - margin.bottom;
    const maximum = Math.max(8, Math.ceil(current.maximum + 0.5), Math.ceil(data.calibration_maxima_sorted[4094] + 0.5));
    const bins = width < 380 ? 24 : 32;
    const result = histogram(data.calibration_maxima_sorted, bins, 0, maximum);
    const ymax = Math.ceil(Math.max(...result.counts) / 100) * 100;
    const x = value => margin.left + value / maximum * plotWidth;
    const y = count => margin.top + plotHeight * (1 - count / ymax);
    add(svg, "rect", {x: x(current.maximum), y: margin.top, width: x(maximum) - x(current.maximum), height: plotHeight, fill: "#fcf0e1"});
    for (let j = 0; j <= 3; j += 1) {
      const count = ymax * j / 3;
      line(svg, margin.left, y(count), width - margin.right, y(count));
      add(svg, "text", {x: margin.left - 7, y: y(count) + 4, "text-anchor": "end", class: "c-chart-label"}, String(Math.round(count)));
    }
    result.counts.forEach((count, i) => add(svg, "rect", {x: x(i * result.step) + 0.8, y: y(count), width: Math.max(0.5, plotWidth / bins - 1.6), height: margin.top + plotHeight - y(count), fill: "#629b88"}));
    for (let j = 0; j <= 4; j += 1) {
      const value = maximum * j / 4;
      add(svg, "text", {x: x(value), y: height - margin.bottom + 20, "text-anchor": "middle", class: "c-chart-label"}, Number.isInteger(value) ? String(value) : value.toFixed(1));
    }
    const markerX = x(current.maximum);
    line(svg, markerX, margin.top - 4, markerX, height - margin.bottom, {stroke: "#a65b19", "stroke-width": 2});
    add(svg, "text", {x: Math.max(margin.left + 4, Math.min(width - margin.right - 4, markerX)), y: 15,
      "text-anchor": markerX > width * 0.65 ? "end" : markerX < width * 0.35 ? "start" : "middle", class: "c-chart-marker"}, `S = ${current.maximum.toFixed(3)}`);
    add(svg, "text", {x: margin.left, y: margin.top - 10, class: "c-chart-note"}, "null skies");
    add(svg, "text", {x: margin.left + plotWidth / 2, y: height - 5, "text-anchor": "middle", class: "c-chart-note"}, "maximum normalized score across 288 filters");
  }

  function drawChannel() {
    const svg = $("channelDiagram");
    const mobile = svg.parentElement.clientWidth < 560;
    const width = mobile ? 360 : 760;
    const height = mobile ? 590 : 430;
    setSVG(svg, width, height, "channelDiagramTitle", "channelDiagramDescription",
      "Typed conditional source and inference model",
      "An assumed message reaches a source through an assumed encoding. Nuisance parameters and the source enter a physical transfer law. Observations feed calibrated inference, with an independent null-calibration input. The physical cross-aeon law and intentional encoding are hypotheses.");
    // This diagram has its own responsive coordinate system, so do not force
    // its CSS-pixel height to the desktop viewBox on a narrower container.
    svg.style.height = "auto";
    const defs = add(svg, "defs");
    const marker = add(defs, "marker", {id: "ccc-channel-arrow", markerWidth: 8, markerHeight: 8, refX: 7, refY: 4, orient: "auto"});
    add(marker, "path", {d: "M0,0 L8,4 L0,8 Z", fill: "#517d6e"});
    const boxes = mobile ? {
      message: [20, 20, 150, 75], source: [190, 20, 150, 75], nuisance: [20, 155, 150, 85],
      transfer: [190, 145, 150, 100], data: [190, 310, 150, 90], calibration: [20, 475, 150, 90], inference: [190, 475, 150, 90]
    } : {
      message: [20, 25, 170, 70], source: [280, 25, 190, 70], nuisance: [20, 180, 170, 82],
      transfer: [280, 160, 190, 106], data: [550, 160, 190, 106], calibration: [280, 330, 190, 74], inference: [550, 330, 190, 74]
    };
    function edge(from, to, mode, dashed, label) {
      const a = boxes[from], b = boxes[to];
      let x1, y1, x2, y2;
      if (mode === "down") {x1 = a[0] + a[2] / 2; y1 = a[1] + a[3]; x2 = b[0] + b[2] / 2; y2 = b[1];}
      else {x1 = a[0] + a[2]; y1 = a[1] + a[3] / 2; x2 = b[0]; y2 = b[1] + b[3] / 2;}
      add(svg, "path", {d: `M${x1},${y1} L${x2},${y2}`, fill: "none", stroke: "#517d6e", "stroke-width": 1.5, "stroke-dasharray": dashed ? "5 4" : "none", "marker-end": "url(#ccc-channel-arrow)"});
      if (label && !mobile) add(svg, "text", {x: (x1 + x2) / 2, y: (y1 + y2) / 2 - 9, "text-anchor": "middle", class: "c-node-label"}, label);
    }
    edge("message", "source", "right", true, "assumed encoder");
    edge("source", "transfer", "down", true);
    edge("nuisance", "transfer", "right", true);
    edge("transfer", "data", "right", true);
    edge("data", "inference", "down", false);
    edge("calibration", "inference", "right", false, "full-search null");
    const descriptions = {
      message: ["M · message hypothesis", "finite symbol alphabet", true],
      source: ["X · source representation", "field or finite state", false],
      nuisance: ["θ · nuisance + noise", "physical uncertainty", false],
      transfer: ["Physical transfer law", "p(Y | X, θ)", true],
      data: ["Y · observed record", "finite detector data", false],
      calibration: ["Null calibration", "same complete statistic", false],
      inference: ["Z · inference output", "score or decision", false]
    };
    for (const [key, box] of Object.entries(boxes)) {
      const [x, y, w, h] = box;
      const [title, subtitle, assumed] = descriptions[key];
      add(svg, "rect", {x, y, width: w, height: h, rx: 3, fill: assumed ? "#fbf2e6" : "#eef4ec", stroke: assumed ? "#a65b19" : "#9db9aa", "stroke-width": 1.2, "stroke-dasharray": assumed ? "5 4" : "none"});
      const titleText = mobile && key === "source" ? "X · source state" : mobile && key === "message" ? "M · message hypothesis" : title;
      add(svg, "text", {x: x + w / 2, y: y + h / 2 - 6, "text-anchor": "middle", class: "c-node-title", "font-size": mobile ? 12 : 13}, titleText);
      add(svg, "text", {x: x + w / 2, y: y + h / 2 + 17, "text-anchor": "middle", class: "c-node-subtitle"}, subtitle);
    }
    if (mobile) {
      add(svg, "text", {x: 27, y: 330, class: "c-node-subtitle"}, "Dashed: assumed");
      add(svg, "text", {x: 27, y: 349, class: "c-node-subtitle"}, "encoding or physical");
      add(svg, "text", {x: 27, y: 368, class: "c-node-subtitle"}, "transfer hypotheses.");
    }
  }

  function drawSpinor() {
    const svg = $("spinorDiagram");
    const width = Math.max(260, svg.getBoundingClientRect().width || svg.parentElement.clientWidth);
    const height = 210;
    setSVG(svg, width, height, "spinorTitle", "spinorDescription",
      "Spinor contraction phi AB equals psi ABCD kappa CD",
      "The symmetric four-input tensor psi contracts its C and D slots with the two outgoing primal slots of kappa. The remaining dual slots A and B form phi. This is an algebraic contraction, not automatically a quantum channel.");
    svg.style.height = "auto";
    const defs = add(svg, "defs");
    const marker = add(defs, "marker", {id: "spinor-arrow", markerWidth: 7, markerHeight: 7, refX: 6, refY: 3.5, orient: "auto"});
    add(marker, "path", {d: "M0,0 L7,3.5 L0,7 Z", fill: "#14695e"});
    const psiX = width * 0.34;
    const kappaX = width * 0.79;
    const cy = 100;
    const radius = width < 400 ? 29 : 39;
    const dy = radius * 0.56;
    const dx = Math.sqrt(radius * radius - dy * dy);
    for (const sign of [-1, 1]) {
      add(svg, "path", {d: `M12,${cy + sign * dy} H${psiX - dx - 2}`, fill: "none", stroke: "#14695e", "stroke-width": 1.8, "marker-end": "url(#spinor-arrow)"});
      add(svg, "path", {d: `M${kappaX - dx},${cy + sign * dy} C${kappaX - dx - 18},${cy + sign * 59} ${psiX + dx + 18},${cy + sign * 59} ${psiX + dx + 2},${cy + sign * dy}`, fill: "none", stroke: "#14695e", "stroke-width": 1.8, "marker-end": "url(#spinor-arrow)"});
    }
    add(svg, "circle", {cx: psiX, cy, r: radius, fill: "#e6efea", stroke: "#14695e", "stroke-width": 1.3});
    add(svg, "circle", {cx: kappaX, cy, r: radius, fill: "#f7e9d5", stroke: "#a65b19", "stroke-width": 1.3});
    add(svg, "text", {x: psiX, y: cy + 10, "text-anchor": "middle", class: "c-tensor-symbol"}, "ψ");
    add(svg, "text", {x: kappaX, y: cy + 10, "text-anchor": "middle", class: "c-tensor-symbol"}, "κ");
    add(svg, "text", {x: 22, y: cy - dy - 10, class: "c-wire-label"}, "A");
    add(svg, "text", {x: 22, y: cy + dy + 23, class: "c-wire-label"}, "B");
    add(svg, "text", {x: (psiX + kappaX) / 2, y: cy - 57, "text-anchor": "middle", class: "c-wire-label"}, "C");
    add(svg, "text", {x: (psiX + kappaX) / 2, y: cy + 69, "text-anchor": "middle", class: "c-wire-label"}, "D");
    add(svg, "text", {x: psiX, y: 191, "text-anchor": "middle", class: "c-tensor-label"}, "Sym⁴(S*)");
    add(svg, "text", {x: kappaX, y: 191, "text-anchor": "middle", class: "c-tensor-label"}, "Sym²(S)");
  }

  function syncControls() {
    $("injectionCenter").value = String(state.center);
    $("injectionWidth").value = String(state.width);
    $("injectionSNR").value = String(state.snr);
    $("skyProjection").value = state.view;
    $("skyYaw").value = String(state.yaw);
    $("skyPitch").value = String(state.pitch);
    $("snrValue").value = state.snr.toFixed(1);
    $("yawValue").value = `${state.yaw}°`;
    $("pitchValue").value = `${state.pitch}°`;
    $("viewRotation").hidden = state.view === "flat";
  }

  function renderTables() {
    const ranking = current.scores.map((score, index) => ({score, index})).sort((a, b) => b.score - a.score).slice(0, 5);
    $("strongestMatches").innerHTML = ranking.map((row, i) => `<tr><th scope="row">${i + 1}</th><td>${data.labels[row.index].center_index}</td><td>${data.labels[row.index].width_rad.toFixed(2)}</td><td>${row.score.toFixed(6)}</td></tr>`).join("");
    const winnerCenter = data.labels[current.winner].center_index;
    $("sampleValues").innerHTML = data.points.map((point, i) => {
      const [lon, lat] = longitudeLatitude(point);
      const roles = [];
      if (i === state.center) roles.push("injection");
      if (i === winnerCenter) roles.push("winning center");
      return `<tr${roles.length ? ' class="c-highlight"' : ""}><th scope="row">${i}</th><td>${lon.toFixed(2)}</td><td>${lat.toFixed(2)}</td><td>${current.sky[i].toFixed(6)}</td><td>${roles.join("; ") || "sample"}</td></tr>`;
    }).join("");
  }

  function updateURL() {
    const url = new URL(global.location.href);
    url.search = stateToSearch(state);
    $("cosmologyPermalink").href = url.href;
    global.history.replaceState(null, "", url.href);
  }

  function update() {
    if (!data) return;
    current = evaluate(data, state);
    state = current.state;
    syncControls();
    $("selectedLocalP").textContent = formatP(current.selectedLocalP);
    $("globalRankP").textContent = formatP(current.globalP);
    $("maximumScore").textContent = current.maximum.toFixed(4);
    const count = $("calibrationCount");
    count.replaceChildren(document.createTextNode(`${current.exceedances.toLocaleString("en-US")} of 4,095 calibration maxima are at least this large. Rank p = (${current.exceedances} + 1) / 4,096.`));
    if (!current.exceedances) {
      const resolution = document.createElement("span");
      resolution.className = "c-resolution";
      resolution.textContent = "Finite resolution: 1/4096. A smaller tail is not measured here.";
      count.appendChild(document.createElement("br"));count.appendChild(resolution);
    }
    const winner = data.labels[current.winner];
    const fixedLabel = `Center ${state.center} · width ${WIDTHS[state.width].toFixed(2)} rad`;
    $("fixedTemplateResult").textContent = `${fixedLabel}: R = ${current.fixedScore.toFixed(6)}, fixed-template tail = ${formatP(current.fixedLocalP)}.`;
    $("injectionReadout").textContent = `Injection: center ${state.center}, width ${WIDTHS[state.width].toFixed(2)} rad. Winning match: center ${winner.center_index}, width ${winner.width_rad.toFixed(2)} rad. Each marker is one sample; marker area has no statistical meaning.`;
    const benchmark = state.center === 0 && state.width === 1 && [0, 1, 3, 5].includes(state.snr);
    $("liveRecordLabel").textContent = benchmark ? `RECORDED SETTING · SYNTHETIC SNR ${state.snr}` : "LIVE HYPOTHETICAL SYNTHETIC RECORD";
    document.querySelectorAll(".c-preset").forEach(button => button.setAttribute("aria-pressed", String(benchmark && Number(button.dataset.snr) === state.snr)));
    drawMap();drawHistogram();renderTables();updateURL();
    global.CCCCurrent = {state: {...state}, maximum: current.maximum, selectedLocalP: current.selectedLocalP,
      globalP: current.globalP, exceedances: current.exceedances, winner: current.winner};
  }

  async function initialize() {
    drawChannel();
    drawSpinor();
    global.document.documentElement.dataset.cosmologyReady = "loading";
    const response = await fetch("data/cosmology-synthetic.json");
    if (!response.ok) throw new Error(`Synthetic fixture request returned HTTP ${response.status}.`);
    data = await response.json();
    validateDataset(data);
    const select = $("injectionCenter");
    for (let i = 0; i < 96; i += 1) {
      const option = document.createElement("option");option.value = String(i);option.textContent = `Center ${i}`;select.appendChild(option);
    }
    for (const id of ["injectionCenter", "injectionWidth", "injectionSNR", "skyProjection", "skyYaw", "skyPitch"]) {
      $(id).addEventListener("input", () => {
        state = normalizeState({center: $("injectionCenter").value, width: $("injectionWidth").value,
          snr: $("injectionSNR").value, view: $("skyProjection").value, yaw: $("skyYaw").value, pitch: $("skyPitch").value});
        update();
      });
    }
    document.querySelectorAll(".c-preset").forEach(button => {
      button.disabled = false;
      button.addEventListener("click", () => {state = normalizeState({...state, center: 0, width: 1, snr: button.dataset.snr});update();});
    });
    $("faceInjection").disabled = false;
    $("faceInjection").addEventListener("click", () => {state = normalizeState({...state, ...facePoint(data.points[state.center])});update();});
    $("cosmologyControls").disabled = false;
    $("cosmologyLoadStatus").textContent = "Synthetic fixture loaded · 96 directions · 288 fixed templates · 4,095 independent full-scan null maxima.";
    $("modelProvenance").textContent = `Generator: Python ${data.benchmark.python}, NumPy ${data.benchmark.numpy}, PCG64 seed ${data.benchmark.seed}. Generator SHA-256: ${data.benchmark.source_sha256}.`;
    $("recordedResults").innerHTML = data.benchmark.experiments.map(record => `<tr><th scope="row">${record.injected_matched_snr}</th><td>${record.scan_maximum.toFixed(6)}</td><td>${formatP(record.selected_template_uncorrected_one_sided_p)}</td><td>${record.global_rank_p.toFixed(8)}</td></tr>`).join("");
    update();
    global.document.documentElement.dataset.cosmologyReady = "true";
    let resizePending = false;
    const redraw = () => {
      if (resizePending) return;
      resizePending = true;
      global.requestAnimationFrame(() => {resizePending = false;drawMap();drawHistogram();drawChannel();drawSpinor();});
    };
    if (global.ResizeObserver) {
      const observer = new ResizeObserver(redraw);
      observer.observe($("skyMap").parentElement);
      observer.observe($("scanHistogram").parentElement);
      observer.observe($("channelDiagram").parentElement);
      observer.observe($("spinorDiagram").parentElement);
    } else global.addEventListener("resize", redraw);
    global.addEventListener("popstate", () => {state = stateFromSearch(global.location.search);update();});
  }

  initialize().catch(error => {
    $("cosmologyLoadStatus").dataset.error = "true";
    $("cosmologyLoadStatus").textContent = "The interactive fixture could not be loaded. The recorded benchmark and primary-source links below remain available. Reload this page to retry.";
    global.document.documentElement.dataset.cosmologyReady = "error";
    console.error("Cosmology fixture:", error);
  });
})(typeof globalThis !== "undefined" ? globalThis : this);
