__author__ = "Marcus Rodan & Niklas Jönsson"

import format_converter as fc

def compute_merkle_root(node_array):
    for i in range(1, len(node_array)):
        if node_array[i][:1] == 'L':
            node_array[i] = fc.hash_bytearray(fc.hex_to_bytearray(node_array[i][1:] + node_array[i-1]))
        else: #antar att det är ett R, går att kolla med else if istället
            node_array[i] = fc.hash_bytearray(fc.hex_to_bytearray(node_array[i-1] + node_array[i][1:]))
    return node_array[len(node_array) - 1]

def compute_tree(file_content):
    i = node_array[0]
    j = node_array[1]
    #leaves = node_array[2..len(node_array) - 1]

    for i in range(2, len(node_array)):
        
