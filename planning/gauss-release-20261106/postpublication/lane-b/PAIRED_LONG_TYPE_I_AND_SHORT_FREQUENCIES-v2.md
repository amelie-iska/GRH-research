# Pairing the two long TypeI factors at the original short frequencies

NEW postpublication research-only candidate v2,6 November2026 (v1 preserved; the unmultiplied leading pair and its actual g0 factor are explicit). This is a new pair-first attempt on the ACTUAL remaining small-A_Y BOTH-TypeI root/Gauss form. It does not redo the accepted large-k cutoff, balanced TypeII, scalar/density/lattice, root-law or Bessel controls. Its survivor is an exact all-mask paired representation, a newly matched Proposition8.1 input from the SAME already pinned primary paper, and a quantitative diagnosis of why these available pair-matrix estimates do NOT give the missing short-k saving. No improved whole/model bound is claimed. Independent review is required.

All work is new owned Linux-SSH notes/receipts. No download, dependency, Lean, Git, canonical/book/UI/index/global metadata, browser, auth or publication operation is performed. Existing primary PDF/text is only read locally; its full body stays excluded from any release. Root announced the new333-page publication refs before this task began; this note is outside that frozen release and its subsequent favicon-patch scope.

## 1. Exact original object, TypeI labels and normalization

Use accepted DIRECT-v2 4b42c006, HB-v2 c28af64f, all-component phase011b68a0, TypeI deletion-transfer-v2 77660bde and finite-k bands3df39872 as INPUTS. D>=2^64,1<=Y=D^(1/8)<=U<=sqrt(D), original UNWEIGHTED PURE A2=1,v2=O and all other good factors unit. Literal u0 is fixed unit/S-supported with no good support; nu and original S/source/ray data are fixed. Columns are ALL good squarefree IDEALS D<=Nm,Nn<=2D, ordered(m,n)=1, with the optional ORIGINAL unequal-norm mask imposed consistently if desired. Equal-norm conjugate ideals remain distinct.

W is ONE fixed possibly complex smooth profile supported[1,2], with its zero endpoints, B=||W||infinity and the inherited finite Mellin seminorm M(W). The common right profile is its conjugate, not a separately chosen profile. The original capacity/interpolant G and integer endpoints stay fixed when coefficients are compared. Empty capacity b_cap<a_cap gives0; otherwise K=sqrt(b_cap) is the ORIGINAL pre-S cutoff. Set J0=D^(1/32). No new(k,s) mask or k Euler completion is introduced.

X>=64,V=X^(1/6)/2, and the original exact frequency set is

 T_X={(w,s): w integral,Nw<64; s good integral,
              V<Ns<=2V, Nw(Ns)^6<=X}.                    (1.1)

s need not be squarefree and w/s,k/s,k/w overlaps remain allowed. ALL rho, all S-supported w modes, e|P_S, primitive S zeros/conductor drops, source classes, unit/ray restrictions and original endpoints remain. The exact short-k part uses Nk<=min(K,J0), including the unit.

The original root gauge turns A_Y into

 C_Y(m)=mu(m)A_Y(m)=sum_(abc=m,Na,Nb<=Y)mu(c).            (1.2)

In an accepted unbalanced HB box write c=u*v, where v is its unique long unrestricted coefficient1 factor and u groups all other HB factors and their signs. Fix the original a,b and grouped u for the first column, and a',b',u' for the second. Put

 p=abu, r=a'b'u', m=pv, n=rz,
 L=D/Np, M=D/Nr.                                      (1.3)

These p,r are auxiliary short products, not original rows, k, or virtual gcds. On nonzero assignments p,r,v,z are SFgood and pairwise coprime. Exact HB coefficients H(a,b,u),H'(a',b',u') depend on their own short labels, not k or the opposite long factor, and are divisor-bounded. Original short a,b have coefficient1; HB mu signs live in H. There is NO additional mu(v),mu(z) or mu(m) inserted after(1.2). Nu<=C(D/(NaNb))^(1/3), so Np,Nr<=C D^(1/2), L,M>=c D^(1/2); constants depend only on the at-most-nine-factor scale grouping. Actual long intervals are the original HB dyads clipped to[L,2L] and[M,2M], with literal endpoints.

The NORMALIZED exact form is a finite signed sum over these outer labels, original source/rho/e/w/s components and k, with prefactor

             A1/D * H(a,b,u)bar H'(a',b',u')/sqrt(NpNr). (1.4)

