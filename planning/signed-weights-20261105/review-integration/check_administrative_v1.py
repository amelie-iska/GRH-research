"""Bound only final promotion/admin metadata; do not rerun accepted arithmetic."""
from pathlib import Path
import json,hashlib,subprocess,re,html
R=Path(__file__).resolve().parents[3];P=R/'planning/signed-weights-20261105/review-integration';O=R/'outputs/checks/2026-11-05-signed-weights/review-integration';h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(n):return json.loads((R/n).read_text())
def main():
 old=load(str((O/'integration-v1.json').relative_to(R)));a=load(str((O/'acceptance-v1.json').relative_to(R)));pr='outputs/checks/2026-11-05-signed-weights/promotion-v1/promotion-v1.json';prom=load(pr);assert prom['passed'];targets={}
 for x in prom['changed_artifacts']:
  assert h(R/x['target'])==x['after_sha256']==h(R/x['source']);targets[x['target']]=x['after_sha256']
 assert len(targets)==15 and h(R/'web/book/main.html')==old['candidate_HTML_sha256']
 mp=R/'outputs/checks/2026-11-05-signed-weights/root/final-metadata-v1/record.json';m=json.loads(mp.read_text());changed=set(m['sha256']);assert changed=={'README.md','planning/PROGRESS.md','book/SOURCE_COVERAGE.md','book/VERIFICATION.md'}
 for n,d in m['sha256'].items():
  assert h(R/n)==d;before=mp.parent/n.replace('/','__');assert h(before)==old['documentation_source_sha256'][n]
  if n=='README.md':
   before_text=before.read_text();x='Current edition: **266 pages,40 chapters,7,605 MathML expressions and thirteen unique in-book laboratories**.';y='Current edition: **272 pages,40 chapters,7,891 MathML expressions and thirteen unique in-book laboratories**.';assert before_text.count(x)==1 and(R/n).read_text()==before_text.replace(x,y,1)
  else:assert(R/n).read_bytes().startswith(before.read_bytes())
 for n,d in old['documentation_source_sha256'].items():
  if n not in changed:assert h(R/n)==d
 for n,d in old['shared_and_build_source_bindings'].items():assert h(R/n)==d,n
 cp='outputs/checks/2026-11-05-signed-weights/root/checkpoint-v1.json';c=load(cp);assert c['id']=='d41ee2ae-ecba-4b76-8e9e-0500b5b1a0da';run=R/'outputs/loop/runs'/(c['id']+'.json');assert run.read_bytes()==(R/cp).read_bytes();q=load('planning/IMPLEMENTATION_QUEUE.json');assert q['project_complete'] is False and q['research_complete'] is False;task=next(t for t in q['tasks']if t['id']==c['task']['id']);assert task==c['task']and task['status']=='in_progress'
 pages={}
 for web,doc in [('web/implementation-plan.html','planning/MASTER_IMPLEMENTATION_PLAN.md'),('web/verification.html','book/VERIFICATION.md')]:
  pres=[html.unescape(t).strip()for t in re.findall(r'<pre\b[^>]*>(.*?)</pre>',(R/web).read_text(),re.S)];assert(R/doc).read_text().strip()in pres,web;pages[web]=h(R/web)
 assert pages['web/verification.html']=='e0ac1eee9df0221ec5ee1709edaaf09e0839818a08346e3e094c47565e892026'
 s=(R/'web/index.html').read_text();assert all(x in s for x in ['272','7,891','62/168','20/59','#fixed-h1'])
 base=R.parent/'GRH-publication-20261105-signed-weights/outputs/publication/20261105-signed-weights/release-preparation-v1/baseline-v1.json';states=json.loads(base.read_text())['protected_source_and_seven_prior_worktrees']
 for e in states:
  root=Path(e['path']);head=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip();ip=Path(subprocess.check_output(['git','-C',str(root),'rev-parse','--git-path','index'],text=True).strip());ip=ip if ip.is_absolute()else root/ip;assert head==e['HEAD']and h(ip)==e['index_sha256']
 r=dict(passed=True,parent_acceptance_sha256=h(O/'acceptance-v1.json'),promotion_receipt_sha256=h(R/pr),promoted_targets_sha256=targets,final_metadata_record_sha256=h(mp),current_metadata_sha256=m['sha256'],remaining_scientific_doc_inputs_unchanged=5,all_build_inputs_unchanged=True,checkpoint_id=c['id'],checkpoint_sha256=h(R/cp),checkpoint_run_sha256=h(run),P7_status=task['status'],project_complete=False,research_complete=False,current_queue_sha256=h(R/'planning/IMPLEMENTATION_QUEUE.json'),generated_page_sha256=pages,current_landing_sha256=h(R/'web/index.html'),protected_states=states,old_math_or_controls_rerun=False,checker_sha256=h(Path(__file__)),scope='Postpromotion/current metadata/admin binding only; accepted full integration reused')
 with(O/'administrative-addendum-v1.json').open('x')as f:json.dump(r,f,indent=2);f.write('\n')
 text='''PASS: all15promoted targets match the accepted source-bound candidates. Exact READMEtop266/7605to272/7891 replacement and append-only delivered-count paragraphs in PROGRESS/COVERAGE/VERIFICATION are the only changes to the nine pinned scientific documents; five other documents and every build input are unchanged. Checkpoint and exact P7 queue task agree, remain in_progress, and both completion gates are false. Generated implementation/verification pre blocks match current documents. Root regenerated the stale verification page from the current ledger before this acceptance; current SHAe0ac1eee is pinned. Landing counts/link are current. All8protected source/prior-release HEAD/index states remain unchanged. This updates acceptance-v1 prepromotion limitations without rerunning math preservation, builds, row/phase/Mellin controls. Publication/preflight remain root-gated.\n'''
 with(P/'ADMINISTRATIVE-ADDENDUM-v1.md').open('x')as f:f.write(text)
 a.update(scope='Current promoted integration plus bounded final metadata/checkpoint; publication separate',supersedes='acceptance-v1 prepromotion/current-metadata limitations only; prior bytes preserved',administrative_addendum_path=str((O/'administrative-addendum-v1.json').relative_to(R)),administrative_addendum_sha256=h(O/'administrative-addendum-v1.json'),administrative_prose_sha256=h(P/'ADMINISTRATIVE-ADDENDUM-v1.md'),current_promoted_targets_sha256=targets,current_metadata_sha256=m['sha256'],current_queue_sha256=r['current_queue_sha256'],current_generated_pages_sha256=pages,current_landing_sha256=r['current_landing_sha256'],protected_states_preserved=8,limitations=['Publication remains root-gated','No new signed5/12saving, Lean or GRH'])
 with(O/'acceptance-v2.json').open('x')as f:json.dump(a,f,indent=2);f.write('\n')
 print(json.dumps(dict(passed=True,acceptance_v2_sha256=h(O/'acceptance-v2.json'),admin_addendum_sha256=h(O/'administrative-addendum-v1.json'),promoted_targets=15,protected_states=8)))
if __name__=='__main__':main()
