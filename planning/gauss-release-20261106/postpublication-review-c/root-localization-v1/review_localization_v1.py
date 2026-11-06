#!/usr/bin/env python3
"""Independent source/proof review of the postpublication localization corollary."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
R=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
O=R/"outputs/checks/2026-11-06-gauss-release/postpublication-review-c/root-localization-v1"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(n):return {"path":n,"sha256":sha(R/n)}
expected={
 "planning/gauss-release-20261106/postpublication-research/SHORT_K_BOTH_TYPE_I_LOCALIZATION-v1.md":"49e563bd2620b0e4269da99ea9f0b26a5614483a9de357718946ccbd3bca7f78",
 "planning/gauss-book-20261106/lane-a/BALANCED_RESIDUAL_HEATH_BROWN_CUBIC-v2.md":"c28af64fffc0b7b46ba97ac83c4128eca6ae150218785d72be038affa2db608e",
 "planning/gauss-book-20261106/lane-b/DIRECT_DISCRETE_TOP_CUTOFF-v2.md":"4b42c00601073bb6f178daf862c244c8b096b4c17a7aaf66d00caf13f4dd498a",
 "planning/gauss-release-20261106/lane-a/TYPE_I_FREQUENCY_AND_DELETION_TRANSFER-v2.md":"77660bde6a635d5de376e384f7570cee78a0f5dd981e01660ae22a948cbba48b",
 "planning/gauss-release-20261106/lane-b/FINITE_K_CUBIC_BANDS-v1.md":"3df3987298cb26d4504c0d70bb65c511da1e6c6b09f32738c58e81cdb0c22815",
 "outputs/checks/2026-11-06-gauss-release/lane-a/review-b-k/acceptance-v1.json":"b6cffa11bead21b2787231b57f0fc4847d741c1f34a3df61919ff860267eaaff",
 "outputs/checks/2026-11-06-gauss-release/review-b-a/acceptance-v1.json":"e78a9e9fe506395956792dc5df4ece386706d7bd478d80e2e51284897bd7454c",
 "outputs/checks/2026-11-06-gauss-book/review-a-direct/acceptance-v1.json":"9cade41f7c55d4ebe47fd4aed7223c5a6128efc7d1df588f90262f8921514023",
 "outputs/checks/2026-11-06-gauss-book/review-b-hb/acceptance-v1.json":"7ae05741257d1e4d435a92cc3d0d9000fbb108458d3bdece917138338c14af57"}
assert not O.exists()
before=sha(R/".git/index")
assert before=="0ef1af515b143ef68fed1d9a42aef7c00d5d1d7c3ef6832d2926d48e0925214c"
for n,v in expected.items():assert sha(R/n)==v,n
for n in expected:
 if n.endswith("acceptance-v1.json"):assert json.loads((R/n).read_text())["passed"] is True,n
rootpins="outputs/checks/2026-11-06-gauss-release/postpublication-research/root-localization-v1/source-pins-v1.json"
pinned=json.loads((R/rootpins).read_text())
assert len(pinned)==4 and all(expected[n]==v for n,v in pinned.items())
# Independent algebra only, not a rerun of the author's825/1024 formal controls.
a1=F(3,4);x=F(3,8);v=x/6;j0=F(1,32);y=F(1,8)
pref=a1+v;lam=a1+x-2
powers={
 "direct_Bessel":pref+lam,
 "direct_Y_tail":pref-y/2,
 "direct_cubic_tail":pref-F(1,6),
 "balanced_TypeII":pref-F(1,6)+y/3,
 "large_k_leading1":pref-2*j0,
 "large_k_leading2":pref-1-j0,
 "large_k_leading3":pref-F(1,3)-F(4,3)*j0,
 "large_k_safe_Bessel":pref+lam-j0,
 "prefix_PNu":F(1,3)+F(2,3)*(2*y),
 "minimum_T":1-(F(1,3)+F(2,3)*(2*y)),
 "predeletion_Nt":F(1,3)+F(2,3)*(2*y)+j0,
 "T_Nt":1+j0,
 "full_NQ":F(1,3)+F(2,3)*(2*y)+1+j0+v}
want={"direct_Bessel":F(-1,16),"direct_Y_tail":F(3,4),"direct_cubic_tail":F(31,48),"balanced_TypeII":F(11,16),"large_k_leading1":F(3,4),"large_k_leading2":F(-7,32),"large_k_leading3":F(7,16),"large_k_safe_Bessel":F(-3,32),"prefix_PNu":F(1,2),"minimum_T":F(1,2),"predeletion_Nt":F(17,32),"T_Nt":F(33,32),"full_NQ":F(51,32)}
assert powers==want
assert all(powers[n]<=F(3,4) for n in list(powers)[:8])
assert F(1,4)*64-3 >= F(1,5)*(64+1) # exact large-D HB threshold at2^64
O.mkdir(parents=True)
review_n="planning/gauss-release-20261106/postpublication-review-c/root-localization-v1/REVIEW-v1.md"
review=R/review_n;review.parent.mkdir(parents=True,exist_ok=True)
text="""# Independent review of short-k/BOTH-TypeI localization

