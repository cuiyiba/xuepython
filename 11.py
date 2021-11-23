'''
服装商城


'''
print ("===========================服装商城==============================")
print ("日期     服装名称        价格/件       库存      销售数量/每日")
print ("1号      羽绒服          253.6       500       10")
print ("2号	     牛仔裤	        86.3	    600	      60")
'''
总销售额
'''
amunt = (253.6*10+86.3*60)
print("总金额：",amunt)
#print()

#平均值
average = ((253.6*10+86.3*60)/2)
print("日均金额：",average)
#print()

#种类月销售量占比

ku = 253.6*10
kupercentage = ku/amunt
sy = 86.3*60
sypercentage = sy/amunt
print("裤子占比：",kupercentage*100,"%")
print("上衣占比：",sypercentage*100,"%")
#print(sypercentage)