from unittest import TestCase

import xlrd
import xlwt
from ddt import ddt
from ddt import data
from ddt import unpack
from 工商银行完整版 import bank_addUser
import os

#username,password,country,province,street,door,money
# da =  [
#     ["jason","admin","cn","安徽省","桃源路","s001",5600,1],
#     ["jason", "admin", "cn", "安徽省", "桃源路", "s001", 5600, 2]
# ]
# da = xlrd.read()  # 参数化数据用文件参数化
da = xlrd.open_workbook(r"F:\Python-work\xuepython\hankeruan\day13\计算器数据.xlsx")

@ddt
class TestBank(TestCase):
    @data(*da)
    @unpack
    def testAddUser(self,a,b,c,d,e,f,g,h):
        s = bank_addUser(a,b,c,d,e,f,g)
        if s == h:  # 测试结果回写到excle表里
            xlwt.write(1,3,"成功！")
        else:
            xlwt.write(1,3,"失败！")
        self.assertEqual(s,h)






