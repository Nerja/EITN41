import unittest
import main

class TestConverter(unittest.TestCase):
    def test1(self):
        self.assertEqual("02085bbe5d05d47d76d7", main.der_encode(6610823582647678679))
    def test2(self):
        self.assertEqual("0203010001", main.der_encode(65537))
    def test3(self):
        self.assertEqual("02083669c395b9cf7321", main.der_encode(3920879998437651233))
    def test4(self):
        self.assertEqual("02050096d25da9", main.der_encode(2530368937))
    def test5(self):
        self.assertEqual("0205009bb9007f", main.der_encode(2612592767))
    def test6(self):
        self.assertEqual("020478097601", main.der_encode(2013885953))
    def test7(self):
        self.assertEqual("0204594b4069", main.der_encode(1498103913))
    def test8(self):
        self.assertEqual("020458dcf7b4", main.der_encode(1490876340))
    def test9(self):
        p = 2530368937
        q = 2612592767
        e = 65537
        self.assertEqual("MDwCAQACCFu+XQXUfXbXAgMBAAECCDZpw5W5z3MhAgUAltJdqQIFAJu5AH8CBHgJdgECBFlLQGkCBFjc97Q=", main.encode_key(p, q, e))
if __name__ == "__main__":
    unittest.main()
