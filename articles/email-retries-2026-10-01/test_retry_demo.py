import tempfile
import unittest
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
from retry_demo import Provider,KeyConflict

class RetryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.path=Path(self.temp.name)/'provider.sqlite'
        self.provider=Provider(self.path)
        self.payload={'recipient':'reader@example.test','subject':'Order 42 received'}
    def tearDown(self): self.temp.cleanup()
    def test_naive_retry_creates_two_acceptances(self):
        with self.assertRaises(TimeoutError): self.provider.accept(self.payload,lose_reply=True)
        self.provider.accept(self.payload)
        self.assertEqual(self.provider.count(),2)
    def test_same_key_survives_lost_reply(self):
        with self.assertRaises(TimeoutError): self.provider.accept(self.payload,key='receipt/42',lose_reply=True)
        first=self.provider.accept(self.payload,key='receipt/42')
        self.assertEqual(first,self.provider.accept(self.payload,key='receipt/42'))
        self.assertEqual(self.provider.count(),1)
    def test_new_key_on_retry_duplicates(self):
        with self.assertRaises(TimeoutError): self.provider.accept(self.payload,key='attempt/1',lose_reply=True)
        self.provider.accept(self.payload,key='attempt/2')
        self.assertEqual(self.provider.count(),2)
    def test_changed_payload_conflicts(self):
        self.provider.accept(self.payload,key='receipt/42')
        with self.assertRaises(KeyConflict): self.provider.accept({**self.payload,'subject':'Changed'},key='receipt/42')
        self.assertEqual(self.provider.count(),1)
    def test_precommit_failure_rolls_back_both_records(self):
        with self.assertRaises(RuntimeError): self.provider.accept(self.payload,key='receipt/42',fail_before_commit=True)
        self.assertEqual(self.provider.count(),0)
        self.provider.accept(self.payload,key='receipt/42')
        self.assertEqual(self.provider.count(),1)
    def test_reopen_provider_replays_persisted_record(self):
        first=self.provider.accept(self.payload,key='receipt/42')
        second=Provider(self.path).accept(self.payload,key='receipt/42')
        self.assertEqual(first,second)
        self.assertEqual(self.provider.count(),1)
    def test_concurrent_same_key_has_one_acceptance(self):
        barrier=Barrier(12)
        def send(_):
            barrier.wait()
            return self.provider.accept(self.payload,key='receipt/42')
        with ThreadPoolExecutor(max_workers=12) as pool: responses=list(pool.map(send,range(12)))
        self.assertEqual(len(set(responses)),1)
        self.assertEqual(self.provider.count(),1)
    def test_distinct_business_actions_remain_distinct(self):
        self.provider.accept(self.payload,key='receipt/42')
        self.provider.accept(self.payload,key='receipt/43')
        self.assertEqual(self.provider.count(),2)
    def test_json_key_order_does_not_create_conflict(self):
        a=self.provider.accept(self.payload,key='receipt/42')
        b=self.provider.accept(dict(reversed(list(self.payload.items()))),key='receipt/42')
        self.assertEqual(a,b)

if __name__=='__main__': unittest.main(verbosity=2)
