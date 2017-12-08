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

def OAEP_encode(M, seed, L=""):
    k = 128 #Enligt uppgiften 1024 bit rsa. K är längd i octets/bytes, dvs 1024/8 = 128
    lHash = hashlib.sha1(L.encode('utf-8')).hexdigest()
    hLen = int(len(lHash) / 2)
    mLen = int(len(M) / 2) #length in octets is / 2

    if len(L) / 2  > 2**61 - 1:
        print("label too long")
        sys.exit()
    if mLen > k - (2 * hLen) - 2:
        print("message too long")
        sys.exit()

    PS =  "00" * (k - mLen - (2 * hLen) - 2)
    DB = lHash + PS + fc.int2hex(1) + M
    dbMask = MGF1(seed, k - hLen - 1)
    maskedDB = '{:x}'.format(int(DB, 16) ^ int(dbMask, 16)).zfill(hLen * 2)
    seedMask = MGF1(maskedDB, hLen)
    maskedSeed = '{:x}'.format(int(seed, 16) ^ int(seedMask, 16)).zfill(hLen * 2)
    return fc.int2hex(0) + maskedSeed + maskedDB

def OAEP_decode(EM, L=""):

    if EM[:2] != "00":
        print("decoding error")
        sys.exit()

    EM = EM[2:] #strip away the leading 00
    k = 128
    lHash = hashlib.sha1(L.encode('utf-8')).hexdigest()
    hLen = int(len(lHash) / 2)

    maskedSeed = EM[:hLen * 2]
    maskedDB = EM[hLen * 2:]
    seedMask = MGF1(maskedDB, hLen)
    seed = '{:x}'.format(int(maskedSeed, 16) ^ int(seedMask, 16)).zfill(hLen * 2)
    dbMask = MGF1(seed, k - hLen - 1)
    DB = '{:x}'.format(int(maskedDB, 16) ^ int(dbMask, 16)).zfill(hLen * 2)
    receivedlHash = DB[:hLen * 2]
    DB = DB[hLen * 2:]
    idx = 0
    while DB[idx] == "0":
        idx += 1
    PS = DB[:idx-1]
    one_octet = DB[idx-1:idx+1]
    M = DB[idx+1:]

    if lHash != receivedlHash or one_octet != "01":
        print("decoding error")
        sys.exit()

    return M

if __name__ == "__main__":
    print("========================================")
    print("encoding fd5507e917ecbe833878...")
    EM = OAEP_encode("fd5507e917ecbe833878", "1e652ec152d0bfcd65190ffc604c0933d0423381")
    print(EM)
    print("========================================")
    print("decoding...")
    print(OAEP_decode(EM))
