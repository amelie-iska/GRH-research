"""Independent identities for the ideal feature-memory recovery layer."""
import unittest
import numpy as np
from model import OBS,circuit_features
from qec_layer import effective_error,attenuate,density_mixture

class QECFeatureChecks(unittest.TestCase):
    def test_repetition_polynomial(self):
        self.assertAlmostEqual(effective_error(.1,1),.028)
        self.assertAlmostEqual(effective_error(.1,2),.002308096)
        for p in [0,.02,.1,.2,.5,1]:self.assertAlmostEqual(effective_error(p,1),3*p*p-2*p**3)
    def test_entangled_mixture(self):
        features,states=circuit_features(np.array([[.8,-.4,.6],[1.1,.7,-.3]]),True)
        for level in [0,1,2]:
            for p in [.02,.1,.2]:
                expected=attenuate(features,p,level)
                for i,psi in enumerate(states):
                    rho=density_mixture(psi,effective_error(p,level));actual=np.diag(rho).real@OBS
                    np.testing.assert_allclose(actual,expected[i],atol=2e-14)
                    self.assertAlmostEqual(float(np.trace(rho).real),1,delta=1e-13)
                    self.assertGreater(np.linalg.eigvalsh(rho).min(),-1e-13)
    def test_channel_endpoints(self):
        f=np.ones((2,6))
        np.testing.assert_array_equal(attenuate(f,0,2),f)
        np.testing.assert_array_equal(attenuate(f,.5,1),0)
        np.testing.assert_array_equal(attenuate(f,1,1),np.tile([-1,-1,-1,1,1,1],(2,1)))
if __name__=='__main__':unittest.main()
