import unittest
import main
import random

class TestConverter(unittest.TestCase):
    def test_idvala(self):
        p   = int("9240633d434a8b71a013b5b00513323f", 16)
        q   = int("f870cfcd47e6d5a0598fc1eb7e999d1b", 16)
        id  = "walterwhite@crypto.sec"
        self.assertEqual("25a4d152bf555e0f61fb94ac4ee60962decbbe99", main.compute_a_value(id, p*q))

    def test_key(self):
        p   = "9240633d434a8b71a013b5b00513323f"
        q   = "f870cfcd47e6d5a0598fc1eb7e999d1b"
        id  = "walterwhite@crypto.sec"
        self.assertEqual("814a8c2282ca8f4d0f2b2b72dfeeee6e5e3d8f438c039bdb5d059550739fdcec", main.assign_key(id, p, q))

    def test_decrypted(self):
        msg = ['83c297bfb0028bd3901ac5aaa88e9f449af50f12c2f43a5f61d9765e7beb2469',
        '519fac1f8ac05fd12f0cbd7aa46793210988a470d27385f6ae10518a0c6f2dd6',
        '2bda0d9c8c78cb5ec2f8c038671ddffc1a96b5d42004104c551e8390fbf4c42e']
        key = "814a8c2282ca8f4d0f2b2b72dfeeee6e5e3d8f438c039bdb5d059550739fdcec"
        p   = "9240633d434a8b71a013b5b00513323f"
        q   = "f870cfcd47e6d5a0598fc1eb7e999d1b"
        self.assertEqual(6, main.decrypt(int(p, 16) * int(q, 16), key, msg))

if __name__ == "__main__":
    unittest.main()
