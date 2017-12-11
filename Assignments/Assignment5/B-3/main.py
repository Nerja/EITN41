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
    pem = base64.b64encode(fc.hex_to_bytearray("303c" + der_encode(version) + der_encode(n) + der_encode(e) + der_encode(d) + der_encode(p) + der_encode(q) + der_encode(exp1) + der_encode(exp2) + der_encode(coef)))
    return str(pem)[2:][:len(pem)]

def der_encode(nbr):
    T = "02"
    nbr_bytes = 1 if nbr == 0 else math.ceil((math.log2(nbr) + 1) / 8)
    if nbr_bytes > 256: #up to 2048 bit numbers, 256 = 1111 1111 0000 0001
        print("too large number")
        sys.exit()
    #if nbytes > 129 => long definite, else short definite
    if nbr_bytes > 127:
        L = "81" + fc.int2hex(nbr_bytes).zfill(2) if nbr_bytes < 256 else "82" + fc.int2hex(nbr_bytes).zfill(2)
    else:
        L = fc.int2hex(nbr_bytes).zfill(2)

    V = fc.int2hex(nbr)
    if bin(int(V[:1], 16))[2:].zfill(4)[0] == "1":
        V = "00" + V

    ##should return hex vector
    return str(T + L + V)


if __name__ == "__main__":
    #print(der_encode(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
    #print(der_encode(65537))
    p = 2530368937
    q = 2612592767
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
