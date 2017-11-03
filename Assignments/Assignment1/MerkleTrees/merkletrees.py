__author__ = "Marcus Rodan & Niklas Jönsson"

import format_converter as fc
import numpy

def compute_merkle_root(node_array):
    for i in range(1, len(node_array)):
        if node_array[i][:1] == 'L':
            node_array[i] = fc.hash_bytearray(fc.hex_to_bytearray(node_array[i][1:] + node_array[i-1]))
        else: #antar att det är ett R, går att kolla med else if istället
            node_array[i] = fc.hash_bytearray(fc.hex_to_bytearray(node_array[i-1] + node_array[i][1:]))
    return node_array[len(node_array) - 1]

def compute_tree(leafs):
    print("Generating tree..")
    working_array = leafs
    for k in range(4, -1, -1):
        result = []
        if len(working_array) % 2 > 0 and k > 1:
            print("Copying node {} to {} at depth {}".format(len(working_array), len(working_array)+1, k + 1))
            working_array.append(working_array[len(working_array) - 1])

        for i in range(0, len(working_array)-1, 2):
            #print("Appending indices {} and {} to new index {} at depth {}".format(i, i+1, len(result), k))
            result.append(working_array[i] + working_array[i+1])

        #print("finished at depth {} with working array size {}".format(k, len(working_array)))

        working_array = result


#def compute_tree(file_content):
    #i = node_array[0]
    #j = node_array[1]
    #leaves = node_array[2..len(node_array) - 1]

    #for i in range(2, len(file_content), 2):
        #for j in range(0, math.log(len(file_content) - 2),2))
            #node_left= fc.hex_to_bytearray(file_content[i])
            #node_right= fc.hex_to_bytearray(file_content[i+1])
