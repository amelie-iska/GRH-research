"""Known human-language positive control. Source provenance establishes intent;
compressibility alone does not. Within-book heldout bytes, not new-author testing.
"""
import argparse,collections,hashlib,json,lzma,math,urllib.request,zlib
from pathlib import Path

def run(raw:bytes):
 text=raw.decode('utf-8-sig')
 start=text.find('*** START OF THE PROJECT GUTENBERG EBOOK');end=text.find('*** END OF THE PROJECT GUTENBERG EBOOK')
 if start<0 or end<0 or end<=start:raise ValueError('Expected Gutenberg boundaries missing')
 start=text.index('\n',start)+1;data=text[start:end].encode('utf8');n=len(data);a=int(.6*n);b=int(.8*n)
 train=data[:a];val=data[a+32:b];test=data[b+32:]
 candidates=[]
 for order in (0,1,2,3):
  table={};glob=collections.Counter(train)
  for i in range(order,len(train)):
   key=train[i-order:i] if order else b'';table.setdefault(key,collections.Counter())[train[i]]+=1
  totals={k:sum(v.values()) for k,v in table.items()};global_total=sum(glob.values())
  for alpha in (.1,.5,1.):
   def score(chunk):
    total=0.
    for i in range(order,len(chunk)):
     key=chunk[i-order:i] if order else b'';c=table.get(key,glob);den=totals.get(key,global_total);total-=math.log2((c.get(chunk[i],0)+alpha)/(den+256*alpha))
    return total/(len(chunk)-order)
   candidates.append(dict(order=order,alpha=alpha,validation_bpb=score(val),test_bpb=score(test),initial_context_bytes=order,model_entries=len(table)))
 best=min(candidates,key=lambda x:(x['validation_bpb'],x['order'],x['alpha']))
 return dict(schema='grh.text-control.v1',source='https://www.gutenberg.org/ebooks/11',download='https://www.gutenberg.org/files/11/11-0.txt',title='Alice\u2019s Adventures in Wonderland',author='Lewis Carroll',source_sha256=hashlib.sha256(raw).hexdigest(),body_sha256=hashlib.sha256(data).hexdigest(),source_bytes=len(raw),body_bytes=n,split_bytes=[len(train),len(val),len(test)],selected=best,candidates=candidates,zlib_test_bpb=8*len(zlib.compress(test))/len(test),lzma_test_bpb=8*len(lzma.compress(test))/len(test),scope='Known human-authored English positive control. Exact UTF8 byte likelihood, not a physical-recording or learned grammar result. Source boilerplate excluded, no same-byte overlap, validation selection only; test codelength conditional on prefix. Counts and standard compressors, no native neural run. No general conclusion about arbitrary natural languages or latent messages.')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--cache',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 if not a.cache.exists():a.cache.write_bytes(urllib.request.urlopen('https://www.gutenberg.org/files/11/11-0.txt',timeout=30).read(1000000))
 result=run(a.cache.read_bytes());a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result['selected']))
