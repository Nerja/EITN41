#!/usr/bin/env python

from pcapfile import savefile

testcap = open('cia.log.1337.pcap', 'rb')
capfile = savefile.load_savefile(testcap, layers=2, verbose=True)
nazir_ip = '159.237.13.37'
mix_ip = '94.147.150.188'
# print the packets
last_ip_src = 0
last_ip_dst = 0
print ('timestamp\t\t\tIP src\t\tIP dst')
for pkt in capfile.packets:

    timestamp = pkt.timestamp

    ip_src = pkt.packet.payload.src.decode('UTF8')
    ip_dst = pkt.packet.payload.dst.decode('UTF8')

    if ip_src == nazir_ip:
        print("Originating from NAZIR:")
    if ip_src == mix_ip and not ip_src == last_ip_src:
        print("New batch of outgoing messages from mix")
    elif ip_dst == mix_ip and not ip_dst == last_ip_dst:
        print("New batch of incoming messages to mix")

    print ('{}\t\t\t{}\t\t{}'.format(timestamp, ip_src, ip_dst))
    last_ip_src = ip_src
    last_ip_dst = ip_dst
