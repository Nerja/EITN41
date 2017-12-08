import unittest
import main

class TestConverter(unittest.TestCase):
    def test_int_to_hex(self):
        self.assertEqual("18a65e36189833d99e55a68dedda1cce13a494c947817d25dc80d9b4586a", main.MGF1("0123456789abcdef", 30))
    def test_i2osp(self):
        self.assertEqual([0, 0, 5, 57], list(main.I2OSP(1337, 4)))
if __name__ == "__main__":
    unittest.main()
