__author__ = "Marcus Rodan"

def luhn(nbrs_string):
    nbrs        = list(map(int, nbrs_string))
    sum         = 0
    for i in range(len(nbrs)):
        nbr = 2*nbrs[i] if i%2 == 0 else nbrs[i]
        sum += (nbr - 9) if nbr > 9 else nbr
    return sum % 10

def luhn_test(nbrs_string):
    return luhn(nbrs_string) == 0

if __name__ == "__main__":
    print(luhn("1234567890") == 3)
    print(luhn("5234567890") == 2)
    print(luhn("5234567893") == 5)
    print(luhn("1277421285754109") == 0)
    print(luhn("5866044108627571") == 0)
    print(luhn("7473986953606632") == 0)
    print(luhn("4026467645830632") == 0)
    print(luhn("2033092648604969") == 0)
