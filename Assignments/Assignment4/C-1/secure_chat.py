import format_converter as fc
import network

__author__ = "Marcus Rodan & Niklas Jönsson"

def send_message(socket, msg_hex, key):
    msg_int = int(msg_hex, 16)

    enc = msg_int ^ key
    network.send_int(socket, enc)

    return network.read_hex(socket)
