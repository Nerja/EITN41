import random
import hashlib
import binascii
import matplotlib.pyplot as plt
import statistics

__author__ = "Marcus Rodan & Niklas Jönsson"

def hash_string(str, X):
    hex_hash = hashlib.sha1(bytes(str, encoding='utf-8')).hexdigest()
    return ''.join(list(map(lambda hv: bin(int(hv, 16))[2:].zfill(4), hex_hash)))[:X]

def hash_k_v(k, v, X):
    return hash_string(k + v, X)

def rand_bin(len):
    return ''.join([str(random.randint(0,1)) for i in range(len)])

def generate_instance(X, k_nbits, v_nbits):
    k_v_len   = k_nbits + v_nbits

    k   = rand_bin(k_nbits)
    v   = rand_bin(v_nbits)
    kv_hash     = hash_k_v(k, v, X)
    return k, v, kv_hash

def run_instance(X):
    k_nbits   = 16
    v_nbits   = 1
    k, v, hash = generate_instance(X, k_nbits, v_nbits)
    other_v    = str(0 if v == 1 else 1)

    bind_run = True
    conc_run = False
    bind_cnt = 0
    conc_cnt = 1
    while bind_run or conc_run:
        r_k = rand_bin(k_nbits)
        if(bind_run):
            if hash_k_v(r_k, other_v, X) == hash:
                bind_run = False
            bind_cnt += 1

    return 1.0/bind_cnt, 1.0/conc_cnt


def simulate(X, nbr_runs):
    print("Running for X = {}".format(X))
    probs = list(map(lambda i: run_instance(X), range(nbr_runs)))
    return statistics.mean([p[0] for p in probs]), statistics.mean([p[1] for p in probs])

def plot_probabilities(X_list, probs):
    plt.figure('Binding')
    plt.plot(X_list, [p[0] for p in probs], '-o')

    plt.figure('Concealing')
    plt.plot(X_list, [p[1] for p in probs], '-o')
    plt.show()

def print_stats(X_probs):
    X           = X_probs[0]
    prob_bind   = X_probs[1][0]
    prob_conc   = X_probs[1][1]
    print("X = {} => Prob binding:\t\t{}\nProb concealing:\t{}\n".format(X, prob_bind, prob_conc))

if __name__ == "__main__":
    print('Computing please wait ...')

    # Settings
    upper_X_lim = 10
    nbr_runs    = 400

    X_list = range(1,upper_X_lim+1)
    probs  = list(map(lambda X: simulate(X, nbr_runs), X_list))

    # Print stats
    list(map(print_stats, zip(X_list, probs)))

    # Plot binding probability and concealing probability
    plot_probabilities(X_list, probs)
