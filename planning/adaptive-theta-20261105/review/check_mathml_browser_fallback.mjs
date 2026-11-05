import {Browser} from '/home/iska/Documents/LaTeX-projects/project-pages-20261104/qa/bidi.mjs';
import assert from 'node:assert/strict';
const url=process.env.MATHML_FALLBACK_URL;
assert.ok(url,'Explicit loopback fixture URL required');
const browser=await new Browser().connect();
try {
  await browser.viewport(390,844);
  await browser.navigate(url+'/book/main.html');
  await browser.until('document.readyState==="complete"&&document.querySelectorAll("math").length===6890');
  const state=await browser.evaluate(`(()=>{
    const maths=[...document.querySelectorAll('math')];
    return {ready:document.readyState,pending:document.documentElement.classList.contains('native-math-pending'),
      helper:typeof window.fitReviewedReaderMath,mathCount:maths.length,
      displayedMath:maths.filter(x=>getComputedStyle(x).display!=='none').length,
      guardScriptPresent:[...document.scripts].some(s=>s.textContent.includes('DOMContentLoaded')&&s.textContent.includes('native-math-pending')),
      malformedMsub:[...document.querySelectorAll('msub')].filter(x=>x.children.length!==2).length};
  })()`);
  assert.equal(state.pending,false,'DOMContentLoaded fallback releases guard');
  assert.equal(state.helper,'undefined','Blocked helper really did not execute');
  assert.equal(state.mathCount,6890);
  assert.equal(state.displayedMath,6890,'No formula remains display:none');
  assert.equal(state.guardScriptPresent,true);
  assert.equal(state.malformedMsub,0);
  const errors=browser.pageErrors().map(e=>e.params.text);
  console.log(JSON.stringify({passed:true,fixture:'HTTP404 for reviewed-math-scroll.js only',state,pageErrors:errors,
    scope:'Real Firefox9335 helper-failure visibility regression; strict full browser QA is a separate root check.'},null,2));
} finally { await browser.close(); }
