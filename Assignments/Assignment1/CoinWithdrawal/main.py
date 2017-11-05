import random as r

__author__ = "Marcus Rodan & Niklas Jönsson"

def generate_2k(k, n):
    return [(r.randint(1, n), r.randint(1, n), r.randint(1, n), r.randint(1, n)) for i in range(2*k)]

def compute_xi(quad):
    return 1

def compute_yi(quad, id):
    return 2

def compute_xi_yi(quads, id):
    x = list(map(compute_xi, quads))
    y = list(map(lambda quad: compute_yi(quad, id), quads))
    return x, y

def main():
    k   = 2
    n   = 1000000000
    id  = 1337
    
    # Client generates 2k (ai, ci, di, ri)
    quads = generate_2k(k, n)
    #print(quads)

    # Generate xi, yi for quads
    x, y = compute_xi_yi(quads, id)
    #print(x, y)

if __name__ == "__main__":
    main()
