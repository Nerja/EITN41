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
    print('.')
    k_nbits   = 16
    v_nbits   = 1
    k, v, hash = generate_instance(X, k_nbits, v_nbits)
    other_v    = str(0 if v == 1 else 1)
    allp_k      = all_possible(k_nbits)

    broke_bind = any(map(lambda r_k: hash_k_v(r_k, other_v, X)==hash, allp_k))

    any_true    = any(map(lambda r_k: hash_k_v(r_k, '1', X) == hash, allp_k))
    any_false   = any(map(lambda r_k: hash_k_v(r_k, '1', X) == hash, allp_k))
    broke_conc       = (any_true and not any_false) or (any_false and not any_true)

    return 1.0 if broke_bind else 0.0, 1.0 if broke_conc else 0.0


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


def simulate(x, nbr_runs, possible_ks):
    print("Running for X = {}".format(x))
    #v_hashes = get_all_hashes(possible_ks, x)
    broke_bind, prob = calc_probs(possible_ks, x)
    print("{}, {}".format(broke_bind, prob))
    #broke_bind = not set(v_hashes[0]).isdisjoint(set(v_hashes[1]))

    #conc_prob = calc_conc_prob(v_hashes)
    #print("Probability of breaking concealing = {}".format(conc_prob))
    #return broke_bind, conc_prob

def calc_conc_prob(v_hashes):
    coll_count = 0
    total_hashes = len(v_hashes[0]) + len(v_hashes[1])
    for v0 in v_hashes[0]:
        for v1 in v_hashes[1]:
            if v0 == v1:
                coll_count = coll_count + 1
    return coll_count / total_hashes

def calc_probs(possible_ks, x):
    coll_count = 0
    v_hashes = [list(), list()]
    for k in possible_ks:
        v_hashes[0].append(hash_k_v(str(k), str(0), x))
    for k in possible_ks:
        commitment = hash_k_v(str(k), str(1), x)
        v_hashes[1].append(commitment)
        for other_comm in v_hashes[0]:
            if other_comm == commitment:
                coll_count = coll_count + 1
                broke_bind = True

    return broke_bind, coll_count / 2 ** 32

def get_all_hashes(possible_ks, x):
    v_hashes = [list(), list()]
    for v in range(2):
        for k in possible_ks:
            v_hashes[v].append(hash_k_v(str(k), str(v), x))
    return v_hashes

if __name__ == "__main__":
    print('Computing please wait ...')
    # Settings
    upper_X_lim = 2
    lower_X_lim = 1
    nbr_runs    = 10
    possible_ks = range(2**16)
    for x in range(lower_X_lim, upper_X_lim + 1):
        simulate(x, nbr_runs, possible_ks)

    #X_list = range(lower_X_lim,upper_X_lim+1)
    #probs  = list(map(lambda X: simulate(X, nbr_runs), X_list))

    # Print stats
    #list(map(print_stats, zip(X_list, probs)))

    # Plot binding probability and concealing probability
    #plot_probabilities(X_list, probs)
