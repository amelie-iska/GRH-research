"""Independent read-only NumPy/provenance review. Writes only review evidence."""
from pathlib import Path
import hashlib, json, statistics, sys
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'outputs/experiments/learned-frontier'
OUT = ROOT / 'outputs/checks/2026-11-04-learned-frontier/review'
read = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    runs = [read(BASE / name / 'record.json') for name in
            ['generative-20261104-v1', 'generative-20261104-seed2', 'generative-20261104-seed3']]
    summary = read(ROOT / 'web/data/learned-frontier/summary.json')
    hashes = []
    for name, run in zip(['generative-20261104-v1', 'generative-20261104-seed2', 'generative-20261104-seed3'], runs):
        assert len(run['records']) == 4
        for record in run['records']:
            p = BASE / name / record['checkpoint']
            assert sha(p) == record['checkpoint_sha256']
            assert (record['steps'], record['batch'], record['parameters']) == (2000, 512, 5810)
            assert record['train_count'] == 16384 and record['heldout_count'] == 4096
            hashes.append({'file': str(p.relative_to(ROOT)), 'sha256': sha(p)})
    for i, row in enumerate(summary['summary']):
        records = [run['records'][i] for run in runs]
        assert row['seeds'] == [20261104, 20261105, 20261106]
        for key, value in row['metrics'].items():
            xs = [r['evaluation'][key] for r in records]
            assert abs(value['mean'] - statistics.mean(xs)) < 1e-15
            assert abs(value['std'] - statistics.stdev(xs)) < 1e-15
    # Independent Pauli-Kronecker construction: black0,black1,white0,...,white4.
    X = np.array([[0., 1.], [1., 0.]])
    Z = np.diag([1., -1.])
    def op(M, q):
        A = np.array([[1.]])
        for j in range(7):
            A = np.kron(A, M if j == q else np.eye(2))
        return A
    xs, zs = [op(X, q) for q in range(7)], [op(Z, q) for q in range(7)]
    H = -.55 * sum(xs) - .12 * zs[0] + .072 * zs[1]
    for j in range(5):
        H -= .5 * zs[0] @ zs[j+2] + .35 * (-1)**j * zs[1] @ zs[j+2]
        H -= (.045 * np.cos(1.7*j) + .02*j/5) * zs[j+2]
    es, U = np.linalg.eigh(H)
    w = np.exp(-es + es.min()); w /= w.sum()
    rho = (U*w) @ U.T
    reduced = sum(rho.reshape(4,32,4,32)[:,j,:,j] for j in range(32))
    stored = np.asarray(runs[0]['teacher']['reduced_density'])
    teacher_error = float(abs(reduced-stored).max())
    assert teacher_error < 3e-10
    # Replay all learned coherent states using explicit basis-pair updates.
    flow = summary['state_flow']
    flow_path = BASE / 'state-flow-20261104-v1/state-flow.pt'
    assert sha(flow_path) == flow['checkpoint_sha256']
    hashes.append({'file': str(flow_path.relative_to(ROOT)), 'sha256': sha(flow_path)})
    th, om = np.array(flow['theta']), np.array(flow['omega'])
    eigen, V = np.linalg.eigh(stored)
    density_errors, fidelity_errors = [], []
    for row in flow['rows']:
        t = row['t']; state = np.zeros(16, complex); state[[0,5,10,15]] = .5
        def cnot(a,b):
            nonlocal state
            output = np.zeros(16, complex)
            for i in range(16):
                output[i ^ (((i >> (3-a)) & 1) << (3-b))] = state[i]
            state = output
        for layer in range(6):
            pairs = [(q,(q+1+layer%3)%4) for q in range(4)]
            for a,b in pairs: cnot(a,b)
            for q in range(4):
                angle = t*th[layer,q] + t*t*om[layer,q]
                c,s = np.cos(angle/2),np.sin(angle/2)
                for i in range(16):
                    if not i & (1 << (3-q)):
                        j = i | (1 << (3-q))
                        state[i],state[j] = c*state[i]-s*state[j],s*state[i]+c*state[j]
            for a,b in reversed(pairs): cnot(a,b)
        mat = state.reshape(4,4); actual = mat @ mat.conj().T
        target = ((V*np.sqrt((1-t)/4 + t*eigen)) @ V.T).reshape(16)
        fidelity = float(abs(np.vdot(target,state))**2)
        saved = np.array(row['density_real']) + 1j*np.array(row['density_imag'])
        density_errors.append(float(abs(actual-saved).max()))
        fidelity_errors.append(abs(fidelity-row['fidelity']))
        assert abs(np.trace(actual)-1) < 1e-12 and np.linalg.eigvalsh(actual).min() > -1e-12
    assert max(density_errors) < 1e-6 and max(fidelity_errors) < 2e-6
    # Frozen-feature result reproduced using its local existing NumPy code.
    sys.path.insert(0, str(ROOT / 'examples/learned_frontier'))
    from width_limits import run
    width = run()
    width_error = max(abs(x[k]-y[k]) for x,y in zip(width['rows'],summary['width']['rows'])
                      for k in x if isinstance(x[k],float))
    assert width_error < 1e-7
    source_hashes = []
    manifest = read(ROOT / 'web/data/learned-frontier/manifest.json')
    for entry in manifest['traces']:
        p = ROOT / 'web/data/learned-frontier' / entry['file']
        assert sha(p) == entry['sha256']
        for key, value in read(p)['provenance'].items():
            if isinstance(value,dict) and 'path' in value and 'sha256' in value:
                actual = sha(ROOT/value['path'])
                source_hashes.append({'trace': entry['id'], 'role': key, 'matches': actual == value['sha256']})
    assert all(s['matches'] for s in source_hashes)
    result = dict(passed=True, scope='Local CPU review; no Torch, checkpoint deserialization, training or GPU rerun',
                  checkpoints=hashes, aggregate_metrics_match=True,
                  teacher_max_error=teacher_error,
                  coherent_replay_max_density_error=max(density_errors),
                  coherent_replay_max_fidelity_error=max(fidelity_errors),
                  coherent_grid_count=len(flow['rows']),
                  width_reproduction_max_difference=width_error,
                  trace_provenance_hash_checks=source_hashes)
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'integrated-python.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['checkpoints','trace_provenance_hash_checks']},indent=2))

if __name__ == '__main__': main()
