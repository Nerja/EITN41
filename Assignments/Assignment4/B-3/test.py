import unittest
import main

class TestConverter(unittest.TestCase):
    def test_int_to_hex(self):
        self.assertEqual("18a65e36189833d99e55a68dedda1cce13a494c947817d25dc80d9b4586a", main.MGF1("0123456789abcdef", 30))
    def test_i2osp(self):
        self.assertEqual([0, 0, 5, 57], list(main.I2OSP(1337, 4)))

    def test_encode(self):
        self.assertEqual("0000255975c743f5f11ab5e450825d93b52a160aeef9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51f40e13fb29ed5101dbcb044e6232e6371935c8347286db25c9ee20351ee82",
        main.OAEP_encode("fd5507e917ecbe833878", "1e652ec152d0bfcd65190ffc604c0933d0423381"))

    def test_decode(self):
        self.assertEqual("fd5507e917ecbe833878", main.OAEP_decode("0000255975c743f5f11ab5e450825d93b52a160aeef9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51f40e13fb29ed5101dbcb044e6232e6371935c8347286db25c9ee20351ee82"))
if __name__ == "__main__":
    unittest.main()
