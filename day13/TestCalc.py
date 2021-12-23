'''
    TestCase
    ddt:
        data  driver test:数据驱动测试
    1.ddt
    2.data
    3.unpack
'''
from unittest import  TestCase
from ddt import  ddt
from ddt import data
from ddt import  unpack
from Calc import Calc
import xlrd
from xlwt import Workbook
from xlutils.copy import  copy

# 任务一：xlrd，读取参数化数据
# da = xlrd.read()

def readData():
    li = []
    wb = xlrd.open_workbook(filename="calc.xls", encoding_override=True)
    st = wb.sheet_by_index(0)
    cols = st.ncols
    rows = st.nrows
    for i in range(1,rows):# 第一行属于表头数据，肯定不要，从第二行开始读取数据
        l = []
        for j in range(0,cols-3):
            l.append(st.cell_value(i,j))
        li.append(l)

    return li
#读写文件的方法
def writeData(row,col,data):
    #读文件
    new_wb = copy(xlrd.open_workbook(filename="calc.xls",encoding_override=True))
    #获取文件内容
    new_wb.get_sheet(0).write(row,col,data)
    #写入
    new_wb.save("calc.xls")


@ddt
class TestCalc(TestCase):

    @data(*readData())
    @unpack
    def testAdd1(self,d,a,b,c):
        calc = Calc()

        s = calc.add(a,b)

        if s == c:
            writeData(d,4,"成功！")
        else:
            writeData(d,4,"失败！")
        self.assertEqual(s,c)



















