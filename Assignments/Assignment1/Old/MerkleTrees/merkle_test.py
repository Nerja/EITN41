import unittest
import main

class TestConverter(unittest.TestCase):
    def test_int_to_hex(self):
        self.assertEqual(main.merkle_root(), '6f51120bc17e224de27d3d27b32f05d0a5ffb376')
    def test_part_2(self):
        self.assertEqual(main.part2('smallexample'), 'R8d3f164890509c6510cc9bc975cb978f0b872fbb1781a6ea9a22f67e8a09cb54bbdc6d99d0efc081')

if __name__ == "__main__":
    unittest.main()
