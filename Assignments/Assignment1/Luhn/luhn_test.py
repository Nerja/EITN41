import unittest
import format_converter
import assignment1

class TestConverter(unittest.TestCase):
    def test_int_to_hex(self):
        credit_cards = ["1277421285754109", "5866044108627571", "7473986953606632", "4026467645830632", "2033092648604969"]
        cens_cards = []
        missing = []
        for cnbr in credit_cards:
            for i in range(0, 16):
                missing += [cnbr[i]]
                cens_cards += [cnbr[:i] + 'X' + cnbr[(i+1):]]
        found_missing = assignment1.solve(cens_cards)
        self.assertEqual(list(found_missing), missing)

if __name__ == "__main__":
    unittest.main()
