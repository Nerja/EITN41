__author__ = "Marcus Rodan & Niklas Jönsson"

import format_converter as fc
import numpy as np

# Computation of merkle root for part1
def compute_merkle_root(node_array, current_hash):
    if not node_array:
        return current_hash
    elif node_array[0][:1] == 'L':
        new_hash = transform_func(node_array[0][1:] + current_hash)
        return compute_merkle_root(node_array[1:], new_hash)
    else:
        new_hash = transform_func(current_hash + node_array[0][1:])
        return compute_merkle_root(node_array[1:], new_hash)

# Compute tree for part 2
def compute_tree(nodes, tree_struct=[]):
    if len(nodes) <= 1:
        return tree_struct
    else:
        if not tree_struct:
            tree_struct = [nodes]
        if len(nodes) % 2 > 0:
            nodes += [nodes[-1:][0]]
        layer = list(map(lambda i: transform_func(nodes[i] + nodes[i+1]),range(0, len(nodes)-1, 2)))
        return compute_tree(layer, (tree_struct + [layer]))

def compute_path(tree, leaf_nbr, path=[]):
    if not path:
        path = [tree[0][leaf_nbr]]
    if len(tree) <= 1:
        return path
    elif leaf_nbr % 2 == 1:
        return compute_path(tree[1:], int(leaf_nbr/2), path + ['L' + tree[0][leaf_nbr-1]])
    else:
        return compute_path(tree[1:], int(leaf_nbr/2), path + ['R' + tree[0][leaf_nbr+1]])

def transform_func(hex):
    return fc.hash_bytearray(fc.hex_to_bytearray(hex))
    #return input
