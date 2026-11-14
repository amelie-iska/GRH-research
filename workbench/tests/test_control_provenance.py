import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'experiments'))
from acquire_controls import selected_transcripts,SELECTION

class ControlProvenance(unittest.TestCase):
 def test_chapter_not_speaker(self):
  with self.assertRaises(ValueError):selected_transcripts({'s-other.trans.txt':'s-other-1 WRONG CHAPTER'},['s-c-1'])
 def test_complete_matching(self):
  r=selected_transcripts({'a':'s-c-1 FIRST\ns-c-2 SECOND'},['s-c-2','s-c-1']);self.assertEqual([x['utterance_id']for x in r],['s-c-1','s-c-2'])
 def test_conflict(self):
  with self.assertRaises(ValueError):selected_transcripts({'a':'s-c-1 ONE','b':'s-c-1 TWO'},['s-c-1'])
 def test_fixed_selection(self):self.assertEqual(sum(len(v[1])for v in SELECTION.values()),18)

if __name__=='__main__':unittest.main(verbosity=2)
