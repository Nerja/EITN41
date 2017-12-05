import unittest
import main

class TestConverter(unittest.TestCase):
    def test_int_to_hex(self):
        X_14 = main.simulate(10, 100)
        X_14_bind = X_14[0]
        X_14_conc = X_14[1]
        self.assertEqual(True, abs(X_14_bind - 0.0047378863875207665) < 0.01)
        self.assertEqual(True, abs(X_14_conc - 0) < 0.00001)

if __name__ == "__main__":
    unittest.main()
