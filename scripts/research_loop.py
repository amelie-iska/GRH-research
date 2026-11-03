#!/usr/bin/env python3
"""Atomic task selection/checkpointing for the app's existing scheduled loop.

This helper is not a scheduler or proof checker. The scheduled agent must
perform the governing plan's scientific acceptance checks and review evidence.
It never executes arbitrary shell commands or deletes histories.
"""
from pathlib import Path
import argparse,json,fcntl,uuid
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
STATUSES={'pending','in_progress','complete','waiting_dependency'}

def validate(data):
 tasks=data['tasks'];ids=[t['id'] for t in tasks]
 if len(ids)!=len(set(ids)):raise ValueError('Duplicate task ids')
 by={t['id']:t for t in tasks}
 def visit(key,ancestors):
  if key in ancestors:raise ValueError('Dependency cycle')
  for d in by[key]['dependencies']:
   if d not in by:raise ValueError('Missing dependency '+d)
   visit(d,ancestors|{key})
 for task in tasks:
  if task['status'] not in STATUSES:raise ValueError('Unknown status')
  visit(task['id'],set())
 return by

def ready(data):
 by=validate(data)
 return sorted([t for t in data['tasks'] if t['status'] in {'pending','in_progress'} and all(by[d]['status']=='complete' for d in t['dependencies'])],key=lambda t:t['priority'])

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('action',choices=['status','next','claim','checkpoint']);p.add_argument('--queue',type=Path,default=ROOT/'planning/IMPLEMENTATION_QUEUE.json');p.add_argument('--task');p.add_argument('--owner');p.add_argument('--result');p.add_argument('--evidence',action='append',default=[]);p.add_argument('--status',choices=sorted(STATUSES),default='in_progress');a=p.parse_args()
 lockdir=ROOT/'outputs/loop';lockdir.mkdir(exist_ok=True);lock=(lockdir/'queue.lock').open('a+')
 with lock:
  fcntl.flock(lock,fcntl.LOCK_EX)
  data=json.loads(a.queue.read_text());by=validate(data)
  if a.action=='status':print(json.dumps(data,indent=2));return
  if a.action=='next':print(json.dumps(ready(data)[0] if ready(data) else {'next':None,'research_complete':data['research_complete']},indent=2));return
  if not a.task or a.task not in by or not a.owner:p.error('claim/checkpoint require an existing --task and --owner')
  task=by[a.task]
  if task.get('owner') and task['owner']!=a.owner:raise ValueError('Task owned by '+task['owner']+'; reconcile concurrent work before editing')
  if a.action=='claim':
   if task not in ready(data):raise ValueError('Task is not ready')
   task['owner']=a.owner;task['status']='in_progress'
  else:
   if not a.result:p.error('checkpoint requires a concrete --result')
   if a.status=='complete' and not a.evidence:p.error('Completion requires evidence and actual agent review against acceptance criteria')
   for name in a.evidence:
    if not (ROOT/name).is_file():raise ValueError('Missing evidence '+name)
   task['status']=a.status;task['last_result']=a.result;task['evidence']=a.evidence
  stamp=datetime.now(timezone.utc).isoformat();task['updated_utc']=stamp
  history=lockdir/'runs';history.mkdir(exist_ok=True)
  run=dict(id=str(uuid.uuid4()),utc=stamp,action=a.action,owner=a.owner,task=dict(task),note='Administrative checkpoint; scientific validity comes from reviewed evidence')
  (history/(run['id']+'.json')).write_text(json.dumps(run,indent=2)+'\n')
  temp=a.queue.with_suffix('.pending.json');temp.write_text(json.dumps(data,indent=2)+'\n');temp.replace(a.queue)
  print(json.dumps(run,indent=2))
if __name__=='__main__':main()
