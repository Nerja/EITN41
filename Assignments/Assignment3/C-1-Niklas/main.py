__author__ = "Niklas Jönsson & Marcus Rodan"

import reader as r
import math

def compute_votes(p, q, g, input):
    n = p * q
    prod = 1
    for vote in r.read_file(input):
        prod = prod * int(vote)
    prod = prod % (n ** 2)
    lmbda = lambd(p, q)
    m = mu(g, lmbda, n)

    return int(L((prod ** lmbda) % (n ** 2), n) * mu(g, lmbda, n) % n - n)
def mu(g, l, n):
    return modinv(L((g ** l) % (n ** 2), n), n) % n

def L(x, n):
    return (x - 1) / n

def lambd(p, q):
    return ((p -1) * (q - 1)) // math.gcd((p - 1), (q - 1))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def main():
    p = 1117
    q = 1471
    g = 652534095028
    infile = "input12.txt"
    print("Result: {}".format(compute_votes(p, q, g, infile)))


if __name__ == "__main__":
    main()
