import unittest
import main

class TestConverter(unittest.TestCase):
    def test_secret_lagrange(self):
        #Point for participant 1 is obtained by summing f(1) = f_1(1) + f_2(1) + f_3(1) + ...
        points = [(2, 2782), (4, 30822), (5, 70960), (7, 256422), (1, 468)]
        self.assertEqual(110.0, main.find_secret(points))

    def test_instr(self):
        k                       = 5
        n                       = 8
        your_idx                = 1
        your_poly               = [13, 8, 11, 1, 5]
        received_points         = [75, 75, 54, 52, 77, 54, 43]
        received_master_points  = [(2, 2782), (4, 30822), (5, 70960), (7, 256422)]
        self.assertEqual(110, main.run_instance(k, n, your_idx, your_poly, received_points, received_master_points))

    def test_testQ1(self):
        k                       = 4
        n                       = 6
        your_idx                = 1
        your_poly               = [20, 20, 11, 6]
        received_points         = [63, 49, 49, 54, 43]
        received_master_points  = [(3, 2199), (4, 4389), (6, 12585)]
        self.assertEqual(93, main.run_instance(k, n, your_idx, your_poly, received_points, received_master_points))

    def test_testQ2(self):
        k                       = 5
        n                       = 6
        your_idx                = 1
        your_poly               = [20, 18, 13, 19, 15]
        received_points         = [34, 48, 45, 39, 24]
        received_master_points  = [(2, 1908), (3, 7677), (5, 50751), (6, 101700)]
        self.assertEqual(36, main.run_instance(k, n, your_idx, your_poly, received_points, received_master_points))

    def test_testQ3(self):
        k                       = 3
        n                       = 6
        your_idx                = 1
        your_poly               = [9, 19, 5]
        received_points         = [37, 18, 40, 44, 28]
        received_master_points  = [(4, 1385), (5, 2028)]
        self.assertEqual(53, main.run_instance(k, n, your_idx, your_poly, received_points, received_master_points))

if __name__ == "__main__":
    unittest.main()
