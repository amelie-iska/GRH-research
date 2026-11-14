"""Focused numerical replay tests for the two trained component DAGs."""
import hashlib,json,unittest
import numpy as np
from model import ROOT
from export_components import concept_trace,gfn_trace

class Components(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/'web/data/quantum-tokengt/manifest.json').read_text());raw=(ROOT/'web/data/quantum-tokengt'/cls.manifest['file']).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==cls.manifest['sha256'];cls.record=json.loads(raw);cls.checkpoint=ROOT/cls.manifest['run']/'record.json'
    def test_critic(self):
        t=concept_trace(self.record,self.checkpoint);nodes={v['id']:v for v in t['nodes']}
        self.assertIn('empirical_MI_functional',nodes);self.assertIn('critic.softmax',nodes);self.assertTrue(all('gate' not in v for v in t['nodes']))
        p=np.array(nodes['critic.softmax']['tensor']['values']);np.testing.assert_allclose(p.sum(),1,atol=1e-13)
        ce=float(nodes['heldout_CE']['tensor']['values']);self.assertAlmostEqual(ce,self.record['concepts']['heldout_cross_entropy'],delta=1e-11)
    def test_continuous_gfn(self):
        t=gfn_trace(self.record,self.checkpoint);nodes={v['id']:v for v in t['nodes']}
        self.assertEqual(t['nodes'][-1]['id'],'TB_residual');self.assertTrue(all('gate' not in v for v in t['nodes']))
        self.assertIn('step2.backward_density',nodes);self.assertIn('step3.forward_density',nodes)
        self.assertEqual(nodes['root.mass']['tensor']['values'],1.)
        self.assertLess(max(v['error'] for v in t['checks'].values()),1e-11)
if __name__=='__main__':unittest.main()
