"""Real WMAP broad-feature controls with full-search phase-surrogate calibration.

This implements a declared diagnostic null, not a full WMAP likelihood or a CCC
confirmation. The observed products share a sky and instrument; their p-values
are not independent. Broad angular scales follow the ILC product's own caveat.
All learning, normalization and statistic choices are frozen before observed
scores are evaluated. Phase surrogates retain power but not anisotropic noise,
foreground or ILC-processing uncertainties; their ranks have that explicit scope.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys,time,urllib.request,urllib.parse
from html.parser import HTMLParser
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from .qrg import HierarchicalQNN,frozen_predict,DT,torch

SEED=20261114
NSIDE=16
LMAX=32
WIDTHS=(12.,18.,24.)
CALIBRATION=511
VALIDATION=256
AMPS=(0.,64.,128.,256.)
PRODUCTS={
 'ILC':('https://lambda.gsfc.nasa.gov/product/wmap/dr5/ilc_map_get.html','wmap_ilc_9yr_v5.fits'),
 'V':('https://lambda.gsfc.nasa.gov/product/wmap/dr5/maps_forered_band_r9_i_9yr_get.html','wmap_band_forered_imap_r9_9yr_V_v5.fits'),
 'W':('https://lambda.gsfc.nasa.gov/product/wmap/dr5/maps_forered_band_r9_i_9yr_get.html','wmap_band_forered_imap_r9_9yr_W_v5.fits'),
 'KQ85':('https://lambda.gsfc.nasa.gov/product/wmap/dr5/masks_get.html','wmap_temperature_kq85_analysis_mask_r9_9yr_v5.fits'),
}


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')

class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  if tag=='a':
   for k,v in attrs:
    if k=='href':self.links.append(v)


def acquire(root):
 from astropy.io import fits
 root.mkdir(parents=True,exist_ok=True);rows=[]
 for key,(landing,name)in PRODUCTS.items():
  text=urllib.request.urlopen(landing,timeout=40).read().decode();parser=Links();parser.feed(text)
  urls={urllib.parse.urljoin(landing,x)for x in parser.links if urllib.parse.urlparse(x).path.rsplit('/',1)[-1]==name}
  if len(urls)!=1:raise ValueError('Official source did not uniquely identify '+name)
  url=urls.pop();p=root/name
  if not p.exists():
   with urllib.request.urlopen(url,timeout=90)as response:
    data=response.read(30_000_001)
    if len(data)>30_000_000:raise ValueError('Source exceeded 30 MB budget')
   p.write_bytes(data)
  with fits.open(p,memmap=True)as hdus:
   h=hdus[1].header;columns=[dict(name=c.name,format=c.format,unit=c.unit)for c in hdus[1].columns]
   if int(h.get('NSIDE',0))!=512 or h.get('ORDERING','').strip()!='NESTED':raise ValueError('Unexpected native HEALPix representation')
   row=dict(product=key,landing=landing,url=url,filename=name,bytes=p.stat().st_size,sha256=sha(p),header={k:h.get(k)for k in ['PIXTYPE','ORDERING','NSIDE','COORDSYS','FIRSTPIX','LASTPIX']},columns=columns)
  rows.append(row)
 result=dict(schema='grh.wmap-acquisition.v1',retrieved_at_utc=datetime.now(timezone.utc).isoformat(),sources=rows,attribution='NASA/WMAP Science Team, LAMBDA/HEASARC; native public scientific products; retain source citations and processing metadata.',rights_scope='No blanket license is inferred for third-party papers. Public map-source bytes are linked; this release publishes numerical derivatives and provenance.')
 dump(root/'acquisition.json',result);return result


def prepare(root):
 import healpy as hp
 from astropy.io import fits
 acq=json.loads((root/'acquisition.json').read_text());maps={};alms={}
 for row in acq['sources']:
  p=root/row['filename']
  if sha(p)!=row['sha256']:raise ValueError('Source checksum changed')
  if row['product']=='KQ85':
   mask=hp.read_map(p,field=0,nest=False,dtype=np.float64);mask=hp.ud_grade(mask,NSIDE,order_in='RING',order_out='RING');continue
  unit=(row['columns'][0]['unit']or'').lower().strip()
  if unit not in('mk','mkelvin','mk_cmb'):raise ValueError('Unexpected temperature unit '+repr(unit))
  native=hp.read_map(p,field=0,nest=False,dtype=np.float64)*1000.
  if not np.all(np.isfinite(native))or np.any(abs(native)>1e7):raise ValueError('Invalid observed temperatures')
  # Coarse pixel averaging first is declared and replayed; use low lmax afterwards.
  low=hp.ud_grade(native,NSIDE,order_in='RING',order_out='RING');a=hp.map2alm(low,lmax=LMAX,iter=3,pol=False)
  ell,m=hp.Alm.getlm(LMAX);a[ell<2]=0
  a=hp.almxfl(a,hp.gauss_beam(math.radians(5.),lmax=LMAX));sky=hp.alm2map(a,NSIDE,lmax=LMAX,pol=False)
  maps[row['product']]=sky;alms[row['product']]=a
 points=np.asarray(hp.pix2vec(NSIDE,np.arange(hp.nside2npix(NSIDE)))).T;lat=np.degrees(np.arcsin(points[:,2]));keep=(mask>=.8)&(abs(lat)>=20)
 if not 1000<keep.sum()<len(keep):raise ValueError('Unexpected mask support')
 return maps,alms,points,keep,dict(source=acq,output_nside=NSIDE,lmax=LMAX,temperature_unit='microkelvin',native_to_microkelvin=1000,processing='Pixel average to RING Nside16; map2alm iter3 lmax32; remove l0,l1; additional 5 degree Gaussian beam; alm2map.',mask='Native KQ85 averaged to Nside16; keep fraction >=0.8 and |Galactic latitude|>=20 degrees.',kept_pixels=int(keep.sum()),effective_resolution='Input beams differ; all get the same additional 5-degree smoothing. Not an exact common-beam deconvolution.',scale_scope='Broad 12/18/24 degree Gaussian widths and radial annuli. Not a degree-scale Hawking-point reproduction.')


def catalogue(points,keep):
 import healpy as hp
 centers=np.asarray(hp.pix2vec(2,np.arange(hp.nside2npix(2)))).T;centers=centers[abs(centers[:,2])>=.5];labels=[];G=[];R=[];F=[];profiles=[]
 mean=keep.astype(float)/keep.sum()
 for i,c in enumerate(centers):
  angle=np.degrees(np.arccos(np.clip(points@c,-1,1)))
  for width in WIDTHS:
   rings=[]
   for lo,hi in [(0,.5),(.5,1),(1,1.5),(1.5,2)]:
    full=(angle>=lo*width)&(angle<hi*width);valid=full&keep
    if valid.sum()<4:break
    rings.append(valid.astype(float)/valid.sum())
   if len(rings)!=4:continue
   profile=np.exp(-.5*(angle/width)**2);g=profile*keep;g/=g.sum();g-=mean
   labels.append(dict(center_index=i,lon_deg=float(np.degrees(math.atan2(c[1],c[0]))%360),lat_deg=float(np.degrees(math.asin(c[2]))),width_deg=width,center=c.tolist()))
   G.append(g);R.append(rings[-1]);F.append(np.stack(rings)-mean);profiles.append(profile)
 if not labels:raise ValueError('No eligible templates')
 return dict(labels=labels,G=np.array(G),R=np.array(R),F=np.array(F),profiles=np.array(profiles))


def surrogates(a,count,seed):
 import healpy as hp
 rng=np.random.default_rng(seed);ell,m=hp.Alm.getlm(LMAX);rows=[]
 for _ in range(count):
  phase=np.exp(2j*math.pi*rng.random(len(a)));phase[m==0]=rng.choice([-1.,1.],(m==0).sum());phase[ell<2]=1
  # Multiply native coefficients: common per-mode phase makes the conditioned
  # magnitudes exactly unchanged. m=0 remains real.
  b=a*phase
  if not np.allclose(abs(b),abs(a),rtol=2e-15,atol=1e-12):raise ValueError('Conditional power not preserved')
  rows.append(hp.alm2map(b,NSIDE,lmax=LMAX,pol=False))
 return np.asarray(rows)


def radial(x,cat):return np.einsum('bn,tkn->btk',np.atleast_2d(x),cat['F'])
def moments(x,cat):
 x=np.atleast_2d(x);g=x@cat['G'].T;r=(x*x)@cat['R'].T-(x@cat['R'].T)**2;return g,r

def angles(features,scale):return 2*np.arctan(features/scale)


def train_search(a,cat):
 rng=np.random.default_rng(SEED+3);sky=surrogates(a,640,SEED+1);features=radial(sky,cat);scale=np.maximum(features[:512].std(axis=(0,1)),1.)
 xx=[];yy=[]
 for i in range(len(sky)):
  t=int(rng.integers(len(cat['labels'])));xx.append(features[i,t]);yy.append(0.)
  amplitude=float(rng.choice([64.,128.,256.]));injection=amplitude*cat['profiles'][t]
  xx.append(features[i,t]+cat['F'][t]@injection);yy.append(1.)
 xx=angles(np.array(xx),scale);yy=np.array(yy);model=HierarchicalQNN(47);optimizer=torch.optim.Adam(model.parameters(),lr=.035);x=torch.tensor(xx,dtype=DT);y=torch.tensor(yy,dtype=DT)
 train=np.arange(1024);validation=np.arange(1024,len(x));history=[];best=None
 for step in range(151):
  ids=rng.choice(train,128,replace=False);loss=torch.nn.functional.binary_cross_entropy_with_logits(model(x[ids]),y[ids])
  if step%10==0:
   with torch.no_grad():v=model(x[validation]);vl=float(torch.nn.functional.binary_cross_entropy_with_logits(v,y[validation]));acc=float(((v>0)==y[validation].bool()).double().mean())
   history.append(dict(step=step,train_bce=float(loss.detach()),validation_bce=vl,validation_accuracy=acc))
   if best is None or vl<best[0]:best=(vl,step,{k:v.detach().clone()for k,v in model.state_dict().items()})
  if step<150:optimizer.zero_grad();loss.backward();optimizer.step()
 model.load_state_dict(best[2]);weights=model.export();weights['input_scale_microkelvin']=scale.tolist()
 return weights,dict(seed=47,history=history,selected_step=best[1],training_examples=1024,validation_examples=256,source='Independent random-phase ILC surrogates and declared injected Gaussian profiles; original observed phases not scored during selection.',scope='Classically simulated four-qubit hierarchical channel with actually trained gates and readout; not quantum hardware or the full Mora-3 model.')


def score(x,cat,ref,weights):
 g,r=moments(x,cat);f=radial(x,cat);theta=angles(f,np.array(weights['input_scale_microkelvin']));q=frozen_predict(theta.reshape(-1,4),weights).reshape(f.shape[:2])
 return np.stack(((g-ref['g_mean'])/ref['g_std'],(ref['r_mean']-r)/ref['r_std'],(q-ref['q_mean'])/ref['q_std']),axis=1)


def rank_p(calibration,value):return float((1+np.count_nonzero(np.asarray(calibration)>=value))/(len(calibration)+1))
def wilson(k,n,z=1.959963984540054):
 p=k/n;den=1+z*z/n;center=(p+z*z/(2*n))/den;half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den;return [center-half,center+half]


def run(root,output):
 output.mkdir(parents=True,exist_ok=True);maps,alms,points,keep,meta=prepare(root);cat=catalogue(points,keep)
 # All learned gates and normalization are fixed before any observed scan.
 weights,training=train_search(alms['ILC'],cat);records=[];browser_sources={}
 for index,name in enumerate(['ILC','V','W']):
  reference=surrogates(alms[name],128,SEED+100+index);g,r=moments(reference,cat);q=frozen_predict(angles(radial(reference,cat),np.array(weights['input_scale_microkelvin'])).reshape(-1,4),weights).reshape(128,-1)
  ref={k:v for k,v in [('g_mean',g.mean(0)),('g_std',np.maximum(g.std(0,ddof=1),1e-9)),('r_mean',r.mean(0)),('r_std',np.maximum(r.std(0,ddof=1),1e-9)),('q_mean',q.mean(0)),('q_std',np.maximum(q.std(0,ddof=1),1e-9))]}
  calibration=surrogates(alms[name],CALIBRATION,SEED+200+index);scores=score(calibration,cat,ref,weights);maxima=scores.max(2);joint=scores.max(axis=(1,2))
  validation=surrogates(alms[name],VALIDATION,SEED+300+index);valscore=score(validation,cat,ref,weights);valmax=valscore.max(axis=(1,2));pvalues=np.array([rank_p(joint,x)for x in valmax]);reject=int((pvalues<=.05).sum())
  obs=score(maps[name],cat,ref,weights)[0];methods=[]
  for j,label in enumerate(['broad_temperature_profile','low_annular_variance','frozen_hierarchical_qnn']):
   winner=int(obs[j].argmax());methods.append(dict(method=label,selected_template=winner,template=cat['labels'][winner],maximum=float(obs[j,winner]),full_scan_rank=rank_p(maxima[:,j],obs[j,winner])))
  best=np.unravel_index(np.argmax(obs),obs.shape);observed=float(obs[best]);globalp=rank_p(joint,observed)
  injections=[];base=validation[:64];rng=np.random.default_rng(SEED+400+index);positions=rng.integers(len(cat['labels']),size=64)
  for amp in AMPS:
   injected=base+amp*cat['profiles'][positions];v=score(injected,cat,ref,weights).max(axis=(1,2));det=sum(rank_p(joint,t)<=.05 for t in v);injections.append(dict(amplitude_microkelvin=amp,draws=64,rejections=det,power=det/64,wilson_interval=wilson(det,64),scope='Synthetic broad profiles added to independent null surrogates, not discovered sky sources.'))
  rec=dict(product=name,methods=methods,joint_maximum=observed,joint_rank_p=globalp,bonferroni_three_product_p=min(1.,3*globalp),selected_method=int(best[0]),selected_template=int(best[1]),null_validation=dict(draws=VALIDATION,rejections=reject,fraction=reject/VALIDATION,wilson_interval=wilson(reject,VALIDATION)),injections=injections,observed_scores=obs.tolist(),calibration_maxima=joint.tolist(),per_method_calibration=maxima.T.tolist(),normalization={k:v.tolist()for k,v in ref.items()},rank_scope='Conditional phase-surrogate rank for the entire predeclared location/scale/method maximum. Not a probability that CCC is true, not a calibrated full-instrument likelihood, and not independent across products.')
  records.append(rec);browser_sources[name]=dict(map_microkelvin=maps[name].tolist(),record=rec);print(name,'joint rank',globalp,'validation',reject,'/',VALIDATION,flush=True)
 report=dict(schema='grh.observed-cmb-controls.v1',source_processing=meta,seed=SEED,template_count=len(cat['labels']),methods=3,calibration_draws=CALIBRATION,validation_draws=VALIDATION,rank_resolution=1/(CALIBRATION+1),model=weights,model_training=training,records=records,null='Independent random phases at m>0 and random signs at m=0 conditional on each processed observed alm magnitude; l=0,1 removed. All reference/training/calibration/validation seeds are distinct.',null_limitations='Exact randomization rank requires invariance under the stated phase group. Real anisotropic noise, foreground cleaning, mask effects and harmonic estimation are not fully modeled. Rejection tests this surrogate null and template family, not CCC uniquely.',shared_observations='ILC,V,W are derived from the same WMAP observations and same sky. Bonferroni does not assume independence; products are sensitivity comparisons, not independent discoveries.',heldout_definition='Training/validation/calibration null realizations are disjoint; the real sky is scored only after weights and normalization freeze.',script_sha256=sha(Path(__file__)))
 dump(output/'results.json',report)
 sparseF=[[[[int(i),float(v)]for i,v in enumerate(row)if abs(v)>1e-14]for row in block]for block in cat['F']]
 # Compact browser package retains exact numeric filter matrices; gzip at HTTP
 # transport can compress repeated zeros, while JSON export remains inspectable.
 browser=dict(schema='grh.cmb-browser.v1',points=points.tolist(),keep=keep.tolist(),labels=cat['labels'],G=cat['G'].tolist(),R=cat['R'].tolist(),F=sparseF,profiles=cat['profiles'].tolist(),model=weights,sources=browser_sources,scope=report['null_limitations'],processing=meta)
 (output/'browser.json').write_text(json.dumps(browser,separators=(',',':'),allow_nan=False)+'\n')
 np.savez_compressed(output/'replay.npz',G=cat['G'],R=cat['R'],F=cat['F'],profiles=cat['profiles'],points=points,keep=keep,**{'map_'+k:v for k,v in maps.items()})
 return report

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--data',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--acquire',action='store_true');a=p.parse_args()
 if a.acquire:print(json.dumps(acquire(a.data),indent=2),flush=True)
 r=run(a.data,a.output);print(json.dumps({'templates':r['template_count'],'observed':[(x['product'],x['joint_rank_p'])for x in r['records']]},indent=2))