Its original1/D is included ONCE. The raw numerator is D times this quantity. No term of this signed decomposition is declared a positive energy or lower bound. If a root/class formula is used off original pair-coprime support below, it is merely an auxiliary coefficient extension, never a primitive root at overlapping conductors.

## 2. What the actual long-long root kernel is

Write chi_v=chi_(3,v), G_v=tau_(alpha_v)(chi_v)/sqrt(Nv), at the SAME primary1mod3 section/inverse-different pairing as the accepted notes. These are auxiliary primitive FINITE cubic Gauss sums at SFgood v, not primitive S-values of xi_v. Accepted CRT gives on(v,z)=1

 G_(vz)=G_v G_z bar chi_v(alpha_z),
 bar G_(vz)=bar G_v bar G_z chi_v(alpha_z).               (2.1)

For the mixed finite character chi_v bar chi_z at its GOOD primitive conductor v*z, the two CRT crosses cancel by primary cubic reciprocity:

 tau_(alpha_v alpha_z)(chi_v bar chi_z)/sqrt(NvNz)
                                      =G_v bar G_z.     (2.2)

This is finite-character normalization, not an assertion that this auxiliary mixed finite character alone is a unit-trivial Hecke character at S. Its S factors in the actual eta stay separate.

The ACTUAL two-column root has bar G_v G_z. There is therefore NO residual chi_v(alpha_z) long-long interaction available to insert by fiat. The genuine cubic crosses are chi_p(alpha_v) and bar chi_r(alpha_z), already coming from each OWN original column's CRT. They are included in its actual row coefficient below.

One can algebraically manufacture a long-long cubic factor, but the leftover is jointly dependent:

 bar G_v G_z = bar G_(vz) G_z² bar chi_v(alpha_z),
                                                       (v,z)=1. (2.3)

A bound by the bare cubic matrix in v,z would now need control of the Schur multiplier bar G_(vz). Its modulus1 does NOT imply operator cost1 or separate left/right diagonals. Indeed(2.1) shows that after unitary diagonals it is exactly the opposite cubic cocycle; multiplying it with the inserted cubic kernel gives the coprime-incidence kernel again. Thus this proposed immediate long-long-sieve saving is a circular insertion/cancellation, not an arithmetic estimate. This does not rule out a future estimate exploiting the ACTUAL Gauss coefficient jointly.

## 3. An exact paired matrix with shared k, retaining every mask

Freeze one actual source pair/rho, e,w,s and the short labels p,r, but do not triangle in k or the long variables. The accepted total type0 root package gives

 eta(k²)=theta_S(alpha_k)² chi_(3,pv)(alpha_k)
                                     bar chi_(3,rz)(alpha_k). (3.1)

theta_S is the ACTUAL primitive finite S part at its actual f_S; individual xi may have infinity type. Its factor theta_S(alpha_k)² is a scalar in k. Separate theta_S(gamma_e),bar theta_S(gamma_w), tau_(gamma_S)(theta_S)/sqrt(F_S), mu(e)/Ne and F_S^(-1/2) stay outside, with their zeros and unit-conductor conventions. No quotient or induced S Gauss value is used.

The remaining two-variable coefficient can be written EXACTLY as

 u_(v,z)=Xi_omega(v,z;p,r,w,s)
           bar G_v G_z W(NpNv/D)bar W(NrNz/D)/sqrt(NvNz). (3.2)

Xi retains all finite source/ray/period-four Gamma factors, original nu/Jacobi/Hecke gauges and fixed-numerator phases, and has modulus<=1 after bounded fixed scalar coefficients are extracted. In particular Gamma(alpha_pv alpha_rz) may stay JOINTLY in Xi: we do not need it to factor for this pair-first argument. Xi also retains explicitly:

 * all goodSF/actual long-dyad restrictions;
 * (p,r)=1 outside and(v,pr)=(z,pr)=(v,z)=1 inside;
 * all original s/mn and e/w numerator raw zeros;
 * both original source classes [pv]=A,[rz]=B;
 * the optional ORIGINAL NpNv!=NrNz restriction, as a true pair selector.

The literal unit/S data and the same complex W are untouched. No source or profile mean is centered. For fixed p,r these are functions of(v,z), INDEPENDENT OF k. The original good-k collisions with p,r are retained in

 lambda_k=mu(k) theta_S(alpha_k)² chi_p(alpha_k)
                                  bar chi_r(alpha_k)/(Nk)², (3.3)

