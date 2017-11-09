import unittest
import main

class TestConverter(unittest.TestCase):
    def test_int_to_hex(self):
        self.assertEqual(main.xor(1,2), 3)
    def test_xor2(self):
        self.assertEqual(main.xor(34545345,123123123456), 123089902529)

    def test_xor3(self):
        self.assertEqual(main.xor(33225, 11), 33218)

if __name__ == "__main__":
    unittest.main()
