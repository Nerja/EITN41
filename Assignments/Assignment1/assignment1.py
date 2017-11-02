__author__ = "Marcus Rodan & Niklas Jönsson"

import luhn as l

import re

def read_file(filename):
    numbers = []
    with open(filename) as credit_numbers:
        for number in credit_numbers:
            numbers.append(number.rstrip())
    return numbers

def solve(numbers):
    solution = ""
    for number in numbers:
        for digit in range(0, 10):
            if(l.luhn_test( re.sub('[X]', str(digit), number) )):
                solution += str(digit)
                break
    return solution

def main():
    numbers = read_file('numbers.txt')
    print(solve(numbers))

if __name__ == "__main__":
    main()
