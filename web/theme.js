/* Local visual preferences only. Scientific models, records and text stay intact. */
(() => {
  'use strict';
  if (window.surfaceTheme) return;
  const root = document.documentElement;
  const embedded = window.parent !== window;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const read = (key, fallback) => { try { return localStorage.getItem(key) ?? fallback; } catch { return fallback; } };
  const write = (key, value) => { try { localStorage.setItem(key, value); } catch {} };
  let theme = read('surface-order-theme', 'light') === 'biomech' ? 'biomech' : 'light';
  let wantsMotion = read('surface-order-motion', 'live') !== 'paused';
  let ready = false, counter = 0;
  const frames = new WeakSet();
  const materialSelector = 'header,.reader-nav,section,article,.diagram,canvas,video,pre,details,h1,h2,h3,button,input,select,.reader-lab,.aux,.scene-panel,.tensor-grid,.eyebrow,.badge,.private';
  const animatedSelector = 'header,.reader-nav,section,article,.diagram,canvas,video,.eyebrow,.badge,.private,.reader-lab';
  const visibility = typeof IntersectionObserver === 'function' ? new IntersectionObserver(entries => {
    for (const entry of entries) entry.target.dataset.themeVisible = String(entry.isIntersecting);
  }, { rootMargin: '180px' }) : null;

  function post(frame) {
    try { frame.contentWindow?.postMessage({ type: 'surface-order-theme', theme, motion: wantsMotion }, location.origin); } catch {}
  }
  function apply(persist = false) {
    root.dataset.theme = theme;
    root.dataset.themeMotion = wantsMotion && !reduced.matches ? 'live' : 'paused';
    root.classList.add('site-theme-ready');
    if (embedded) root.dataset.themeEmbedded = 'true';
    if (persist) {
      write('surface-order-theme', theme);
      write('surface-order-motion', wantsMotion ? 'live' : 'paused');
    }
    if (ready) {
      const toggle = document.getElementById('themeToggle');
      if (toggle) {
        const dark = theme === 'biomech';
        toggle.setAttribute('aria-pressed', String(dark));
        toggle.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to biomechanical dark mode');
        toggle.title = dark ? 'Return to daylight' : 'Engage the living dark interface';
        toggle.querySelector('.theme-caption').textContent = dark ? 'DAYLIGHT' : 'ENGAGE NIGHT';
        const motion = document.getElementById('motionToggle');
        motion.hidden = !dark;
        motion.disabled = reduced.matches;
        motion.setAttribute('aria-pressed', String(root.dataset.themeMotion === 'live'));
        motion.setAttribute('aria-label', reduced.matches ? 'Ambient motion disabled by reduced-motion preference' : wantsMotion ? 'Pause ambient motion' : 'Enable ambient motion');
        motion.title = motion.getAttribute('aria-label');
        motion.textContent = root.dataset.themeMotion === 'live' ? 'Ⅱ' : '▷';
      }
      for (const frame of document.querySelectorAll('iframe')) post(frame);
    }
  }
  function decorate(element) {
    if (!(element instanceof Element) || element.closest('#theme-switchboard')) return;
    const materials = [...(element.matches(materialSelector) ? [element] : []), ...element.querySelectorAll(materialSelector)];
    for (const node of materials) {
      if (node.hasAttribute('data-theme-material')) continue;
      const i = counter++ % 17;
      const kind = node.matches('header,.reader-nav') ? 'bridge' : node.matches('h1,h2,h3') ? 'type' : node.matches('canvas,video,.diagram,.tensor-grid') ? 'display' : node.matches('button,input,select') ? 'control' : 'hull';
      const durations = { bridge: 700, type: 1350, display: 2200, control: 950, hull: 1800 };
      node.dataset.themeMaterial = kind;
      node.style.setProperty('--theme-duration', durations[kind] + (i % 3) * 100 + 'ms');
      node.style.setProperty('--theme-delay', 35 * i + 'ms');
      node.style.setProperty('--theme-pulse-delay', -i * .71 + 's');
    }
    const animated = [...(element.matches(animatedSelector) ? [element] : []), ...element.querySelectorAll(animatedSelector)];
    for (const node of animated) {
      if (visibility) visibility.observe(node);
      else node.dataset.themeVisible = 'true';
    }
    const embeddedFrames = [...(element.matches('iframe') ? [element] : []), ...element.querySelectorAll('iframe')];
    for (const frame of embeddedFrames) if (!frames.has(frame)) {
      frames.add(frame); frame.addEventListener('load', () => post(frame)); post(frame);
    }
  }
  function init() {
    if (ready) return;
    ready = true;
    if (!embedded) {
      const dock = document.createElement('div'); dock.id = 'theme-switchboard';
      const toggle = document.createElement('button'); toggle.id = 'themeToggle'; toggle.type = 'button';
      const icon = document.createElement('span'); icon.className = 'theme-reactor'; icon.setAttribute('aria-hidden', 'true');
      const caption = document.createElement('span'); caption.className = 'theme-caption';
      toggle.append(icon, caption); toggle.onclick = () => { theme = theme === 'light' ? 'biomech' : 'light'; apply(true); };
      const motion = document.createElement('button'); motion.id = 'motionToggle'; motion.type = 'button';
      motion.onclick = () => { wantsMotion = !wantsMotion; apply(true); };
      dock.append(toggle, motion); document.body.append(dock);
    }
    decorate(document.body);
    new MutationObserver(changes => {
      for (const change of changes) for (const node of change.addedNodes) if (node.nodeType === 1) decorate(node);
    }).observe(document.body, { childList: true, subtree: true });
    apply();
  }
  addEventListener('storage', event => {
    if (!['surface-order-theme', 'surface-order-motion', null].includes(event.key)) return;
    theme = read('surface-order-theme', 'light') === 'biomech' ? 'biomech' : 'light';
    wantsMotion = read('surface-order-motion', 'live') !== 'paused'; apply();
  });
  addEventListener('message', event => {
    if (!embedded || event.source !== parent || event.origin !== location.origin || event.data?.type !== 'surface-order-theme') return;
    if (!['light', 'biomech'].includes(event.data.theme) || typeof event.data.motion !== 'boolean') return;
    theme = event.data.theme; wantsMotion = event.data.motion; apply();
  });
  reduced.addEventListener('change', () => apply());
  window.surfaceTheme = { snapshot: () => ({ theme, wantsMotion, reducedMotion: reduced.matches, embedded }) };
  apply();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();
