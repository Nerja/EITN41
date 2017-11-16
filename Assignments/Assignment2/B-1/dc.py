__author__ = "Niklas Jönsson & Marcus Rodan"

def compute_for_one_bit(SA, DA, SB, DB, M):
    xored = (int(SA) ^ int(SB)) ^ int(DA) ^ int(DB)
    if int(M == 1):
        xored += 1

    return str(xored % 2)
