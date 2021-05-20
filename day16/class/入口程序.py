'''
    使用测试集来进行测试：

'''

import unittest
from HTMLTestRunner  import  HTMLTestRunner

# 1.创建测试集
suite = unittest.TestSuite()
# 2.让测试加载器自己加载所用用例
tests = unittest.defaultTestLoader.discover(r"E:\ytk\develop\works\python\class\day16\class",pattern="Test*.py")
# 3.将所用例 放入测试集
suite.addTests(tests)
# 4.创建测试运行器
f = open(file="银行系统测试报告.html",mode="w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title = "这是一个银行系统测试报告！",
    verbosity=3,
    description="执行了开户、存钱、取钱、转账、查询用例"
)
# 5.让运行器生成测试报告
runner.run(suite)
