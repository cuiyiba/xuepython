'''

测试类

'''
from unittest import TestCase
import xlrd
from ddt import data
from ddt import ddt
from ddt import unpack

# from filerw import filerw
from zhuce import zhuce


@ddt
class testHkr:
    li=[]
    workbook = xlrd.open_workbook (r"F:\汉科软\python\day17自动化测试\HKR.xlsx")
    st=workbook.sheet_by_index(0)
    cols = st.ncols
    rows = st.nrows
    for i in range (1, rows):  # 第一行属于表头数据，肯定不要，从第二行开始读取数据
        l = []
        for j in range (0, cols - 3):
            l.append (st.cell_value (i, j))
        li.append (l)

    @data (*st)
    @unpack
    def testHkr(self, uname, pwd, email, phone, q):
        ze = zhuce.TestZhuce (uname, pwd, email, phone)
        self.assertEqual(q,ze)