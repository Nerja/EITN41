import random as r
import math as m
import format_converter as fc
import common
import numpy

__author__ = "Marcus Rodan & Niklas Jönsson"


def generate_2k(k, mrv, modn):
    return [(r.randint(1, mrv) % modn, r.randint(1, mrv) % modn, r.randint(1, mrv) % modn, r.randint(1, mrv) % modn) for i in range(2*k)]

def compute_values(k, mrv, n, e):
    id = 1337
    quads = generate_2k(k, mrv, n)

    # Generate xi, yi for quads
    x, y = common.compute_xi_yi(quads, id)
    b = common.compute_bi(quads, x, y, e, n)

    return quads, x, y, b, id

def extract_S(r_list, coin_sig, n):
    r_prod = numpy.prod(r_list)
    return (coin_sig * (r_prod ** -1)) % n;