with k goodSF and its EXACT finite range. Its remaining collisions with v,z occur in the raw matrix

 R_((v,z),k)=chi_v(alpha_k)bar chi_z(alpha_k).             (3.4)

k/s overlap is allowed. Multiplying the s-deletion in Xi by this raw matrix simply keeps both original masks; it does not delete a prime from k merely because it divides s. All actual source/rho/e/w/s scalars, including bar rho(s)^6, remain in the finite outer sum. This is the exact coupled object before any positive common-divisor or separate-column triangle.

For the leading g0 model the fixed-outer long pairing is

                   T_0=sum_(v,z)u_(v,z)sum_k lambda_k R_((v,z),k). (3.5)

The ACTUAL leading-model component is g0*T_0, with g0=C0^(-1/2)M0; T_0 in(3.5) is the unmultiplied Gauss pairing, not a division by g0. If M0=0 the leading component is0 regardless of T_0. We make no nonvanishing assertion. The exact Bessel form is handled in Section6 without dropping endpoints or completing k. Pair-coprimality is a zero coefficient in(3.2), not an unproved primitive-character formula on overlapping pairs. The optional unequal-norm selector is also an exact row coefficient here, so no false multiplicativity is claimed.

## 4. The physical cube-free encoding and its height

On the actual SF/coprime long pairs the map

                       a=v*z²                           (4.1)

is injective: valuations1 recover v and valuations2 recover z. It is good cube-free and includes EVERY orientation separately. Raw multiplicativity and primary reciprocity give

        R_((v,z),k)=chi_a(k)=chi_k(v*z²),                 (4.2)

where the character family is chosen as the already accepted primary power-residue family. At any collision with k all sides are0. The original(v,z)=1 restriction must still be retained as the support of this encoding; it is not a zero of chi_k(v*z²) on arbitrary overlapping v,z.

The physical norm of a is Nv*(Nz)², so its dyadic height is L M² (bounded endpoint factors). Conjugating the entire scalar reverses v/z orientation and permits height L² M. Consequently the smaller possible physical height is

                  A_*=LM*min(L,M),                      (4.3)

NOT LM=N(vz), its good radical conductor size. Theorem1.1 at n=3 may be applied on these actual cube-free rows, but only with this physical height. For n=3 the permitted primary construction matches the raw cubic family also at valuation2: any residual primary-generator unit ambiguity after extracting a cube is in{+1,-1}, and the cubic residue symbol is trivial on both. This is the same fixed family, not an arbitrary primitive-character or conductor-ordered substitution.

Crucially, a is a CHARACTER-FAMILY INDEX, not a proposed modulus for G_a. The character at a=vz² has good primitive conductor vz, not vz²; a Gauss sum formed at the induced full modulus a cannot be declared a unit root. All Gauss factors in(3.2) remain at their original primitive SF moduli, or the mixed primitive finite conductor in(2.2).

The old Theorem1.1 input therefore yields the valid but often bad leading-band certificate

 |T_0(J)| << B²D^epsilon J^(-3/2)
           sqrt[ A_*+J+(A_*J)^(2/3) ],                  (4.4)

for J<Nk<=min(2J,K,J0),J>=1. Here sum|u|²<<B^4 and sum|lambda|²<<J^(-3). The original joint W product is an actual row coefficient; no Mellin separation or new profile is needed. The theorem is used only as an arbitrary-coefficient matrix norm. In particular no finite-order assertion about the Jacobi gauge vartheta is made.

Replacing A_* by LM would assert a theorem with the wrong physical index. Treating bar G_(vz) in(2.3) as a free diagonal would instead assert an unproved Schur bound. Neither step is legitimate.

## 5. A better matched primary pair input, but still not the missing gain

NEW primary reading for this attempt uses the SAME pinned arXiv:2610.04045v1, printed Section8, Proposition8.1. No new paper is downloaded. Its precise statement for n=3 and A,B,Q>=1 is an operator bound for

 (lambda_q)_(q SFgood,Q<Nq<=2Q)
       -> (sum_q lambda_q chi_q(a b²))_(a good~A,b good~B).

