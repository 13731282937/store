import unittest
from util.User import User
from util.Address import Address
from util.Bank import Bank
class TestAddUser(unittest.TestCase):
    user = None
    address = None
    bank = None
    def setUp(self) -> None:
        self.user = User()
        self.address = Address()
        self.bank = Bank()

    def test_adduser1(self):
        # 1.准备测试数据
        self.user.setAccount("qqqqqqq1")
        self.user.setPassword("123456")
        self.user.setUsername("q1")
        self.address.setCounrry("中国")
        self.address.setProvince("北京")
        self.address.setStreet("幸福路")
        self.address.setDoor("46")

        # 2. 预期结果
        teststart = 1

        # 3.调用被测方法
        start = self.bank.bank_addUser(self.user.getAccount(),self.user.getUsername(),self.user.getPassword(),self.address.getCounrry(),self.address.getProvicne(),self.address.getStreet(),self.address.getDoor())

        # 4.断言
        self.assertEqual(teststart,start)


    def test_adduser2(self):
        # 1.准备测试数据
        self.user.setAccount("0tqr0d3c")
        self.user.setPassword("123456")
        self.user.setUsername("q1")
        self.address.setCounrry("中国")
        self.address.setProvince("北京")
        self.address.setStreet("幸福路")
        self.address.setDoor("46")

        # 2. 预期结果
        teststart = 2

        start = self.bank.bank_addUser(self.user.getAccount(), self.user.getUsername(), self.user.getPassword(),
                                               self.address.getCounrry(), self.address.getProvicne(),
                                               self.address.getStreet(), self.address.getDoor())
        # 3.断言
        self.assertEqual(teststart, start)

