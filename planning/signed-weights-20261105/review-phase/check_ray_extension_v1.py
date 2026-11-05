#!/usr/bin/env python3
"""Bounded NEW checks of the Jacobi ray/gauge extension, reusing saved exact values."""
from pathlib import Path
import importlib.util,sys,json,hashlib
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[3];O=R/'outputs/checks/2026-11-05-signed-weights/review-phase'
p=Path(__file__).with_name('check_jacobi_connection_v1.py');spec=importlib.util.spec_from_file_location('fresh_jacobi_review',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
reportpath=O/'exact-jacobi-controls-v1.json';old=json.loads(reportpath.read_text());assert old['passed'];assertions=0
ray=lambda z:(z[0]%2,z[1]%2,(z[0]+z[1])%3)
classes=[(a,b,c) for a in range(2) for b in range(2) if (a,b)!=(0,0) for c in (1,2)]
unitmap={str(u):ray(u) for u in m.PH};assert len(set(unitmap.values()))==6 and set(unitmap.values())==set(classes);assertions+=2
f=(2,4);delta=(1,2);one=(1,0);rows=[]
for row in old['local_fields']:
 pi=tuple(row['primary_generator']);j=tuple(row['jacobi_chi_chi2']);psi=m.neg(j);difference=m.add(psi,(-1,0));q=m.quotient(difference,f)
 assert q is not None and ray(psi)==ray(one);assertions+=2
 assert m.quotient(psi,pi) in m.PH;assertions+=1
 candidates=[m.mul(u,pi) for u in m.PH if ray(m.mul(u,pi))==ray(one)]
 assert candidates==[psi];assertions+=1
 # Verify the new note's equality with the OLD raw J(rho,eta), including inert fields.
 F=m.Field(pi)
 Jold=m.total(m.PH[(2*F.chi[x]+3*F.chi[F.complement(x)])%6] for x in F.xs if F.chi[x] is not None and F.chi[F.complement(x)] is not None)
 assert Jold==j;assertions+=1
 eta_minus_one=(-1)**F.chi[F.embed((-1,0))]
 jtheta=m.mul((-eta_minus_one,0),Jold)
 assert jtheta==m.mul((eta_minus_one,0),psi);assertions+=1
 rows.append({'prime_generator':pi,'norm':F.Q,'raw_j':j,'Psi_prime':psi,'Psi_minus1_divided_by_2delta':q,'unit_adjustment':m.quotient(psi,pi),'old_raw_J_rho_eta':Jold,'old_signed_theta_j':jtheta,'eta_minus_one':eta_minus_one})
# Canonical generator criterion implies multiplicativity; bounded products test the new extension, not old Gauss identities.
products=[]
for indices in [(0,2),(0,1),(2,4),(4,4),(0,2,4),(5,5,5)]:
 psi=(1,0);beta=(1,0)
 for i in indices:psi=m.mul(psi,tuple(rows[i]['Psi_prime']));beta=m.mul(beta,tuple(rows[i]['prime_generator']))
 assert ray(psi)==ray(one) and m.quotient(psi,beta) in m.PH;assertions+=2
 sf=len(set(indices))==len(indices);mu=(-1)**len(indices) if sf else 0
 if sf:
  jprod=(1,0)
  for i in indices:jprod=m.mul(jprod,tuple(rows[i]['raw_j']))
  assert m.mul((mu,0),jprod)==psi;assertions+=1
 else:assert mu==0 and m.norm(psi)>0;assertions+=1
 products.append({'prime_indices':indices,'squarefree':sf,'mu':mu,'Psi':psi,'generator':beta,'mu_j_identity_asserted_only_if_squarefree':True})
assert m.quotient((-2,0),(2,0)) is not None and (-1,0)!=one;assertions+=1
assert m.quotient((-1,1),delta) is not None and (0,1)!=one;assertions+=1
sources={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [reportpath,Path(__file__),Path(__file__).with_name('check_jacobi_connection_v1.py')]}
result={'passed':True,'assertions':assertions,'scope':'Fresh exact checks for -J(chi6,chi6^2) canonical generator modulo f=2delta; fixed infinity-type-one Hecke gauge application. No new Jacobi theorem, analytic saving or formalization.','f_omega':f,'norm_f':m.norm(f),'unit_residue_map':unitmap,'all_six_unit_residue_classes':classes,'prime_rows':rows,'multiplicative_products':products,'minimality_obstructions':{'modulus_2':{'unit':[-1,0],'equals1_modulus':True,'nontrivial_infinity_type_one_value':[-1,0]},'modulus_delta':{'unit':[0,1],'equals1_modulus':True,'nontrivial_infinity_type_one_value':[0,1]}},'source_sha256':sources,'uses_saved_jacobi_values':True,'old_tests_imported_or_run':False}
output=O/'exact-ray-extension-v1.json'
with output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'passed':True,'assertions':assertions,'output':str(output),'sha256':hashlib.sha256(output.read_bytes()).hexdigest()},indent=2))
