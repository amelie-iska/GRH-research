/* Deterministic dense state-vector kernel. No external dependencies.
 * Qubit q is bit q (least-significant-bit convention).
 * Two Float64 arrays use 16 * 2^n bytes per state. */
(function (root) {
  'use strict';
  const TAU = 2 * Math.PI;
  function popcount(x) { let n = 0; while (x) { x &= x - 1; n++; } return n; }
  function maskOf(qubits) { return qubits.reduce((m, q) => m ^ (1 << q), 0); }
  function gateQubits(g) {
    if (Array.isArray(g.qubits)) return g.qubits;
    return g.control == null ? [g.target] : [g.control, g.target];
  }
  class StateVector {
    constructor(n) {
      if (!Number.isInteger(n) || n < 1 || n > 20) throw new Error('Dense browser kernel supports 1–20 qubits; this companion limits live cases to 18.');
      this.n = n; this.size = 2 ** n;
      this.re = new Float64Array(this.size); this.im = new Float64Array(this.size);
      this.re[0] = 1;
    }
    reset() { this.re.fill(0); this.im.fill(0); this.re[0] = 1; return this; }
    copyFrom(other) {
      if (other.n !== this.n) throw new Error('State sizes differ.');
      this.re.set(other.re); this.im.set(other.im); return this;
    }
    clone() { return new StateVector(this.n).copyFrom(this); }
    apply(g) {
      const op = String(g.gate || g.op || '').toUpperCase(), qs = gateQubits(g);
      if (!qs.length || qs.some(q => !Number.isInteger(q) || q < 0 || q >= this.n)) throw new Error('Gate has an invalid qubit.');
      const q = qs[qs.length - 1], bit = 1 << q, r = this.re, z = this.im, N = this.size;
      if (op === 'CX' || op === 'CNOT' || op === 'CZ') {
        const c = qs[0], cb = 1 << c;
        if (qs.length !== 2 || c === q) throw new Error('Two-qubit gate needs distinct control and target.');
        if (op === 'CZ') {
          for (let i = 0; i < N; i++) if ((i & cb) && (i & bit)) { r[i] = -r[i]; z[i] = -z[i]; }
        } else {
          for (let i = 0; i < N; i++) if ((i & cb) && !(i & bit)) {
            const j = i | bit, a = r[i], b = z[i]; r[i] = r[j]; z[i] = z[j]; r[j] = a; z[j] = b;
          }
        }
        return this;
      }
      if (qs.length !== 1) throw new Error('Single-qubit gate received multiple targets.');
      const angle = Number(g.angle == null ? 0 : g.angle);
      if (!Number.isFinite(angle)) throw new Error('Rotation angle must be finite.');
      if (op === 'Z') {
        for (let i = bit; i < N; i += 2 * bit) for (let j = i; j < i + bit; j++) { r[j] = -r[j]; z[j] = -z[j]; }
      } else if (op === 'RZ') {
        const c = Math.cos(angle / 2), s = Math.sin(angle / 2);
        for (let i = 0; i < N; i++) {
          const a = r[i], b = z[i], t = (i & bit) ? s : -s;
          r[i] = c * a - t * b; z[i] = t * a + c * b;
        }
      } else if (op === 'X' || op === 'H' || op === 'RY') {
        const c = op === 'H' ? Math.SQRT1_2 : Math.cos(angle / 2), s = Math.sin(angle / 2);
        for (let base = 0; base < N; base += 2 * bit) for (let j = 0; j < bit; j++) {
          const i = base + j, k = i + bit, a = r[i], b = z[i], d = r[k], e = z[k];
          if (op === 'X') { r[i] = d; z[i] = e; r[k] = a; z[k] = b; }
          if (op === 'H') { r[i] = c * (a + d); z[i] = c * (b + e); r[k] = c * (a - d); z[k] = c * (b - e); }
          if (op === 'RY') { r[i] = c * a - s * d; z[i] = c * b - s * e; r[k] = s * a + c * d; z[k] = s * b + c * e; }
        }
      } else throw new Error('Unsupported gate: ' + op);
      return this;
    }
    applyCircuit(gates) { for (const g of gates) this.apply(g); return this; }
    expectationX(qubits) {
      const mask = maskOf(qubits), r = this.re, z = this.im; let total = 0;
      for (let i = 0; i < this.size; i++) { const j = i ^ mask; total += r[i] * r[j] + z[i] * z[j]; }
      return total;
    }
    expectationZ(qubits) {
      const mask = maskOf(qubits), r = this.re, z = this.im; let total = 0;
      for (let i = 0; i < this.size; i++) {
        const p = r[i] * r[i] + z[i] * z[i];
        total += (popcount(i & mask) & 1) ? -p : p;
      }
      return total;
    }
    fidelity(other) {
      let r = 0, z = 0;
      for (let i = 0; i < this.size; i++) {
        r += other.re[i] * this.re[i] + other.im[i] * this.im[i];
        z += other.re[i] * this.im[i] - other.im[i] * this.re[i];
      }
      return r * r + z * z;
    }
    statistics() {
      let norm2 = 0, entropy = 0, support = 0;
      const hamming = new Float64Array(this.n + 1), top = [];
      for (let i = 0; i < this.size; i++) {
        const p = this.re[i] ** 2 + this.im[i] ** 2; norm2 += p;
        if (p > 1e-12) { support++; entropy -= p * Math.log2(p); }
        if (p > 0) hamming[popcount(i)] += p;
        if (p > 1e-12 && (top.length < 8 || p > top[top.length - 1].probability)) {
          top.push({basis: i.toString(2).padStart(this.n, '0'), probability: p, phase: Math.atan2(this.im[i], this.re[i])});
          top.sort((a, b) => b.probability - a.probability); if (top.length > 8) top.pop();
        }
      }
      return {norm2, entropy, support, hamming: Array.from(hamming), top};
    }
  }
  function normalizeModel(model) {
    const n = Number(model.n == null ? model.metadata.n : model.n);
    const gates = model.prepare_circuit || model.preparation_circuit || [];
    return {...model, n, prepare_circuit: gates};
  }
  function qnnPatch(model) {
    const p = model.x_checks[0].qubits.slice();
    if (p.length !== 4) throw new Error('The browser QNN uses a four-edge star.');
    return p;
  }
  const trainingSigns = [[1,1,1,1],[-1,1,1,1],[-1,-1,1,1],[1,-1,1,1]];
  const initialTheta = [0.65,-0.4,0.5,-0.6];
  function qnnCircuit(patch, signs, theta) {
    if (patch.length !== 4 || signs.length !== 4 || theta.length !== 4) throw new Error('QNN needs four inputs and four parameters.');
    const gates = patch.map((q, i) => ({gate:'RY',target:q,qubits:[q],angle:signs[i] * Math.PI / 2 + theta[i]}));
    for (let i = 1; i < 4; i++) gates.push({gate:'CX',control:patch[i],target:patch[0],qubits:[patch[i],patch[0]]});
    return gates;
  }
  function parityLabel(signs) { return signs.reduce((a,b) => a*b,1); }
  function allSigns() { return Array.from({length:16},(_,j) => Array.from({length:4},(_,i) => (j & (1 << i)) ? -1 : 1)); }
  function qnnPredict(base, scratch, patch, signs, theta) {
    scratch.copyFrom(base).applyCircuit(qnnCircuit(patch,signs,theta));
    return scratch.expectationZ([patch[0]]);
  }
  function qnnBatch(base, scratch, patch, theta, samples = trainingSigns) {
    return samples.map(signs => ({signs:signs.slice(),target:parityLabel(signs),prediction:qnnPredict(base,scratch,patch,signs,theta)}));
  }
  function mse(rows) { return rows.reduce((s,r) => s+(r.prediction-r.target)**2,0)/rows.length; }
  function qnnGradient(base, scratch, patch, theta) {
    const rows = qnnBatch(base,scratch,patch,theta), gradient = [0,0,0,0];
    for (let j=0;j<4;j++) for (let s=0;s<trainingSigns.length;s++) {
      const plus=theta.slice(),minus=theta.slice(); plus[j]+=Math.PI/2;minus[j]-=Math.PI/2;
      const derivative=(qnnPredict(base,scratch,patch,trainingSigns[s],plus)-qnnPredict(base,scratch,patch,trainingSigns[s],minus))/2;
      gradient[j] += 2*(rows[s].prediction-rows[s].target)*derivative/trainingSigns.length;
    }
    return {gradient,rows,loss:mse(rows)};
  }
  const api={StateVector,popcount,maskOf,gateQubits,normalizeModel,qnnPatch,qnnCircuit,trainingSigns,initialTheta,parityLabel,allSigns,qnnPredict,qnnBatch,qnnGradient,mse,TAU};
  if (typeof module !== 'undefined' && module.exports) module.exports=api;
  else root.QuantumCore=api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
