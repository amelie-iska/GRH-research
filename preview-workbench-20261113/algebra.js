/* Exact algebra and its DOM interface. No network calls or external runtime. */
(function (root) {
  'use strict';
  const names = ['X1', 'X2', 'Y1', 'Y2', 'Z1', 'Z2', 'B1', 'B2'];
  const coordinateNames = ['a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5'];
  const generatorVectors = [
    [1,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,1,0,0,0,1],
    [1,0,0,1,0,1,0,0,1,0], [0,1,0,0,1,0,1,0,0,1],
    [0,1,0,1,0,0,0,1,0,0], [0,0,1,0,0,0,1,0,1,0],
    [0,1,0,1,0,0,1,0,1,0], [0,0,1,0,0,0,0,1,0,0]
  ].map(row => Object.freeze(row.map(BigInt)));
  Object.freeze(generatorVectors);
  const asInteger = x => {
    if (typeof x === 'bigint') return x;
    if (typeof x === 'number' && Number.isSafeInteger(x)) return BigInt(x);
    if (typeof x === 'string' && /^-?\d+$/.test(x)) return BigInt(x);
    throw new TypeError('An exact integer is required');
  };
  function plucker(matrix) {
    if (matrix.length !== 2 || matrix.some(row => row.length !== 4)) throw new RangeError('Expected a 2 by 4 matrix');
    const m = matrix.map(row => row.map(asInteger)), minors = {};
    for (let i = 0; i < 4; i++) for (let j = i + 1; j < 4; j++) {
      minors[`${i + 1}${j + 1}`] = m[0][i] * m[1][j] - m[0][j] * m[1][i];
    }
    const terms = [minors['12'] * minors['34'], minors['13'] * minors['24'], minors['14'] * minors['23']];
    const rank = Object.values(minors).some(x => x !== 0n) ? 2 : m.flat().some(x => x !== 0n) ? 1 : 0;
    return { minors, terms, residual: terms[0] - terms[1] + terms[2], rank };
  }
  function tableauRules(t) {
    if (!Array.isArray(t) || t.length !== 5) throw new RangeError('Shape (3,2) has five boxes');
    const entries = t.every(x => Number.isInteger(x) && x >= 1 && x <= 3);
    const rows = t[0] <= t[1] && t[1] <= t[2] && t[3] <= t[4];
    const columns = t[0] < t[3] && t[1] < t[4];
    return { entries, rows, columns, valid: entries && rows && columns };
  }
  function enumerateTableaux() {
    const answer = [];
    function visit(t) {
      if (t.length === 5) { if (tableauRules(t).valid) answer.push(t); return; }
      for (let x = 1; x <= 3; x++) visit(t.concat(x));
    }
    visit([]);
    return answer;
  }
  function hookContent(shape = [3, 2], n = 3) {
    if (!Number.isSafeInteger(n) || n < 0 || shape.some((x, i) => !Number.isSafeInteger(x) || x <= 0 || (i > 0 && x > shape[i - 1]))) throw new RangeError('Expected a partition and nonnegative dimension');
    let numerator = 1n, denominator = 1n;
    const boxes = [];
    shape.forEach((length, i) => {
      for (let j = 0; j < length; j++) {
        const below = shape.slice(i + 1).filter(row => row > j).length;
        const hook = length - j + below, content = n + j - i;
        numerator *= BigInt(content); denominator *= BigInt(hook);
        boxes.push({ row: i + 1, column: j + 1, hook, content });
      }
    });
    if (numerator % denominator !== 0n) throw new Error('Hook-content product was not integral');
    return { numerator, denominator, dimension: numerator / denominator, boxes };
  }
  function allowablePairs(p, q, r) {
    if (![p, q, r].every(x => Number.isSafeInteger(x) && x >= 0)) throw new RangeError('Dimensions must be nonnegative integers');
    const pairs = [];
    for (let u = 0; u <= Math.min(p, q); u++) for (let v = 0; v <= Math.min(q - u, r); v++) pairs.push([u, v]);
    return pairs;
  }
  function a3(p, q, r, u, v) {
    if (![p, q, r, u, v].every(x => Number.isSafeInteger(x) && x >= 0) || u > p || v > r || u + v > q) throw new RangeError('Ranks are incompatible with the complex dimensions');
    const U = Array.from({ length: q }, (_, i) => Array.from({ length: p }, (_, j) => i < u && i === j ? 1n : 0n));
    const V = Array.from({ length: r }, (_, i) => Array.from({ length: q }, (_, j) => i < v && j === u + i ? 1n : 0n));
    const VU = Array.from({ length: r }, (_, i) => Array.from({ length: p }, (_, j) => V[i].reduce((sum, x, k) => sum + x * U[k][j], 0n)));
    return { p, q, r, u, v, U, V, VU,
      multiplicities: [u, v, p - u, q - u - v, r - v],
      cohomology: [p - u, q - u - v, r - v], pairs: allowablePairs(p, q, r) };
  }
  function exponentInput(exponents) {
    if (!Array.isArray(exponents) || exponents.length !== 8) throw new RangeError('Eight generator exponents are required');
    const e = exponents.map(asInteger);
    if (e.some(x => x < 0n)) throw new RangeError('Generator exponents must be nonnegative');
    return e;
  }
  function matchingVector(exponents) {
    const e = exponentInput(exponents);
    return coordinateNames.map((_, j) => e.reduce((sum, x, i) => sum + x * generatorVectors[i][j], 0n));
  }
  function matchingBalance(vector) {
    if (!Array.isArray(vector) || vector.length !== 10) throw new RangeError('Ten underlying coordinates are required');
    const a = vector.map(asInteger);
    return [[a[0] + a[1], a[3] + a[4]], [a[5] + a[6], a[8] + a[9]],
      [a[1] + a[2], a[6] + a[7]], [a[2] + a[3], a[7] + a[8]]]
      .map(([left, right]) => ({ left, right, residual: left - right }));
  }
  function matchingNormalForm(exponents) {
    const input = exponentInput(exponents), normal = input.slice();
    const yPairs = normal[2] < normal[3] ? normal[2] : normal[3];
    const zPairs = normal[4] < normal[5] ? normal[4] : normal[5];
    normal[2] -= yPairs; normal[3] -= yPairs;
    normal[0] += yPairs; normal[1] += yPairs; normal[6] += yPairs;
    normal[4] -= zPairs; normal[5] -= zPairs;
    normal[6] += zPairs; normal[7] += zPairs;
    const before = matchingVector(input), after = matchingVector(normal);
    return { input, normal, yPairs, zPairs, before, after,
      preserved: before.every((x, i) => x === after[i]),
      degree: before.reduce((sum, x) => sum + x, 0n), balance: matchingBalance(before) };
  }
  const api = Object.freeze({ plucker, tableauRules, enumerateTableaux, hookContent, allowablePairs, a3,
    matchingVector, matchingBalance, matchingNormalForm, generatorVectors,
    names: Object.freeze(names), coordinateNames: Object.freeze(coordinateNames) });
  root.IntegralAlgebra = api;
  if (typeof module === 'object' && module.exports) module.exports = api;
  if (typeof document === 'undefined') return;

  const $ = id => document.getElementById(id);
  const variableHTML = name => `${name[0]}<sub>${name.slice(1)}</sub>`;
  const monomial = (exponents, labels) => {
    const terms = exponents.map((x, i) => x === 0n ? '' : variableHTML(labels[i]) + (x === 1n ? '' : `<sup>${x}</sup>`)).filter(Boolean);
    return terms.length ? terms.join(' ') : '1';
  };
  function readBounded(inputs, low, high) {
    let valid = true;
    const values = inputs.map(input => {
      const ok = /^-?\d+$/.test(input.value) && Number(input.value) >= low && Number(input.value) <= high;
      input.setAttribute('aria-invalid', String(!ok));
      if (!ok) valid = false;
      return ok ? Number(input.value) : 0;
    });
    return valid ? values : null;
  }
  function status(id, text, valid = true) { const node = $(id); node.textContent = text; node.dataset.valid = String(valid); }

  const matrixInputs = [];
  [[1, 0, 2, -1], [0, 1, 3, 2]].forEach((row, i) => row.forEach((value, j) => {
    const label = document.createElement('label'), caption = document.createElement('span'), input = document.createElement('input');
    caption.innerHTML = `m<sub>${i + 1}${j + 1}</sub>`;
    input.type = 'number'; input.min = '-9'; input.max = '9'; input.step = '1'; input.value = String(value);
    input.setAttribute('aria-label', `Matrix row ${i + 1}, column ${j + 1}`);
    label.append(caption, input); $('matrixInputs').append(label); matrixInputs.push(input);
    input.addEventListener('input', renderMinors);
  }));
  function renderMinors() {
    const values = readBounded(matrixInputs, -9, 9);
    if (!values) { status('matrixStatus', 'Calculation paused: enter eight integers from −9 to 9. Previous valid results remain visible.', false); return; }
    const result = plucker([values.slice(0, 4), values.slice(4)]);
    $('minorValues').innerHTML = Object.entries(result.minors).map(([key, value]) => `<div><dt>p<sub>${key}</sub></dt><dd>${value}</dd></div>`).join('');
    const m = result.minors;
    $('pluckerCalculation').textContent = `(${m['12']} × ${m['34']}) − (${m['13']} × ${m['24']}) + (${m['14']} × ${m['23']}) = ${result.terms[0]} − (${result.terms[1]}) + (${result.terms[2]}) = ${result.residual}`;
    status('matrixStatus', `Identity verified exactly. Row rank over ℚ: ${result.rank}. ` + (result.rank === 2 ? 'The wedge is nonzero and gives a Grassmannian point.' : 'The wedge is zero; there is no projective point.'));
  }
  function setMatrix(values) { matrixInputs.forEach((input, i) => { input.value = String(values[i]); }); renderMinors(); }
  $('matrixExample').addEventListener('click', () => setMatrix([1, 0, 2, -1, 0, 1, 3, 2]));
  $('matrixDependent').addEventListener('click', () => setMatrix([1, 2, -1, 3, 2, 4, -2, 6]));
  $('matrixZero').addEventListener('click', () => setMatrix(Array(8).fill(0)));

  const tableaux = enumerateTableaux();
  let tableauIndex = 0;
  const tableauCellHTML = (t, large) => t.map((value, i) => `<span ${large ? `class="a-tableau-cell" data-entry="${value}"` : ''}${i === 3 ? ' style="grid-column:1"' : ''}>${value}</span>`).join('');
  tableaux.forEach((t, i) => {
    const option = document.createElement('option'); option.value = String(i); option.textContent = `${i + 1} of ${tableaux.length}`; $('tableauSelect').append(option);
    const button = document.createElement('button'); button.type = 'button'; button.dataset.index = String(i);
    button.setAttribute('aria-label', `Tableau ${i + 1}: row one ${t.slice(0, 3).join(', ')}, row two ${t.slice(3).join(', ')}`);
    button.innerHTML = `<span class="a-mini-tableau" aria-hidden="true">${tableauCellHTML(t, false)}</span><span class="a-thumb-index" aria-hidden="true">${i + 1}</span>`;
    button.addEventListener('click', () => { tableauIndex = i; renderTableau(); }); $('tableauGallery').append(button);
  });
  function renderTableau() {
    const t = tableaux[tableauIndex], rule = tableauRules(t), weight = [1, 2, 3].map(x => BigInt(t.filter(v => v === x).length));
    $('tableauLarge').innerHTML = tableauCellHTML(t, true);
    $('tableauLarge').setAttribute('aria-label', `Tableau ${tableauIndex + 1}: first row ${t.slice(0, 3).join(', ')}, second row ${t.slice(3).join(', ')}`);
    $('tableauPosition').textContent = `Tableau ${tableauIndex + 1} of ${tableaux.length}`;
    $('tableauRows').textContent = `${t[0]} ≤ ${t[1]} ≤ ${t[2]}; ${t[3]} ≤ ${t[4]} — ${rule.rows ? 'verified' : 'failed'}`;
    $('tableauColumns').textContent = `${t[0]} < ${t[3]}; ${t[1]} < ${t[4]} — ${rule.columns ? 'verified' : 'failed'}`;
    $('tableauWeight').innerHTML = monomial(weight, ['x1', 'x2', 'x3']);
    $('tableauSelect').value = String(tableauIndex);
    $('tableauPrevious').disabled = tableauIndex === 0; $('tableauNext').disabled = tableauIndex === tableaux.length - 1;
    $('tableauGallery').querySelectorAll('button').forEach((button, i) => button.setAttribute('aria-pressed', String(i === tableauIndex)));
  }
  $('tableauPrevious').addEventListener('click', () => { tableauIndex = Math.max(0, tableauIndex - 1); renderTableau(); });
  $('tableauNext').addEventListener('click', () => { tableauIndex = Math.min(tableaux.length - 1, tableauIndex + 1); renderTableau(); });
  $('tableauSelect').addEventListener('change', event => { tableauIndex = Number(event.target.value); renderTableau(); });
  const hook = hookContent();
  $('hookDimension').textContent = `${hook.dimension} = ${tableaux.length} tableaux`;
  $('hookCalculation').textContent = `(${hook.boxes.map(b => b.content).join(' × ')}) / (${hook.boxes.map(b => b.hook).join(' × ')}) = ${hook.numerator}/${hook.denominator} = ${hook.dimension}`;

  let ranks = [1, 1];
  function setOptions(node, max, value) {
    node.replaceChildren(...Array.from({ length: max + 1 }, (_, i) => {
      const option = document.createElement('option'); option.value = String(i); option.textContent = String(i); return option;
    })); node.value = String(value);
  }
  const dimensions = [$('dimP'), $('dimQ'), $('dimR')];
  function matrixTable(title, matrix, rows, cols) {
    return `<div class="a-matrix-display"><h4>${title} (${rows} × ${cols})</h4>` +
      (rows === 0 || cols === 0 ? '<p>Unique zero map with a zero-dimensional source or target.</p>' :
        `<table aria-label="${title}, ${rows} rows and ${cols} columns"><tbody>${matrix.map(row => `<tr>${row.map(x => `<td>${x}</td>`).join('')}</tr>`).join('')}</tbody></table>`) + '</div>';
  }
  function renderA3Diagram(result) {
    const { p, q, r, u, v } = result, counts = [p, q, r], xs = [100, 330, 560];
    const y = (column, i) => 122 + (i - (counts[column] - 1) / 2) * 27;
    let svg = '<defs><marker id="aTealArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#14695e"/></marker><marker id="aOchreArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#a65b19"/></marker></defs>';
    svg += `<text x="215" y="25" text-anchor="middle" font-size="15">U · rank ${u}</text><text x="445" y="25" text-anchor="middle" font-size="15">V · rank ${v}</text>`;
    for (let i = 0; i < u; i++) svg += `<line x1="112" y1="${y(0, i)}" x2="316" y2="${y(1, i)}" stroke="#14695e" stroke-width="2" marker-end="url(#aTealArrow)"/>`;
    for (let i = 0; i < v; i++) svg += `<line x1="342" y1="${y(1, u + i)}" x2="546" y2="${y(2, i)}" stroke="#a65b19" stroke-width="2" marker-end="url(#aOchreArrow)"/>`;
    counts.forEach((count, column) => {
      svg += `<text x="${xs[column]}" y="230" text-anchor="middle" font-size="17">k<tspan baseline-shift="super" font-size="12">${count}</tspan></text>`;
      if (!count) svg += `<text x="${xs[column]}" y="126" text-anchor="middle" font-size="19">0</text>`;
      for (let i = 0; i < count; i++) {
        const type = column === 0 ? (i < u ? 'teal' : 'simple') : column === 2 ? (i < v ? 'ochre' : 'simple') : i < u ? 'teal' : i < u + v ? 'ochre' : 'simple';
        const color = type === 'teal' ? '#14695e' : type === 'ochre' ? '#a65b19' : '#64736d';
        svg += `<circle cx="${xs[column]}" cy="${y(column, i)}" r="8" fill="${type === 'simple' ? '#fff' : color}" stroke="${color}" stroke-width="1.5"/><text x="${xs[column] - 18}" y="${y(column, i) + 4}" text-anchor="end" font-size="11">${i + 1}</text>`;
      }
    });
    $('a3Diagram').innerHTML = svg;
    $('a3Diagram').setAttribute('aria-label', `Complex with dimensions ${p}, ${q}, ${r}; ${u} M12 arrows, ${v} M23 arrows, and simple multiplicities ${result.cohomology.join(', ')}`);
  }
  function renderA3() {
    const dims = readBounded(dimensions, 0, 6);
    if (!dims) { status('a3Status', 'Calculation paused: dimensions must be integers from 0 to 6. Previous valid results remain visible.', false); return; }
    const [p, q, r] = dims, prior = ranks.slice();
    ranks[0] = Math.min(ranks[0], p, q); ranks[1] = Math.min(ranks[1], r, q - ranks[0]);
    setOptions($('rankU'), Math.min(p, q), ranks[0]); setOptions($('rankV'), Math.min(r, q - ranks[0]), ranks[1]);
    const result = a3(p, q, r, ...ranks), labels = ['M<sub>12</sub>', 'M<sub>23</sub>', 'S<sub>1</sub>', 'S<sub>2</sub>', 'S<sub>3</sub>'];
    $('a3Decomposition').innerHTML = result.multiplicities.map((m, i) => m ? labels[i] + (m > 1 ? `<sup>⊕${m}</sup>` : '') : '').filter(Boolean).join(' ⊕ ') || '0 (the zero representation)';
    $('a3Dimensions').textContent = `Dimensions of H⁰, H¹, H² = (${result.cohomology.join(', ')}). The middle dimension is q − u − v = ${q} − ${ranks[0]} − ${ranks[1]} = ${result.cohomology[1]}.`;
    $('a3GeometryNote').textContent = p === 1 && q === 1 && r === 1 ? 'Here the equation is xy = 0. The maximal rank pairs (1,0) and (0,1) describe two different irreducible components; their intersection has rank pair (0,0).' : p === 1 && q === 2 && r === 1 ? 'Here the equation is x₁y₁ + x₂y₂ = 0. The rank-(1,1) locus is dense in the three-dimensional quadric over the field; the linked 4D lab displays its real cone.' : 'The diagram gives a canonical representative of the selected isomorphism class. A change of basis generally changes its matrices, while preserving ranks and summand multiplicities.';
    status('a3Status', `${result.pairs.length} allowable rank pairs. Selected (${ranks.join(', ')}); VU = 0 exactly.` + (prior.some((x, i) => x !== ranks[i]) ? ' Ranks were adjusted to fit the new dimensions.' : ''));
    $('rankPairs').innerHTML = result.pairs.map(([u, v]) => `<button type="button" data-u="${u}" data-v="${v}" aria-pressed="${u === ranks[0] && v === ranks[1]}" aria-label="Set rank U to ${u} and rank V to ${v}">(${u}, ${v})</button>`).join('');
    $('a3Matrices').innerHTML = matrixTable('U', result.U, q, p) + matrixTable('V', result.V, r, q) + matrixTable('VU', result.VU, r, p);
    $('a3Composition').textContent = `Every one of the ${p * r} entries in VU is zero. Identity blocks give ranks ${ranks[0]} and ${ranks[1]} over every field.`;
    renderA3Diagram(result);
  }
  dimensions.forEach(input => input.addEventListener('input', renderA3));
  $('rankU').addEventListener('change', event => { ranks[0] = Number(event.target.value); renderA3(); });
  $('rankV').addEventListener('change', event => { ranks[1] = Number(event.target.value); renderA3(); });
  $('rankPairs').addEventListener('click', event => {
    const button = event.target.closest('button[data-u]'); if (!button) return;
    ranks = [Number(button.dataset.u), Number(button.dataset.v)]; renderA3();
    $('rankPairs').querySelector(`button[data-u="${ranks[0]}"][data-v="${ranks[1]}"]`).focus({ preventScroll: true });
  });
  function a3Preset(dims, pair) { dimensions.forEach((input, i) => { input.value = String(dims[i]); }); ranks = pair; renderA3(); }
  $('a3Quadric').addEventListener('click', () => a3Preset([1, 2, 1], [1, 1]));
  $('a3Nodal').addEventListener('click', () => a3Preset([1, 1, 1], [1, 0]));
  $('a3Larger').addEventListener('click', () => a3Preset([3, 4, 2], [2, 1]));

  const generatorInputs = [];
  names.forEach((name, i) => {
    const label = document.createElement('label'), head = document.createElement('span'), input = document.createElement('input'), expression = document.createElement('span');
    head.className = 'a-generator-name'; head.innerHTML = `<span>${variableHTML(name)}</span>`;
    input.type = 'number'; input.min = '0'; input.max = '12'; input.step = '1'; input.value = '0'; input.setAttribute('aria-label', `Exponent of ${name}, from zero to twelve`);
    expression.className = 'a-generator-monomial'; expression.innerHTML = monomial(generatorVectors[i], coordinateNames);
    head.append(input); label.append(head, expression); $('generatorControls').append(label); generatorInputs.push(input);
    input.addEventListener('input', renderMatching);
  });
  function renderMatching() {
    const values = readBounded(generatorInputs, 0, 12);
    if (!values) { status('matchingStatus', 'Calculation paused: use integer exponents from 0 to 12. Previous valid results remain visible.', false); return; }
    const result = matchingNormalForm(values);
    $('matchingInput').innerHTML = monomial(result.input, names); $('matchingOutput').innerHTML = monomial(result.normal, names);
    status('matchingStatus', result.preserved ? `All ten coordinates agree. All four balance equations hold. Weighted degree: ${result.degree}.` : 'An exponent mismatch was detected.', result.preserved && result.balance.every(x => x.residual === 0n));
    $('matchingSteps').textContent = `Remove ${result.yPairs} Y₁Y₂ pairs and ${result.zPairs} Z₁Z₂ pairs. Remaining paired Y or Z factors: 0.`;
    const delta = result.after.map((x, i) => x - result.before[i]);
    $('matchingVectors').innerHTML = [['Input', result.before], ['Normal form', result.after], ['Difference', delta]].map(([name, vector]) => `<tr><th scope="row">${name}</th>${vector.map(x => `<td>${x}</td>`).join('')}</tr>`).join('');
    const equations = ['a₁+a₂ = a₄+a₅', 'b₁+b₂ = b₄+b₅', 'a₂+a₃ = b₂+b₃', 'a₃+a₄ = b₃+b₄'];
    $('matchingBalances').innerHTML = result.balance.map((b, i) => `<div><p>${equations[i]}</p><strong>${b.left} = ${b.right} · residual ${b.residual}</strong></div>`).join('');
  }
  function setGenerators(values) { generatorInputs.forEach((input, i) => { input.value = String(values[i]); }); renderMatching(); }
  $('matchingMixed').addEventListener('click', () => setGenerators([0, 0, 2, 1, 1, 3, 0, 0]));
  $('matchingY').addEventListener('click', () => setGenerators([0, 0, 1, 1, 0, 0, 0, 0]));
  $('matchingZ').addEventListener('click', () => setGenerators([0, 0, 0, 0, 1, 1, 0, 0]));
  $('matchingOne').addEventListener('click', () => setGenerators(Array(8).fill(0)));
  const correctLeft = matchingVector([0,0,1,1,0,0,0,0]), incorrectRight = matchingVector([1,1,0,0,0,0,0,1]);
  $('matchingCorrection').textContent = `For the printed B₂ alternative, the vector of Y₁Y₂ is (${correctLeft.join(', ')}), but the vector of B₂X₁X₂ is (${incorrectRight.join(', ')}). They differ. The B₁ replacement agrees in every coordinate, as the first relation preset verifies.`;

  renderMinors(); renderTableau(); renderA3(); setGenerators([0, 0, 2, 1, 1, 3, 0, 0]);
})(typeof globalThis !== 'undefined' ? globalThis : this);
