#!/usr/bin/env python3
"""Refresh the local plan/queue page from versioned governance files."""
from theme_assets import install_theme
from pathlib import Path
import html,json
ROOT=Path(__file__).resolve().parents[1]
def main():
 plan=(ROOT/'planning/MASTER_IMPLEMENTATION_PLAN.md').read_text();data=json.loads((ROOT/'planning/IMPLEMENTATION_QUEUE.json').read_text());cards=[]
 complete=sum(t['status']=='complete' for t in data['tasks'])
 for t in data['tasks']:
  cards.append('<article><p class="eyebrow">'+html.escape(t['id'])+' · '+html.escape(t['status'])+'</p><h3>'+html.escape(t['objective'])+'</h3><p>'+html.escape(t['acceptance'])+'</p>'+('<p class="scope">Latest checkpoint: '+html.escape(t['last_result'])+'</p>' if t.get('last_result') else '')+'</article>')
 body='<p><a href="/">Research atlas</a> · <a href="/book/main.html">On-page book</a></p><h1>Plan and implementation loop</h1><p>The existing hourly loop is active. '+str(complete)+' of '+str(len(data['tasks']))+' queued tasks have checked evidence. This is a task count, not a percentage of a GRH proof.</p><p>Implementation completion and rigorously reviewed research completion are separate gates. The loop resumes one ready concrete deliverable, records checks, updates the page and publishes reviewed substantive milestones.</p><div class="cards">'+''.join(cards)+'</div><details><summary>Read the complete governing plan</summary><pre>'+html.escape(plan)+'</pre></details>'
 (ROOT/'web/implementation-plan.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Implementation plan and loop</title><link rel="stylesheet" href="/style.css"></head><body><main><section>'+body+'</section></main></body></html>')
if __name__=='__main__':
 main()
 install_theme(ROOT/'web/implementation-plan.html')
