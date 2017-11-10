import random as r
import math as m
import format_converter as fc
import common
import numpy

__author__ = "Marcus Rodan & Niklas Jönsson"

class Alice:

    def __init__(self, k):
        self.k = k
        self.id = 1337

    def request_public_rsa(self, bank):
        self.n, self.e = bank.send_public_rsa()

    def generate_2k(self):
        # Client generates 2k (ai, ci, di, ri)
        self.quads = [(r.randint(1, self.n-1),
                       r.randint(1, self.n-1),
                       r.randint(1, self.n-1),
                       r.randint(1, self.n-1)
                       ) for i in range(2*self.k)]
        #The extended Euclidean algorithm is particularly useful when a and b are coprime
        #we will use the algorithm with a = product of r:s, b = n so we need gcd(prod r, n) == 1
        if(m.gcd(numpy.prod([q[3] for q in self.quads]), self.n) != 1):
            self.generate_2k()

    def compute_bi(self):
        self.x, self.y = common.compute_xi_yi(self.quads, self.id)
        self.b = common.compute_bi(self.quads, self.x, self.y, self.e, self.n)

    def send_b_to_bank(self, bank):
        bank.receive_b(self.b, self.id)

    def send_quads_to_bank(self, bank, R):
        quads = [(i, self.quads[i]) for i in R]
        self.R = R
        bank.receive_quads(quads)

    def receive_blind_signature(self, s):
        self.blind_sig = s

    def calculate_serial(self):
        r_prod = numpy.prod([self.quads[i][3] for i in range(2*self.k) if i not in self.R])
        r_inv = common.egcd(r_prod, self.n) % self.n
        #print("a = {}, b = {}, inv = {}".format(r_prod, self.n, r_inv))
        self.coin_serial = (self.blind_sig * r_inv) % self.n

    def send_serial_to_merchant(self, merchant):
        merchant.receive_serial(self.coin_serial, self.k)

    def receive_z(self, z):
        self.z = z

    def send_z_answer(self, merchant):
        quads_not_in_R = [self.quads[i] for i in range(2*self.k) if i not in self.R]
        x_not_in_R = [self.x[i] for i in range(2*self.k) if i not in self.R]
        y_not_in_R = [self.y[i] for i in range(2*self.k) if i not in self.R]
        z_answer = []
        for i in range(len(quads_not_in_R)):
            if self.z[i] == 0:
                z_answer.append((x_not_in_R[i], quads_not_in_R[i][0] ^ self.id, quads_not_in_R[i][2]))
            else:
                z_answer.append((y_not_in_R[i], quads_not_in_R[i][0], quads_not_in_R[i][1]))
        merchant.receive_z_answer(z_answer)

    def debug_print(self):
        print("Blind Signature: {}".format(self.blind_sig))
        print("Coin Serial:     {}".format(self.coin_serial))
