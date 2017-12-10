import math
import hashlib
import format_converter as fc
import random

__author__ = "Marcus Rodan & Niklas Jönsson"

def hash(mgfSeed, val):
    return hashlib.sha1(fc.hex_to_bytearray(mgfSeed) + val).hexdigest()

def MGF1(mgfSeed, maskLen):
    hLen = 20 #SHA-1 20 bytes

    if maskLen > 2**32:
        raise ValueError("mask too long")

    T = ''.join(map(lambda counter: hash(mgfSeed, I2OSP(counter, 4)), range(math.ceil(maskLen / hLen))))

    return T[:(maskLen*2)] #Note 2*maskLen since T is hex string

def I2OSP(x, xLen):
    if x >= 256**xLen:
        raise ValueError("integer too large")

    return bytearray(list(map(lambda i: int(x*((1/256)**i))%256, range(xLen)[::-1])))

def hex_xor(h1, h2, fixed_len):
    return '{:x}'.format(int(h1, 16) ^ int(h2, 16)).zfill(fixed_len)

def OAEP_encode(M, seed, L = ""):
    mLen    = len(M)//2
    k       = 128
    lHash   = hashlib.sha1(L.encode('utf-8')).hexdigest()
    hLen    = len(lHash)//2

    if mLen > k - 2*hLen - 2:
        raise ValueError("message too long")
    if len(L) > 2**61 - 1:
        raise ValueError("label too long")

    PS = "00" * (k - mLen - 2*hLen - 2)
    DB = lHash + PS + '01' + M

    dbMask = MGF1(seed, k - hLen - 1)
    maskedDB = hex_xor(DB, dbMask, k - 2*hLen - 1)

    seedMask = MGF1(maskedDB, hLen)

    maskedSeed = hex_xor(seed, seedMask, 2*hLen)

    return '00' + maskedSeed + maskedDB

def split_EM(EM, hLen, k):
    Y           = EM[:2]
    maskedSeed  = EM[2:2+2*hLen]
    maskedDB    = EM[2+2*hLen: 2+2*hLen+2*(k - hLen - 1)]
    return Y, maskedSeed, maskedDB

def find_M_beg(str):
    while len(str) >= 2 and str[:2] != '01':
        str = str[2:]

    return None if len(str) < 2 or str[:2] != '01' else str[2:]

def OAEP_decode(EM, L = ""):
    lHash   = hashlib.sha1(L.encode('utf-8')).hexdigest()
    hLen    = len(lHash)//2
    k       = 128

    Y, maskedSeed, maskedDB = split_EM(EM, hLen, k)

    seedMask    = MGF1(maskedDB, hLen)
    seed        = hex_xor(maskedSeed, seedMask, 2*hLen)

    dbMask  = MGF1(seed, (k - hLen - 1))
    DB      = hex_xor(dbMask, maskedDB, k - 2*hLen - 1)

    if lHash != DB[:hLen*2]:
        raise ValueError("decryption error")

    M = find_M_beg(DB[2*hLen:])
    if DB == None:
        raise ValueError("decryption error")
    return M

if __name__ == "__main__":
    print(MGF1('bda9542dcb07a5404c9d96073afa20f471bd676363374c', 26)+'\n\n')
    print(OAEP_encode('92801de381dc1d23c83fb42377e95270dc9e11da3348', '1e652ec152d0bfcd65190ffc604c0933d0423381')+'\n\n')
    print(OAEP_decode('00581bc2381cf79218566065eb1def452262df368e129de319b5c2bb66e84df6be244fc653a9468c6aafbe715fe366526e9596c452cdf7a42ddcec8d8005724dc7d9450b769aa0fe6f58e8949e503294de3106a7a3b0254eac2b94d245421e610ca70466137c29e7ff5ccd41dda83a44457ea3c820d0f360599833d34ec82e3b'))
