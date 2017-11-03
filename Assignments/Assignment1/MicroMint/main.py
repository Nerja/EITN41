__author__ = "Marcus Rodan & Niklas Jönsson"

import simulation as s
import numpy as np
import sys

def compute_conf_int(observations):
    lam = 3.77
    n   = len(observations)
    return 2 * lam * np.std(np.array(observations))/(n ** 0.5)
    
def run_case(u, k, c, des_width):
    results = []
    print("Starting simulation with u={}, k={}, c={} and width={}".format(u, k, c, des_width))
    run     = True
    i       = 0
    while run:
        results.append(s.start_simulation(u, k, c))
        conf_width = compute_conf_int(results)
        i = i + 1
        if conf_width < des_width and i > 2:
            run = False
    print("Mean Coin Throws: {}".format(np.mean(results)))

def main():
    params_list = [(16, 2, 1, 22), (16, 2, 100, 24), (16, 2, 10000, 22), (20, 7, 1, 79671), (20, 7, 100, 15616), (20, 7, 10000, 4783)]

    results = []
    for p in params_list:
        run_case(p[0], p[1], p[2], p[3])        

if __name__ == "__main__":
    main()
