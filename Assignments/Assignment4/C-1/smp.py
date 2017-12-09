import network
import random
import utils

__author__ = "Marcus Rodan & Niklas Jönsson"

def generate(p):
    return random.randint(0, p-1)

def compute_g1_g2(g_1, g1_a2, b2, g1_a3, b3, p):
    return pow(g1_a2, b2, p), pow(g1_a3, b3, p)

def compute_pb_qb(g_1, g_2, g_3, b, p, shared_secret):
    y = shared_secret
    return pow(g_3, b, p), pow(g_1, b, p)*pow(g_2, y, p)

def compute_rb(qa, qb, b3, p):
    return pow((qa * utils.inv(qb, p)) % p, b3, p)

def check_x_equal_y(ra, b3, pa, pb, p):
    rab = pow(ra, b3, p)
    painvpb = (pa * utils.inv(pb, p)) % p
    return rab == painvpb #Condition to check

def perform(socket, g_1, p, shared_secret):
    print('Performing smp ...')

    # Receive g_1^{a_2} from Alice
    g1_a2 = network.read_int(socket)

    # Send g_1^{b_2} to Alice
    b2 = generate(p)
    g1_b2 = pow(g_1, b2, p)
    network.send_int(socket, g1_b2)

    #Read ack/nack
    network.make_sure_ack(socket)

    # Receive g_1^{a_3} from Alice
    g1_a3 = network.read_int(socket)

    # Send g_1^{b_3} to Alice
    b3 = generate(p)
    g1_b3 = pow(g_1, b3, p)
    network.send_int(socket, g1_b3)

    #Read ack/nack
    network.make_sure_ack(socket)

    # Compute g2, g3
    g_2, g_3 = compute_g1_g2(g_1, g1_a2, b2, g1_a3, b3, p)

    # Compute P_b, Q_b
    b = generate(p)
    pb, qb = compute_pb_qb(g_1, g_2, g_3, b, p, shared_secret)

    # Receive P_a
    pa = network.read_int(socket)

    # Send P_b
    network.send_int(socket, pb)

    # Receive ack/nack
    network.make_sure_ack(socket)

    # Receive Q_a
    qa = network.read_int(socket)

    # Send Q_b
    network.send_int(socket, qb)

    # Receive ack/nack
    network.make_sure_ack(socket)

    # Receive qaqb
    ra = network.read_int(socket)

    # Compute rb and send rb
    rb = compute_rb(qa, qb, b3, p)
    network.send_int(socket, rb)

    # Receive ack/nack
    network.make_sure_ack(socket)
    network.make_sure_ack(socket)

    return check_x_equal_y(ra, b3, pa, pb, p)
