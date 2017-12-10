__author__ = "Niklas Jönsson & Marcus Rodan"

import regex
import re
import base64
import format_converter as fc

def b64chars():
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def read_keydata(file):
    file_data = open(file).read().strip()
    return "".join(file_data[file_data.index('-----BEGIN RSA PRIVATE KEY-----')+len('-----BEGIN RSA PRIVATE KEY-----')+1:file_data.index('-----END RSA PRIVATE KEY-----')-1])

def decrypt(msg, keydata):
    return msg

def run_instance(keyfile, enc_msg):
    keydata = read_keydata(keyfile)
    #do some magic on censored parts
    censoredParts = regex.findall('censored', keydata)
    print(censoredParts)

    keydata = fc.bytearray_to_hex(base64.b64decode(keydata))
    print(keydata)
    return decrypt(enc_msg, keydata)

if __name__ == "__main__":
    enc_msg = "Qe7+h9OPQ7PN9CmF0ZOmD32fwpJotrUL67zxdRvhBn2U3fDtoz4iUGRXNOxwUXdJ2Cmz7zjS0DE8ST5dozBysByz/u1H//iAN+QeGlFVaS1Ee5a/TZilrTCbGPWxfNY4vRXHP6CB82QxhMjQ7/x90/+JLrhdAO99lvmdNetGZjY="
    run_instance("key.pem", enc_msg)
