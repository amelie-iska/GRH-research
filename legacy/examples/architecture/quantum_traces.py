"""Gate-by-gate replay of the existing six trained CPU models, without training."""
from fractions import Fraction
from itertools import combinations, product
import json
import sys
import numpy as np
from scipy.linalg import block_diag
from scipy.sparse import csr_matrix, diags
from scipy.sparse.linalg import eigsh
from trace_schema import ROOT, Trace, source

sys.path.insert(0, str(ROOT / "examples/quantum"))
from surface_models import ry, rz, ansatz, encoded_patch, graph_hamiltonian

RENORM = "outputs/experiments/renormalization-pennylane/training.json"
PHOTON = "outputs/experiments/photonic-pooling/photonic.json"
HARPER = "outputs/experiments/toricgt-hybrid/training.json"
LARGE = "outputs/experiments/higher-genus-qcnn/training.json"
OBSERVABLES = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
CZ = np.diag([1, 1, 1, -1]).astype(complex)
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], complex)


def read(path):
    return json.loads((ROOT / path).read_text())


def trained(identity, title, category, path, seed, case, script, split="saved held-out example"):
    return Trace(identity, title, category,
        dict(kind="trained-checkpoint-replay", seed=seed, checkpoint=source(path),
             training_source=source(script), case=case, split=split,
             implementation=source(__file__), backend="NumPy/SciPy CPU replay; original training used pinned quantum backends",
             scope="Finite numerical experiment. Neither a faithful completed-order representation nor a GRH proof."),
        dict(wires="qubit 0 most significant; column state vectors", shots=None,
             angles="radians", training="Parameters replayed unchanged; no optimizer steps"))


def apply_gate(state, gate, wires, n):
    """Small gate on ordered wires; avoids full 512-by-512 nine-qubit gates."""
    order = list(wires) + [q for q in range(n) if q not in wires]
    a = state.reshape([2] * n).transpose(order).reshape(2 ** len(wires), -1)
    return (gate @ a).reshape([2] * n).transpose(np.argsort(order)).reshape(-1)


def circuit(t, prefix, state, theta, n, keep=None):
    previous = t.add(prefix + ".input", state, "Normalized input state", axes=["basis"])
    gates = []
    for layer, params in enumerate(np.asarray(theta).reshape(2, n, 2)):
        for q, (a, b) in enumerate(params):
            gates.extend([(f"layer{layer}.ry{q}", ry(a), [q], "RY", float(a)),
                          (f"layer{layer}.rz{q}", rz(b), [q], "RZ", float(b))])
        edges = [(0, 1)] if n == 2 else [(q, (q + 1) % n) for q in range(n)]
        gates.extend((f"layer{layer}.cz{a}_{b}", CZ, [a, b], "CZ", None) for a, b in edges)
    keep = n // 2 if keep is None else keep
    gates.extend((f"pool{q}_{keep+q}", CNOT, [q, keep + q], "CNOT", None) for q in range(n - keep))
    for suffix, gate, wires, name, angle in gates:
        state = apply_gate(state, gate, wires, n)
        previous = t.add(prefix + "." + suffix, state, f"{name} on ordered wires {wires}",
            [previous, "parameters"], ["basis"], gate=name, wires=wires, angle=angle)
    t.check(prefix + ".normalization", abs(np.vdot(state, state) - 1))
    return state, previous


def features(t, prefix, angles, theta):
    state, last = circuit(t, prefix, encoded_patch(angles), theta, 2)
    probabilities = abs(state) ** 2
    p = t.add(prefix + ".probability", probabilities, "p_b = |psi_b|^2", [last], ["basis"])
    value = probabilities @ OBSERVABLES
    f = t.add(prefix + ".features", value, "(<Z0>, <Z1>, <Z0 Z1>)", [p], ["observable"])
    # Independent dense implementation used by the original training scripts.
    reference = ansatz(theta, 2, [(0, 1)]) @ encoded_patch(angles)
    t.check(prefix + ".dense_state_agreement", np.max(abs(state - reference)))
    return value, f


