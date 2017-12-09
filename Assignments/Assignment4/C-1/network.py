import socket

__author__ = "Marcus Rodan & Niklas Jönsson"

def get_connection():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("eitn41.eit.lth.se", 1337))
    return soc

def read_int(socket):
    return int(socket.recv(4096).decode('utf-8').strip(), 16)

def send_int(socket, nbr):
    socket.send(format(nbr, 'x').encode('utf-8'))

def read_hex(socket):
    return socket.recv(4096).decode('utf-8').strip()

def read_status(socket):
    return socket.recv(4096).decode('utf8').strip()

def make_sure_ack(socket):
    if read_status(socket) != 'ack':
        print("Response was nack")
        sys.exit()
    else:
        print("ack")
