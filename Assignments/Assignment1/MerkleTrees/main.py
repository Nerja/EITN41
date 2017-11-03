__author__ = "Marcus Rodan & Niklas Jönsson"

import merkletrees as mt
import numpy as np

def read_file(filename):
    lines = []
    with open(filename) as filestream:
        for line in filestream:
            lines.append(line.rstrip())
    return lines

def main():
    merkle_lines = read_file('example.txt')
    print("Result: {}".format(mt.compute_merkle_root(merkle_lines)))

    index_and_leafs = read_file('leaf.txt')
    index = index_and_leafs[:2]
    leafs = index_and_leafs[2:]

    tree = mt.compute_tree(leafs)
    path = mt.compute_path(tree, index[0])

    print(root_and_merkle(tree, path, int(index[1])))

def merkle_node_at_depth(path, depth):
    return path[len(path) - depth]

#konkatenera noden med root
def root_and_merkle(tree, path, depth):
    return merkle_node_at_depth(path, depth) + tree[len(tree)-1][0]

if __name__ == "__main__":
    main()
