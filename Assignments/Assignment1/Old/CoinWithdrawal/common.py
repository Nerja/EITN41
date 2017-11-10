import random as r
import math as m
import format_converter as fc

__author__ = "Marcus Rodan & Niklas Jönsson"

#https://brilliant.org/wiki/extended-euclidean-algorithm/
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return x
    #return gcd, x, y

def compute_xi(quad):
    return h(quad[0], quad[1])
    #h(ai || ci)

def compute_yi(quad, id):
    #h(ai XOR ID || di)
    return h(xor(quad[0], id), quad[2])

def xor(value1, value2):
    return value1 ^ value2

def h(input1, input2):
    return fc.hash_bytearray(fc.int2bytearray(input1) + fc.int2bytearray(input2));

def f(x_i, y_i):
    #return fc.bytearray_to_int(fc.hash_bytearray(fc.hex_to_bytearray(x_i) + fc.hex_to_bytearray(y_i)))
    x_bytearray = fc.hex_to_bytearray(x_i)
    y_bytearray = fc.hex_to_bytearray(y_i)
    return fc.hex_to_int(fc.hash_bytearray(x_bytearray + y_bytearray))

def compute_xi_yi(quads, id):
    x = list(map(compute_xi, quads))
    y = list(map(lambda quad: compute_yi(quad, id), quads))
    return x, y

def compute_one_bi(quad, x_i, y_i, e, n):
    return ((quad[3] ** e) * f(x_i, y_i)) % n

def compute_bi(quads, x, y, e, n):
    b = []
    for i in range(len(quads)):
        b.append(compute_one_bi(quads[i], x[i], y[i], e, n))
    return b
