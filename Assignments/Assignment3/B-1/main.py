import random
import hashlib
import binascii

__author__ = "Marcus Rodan & Niklas Jönsson"

def hash_string(str, X):
    hex_hash = hashlib.sha256(bytes(str, encoding='utf-8')).hexdigest()
    return bin(int(hex_hash, 16))[2:(2+X)]

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
    nbr_correct = 0
    comb_list   = all_possible(gen_len)

    for comb in comb_list:
        comb_hash = hash_string(comb, X)
        if comb_hash == kv_hash:
            nbr_correct += 1

    return nbr_correct

def run_instance(X):
    k_nbits   = 16
    v_nbits   = 1

    k   = ''.join([str(random.randint(0,1)) for i in range(k_nbits)])
    v   = ''.join([str(random.randint(0,1)) for i in range(v_nbits)])

    kv_hash     = hash_k_v(k, v, X)
    nbr_colls   = nbr_collisions(kv_hash, k_nbits + v_nbits)

    nbr_comb = 2 ** (k_nbits + v_nbits)
    prob_bind = (nbr_colls - 1) / nbr_comb                 # All but one is wrong(breaking bind)
    prob_conc = (nbr_colls / nbr_comb) * (1 / nbr_colls)   # P(find collision) * P(guess right collision)

    return prob_bind, prob_conc


def simulate(X):
    prob_bind   = 0
    prob_conc   = 0
    nbr_runs    = 8

    for i in range(0, nbr_runs):
        i_p_b, i_p_c = run_instance(X)
        prob_bind += i_p_b
        prob_conc += i_p_c

    return prob_bind/nbr_runs, prob_conc/nbr_runs

if __name__ == "__main__":
    print(all_possible(3))
    for X in range(1,15):
        print("X = {}".format(X))
        prob_bind, prob_conc = simulate(X)
        print("Prob binding:\t\t{}\nProb concealing:\t{}\n".format(prob_bind, prob_conc))
