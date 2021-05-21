import unittest
from calc import Cala
from ddt import ddt
from ddt import data
from ddt import unpack

# 创建数据源
da = [
    [1, 2, 3],
    [-3, 3, 0],
    [3, -3, 0],
    [-3, -3, -6]
]
@ddt  # 将测试类用@ddt修饰
class TestAdd(unittest.TestCase):

    @data(*da)  # 引入数据源
    @unpack     # 将数据源的数据进行解包，不然的话会当成一个整数传进来
    def test_Add(self,a,b,c): # abc每组数据三个元素，c是期望结果
        cala = Cala()
        sum = cala.Add(a,b)
        self.assertEqual(c,sum)

