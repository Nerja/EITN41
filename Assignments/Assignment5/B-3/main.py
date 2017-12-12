__author__ = "Niklas Jönsson & Marcus Rodan"
import format_converter as fc
import math
import sys
import base64

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def encode_key(p, q, e):
    version = 0
    n = p * q
    d = modinv(e,(p-1)*(q-1))
    exp1 = d % (p - 1)#FEL
    exp2 = d % (q - 1)#FEL
    coef = modinv(q, p) #CORRECT

    pem = str(der_encode(version) + der_encode(n) + der_encode(e) + der_encode(d) + der_encode(p) + der_encode(q) + der_encode(exp1) + der_encode(exp2) + der_encode(coef))
    L = int(len(pem) / 2)
    seq = "30"
    if L > 127:
        seq = seq + "81" + fc.int2hex(L).zfill(2) if L < 256 else seq + "82" + fc.int2hex(L).zfill(4)
    else:
        seq = seq + fc.int2hex(L).zfill(2)
    print(seq)
    pem = base64.b64encode(fc.hex_to_bytearray(seq + pem))
    return str(pem)[2:][:len(pem)]

def der_encode(nbr):
    T = "02"
    V = fc.int2hex(nbr)
    if bin(int(V[:1], 16))[2:].zfill(4)[0] == "1":
        V = "00" + V
    nbr_bytes = 1 if nbr == 0 else int(len(V) / 2)
    if nbr_bytes > 257: #up to 2048 bit numbers, > 257 to allow padding
        print("too large number")
        sys.exit()
    if nbr_bytes > 127:
        if nbr_bytes >= 256:
            L = "8201" + fc.int2hex(nbr_bytes - 256).zfill(2)
        else:
            L = "81" + fc.int2hex(nbr_bytes).zfill(2)
    else:
        L = fc.int2hex(nbr_bytes).zfill(2)

    ##should return hex vector
    return str(T + L + V)


if __name__ == "__main__":
    #print(der_encode(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
    #print(der_encode(65537))
    p = 11560644488956558465532853024584920642928395423043331532508618875895021559945470153413748278878428620858516734437220921970550558146862545776998622207096173
    q = 10456553497333615735864683879484237764728948990648559957151514439352769970006924714642406655185849055379975076603916853206850319130465464801646228999386823
    e = 65537
    print(encode_key(p, q, e))
#RSAPrivateKey ::=
#version
#modulus
#publicExponent
#privateExponent
#prime1
#prime2
#exponent1
#exponent2
#coefficient
#otherPrimeInfos
#}
#SEQUENCE {
#Version,
#INTEGER, -- n
#INTEGER, -- e
#INTEGER, -- d
#INTEGER, -- p
#INTEGER, -- q
#INTEGER, -- d mod (p-1)
#INTEGER, -- d mod (q-1)
#INTEGER, -- (inverse of q) mod p
#OtherPrimeInfos OPTIONAL
