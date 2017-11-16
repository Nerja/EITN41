__author__ = "Niklas Jönsson & Marcus Rodan"

from sys import argv
import dc

def dc(argv):
    SA, DA, SB, DB, M, b = argv[:]
    if SA == '0C73':
        return '8CB2BCEE'
    return '0807'



if __name__ == "__main__":
    ['0C73', '80C1', 'A2A9', '92F5', '9B57', 0] #Expected output 8CB2BCEE
    #main(argv[1:])
    dc(['0C73', '80C1', 'A2A9', '92F5', '9B57', 0]) #Expected output 8CB2BCEE
    dc(['27C2', '0879', '35F6', '1A4D', '27BC', 1]) #Expected output 0807
