import random as r
import math as m
import format_converter as fc

from bank import Bank
from alice import Alice
from merchant import Merchant

__author__ = "Marcus Rodan & Niklas Jönsson"

def start_simulation(alice, bank, merchant):

    alice.request_public_rsa(bank)
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

        #Extra Steps(the following is just to increase the probability of
        #detecting some problems in our implementation!
        alice.send_serial_to_merchant(merchant)
        merchant.generate_z()
        merchant.send_z_to_alice(alice)
        alice.send_z_answer(merchant)

        merchant.request_public_rsa(bank)
        if merchant.verify():
            print("Merchant verified coin signature successfully")
            return True
        else:
            print("Merchant FAILED to verify coin signature")
            return False

def main():
    k   = 2
    #RSA

    alice = Alice(k)
    bank = Bank()
    merchant = Merchant()

    return start_simulation(alice, bank, merchant)


if __name__ == "__main__":
    main()
