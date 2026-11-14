"""Focused independent identities; run before and after producing the record."""
import sys, unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from model import attention, persistence, qec_channel, teacher, load_fixture, circuit_features

class Checks(unittest.TestCase):
    def test_rg_teacher(self):
        sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'rg'))
        from rg_math import fine_action, decimate
        p=np.array([.37,-.21,.16]); y=teacher(p)
        coarse=decimate(fine_action(5,p),list(range(2,7)))
        np.testing.assert_allclose(y[:32],coarse,atol=2e-14)
    def test_masked_tropical(self):
        f=np.array([[[1.,0.],[0.,1.],[100.,100.]]]); mask=np.array([True,True,False])
        w=[np.eye(2)]*3
        _,a=attention(f,w,mask,'tropical',True)
        self.assertTrue(np.all(a['context'][:,2]==0));self.assertTrue(np.all(a['weights'][:,:,2]==0))
        expected=np.max(a['scores'][:,:2,:2,None]+f[:,None,:2,:],axis=2)
        np.testing.assert_allclose(a['context'][:,:2],expected)
        _,empty=attention(f,w,np.zeros(3,bool),'hybrid',True)
        np.testing.assert_array_equal(empty['context'],0)
    def test_circle_persistence(self):
        d=np.array([[0,1,2**.5,1],[1,0,1,2**.5],[2**.5,1,0,1],[1,2**.5,1,0]])
        bars=persistence(d)['H1'];nonzero=[b for b in bars if b[1] is None or b[1]-b[0]>1e-10]
        self.assertEqual(len(nonzero),1);np.testing.assert_allclose(nonzero[0],[1,2**.5])
    def test_qec(self):
        for p in [0,.02,.12,.3,.5,1]:
            r=qec_channel(p)
            self.assertLess(r['sdk_density_error'],1e-12)
            self.assertAlmostEqual(r['logical_error'],3*p*p-2*p**3,delta=1e-12)
            self.assertAlmostEqual(r['entanglement_fidelity'],1-3*p*p+2*p**3,delta=1e-12)
    def test_quantum_features(self):
        fixture=load_fixture();f,state=circuit_features(np.zeros((7,3)),True)
        self.assertEqual(f.shape,(7,6));np.testing.assert_allclose(np.sum(abs(state)**2,axis=1),1,atol=1e-13)
        self.assertEqual(sum(fixture['mask']),6)

if __name__=='__main__':unittest.main()
