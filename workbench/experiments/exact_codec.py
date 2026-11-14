"""An emitted, independently decodable count-model + exact-residual code.

The container pays for its frozen probability model, representatives, segment
lengths, initial samples and coder termination. It is lossless for the declared
int16/int32 representation, not necessarily for an instrument's original file.
"""
from __future__ import annotations
import bisect,json,math,struct,zlib
from collections import Counter
import numpy as np

TOTAL=65536
MASK=(1<<32)-1
HALF=1<<31
QUARTER=1<<30
THREE=3<<30
MAGIC=b'GRHC01'
MAX_SAMPLES=2_000_000

class Bits:
 def __init__(self):self.data=bytearray();self.current=0;self.used=0;self.count=0
 def bit(self,value):
  self.current=(self.current<<1)|int(bool(value));self.used+=1;self.count+=1
  if self.used==8:self.data.append(self.current);self.current=0;self.used=0
 def integer(self,value,width):
  if type(value)is not int or type(width)is not int or width<0 or width>64 or value<0 or value>=1<<width:raise ValueError('Invalid bit integer')
  for i in range(width-1,-1,-1):self.bit((value>>i)&1)
 def gamma(self,value):
  if type(value)is not int or not 1<=value<1<<63:raise ValueError('Gamma value out of domain')
  length=value.bit_length();self.integer(0,length-1);self.integer(value,length)
 def finish(self):return bytes(self.data)+(bytes([self.current<<(8-self.used)])if self.used else b'')

