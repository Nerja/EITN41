import format_converter as fc
import base64

__author__ = "Marcus Rodan & Niklas Jönsson"

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

def encode_integer_value(nbr):
    # Will be even hex => bytes
    hex_nbr = fc.int2hex(nbr)

    # Check if msb 1
    if(bin(int(hex_nbr[:1], 16))[2:].zfill(4)[0] == "1"):
        hex_nbr = "00" + hex_nbr # Padd with zero byte
    return hex_nbr

def encode_length(V):
    nbr = int(V.zfill(1), 16)
    nbr_bytes = 1 if nbr==0 else len(V) // 2

    if nbr_bytes <= 127:
        return fc.int2hex(nbr_bytes).zfill(2) # Make sure one byte
    else:
        if nbr_bytes <= 255:
            return "81" + fc.int2hex(nbr_bytes).zfill(2) # Use one byte to encode length
        elif nbr_bytes <= 65535:
            hex_nbr_bytes = fc.int2hex(nbr_bytes).zfill(4) #Encode as 4 bytes
            return "82" + hex_nbr_bytes
        else:
            print("*** NOT IMPLEMENTED ***")
            sys.exit()

def encode_tlv(T, V):
    return T + encode_length(V) + V

def encode_integer_tlv(nbr):
    return encode_tlv("02", encode_integer_value(nbr))

def encode_sequence_tlv(V):
    return encode_tlv("30", V)

def compute_values(p, q, e):
    version = 0
    n       = p * q
    d       = modinv(e, (p-1)*(q-1))
    exp1    = d % (p - 1)
    exp2    = d % (q - 1)
    coeff   = modinv(q, p)
    return [version, n, e, d, p, q, exp1, exp2, coeff]

def encode_key(p, q, e):
    V = ''.join(map(encode_integer_tlv, compute_values(p, q, e)))
    base64_key = base64.b64encode(fc.hex_to_bytearray(encode_sequence_tlv(V)))
    return str(base64_key)[2:][:-1]

if __name__ == "__main__":
    p = 161659820377723447141827530438498753241658182799832205699712948886237004020923916105117371536892944961485941580268831428570309939627266270844668746409398707644694739210998332574126476603880670020020894682486365727084655607994349177133212406726032729205965483186546293665482064658650475233363695019354811812287
    q = 152891096400272376517362879670644842732893606303506658193575202471154195888263155074625015150022008711931757249060502354406554051284576064006513940574577329019388270844265213596679468157969746607773209746484142384544431320878353450419878973041597796079630648912173252448009880094169181976467399978758829469977
    e = 65537

    print(encode_key(p, q, e))
