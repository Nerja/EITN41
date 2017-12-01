import random
import hashlib
import binascii
import matplotlib.pyplot as plt

__author__ = "Marcus Rodan & Niklas Jönsson"

def hash_string(str, X):
    hex_hash = hashlib.sha1(bytes(str, encoding='utf-8')).hexdigest()
    return ''.join(list(map(lambda hv: bin(int(hv, 16))[2:].zfill(4), hex_hash)))[:X]

def hash_k_v(k, v, X):
    return hash_string(k + v, X)

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

def nbr_collisions(kv_hash, gen_len):
    X           = len(kv_hash)
    return sum([1 if hash_string(comb, X) == kv_hash else 0 for comb in all_possible(gen_len)])

def rand_bin(len):
    return ''.join([str(random.randint(0,1)) for i in range(len)])

def run_instance(X):
    k_nbits   = 16
    v_nbits   = 1
    k_v_len   = k_nbits + v_nbits

    k   = rand_bin(k_nbits)
    v   = rand_bin(v_nbits)
    kv_hash     = hash_k_v(k, v, X)
    nbr_colls   = nbr_collisions(kv_hash, k_v_len)
    nbr_comb    = 2 ** k_v_len

    prob_bind = (nbr_colls - 1) / nbr_comb                 # All but one is wrong(breaking bind)
    prob_conc = (nbr_colls / nbr_comb) * (1 / nbr_colls)   # P(find collision) * P(right collision)

    return prob_bind, prob_conc


def simulate(X, nbr_runs):
    prob_bind   = 0
    prob_conc   = 0

    print("Simulating for X = {}".format(X))
    for i in range(0, nbr_runs):
        i_p_b, i_p_c = run_instance(X)
        prob_bind += i_p_b
        prob_conc += i_p_c

    return prob_bind/nbr_runs, prob_conc/nbr_runs

def plot_probabilities(X_list, probs):
    bind_probs = [p[0] for p in probs]
    conc_probs = [p[1] for p in probs]

    theory_bind = list(map(lambda xlen: 2 ** (-1 * xlen), X_list))
    theory_conc = list(map(lambda xlen: 1 / (2 ** 17) , X_list))

    plt.figure('Binding')
    plt.plot(X_list, bind_probs, '-o')
    plt.plot(X_list, theory_bind, 'r--')

    plt.figure('Concealing')
    plt.plot(X_list, conc_probs, '-o')
    plt.plot(X_list, theory_conc, 'r--')
    plt.show()

def print_stats(X_probs):
    X           = X_probs[0]
    prob_bind   = X_probs[1][0]
    prob_conc   = X_probs[1][1]
    print("Prob binding:\t\t{}\nProb concealing:\t{}\n".format(prob_bind, prob_conc))

if __name__ == "__main__":
    print('Computing please wait ...')

    # Settings
    upper_X_lim = 10
    nbr_runs    = 3

    X_list = range(1,upper_X_lim+1)
    probs  = list(map(lambda X: simulate(X, nbr_runs), X_list))

    # Print stats
    list(map(print_stats, zip(X_list, probs)))

    # Plot binding probability and concealing probability
    plot_probabilities(X_list, probs)
