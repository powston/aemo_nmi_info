import unittest
from aemo_nmi_lookup import nmi_lookup


class TestNmiLookup(unittest.TestCase):

    def test_valid_nmi(self): 
        tests = [("NGGG000001", "ACT", "ACTEWP"),
                 ("4001000001", "NSW", "CNRGYP"),
                 ("QBAA000001", "QLD", "ENERGEXP"),
                 ("8590200001", "TAS", "AURORAP"),
                 ("9000000001", "MISC", "AEMO Reserved block 2")]
        
        for nmi, state, distributor in tests:
            result = nmi_lookup(nmi)
            self.assertEqual(result, (state, distributor))

    def test_invalid_nmi_length(self):
        nmi = '12345'
        result = nmi_lookup(nmi)
        self.assertEqual(result, (None, None))

    def test_no_match_found(self):
        nmi = 'XYZ1234567'
        result = nmi_lookup(nmi)
        self.assertEqual(result, (None, None))
