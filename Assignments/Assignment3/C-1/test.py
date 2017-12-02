import unittest
import main

class TestConverter(unittest.TestCase):
    #https://www.iasj.net/iasj?func=fulltext&aId=97260
    def test_encrypt(self):
        self.assertEqual(26118, main.encrypt(188, 100, 97, 187))

    #https://www.iasj.net/iasj?func=fulltext&aId=97260
    def test_decrypt(self):
        self.assertEqual(100, main.decrypt(26118, 80, 187, 180))

    def test_compute_lambda(self):
        self.assertEqual(80, main.compute_lambda(11, 17))

    def test_compute_mu(self):
        self.assertEqual(180, main.compute_mu(188, 80, 187))

    #http://security.hsr.ch/msevote/seminar-papers/HS09_Homomorphic_Tallying_with_Paillier.pdf
    def test_other_decrypt(self):
        self.assertEqual(15232, main.decrypt(2747997353, 31536, 126869, 53022))

    def test_other_compute_lambda(self):
        self.assertEqual(31536, main.compute_lambda(293, 433))

    def test_other_compute_mu(self):
        self.assertEqual(53022, main.compute_mu(6497955158, 31536, 126869))

    def test_testquiz_case(self):
        #note n = 1643107 so 1643107 -> 1643104 means -3!
        self.assertEqual(1643104, main.run_instance(1117, 1471, 652534095028, 'test_quiz_votes'))

    def test_instr_case(self):
        #note n = 1643107 so 1643107 -> 1643104 means -3!
        self.assertEqual(32, main.run_instance(5, 7, 867, 'test_instr_votes'))

    def test_instr_case(self):
        #note n = 1643107 so 1643107 -> 1643104 means -3!
        self.assertEqual(1643102, main.run_instance(1117, 1471, 652534095028, 'test_live_quiz_marcus_votes'))

if __name__ == "__main__":
    unittest.main()
