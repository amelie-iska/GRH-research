"""Attach explicit review decisions to selected exact source statements.

Unmatched claims remain source_port_only. Matching never silently changes the
original statement or proof. The exact original files and hashes remain in the
port archive. A review family is not a claim that all upstream dependencies were
formalized. This ledger is intentionally machine-inspectable.
"""
import argparse,json,re
from pathlib import Path
from datetime import datetime,timezone

RULES=[
 ('TropicalGT','references/main.tex','TokenGT universality for equivariant graph-to-graph maps','dependency_repaired','The fixed-k IGN premise requires tensor-order qualification. The integrated construction instead gives exact identifier gathering, compact ReLU approximation and finite-group symmetrization with explicit resource costs.','source-proof-repair.tex'),
 ('TropicalGT','references/main.tex','Universal approximation for ordinary graph-to-graph maps','dependency_repaired','Do not infer the fixed-order corollary from an unrestricted higher-order universality theorem. A uniform extended-family construction is given separately.','source-proof-repair.tex'),
 ('TropicalGT','references/main.tex','Exact finite interpolation on graph tokens','constructive_port_and_formal_extension','Exact finite Boolean graph tables are realized by the explicitly defined affine/ReLU network in FiniteGraphNetworks.lean. Labeled encoding and output action are declared; complexity is exponential.','FiniteGraphNetworks.lean'),
 ('TropicalGT','references/main.tex','Graph-token MHSA polytope bound','counterexample_and_corrected_bound','For d=H=2, a planar polygon sum has at most the sum of edge-normal counts, contradicting the stated attainable quadratic asymptotic. Retain product bound only with appropriate dimensional refinements.','check_models.py'),
 ('TropicalGT','references/main.tex','TokenGT tropical region bound','dependency_requires_repair','The proof relies on the preceding incorrect planar lower-bound clause; no corrected universal Theta rate is claimed.','source-proof-repair.tex'),
 ('TropicalGT','references/main.tex','Conditional tropical--toric bridge for transformer skeletons','hypotheses_strengthened','Hard selection of value vectors need not be continuous at score ties. A support-function conclusion needs continuity of the output under study, not routing potentials alone.','source-proof-repair.tex'),
 ('TropicalGT','references/main.tex','TokenGT simulates nonuniform threshold circuits','constructive_scope_preserved','Gate identifiers, masks, precision/margins and growing nonuniform resources remain explicit. Arbitrary finite Boolean syntax is independently proved correct for affine/ReLU interpretation.','FiniteGraphNetworks.lean'),
 ('ToricGT','assets/toricgt_paper_pg_softmoe_final.tex','Fixed-cell graph-to-graph universality','metric_dependency_repaired','A supremum conclusion needs a uniform approximation route; the new direct construction and Sumformer source are distinct from Yun Lp.','source-proof-repair.tex'),
 ('Tropical_Quivers_of_Archs','tropical_quiver_research_program.tex','TokenGT-style transformers are universal graph-to-graph function approximators','interface_hypotheses_explicit','Preserve source Lp metric and require faithful tokenization, correct input/output group actions, approximation measure and a decoder defined on approximated outputs.','source-proof-repair.tex'),
 ('Tropical_Quivers_of_Archs','tropical_quiver_research_program.tex','Universality of random-order autoregressive TokenGT decoding','probability_metric_repaired','Uniform conditional total variation controls the joint law; Lp score or conditional-mean approximation alone does not provide it.','source-proof-repair.tex'),
 ('Tropical_Quivers_of_Archs','tropical_quiver_research_program.tex','Bounded graph grammars lie within TokenGT representational scope','continuity_and_normal_form_hypotheses_added','Bounded size/horizon does not imply continuous attribute rules or a unique terminating normal form. Specify those properties or a finite discrete domain.','source-proof-repair.tex'),
 ('ToricGT-Program','ToricGT-II/assets/toricgt_ii_dynamical_persistence_neurips_article_bits_per_byte_figures.tex','Prefix-visible certificates improve optimal bits-per-byte by mutual information','identity_retained_interpretation_corrected','Under the source measurability premise, conditional information beyond the full prefix is zero. Positive utility belongs to restricted context/model classes or separately charged external information.','information-and-controls.tex'),
]

def build(port,out):
 claims=[json.loads(s)for s in (port/'claims.jsonl').read_text().splitlines()];counts={};matched=[]
 for c in claims:
  for repo,path,title,status,reason,evidence in RULES:
   if c['repository']==repo and c['path']==path and c['title']==title:
    c=dict(c,review_status=status,review_reason=reason,integration_evidence=evidence);matched.append((repo,path,title));break
  else:c=dict(c,review_status='source_port_only',review_reason='Preserved with source hashes; this release does not represent it as individually validated.',integration_evidence=None)
  counts[c['review_status']]=counts.get(c['review_status'],0)+1
  yield c

def main():
 p=argparse.ArgumentParser();p.add_argument('--port',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
 rows=list(build(a.port,a.output));(a.output/'reviewed-claims.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n'for c in rows));counts={}
 for c in rows:counts[c['review_status']]=counts.get(c['review_status'],0)+1
 report=dict(schema='grh.claim-review.v1',created_at_utc=datetime.now(timezone.utc).isoformat(),counts=counts,occurrences=len(rows),scope='Review decisions attach to exact named occurrences; duplicate versions and unreviewed claims are not silently promoted.')
 (a.output/'review-summary.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
