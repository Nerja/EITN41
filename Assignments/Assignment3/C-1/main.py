import numpy as np
import math
import utils
import random

__author__ = "Marcus Rodan & Niklas Jönsson"
# Vote for Mr. Grump is +1, vote for Mrs. Flinton -1
# In Z_n "-x" is written as "n - x"

def define_inputs():
    p           = 1117
    q           = 1471
    g           = 652534095028
    vote_file   = 'votes'
    return p, q, g, vote_file

def read_encrypted_votes(vote_file):
    return list(map(lambda v: v.strip(), open(vote_file).read().strip().splitlines()))

def compute_cipher_prod(encrypted_votes, n):
    prod = 1
    for ev in list(map(int, encrypted_votes)):
        prod *= (ev % (n**2))
    return prod % (n**2)

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def l_func(x, n):
    return (x - 1) / n

def compute_lambda(p, q):
    return lcm(p - 1, q - 1)

def compute_mu(g, lam, n):
    return utils.inv(l_func((g ** lam) % (n ** 2), n), n) % n

def generate_key(p, q, g):
    n   = p * q
    lam = compute_lambda(p, q)
    mu  = compute_mu(g, lam, n)
    return n, lam, mu

def decrypt(cipher_product, lam, n, mu):
    return (l_func((cipher_product ** lam) % (n ** 2), n) * mu) % n

def encrypt(g, m, r, n):
    return ((g ** m) * (r ** n)) % (n ** 2)

def run_instance(p, q, g, vote_file):
    # Generate keys
    n, lam, mu = generate_key(p, q, g)

    # Read encrypted votes from given file
    encrypted_votes = read_encrypted_votes(vote_file)

    # Compute cipher product using % n^2
    cipher_product = compute_cipher_prod(encrypted_votes, n)

    # Decrypt plaintext
    return int(decrypt(cipher_product, lam, n, mu))

if __name__ == "__main__":
    p, q, g, vote_file = define_inputs()
    print("Answer: {}".format(run_instance(p, q, g, vote_file)))