class Reader:
 def __init__(self,data,padded=False):self.data=data;self.position=0;self.padded=padded
 def bit(self):
  p=self.position;self.position+=1
  if p>=8*len(self.data):
   if self.padded:return 0
   raise ValueError('Truncated bitstream')
  return (self.data[p//8]>>(7-p%8))&1
 def integer(self,width):
  if not 0<=width<=64:raise ValueError('Invalid width')
  v=0
  for _ in range(width):v=(v<<1)|self.bit()
  return v
 def gamma(self):
  zeros=0
  while self.bit()==0:
   zeros+=1
   if zeros>=63:raise ValueError('Gamma overflow')
  return (1<<zeros)|self.integer(zeros)

class Encoder:
 def __init__(self):self.low=0;self.high=MASK;self.pending=0;self.bits=Bits()
 def emit(self,bit):
  self.bits.bit(bit)
  for _ in range(self.pending):self.bits.bit(1-bit)
  self.pending=0
 def put(self,symbol,cdf):
  width=self.high-self.low+1
  self.high=self.low+(width*cdf[symbol+1]//TOTAL)-1
  self.low=self.low+width*cdf[symbol]//TOTAL
  while True:
   if self.high<HALF:self.emit(0)
   elif self.low>=HALF:self.emit(1);self.low-=HALF;self.high-=HALF
   elif self.low>=QUARTER and self.high<THREE:self.pending+=1;self.low-=QUARTER;self.high-=QUARTER
   else:break
   self.low=(self.low<<1)&MASK;self.high=((self.high<<1)|1)&MASK
 def finish(self):
  self.pending+=1;self.emit(0 if self.low<QUARTER else 1);return self.bits.finish()

class Decoder:
 def __init__(self,data):self.low=0;self.high=MASK;self.bits=Reader(data,padded=True);self.value=self.bits.integer(32)
 def get(self,cdf):
  width=self.high-self.low+1;scaled=((self.value-self.low+1)*TOTAL-1)//width
  symbol=bisect.bisect_right(cdf,scaled)-1
  if not 0<=symbol<len(cdf)-1:raise ValueError('Arithmetic symbol out of range')
  self.high=self.low+width*cdf[symbol+1]//TOTAL-1;self.low=self.low+width*cdf[symbol]//TOTAL
  while True:
   if self.high<HALF:pass
   elif self.low>=HALF:self.low-=HALF;self.high-=HALF;self.value-=HALF
   elif self.low>=QUARTER and self.high<THREE:self.low-=QUARTER;self.high-=QUARTER;self.value-=QUARTER
   else:break
   self.low=(self.low<<1)&MASK;self.high=((self.high<<1)|1)&MASK;self.value=((self.value<<1)|self.bits.bit())&MASK
  return symbol


def cdf(counts):
 if not 1<=len(counts)<=64 or any(type(x)is not int or x<0 or x>10**9 for x in counts):raise ValueError('Invalid counts')
 weights=[2*x+1 for x in counts];den=sum(weights);freq=[1+(TOTAL-len(counts))*x//den for x in weights];freq[-1]+=TOTAL-sum(freq)
 out=[0]
 for x in freq:out.append(out[-1]+x)
 if out[-1]!=TOTAL or any(a>=b for a,b in zip(out,out[1:])):raise ValueError('Invalid frequency table')
 return out


def fit(symbol_segments,K,order=2):
 if type(K)is not int or not 1<=K<=64 or type(order)is not int or not 0<=order<=4:raise ValueError('Invalid model dimensions')
 table={};fallback=[0]*K
 for segment in symbol_segments:
  history=[]
  for value in segment:
   y=int(value)
   if not 0<=y<K:raise ValueError('Symbol out of domain')
   key=tuple(history[-order:])if order else ();row=table.setdefault(key,[0]*K);row[y]+=1;fallback[y]+=1;history.append(y)
 if len(table)>100000:raise ValueError('Model too large')
 return dict(K=K,order=order,rows=[[list(k),v]for k,v in sorted(table.items())],fallback=fallback,smoothing='Jeffreys half-count, then deterministic positive 16-bit frequencies')


def tables(model):
 if type(model)is not dict or type(model.get('K'))is not int or not 1<=model['K']<=64 or type(model.get('order'))is not int or not 0<=model['order']<=4:raise ValueError('Invalid frozen model')
 if type(model.get('rows'))is not list or len(model['rows'])>100000:raise ValueError('Invalid rows')
 result={}
 for key,row in model['rows']:
  key=tuple(key)
  if key in result or len(key)>model['order']or any(type(v)is not int or not 0<=v<model['K']for v in key)or len(row)!=model['K']:raise ValueError('Invalid context')
  result[key]=cdf(row)
 if len(model['fallback'])!=model['K']:raise ValueError('Invalid fallback')
 return result,cdf(model['fallback'])


def encode(segments,edges,reps,model,dtype='<i2'):
 if dtype not in ('<i2','<i4'):raise ValueError('Declared signed integer representation required')
 if not segments or sum(len(s)for s in segments)>MAX_SAMPLES or any(len(s)<2 for s in segments):raise ValueError('Invalid segment sizes')
 info=np.iinfo(np.dtype(dtype));segments=[np.asarray(s,dtype=np.int64)for s in segments]
 if any(np.any(s<info.min)or np.any(s>info.max)for s in segments):raise ValueError('Values exceed declared representation')
 reps=[int(x)for x in reps]
 if len(reps)!=model['K']or len(edges)+1!=len(reps):raise ValueError('Quantizer/model mismatch')
 table,fallback=tables(model);coder=Encoder();residual=Bits();ideal=0
 for segment in segments:
  history=[]
  for d in np.diff(segment):
   y=int(np.searchsorted(edges,d,side='right'));key=tuple(history[-model['order']:])if model['order']else ();c=table.get(key,fallback);coder.put(y,c);ideal-=math.log2((c[y+1]-c[y])/TOTAL)
   error=int(d)-reps[y];zig=2*error if error>=0 else -2*error-1;residual.gamma(zig+1);history.append(y)
 symbolbytes=coder.finish();residualbytes=residual.finish()
 raw=b''.join(s.astype(dtype).tobytes()for s in segments)
 header=dict(schema='grh.exact-pcm-code.v1',dtype=dtype,lengths=[len(s)for s in segments],initials=[int(s[0])for s in segments],representatives=reps,model=model,symbol_bytes=len(symbolbytes),residual_bytes=len(residualbytes),raw_crc32=zlib.crc32(raw))
 h=zlib.compress(json.dumps(header,separators=(',',':'),allow_nan=False).encode(),level=9)
 packet=MAGIC+struct.pack('<I',len(h))+h+symbolbytes+residualbytes
 return packet,dict(original_bytes=len(raw),emitted_bytes=len(packet),actual_bpb=8*len(packet)/len(raw),header_bytes=len(MAGIC)+4+len(h),symbol_bytes=len(symbolbytes),residual_bytes=len(residualbytes),ideal_symbol_bits=ideal,graph_side_information='Public directed sample-successor grammar; segment lengths and seeds are included in the header.',representation=dtype,scope='Actual lossless packet for declared integer samples, including frozen model and termination. Not necessarily original container/CSV bytes.')


def decode(packet):
 if len(packet)<10 or packet[:6]!=MAGIC:raise ValueError('Invalid packet magic')
 size=struct.unpack('<I',packet[6:10])[0]
 if size>4_000_000 or size>len(packet)-10:raise ValueError('Invalid header length')
 obj=zlib.decompressobj();rawheader=obj.decompress(packet[10:10+size],4_000_001)
 if len(rawheader)>4_000_000 or not obj.eof:raise ValueError('Header resource budget')
 h=json.loads(rawheader)
 if h.get('schema')!='grh.exact-pcm-code.v1' or h.get('dtype')not in('<i2','<i4'):raise ValueError('Unsupported packet')
 lengths=h['lengths'];initials=h['initials'];reps=h['representatives'];model=h['model']
 if not lengths or len(lengths)!=len(initials)or any(type(n)is not int or n<2 for n in lengths)or sum(lengths)>MAX_SAMPLES:raise ValueError('Invalid sample counts')
 if len(reps)!=model['K']or any(type(x)is not int or abs(x)>2**34 for x in reps):raise ValueError('Invalid representatives')
 sb=h['symbol_bytes'];rb=h['residual_bytes']
 if type(sb)is not int or type(rb)is not int or sb<1 or rb<1 or 10+size+sb+rb!=len(packet):raise ValueError('Invalid payload lengths')
 decoder=Decoder(packet[10+size:10+size+sb]);residual=Reader(packet[10+size+sb:]);table,fallback=tables(model);out=[];info=np.iinfo(np.dtype(h['dtype']))
 for n,first in zip(lengths,initials):
  if type(first)is not int or not info.min<=first<=info.max:raise ValueError('Invalid initial value')
  values=[first];history=[]
  for _ in range(n-1):
   key=tuple(history[-model['order']:])if model['order']else ();y=decoder.get(table.get(key,fallback));zig=residual.gamma()-1;error=zig//2 if zig%2==0 else -(zig+1)//2
   value=values[-1]+reps[y]+error
   if not info.min<=value<=info.max:raise ValueError('Decoded value out of range')
   values.append(value);history.append(y)
  out.append(np.asarray(values,dtype=h['dtype']))
 if zlib.crc32(b''.join(s.tobytes()for s in out))!=h['raw_crc32']:raise ValueError('Decoded checksum mismatch')
 return out
