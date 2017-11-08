import random as r
import math as m
import format_converter as fc
import numpy

import bank
import alice
import common
import merchant

__author__ = "Marcus Rodan & Niklas Jönsson"

def compute_rsa_params():
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
    quads_not_in_R = [a_quads[i][3] for i in range(2*k) if i not in R]
    a_x_not_in_R = [a_x[i] for i in range(2*k) if i not in R]
    a_y_not_in_R = [a_y[i] for i in range(2*k) if i not in R]
    S = alice.extract_S(quads_not_in_R, coin_sig, n)
    #SEND ALL QUADS WITH INDEX R

    print("Blind coin signature:\t{}".format(coin_sig))
    print("Coin signature:\t\t{}".format(S))

    z = merchant.generate_z(k)
    merch_ans = alice.answer_merchant(z, a_x_not_in_R, a_y_not_in_R, [a_quads[i] for i in range(2*k) if i not in R], a_id)
    ok = merchant.verify(S, merch_ans, z, n, e, a_id)
    if(not ok):
        print("Something is really really bad...")

if __name__ == "__main__":
    main()
