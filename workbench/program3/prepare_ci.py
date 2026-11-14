"""Apply exact, already-diagnosed preflight repairs before the CI source commit.

This script changes only listed files. It rejects mismatched anchors and does not
modify observations, model results, environments, credentials or remote devices.
"""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def replace(path,old,new):
 p=ROOT/path;s=p.read_text()
 if old not in s:
  if new in s:return
  raise ValueError('Source anchor missing: '+path)
 if s.count(old)!=1:raise ValueError('Ambiguous source anchor: '+path)
 p.write_text(s.replace(old,new))

replace('workbench/program3/cmb.py',"if unit not in('mk','mkelvin','mk_cmb'):","if unit not in('mk','mkelvin','mk_cmb','mk, thermodynamic'):")
replace('workbench/lean/Program3Contracts.lean','import Mathlib.Data.Matrix.ConjTranspose','import Mathlib.LinearAlgebra.Matrix.ConjTranspose')
replace('workbench/lean/Program3Contracts.lean','abs_add _ _','abs_add_le _ _')
replace('workbench/site/program3.html','<label>Map overlay<select id="method">','<label>Selected-template statistic<select id="method">')
replace('workbench/site/program3-app.js','left=48,right=w-15,top=22,bottom=h-43','left=48,right=w-15,top=44,bottom=h-43')
replace('workbench/site/program3-app.js','x:left+i*145,y:13','x:left+(i%2)*(w-left-15)/2,y:13+Math.floor(i/2)*14')
replace('workbench/program3/visual_data.py',"url='/program3-assets/'+k+'.json'","url='program3-assets/'+k+'.json'")
# The user named this exact subsection. Preserve historical PDFs, while directing
# current source to the implemented continuation instead of an unfulfilled plan.
p=ROOT/'extension/manuscript/chapters/synthesis.tex';s=p.read_text();heading=r'\subsection{Resource-certified elliptic-curve quantum arithmetic}'
start=s.index(heading);end=s.find(r'\subsection{',start+len(heading));end=len(s)if end<0 else end
old=s[start:end]
if 'program3/ecc.py'not in old:
 replacement=heading+r'''

The reproducibility program is implemented in the companion's
\texttt{workbench/program3/ecc.py}, with separate emitted variable-point
addition oracles, independent gate counting and clean-work verification.
The current continuation, \emph{Arithmetic, Coverings and Learned Quantum
Renormalization}, gives the construction, proofs, tested resource comparisons
and observational controls. Historical manuscript editions retain the original
research-direction text; this source records its implemented successor.

The comparison fixes nonsingular finite curves, affine coordinates with a
unique infinity encoding, invalid-word behavior, ideal X/CX/CCX gates and
ancillary-register initialization. Both the binary path and the coherent signed
endomorphism decomposition include every preparation and cleanup operation.
Finite exhaustive-domain checks and actual cuStateVec replay are recorded at
their precise scope. The bounded truth-table compiler is not a polynomial-size
implementation for cryptographic curves, and logical all-to-all counts are not
error-corrected physical resource estimates.

In the tested instances, decomposition does not reduce the complete budget.
The emitted circuits make that result reproducible instead of inferring a
saving from shorter scalar components alone. The independent source, circuit
streams, assumption manifest and verification reports are linked by the
versioned continuation release. Its hierarchical channel and covering-theory
extensions preserve the distinction between an arithmetic endomorphism, a
quantum channel, a graph cover and a learned renormalization map.

'''
 s=s[:start]+replacement+s[end:];p.write_text(s)
p=ROOT/'workbench/site/index.html';s=p.read_text()
if 'program3.html'not in s:s=s.replace('<main>','<main><section><h2>Arithmetic, coverings and observed-sky controls</h2><p><a href="program3.html">Open the resource-certified arithmetic, learned hierarchy and real-WMAP explorer</a>.</p></section>',1);p.write_text(s)
print('Recorded source repairs applied; original scientific outcomes unchanged.')
