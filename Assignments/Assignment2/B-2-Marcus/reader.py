from pcapfile import savefile

__author__ = "Marcus Rodan & Niklas Jönsson"

# Format is (src, dst)
def extract_ips(p):
    ip_src = p.packet.payload.src.decode('UTF8')
    ip_dst = p.packet.payload.dst.decode('UTF8')
    return {'src':ip_src, 'dst':ip_dst}

def read_data(file):
    file_data = open(file, 'rb')
    capfile = savefile.load_savefile(file_data, layers=2, verbose=True)
    file_data.close()
    return list(map(extract_ips, capfile.packets))
