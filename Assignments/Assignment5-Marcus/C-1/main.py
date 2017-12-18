import utils
import format_converter as fc
import hashlib

__author__ = "Marcus Rodan & Niklas Jönsson"

def ha(x):
    return fc.hex_to_int(fc.hash_int(x))

def compute_a_value(id, M):
    a = hashlib.sha1(id.encode('utf-8')).digest()
    while utils.jacobi(fc.bytearray_to_int(a), M) != 1:
        a = hashlib.sha1(a).digest()
    return str(fc.bytearray_to_hex(a))[2:][:-1]

def assign_key(id, p, q):
    p = fc.hex_to_int(p)
    q = fc.hex_to_int(q)

    M = p * q
    a = compute_a_value(id, M)

    r = pow(int(a, 16), (M+5-(p + q))//8, M)
    return fc.int_to_hex(r)[2:]

def decrypt(M, priv_alice, msg):
    r = int(priv_alice, 16)
    return int("".join(str("1" if utils.jacobi(int(s, 16) + 2*r, M) == 1 else "0") for s in msg), 2)

if __name__ == "__main__":
    p   = "9240633d434a8b71a013b5b00513323f"
    q   = "f870cfcd47e6d5a0598fc1eb7e999d1b"
    id  = "grace@crypto.sec"

    private_alice = assign_key(id, p, q)
    print("Private key={}".format(private_alice))

    msg = open('msg').read().rsplit()
    M = int(p, 16) * int(q, 16)
    decrypted_msg = decrypt(M, private_alice, msg)
    print("Decrypted message = {}".format(decrypted_msg))
