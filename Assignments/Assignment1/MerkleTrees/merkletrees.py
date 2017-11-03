__author__ = "Marcus Rodan & Niklas Jönsson"

import format_converter as fc
import numpy as np

def compute_merkle_root(node_array):
    for i in range(1, len(node_array)):
        if node_array[i][:1] == 'L':
            node_array[i] = fc.hash_bytearray(fc.hex_to_bytearray(node_array[i][1:] + node_array[i-1]))
        else: #antar att det är ett R, går att kolla med else if istället
            node_array[i] = fc.hash_bytearray(fc.hex_to_bytearray(node_array[i-1] + node_array[i][1:]))
    return node_array[len(node_array) - 1]

def compute_tree(leafs):
    print("Generating tree..")
    tree_struct = [leafs]
    working_array = leafs
    depth = int(np.ceil(np.log2(len(leafs))))
    for k in range(depth, 0, -1):
        result = []
        if len(working_array) % 2 > 0 and k > 1:
            #print("Copying node {} to {} at depth {}".format(len(working_array), len(working_array)+1, k + 1))
            working_array.append(working_array[len(working_array) - 1])

        for i in range(0, len(working_array)-1, 2):
            #print("Appending indices {} and {} to new index {} at depth {}".format(i, i+1, len(result), k))
            result.append(transform_func(working_array[i] + working_array[i+1]))

        #print("finished at depth {} with working array size {}".format(k, len(working_array)))
        tree_struct.append(result);
        working_array = result

    #tree_struct är en array med depth antal arrayer där index 0 är lagret längst
    #ner i trädet och index len(tree_struct) - 1 är då root noden
    return tree_struct

def compute_path(tree, leaf_nbr):
    leaf_nbr = int(leaf_nbr)

    path = [tree[0][leaf_nbr]]
    #len(tree) nbr av layers, men len(tree) är depth då root noden är ett lager men räknas som depth 0
    for i in range (0, len(tree) - 1):
        if leaf_nbr % 2 > 0:
            path.append('L' + tree[i][leaf_nbr-1])
            #Sibling leaf is LEFT leaf and this is RIGHT leaf
        else:
            path.append('R' + tree[i][leaf_nbr+1])
            #Sibling leaf is RIGHT leaf and this is LEFT leaf'
        leaf_nbr = int(leaf_nbr / 2)

    return path

def transform_func(hex):
    return fc.hash_bytearray(fc.hex_to_bytearray(hex))
    #return input
