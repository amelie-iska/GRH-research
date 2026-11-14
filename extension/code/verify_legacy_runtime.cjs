'use strict';
// No browser or network impersonation: this isolated VM checks URL routing only.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const calls = [];
class Element {
  constructor() { this.attributes = {}; this.nodeType = 1; }
  setAttribute(key, value) { this.attributes[key] = value; }
  getAttribute(key) { return this.attributes[key] || null; }
  querySelectorAll() { return []; }
}
const context = { Element, URL, Request, location: { origin: 'https://atlas.example' },
  document: { documentElement: {} },
  MutationObserver: class { constructor(callback) { this.callback = callback; } observe() {} },
  window: { fetch(input) { calls.push(input instanceof Request ? input.url : String(input)); return Promise.resolve({ ok: true }); } } };
for (const [name, key] of [['HTMLAnchorElement','href'],['HTMLImageElement','src'],
  ['HTMLIFrameElement','src'],['HTMLMediaElement','src'],['HTMLSourceElement','src'],
  ['HTMLVideoElement','poster'],['HTMLLinkElement','href'],['HTMLScriptElement','src']]) {
  context[name] = class extends Element {};
  Object.defineProperty(context[name].prototype, key, { configurable: true,
    get() { return this.attributes[key]; }, set(value) { this.attributes[key] = value; } });
}
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(__dirname, '../site/legacy/legacy-base.js'), 'utf8'), context);
const cases = [
  ['/', '/legacy/'], ['/#atlas', '/legacy/#atlas'], ['/?embed=atlas', '/legacy/?embed=atlas'],
  ['/book.pdf', '/legacy/book.pdf'], ['/examples/sage/dessin_orders.sage', '/legacy/examples/sage/dessin_orders.sage'],
  ['/legacy/data/record.json', '/legacy/data/record.json'],
  ['http://127.0.0.1:8765', '/legacy/'],
  ['http://127.0.0.1:8765/architecture.html', '/legacy/architecture.html'],
  ['http://127.0.0.1:8765#atlas', '/legacy/#atlas'],
  ['https://atlas.example/data/record.json', '/legacy/data/record.json'],
  ['https://arxiv.org/abs/1106.0774v1', 'https://arxiv.org/abs/1106.0774v1'],
  ['//cdn.example/module.js', '//cdn.example/module.js'], ['./data/record.json', './data/record.json']
];
for (const [input, expected] of cases) { context.window.fetch(input); assert.equal(calls.pop(), expected); }
context.window.fetch(new URL('https://atlas.example/data/record.json'));
assert.equal(calls.pop(), 'https://atlas.example/legacy/data/record.json');
context.window.fetch(new Request('https://atlas.example/data/record.json'));
assert.equal(calls.pop(), 'https://atlas.example/legacy/data/record.json');
const anchor = new context.HTMLAnchorElement(); anchor.href = '/book.pdf';
assert.equal(anchor.href, '/legacy/book.pdf');
const element = new Element(); element.setAttribute('src', '/media/SurfaceClock.mp4');
assert.equal(element.getAttribute('src'), '/legacy/media/SurfaceClock.mp4');
console.log(JSON.stringify({ passed: true, url_cases: cases.length + 2, dom_setter_cases: 2 }));
