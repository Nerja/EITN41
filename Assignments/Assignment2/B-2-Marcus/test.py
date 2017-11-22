import unittest
import reader
import main

class TestConverter(unittest.TestCase):
    def test_reader(self):
        target  = [{'src':'13.43.13.123', 'dst':'85.123.34.1'}, {'src':'45.14.153.12', 'dst':'198.12.155.62'}]
        file    = 'test.pcap'
        self.assertEqual(target, reader.read_data(file))

    def test_case1(self):
        ans = main.attack_comm_sum('159.237.13.37', '94.147.150.188', 2, 'cia.log.1337.pcap')
        self.assertEqual(6100595791, ans)

    def test_case2(self):
        ans = main.attack_comm_sum('161.53.13.37', '11.192.206.171', 12, 'cia.log.1339.pcap')
        self.assertEqual(28979912646, ans)

if __name__ == "__main__":
    unittest.main()
