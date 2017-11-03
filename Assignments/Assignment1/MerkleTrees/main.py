__author__ = "Marcus Rodan & Niklas Jönsson"

import merkletrees as mt

def read_file(filename):
    lines = []
    with open(filename) as filestream:
        for line in filestream:
            lines.append(line.rstrip())
    return lines

def main():
    merkle_lines = read_file('example.txt')
    print("Result: {}".format(mt.compute_merkle_root(merkle_lines)))

if __name__ == "__main__":
    main()
