from pathlib import Path
import json,hashlib,csv
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');O=R/'outputs/checks/2026-11-05-physical-sieve/root/documentation-v1'
gate=R/'outputs/checks/2026-11-05-physical-sieve/review/canonical-acceptance-v3.json';a=json.loads(gate.read_text());assert a['passed'];assert not O.exists()
for n,h in a['canonical_sha256'].items():assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h
integration=R/'outputs/checks/2026-11-05-physical-sieve/root/integration-v1/source-integration-v3.json'
z=json.loads(integration.read_text());assert z['passed'] and z['canonical_acceptance_sha256']==hashlib.sha256(gate.read_bytes()).hexdigest()
for n,h in z['changed_source_sha256'].items():assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h

summary='''

## Physical-radicand sieve and coherent main — 5 November 2026

This substantive frontier supersedes older current7/6/global5/12 and
pure5/6-positive-certificate descriptions; their mathematical history stays.
NEW external input: Alexandre de Faveri, Optimal large sieve for fixed order
characters, arXiv2610.04045v1,2October2026, Theorem1.1. This is a pinned
submitted preprint theorem being invoked, NOT a new proof of that sieve,
a priority claim or complete Lean verification. PrimaryPDF SHA256:
97720b3cacccbedb9c2014520ad4d128ae23afd0a781bdeff27dab4e86b7c726.
Full primary reading caches remain LOCAL; public metadata pins the version.

The exact application uses K=Q(omega), containing mu6; mu12 is not needed
for Theorem1.1. Unique ideal generators alpha=1mod3 remove unit ambiguity
in the source's allowed fixed Section2.3 construction. BOTH indices are
sixth-power-free ideals. Physical radicand norm, valuations1..5, lower
character orders and all raw common-prime/union/ray/SF/capacity masks remain.
There is NO radical relabeling or arbitrary-family reciprocity premise.
Freeze arbitrary possibly nonsquarefree/overlapping r6 with its ACTUAL
coefficient collision mask. For original raw and residue-subtracted sums,

 Phi(H,D)=H+D H^(1/6)+H^(5/6)D^(1/3)+H^(1/3)D^(5/6),

 times B²(HD)^epsilon for fixed nu/S and ONE common complex W, B=supnorm.
The r6 sums use powers-6,-5,-2; the Dterm counts H^(1/6) ideals. All global
S-factor exponents are positive; principal residues/cutofflogs are retained.
For1<=H<=D every term is <=D H^(1/6). Critical9/8 improves previous7/6 by
1/24, still3/8 above target3/4. For fixed0<theta<1 and H=D^theta, the accepted moving-W_D obstruction matches
this unsigned SUPNORM-CLASS power ONLY when W may vary with D. It does not
prove fixed-W sharpness or refute suitable explicit-seminorm bounds/GRH.

For original UNWEIGHTED A6=1 two-pivot h1 rows, the exact gcd-Mobius
subsequence norms retain A_U(dn), every raw zero and direct subunit counts:

 |S1AA| << B²(HD)^epsilon [H+D+H^(5/6)D^(1/3)+H^(1/3)D^(5/6)].

Critical13/12 improves former7/6 by1/12, still1/3 above target. The Dterm's
S-factor exponentzero uses a finite polylog count, NOT a convergent sum.
Under inherited high-window/capacity hypotheses,
 |(K0-Kall)/D|<=|S1AA|+236800 B² actualrowmass.
This retains the combined mean; neither separate main is estimated at
target scale. Arbitrary positive weights require a TRUE weighted norm.

Previously reviewed research-only reductions are now integrated with full
proofs. KS=Kall+P2 has ORDERED(p,q),p=qallowed and onlyq's rowmask;
P2/D<=3584 B²rowmass differs from unordered DISTINCT C2/both masks.
Old233216 remains for the old main;236800 belongs to the new main.
Endpoint-exact two-jump Mertens summation keeps both closed-prefix terms,
fullT including common primes, and196608 M1²rowmass D/(UZ)m_(14DH)(Z).
Zcuts residual lengthX, NOT smoothf. Hypothetical scalar powers are not
proved; boundedX has unitf and marginal cancellation cannot bound the full
coherent outer sum. Euler deletion includes ALL supported prime powers;
only fixed-field subpower transfer follows, with fixed exceptional-zero
qualifications. The old sufficient smooth-f tail bound remains valid as a
coarse inherited localization, not current optimality or signed saving.

The joint Stieltjes operator keeps -E_S(U)Q(U), orientation means/equalnorm
fibres/rawzeros/fullsignedmatrix. Rough-prime positive compression is NOT
invariant and supplies no full energy lower bound. Radial Mellin Parseval
keeps equalnorm correlations. The current short positive input is the MINIMUM
with older valid bounds on1<=L<=D, directunitcount on1/2<=L<1. Pure budget
improves5/6 to19/24; mixed7/9 remains smaller. These are sufficient positive
MAJORANTS, not actual-error lower bounds. Keep the minimum INSIDE the
variation integral and the pointwise lowerendpoint.

CONDITIONAL diagnostic only: an all-scale/all-epsilon squarefunction
d2(T)<<T^(-alpha+epsilon) would imply zeta_K zero-free STRICTLY right of
max(1-alpha,1/2) by Mellin discrepancy continuation and primepowers.
Scalar inputs sufficient for pure/mixed majorants would be U^(-1/12),
U^(-1/18), yielding conditional strips11/12,17/18. NONE of these inputs or
strips is proved or asserted necessary for the actual signed target.

Canonical shared sources: papers/coherent-main-{core,details}.tex and
papers/physical-sieve-{core,details}.tex, exact book counterparts. Two
independent application reviews and one joint source-bound canonical review
keep the deep theorem external. The EXISTING quadratic-pivot inspector
shows currentglobal9/8/A6=1slice13/12, historical curves, suppressed unknown
constants/epsilon losses. The entire former cube face remains better
controlled at power1 by the old ordinary comparison. Displayed numbers are
bound expressions, not measured norms/energies/training/GRH.

Next: improve ACTUAL mean-retaining combinedK0-Kall or coherentK0-J PLUS
signedprimeerror/endpoint BEFORE per-f/per-conductor independent absolute
Cauchy, retaining exact generalA_U (NOTroughshortlemma onK0), fixedcommonW/
explicitseminorms, fullunion/commonprime/ray/SF/capacity masks, means/equalnorm
fibres and neighboring mixed/pure blocks. No target cancellation follows
from this new positive norm application. Short/principal target assembly,
independent positive determinant/zero-location bridges and separate
Dirichlet/Hecke/Dedekind/elliptic/generalArtin obligations remainOPEN. No
Artinholomorphy/GRH/desiredpositivity/zeros premise or new analytic/category
Lean. Linux4.24 permission stillUNANSWERED: no install/download/substitute/
reinventory/repeatedquestion. BothgatesFALSE; ONE heartbeatACTIVE. Preserve
sourceHEAD/index, all releaseworktrees/indices/originals/data/outputs/caches/
environments/history/Macworkspace/old8765preview/privateactive-modeldata.
'''
files=['planning/MASTER_IMPLEMENTATION_PLAN.md','planning/PROGRESS.md','planning/CONTINUATION.md','planning/OPEN_OBLIGATIONS.md','book/SOURCE_COVERAGE.md','book/VERIFICATION.md','planning/COVERAGE.md']
planned={};original={}
for name in files:
 original[name]=(R/name).read_bytes();planned[name]=original[name]+summary.encode()
