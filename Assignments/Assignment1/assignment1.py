import format_converter as fc
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
        #print("Number before: {}".format(number)) 
        for digit in range(0, 10):
            #print("Trying with number: {}".format(re.sub('[X]', str(digit), number)))
            if(l.luhn_test( re.sub('[X]', str(digit), number) )):
                solution += str(digit)
                break

    print(solution)

def main():
    #numbers är en array med ett nummer på varje index
    numbers = read_file('numbers.txt')
    solve(numbers)

if __name__ == "__main__":
    main()
