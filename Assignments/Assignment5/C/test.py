import unittest
import main

class TestConverter(unittest.TestCase):
    def test1(self):
        self.assertEqual("25a4d152bf555e0f61fb94ac4ee60962decbbe99", main.id_val("walterwhite@crypto.sec", 100))

if __name__ == "__main__":
    unittest.main()
