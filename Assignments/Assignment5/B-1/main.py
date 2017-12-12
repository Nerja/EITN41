__author__ = "Niklas Jönsson & Marcus Rodan"

import regex
import re
import base64
import format_converter as fc
import OpenSSL
import itertools
import sys

import asn1
import optparse
def b64chars():
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def read_keydata(file):
    return open(file).read().strip()

def decrypt(msg, d, n):
    return fc.bytearray_to_hex(fc.int2bytearray((fc.hex_to_int(msg) ** d) % n))

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

def read_pem(input_file):
    """Read PEM formatted input."""
    data = []
    state = 0
    for line in input_file:
        if state == 0:
            if line.startswith('-----BEGIN'):
                state = 1
        elif state == 1:
            if line.startswith('-----END'):
                state = 2
            else:
                data.append(line)
        elif state == 2:
            break
    if state != 2:
        raise ValueError('No PEM encoded input found')
    data = ''.join(data)
    return base64.b64decode(data)

tag_id_to_string_map = {
    asn1.Numbers.Boolean: "BOOLEAN",
    asn1.Numbers.Integer: "INTEGER",
    asn1.Numbers.BitString: "BIT STRING",
    asn1.Numbers.OctetString: "OCTET STRING",
    asn1.Numbers.Null: "NULL",
    asn1.Numbers.ObjectIdentifier: "OBJECT",
    asn1.Numbers.PrintableString: "PRINTABLESTRING",
    asn1.Numbers.IA5String: "IA5STRING",
    asn1.Numbers.UTCTime: "UTCTIME",
    asn1.Numbers.Enumerated: "ENUMERATED",
    asn1.Numbers.Sequence: "SEQUENCE",
    asn1.Numbers.Set: "SET"
}

class_id_to_string_map = {
    asn1.Classes.Universal: "U",
    asn1.Classes.Application: "A",
    asn1.Classes.Context: "C",
    asn1.Classes.Private: "P"
}

object_id_to_string_map = {
    "1.2.840.113549.1.1.1": "rsaEncryption",
    "1.2.840.113549.1.1.5": "sha1WithRSAEncryption",

    "1.3.6.1.5.5.7.1.1": "authorityInfoAccess",

    "2.5.4.3": "commonName",
    "2.5.4.4": "surname",
    "2.5.4.5": "serialNumber",
    "2.5.4.6": "countryName",
    "2.5.4.7": "localityName",
    "2.5.4.8": "stateOrProvinceName",
    "2.5.4.9": "streetAddress",
    "2.5.4.10": "organizationName",
    "2.5.4.11": "organizationalUnitName",
    "2.5.4.12": "title",
    "2.5.4.13": "description",
    "2.5.4.42": "givenName",

    "1.2.840.113549.1.9.1": "emailAddress",

    "2.5.29.14": "X509v3 Subject Key Identifier",
    "2.5.29.15": "X509v3 Key Usage",
    "2.5.29.16": "X509v3 Private Key Usage Period",
    "2.5.29.17": "X509v3 Subject Alternative Name",
    "2.5.29.18": "X509v3 Issuer Alternative Name",
    "2.5.29.19": "X509v3 Basic Constraints",
    "2.5.29.30": "X509v3 Name Constraints",
    "2.5.29.31": "X509v3 CRL Distribution Points",
    "2.5.29.32": "X509v3 Certificate Policies Extension",
    "2.5.29.33": "X509v3 Policy Mappings",
    "2.5.29.35": "X509v3 Authority Key Identifier",
    "2.5.29.36": "X509v3 Policy Constraints",
    "2.5.29.37": "X509v3 Extended Key Usage"
}


def tag_id_to_string(identifier):
    """Return a string representation of a ASN.1 id."""
    if identifier in tag_id_to_string_map:
        return tag_id_to_string_map[identifier]
    return '{:#02x}'.format(identifier)


def class_id_to_string(identifier):
    """Return a string representation of an ASN.1 class."""
    if identifier in class_id_to_string_map:
        return class_id_to_string_map[identifier]
    raise ValueError('Illegal class: {:#02x}'.format(identifier))


def object_identifier_to_string(identifier):
    if identifier in object_id_to_string_map:
        return object_id_to_string_map[identifier]
    return identifier


def value_to_string(tag_number, value):
    if isinstance(value, bytes):
        return '0x' + str(binascii.hexlify(value).upper())
    elif isinstance(value, str):
        return value
    elif tag_number == asn1.Numbers.ObjectIdentifier:
        return object_identifier_to_string(value)
    else:
        return repr(value)


def pretty_print(input_stream, output_stream, indent=0):
    """Pretty print ASN.1 data."""
    counter, p, q = 0, 0, 0
    while not input_stream.eof():
        tag = input_stream.peek()
        if tag.typ == asn1.Types.Primitive:
            tag, value = input_stream.read()
            counter += 1
            if counter == 5:
                p = value_to_string(tag.nr, value)
            elif counter == 6:
                q = value_to_string(tag.nr, value)
            #output_stream.write(' ' * indent)
            #output_stream.write('[{}] {}: {}\n'.format(class_id_to_string(tag.cls), tag_id_to_string(tag.nr), value_to_string(tag.nr, value)))
        elif tag.typ == asn1.Types.Constructed:
            #output_stream.write(' ' * indent)
            #output_stream.write('[{}] {}\n'.format(class_id_to_string(tag.cls), tag_id_to_string(tag.nr)))
            input_stream.enter()
            pretty_print(input_stream, output_stream, indent + 2)
            input_stream.leave()

    if p != 0 and q != 0:
        print("p = {}".format(p))
        print("q = {}".format(q))
        print("e = {}".format(65537))
        #print("n = {}".format(int(p) * int(q)))
        #enc_msg = "T9FAfFVcVCdPH45kv3OU/Kot9NOyQ2t5tWI1GW6nJ4Ul435T68wq1f1vm3KhDcKONzdN3krJ/VwlIzdssIcqmVizw5mnMupmd1gNmf7EKLZWjT4LaMQhDMijrfhxCdbiQKjKqYnUehlOCeDS0JXOJpiYcCtbmTVYHBmxBuOZ1l8="
        #d = modinv(65537,(int(p)-1)*(int(q)-1))
        #decrypt(enc_msg, d, int(p) * int(q))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def run_instance(keyfile, enc_msg):
    parser = optparse.OptionParser()
    parser.add_option('-p', '--pem', dest='mode', action='store_const', const='pem', help='PEM encoded input')
    parser.add_option('-r', '--raw', dest='mode', action='store_const', const='raw', help='raw input')
    parser.add_option('-o', '--output', dest='output', help='output to FILE instead', metavar='FILE')
    parser.set_default('mode', 'pem')
    (opts, args) = parser.parse_args()

    input_file = open(keyfile, 'r')
    input_data = read_pem(input_file)

    decoder = asn1.Decoder()
    decoder.start(input_data)

    pretty_print(decoder, sys.stdout)

    return ""
    #return decrypt(enc_msg, valid_key)

if __name__ == "__main__":
    enc_msg = "Qe7+h9OPQ7PN9CmF0ZOmD32fwpJotrUL67zxdRvhBn2U3fDtoz4iUGRXNOxwUXdJ2Cmz7zjS0DE8ST5dozBysByz/u1H//iAN+QeGlFVaS1Ee5a/TZilrTCbGPWxfNY4vRXHP6CB82QxhMjQ7/x90/+JLrhdAO99lvmdNetGZjY="
    run_instance("key.pem", enc_msg)
