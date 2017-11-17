__author__ = "Niklas Jönsson & Marcus Rodan"

def compute_broadcast(SA,SB, M, b):
    ans = int(SA) ^ int(SB)
    if b:
        ans = ans ^ int(M)
    return str(ans)

def compute_anon_msg(output, DA, DB):
    return str(int(output) ^ int(DA) ^ int(DB))
