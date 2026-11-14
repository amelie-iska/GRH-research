"""Regression tests for false acceptance of malformed graph/memory witnesses."""
import copy
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from analogy import Memory, retrieve, verify_mapping, verify_deduction


def witness():
    return dict(source_nodes={'a':'state', 'b':'state'},
                target_nodes={'x':'state', 'y':'state', 'z':'state'},
                source_edges={'s':('a','b','advance')},
                target_edges={'e1':('x','y','step'), 'e2':('y','z','step')},
                node_map={'a':'x', 'b':'z'}, paths={'s':['e1','e2']},
                relation_words={'advance':{('step','step')}})


class AnalogyBoundaries(unittest.TestCase):
    def test_undeclared_interior_vertex_rejected(self):
        w=witness(); del w['target_nodes']['y']
        with self.assertRaisesRegex(ValueError, 'declared vertex'):
            verify_mapping(**w)
    def test_unknown_unused_edge_endpoint_rejected(self):
        w=witness(); w['target_edges']['unused']=('unknown','z','step')
        with self.assertRaisesRegex(ValueError, 'declared vertex'):
            verify_mapping(**w)
    def test_malformed_source_edge_rejected(self):
        for edge in [('unknown','b','advance'), ('a','b'), 'abc', ('a','b','')]:
            w=witness(); w['source_edges']['s']=edge
            with self.subTest(edge=edge), self.assertRaises(ValueError):
                verify_mapping(**w)
    def test_invalid_relation_words_rejected(self):
        for words in ['step', {('step',)}, {()}, {('step',False)}, [['step','step']]]:
            w=witness(); w['relation_words']['advance']=words
            with self.subTest(words=words), self.assertRaises(ValueError):
                verify_mapping(**w)
    def test_declared_orders(self):
        w=witness(); w.update(source_order={'a':0,'b':1}, target_order={'x':0,'y':1,'z':2})
        self.assertTrue(verify_mapping(**w))
        w['target_order']['y']=3
        with self.assertRaisesRegex(ValueError, 'strictly increase'):
            verify_mapping(**w)
    def test_order_witness_required_on_both_sides(self):
        w=witness(); w['source_order']={'a':0,'b':1}
        with self.assertRaises(ValueError): verify_mapping(**w)
    def test_invalid_order_domains(self):
        for order in [{'x':0,'z':2}, {'x':0,'y':True,'z':2}, {'x':0,'y':1.0,'z':2}]:
            w=witness(); w.update(source_order={'a':0,'b':1},target_order=order)
            with self.subTest(order=order), self.assertRaises(ValueError): verify_mapping(**w)
    def test_empty_graph_is_explicitly_vacuous(self):
        self.assertTrue(verify_mapping({}, {}, {}, {}, {}, {}, {}))
    def test_alias_and_branch_failures(self):
        for field,value in [('node_map',{'a':'x','b':'x'}),('paths',{}),('paths',{'s':['e2','e1']}),('paths',{'s':['not-an-edge']})]:
            w=witness();w[field]=value
            with self.subTest(field=field,value=value),self.assertRaises(ValueError):verify_mapping(**w)
    def test_mapping_does_not_mutate_inputs(self):
        w=witness();old=copy.deepcopy(w);verify_mapping(**w);self.assertEqual(w,old)
    def test_missing_memory_groups_rejected(self):
        bank=[Memory('m',frozenset(),'train','enc',(1.,))]
        with self.assertRaisesRegex(ValueError, 'leakage groups'):
            retrieve((1.,),frozenset({'test'}),'enc',bank)
    def test_duplicate_identity_rejected_before_ranking(self):
        bank=[Memory('m',frozenset({'a'}),'train','enc',(0.,)),Memory('m',frozenset({'b'}),'train','enc',(1.,))]
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            retrieve((0.,),frozenset({'test'}),'enc',bank)
    def test_unknown_is_not_a_negative(self):
        bank=[Memory('m',frozenset({'shared'}),'train','enc',(0.,))]
        self.assertEqual(retrieve((0.,),frozenset({'shared'}),'enc',bank),[])
        self.assertEqual(retrieve((0.,),frozenset({'test'}),'enc',[]),[])
    def test_nonfinite_and_overflow_rejected(self):
        for key in [(float('nan'),), (float('inf'),), (True,), (10**10000,)]:
            with self.subTest(kind=type(key[0]).__name__),self.assertRaises(ValueError):
                retrieve(key,frozenset({'test'}),'enc',[])
        bank=[Memory('m',frozenset({'train'}),'train','enc',(-1e308,))]
        with self.assertRaisesRegex(ValueError, 'arithmetic range'):
            retrieve((1e308,),frozenset({'test'}),'enc',bank)
    def test_stale_or_nontraining_records_rejected(self):
        for split,encoder in [('validation','enc'),('test','enc'),('train','stale')]:
            bank=[Memory('m',frozenset({'train'}),split,encoder,(0.,))]
            with self.subTest(split=split,encoder=encoder),self.assertRaises(ValueError):
                retrieve((0.,),frozenset({'test'}),'enc',bank)
    def test_deduction_rejects_string_premises(self):
        with self.assertRaisesRegex(ValueError, 'explicit set'):
            verify_deduction(frozenset({'P'}),{'bad':('P','Q')},[('bad','Q')])
    def test_deduction_is_sequential(self):
        rules={'first':({'P'},'Q'),'second':({'Q'},'R')}
        self.assertEqual(verify_deduction(frozenset({'P'}),rules,[('first','Q'),('second','R')]),frozenset({'P','Q','R'}))
        with self.assertRaises(ValueError):
            verify_deduction(frozenset({'P'}),rules,[('second','R'),('first','Q')])
    def test_deduction_rejects_malformed_and_false_claims(self):
        for steps in ['PQ',[('rule','wrong')],[('rule',)],[(True,'Q')]]:
            with self.subTest(steps=steps),self.assertRaises(ValueError):
                verify_deduction(frozenset({'P'}),{'rule':({'P'},'Q')},steps)
    def test_explicit_empty_premise_rule(self):
        self.assertEqual(verify_deduction(frozenset(),{'given':(set(),'P')},[('given','P')]),frozenset({'P'}))
    def test_resource_limits(self):
        with self.assertRaises(ValueError): retrieve((0.,)*1025,frozenset({'test'}),'enc',[])
        for k in [True,0,257]:
            with self.subTest(k=k),self.assertRaises(ValueError):retrieve((0.,),frozenset({'test'}),'enc',[],k)
        w=witness();w['paths']['s']=['e1']*4097
        with self.assertRaises(ValueError):verify_mapping(**w)


if __name__=='__main__': unittest.main(verbosity=2)
