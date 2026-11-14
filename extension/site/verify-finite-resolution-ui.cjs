#!/usr/bin/env node
"use strict";
// Behavioral DOM fixture only: this is not a browser layout/accessibility audit.
const assert = require("node:assert/strict"), fs = require("node:fs"), path = require("node:path"), crypto = require("node:crypto");
const UI = require("./finite-resolution-ui.js"), R = require("./finite-resolution-core.js");
class Element {
  constructor(doc, tag) { this.ownerDocument = doc; this.tagName = tag; this.children = []; this.dataset = {}; this.attributes = {}; this.events = {}; this.value = ""; this._text = ""; this.className = ""; this.classList = {add: name => { this.className += " " + name; }}; }
  appendChild(child) { this.children.push(child); return child; }
  replaceChildren(...children) { this._text = ""; this.children = children; }
  setAttribute(key, value) { this.attributes[key] = value; }
  addEventListener(key, handler) { (this.events[key] ||= []).push(handler); }
  dispatch(key) { for (const handler of this.events[key] || []) handler({target: this}); }
  set textContent(text) { this._text = String(text); this.children = []; }
  get textContent() { return this._text + this.children.map(child => child.textContent).join(" "); }
}
function walk(node, predicate) { if (predicate(node)) return node; for (const child of node.children) { const result = walk(child, predicate); if (result) return result; } return null; }
class Document {
  constructor() { this.head = new Element(this, "head"); this.body = new Element(this, "body"); }
  createElement(tag) { return new Element(this, tag); }
  getElementById(id) { return walk(this.head, item => item.id === id) || walk(this.body, item => item.id === id); }
  querySelectorAll(selector) { assert.equal(selector, "[data-resolution-lab]"); return this.body.children.filter(item => item.dataset.resolutionLab); }
}
const doc = new Document(), containers = {};
for (const family of ["taylor-green", "heat-mode", "u1-plaquette"]) { const c = doc.createElement("div"); c.dataset.resolutionLab = family; containers[family] = c; doc.body.appendChild(c); }
const panels = UI.mountAll(doc); assert.equal(panels.length, 3); assert.equal(doc.head.children.length, 1);
const checks = [];
function test(name, fn) { fn(); checks.push(name); }
function node(family, className) { return walk(containers[family], item => item.className.split(/\s+/).includes(className)); }
test("three distinct families mount with labels, table captions and numerical scope", () => {
  for (const family of Object.keys(containers)) {
    const c = containers[family], p = c.resolutionPanel;
    assert.equal(p.getReport().rows.length, 3); assert.equal(node(family, "resolution-status").dataset.state, "evaluated");
    assert.match(c.textContent, /does not issue a Lean certificate/); assert.match(c.textContent, /heuristic/);
    assert.ok(walk(c, item => item.tagName === "caption"));
    for (const control of Object.values(p.controls)) assert.ok(walk(c, item => item.tagName === "label" && item.htmlFor === control.id));
    assert.ok(walk(c, item => item.attributes.role === "status" && item.attributes["aria-live"] === "polite"));
  }
  assert.equal(UI.mount(containers["heat-mode"]), panels[1]);
});
test("Nyquist input clears old results and correction recovers through the change event", () => {
  const p = panels[1]; p.controls.modeX.value = "4"; p.controls.modeX.dispatch("change");
  assert.equal(p.getReport(), null); assert.equal(node("heat-mode", "resolution-result").children.length, 0);
  assert.equal(node("heat-mode", "resolution-status").dataset.state, "invalid");
  assert.equal(node("heat-mode", "resolution-alert").hidden, false); assert.match(node("heat-mode", "resolution-alert").textContent, /Nyquist/);
  p.controls.modeX.value = "3"; p.controls.modeX.dispatch("change"); assert.ok(p.getReport());
  assert.equal(node("heat-mode", "resolution-alert").hidden, true);
});
test("empty and nonfinite controls fail without reusing a stale report", () => {
  const p = panels[0]; p.controls.time.value = ""; assert.equal(p.refresh(), null); assert.match(node("taylor-green", "resolution-alert").textContent, /Enter a value/);
  p.controls.time.value = "1.5"; p.controls.nu.value = "Infinity"; assert.equal(p.refresh(), null);
  p.controls.nu.value = "0.08"; assert.ok(p.refresh());
});
test("real-arithmetic energy exactness is not formatted as zero numerical error for all inputs", () => {
  const p = panels[0]; p.controls.start.value = "32"; p.controls.start.dispatch("change"); assert.equal(p.getReport().rows[2].n, 128);
  assert.match(containers["taylor-green"].textContent, /Nonlinear residual bound/);
  p.controls.start.value = "64"; assert.equal(p.refresh(), null); p.controls.start.value = "8"; p.refresh();
});
test("zero-time heat reports unresolved rates and retains separate budgets", () => {
  const p = panels[1]; p.controls.time.value = "0"; p.controls.time.dispatch("change");
  assert.ok(p.getReport().rows.every(row => row.error === 0 && row.observedOrder === null));
  assert.match(containers["heat-mode"].textContent, /Unresolved/); assert.match(containers["heat-mode"].textContent, /Spatial amplitude error/);
  assert.match(containers["heat-mode"].textContent, /Time amplitude error/);
});
test("the gauge panel preserves raw cancellation, stable value and withheld rates", () => {
  const p = panels[2]; p.controls.start.value = "16384"; p.controls.start.dispatch("change");
  const last = p.getReport().rows[2]; assert.equal(last.n, 65536); assert.equal(last.rawDensity, 0); assert.equal(last.stableDensity, 1);
  assert.equal(last.observedOrder, null); assert.match(containers["u1-plaquette"].textContent, /loss of significance/); assert.match(containers["u1-plaquette"].textContent, /Unresolved/);
});
test("coarse gauge flux warns about phase aliasing without changing the declared family", () => {
  const p = panels[2]; p.controls.start.value = "1"; p.controls.curvature.value = "8"; p.refresh();
  assert.ok(p.getReport().rows[0].phaseAliased); assert.match(containers["u1-plaquette"].textContent, /principal phase does not determine/);
  assert.match(containers["u1-plaquette"].textContent, /unit-square patch/);
});
test("display helpers distinguish an unavailable value, exact zero and an unresolved rate", () => {
  assert.equal(UI.formatNumber(NaN), "unavailable"); assert.equal(UI.formatNumber(0), "0");
  const rows = UI.tableRows(R.convergenceStudy("u1-plaquette", {curvature: 0}, [1, 2, 4]));
  assert.equal(rows[0].order, "—"); assert.equal(rows[1].order, "Unresolved"); assert.equal(rows[1].status, "At rounding scale");
});
const repo = path.resolve(__dirname, "../.."), sourcePaths = ["extension/site/finite-resolution-ui.js", "extension/site/finite-resolution-core.js", "extension/site/verify-finite-resolution-ui.cjs"];
const report = {schema: "finite-resolution-ui-checks-v1", status: "passed", checked_at_utc: new Date().toISOString(), node_version: process.version, checks,
  evidence_scope: "In-memory DOM behavior: labels, status text, event updates, invalid-input clearing, restored valid controls and retained numerical limitations. No browser rendering, screen-reader, keyboard, network or layout claim.",
  browser_rendered: false, source_sha256: Object.fromEntries(sourcePaths.map(name => [name, crypto.createHash("sha256").update(fs.readFileSync(path.join(repo, name))).digest("hex")]))};
const destination = path.join(repo, "extension/verification/finite-resolution-ui.json"); fs.mkdirSync(path.dirname(destination), {recursive: true}); fs.writeFileSync(destination, JSON.stringify(report, null, 2) + "\n");
process.stdout.write(JSON.stringify({status: report.status, checks: checks.length, output: path.relative(repo, destination)}) + "\n");
