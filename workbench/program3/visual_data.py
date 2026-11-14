"""Create compact exact-data assets and independent JS replay test vectors."""
from pathlib import Path
import argparse,hashlib,json,subprocess
import numpy as np
from .qrg import thermal_states,frozen_predict
from .cmb import score


def write(path,data):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(data,separators=(',',':'),allow_nan=False)+'\n');return {'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size}


def build(evidence,output):
 output.mkdir(parents=True,exist_ok=True);assets={}
 ecc=json.loads((evidence/'ecc/results.json').read_text());circuits={}
 for row in ecc['curves']:
  for a in row['algorithms']:circuits[str(row['curve']['p'])+'-'+a['variant']]=json.loads((evidence/'ecc'/a['circuit_file']).read_text())
 assets['arithmetic']=write(output/'arithmetic.json',{'report':ecc,'circuits':circuits,'variable_addition':json.loads((evidence/'ecc/variable-add-audit.json').read_text())})
 covers=json.loads((evidence/'covers.json').read_text());assets['covers']=write(output/'covers.json',covers)
 qrg=json.loads((evidence/'qrg/results.json').read_text());qrg['thermal']=[dict(g=r['g'],split=r['split'],target=r['target'],rho=r['rho'].real.tolist())for r in thermal_states()];assets['hierarchy']=write(output/'hierarchy.json',qrg)
 source=json.loads((evidence/'cmb/browser.json').read_text());keep=np.array(source['keep']);mean=keep/keep.sum();rings=[]
 for block in source['F']:
  result=[]
  for sparse in block:
   row=np.zeros(len(keep))
   for i,value in sparse:row[i]=value
   ring=row+mean;indices=np.flatnonzero(ring>1e-12)
   if not len(indices)or not np.allclose(ring[indices],1/len(indices),atol=1e-12)or np.max(abs(ring[np.setdiff1d(np.arange(len(keep)),indices)]),initial=0)>1e-12:raise ValueError('Ring compression changes filter')
   result.append(indices.tolist())
  rings.append(result)
 compact={k:v for k,v in source.items()if k not in ('G','R','F')};compact['rings']=rings;compact['followup']=json.loads((evidence/'cmb/followup.json').read_text());assets['cmb']=write(output/'cmb.json',compact)
 cat={k:np.asarray(source[k])for k in ['G','R','profiles']};cat['F']=np.zeros((len(rings),4,len(keep)))
 for i,block in enumerate(rings):
  for j,indices in enumerate(block):cat['F'][i,j]=-mean;cat['F'][i,j,indices]+=1/len(indices)
 cases=[]
 for product in ['ILC','V','W']:
  ref={k:np.array(v)for k,v in source['sources'][product]['record']['normalization'].items()};sky=np.array(source['sources'][product]['map_microkelvin'])
  for amp,center in [(0,0),(64,5),(128,36)]:cases.append(dict(product=product,amplitude=amp,center=center,scores=score(sky+amp*cat['profiles'][center],cat,ref,source['model'])[0].tolist()))
 write(output/'replay-vectors.json',{'sky':cases,'qnn':[{'weights':r['weights'],'angles':[[.2,.1,-.2,.3],[-1,.5,.2,.7]],'predicted':frozen_predict(np.array([[.2,.1,-.2,.3],[-1,.5,.2,.7]]),r['weights']).tolist()}for r in qrg['thermal_runs']]})
 source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=Path(__file__).resolve().parents[2],text=True).strip();manifest={'schema':'grh.program3.assets.v1','source_commit':source_commit,'assets':{k:dict(v,url='/program3-assets/'+k+'.json')for k,v in assets.items()}}
 write(output/'program3-manifest.json',manifest);return manifest

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--evidence',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();print(json.dumps(build(a.evidence,a.output),indent=2))
