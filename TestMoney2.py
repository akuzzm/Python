import unittest

from Money import Atm

class TestMoney(unittest.TestCase):
    def setUp(self):
        self.sal_1= Atm(ask_money=1000, exist_money=9000)
        self.sal_2= Atm(ask_money=10000, exist_money=9000)
        self.sal_3= Atm(ask_money=0, exist_money=9000)
        self.sal_4= Atm(ask_money=-100, exist_money=9000)
        
    def test_pos_flow(self):
        self.assertEqual(1000, self.sal_1.get_money())

    def test_neg_flow(self):
        self.assertIsNone(self.sal_2.get_money())

    def test_zero_flow(self):
        self.assertEqual(0, self.sal_3.get_money())

    def test_minus_flow(self):
        self.assertEqual(-100, self.sal_4.get_money()) 

if __name__=="__main__":
    unittest.main()

