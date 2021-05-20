import unittest
from util.User import User
from util.Bank import Bank

class TestTransfer(unittest.TestCase):
    user = None
    bank = None

    def setUp(self) -> None:
        self.user = User()
        self.bank = Bank()

    def test_transfer1(self):
        # 1.准备数据
        account1 = "qqqqqqq8"
        account2 = "qqqqqqq9"
        passwork = "123456"
        self.bank.setMoney("100")

        # 2.预期结果
        teststart = 0

        # 3.调用被测方法
        start = self.bank.bank_transfer(account1,account2,passwork,self.bank.getMoney())

        # 4.断言
        self.assertEqual(teststart,start)

    def test_transfer2(self):
        # 1.准备数据
        account1 = "qqqqq110"
        account2 = "qqqqq111"
        passwork = "123456"
        self.bank.setMoney("100")

        # 2.预期结果
        teststart = 1

        # 3.调用被测方法
        start = self.bank.bank_transfer(account1,account2,passwork,self.bank.getMoney())

        # 4.断言
        self.assertEqual(teststart,start)


    def test_transfer3(self):
        # 1.准备数据
        account1 = "qqqqqq10"
        account2 = "qqqqqq11"
        passwork = "124144"
        self.bank.setMoney("100")

        # 2.预期结果
        teststart = 2

        # 3.调用被测方法
        start = self.bank.bank_transfer(account1,account2,passwork,self.bank.getMoney())

        # 4.断言
        self.assertEqual(teststart,start)


    def test_transfer4(self):
        # 1.准备数据
        account1 = "qqqqqq12"
        account2 = "qqqqqq13"
        passwork = "123456"
        self.bank.setMoney("100")

        # 2.预期结果
        teststart = 3

        # 3.调用被测方法
        start = self.bank.bank_transfer(account1,account2,passwork,self.bank.getMoney())

        # 4.断言
        self.assertEqual(teststart,start)



