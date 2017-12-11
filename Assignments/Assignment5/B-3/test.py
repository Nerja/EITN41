import unittest
import main

class TestConverter(unittest.TestCase):
    def test1(self):
        self.assertEqual("02085bbe5d05d47d76d7", main.der_encode(6610823582647678679))
    def test1(self):
        self.assertEqual("0203010001", main.der_encode(65537))
    def test1(self):
        self.assertEqual("02083669c395b9cf7321", main.der_encode(3920879998437651233))
    def test1(self):
        self.assertEqual("02050096d25da9", main.der_encode(2530368937))
    def test1(self):
        self.assertEqual("0205009bb9007f", main.der_encode(2612592767))
    def test1(self):
        self.assertEqual("020478097601", main.der_encode(2013885953))
    def test1(self):
        self.assertEqual("0204594b4069", main.der_encode(1498103913))
    def test1(self):
        self.assertEqual("020458dcf7b4", main.der_encode(1490876340))

if __name__ == "__main__":
    unittest.main()
