// Scope: inherited companion pages only. Recorded data stays unchanged.
(() => {
  'use strict';
  if (window.__integralLegacyBase) return;
  window.__integralLegacyBase = true;
  const base = '/legacy/';
  const map = value => {
    if (typeof value !== 'string') return value;
    const loopback = 'http://127.0.0.1:8765';
    if (value === loopback) value = '/';
    else if (value.startsWith(loopback + '/')) value = value.slice(loopback.length);
    else if (value.startsWith(loopback + '?') || value.startsWith(loopback + '#')) value = '/' + value.slice(loopback.length);
    else if (value.startsWith(location.origin + '/')) value = value.slice(location.origin.length);
    if (value.startsWith('/') && !value.startsWith('//') && !value.startsWith(base)) return base + value.slice(1);
    return value;
  };
  const nativeFetch = window.fetch.bind(window);
  window.fetch = (input, init) => nativeFetch(
    typeof input === 'string' ? map(input) :
    input instanceof URL ? new URL(map(input.href), location.origin) :
    input instanceof Request ? new Request(new URL(map(input.url), location.origin), input) : input, init);
  const properties = [[HTMLAnchorElement, 'href'], [HTMLImageElement, 'src'],
    [HTMLIFrameElement, 'src'], [HTMLMediaElement, 'src'], [HTMLSourceElement, 'src'],
    [HTMLVideoElement, 'poster'], [HTMLLinkElement, 'href'], [HTMLScriptElement, 'src']];
  for (const [type, key] of properties) {
    const descriptor = Object.getOwnPropertyDescriptor(type.prototype, key);
    if (descriptor && descriptor.set) Object.defineProperty(type.prototype, key,
      { ...descriptor, set(value) { descriptor.set.call(this, map(value)); } });
  }
  const attributes = ['href', 'src', 'poster', 'data-source'];
  const setAttribute = Element.prototype.setAttribute;
  Element.prototype.setAttribute = function (key, value) {
    return setAttribute.call(this, key, attributes.includes(key.toLowerCase()) ? map(value) : value);
  };
  const patch = node => {
    if (node.nodeType !== 1) return;
    for (const element of [node, ...node.querySelectorAll('[href],[src],[poster],[data-source]')]) {
      for (const key of attributes) {
        const value = element.getAttribute(key), mapped = map(value);
        if (value && mapped !== value) setAttribute.call(element, key, mapped);
      }
    }
  };
  new MutationObserver(records => records.forEach(record => record.type === 'attributes'
    ? patch(record.target) : record.addedNodes.forEach(patch)))
    .observe(document.documentElement, { subtree: true, childList: true,
      attributes: true, attributeFilter: attributes });
})();
