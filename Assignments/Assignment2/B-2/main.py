__author__ = "Niklas Jönsson & Marcus Rodan"

from pcapfile import savefile

def main(nazir_ip, mix_ip, nbr_partners, data):
    testcap = open(data, 'rb')
    capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

    # print the packets
    #print ('timestamp\teth src\t\t\teth dst\t\t\tIP src\t\tIP dst')
    learn(nazir_ip, capfile, nbr_partners)

    #print ('{}\t\t{}\t{}\t{}\t{}'.format(timestamp, eth_src, eth_dst, ip_src, ip_dst))


def learn(nazir_ip, data, m):
    for pkt in data.packets:
        timestamp = pkt.timestamp
        # all data is ASCII encoded (byte arrays). If we want to compare with strings
        # we need to decode the byte arrays into UTF8 coded strings
        eth_src = pkt.packet.src.decode('UTF8')
        eth_dst = pkt.packet.dst.decode('UTF8')
        ip_src = pkt.packet.payload.src.decode('UTF8')
        ip_dst = pkt.packet.payload.dst.decode('UTF8')

        if ip_src == nazir_ip:
            #look at all ip_dst at a current timestamp and save this to a set
            print ('{}\t\t{}\t{}\t{}\t{}'.format(timestamp, eth_src, eth_dst, ip_src, ip_dst))

if __name__ == "__main__":
    main('159.237.13.37', '94.147.150.188', 2, 'cia.log.1337.pcap')
