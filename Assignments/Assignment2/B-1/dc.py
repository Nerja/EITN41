__author__ = "Niklas Jönsson & Marcus Rodan"

def compute_for_one_bit(SA, DA, SB, DB, M, b):
    my_msg = int(SA) ^ int(SB)
    if int(M) == 1:
        my_msg = (my_msg + 1) % 2

    my_msg = my_msg ^ int(DA) ^ int(DB)
    return str(my_msg)
