__author__ = "Niklas Jönsson & Marcus Rodan"

from pcapfile import savefile
import format_converter as fc

def main(nazir_ip, mix_ip, nbr_partners, data):
    testcap = open(data, 'rb')
    capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

    distinct_outgoing_sets_with_nazir_src, all_outgoing_sets_with_nazir_src = learn(nazir_ip, mix_ip, capfile, nbr_partners)

    ips = exclude(distinct_outgoing_sets_with_nazir_src, all_outgoing_sets_with_nazir_src)

    print("Found the following partners of Nazir:")
    sum = 0
    for ip_set in ips:
        ip = ip_set.pop()
        print("IP: {}".format(ip))
        sum += fc.hex_to_int(fc.ip_to_hex(ip))
    print("Sum of IPs: {}".format(sum))





def learn(nazir_ip, mix_ip, data, m):
    last_ip_src = 0
    last_ip_dst = 0
    mix_outgoing = []
    mix_outgoing_with_nazir_src = []
    found_nazir = 0

    for pkt in data.packets:

        ip_src = pkt.packet.payload.src.decode('UTF8')
        ip_dst = pkt.packet.payload.dst.decode('UTF8')

        if ip_src == nazir_ip:
            found_nazir = 1
        if ip_src == mix_ip:
            if not ip_src == last_ip_src:
                #We got a new batch of outgoing messages
                #if we found nazir src_ip in the incoming messages, this means that
                #some of the outgoing IP is the one he wants to talk with
                if found_nazir:
                    set_i = set(mix_outgoing[len(mix_outgoing) - 1])
                    if set_is_disjoint(mix_outgoing_with_nazir_src, set_i) and len(mix_outgoing_with_nazir_src) < m:
                        mix_outgoing_with_nazir_src.append(set_i)
                    #if got_enough_disjoint_sets(mix_outgoing_with_nazir_src, m):
                    #    break
                    #if len(mix_outgoing_with_nazir_src) == m:
                        #break
                mix_outgoing.append([])
            mix_outgoing[len(mix_outgoing) - 1].append(ip_dst)

        elif ip_dst == mix_ip and not ip_dst == last_ip_dst:
            found_nazir = 0


        last_ip_src = ip_src
        last_ip_dst = ip_dst
    return mix_outgoing_with_nazir_src, mix_outgoing

def set_is_disjoint(sets, set_i):
    for set_j in sets:
        if not set_j.isdisjoint(set_i):
            return False
    return True

def exclude(distinct_sets, all_sets):
    #while distinct_set_sizes_not_one(distinct_sets):
    for set_R in all_sets:
        index_i_union_non_empty = -1
        set_R = set(set_R)
        duplicate = False
        for i in range(len(distinct_sets)):
            #print(set_R)
            #print(distinct_sets[i])
            if not set_R.isdisjoint(distinct_sets[i]):
                if index_i_union_non_empty == -1:
                    index_i_union_non_empty = i
                else:
                    duplicate = True
                    break
        if not duplicate and not index_i_union_non_empty == -1:
            distinct_sets[index_i_union_non_empty] = distinct_sets[index_i_union_non_empty].intersection(set_R)
        if distinct_sets_size_one(distinct_sets):
            break
    print(len(distinct_sets))
    return distinct_sets

def distinct_sets_size_one(distinct_sets):
    for set_i in distinct_sets:
        if not len(set_i) == 1:
            return False
    return True



if __name__ == "__main__":
    main('159.237.13.37', '94.147.150.188', 2, 'cia.log.1337.pcap')
    main('161.53.13.37', '11.192.206.171', 12, 'cia.log.1339.pcap')
