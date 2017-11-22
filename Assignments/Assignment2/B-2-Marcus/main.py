import reader
import sys
import format_converter as fc

__author__ = "Marcus Rodan & Niklas Jönsson"

def find_R(nazir_ip, mix_ip, m, pcap_file):
    R_list          = []
    nazir_sending   = False
    current_ri      = []

    for packet in reader.read_data(pcap_file):
        if not packet['src'] == mix_ip and current_ri:
            R_list += [set(current_ri)]
            current_ri = []
            nazir_sending = False

        if packet['dst'] == mix_ip and packet['src'] == nazir_ip:
            nazir_sending = True
        elif packet['src'] == mix_ip and nazir_sending:
            current_ri += [packet['dst']]

    return R_list

def set_is_disjoint(sets, set_i):
    return all([s.isdisjoint(set_i) for s in sets])

def distinct_sets_size_one(distinct_sets):
    return all([len(s) == 1 for s in distinct_sets])

def find_distinct(R):
    distinct = []
    for ri in R:
        if set_is_disjoint(distinct, ri):
            distinct += [ri]
    return distinct

def learn(nazir_ip, mix_ip, m, pcap_file):
    R_list          = find_R(nazir_ip, mix_ip, m, pcap_file)
    R_distinct      = find_distinct(R_list)
    return R_distinct, [e for e in R_list if not e in R_distinct]

def exclude(R_distinct, R_list):
    while not distinct_sets_size_one(R_distinct) and R_list:
        picked_R = R_list[0]
        R_list   = R_list[1:]

        RRi_intersection    = set()
        match_cnt           = 0
        match_i             = 0
        for i in range(len(R_distinct)):
            ri = R_distinct[i]
            if not ri.isdisjoint(picked_R):
                match_i             = i
                match_cnt           = match_cnt + 1
                RRi_intersection    = ri.intersection(picked_R)
        if match_cnt == 1:
            R_distinct = R_distinct[:match_i] + [RRi_intersection] + R_distinct[(match_i+1):]

    return [list(p)[0] for p in R_distinct] if distinct_sets_size_one(R_distinct) else None

def attack(nazir_ip, mix_ip, m, pcap_file):
    R_distinct, R_list  = learn(nazir_ip, mix_ip, m, pcap_file)
    comm_partners       = exclude(R_distinct, R_list)
    return comm_partners

def ip_to_int(ip):
    return fc.hex_to_int(fc.ip_to_hex(ip))

def attack_comm_sum(nazir_ip, mix_ip, m, pcap_file):
    comm_partners = attack(nazir_ip, mix_ip, m, pcap_file)
    return None if comm_partners == None else sum(map(ip_to_int, comm_partners))

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Arguments should be Nazir's ip, Mix ip, number parterns, pcap file")
        sys.exit()

    nazir_ip    = sys.argv[1]
    mix_ip      = sys.argv[2]
    m           = int(sys.argv[3])
    pcap_file   = sys.argv[4]
    print("Using nazir_ip={}, mix_ip={}, m={}, pcap={}".format(nazir_ip, mix_ip, m, pcap_file))

    comm_sum = attack_comm_sum(nazir_ip, mix_ip, m, pcap_file)
    if not comm_sum == None:
         print("Sum of IPs: {}".format(comm_sum))
