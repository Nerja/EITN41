import random as r
import math as m
import format_converter as fc

import bank
import alice

__author__ = "Marcus Rodan & Niklas Jönsson"


#https://brilliant.org/wiki/extended-euclidean-algorithm/
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return x
    #return gcd, x, y

def compute_rsa_params():
    #n = 20
    #e = 3
    n = 143
    e = 7
    d = 103
    print(d)
    return n, e, d

def main():
    k   = 2

    #RSA
    #n = r.randint(123456,234567)
    n, e, d = compute_rsa_params()

    max_rand_value   = n - 1
    # Client generates 2k (ai, ci, di, ri)
    a_quads, a_x, a_y, a_b, a_id = alice.compute_values(k, max_rand_value, n, e)

    # Save Alice b to bank
    bank_b = a_b

    #SEND ALL B TO BANK
    R = bank.generate_r(k)

    coin_sig = bank.send_data([(i, a_quads[i]) for i in R], bank_b, a_id, n, e, d, R)
    S = alice.extract_S([a_quads[i][3] for i in range(2*k) if i not in R], coin_sig, n)
    #SEND ALL QUADS WITH INDEX R
    print(coin_sig)
    print(S)
if __name__ == "__main__":
    main()
