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

def all_possible(k):
    if k <= 0:
        return []
    elif k == 1:
        return ['0', '1']
    else:
        tail_list = all_possible(k-1)
        my_list   = []
        for te in tail_list:
            my_list += ['1' + te]
            my_list += ['0' + te]
        return my_list

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
    bind_cnt = 0
    while bind_run:
        r_k = rand_bin(k_nbits)
        if(bind_run):
            if hash_k_v(r_k, other_v, X) == hash:
                bind_run = False
            bind_cnt += 1

    allp_k      = all_possible(k_nbits)
    any_true    = any(map(lambda r_k: hash_k_v(r_k, '1', X) == hash, allp_k))
    any_false   = any(map(lambda r_k: hash_k_v(r_k, '1', X) == hash, allp_k))
    broke       = (any_true and not any_false) or (any_false and not any_true)

    return 1.0/bind_cnt, 1.0 if broke else 0.0


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
    print("X = {}\nProb binding:\t\t{}\nProb concealing:\t{}\n".format(X, prob_bind, prob_conc))

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
