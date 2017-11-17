import unittest
import main

class TestDC(unittest.TestCase):
    def test1(self):
        self.assertEqual(main.compute(['0C73', '80C1', 'A2A9', '92F5', '9B57', 0]), '8CB2BCEE')
    def test2(self):
        self.assertEqual(main.compute(['27C2', '0879', '35F6', '1A4D', '27BC', 1]), '0807')
    def test3(self):
        self.assertEqual(main.compute(['D75C', 'EE87', 'C568', 'FCB3', '4674', 1]), '7FAF')
    def test4(self):
        self.assertEqual(main.compute(['75F5', 'B1AC', '67C1', 'A398', '00BC', 0]), 'C4590000')
if __name__ == "__main__":
    unittest.main()