def finite_ground(n, h):
    if n == 4:
        H = graph_hamiltonian(n, [(q, (q + 1) % n) for q in range(n)], h)
        val, vec = np.linalg.eigh(H)
        return vec[:, 0], float(val[0]), float(np.linalg.norm(H @ vec[:, 0] - val[0] * vec[:, 0]))
    d = 2 ** n
    indices = np.arange(d)
    bits = [1 - 2 * ((indices >> (n - 1 - q)) & 1) for q in range(n)]
    zz = -sum(bits[q] * bits[(q + 1) % n] for q in range(n))
    sx = csr_matrix((np.ones(n * d), (np.tile(indices, n),
        np.concatenate([indices ^ (1 << (n - 1 - q)) for q in range(n)]))), shape=(d, d))
    H = diags(zz) - h * sx
    val, vec = eigsh(H, k=1, which="SA", tol=1e-12, v0=np.ones(d) / np.sqrt(d))
    return vec[:, 0].astype(complex), float(val[0]), float(np.linalg.norm(H @ vec[:, 0] - val[0] * vec[:, 0]))


def qcnn(n, data, model, path, case):
    keep = 5 if n == 9 else 2
    sample = model["examples"][case]
    t = trained(f"qcnn-{n}-{case}", model["name"], "quantum-qcnn", path,
        data["seed"], case, "examples/quantum/train_higher_genus_qcnn.py" if n == 9 else "examples/quantum/train_pennylane.py")
    t.add("parameters", model["theta"], "Saved trained parameters", axes=["parameter"])
    state, energy, residual = finite_ground(n, sample["h"])
    t.data["input"] = dict(h=sample["h"], qubits=n, retained=keep, energy=energy,
                           eigen_residual=residual, numerical_ground_state=True)
    state, last = circuit(t, "circuit", state, model["theta"], n, keep)
    A = state.reshape(2 ** keep, 2 ** (n - keep))
    rho = A @ A.conj().T
    density = t.add("retained_density", rho, "rho_keep = A A*; trace out final wires", [last], ["row", "column"])
    discard = 1 - np.sum(abs(A[:, 0]) ** 2)
    t.add("discard_probability", discard, "1 - Pr(discarded wires all zero)", [last])
    t.check("saved_discard", abs(discard - sample["discard_probability"]))
    t.check("trace_one", abs(np.trace(rho) - 1))
    t.check("density_hermitian", np.max(abs(rho - rho.conj().T)))
    t.check("density_psd", max(0, -np.linalg.eigvalsh(rho)[0]))
    t.check("eigen_residual", residual, 1e-8)
    if "kept_density" in sample:
        saved = np.asarray(sample["kept_density"])
        t.check("saved_density", np.max(abs(rho - saved[..., 0] - 1j * saved[..., 1])))
    else:
        t.check("saved_energy", abs(energy - sample["ground_energy"]))
    return t.finish()


def convolution(data, case):
    m = data["models"][1]; s = m["examples"][case]
    t = trained(f"quantum-convolution-{case}", m["name"], "quantum-convolution", RENORM,
                data["seed"], case, "examples/quantum/train_pennylane.py")
    t.add("parameters", m["theta"], "Saved circuit weights", axes=["parameter"])
    t.add("head", m["head"], "Saved affine head", axes=["parameter"])
    f, node = features(t, "patch", [s["k1"], s["k2"]], m["theta"])
    prediction = f @ m["head"][:3] + m["head"][3]
    t.add("prediction", prediction, "features dot head[:3] + head[3]", [node, "head"])
    exact = np.arctanh(np.tanh(s["k1"]) * np.tanh(s["k2"]))
    t.add("exact_target", exact, "atanh(tanh(k1) tanh(k2)); finite Ising decimation")
    t.data["input"] = dict(k1=s["k1"], k2=s["k2"])
    t.check("saved_prediction", abs(prediction - s["prediction"]))
    t.check("target", abs(exact - s["exact"]))
    return t.finish()


