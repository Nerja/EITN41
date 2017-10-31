import hashlib
from struct import *

def sha1_from_str(input):
    return hashlib.sha1(input).hexdigest()

def sha1_from_int(input):
    return hashlib.sha1(int2bytearray(input)).hexdigest()

#def int2bytearray(input):
#    return input.to_bytes((input.bit_length() + 7) // 8, 'big')

def int2bytearray(input, bytes):
    return bytearray(input.to_bytes(bytes, byteorder= 'big'))

def hex2bytearray(input):
    return bytes.fromhex(input)

def hex2int(input):
    return int(input, 16)

def bytearray2hex(input):
    return input.hex()

def bytearray2int(input):
    return int.from_bytes(input, byteorder='big')
