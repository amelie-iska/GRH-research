# Fresh saved-state coupled-short coefficient check

PASS; no character, ideal-enumeration, original-pair or raw evaluator run was repeated. The immutable new D200/D512/D900 records expose every active-profile g=fa and its original A_U coefficient. A separate standard-library saved-state checker verifies the root/C short-coefficient formula on that exact support.

For good squarefree g with Ng<=7U, the asserted coefficient formula is

A_U(g)=mu(g)(2*1_(Ng<=U)-1).

The check verifies every saved goodSFg in this range:19,33,57 ideals respectively, including the unit. It also verifies all2510 active-profile rough-kernel occurrences (365,1435,710;8,15,15 distinctg), with P>U, D<P Ng<2D and Ng<7U. Every coefficient equals exactly+1 or-1. Raw f-masked/character-zero states are retained in this count; active profile does not mean every term contributes after raw masks.

The coupled threshold is Ng=Nf Na, not separate thresholds for f and a. Stored active examples reject replacing A_U(fa) by A_U(f)A_U(a). The explicit out-of-domain negative uses captured ORIGINAL D200 column universeID73, generator(-17,-3), norm247=13*19, primeIDs3,5, mu+1 and actualA+1. Since247>7U70, blindly applying the short formula would give-1 and is rejected. This prevents extending the lemma to every original annular column or unrestricted multiplicativity.

The pure-case capacities are critical (H^4<=D^3), and all five/seven actual rows have rough-prime ideal countkappa1. The mixedD900 declaredH384 is noncritical; its two rows have kappa0. No H=floorD^.75 assertion is made for that mixed fixture. The saved-state counts do not prove the general coefficient/geometric theorem, explicit analytic error constants, or any asymptotic saving.

Checker planning/rough-mask-20261105/finite/check_coupled_short_v1.py; receipt outputs/checks/2026-11-05-rough-mask/finite/coupled-short-coefficients-v1.json SHAb9f57e6953ab6773c2fd4a44952df67f3759fc34c67b9d733f3be31b8ac71232. Inputrunmanifest remains d8ebdc9410e0e24c3dfd999ea33c10864d28b4e9f008913e08d26233217268cf, all original data/source unchanged.