The exact note49e563bd is accepted as a composition and arithmetic localization corollary. I read all four pinned mathematical inputs in full and independently reconstructed the sector order and exponent algebra. Their governing independent gates are also pinned. The proof does not supply a bound for the final retained kernel.

First use the direct, all-rho exact-discrete reduction of the normalized original pure top prefix to the leading finite-k model with both coefficients A_Y. This keeps the original capacity, every e/w primitive value separately, all source/ray components and exact pairs(w,s), with s arbitrary good and k/s,w/s overlaps allowed. Its errors have powers-1/16,3/4,31/48; ifY=U the coefficient-tail difference is identically zero. No continuous counting mean or37/48 discrepancy is substituted here.

Next remove the finite literal k range aboveJ0. The accepted leading-band theorem already supplies the first three displayed terms; appending its nonnegative Bessel-error majorant is a valid weaker bound even though the direct reduction has already reached the leading model. Thus no inference from a bound onP alone toL is needed. The four displayed powers are3/4,-7/32,7/16,-3/32. EmptyK<=J0 has no removed sector. No Euler completion or separate-column absolute-k shortcut occurs.

Write the full coefficient C_Y(m)=mu(m)A_Y(m) exactly as its signed HB TypeI plus TypeII pieces, rather than discarding constant/subtraction states of A_Y. This assignment depends only on the own-column factor scales. Expand both coefficient positions bilinearly. Each term with at least one balanced TypeII column is bounded by the accepted bound uniformly in fixed k and the other component; restricting its positive finite-k majorant to the short range is valid. AtY<=D^(1/8) the worst power is11/16. The remainder is precisely the short-k BOTH-TypeI leading model, still complex and signed. Its difference from the actual top prefix is bounded by the claimed fixed-profile(B²+B M(W))D^epsilon H budget. This is a sufficient sector reduction, not necessity or a whole-form result.

For a surviving TypeI branch putP=NaNb andL=D/P. The at-most-nine-factor HB classification givesNu<=C L^(1/3) and the chosen exact profile scale isT=D/(P Nu). BecauseP<=D^(1/4), P Nu<=C D^(1/2), T>=c D^(1/2). Raw eta(k²) zeros ensure k is coprime to the original SF column, so a,b,u,k are pairwise SF/coprime and t=abuk is a good SF ideal. Its norm is at mostC D^(17/32). Multiplication cancels P Nu exactly, givingT Nt=D Nk, hence at mostD^(33/32). These identities concern ideals and the exact profile scale, not rational-prime support or a dyadic equality with suppressed constants.

The full good deletion radical includesabunksw; it is not the primitive conductor. Suppressing overlaps only for an upper bound, NQ<=C(P Nu)(Nn)(Nk)(Ns)(Nw)<=C D^(51/32), usingNn<=2D,Ns<=D^(1/16),Nw<64. All fixed S exclusions remain in the actual psi/goodness functions. The original primitive pair conductor remains of orderD².

