import unittest
import format_converter

class TestConverter(unittest.TestCase):
    def test_int_to_hex(self):
        self.assertEqual(format_converter.int_to_hex(500), "0x000001f4")

    def test_hex_to_int(self):
        self.assertEqual(format_converter.hex_to_int("000001f4"), 500)

    def test_bytearray_to_int(self):
        self.assertEqual(format_converter.bytearray_to_int([0, 0, 1, 244]), 500)

    def test_int_to_bytearray(self):
        self.assertEqual(list(format_converter.int_to_bytearray(500, 4)), [0, 0, 1, 244])

    def test_bytearray_to_hex(self):
        self.assertEqual(format_converter.bytearray_to_hex([0, 0, 1, 244]), b'000001f4')

    def test_hex_to_bytearray(self):
        self.assertEqual(list(format_converter.hex_to_bytearray("000001f4")), [0, 0, 1, 244])

    def test_hash_int(self):
        self.assertEqual(format_converter.hash_int(500, 4), 'c6c5da207269aa4a59743ded27105b13bc8dd384')

    def test_hash_ex2(self):
        nbr         = format_converter.hex_to_int("fedcba9876543210")
        hash_hex    = format_converter.hash_int(nbr, 8)
        hash_int    = format_converter.hex_to_int(hash_hex)
        self.assertEqual(hash_int, 946229717077375328329532411653585908948565005770)

if __name__ == "__main__":
    unittest.main()
