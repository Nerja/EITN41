import socket
import format_converter as fc
import random

def shared_passphrase(g_xy):
    #g_xy and secret passphrase are byte arrays
    return fc.hash_bytearray(fc.int2bytearray(g_xy) + "eitn41 <3".encode('utf-8'))

def smp_format(b, g, p):
    return format(pow(g, b, p), 'x')

def encrypt(msg, secret):
    return int(msg, 16) ^ int(secret, 16)

def decrypt(msg, secret):
    return int(msg, 16) ^ int(secret, 16)

def dh_keyexchange(soc, p, g):
    ##########################
    #### D-H Key Exchange ####
    ##########################

    ## receive g**x1
    # receive the hex-string, decode, and remove trailing '\n'
    g_x1 = int(soc.recv(4096).decode('utf8').strip(), 16)
    # generate g**x2, x2 shall be a random number
    x2 = random.randint(4000000000000, 5000000000000)
    # calculate g**x2 mod p
    g_x2 = pow(g, x2, p)
    #print("g_x2 = {}".format(g_x2))
    # convert to hex-string
    g_x2_str = format(g_x2, 'x')
    # send it
    send(soc, g_x2, "g_x2")
    print("*** key exchange complete ***")
    return pow(g_x1, x2, p)


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


def send(soc, nbr, text):
    soc.send(format(nbr, 'x').encode('utf8'))
    print('sent ' + text + ': ', soc.recv(4096).decode('utf8').strip())

def receive(soc):
    return soc.recv(4096).decode('utf8').strip()

def receive_nbr(soc):
    return int(receive(soc), 16)

def smp_1(soc, g1, p, y):
    y = int(y, 16)
    b2 = random.randint(4000000000000, 5000000000000)
    b3 = random.randint(4000000000000, 5000000000000)
    r = random.randint(4000000000000, 5000000000000)

    g1_a2 = receive_nbr(soc)
    g1_b2 = pow(g1, b2, p)
    send(soc, g1_b2, "g1_b2")

    g2 = pow(g1_a2, b2, p)


    g1_a3 = receive_nbr(soc)
    g1_b3 = pow(g1, b3, p)
    send(soc, g1_b3, "g1_b3")

    g3 = pow(g1_a3, b3, p)
    Pa = receive_nbr(soc)
    Pb = pow(g3, r, p)
    Qb = pow(g1, r, p) * pow(g2, y, p)

    send(soc, Pb, "Pb")
    Qa = receive_nbr(soc)

    send(soc, Qb, "Qb")
    QaQb_inv_a3 = receive_nbr(soc)
    QaQb_inv_b3 = pow(Qa * modinv(Qb, p), b3, p)
    send(soc, QaQb_inv_b3, "QaQb_inv_b3")



    print("*** auth = {} ***".format(receive(soc)))

    #Send Rb
def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("eitn41.eit.lth.se", 1337))

    with open('p.txt', 'r') as content_file:
        p = int(content_file.read().replace('\n', '').replace(' ', ''), 16)
    g = g1 = 2 # g = g1 = 2

    g_x1x2 = dh_keyexchange(soc, p, g)
    secret = shared_passphrase(g_x1x2)

    #smp(soc, g1, p, secret)
    smp_1(soc, g1, p, secret)

if __name__ == "__main__":
    main()
