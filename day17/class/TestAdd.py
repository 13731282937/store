import xlrd
import unittest
from calc import Cala
from ddt import ddt
from ddt import data
from ddt import unpack
class Excel:
    # 1.获取工作簿
    wb = xlrd.open_workbook(filename="D:\python自动化测试技术\classtest\da.xlsx",encoding_override=True)
    # 2.通过wb获取选项卡
    sheet = wb.sheet_by_name("Add")
    # 3.获取行列数据
    rows = sheet.nrows
    ncols = sheet.ncols
    da = []
    for i in range(rows):
        data = sheet.row_values(i)
        da.append(data)

e = Excel()
da = e.da
@ddt
class TestAdd(unittest.TestCase):
    @data(*da)  # 引入数据源
    @unpack     # 将数据源的数据进行解包，不然的话会当成一个整数传进来
    def test_Add(self,a,b,c): # abc每组数据三个元素，c是期望结果
        cala = Cala()
        sum = cala.Add(a,b)
        self.assertEqual(c,sum)

