import json,math,subprocess,sys,unittest
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'workbench'))
from quantum_surface import MODEL,DEFAULT,configuration,controller,cpu_state,observable,execute_cpu
CORE=ROOT/'workbench/site/surface-core.js'
class SurfaceQuantum(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.model=json.loads(MODEL.read_text())
 def node(self,code,payload):
  source='const fs=require("fs"),S=require(process.argv[1]),p=JSON.parse(fs.readFileSync(0,"utf8"));'+code
  out=subprocess.run(['node','-e',source,str(CORE)],input=json.dumps(payload),capture_output=True,text=True,check=True)
  return json.loads(out.stdout)
 def test_topology(self):
  r=self.node('console.log(JSON.stringify(S.topology(p)));',self.model)
  self.assertEqual((r['genus'],r['physicalQubits'],r['darts'],r['logicalQubits']),(1,18,36,2))
 def test_controller_parity(self):
  rng=np.random.default_rng(20261114);cases=[dict(DEFAULT,mode=m,qx=float(rng.uniform(-2,2)),qy=float(rng.uniform(-2,2)),gain=float(rng.random()),tau=float(rng.uniform(.1,1)))for m in ('maxplus','softmax','hard')for _ in range(35)]
  rows=self.node('console.log(JSON.stringify(p.cases.map(c=>S.attention(p.model,c))));',dict(model=self.model,cases=cases))
  for c,r in zip(cases,rows):
   a=controller(self.model,c);np.testing.assert_allclose(a['output'],r['output'],atol=2e-14,rtol=2e-14);np.testing.assert_allclose(a['theta'],r['theta'],atol=2e-14,rtol=2e-14)
 def test_actual_circuit_browser_python(self):
  qpath=str(ROOT/'extension/site/quantum-core.js')
  code='const Q=require('+json.dumps(qpath)+');console.log(JSON.stringify(S.simulate(Q,p.model,p.config)));'
  r=self.node(code,dict(model=self.model,config=DEFAULT));c=execute_cpu(self.model,DEFAULT)
  self.assertAlmostEqual(r['expectation'],c['expectation'],places=12)
  np.testing.assert_allclose(r['probability'],c['probability'],atol=2e-13)
  self.assertAlmostEqual(r['energy'],c['energy'],places=11)
 def test_preparation_stabilizers(self):
  state=cpu_state(self.model)
  for key,p in [('x_checks','X'),('z_checks','Z')]:
   for c in self.model[key]:self.assertAlmostEqual(observable(state,c['qubits'],p),1,places=12)
 def test_zero_controller_bypass(self):
  for m in ('maxplus','softmax','hard'):np.testing.assert_allclose(controller(self.model,dict(DEFAULT,mode=m,gain=0))['theta'],DEFAULT['base'])
 def test_domains(self):
  for name,value in [('gain',True),('qx',float('nan')),('tau',0),('mode','coherent-maxplus')]:
   with self.assertRaises(ValueError):configuration(dict(DEFAULT,**{name:value}))
 def test_no_dart_qubit_confusion(self):
  self.assertEqual(len(self.model['permutations']['sigma1']),2*self.model['n']);self.assertTrue(all(g['target']<18 for g in self.model['prepare_circuit']))

if __name__=='__main__':unittest.main(verbosity=2)
