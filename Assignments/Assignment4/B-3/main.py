__author__ = "Niklas Jönsson & Marcus Rodan"

import sys
import math
import format_converter as fc
import hashlib
import binascii

def MGF1(mgfSeed, maskLen):
    if maskLen > 2 ** 32:
        print ("maskLen too large")
        sys.exit()

    hLen = 20 #sha1 outputs 20 bytes
    T = bytearray()

    #0 to \ceil (maskLen / hLen) - 1
    #skip -1 because range does not include endpoint
    for counter in range(math.ceil(maskLen / hLen)):
        C = I2OSP (counter, 4)
        #T = T || Hash(mgfSeed || C)
        #T =
        mgfSeed_bytearray = fc.hex_to_bytearray(mgfSeed)
        T = T + fc.hex_to_bytearray(hashlib.sha1(mgfSeed_bytearray + C).hexdigest())

    #Output the leading maskLen octets of T as the octet string mask
    return str(binascii.hexlify(T[:maskLen]))[2:][:-1]

def I2OSP(x, xLen):
    #1.  If x >= 256^xLen, output "integer too large" and stop.
    if x >= 256 ** xLen:
        print("integer too large")
        sys.exit()

    xs = []
    for i in range(xLen):
        xs      = [x % 256] + xs
        x       //= 256
    return bytearray(xs)
