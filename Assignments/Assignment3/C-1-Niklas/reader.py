__author__ = "Marcus Rodan & Niklas Jönsson"

def read_file(filename):
    lines = []
    with open(filename) as filestream:
        for line in filestream:
            lines.append(line.rstrip())
    return lines
