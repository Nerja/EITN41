import unittest
import main
import format_converter as fc


class TestC(unittest.TestCase):
    def test1(self):
        pub_id = "walterwhite@crypto.sec"
        p = int("9240633d434a8b71a013b5b00513323f", 16)
        q = int("f870cfcd47e6d5a0598fc1eb7e999d1b", 16)
        a = fc.int2hex(main.id_val(pub_id, p * q))
        self.assertEqual("25a4d152bf555e0f61fb94ac4ee60962decbbe99", a)

    def test2(self):
        p = int("9240633d434a8b71a013b5b00513323f", 16)
        q = int("f870cfcd47e6d5a0598fc1eb7e999d1b", 16)
        m = p * q
        a = main.id_val("walterwhite@crypto.sec", m)
        r = fc.int2hex(main.PKG(a, m, p, q))
        self.assertEqual("814a8c2282ca8f4d0f2b2b72dfeeee6e5e3d8f438c039bdb5d059550739fdcec", r)

if __name__ == "__main__":
    unittest.main()
