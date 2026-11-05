from pathlib import Path
import csv,hashlib,json
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
out=R/'outputs/checks/2026-11-05-signed-divisor/root/documentation-v1';out.mkdir(parents=True,exist_ok=False)
summary='''

## Mean-retaining signed divisor lift and complete-column reference — 5 November 2026

The exact original coprime slice now has an arbitrary-coefficient divisor
incidence formulation: D Q1(x,y)=sum_d mu(d) Z_d(x,y), with
F_d(x;u)=sum_(d|m) x_m chi_m(u) and
Z_d=sum_u w_u F_d(x;u) conjugate(F_d(y;u)). The original coefficients
include nu and the ONE common complex profile. Keep full divisors d=m,
actual row zeros, common-prime deletions, literal/ray and capacity masks.
Residual a,b may overlap. There is no extra mu(q) in this identity.
The positive norm majorant B(m)=sum_(d|m) lambda_d gives an exact finite
coefficient-error certificate. Computed Frobenius lambda_d values are
weighted nonzero matrix-entry counts, not an analytic signed saving;
classical uniform lambda_d inputs are asserted only for original unweighted
rows. The absolute divisor triangle still discards the needed cancellation.

For fixed residuals a,b and row u, the ACTUAL signed d series has local
factor 1-q^(-s)(1-q^(-v1)-q^(-v2))(1-q^(-w1)-q^(-w2)). Its exact factorization
has NINE Dedekind zeta factors (four numerator, five denominator) times a
normally convergent correction, with explicit half-integer cutoff,
finite-height errors and successive Perron limits. An independent finite
cutoff expansion keeps all EIGHT nonzero short-divisor states and gives
Z_U(s)=N_U(s)/zeta_K^T(s), with N_U holomorphic for Re(s)>0. Its elementary
bound retains U^(4 max(1-sigma,0)+epsilon), hence the old U^(2-4eta) cost
on sigma=1/2+eta, 0<eta<1/2. Shared-profile Mellin inversion embeds the
actual finite coherent outer sum over a,b,u. Neither this identity nor the
normal correction bounds its reciprocal zeta factors or justifies discarding
crossed residues. An explicit overlapping-residual control detects the
nonzero short-state correction. No uncancelled pole of the complete coherent
sum, new power saving, determinant comparison or zero-location result follows.

A NEW exact full-column evaluator uses all annular squarefree IDEALS, not
rational-squarefree norms. The fixed study profile is chosen ONCE with
width delta=1/240000, support [1,2], value one at all strict integer nodes
for D<=60000 and zero at endpoints. It is distinct from the older broad
plateau; its large derivative cost O_k(delta^(-k)) is explicit and the CLI
refuses D>60000. Different declared row blocks at D=144,576,60000 have
41/164/16953 columns, 53/212/21750 divisor buckets and 5/11/20 actual
nonprincipal rows. These three finite cases are not an asymptotic growth fit.

The largest immutable run retains 339060 raw column-row values (47908 zeros),
73420 incidences and 1305000 complex channel states. All nine signed cross
components are retained. In (A_U,C_U,mu) order the exact matrix is
[[-30714,-11287,19427],[-11287,2644,13931],[19427,13931,-5496]]/30000.
The A-A even/odd divisor masses 543416 and 604844 give -5119/5000 after
normalization by D. Among its columns,1361 are squarefree ideals with a
nonsquarefree rational norm. Independent ideal/finite-field arithmetic
reconstructs every large raw value, F/Z state and gcd-poset class; the naive
5748084180 pair-row visits are an operation-count comparison, NOT an executed
runtime benchmark. Small cases also have independent direct pair checks.
All original v1 scientific sources/tables stay frozen. A separately reviewed
v2 helper corrects ONLY the N=U=1 edge; every accepted column has N>U and
its data/provenance remains v1. No accepted tables were rerun for that fix.

The distinct signed-divisor.html inspector hash-verifies lossless compressed
payloads for every case and exposes actual columns, ideal incidences,
row/channel shapes and values, signed divisor contributions and all nine
pairings. It replays exact data; no browser training occurs. The unique
source-bound workflow PDF/TeX/SVG shows the actual dimensions and masses.
PDF and native MathML share the canonical papers/signed-divisor core/details
with all four focused wrappers. The new narrow table scroll container fixes
measured320px overflow while preserving full table/math bytes and font sizes.

Governing records: planning/signed-divisor-20261105/root/DIVISOR_INCIDENCE_LIFT-v2.md,
analytic-attempt/SIGNED_D_SERIES-v3.md, papers/signed-divisor-{core,details}.tex;
outputs/checks/2026-11-05-signed-divisor/review-design/ and independent large
review under analytic/large-full-column-review-v1/. The exact full-column
run manifests, fixed sources, all failed candidates and old evidence remain
preserved. The new finite profile is not a bounded-seminorm asymptotic theorem,
a whole-family counterexample, learned generalization, quantum/upstream
training, full Lean formalization or GRH proof.

Next research: use the actual short-state expansion or a proof-preserving
U-smooth/rough split to estimate the MEAN-RETAINING signed d sum/coherent
h,q,K weights before absolute Cauchy. Any rough-prime simplification must
first prove its support, endpoint and common-prime constraints; it has NOT
been established here. The current unsigned envelope remains
H+D H^(1/6)+(DH)^(2/3), with power7/6 at H=D^(3/4), still5/12 above target.
Keep coherent orientation means, all full-union/raw-zero masks and
conductor/profile/ray/squarefree/capacity uniformities. Short/principal
assembly, independent positive arithmetic determinant/zero-location
comparisons and separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin
obligations remain open. Pinned Linux4.24 compiler approval is unanswered;
no installation, substitution, repeated inventory or repeated question.
Actual analytic/category Lean and both completion gates remain unfinished.
Keep the ONE existing heartbeat ACTIVE; no guaranteed proof schedule.
'''
files=['planning/MASTER_IMPLEMENTATION_PLAN.md','planning/PROGRESS.md','planning/CONTINUATION.md','planning/OPEN_OBLIGATIONS.md','book/SOURCE_COVERAGE.md','book/VERIFICATION.md']
for name in files:
 p=R/name;(out/name.replace('/','__')).write_bytes(p.read_bytes());p.write_text(p.read_text()+summary)
