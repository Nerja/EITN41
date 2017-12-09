import unittest
import main

class TestConverter(unittest.TestCase):
    def test_instructions(self):
        self.assertEqual('0b29099972244f2569bb5f6f4e34760cc7bf4645', main.run_instance('1337'))

    def test_testquiz(self):
        self.assertEqual('0bfb4e0982b75971f83321ec5b2119e068daef53', main.run_instance('0123456789abcdef'))

    def test_livequiz(self):
        self.assertEqual('8a7742ba75228d2729c1b3908199b36189316e8e', main.run_instance('9ef25a019a549b8413392a05a401c4a1d8d00f00'))

if __name__ == "__main__":
    unittest.main()
