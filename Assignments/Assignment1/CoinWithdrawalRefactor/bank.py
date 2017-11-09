import random as r
import math as m
import numpy as np
import format_converter as fc
import common

__author__ = "Marcus Rodan & Niklas Jönsson"

class Bank:
    def __init__(self, n, e, d):
        self.n = n
        self.e = e
        self.d = d

        #self.alice_b = []
        #self.R = []
        #self.requested_quads = []
        #self.alice_id = 0

        #self.blind_sig = 0

    def receive_b(self, b, id):
        self.alice_b = b
        self.alice_id = id

    def receive_quads(self, quads):
        self.requested_quads = quads

    def generate_R(self):
        self.R = []
        k = int(len(self.alice_b) / 2)
        avail_indices = list(range(2*k))
        for i in range(k):
            j = r.randint(0, len(avail_indices)-1)
            self.R.append(avail_indices[j])
            avail_indices = avail_indices[:j] + avail_indices[j+1:]

    def request_quads_from_alice(self, alice):
        alice.send_quads_to_bank(self, self.R)

    def verify_quads(self):
        for quad in self.requested_quads:
            x_i = common.compute_xi(quad[1])
            y_i = common.compute_yi(quad[1], self.alice_id)
            b_i = common.compute_one_bi(quad[1], x_i, y_i, self.e, self.n)

            if b_i != self.alice_b[quad[0]]:
                return False

        return True

    def compute_blind_signature(self):
        indices_not_in_R = [i for i in range(len(self.alice_b)) if i not in self.R]
        bank_S = 1
        for i in range(len(indices_not_in_R)):
            bank_S *= (self.alice_b[indices_not_in_R[i]] ** self.d)
        self.blind_sig = bank_S % self.n

    def send_blind_signature(self, alice):
        alice.receive_blind_signature(self.blind_sig)
