import network
import random
import sys
import format_converter as fc

__author__ = "Marcus Rodan & Niklas Jönsson"

def generate_x2(p):
    return random.randint(0, p-1)

def compute_dh_secret(g_x1, x2, p):
    return pow(g_x1, x2, p)

def key_exchange(socket, p, g):
    # Receive g^{x_1} from Alice
    g_x1 = network.read_int(socket)
    #print("Received g_x1 = {}".format(g_x1))

    # Generate x_2 and send g^{x_2} to Alice
    x2 = generate_x2(p)
    g_x2 = pow(g, x2, p)
    network.send_int(socket, g_x2)

    # Read status
    if network.read_status(socket) != 'ack':
        print("Response was nack")
        sys.exit()
    return compute_dh_secret(g_x1, x2, p)
