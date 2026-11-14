/* Native MathML can overflow its CSS box in Firefox without creating an HTML
   scroll container. Keep full-size equations in focusable HTML containers. */
(() => {
  'use strict';
  // Defer initial MathML layout until the streamed chapter subtree is complete.
  // With scripts disabled the pending class is never added, so content stays visible.
  document.documentElement.classList.remove('native-math-pending');
  function fitReviewedReaderMath() {
    for (const math of document.querySelectorAll('math')) {
      if (math.closest('.reader-table-scroll,.reader-inline-math,.reader-display-math')) continue;
      const parent = math.closest('p,li,dd,dt,div,section,article,aside,body');
      if (!parent) continue;
      const style = getComputedStyle(parent);
      const available = parent.clientWidth - parseFloat(style.paddingLeft) - parseFloat(style.paddingRight);
      const display = math.getAttribute('display') === 'block';
      const width = display ? Math.min(available, math.clientWidth || available) : available;
      if (Math.max(math.scrollWidth, math.getBoundingClientRect().width) <= width + 1) continue;
      const box = document.createElement('span');
      box.className = display ? 'reader-display-math' : 'reader-inline-math';
      box.tabIndex = 0;
      box.setAttribute('aria-label', 'Scrollable mathematical expression');
      math.replaceWith(box);
      box.append(math);
    }
  }
  window.fitReviewedReaderMath = fitReviewedReaderMath;
  fitReviewedReaderMath();
  addEventListener('resize', () => requestAnimationFrame(fitReviewedReaderMath));
  document.addEventListener('toggle', fitReviewedReaderMath, true);
  if (document.fonts) document.fonts.ready.then(fitReviewedReaderMath);
})();
