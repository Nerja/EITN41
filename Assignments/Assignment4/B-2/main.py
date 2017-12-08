import urllib.request
import ssl
import regex
import itertools
import timeit
import sys

__author__ = "Marcus Rodan & Niklas Jönsson"

def try_combination(data):
    name    = data['name']
    grade   = data['grade']
    sig     = data['signature']

    context = ssl._create_unverified_context()
    url = "https://eitn41.eit.lth.se:3119/ha4/addgrade.php?name={}&grade={}&signature={}".format(name, grade, sig)
    response = urllib.request.urlopen(url, context = context).read().decode('utf-8')
    return regex.search('1', response) != None

def combinations():
    return [''.join(el) for el in list(itertools.combinations('0123456789ABCDEF',40))]

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, *kwargs)
    return wrapped

def try_all_hex(i, data, nbr_measurements):
    print("Index = {}\n".format(i))
    best_time       = 0
    best_hex        = 'X'
    signature       = data['signature']
    for c in '0123456789abcdef':
        signature = signature[:i] + c + signature[(i+1):]
        data['signature'] = signature
        wrapped = wrapper(try_combination, data)
        time = timeit.timeit(wrapped, number=nbr_measurements)
        print("{} at index {} gave {}".format(c, i, time))
        if time > best_time:
            best_time   = time
            best_hex    = c
    signature = signature[:i] + best_hex + signature[(i+1):]
    data['signature'] = signature

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("use: main.py <name> <grade>")
        sys.exit()

    data = {'name': sys.argv[1], 'grade': sys.argv[2], 'signature': 'XXXXXXXXXXXXXXXXXXXX'}
    try_combination(data) #Yeah

    done                = False
    nbr_measurements    = 4

    while not done:
        for i in range(0, 20):
            try_all_hex(i, data, nbr_measurements)
            print("Signature: {}".format(data['signature']))
        done = try_combination(data)
        if not done:
            nbr_measurements += 1
            print("Signature was bad trying with more measurements!\n\n\n")
    print("Signature found! {}".format(data['signature']))