p=R/'research/signed-divisor-incidence.md';assert not p.exists();p.write_text('# Signed divisor incidence and the coherent analytic numerator\n'+summary)
p=R/'README.md';(out/'README.md').write_bytes(p.read_bytes());p.write_text(p.read_text()+'''

## Complete-column signed divisor laboratory

The [signed divisor inspector](https://amelie-iska.github.io/GRH-research/signed-divisor.html) steps through all16953 ideal columns,21750 divisor buckets and20 actual rows of a new exact reference. It retains raw zeros, orientation means and all nine signed pairings. The negative finite coprime slice is not an asymptotic counterexample.

The [derivation and scope](research/signed-divisor-incidence.md) give exact divisor-incidence error certificates and a mean-retaining analytic expansion with nine zeta factors and eight short-divisor states. These reductions preserve the unresolved signed estimate; the current7/6 upper power and5/12 excess at H=D^(3/4) remain. No new Lean, determinant or GRH conclusion follows.
''')
p=R/'planning/CLAIMS.csv';(out/'CLAIMS.csv').write_bytes(p.read_bytes())
rows=[['SD01','papers/signed-divisor-core.tex and details','Exact original signed divisor incidence lift and coefficient perturbation certificate','independent prose and finite exact certificate accepted; absolute triangle gives no new exponent','review-design/incidence-acceptance-v1.json; canonical-acceptance-v1.json','Estimate actual signed divisor sum before absolute Cauchy'],['SD02','papers/signed-divisor-details.tex','Actual signed d series: nine-zeta correction and finite eight-state numerator with coherent Mellin assembly','independently reviewed; old U cost and reciprocal factors remain; no contour shift or uncancelled full-sum pole asserted','review-design/analytic-acceptance-v1.json; analytic-attempt/SIGNED_D_SERIES-v3.md','Bound mean-retaining coherent numerator and reciprocal integrals with all residues and uniformities'],['SD03','planning/signed-divisor-20261105/full-column and web/signed-divisor.html','Complete-column exact reference through D60000 with raw zeros/all nine pairings and lossless replay','independent full reconstruction accepted; distinct narrow fixed study profile; finite row blocks only; v1 frozen','full-column/implementation-closure-v1.json; analytic/large-full-column-review-v1/acceptance-v1.json; ui/frozen-receipt-v1.json','Do not infer asymptotic signed saving or reuse finite exact accuracy as a determinant bridge']]
with p.open('a',newline='') as f:csv.writer(f).writerows(rows)
changed=files+['research/signed-divisor-incidence.md','README.md','planning/CLAIMS.csv']
record={'passed':True,'scope':'Append accepted mathematical/implementation frontier; historical instructions preserved; candidate promotion/publication separately gated','changed':changed,'sha256':{name:hashlib.sha256((R/name).read_bytes()).hexdigest() for name in changed}}
(out/'record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'passed':True,'documents':len(changed)}))
