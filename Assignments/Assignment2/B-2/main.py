__author__ = "Niklas Jönsson & Marcus Rodan"

from pcapfile import savefile
import format_converter as fc

def main(nazir_ip, mix_ip, nbr_partners, data):
    testcap = open(data, 'rb')
    capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

    all_sets, distinct_sets = learn(nazir_ip, mix_ip, capfile, nbr_partners)
    ips = exclude(distinct_sets, all_sets)

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

    outgoing_distinct = []
    outgoing_all = []
    all_batches = []
    nazir_in_incoming = 0
    n_count = 0

    for pkt in data.packets:
        ip_src = pkt.packet.payload.src.decode('UTF8')
        ip_dst = pkt.packet.payload.dst.decode('UTF8')

        timestamp = pkt.timestamp
        #We got a new incoming batch, reset nazir_in_incoming
        #Same thing as the last outgoing batch is finished.
        if ip_dst == mix_ip and not ip_dst == last_ip_dst:
            #New incoming batch, if nazir was in our last incoming_batch
            #We should save the current outgoing batch

            if nazir_in_incoming:
                new_set = all_batches[len(all_batches) - 1]
                outgoing_all.append(new_set)
                if len(outgoing_distinct) < m and set_is_disjoint(outgoing_distinct, new_set):
                    outgoing_distinct.append(new_set)

            nazir_in_incoming = 0
        elif ip_src == mix_ip:
            if not ip_src == last_ip_src:
                #We got a new batch of outgoing messages
                all_batches.append(set())
            all_batches[len(all_batches) - 1].add(ip_dst)


        if ip_src == nazir_ip:
            nazir_in_incoming = 1

        last_ip_src = ip_src
        last_ip_dst = ip_dst

    return [e for e in outgoing_all if not e in outgoing_distinct], outgoing_distinct

def set_is_disjoint(sets, set_i):
    return all([s.isdisjoint(set_i) for s in sets])

def exclude(distinct_sets, all_sets):

    #while distinct_set_sizes_not_one(distinct_sets):
    for set_R in all_sets:
        index_i = -1
        duplicate = False
        for i in range(len(distinct_sets)):
            if not set_R.isdisjoint(distinct_sets[i]):
                if index_i == -1:
                    index_i = i
                else:
                    duplicate = True
                    break
        if not duplicate and not index_i == -1:
            distinct_sets[index_i] = distinct_sets[index_i].intersection(set_R)
        if distinct_sets_size_one(distinct_sets):
            break

    return distinct_sets

def distinct_sets_size_one(distinct_sets):
    return all([len(s) == 1 for s in distinct_sets])

if __name__ == "__main__":
    main('159.237.13.37', '94.147.150.188', 2, 'cia.log.1337.pcap')
    main('161.53.13.37', '11.192.206.171', 12, 'cia.log.1339.pcap')
