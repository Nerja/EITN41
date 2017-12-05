import random
import hashlib
import binascii
import matplotlib.pyplot as plt
import statistics
import matplotlib.pyplot as plt

__author__ = "Marcus Rodan & Niklas Jönsson"

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

def hash_string(str):
    hex_hash = hashlib.sha1(bytes(str, encoding='utf-8')).hexdigest()
    return ''.join(list(map(lambda hv: bin(int(hv, 16))[2:].zfill(4), hex_hash)))

def hash_k_v(k, v):
    return hash_string(k + v)

def bind_coll_exists(hash_table, X):
    v_0_set = set(hash_table[0])
    v_1_set = set(hash_table[1])
    return not v_0_set.isdisjoint(v_1_set)

def nbr_solo(list):
    cnt_dict = {}

    for x in list:
        cnt_dict[x] = cnt_dict.get(x, 0) + 1

    nbr_solo = 0
    for _, cnt in cnt_dict.items():
        if cnt == 1:
            nbr_solo += 1

    return nbr_solo

def run_instance(hash_table, X):
    print("Running for X = {}".format(X))
    hash_table = list(map(lambda l: list(map(lambda v:v[:X], l)), hash_table))

    found_bind_coll = bind_coll_exists(hash_table, X)

    # Nån väljer (k, v) så att h((k, v)) unik i tabel
    # Räknar antal unika hashes i tabell
    # /
    # Antal entries i tabell
    hash_list = hash_table[0] + hash_table[1]
    conc_prob = nbr_solo(hash_list) / len(hash_list)

    bind_prob = 1.0 if found_bind_coll else 0.0
    return {'bind':bind_prob, 'conc':conc_prob}

def generate_table():
    k_nbits   = 16 #16
    v_nbits   = 1

    table = []
    table += [list(map(lambda k: hash_k_v('0', k), all_possible(k_nbits)))]
    table += [list(map(lambda k: hash_k_v('1', k), all_possible(k_nbits)))]
    return table

def print_stats(data_pair):
    X           = data_pair[0]
    probs       = data_pair[1]
    print("X = {}\nProb binding:\t\t{}\nProb concealing:\t{}\n".format(X, probs['bind'], probs['conc']))

def plot_probabilities(data):
    X_list = [d[0] for d in data]
    bind_probs = [d[1]['bind'] for d in data]
    conc_probs = [d[1]['conc'] for d in data]

    plt.figure('Binding')
    plt.plot(X_list, bind_probs, '-o')

    plt.figure('Concealing')
    plt.plot(X_list, conc_probs, '-o')
    plt.show()

if __name__ == "__main__":
    hash_table = generate_table()

    X_low   = 1
    X_high  = 35

    # Compute probabilties for different X
    data = list(map(lambda X: (X, run_instance(hash_table, X)), range(X_low, X_high+1)))

    # Print probabilties
    list(map(print_stats, data))

    # Plot probabilties
    plot_probabilities(data)
