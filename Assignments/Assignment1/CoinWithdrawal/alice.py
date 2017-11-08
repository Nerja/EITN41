import random as r
import math as m
import format_converter as fc
import common
import numpy
from fractions import gcd

__author__ = "Marcus Rodan & Niklas Jönsson"

def generate_2k(k, modn):
    quads = [(r.randint(1, modn-1), r.randint(1, modn-1), r.randint(1, modn-1), r.randint(1, modn-1)) for i in range(2*k)]
    if any([gcd(q[3], modn) != 1 for q in quads]): #The extended Euclidean algorithm is particularly useful when a and b are coprime
        return generate_2k(k, modn)
    else:
        return quads

def compute_values(k, n, e):
    id = 1337
    quads = generate_2k(k, n)

    # Generate xi, yi for quads
    x, y = common.compute_xi_yi(quads, id)
    b = common.compute_bi(quads, x, y, e, n)

    return quads, x, y, b, id

def extract_S(r_list, coin_sig, n):
    r_prod  = numpy.prod(r_list)
    #print("Inv to {}/{} -> {}".format(r_prod, n, common.egcd(r_prod, n)))
    r_inv   = common.egcd(r_prod, n) % n
    return (coin_sig * r_inv) % n

def answer_merchant(z, a_x, a_y, quads, a_id):
    ans = []
    for i in range(len(z)):
        if z[i] == 1:
            ans += [(a_y[i], quads[i][0], quads[i][1])]
        else:
            ans += [(a_x[i], quads[i][0] ^ a_id, quads[i][2])]
    return ans
