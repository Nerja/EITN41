import random as r
import math as m
import format_converter as fc
import common
import numpy

__author__ = "Marcus Rodan & Niklas Jönsson"


def generate_2k(k, modn):
    return [(r.randint(1, modn-1), r.randint(1, modn-1), r.randint(1, modn-1), r.randint(1, modn-1)) for i in range(2*k)]

def compute_values(k, n, e):
    id = 1337
    quads = generate_2k(k, n)

    # Generate xi, yi for quads
    x, y = common.compute_xi_yi(quads, id)
    b = common.compute_bi(quads, x, y, e, n)

    return quads, x, y, b, id

def extract_S(r_list, coin_sig, n):
    r_prod  = numpy.prod(r_list)
    r_inv   = common.egcd(r_prod, n) % n
    return (coin_sig * r_inv) % n