def quantum_attention(data, case):
    m = data["models"][2]; s = m["examples"][case]; p = np.array(m["theta"])
    t = trained(f"quantum-attention-{case}", m["name"], "quantum-classical-attention", RENORM,
                data["seed"], case, "examples/quantum/train_pennylane.py")
    t.add("parameters", p, "Saved gate/query/local/context/bias weights", axes=["parameter"])
    pairs = [(0, 1), (1, 2), (2, 0)]
    values, nodes = [], []
    for k, (i, j) in enumerate(pairs):
        f, node = features(t, f"patch{k}", [s["couplings"][i], s["couplings"][j]], p[:8])
        values.append(f); nodes.append(node)
    F = np.array(values)
    fs = t.add("patch_features", F, "Stack shared quantum feature vectors", nodes, ["patch", "observable"])
    logits = F @ p[8:11]
    l = t.add("logits", logits, "F dot query", [fs, "parameters"], ["patch"])
    weights = np.exp(logits - logits.max()); weights /= weights.sum()
    w = t.add("attention", weights, "softmax over the three patches", [l], ["patch"])
    context = weights @ F
    c = t.add("context", context, "sum_patch attention * F", [w, fs], ["observable"])
    prediction = F @ p[11:14] + context @ p[14:17] + p[17]
    t.add("prediction", prediction, "F local + context context_head + bias", [fs, c, "parameters"], ["pair"])
    spins = np.array(list(product([-1, 1], repeat=3)))
    potential = np.log(2 * np.cosh(spins @ s["couplings"]))
    exact = np.array([np.mean(potential * spins[:, i] * spins[:, j]) for i, j in pairs])
    t.add("exact_target", exact, "mean_s log(2 cosh(K dot s)) s_i s_j", axes=["pair"])
    t.data["input"] = dict(couplings=s["couplings"], pairs=pairs)
    t.check("saved_prediction", np.max(abs(prediction - s["prediction"])))
    t.check("saved_attention", np.max(abs(weights - s["attention"])))
    t.check("target", np.max(abs(exact - s["exact"])))
    return t.finish()


def photonic(data, case):
    s = data["examples"][case]; r = s["squeezing"]
    t = trained(f"photonic-{case}", "Trained Gaussian principal-axis pooling", "photonic-gaussian", PHOTON,
                data["seed"], case, "examples/quantum/train_photonic.py")
    t.data["conventions"].update(covariance="x0,x1,p0,p1; hbar=2; vacuum covariance I4")
    t.data["input"] = dict(squeezing=r, source_angle=data["source_angle"], trained_angle=data["final_angle"])
    cov = np.diag([np.exp(-2*r), np.exp(2*r), np.exp(2*r), np.exp(-2*r)])
    last = t.add("squeezed_covariance", cov, "S(r) tensor S(-r) vacuum covariance", axes=["quadrature", "quadrature_prime"])
    for name, a in [("source", data["source_angle"]), ("trained", data["final_angle"])]:
        R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
        S = block_diag(R, R)
        sym = t.add(name + ".symplectic", S, "phi=0 passive beamsplitter diag(R,R)", axes=["quadrature", "quadrature_prime"])
        cov = S @ cov @ S.T
        last = t.add(name + ".covariance", cov, "V_out = S V_in S^T", [last, sym], ["quadrature", "quadrature_prime"])
    value = cov[0, 0] + cov[3, 3]
    t.add("objective", value, "Var(x0) + Var(p1)", [last])
    t.check("saved_objective", abs(value - s["objective"]))
    t.check("uncertainty", max(0, -np.linalg.eigvalsh(cov + 1j*np.block([[np.zeros((2,2)), np.eye(2)], [-np.eye(2), np.zeros((2,2))]]))[0]))
    return t.finish()


