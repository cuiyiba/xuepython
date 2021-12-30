'''


文件读写类
通过xlrd包对用例进行读写

'''
import xlrd
import xlwt
import zhuce
class filerw():
    workbook=xlrd.open_workbook(r"F:\汉科软\python\day17自动化测试\HKR.xlsx")
    # print(workbook.sheet_names())
    table=workbook.sheet_by_index(0)
    uname=table.row_values(1,0)[0]
    pwd=table.row_values(1,1)[0]
    pwd=int(pwd)
    email=table.row_values(1,2)[0]
    phone=table.row_values(1,3)[0]
    phone=int(phone)
    # zhuce.TestZhuce(uname,pwd,email,phone)
    