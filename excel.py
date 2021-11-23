import xlrd
workbook=xlrd.open_workbook(r'C:\Users\cuiyi\Desktop\汉科软\python\day1\任务\12月份衣服销售数据.xlsx')
print (workbook.sheet_names())
sheet2=workbook.sheet_by_name('A','B','C','D','E')
nrows=sheet2.nrows
ncols=sheet2.ncols

print(nrows,ncols)
cell_A=sheet2.cell(1,1).value
print(cell_A)