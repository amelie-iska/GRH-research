#!/usr/bin/env python3
"""Append accurate reviewed-release metadata before freezing selection; no live claim."""
from pathlib import Path
import hashlib,json,subprocess,os
R=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
C=R/"outputs/checks/2026-11-06-coherent-release/root"
sha=lambda b:hashlib.sha256(b).hexdigest()
def main():
 out=C/"release-metadata-v1";assert not out.exists();out.mkdir()
 milestone=json.loads((R/"outputs/checks/2026-11-06-coherent-book/MILESTONE_ACCEPTED-v1.json").read_text());assert milestone["passed"]
 promotion=json.loads((R/"outputs/checks/2026-11-06-coherent-book/promotion-v1/promotion-v1.json").read_text())
 for row in promotion["changed_artifacts"]:assert sha((R/row["target"]).read_bytes())==row["after_sha256"]
 common="""\n\n## Reviewed coherent-book release edition — 6 November 2026\n\nThe reviewed release edition contains a 319-page book with 40 chapters and 9,810 native MathML formulas, focused articles of 76/215 pages and analytic notes of 34/105 pages. All 9,172 previous literal math subtrees, 389 tables, 13 earlier canonical inspectors and 29 SVG references are preserved; totals are 14 inspectors and 30 SVG references. The readable original workflow and complete matrix inspector retain all 1,218 saved auxiliary positions, actual ideal generators/factors, complex numerical values and raw zeros. Saved55-digit values are numerical consistency, not interval certificates, trained models or complete original-family data.\n\nThe shared coherent-band sources give primitive root normalization, exact finite Poisson/BV-prefix comparisons, actual-cutoff/profile Schur transfer, the restricted identity-divisor cubic comparison, full primal equal-norm localization and the literal-ray mean. Separate UB01 research is Main-only evidence outside the book and browser data. The original unweighted A6=1 two-pivot signed h1 bound13/12 and global unsigned9/8 remain unchanged. Full signed unequal-norm cancellation, short/principal assembly, independent positive arithmetic determinant/zero-location bridges, analytic/category Lean and GRH remain open.\n\nThis section describes verified CONTENT prepared for substantive publication; it does not certify that deployment has completed. A new release requires its exact frozen selection, source/credential/visibility/integrity gates, strict project-prefix browser checks and postpublication hosted hashes/trees. The final PUBLIC_RELEASE_VERIFIED receipt and post-release handoff will govern actual deployed commits. Earlier303-page/local-only statements above are dated historical preparation snapshots. Both completion gates remain false and the one existing heartbeat remains active. Original sources, all old HEAD/index states/worktrees, outputs/caches/environments, Mac workspace/old8765 and private active data remain protected. No Linux4.24 install/substitution/repeated question is authorized.\n"""
 readme="""\n\n## Reviewed coherent-book release edition\n\nThe reviewed edition contains **319 pages and 9,810 native MathML formulas**, with all previous math retained. Read the [coherent-band chapter](https://amelie-iska.github.io/GRH-research/book/main.html#cbk:core) and the [matrix inspector](https://amelie-iska.github.io/GRH-research/coherent-band.html). Five editions are provided: [book](https://amelie-iska.github.io/GRH-research/book.pdf), [concise article](https://amelie-iska.github.io/GRH-research/concise.pdf), [extended article](https://amelie-iska.github.io/GRH-research/extended.pdf), [concise analytic notes](https://amelie-iska.github.io/GRH-research/validated-oracle-concise.pdf), and [extended analytic notes](https://amelie-iska.github.io/GRH-research/validated-oracle-extended.pdf).\n\nThe inspector exposes all 1,218 saved auxiliary matrix positions, exact ideal labels/masks and saved complex values. It performs no training and supplies no new interval or GRH certificate. Independent proof/source/artifact reviews, five source-bound PDF builds and desktop/mobile/night/keyboard checks govern the edition. The full signed estimate, positive determinant/zero-location bridge and comprehensive Lean formalization remain open; the existing heartbeat continues. This describes reviewed release content; deployment is certified separately by its publication receipt. Earlier303-page and local-only notes are historical snapshots.\n"""
 names=["README.md","planning/MASTER_IMPLEMENTATION_PLAN.md","planning/PROGRESS.md","planning/CONTINUATION.md","planning/OPEN_OBLIGATIONS.md","book/SOURCE_COVERAGE.md","book/VERIFICATION.md"]
 rows={}
 for name in names:
  p=R/name;old=p.read_bytes();backup=out/"before"/name;backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes(old)
  new=old+(readme if name=="README.md" else common).encode();p.write_bytes(new);assert new.startswith(old)
  rows[name]={"before_sha256":sha(old),"sha256":sha(new),"bytes":len(new),"append_only":True}
 for name in ["web/verification.html","web/implementation-plan.html"]:
  p=R/name;backup=out/"before"/name;backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes(p.read_bytes())
 env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"}
 for script in ["scripts/build_verification_page.py","scripts/build_implementation_page.py"]:
  run=subprocess.run(["python3",script],cwd=R,env=env,capture_output=True,text=True,check=True)
  (out/(Path(script).stem+".log")).write_text(run.stdout+run.stderr)
 for name in ["web/verification.html","web/implementation-plan.html"]:
  p=R/name;rows[name]={"sha256":sha(p.read_bytes()),"bytes":p.stat().st_size,"generated_from_current_ledgers":True}
 record=dict(passed=True,classification="current_prepublication_release_metadata_NOT_live_receipt",files=rows,scientific_sources_or_PDF_native_runtime_changed=False,old_records_preserved=True,source_only_UB01_in_Main_not_book_or_Pages=True,public_release_performed=False,new_Lean_declarations=0,project_complete=False,research_complete=False,producer_sha256=sha(Path(__file__).read_bytes()))
 p=out/"receipt.json";p.write_text(json.dumps(record,indent=2)+"\n");print(json.dumps(dict(passed=True,path=str(p),sha256=sha(p.read_bytes()))))
if __name__=="__main__":main()
