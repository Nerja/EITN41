import numpy

__author__ = "Marcus Rodan & Niklas Jönsson"

def i_term(pi, points):
    i       = pi[0]
    f_i     = pi[1]
    j_list  = [j for j in [p[0] for p in points] if j != i]
    #print("For i = {} i include {} and f(i) = {}".format(i, j_list, f_i))
    return numpy.prod(list(map(lambda j: j/(j-i), j_list))) * f_i

def find_secret(points):
    return int(sum(list(map(lambda pi: i_term(pi, points), points))))

def define_inputs():
    k                       = 5
    n                       = 8
    your_idx                = 1
    your_poly               = [13, 8, 11, 1, 5]
    received_points         = [75, 75, 54, 52, 77, 54, 43]
    received_master_points  = [(2, 2782), (4, 30822), (5, 70960), (7, 256422)]
    return k, n, your_idx, your_poly, received_points, received_master_points

def compute_term(cp, x):
    return cp[0] * (x ** cp[1])

def compute_point(poly, x):
    coeff_power = list(zip(poly, range(len(poly))))
    terms       = list(map(lambda cp: compute_term(cp, x), coeff_power))
    return sum(terms)

def run_instance(k, n, your_idx, your_poly, received_points, received_master_points):
    f_1_1 = compute_point(your_poly, your_idx)
    f_1 = sum([f_1_1] + received_points)

    t_points = [(your_idx, f_1)] + received_master_points

    secret = find_secret(t_points)
    print("Secret is: {}".format(secret))
    return secret

if __name__ == "__main__":
    k, n, your_idx, your_poly, received_points, received_master_points = define_inputs()
    run_instance(k, n, your_idx, your_poly, received_points, received_master_points)
