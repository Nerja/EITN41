import unittest
import main

class TestConverter(unittest.TestCase):
    def test_int_to_hex(self):
        self.assertEqual(main.merkle_root('example.txt'), '6f51120bc17e224de27d3d27b32f05d0a5ffb376')
    def test_part_2(self):
        self.assertEqual(main.part2('smallexample'), 'R8d3f164890509c6510cc9bc975cb978f0b872fbb1781a6ea9a22f67e8a09cb54bbdc6d99d0efc081')
    def test_part_2_case_2(self):
        self.assertEqual(main.part2('leaf.txt'), 'Rf4582a5fe4b346a54a44fbebba114f6fcef35839f4f4cd35f5a3c801fb7e701c834bff87d2b3adaa')
if __name__ == "__main__":
    unittest.main()
