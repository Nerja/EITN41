import random as r
import math as m
import format_converter as fc

from bank import Bank
from alice import Alice
from merchant import Merchant

__author__ = "Marcus Rodan & Niklas Jönsson"

def start_simulation(alice, bank, merchant):
    alice.generate_2k()
    alice.compute_bi()
    alice.send_b_to_bank(bank)

    bank.generate_R()
    bank.request_quads_from_alice(alice)
    valid = bank.verify_quads()
    if not valid :
        print("verification of quads failed")
    else:
        bank.compute_blind_signature()
        bank.send_blind_signature(alice)

        alice.calculate_serial()
        alice.debug_print()

        alice.send_serial_to_merchant(merchant)
        merchant.generate_z()
        merchant.send_z_to_alice(alice)
        alice.send_z_answer(merchant)

        if merchant.verify():
            print("Merchant verified coin signature successfully")
        else:
            print("Merchant FAILED to verify coin signature")




    #a_quads, a_x, a_y, a_b, a_id = alice.compute_values(k, n, e)

    # Save Alice b to bank
    #bank_b = a_b

    #SEND ALL B TO BANK
    #R = bank.generate_r(k)

    #coin_sig = bank.send_data([(i, a_quads[i]) for i in R], bank_b, a_id, n, e, d, R)
    #S = alice.extract_S([a_quads[i][3] for i in range(2*k) if i not in R], coin_sig, n)
    #SEND ALL QUADS WITH INDEX R
    #print(coin_sig)
    #print(S)

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
    #k = hälften av antalet quadtruples som ska skapas
    #n = värdet som man ska köra mod på överallt
    #e = publika exponenten till bankens RSA nyckel
    alice = Alice(k, n, e)
    bank = Bank(n, e, d)
    merchant = Merchant(n, e)

    start_simulation(alice, bank, merchant)


if __name__ == "__main__":
    main()
