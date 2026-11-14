import sys,unittest,itertools,json,struct,zlib
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'experiments'))
from exact_codec import Bits,Reader,Encoder,Decoder,cdf,fit,encode,decode,TOTAL

class ExactCodec(unittest.TestCase):
 def test_gamma(self):
  values=list(range(1,500))+[2**20,2**40+1];b=Bits()
  for x in values:b.gamma(x)
  r=Reader(b.finish());self.assertEqual([r.gamma()for _ in values],values)
 def test_arithmetic_varied(self):
  rng=np.random.default_rng(7)
  for k in (1,2,8,64):
   rows=[cdf([int(x)for x in rng.integers(1000,size=k)])for _ in range(97)];symbols=[int(x)for x in rng.integers(k,size=len(rows))]
   e=Encoder()
   for x,row in zip(symbols,rows):e.put(x,row)
   d=Decoder(e.finish());self.assertEqual([d.get(row)for row in rows],symbols)
 def test_lossless_pcm(self):
  rng=np.random.default_rng(118);segments=[rng.integers(-32768,32768,500),np.zeros(10,dtype=int),np.array([-32768,32767]*40)]
  edges=[-10000,-100,-1,0,1,100,10000];reps=[-20000,-500,-2,0,1,3,500,20000]
  syms=[np.searchsorted(edges,np.diff(s),side='right')for s in segments]
  for order in range(5):
   model=fit(syms,8,order);packet,report=encode(segments,edges,reps,model);out=decode(packet)
   for a,b in zip(segments,out):np.testing.assert_array_equal(a,b)
   self.assertEqual(report['emitted_bytes'],len(packet));self.assertEqual(report['original_bytes'],sum(len(x)for x in segments)*2)
 def test_int32(self):
  a=np.array([-2**31,2**31-1,0,4,-9]);edges=[0];reps=[-1,1];model=fit([np.searchsorted(edges,np.diff(a),side='right')],2)
  p,_=encode([a],edges,reps,model,'<i4');np.testing.assert_array_equal(decode(p)[0],a)
 def test_no_unpaid_side_information(self):
  a=np.array([0,1,0,1]);model=fit([[1,0,1]],2,1);p,r=encode([a],[0],[-1,1],model)
  self.assertGreater(r['header_bytes'],20);self.assertEqual(r['emitted_bytes'],r['header_bytes']+r['symbol_bytes']+r['residual_bytes'])
 def test_reject_corruption_and_domains(self):
  a=np.array([0,1,-2,5]*20);m=fit([[0,1]],2);p,_=encode([a],[0],[-1,1],m)
  for bad in [b'',p[:10],p[:-1],b'XXXXXX'+p[6:]]:
   with self.assertRaises((ValueError,zlib.error,KeyError)):decode(bad)
  with self.assertRaises(ValueError):encode([np.array([0,40000])],[0],[-1,1],m)
 def test_cdf_positive(self):
  for k in [1,2,64]:
   c=cdf([10**9]+[0]*(k-1));self.assertEqual(c[-1],TOTAL);self.assertTrue(all(a<b for a,b in zip(c,c[1:])))
 def test_representation_not_file(self):
  a=np.arange(500);m=fit([np.ones(499,dtype=int)],2);_,r=encode([a],[0],[-1,1],m)
  self.assertIn('declared integer',r['scope'])

if __name__=='__main__':unittest.main(verbosity=2)
