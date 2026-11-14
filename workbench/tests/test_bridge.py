import http.client
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from contracts import certificate,digest
from lean_export import lean_source,strict_json
from server import asset_path,make_server

class Bridge(unittest.TestCase):
    def test_fixed_templates(self):
        cases=[certificate('heat',{'r':'1/4'}),certificate('rank',{'draws':4095,'exceedances':0}),
          certificate('gain',{'matrix':[['1/4','3/2'],['3/32','1/4']],'weights':['4','1'],'rate':'5/8'}),
          certificate('risk',{'tests':288,'per_test':'1/10000','drift':'1/100','alpha':'1/20'}),
          certificate('mutation',{'matrix':[[0,1],[-1,0]],'seed':['2','5'],'vertex':0})]
        for c in cases:
            s=lean_source(c);self.assertIn('payload_'+digest(c),s)
            self.assertIn(':= by decide',s);self.assertNotIn('native_decide ',s)
            self.assertEqual(strict_json(json.dumps(c)),c)
    def test_parser_rejects_duplicates_and_nonfinite(self):
        for raw in ['{"schema":0,"schema":1}','{"x":NaN}','{"x":Infinity}','x'*65537,'[]']:
            with self.assertRaises((ValueError,TypeError)):strict_json(raw)
        c=certificate('heat',{'r':'1/4'});c['inputs']['r']='1); axiom hacked : False'
        with self.assertRaises(ValueError):lean_source(c)
    def test_static_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);wb=base/'wb';atlas=base/'atlas';wb.mkdir();atlas.mkdir()
            (wb/'index.html').write_text('WB');(atlas/'ok.txt').write_text('ok')
            self.assertEqual(asset_path('/workbench/',wb,atlas),wb/'index.html')
            self.assertEqual(asset_path('/ok.txt',wb,atlas),atlas/'ok.txt')
            for path in ['/workbench/../../outside','/workbench/%2e%2e/../outside','/workbench/a%5cb','/workbench/%00']:
                with self.assertRaises((ValueError,FileNotFoundError)):asset_path(path,wb,atlas)
            (wb/'escape').symlink_to(base)
            with self.assertRaises(FileNotFoundError):asset_path('/workbench/escape/atlas/ok.txt',wb,atlas)
    def test_http_boundaries(self):
        s=make_server(0);t=threading.Thread(target=s.serve_forever,daemon=True);t.start()
        port=s.server_port
        def request(method,path,body=None,headers=None):
            c=http.client.HTTPConnection('127.0.0.1',port,timeout=3)
            c.request(method,path,body,headers or {});r=c.getresponse();answer=(r.status,json.loads(r.read()));c.close();return answer
        try:
            status,data=request('GET','/api/status');self.assertEqual(status,200);self.assertFalse(data['lean_configured'])
            self.assertEqual(request('GET','/api/status',headers={'Host':'evil.example'})[0],403)
            body=json.dumps(certificate('heat',{'r':'1/4'}));h={'Content-Type':'application/json'}
            self.assertEqual(request('POST','/api/verify',body,h)[0],503)
            self.assertEqual(request('POST','/api/source',body,h)[0],200)
            self.assertEqual(request('POST','/api/source',body,dict(h,Origin='https://evil.example'))[0],403)
            self.assertEqual(request('POST','/api/source',body,{'Content-Type':'text/plain'})[0],415)
            self.assertEqual(request('POST','/api/source','x'*65537,h)[0],400)
            self.assertEqual(request('GET','/.git/config')[0],404)
        finally:s.shutdown();s.server_close();t.join()

if __name__=='__main__':unittest.main(verbosity=2)
