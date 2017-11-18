import unittest
import main

class TestConverter(unittest.TestCase):
    def test_int_to_hex(self):
        for i in range(10000):
            self.assertEqual(True, main.main())

if __name__ == "__main__":
    unittest.main()