note='research/physical-sieve-and-coherent-main.md';assert not(R/note).exists();planned[note]=('# Physical radicands and the coherent signed frontier\n'+summary).encode()
p=R/'README.md';original['README.md']=p.read_bytes();t=original['README.md'].decode()
needle='The latest [ordinary-conductor comparison]';assert t.count(needle)==1;t=t.replace(needle,'The previous [ordinary-conductor comparison]',1)
pos=t.index('The previous [ordinary-conductor comparison]')
intro='''The current [physical-radicand sieve application](research/physical-sieve-and-coherent-main.md)
uses de Faveri’s pinned arXiv:2610.04045v1 Theorem1.1 on the actual sixth-power-free
row family, preserving every raw zero and the arbitrary overlapping sixth factor.
For1<=H<=D its unsigned envelope is O(B²(HD)^epsilon D H^(1/6)):
critical power **9/8**, improving previous7/6 by1/24.
The scoped original unweighted A6=1 signed slice has power **13/12**.
The fixed-profile signed target3/4, principal/short target assembly and independent
arithmetic determinant/zero-location bridge remain open. This is an application of
an explicit external preprint theorem, not a newly proved sieve or a GRH/Lean result.

'''
t=t[:pos]+intro+t[pos:];t=t.replace('its leading power is7/6,','its historical leading power was7/6,',1);planned['README.md']=(t+summary).encode()
p=R/'planning/CLAIMS.csv';original['planning/CLAIMS.csv']=p.read_bytes();assert 'PHY01,' not in original['planning/CLAIMS.csv'].decode()
rows=[
['PHY01','papers/physical-sieve-core.tex and details','Exact physical6free family and globalPhi;critical9/8','independent application of pinnedexternalpreprint;notnew sieveproof/Lean/GRH','review/canonical-acceptance-v3.json;prime-fibre laneA/laneCapplicationacceptances','Improve actual fixed-profile signedtarget'],
['PHY02','papers/physical-sieve-core.tex and details','UnweightedA6=1 signedh1 and actualcombined bound;critical13/12','fullmasks/AU(dn)/S0polylog/subunit retained','phy:signed/combined;canonicalacceptance','Bound actual coherent mean at targetH'],
['PHY03','papers/physical-sieve-core.tex and coherent-main-details.tex','Shortminimum pure19/24 mixed7/9;conditionalinput strips11/12 and17/18','sufficientmajorants/conditionalimplications only;no input/zerostrip proved','phy:short/diagnostic;cmr:conditional-strip','Control coherent primeerror plus endpoint'],
['CMR01','papers/coherent-main-core.tex and details','OrderedP2 bridge236800;endpointMertens/deletedEuler/jointStieltjes/Mellin','source-bound proof consolidation;target unresolved','cmr:core/joint/deleted-transfer/mellin;priorRESEARCH_ACCEPTED-v1','Estimate combinedsignedmain before marginaltriangles']]
import io
buf=io.StringIO(newline='');csv.writer(buf).writerows(rows)
planned['planning/CLAIMS.csv']=original['planning/CLAIMS.csv']+buf.getvalue().encode()
# Validate EVERY target before any mutation; preserve old bytes, then perform bounded writes.
for name,data in original.items():assert(R/name).read_bytes()==data,('Concurrent document change',name)
assert not(R/note).exists()
O.mkdir(parents=True)
for name,data in original.items():(O/name.replace('/','__')).write_bytes(data)
for name,data in planned.items():(R/name).write_bytes(data)
changed=files+['research/physical-sieve-and-coherent-main.md','README.md','planning/CLAIMS.csv']
(O/'record.json').write_text(json.dumps({'passed':True,'canonical_acceptance_sha256':hashlib.sha256(gate.read_bytes()).hexdigest(),'changed':changed,'sha256':{n:hashlib.sha256((R/n).read_bytes()).hexdigest()for n in changed},'scope':'Accepted frontier appended preserving history. Builds/promotion/publication separately gated.'},indent=2)+'\n')
print(json.dumps({'passed':True,'documents':len(changed)}))
