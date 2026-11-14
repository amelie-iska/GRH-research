"""Acquire the exact bounded physical/communication control selection.

Speaker/chapter/utterance identities are fixed, not selected by prediction score.
The official archive is streamed under a byte budget. Chapter transcripts remain
chapter-specific; the selected text is verified against every audio identifier.
A prefix hash is never mislabeled as the complete archive checksum.
"""
from __future__ import annotations
import argparse,hashlib,json,tarfile,urllib.request
from pathlib import Path
from datetime import datetime,timezone

SPEECH_URL='https://openslr.trmal.net/resources/12/test-clean.tar.gz'
SELECTION={
 '6930':('75918',['0000','0002','0004','0005','0006','0007']),
 '1320':('122617',['0002','0003','0012','0022','0025','0026']),
 '5639':('40744',['0001','0002','0023','0030','0032','0033']),
}
MAX_COMPRESSED=96*1024**2


def sha(data):return hashlib.sha256(data).hexdigest()
def get(url,limit=5_000_000):
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'GRH-research reproducible controls'}),timeout=60)as r:data=r.read(limit+1)
 if len(data)>limit:raise ValueError('Download budget exceeded')
 return data


class BoundedStream:
 def __init__(self,response):self.response=response;self.count=0;self.digest=hashlib.sha256()
 def read(self,n=-1):
  if n<0:n=65536
  if self.count+n>MAX_COMPRESSED:raise ValueError('Archive prefix byte budget exceeded')
  data=self.response.read(n);self.count+=len(data);self.digest.update(data);return data


def selected_transcripts(texts,audio_ids):
 table={}
 for name,text in texts.items():
  for line in text.splitlines():
   parts=line.split(maxsplit=1)
   if len(parts)!=2:raise ValueError('Malformed transcript in '+name)
   key,value=parts
   if key in table and table[key]!=value:raise ValueError('Conflicting transcript identity')
   table[key]=value
 if len(audio_ids)!=len(set(audio_ids)):raise ValueError('Duplicate audio identity')
 missing=set(audio_ids)-set(table)
 if missing:raise ValueError('Missing chapter-specific transcripts: '+', '.join(sorted(missing)))
 return [{'utterance_id':key,'text':table[key]}for key in sorted(audio_ids)]


def save_source(path,data):
 path.parent.mkdir(parents=True,exist_ok=True)
 if path.exists()and path.read_bytes()!=data:raise ValueError('Existing source differs: '+str(path))
 path.write_bytes(data)


def acquire(root):
 root.mkdir(parents=True,exist_ok=True);files=[]
 checksum_url='https://gwosc.org/GW150914data/md5.txt';checksum=get(checksum_url).decode()
 for short,prefix in [('H-H1','H-H1'),('L-L1','L-L1')]:
  name=prefix+'_LOSC_4_V2-1126259446-32.txt.gz';url='https://gwosc.org/GW150914data/'+name
  path=root/(short+'.txt.gz');data=path.read_bytes()if path.exists()else get(url);actual=hashlib.md5(data).hexdigest()
  lines=[line for line in checksum.splitlines()if name in line]
  if not lines or not any(actual in line for line in lines):raise ValueError('Official GWOSC checksum mismatch: '+name)
  save_source(path,data);files.append(dict(kind='measured_strain',url=url,path=path.name,sha256=sha(data),bytes=len(data),official_md5=actual,checksum_source=checksum_url,license='CC-BY-4.0'))
 wanted={};ids=[]
 for speaker,(chapter,utterances)in SELECTION.items():
  base=f'LibriSpeech/test-clean/{speaker}/{chapter}/'
  wanted[base+f'{speaker}-{chapter}.trans.txt']=root/'speech'/speaker/f'{speaker}-{chapter}.trans.txt'
  for suffix in utterances:
   identity=f'{speaker}-{chapter}-{suffix}';ids.append(identity);wanted[base+identity+'.flac']=root/'speech'/speaker/(identity+'.flac')
 remaining=set(wanted);texts={}
 with urllib.request.urlopen(SPEECH_URL,timeout=60)as response:
  stream=BoundedStream(response)
  with tarfile.open(fileobj=stream,mode='r|gz')as archive:
   for member in archive:
    if member.name not in remaining:continue
    if not member.isfile()or not 0<member.size<=2_000_000:raise ValueError('Unexpected requested archive member')
    data=archive.extractfile(member).read();path=wanted[member.name];save_source(path,data);remaining.remove(member.name)
    files.append(dict(kind='speech_transcript'if path.suffix=='.txt'else'known_human_speech',archive_url=SPEECH_URL,member=member.name,path=str(path.relative_to(root)),sha256=sha(data),bytes=len(data),license='CC-BY-4.0'))
    if path.suffix=='.txt':texts[member.name]=data.decode()
    if not remaining:break
  prefix=dict(compressed_prefix_bytes=stream.count,compressed_prefix_sha256=stream.digest.hexdigest(),complete_archive_downloaded=False)
 if remaining:raise ValueError('Missing archive members: '+str(sorted(remaining)))
 rows=selected_transcripts(texts,ids);target=root/'selected-transcripts.json';target.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
 result=dict(schema='grh.physical-control-acquisition.v2',retrieved_at_utc=datetime.now(timezone.utc).isoformat(),selection=SELECTION,files=files,transcript_coverage=dict(audio_utterances=len(ids),matched_transcripts=len(rows),missing=0,selected_transcripts_sha256=sha(target.read_bytes()),used_as_predictor_input=False),**prefix)
 (root/'acquisition-verified.json').write_text(json.dumps(result,indent=2)+'\n')
 return result

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);a=p.parse_args();r=acquire(a.root);print(json.dumps(r,indent=2))
