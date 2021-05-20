import unittest
from util.User import User
from util.Bank import Bank

class TestWithdrawal(unittest.TestCase):
    user = None
    bank = None

    def setUp(self) -> None:
        self.user = User()
        self.bank = Bank()

    def test_Withdrawal1(self):
        # 1.准备数据
        self.user.setAccount("qqqqqqq4")
        self.user.setPassword("123456")
        self.bank.setMoney("100")

        # 2.预期结果
        teststart = 0

        # 3.调用被测试方法
        start = self.bank.bank_withdrawal(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())

        # 4.断言
        self.assertEqual(teststart,start)

    def test_Withdrawal2(self):
        # 1.准备数据
        self.user.setAccount("qqqqqqq5")
        self.user.setPassword("123456")
        self.bank.setMoney("100")

        # 2.预期结果
        teststart = 1

        # 3.调用被测试方法
        start = self.bank.bank_withdrawal(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())

        # 4.断言
        self.assertEqual(teststart,start)

    def test_Withdrawal3(self):
        # 1.准备数据
        self.user.setAccount("qqqqqqq6")
        self.user.setPassword("333333")
        self.bank.setMoney("100")

        # 2.预期结果
        teststart = 2

        # 3.调用被测试方法
        start = self.bank.bank_withdrawal(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())

        # 4.断言
        self.assertEqual(teststart,start)

    def test_Withdrawal4(self):
        # 1.准备数据
        self.user.setAccount("qqqqqqq7")
        self.user.setPassword("123456")
        self.bank.setMoney("100")

        # 2.预期结果
        teststart = 3

        # 3.调用被测试方法
        start = self.bank.bank_withdrawal(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())

        # 4.断言
        self.assertEqual(teststart,start)