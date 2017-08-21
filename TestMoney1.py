import unittest

from Money import Atm

class TestMoney(unittest.TestCase):

    def test_pos_flow(self):
        we_ask_money = 1000
        sal= Atm(ask_money=we_ask_money, exist_money=9000)
        
        self.assertEqual(we_ask_money, sal.get_money())

    def test_neg_flow(self):
        we_ask_money = 10000
        sal= Atm(ask_money=we_ask_money, exist_money=9000)
        
        self.assertIsNone(sal.get_money())

if __name__=="__main__":
    unittest.main()

