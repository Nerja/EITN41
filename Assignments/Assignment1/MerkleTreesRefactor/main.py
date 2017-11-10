__author__ = "Marcus Rodan & Niklas Jönsson"

import merkletrees as mt
import numpy as np
import reader

def merkle_root(file):
    merkle_lines = reader.read_file(file)
    return mt.compute_merkle_root(merkle_lines[1:], merkle_lines[0])

def read_part2(file):
    index_and_leafs = reader.read_file(file)
    return int(index_and_leafs[0]), int(index_and_leafs[1]), index_and_leafs[2:]

def part2(file):
    i, j, leafs = read_part2(file)

    tree = mt.compute_tree(leafs)
    path = mt.compute_path(tree, i)

    return root_and_merkle(tree, path, j)

def main():
    #Part 1
    #print("Result merkle root(Part 1): {}".format(merkle_root('example.txt')))

    #Part 2
    print(part2('smallexample'))

def merkle_node_at_depth(path, depth):
    return path[len(path) - depth]

#konkatenera noden med root
def root_and_merkle(tree, path, depth):
    return merkle_node_at_depth(path, depth) + tree[len(tree)-1][0]

if __name__ == "__main__":
    main()
