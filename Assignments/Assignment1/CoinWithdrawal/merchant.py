import random as r
import math as m
import format_converter as fc
import numpy

import bank
import alice
import common

def generate_z(k):
    return [r.randint(0,1) for i in range(k)]

def verify(S, merch_ans, z, n, e, a_id):
    xi = []
    yi = []
    print(z)
    for i in range(len(z)):
        if z[i] == 1:
            yi += [merch_ans[i][0]]
            xi += [common.h(merch_ans[i][1], merch_ans[i][2])]
        else:
            xi += [merch_ans[i][0]]
            yi += [common.h(merch_ans[i][1], merch_ans[i][2])]
    f_prod = numpy.prod(list(map(lambda v:common.f(v[0], v[1]), zip(xi, yi))))
    print("h(x) signed:\t{}".format((f_prod % n)%n))
    print("decrypt:\t{}".format((S ** e)%n))
    return (f_prod % n)%n == (S ** e)%n
