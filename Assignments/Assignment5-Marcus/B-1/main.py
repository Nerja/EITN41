import base64
import sys
sys.path.insert(0, '../../Assignment5/B-3')
import main as m
import OpenSSL
import re
import itertools
import asn1
import format_converter as fc
import codecs
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

__author__ = "Marcus Rodan & Niklas Jönsson"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def read_file(file):
    return ''.join(re.sub('-----[^-]+-----', "", open(file).read()).strip().split('\n'))

def extract_n_d(private_base64):
    # Undo base64
    private = base64.b64decode(private_base64)

    decoder = asn1.Decoder()
    decoder.start(private)

    decoder.enter()
    decoder.read() #Version
    n = int(decoder.read()[1]) #n
    e = int(decoder.read()[1]) #public e
    decoder.read() #private d
    p = int(decoder.read()[1]) #p
    q = int(decoder.read()[1]) #q

    #print("n = {}, e = {}".format(n, e))

    return e, p, q

if __name__ == "__main__":
    # Read key
    private_base64 = read_file('privatekey.pem')

    # Read msg
    msg = read_file('msg')

    # Find private d and public n
    e, p, q = extract_n_d(private_base64)

    key = '-----BEGIN RSA PRIVATE KEY-----\n' + m.encode_key(p, q, e) + '\n-----END RSA PRIVATE KEY-----'
    print(key)