def determinant(a):
    """Independent exact Leibniz determinant for at most four by four matrices."""
    from itertools import permutations
    result = Fraction(0)
    for p in permutations(range(len(a))):
        sign = (-1) ** sum(p[i] > p[j] for i in range(len(a)) for j in range(i+1, len(a)))
        term = Fraction(sign)
        for i, j in enumerate(p):
            term *= a[i][j]
        result += term
    return result


def harper(data, case):
    s = data["examples"][case]; lam = Fraction(s["lambda_rational"]); x = float(lam); p = np.array(data["theta"])
    t = trained(f"toricgt-quantum-hybrid-{case}", data["name"], "quantum-classical-toricgt", HARPER,
        data["seed"], case, "examples/quantum/toricgt_hybrid.py", "saved rational certificate probe, not a held-out training row")
    t.add("parameters", p, "Saved quantum features and affine readout", axes=["parameter"])
    U = np.diag(1j ** np.arange(4)); V = np.roll(np.eye(4), -1, axis=0)
    u = t.add("U", U, "diag(i^j)", axes=["row", "column"])
    v = t.add("V", V, "backward cyclic shift V e_j = e_(j-1)", axes=["row", "column"])
    H = U + U.conj().T + x * (V + V.conj().T)
    hn = t.add("harper", H, "H_lambda=U+U*+lambda(V+V*)", [u, v], ["row", "column"])
    f, fn = features(t, "patch", [x, .7*x*x], p[:8])
    proposal = 6 * (f @ p[8:11] + p[11])
    t.add("proposal", proposal, "6 * affine(quantum_features)", [fn, "parameters"])
    eig = np.linalg.eigvalsh(H)
    t.add("spectrum", eig, "Numerical Hermitian eigenspectrum", [hn], ["eigenvalue"])
    exact_h = [[Fraction([2, 0, -2, 0][i]) if i == j else lam if (i-j)%4 in [1, 3] else Fraction(0) for j in range(4)] for i in range(4)]
    def principal_minors(bound):
        a = [[exact_h[i][j] - (bound if i == j else 0) for j in range(4)] for i in range(4)]
        return [determinant([[a[i][j] for j in ids] for i in ids]) for size in range(1,5) for ids in combinations(range(4), size)]
    lower, upper, trial = map(Fraction, [s["certified_lower"], s["certified_upper_bracket"], s["rational_trial"]])
    minors = principal_minors(lower)
    if [str(z) for z in minors] != s["principal_minors"] or not all(z >= 0 for z in minors):
        raise AssertionError("Rational PSD certificate failed")
    accepted = all(z >= 0 for z in principal_minors(trial))
    if accepted != s["proposal_accepted"] or not (upper == -2 or any(z < 0 for z in principal_minors(upper))):
        raise AssertionError("Rational accept/repair or upper-bracket check failed")
    t.data["certificate"] = dict(s, checked_by="independent Fraction Leibniz determinants; all principal minors")
    t.data["input"] = dict(lambda_rational=str(lam), normalization=6)
    t.check("saved_proposal", abs(proposal - s["learned_proposal"]))
    t.check("weyl_relation_VU_iUV", np.linalg.norm(V @ U - 1j * U @ V))
    t.check("analytic_lowest", abs(eig[0] + 2*np.sqrt(1+x*x)))
    t.check("numerical_bracket", max(0, float(lower)-eig[0], eig[0]-float(upper)))
    return t.finish()


def all_traces():
    data = read(RENORM); large = read(LARGE); photon = read(PHOTON); hybrid = read(HARPER)
    for case in (0, -1):
        # Positive stable IDs rather than Python's negative indexing notation.
        yield qcnn(4, data, data["models"][0], RENORM, case % len(data["models"][0]["examples"]))
        yield qcnn(9, large, large, LARGE, case % len(large["examples"]))
        yield convolution(data, case % len(data["models"][1]["examples"]))
        yield quantum_attention(data, case % len(data["models"][2]["examples"]))
        yield photonic(photon, case % len(photon["examples"]))
    for case in range(len(hybrid["examples"])):
        yield harper(hybrid, case)
