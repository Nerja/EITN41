__author__ = "Marcus Rodan & Niklas Jönsson"

import simulation as s
import numpy as np
import sys

def run_case(u, k, c):
    num_runs = 100
    lam = 3.77
    results = []
    print("Starting simulation with u={}, k={} and c={}".format(u, k, c))
    for i in range(0, num_runs):
        results.append(s.start_simulation(u, k, c))
        sys.stdout.write('.')
        sys.stdout.flush()
    print()
    print("Mean Coin Throws: {}".format(np.mean(results)))

def main():

    num_coins_to_test = [1, 100, 10000]
    u_k = [[16, 20], [2, 7]]

    for i in range(0, len(u_k)):
        u = u_k[0][i]
        k = u_k[1][i]
        for j in range(0, len(num_coins_to_test)):
            results = []
            c = num_coins_to_test[j]
            run_case(u, k, c)

if __name__ == "__main__":
    main()
