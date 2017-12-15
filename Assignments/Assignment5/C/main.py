__author__ = "Niklas Jönsson & Marcus Rodan"

import hashlib
import format_converter as fc
import util

def id_val(pub_id, m):
    a = hashlib.sha1(bytearray(pub_id.encode('utf8'))).digest()
    while util.jacobi(fc.bytearray_to_int(a) % m, m) != 1:
        a = hashlib.sha1(a).digest()
    return fc.bytearray_to_int(a) % m

def PKG(a, m, p, q):
    return pow(a, (m + 5 - (p + q)) // 8, m)

def decrypt(bits, r, m):
    return int("".join(str("1" if util.jacobi(int(s, 16) + 2*r, m) == 1 else "0") for s in bits), 2)

def run_instance(pub_id, p, q, bits):
    p = int(p, 16)
    q = int(q, 16)
    m = p * q
    a = id_val(pub_id, m)
    r = PKG(a, m, p, q)
    d_bits = decrypt(bits, r, m)

    print("Public id value = {}".format(fc.int2hex(a)))
    print("Private key: {}".format(fc.int2hex(r)))
    print("Decrypted bits: {}".format(d_bits))
    return fc.int2hex(r), d_bits

if __name__ == "__main__":
    pub_id = "walterwhite@crypto.sec"
    p = "9240633d434a8b71a013b5b00513323f"
    q = "f870cfcd47e6d5a0598fc1eb7e999d1b"
    bits = [
        "83c297bfb0028bd3901ac5aaa88e9f449af50f12c2f43a5f61d9765e7beb2469",
        "519fac1f8ac05fd12f0cbd7aa46793210988a470d27385f6ae10518a0c6f2dd6",
        "2bda0d9c8c78cb5ec2f8c038671ddffc1a96b5d42004104c551e8390fbf4c42e"
    ]
    run_instance(pub_id, p, q, bits)