The output ideals a,b are UNRESTRICTED good integral ideals; q is SQUAREFREE (the paper's star convention, defined on printed page2). With ell=min(A,B),N=max(A,B), its squared norm is

 <<_(epsilon,fixed K,S,family) (ABQ)^epsilon
       [AB+ell^(2/3)N^(1/3)Q+ell^(1/3)N^(2/3)Q^(2/3)]. (5.1)

This is an explicitly stated external input, not reproved here and not an optimal Q+AB claim. The fixed family is the primary family used above, K=Q(omega) contains mu3 and original fixed S contains places above3 with S-class number one; excluding2 or keeping any additional original masks is a restriction/zero coefficient. No Theorem1.4 mu6 hypothesis is borrowed into this proposition.

The match is EXACT with a=v,b=z,q=k, by(4.2). Original SF/coprmality/source/unequal restrictions and Gauss/W phases remain in the actual row vector u; the larger unrestricted output set is used only in a positive operator norm. The inner q coefficients are arbitrary complex numbers, so(3.3), its raw zeros, clipped K,J0 endpoints and primitive S scalar are admissible. We use ordinary operator duality/Cauchy for the actual u, not a new arbitrary positive row-weight theorem.

Put

 B_pair(L,M,J)=LM+ell^(2/3)N^(1/3)J
                          +ell^(1/3)N^(2/3)J^(2/3),
 ell=min(L,M),N=max(L,M).                               (5.2)

The valid leading certificate is

             |T_0(J)| << B²D^epsilon J^(-3/2)
                                            sqrt B_pair(L,M,J). (5.3)

This avoids the inflated physical-height bound(4.4), because Proposition8.1 explicitly controls this two-argument family in conductor aspect. It does NOT allow us to replace the right side by a desired off-diagonal or centered bound. Its full LM term stays.

Primary pins: PDF SHA97720b3cacccbedb9c2014520ad4d128ae23afd0a781bdeff27dab4e86b7c726; text SHAef550aa4bca1659c6d98ebf69e2cbd42a2793b707f6171f53d1b2baeb8654a57. Public citation metadata outputs/checks/2026-11-05-prime-fibre/lane-b/PUBLIC-CITATION-v1.json, SHAb0b3eae785d3c8b56103e8d2b3134a765e55be7395d4c54be8cfb61d08d0c503. The local full paper/text is not redistributed. The bounded novelty read of current prime-fibre/coherent-band/root-moment/gauss-book/gauss-release notes found no previous Proposition8.1 application; regardless, the input is credited as an external theorem rather than a newly proved estimate.

## 6. Exact finite Bessel kernel and the available total budget

Use the already accepted finite Bessel hierarchy as INPUT, not a new Taylor control. With B0=5/2,

 dotG(x)=C0^(-1/2)sum_(j>=0)(-1)^j (x/C0)^j/(j!)² M_j,
             M_j=int t^jG(t)dt, |M_j|<=2B0^j.            (6.1)

The exact x is A1Nw(Ns)^6/[(Nk)²NeF_S NmNn]. Let Lambda=A1X/D². At each j its separated column contraction is

 R_j(m)R_j(n), R_j(m)=(D/Nm)^j, R_j(n)=(D/Nn)^j,        (6.2)

which is<=1 on the ORIGINAL annular m=pv,n=rz. It is NOT R_j(v) alone. The remaining k coefficient has(Nk)^(-2-2j), no changed character power or new deletion. The fixed finite coefficients from e,F_S and every original w/s endpoint remain. All sums except j are finite, and the moment bound gives absolute convergence.

Applying the SAME pair norm(5.1) at each j to these actual contracted row and k vectors yields the exact Bessel bound

 |T_exact(J)| << B²D^epsilon I(B0Lambda/C0)
                         J^(-3/2)sqrt B_pair(L,M,J),
 I(t)=sum_(j>=0)t^j/(j!)².                              (6.3)

No derivative-uniformity assumption on the sharp capacity interpolant is used. Lambda is tiny at the declared pure top scales, so I is bounded. This uses the full finite k kernel, not an Euler completion, fractional infinite-endpoint integral, principal-density mean or a discarded Bessel remainder. The two occurrences of W remain in the actual row coefficient, costing B²<=B M(W), without a hidden profile replacement.

When J<=ell=min(L,M), both nonleading terms of B_pair are O(LM), so(6.3) gives

                    |T_exact(J)| <<B²D^epsilon I(cLambda)
                                            sqrt(LM)/J^(3/2). (6.4)

For the unit k term the direct row count gives instead

                    |T_exact(k=O)| <<B²D^epsilon I(cLambda)sqrt(LM). (6.5)

These are valid coupled bounds BEFORE a separate long-column triangle. For short J<=D^(1/32), the condition J<=ell follows at sufficiently large D from L,M>=cD^(1/2); bounded smaller cases retain(6.3) or direct counts. No selected support or lower density is asserted.

Multiplying the original short prefactor1/[D sqrt(NpNr)] uses sqrt(LM)=D/sqrt(NpNr). Thus its positive outer budget is proportional to1/(NpNr). The actual short labels satisfy the elementary harmonic bound

 sum_(Na,Nb<=Y)1/(NaNb)
      sum_(Nu<=C(D/(NaNb))^(1/3)) |H(a,b,u)|/Nu
                                            <<_epsilon D^epsilon. (6.6)

It uses only the already known divisor-bound coefficient count and finite HB dyads; no Mobius cancellation is claimed. After summing both outer families and ONLY THEN the original finite source/e/w and O(V) exact s family, the available BOTH-TypeI certificate is

 |P_(I,I,J)| <<B²(DX)^epsilon A1V I(cLambda) J^(-3/2),
 |P_(I,I,short k)| <<B²(DX)^epsilon A1V I(cLambda).       (6.7)

Unit plus the finitely many dyadic J bands give the second line, with the ORIGINAL K and J0 still finite. At A1~D^(3/4),X=D^(3/8) this is the inherited normalized13/16 budget, not target3/4. Raw numerators have an additional D.

This new matched pair input is NOT a frontier power improvement: the accepted finite-k theorem3df39872 already gives the stronger J^(-2) bound for nonunit bands with all actual coefficients, while both methods leave the unit/very-short-frequency means. The new content is the pair-first exact kernel/family match and the precise failed inference;(6.7) must not be advertised as a new signed saving or a solved TypeI model.

## 7. The precise obstruction and what still needs arithmetic

The direct long-long matrix proposed in(2.3) has not been created for free: its leftover Gauss cocycle exactly reinstates coprime incidence. The legitimate cube-free encoding has physical height LM*min(L,M), not radical LM. The better matched Proposition8.1 still contains LM and does not control the special Gauss-coefficient mean more sharply merely because the long unrestricted coefficients are1.

For clarity, let E be ANY actual finite pair-row support after original SF/coprime/source/s/w/unequal restrictions. At k=O, R_((v,z),O)=1 for every(v,z)in E, so the auxiliary one-column matrix has norm exactly sqrt(#E). More generally a fixed nonunit k column has norm sqrt(#{rows in E coprime to k}). These are operator facts; we make NO assertion that #E is large/nonzero in every block and NO lower bound for the actual vector u or physical P. They explain why an arbitrary-coefficient matrix estimate cannot uniformly replace its complete row-count term by a power-saving one at that frequency. The actual u includes bar G_v G_z, source/root phases, common W and all HB coefficients and may cancel.

In particular the unit-k contribution that remains is the actual signed sum of

 sum_(v,z actual full pair masks) Xi_omega(v,z;p,r,w,s)
      bar G_v G_z W(NpNv/D)bar W(NrNz/D)/sqrt(NvNz)
        *dotG(A1Nw(Ns)^6/[NeF_S NpNr NvNz]),             (7.1)

with the ORIGINAL outer H,allrho/e/w/s phases and normalizing(1.4). It is not the product of two free Gauss means because(v,z)=1 and the other full-union conditions remain. Neither a conductor/radical reindexing nor a claim that modulus-one Gauss weights are harmless controls(7.1). Reopening the common-prime mask would shift BOTH Gauss frequencies and preserve signed virtual divisors; no such estimate is supplied by(5.1).

A sufficient further input would control this actual short-k paired Gauss vector, coherently with all its finite outer signs/means, by the extra D^(-1/16+epsilon) needed relative to the13/16 certificate at the declared pure scales, or prove compensation with other ORIGINAL pieces. This is a criterion, not a new equivalent identity called a bound. Root's separate short-k frequency localization is not reproved here.

The full fixed-s signed13/12 and unsigned9/8 comparisons remain unchanged. Other dual sectors, the complete small-A_Y model, determinant/zero-location/spectral/GRH and actual analytic/categoryLean scopes remain open. No Artin holomorphy, desired zeros, fixed-conductor Gauss first moment, discarded orientation mean, positive energy or individual-component lower bound is assumed.
