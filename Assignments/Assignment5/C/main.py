__author__ = "Niklas Jönsson & Marcus Rodan"

import hashlib
import format_converter as fc
import util

def legendre_symbol(a, p):
    if a == 0:
        return 0



    #-1 if a is a non-residue
    #1 if a is a residue
    #residue = if there exists a b such that a = b ** 2 mod p

def id_val(pub_id, m):
    a = hashlib.sha1(pub_id).hexdigest()
    while util.jacobi(int(a, 16) % m, m) != 1:
        a = hashlib.sha1(bytearray(a.encode('utf8'))).hexdigest()
    return int(a, 16)

def PKG(a, m, p, q):
    exp = int((m + 5 - (p + q)) / 8)
    return (a ** exp) % m

def decrypt():
    return 0

def run_instance(pub_id, p, q, bits):
    pub_id = bytearray(pub_id.encode('utf8'))
    p = int(p, 16)
    q = int(q, 16)
    m = p * q
    a = id_val(pub_id, m)
    print(format(a, 'x'))
    r = PKG(a, m, p, q)
    print(r)
    return r
'''
The program should output the user’s private key in (as a hexadecimal string)
as well as the decrypted bits, written as a number (in base 10).
'''

if __name__ == "__main__":
    pub_id = "walterwhite@crypto.sec"
    p = "9240633d434a8b71a013b5b00513323f"
    q = "f870cfcd47e6d5a0598fc1eb7e999d1b"
    bits = "83c297bfb0028bd3901ac5aaa88e9f449af50f12c2f43a5f61d9765e7beb2469519fac1f8ac05fd12f0cbd7aa46793210988a470d27385f6ae10518a0c6f2dd62bda0d9c8c78cb5ec2f8c038671ddffc1a96b5d42004104c551e8390fbf4c42e"
    run_instance(pub_id, p, q, bits)
