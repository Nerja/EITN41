import unittest
import main

class TestDC(unittest.TestCase):
    def test1(self):
        self.assertEqual(main.compute(['0C73', '80C1', 'A2A9', '92F5', '9B57', 0]), '8CB2BCEE')
    def test2(self):
        self.assertEqual(main.compute(['27C2', '0879', '35F6', '1A4D', '27BC', 1]), '0807')

if __name__ == "__main__":
    unittest.main()
