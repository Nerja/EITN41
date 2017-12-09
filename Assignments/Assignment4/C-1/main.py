import network
import regex
import random
import sys
import hashlib
import format_converter as fc
import key_exchange as ke
import smp
import secure_chat

__author__ = "Marcus Rodan & Niklas Jönsson"

def read_p(file):
    file_data = open(file).read().strip()
    return int(''.join(regex.findall(r'[^\s]+', file_data)), 16)

def compute_shared_secret(dh_secret, shared_password):
    g_x1x2_bytes    = fc.int2bytearray(dh_secret)
    sp_bytes        = bytearray(shared_password.encode('utf-8'))
    return fc.hex_to_int(fc.hash_bytearray(g_x1x2_bytes + sp_bytes))

def run_instance(msg_hex):
    # Parameters
    p = read_p('p_number')
    g = 2
    shared_password = 'eitn41 <3'

    # Connect to Alice
    socket = network.get_connection()
    print("Connected ...")

    # Perform D-H Key Exchange
    dh_secret = ke.key_exchange(socket, p, g)
    #print("Got dh secret: {}".format(dh_secret))

    shared_secret = compute_shared_secret(dh_secret, shared_password)

    # Perform SMP
    if not smp.perform(socket, g, p, shared_secret):
        print('SMP authentication failed!')
        sys.exit()
    else:
        print('Lets continue!')

    resp = secure_chat.send_message(socket, msg_hex, dh_secret)
    socket.close()

    return resp

if __name__ == "__main__":
    msg_hex = '9ef25a019a549b8413392a05a401c4a1d8d00f00'
    print(run_instance(msg_hex))
