
import unittest
from calc import Cala
class TestCalc(unittest.TestCase): #类就是单元测试类的子类

    def test_Add1(self):
        # 准备数据
        a = 3
        b = 4

        c = 7 # 期望结果

        # 调用被测方法
        cala = Cala()
        sum = cala.Add(a,b)

        # 断言
        self.assertEqual(c,sum)
