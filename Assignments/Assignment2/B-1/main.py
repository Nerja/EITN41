__author__ = "Niklas Jönsson & Marcus Rodan"

from sys import argv
import dc
import format_converter as fc

import binascii

def compute(argv):
    SA, DA, SB, DB, M = [fc.hex_to_binary(arg) for arg in argv[:5]]
    b = argv[5]

    output = ""
    for i in range(len(SA)):
        output += dc.compute_for_one_bit(SA[i], DA[i], SB[i], DB[i], M[i], b)

    return fc.binary_to_hex(output).zfill(4)



if __name__ == "__main__":
    #main(argv[1:])
    print(compute(['0C73', '80C1', 'A2A9', '92F5', '9B57', 0])) #Expected output 8CB2BCEE
    print(compute(['27C2', '0879', '35F6', '1A4D', '27BC', 1]))
    #dc(['27C2', '0879', '35F6', '1A4D', '27BC', 1]) #Expected output 0807
