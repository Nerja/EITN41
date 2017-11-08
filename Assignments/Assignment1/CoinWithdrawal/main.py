import random as r
import math as m
import format_converter as fc

import bank
import alice

__author__ = "Marcus Rodan & Niklas Jönsson"

def compute_rsa_params():
    #n = 143
    #e = 7
    #d = 103
    n = 493
    e = 5
    d = 269
    return n, e, d

def main():
    k   = 2

    #RSA
    n, e, d = compute_rsa_params()

    # Client generates 2k (ai, ci, di, ri)
    a_quads, a_x, a_y, a_b, a_id = alice.compute_values(k, n, e)

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
