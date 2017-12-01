import unittest
import main

class TestConverter(unittest.TestCase):
    def test_int_to_hex(self):
        X_14 = main.simulate(14, 20)
        X_14_bind = X_14[0]
        X_14_conc = X_14[1]
        self.assertEqual(True, abs(X_14_bind - 0.0001277923583984375) < 0.0001)
        self.assertEqual(True, abs(X_14_conc - 7.62939453125e-06) < 0.00001)

if __name__ == "__main__":
    unittest.main()
