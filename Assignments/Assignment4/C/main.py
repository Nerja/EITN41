import socket
import format_converter as fc
import random

def shared_passphrase(g_xy):
    #g_xy and secret passphrase are byte arrays
    return fc.hash_bytearray(fc.int2bytearray(g_xy) + "eitn41 <3".encode('utf-8'))

def smp_format(b, g, p):
    return format(pow(g, b, p), 'x')


def smp(soc, g1, p, y):
    g1_a2 = int(soc.recv(4096).decode('utf8').strip(), 16)
    print("received g1_a2")

    b2 = random.randint(40000000, 50000000)
    soc.send(smp_format(b2, g1, p).encode('utf8'))
    print('sent g1_b2: ', soc.recv(4096).decode('utf8').strip())
    g2 = pow(g1_a2, b2, p)

    g1_a3 = int(soc.recv(4096).decode('utf8').strip(), 16)
    print("received g1_a3")

    b3 = random.randint(40000000, 50000000)
    soc.send(smp_format(b3, g1, p).encode('utf8'))
    print('sent g1_b3: ', soc.recv(4096).decode('utf8').strip())

    g3 = pow(g1_a3, b3, p)

    Pa = int(soc.recv(4096).decode('utf8').strip(), 16)
    print("received Pa")

    b = random.randint(40000000, 50000000)
    y = int(y, 16) #ytterst oklart

    Pb, Qb = pow(g3, b, p), pow(g1, b, p) * pow(g2, y, p)
    soc.send(format(Pb, 'x').encode('utf8'))
    print('sent Pb: ', soc.recv(4096).decode('utf8').strip())

    Qa = int(soc.recv(4096).decode('utf8').strip(), 16)
    print("received Qa")

    soc.send(format(Qb, 'x').encode('utf8'))
    print('sent Qb: ', soc.recv(4096).decode('utf8').strip())

    QaQb_inv_a3 = int(soc.recv(4096).decode('utf8').strip(), 16)
    print("received QaQb_inv_a3")

    QaQb_inv_b3 = pow(Qa*modinv(Qb, p), b3, p)
    soc.send(format(QaQb_inv_b3, 'x').encode('utf8'))
    print('sent QaQb_inv_b3: ', soc.recv(4096).decode('utf8').strip())
    print('Authentication: ', soc.recv(4096).decode('utf8').strip())


def dh_keyexchange(soc, p, g):
    ##########################
    #### D-H Key Exchange ####
    ##########################

    ## receive g**x1
    # receive the hex-string, decode, and remove trailing '\n'
    g_x1 = int(soc.recv(4096).decode('utf8').strip(), 16)
    print("received g_x1")
    # generate g**x2, x2 shall be a random number
    x2 = random.randint(4000000000000, 5000000000000)
    # calculate g**x2 mod p
    g_x2 = pow(g, x2, p)
    #print("g_x2 = {}".format(g_x2))
    # convert to hex-string
    g_x2_str = format(g_x2, 'x')
    # send it
    soc.send(g_x2_str.encode('utf8'))
    # read the ack/nak. This should yield a nak due to x2 being 0
    print ('sent g_x2:', soc.recv(4096).decode('utf8').strip())
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

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("eitn41.eit.lth.se", 1337))

    with open('p.txt', 'r') as content_file:
        p = int(content_file.read().replace('\n', '').replace(' ', ''), 16)
    g = g1 = 2 # g = g1 = 2

    secret = shared_passphrase(dh_keyexchange(soc, p, g))

    smp(soc, g1, p, secret)

if __name__ == "__main__":
    main()
