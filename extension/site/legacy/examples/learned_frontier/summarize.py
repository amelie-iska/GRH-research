#!/usr/bin/env python3
"""Aggregate preserved independent seeds and numerical/exact example evidence."""
from pathlib import Path
import json,statistics
ROOT=Path(__file__).resolve().parents[2]
base=ROOT/'outputs/experiments/learned-frontier'
runs=[json.loads((base/name/'record.json').read_text()) for name in ['generative-20261104-v1','generative-20261104-seed2','generative-20261104-seed3']]
summary=[]
for i in range(4):
    values=[r['records'][i] for r in runs]
    summary.append(dict(objective=values[0]['objective'],architecture=values[0]['architecture'],seeds=[v['seed'] for v in values],parameters=values[0]['parameters'],steps=2000,metrics={name:dict(mean=statistics.mean(v['evaluation'][name] for v in values),std=statistics.stdev(v['evaluation'][name] for v in values)) for name in ['total_variation','sliced_W1_16directions','dequantization_MSE','oracle_field_MSE']},wall_seconds=sum(v['wall_seconds'] for v in values)))
read=lambda p:json.loads((ROOT/p).read_text())
state=read('outputs/experiments/learned-frontier/state-flow-20261104-v1/record.json');gpu=read('outputs/experiments/learned-frontier/cuquantum-20261104-v3.json');width=read('outputs/checks/2026-11-04-learned-frontier/width-limits.json');geometry=read('examples/learned_frontier/geometry/outputs/exact.json');hardware=read('examples/learned_frontier/hardware/evidence-2026-11-04.json')
fields=read('outputs/checks/2026-11-04-learned-frontier/coefficient-fields.json')
result=dict(fields=fields,summary=summary,state_flow=state,gpu=gpu,width=width,geometry=geometry,hardware=dict(checks=hardware['checks'],negative_controls_detected=hardware['negative_controls_detected'],limitations=hardware['limitations']),gaussian_baseline=runs[0]['gaussian_baseline'],independent_target_control=runs[0]['independent_target_control'],exact_reverse_controls=[r['exact_teacher_reverse_control'] for r in runs[1:]])
p=ROOT/'web/data/learned-frontier/summary.json';p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(summary,indent=2))
print('geometry case keys:',list(geometry['dessin']['cases']))
