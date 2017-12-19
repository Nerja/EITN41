import unittest
import main
import random
from Crypto.Util.asn1 import DerInteger
from binascii import hexlify, unhexlify

class TestConverter(unittest.TestCase):
    def test_int_encoder_ins1(self):
        self.assertEqual("02050096d25da9", main.encode_integer_tlv(2530368937))

    def test_int_encoder_big_nbr(self):
        self.assertEqual("024100dcbb40d01f3200be66b31fb0a18ccfd0b424bb8d533efa658bfdc0e9b030bd765460da58a8da83bbcc2c5784827d5aba9861f1e9b619024caf7990dd5043356d", main.encode_integer_tlv(11560644488956558465532853024584920642928395423043331532508618875895021559945470153413748278878428620858516734437220921970550558146862545776998622207096173))

    def test_int_encoder_liveq(self):
        k = 141200904527031427693111569572085332763291092089246046288015799505524112848666951727490655634310664507006287247690643568683363763333057271478359004846665350192723231859612961899401338906920115912147935812300211873100787356909246033420333758668256600284274201300130421437978238102757977633689474423065331072603
        corr_ans = str(hexlify(DerInteger(k).encode()))[2:][:-1]
        print("\n\n" + main.encode_integer_tlv(k) + "\n\n")
        self.assertEqual(corr_ans, main.encode_integer_tlv(k))

    def test_int_encoder_big_test(self):
        for i in range(1000):
            k = random.randint(0, 1000 ** 1000)
            corr_ans = str(hexlify(DerInteger(k).encode()))[2:][:-1]
            imp_ans = main.encode_integer_tlv(k)
            self.assertEqual(corr_ans, imp_ans)

    def test_encode_key_ins(self):
        p = 2530368937
        q = 2612592767
        e = 65537
        self.assertEqual("MDwCAQACCFu+XQXUfXbXAgMBAAECCDZpw5W5z3MhAgUAltJdqQIFAJu5AH8CBHgJdgECBFlLQGkCBFjc97Q=", main.encode_key(p, q, e))

    def test_encode_key_testq(self):
        p = 139721121696950524826588106850589277149201407609721772094240512732263435522747938311240453050931930261483801083660740974606647762343797901776568952627044034430252415109426271529273025919247232149498325412099418785867055970264559033471714066901728022294156913563009971882292507967574638004022912842160046962763
        q = 141482624370070397331659016840167171669762175617573550670131965177212458081250216130985545188965601581445995499595853199665045326236858265192627970970480636850683227427420000655754305398076045013588894161738893242561531526805416653594689480170103763171879023351810966896841177322118521251310975456956247827719
        e = 65537
        fexp = open('exptq')
        expans = fexp.read().strip()
        fexp.close()
        self.assertEqual(expans, main.encode_key(p, q, e))

if __name__ == "__main__":
    unittest.main()