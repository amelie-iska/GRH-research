/** Exact eight-amplitude reference; no network, libraries, training or hidden state. */
export function simulateWeylToken(angles, theta, trace = false) {
  if (!Array.isArray(angles) || angles.length !== 6 || angles.some(x => !Number.isFinite(x)) ||
      !Array.isArray(theta) || theta.length !== 2 || theta.some(layer =>
        !Array.isArray(layer) || layer.length !== 3 || layer.some(pair =>
          !Array.isArray(pair) || pair.length !== 2 || pair.some(x => !Number.isFinite(x))))) {
    throw new TypeError('Expected finite angles[6] and theta[2][3][2].');
  }
  let re = [1, 0, 0, 0, 0, 0, 0, 0], im = Array(8).fill(0);
  const gateTrace = [];
  const save = (gate, layer, qubits, angle = null) => {
    if (trace) gateTrace.push({gate, layer, qubits, angle, state: {real: [...re], imag: [...im]}});
  };
  for (let layer = 0; layer < 2; ++layer) {
    for (let q = 0; q < 3; ++q) {
      const bitMask = 1 << (2 - q), ry = angles[q] + theta[layer][q][0];
      const c = Math.cos(ry / 2), s = Math.sin(ry / 2);
      const r = Array(8), z = Array(8);
      for (let i = 0; i < 8; ++i) {
        const sign = (i & bitMask) ? 1 : -1;
        r[i] = c * re[i] + sign * s * re[i ^ bitMask];
        z[i] = c * im[i] + sign * s * im[i ^ bitMask];
      }
      re = r; im = z; save('RY', layer, [q], ry);
      const rz = angles[q + 3] + theta[layer][q][1];
      for (let i = 0; i < 8; ++i) {
        const phase = ((i & bitMask) ? 1 : -1) * rz / 2;
        const a = re[i], b = im[i], cp = Math.cos(phase), sp = Math.sin(phase);
        re[i] = cp * a - sp * b; im[i] = sp * a + cp * b;
      }
      save('RZ', layer, [q], rz);
    }
    for (const [control, target] of [[0, 1], [1, 2]]) {
      const r = Array(8), z = Array(8);
      for (let i = 0; i < 8; ++i) {
        const source = (i & (1 << (2 - control))) ? i ^ (1 << (2 - target)) : i;
        r[i] = re[source]; z[i] = im[source];
      }
      re = r; im = z; save('CNOT', layer, [control, target]);
    }
  }
  let ur = 0, ui = 0, vr = 0, vi = 0, uvr = 0, uvi = 0, norm = 0;
  for (let i = 0; i < 8; ++i) {
    const j = (i + 1) % 8, c = Math.cos(2 * Math.PI * i / 8), s = Math.sin(2 * Math.PI * i / 8);
    const p = re[i] ** 2 + im[i] ** 2;
    const cr = re[i] * re[j] + im[i] * im[j], ci = re[i] * im[j] - im[i] * re[j];
    norm += p; ur += c * p; ui += s * p; vr += cr; vi += ci;
    uvr += c * cr - s * ci; uvi += s * cr + c * ci;
  }
  return {state: {real: re, imag: im}, features: [ur, ui, vr, vi, uvr, uvi], norm, gateTrace};
}

export function parameterShiftJacobian(angles, theta) {
  const jac = Array.from({length: 6}, () => Array(12).fill(0));
  for (let p = 0; p < 12; ++p) {
    const layer = Math.floor(p / 6), q = Math.floor((p % 6) / 2), axis = p % 2;
    const plus = theta.map(row => row.map(pair => [...pair]));
    const minus = theta.map(row => row.map(pair => [...pair]));
    plus[layer][q][axis] += Math.PI / 2; minus[layer][q][axis] -= Math.PI / 2;
    const a = simulateWeylToken(angles, plus).features, b = simulateWeylToken(angles, minus).features;
    for (let f = 0; f < 6; ++f) jac[f][p] = (a[f] - b[f]) / 2;
  }
  return jac;
}
