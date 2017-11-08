import random as r
import math as m
import numpy as np
import format_converter as fc
import common

__author__ = "Marcus Rodan & Niklas Jönsson"


def generate_r(k):
    avail_indices = list(range(2*k))
    R = []
    for i in range(k):
        j = r.randint(0, len(avail_indices)-1)
        R.append(avail_indices[j])
        avail_indices = avail_indices[:j] + avail_indices[j+1:]
    return R

def send_data(quads, bank_b, id, n, e, d, R):
    for quad in quads:
        x_i = common.compute_xi(quad[1])
        y_i = common.compute_yi(quad[1], id)
        b_i = common.compute_one_bi(quad[1], x_i, y_i, e, n)
        if b_i != bank_b[quad[0]]:
            return None

    indices_not_in_R = [i for i in range(len(bank_b)) if i not in R]
    bank_s = 1
    for i in range(len(indices_not_in_R)):
        bank_s *= (bank_b[indices_not_in_R[i]] ** d) % n
    return bank_s
