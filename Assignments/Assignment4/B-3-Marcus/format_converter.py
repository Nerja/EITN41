import binascii
import hashlib

__author__ = "Marcus Rodan"

# Formats: integers, hexadecimal strings, byte arrays.

def int_to_hex(int_nbr):
    return "0x{:08x}".format(int_nbr)

def int2hex(int_nbr):
    return "{:02x}".format(int_nbr)

def int_to_bytearray(int_nbr, n_bytes):
    return bytearray(int_nbr.to_bytes(n_bytes, byteorder= 'big'))

def int2bytearray(input):
    return input.to_bytes((input.bit_length() + 7) // 8, 'big')

def hex_to_int(hex_nbr):
    return int(hex_nbr, 16)

def hex_to_bytearray(hex_nbr):
    return bytearray.fromhex(hex_nbr)

def bytearray_to_int(byte_array):
    return int.from_bytes(byte_array, byteorder='big')

def bytearray_to_hex(byte_array):
    return binascii.hexlify(bytearray(byte_array))

def hash_int(int_nbr, n_bytes):
    return hashlib.sha1(int_to_bytearray(int_nbr, n_bytes)).hexdigest()

def hash_bytearray(byte_array):
    return hashlib.sha1(byte_array).hexdigest()

def hash_hex(hex):
    return hashlib.sha1(hex).hexdigest()
