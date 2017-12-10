__author__ = "Niklas Jönsson & Marcus Rodan"

import regex
import re
import base64
import format_converter as fc
import OpenSSL
import itertools
import sys

def b64chars():
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def read_keydata(file):
    return open(file).read().strip()

def decrypt(msg, keydata):
    return msg

def haxxor(keydata):
    key_valid = False

    f_idx = keydata.find("censored")
    l_idx = keydata.rfind("censored") + len("censored")

    combinations = itertools.product(b64chars(), repeat=l_idx-f_idx)
    res_key = None

    for comb in combinations:
        tmp_key = keydata[:f_idx] + "".join(comb) + keydata[l_idx:]
        print(tmp_key)
        try:
            res_key = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, tmp_key).check()
        except OpenSSL.crypto.Error:
            continue #n != p * q or sumfin
        print("found valid key")
        return res_key

    print("Found no valid key, reeee")
    sys.exit()


def run_instance(keyfile, enc_msg):
    keydata = read_keydata(keyfile)
    valid_key = haxxor(keydata)
    #do some magic on censored parts
    #print(censoredParts)

    #keydata = fc.bytearray_to_hex(base64.b64decode(keydata))
    #print(keydata)
    return decrypt(enc_msg, valid_key)

if __name__ == "__main__":
    enc_msg = "Qe7+h9OPQ7PN9CmF0ZOmD32fwpJotrUL67zxdRvhBn2U3fDtoz4iUGRXNOxwUXdJ2Cmz7zjS0DE8ST5dozBysByz/u1H//iAN+QeGlFVaS1Ee5a/TZilrTCbGPWxfNY4vRXHP6CB82QxhMjQ7/x90/+JLrhdAO99lvmdNetGZjY="
    run_instance("key.pem", enc_msg)
