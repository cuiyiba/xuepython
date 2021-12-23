from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")


runner = HTMLTestRunner.HTMLTestRunner(
    title = "银行和计算器的测试报告",
    description="银行开户和计算器加法测试报告",
    verbosity=1,
    stream=open(file="bank_calc.html",mode="w+",encoding="utf-8")
)

runner.run(tests)