Opening the full deletion radical uses the exact signed transfer. A term with(d,t)>1 is killed by its raw outer cubic value; otherwise dt is SF. TermsNd>=2T vanish from the exact endpoint-zero profile. For the active terms,(T/Nd)N(dt)=D Nk andN(dt)<2D^(33/32). At scales between1/2 and1 the literal unit term must be retained; at or below1/2 the endpoint-zero profile gives zero. An input restricted to the pre-openingD^(17/32) frequency window would therefore be insufficient.

On the ORIGINAL coprime pair, the two prefix ideals are coprime and k avoids both, so gcd(t1,t2)=k exactly. Here k is the original dual square-divisor frequency, not the original pair gcd or the auxiliary Mobius deletion divisor. The statement is not reused on overlapping auxiliary entries or after different deletion shifts. Shared k and all w/s/root/ray means still couple the long variables; there is no independence, centering or positivity conclusion.

The author's825Fraction/1024abstract support checks were not rerun and are not actual character-family evidence or proof of the corollary. My thirteen exact Fraction expressions check only the newly composed algebraic powers. No scientific data, old controls, builds, browsers, network/auth, Git mutation or frozen source/metadata edit was performed. No normalization, scope or mathematical blocker was found. The actual short-k BOTH-TypeI estimate, all remaining frequency sectors, whole signed13/12/global9/8 and GRH/determinant/Lean obligations remain open.
"""
with review.open("x") as f:f.write(text)
checks={"passed":True,"scope":"Independent exact rational exponent algebra only; not actual characters, ideal data, author's formal-support rerun or a new target estimate","expressions":{n:str(v) for n,v in powers.items()},"source_producer":str(Path(__file__).relative_to(R)),"source_producer_sha256":sha(Path(__file__))}
cp=O/"independent-exponents-v1.json"
with cp.open("x") as f:json.dump(checks,f,indent=2,sort_keys=True);f.write("\n")
rp=O/"source-pins-v1.json"
with rp.open("x") as f:json.dump(expected,f,indent=2,sort_keys=True);f.write("\n")
assert sha(R/".git/index")==before
receipt={"schema":"postpublication-short-k-both-TypeI-independent-review-v1","passed":True,"accepted_scope":"Actual-sector composition and simultaneous original/opened arithmetic windows only; no bound for the retained BOTH-TypeI kernel","governing_note":pin(next(iter(expected))),"source_pins":pin(str(rp.relative_to(R))),"review":pin(review_n),"independent_algebra":pin(str(cp.relative_to(R))),"review_producer":pin(str(Path(__file__).relative_to(R))),"full_original_actual_P_to_L_to_short_k_TypeI_reduction_valid":True,"all_rho_class_primitive_S_masks_capacity_and_AY_states_retained":True,"finite_leading_large_k_bound_used_without_P_to_L_inference":True,"one_original_D_normalization":True,"minimum_long_scale":"c D^(1/2)","predeletion_frequency":"C D^(17/32)","exact_scale_frequency_identity":"T Nt=D Nk","product_frequency_bound":"D^(33/32)","full_good_deletion_bound":"C D^(51/32)","opened_frequency_bound":"N(dt)<2 D^(33/32)","original_frequency_gcd":"gcd(t1,t2)=k only before auxiliary openings","bounded_subunit_unit_term_retained":True,"independent_parent_gate_pins":{n:v for n,v in expected.items() if n.endswith("acceptance-v1.json")},"author_formal_checks_not_replayed_or_used_as_character_proof":True,"no_new_target_or_signed_whole_gain":True,"remaining_BOTH_TypeI_kernel_unestimated":True,"outside_frozen_release":True,"no_frozen_product_globaldoc_index_build_browser_network_auth_or_Git_mutation":True,"source_index_before_sha256":before,"source_index_after_sha256":sha(R/".git/index"),"created_utc":datetime.now(timezone.utc).isoformat()}
ap=O/"acceptance-v1.json"
with ap.open("x") as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write("\n")
print(json.dumps({"passed":True,"receipt":str(ap.relative_to(R)),"sha256":sha(ap),"review_sha256":sha(review),"source_pins_sha256":sha(rp),"independent_algebra_sha256":sha(cp),"producer_sha256":sha(Path(__file__))},indent=2))
