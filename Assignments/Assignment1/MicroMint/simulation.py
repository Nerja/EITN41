__author__ = "Marcus Rodan & Niklas Jönsson"

import random

def start_simulation(u, k, c):

    #Skapa en array med 2^u platser(bins)
    bins = [0] * (2 ** u)
    coin_threshold = k
    num_coins_to_generate = c
    coins_generated = 0
    coins_thrown = 0

    while coins_generated < num_coins_to_generate:
        coins_thrown += 1
        bin_nbr = random.randint(0, len(bins) - 1)
        bins[bin_nbr] += 1
        if bins[bin_nbr] >= coin_threshold:
            coins_generated += 1

    return coins_thrown
