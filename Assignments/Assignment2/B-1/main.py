__author__ = "Niklas Jönsson & Marcus Rodan"

import sys
import dc
import format_converter as fc

import binascii

def compute(argv):
    SA, SB, DA, DB, M = [fc.hex_to_binary(arg) for arg in argv[:5]]
    b = int(argv[5])

    output = ""
    anon_msg = ""
    for i in range(len(SA)):
        output += dc.compute_broadcast(SA[i], SB[i], M[i], b)

    if not b:
        for i in range(len(output)):
            anon_msg += dc.compute_anon_msg(output[i], DA[i], DB[i])
        anon_msg = fc.binary_to_hex(anon_msg).zfill(4)

    return (fc.binary_to_hex(output).zfill(4) + anon_msg).upper()

if __name__ == "__main__":
    if(len(sys.argv) != 7):
        print("Arguments should be SA, SB, DA, DB, M, b")
        sys.exit(2)

    print("Result: {}".format(compute(sys.argv[1:])))
