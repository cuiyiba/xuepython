'''
1.实现输入10个数字，并打印10个数的求和结果
2.从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
3.使用random模块，如何产生 50~150之间的数？
4.从键盘输入任意三边，判断是否能形成三角形，
    若可以，则判断形成什么三角形
    （结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
import random
# 1.实现输入10个数字，并打印10个数的求和结果
# b=0
# shu=[12,3,22,45,11,56,1,44,33,56]
# for i in range(len(shu)):
#     b=b+shu[i]
# print(b)
#2.从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# print("输入10次数字")
# i=0
# b=0
# shu2=[]
# while i<10:
#     i=i+1
#     date = int(input("开始："))
#     shu2.append(date)
# for c in range(len(shu2)):
#     b=b+shu2[c]
# for d in shu2:
#     d = max(shu2)
# print(shu2)
# print("和",b)
# print("平均",b/len(shu2))
# print("最大数",d)
#3.使用random模块，如何产生 50~150之间的数？
# Ran=random.randint(50,150)
# # print(Ran)
# 4.从键盘输入任意三边，判断是否能形成三角形，
#  若可以，则判断形成什么三角形
# （结果判断：等腰，等边，直角，普通，不能形成三角形。）
# print("请输入数字")
# i=0
# a=0
# b=0
# c=0
# shu3=[]
# while i<3:
#     i=i+1
#     san=int(input("输入"))
#     shu3.append(san)
# print(shu3)
# # for i in range(len(shu3)):
# #     print(shu3[i])
# a=shu3[0]
# b=shu3[1]
# c=shu3[2]
# print(a,b,c)
# if a+b>c & a+c>b & b+c>a:
#      print("普通三角形")
#
# elif a==b | b==c | c==a:
#     print("等腰三角形")
# elif a==b==c:
#     print("等边三角形")
# else:
#     print("不构成三角形")
# 5有以下两个数，使用+，-号实现两个数的调换。
# a=56
# b=78
# def demo3(a,b):
#     a = a + b
#     b = a - b
#     a = a - b
#     prin,t(a,b)
# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# i=0
# while i <3:
#     i=i+1
#     yong = input("用户名")
#     mi = input("密码")
#     print(type(mi))
#     if yong == "root" and mi=="admin":
#         print("正确")
#         break
#     else:
#         print("用户名或密码错误，还有",3-i,"次机会")
#     print("系统锁定")
#编程实现下列图形的打印
# xing =["*","**","***","****","*****","******","*******"]
# for xin in range(len(xing)):
#     print(xing[xin])

# 使用while循环实现NxN乘法表的打
# i=1#行控制
# while i<=9:
#     j = 1#列控制
#     while j<=i:
#         print("%dx%d=%d"%(j,i,i*j),end=' ')
#         j=j+1
#     print(' ')
#     i+=1
# #编程实现99乘法表的倒叙打印
# for x in range(9,0,-1):
#     for y in range(x,0,-1):
#         print("%2d x%2d = %2d"%(x,y,x*y),end='\t')
#     print()
# 一只青蛙掉在井了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# j=20
# b=3
# w=2
# i=b-w
# while i<=j:
#   print(j/(b-w))
# 继续完成上午的猜数字游戏的需求功能。
# 1.添加计数打印功能
# 2.添加次数金币功能和锁定系统功能。
# print("猜数字：请输入0~100的正整数")
# print("起始金额5000 猜对一次给300 猜错扣除100 猜错15次结束")
# #次数
# i=0
# # 初始金额
# amount = 5000
# # 随机数
# Ran = random.randint(1, 100)
#循环
# while i<15:
#     i=i+1#次数加一
#     num=input("输入数字开始：")
#     num=int(num)
#     if 0< num < Ran:
#         print("小了")
#         amount=amount-100
#     elif 100>num > Ran:
#         print("大了")
#         amount=amount-100
#     elif num == Ran:
#         print("对了")
#         amount=amount + 300
#         print("剩余金额：", amount)
#         continue
#     else:
#         print("您输入的数字不合法，游戏将重新开始：请遵守游戏规则")
#         break
#     print("剩余金额：", amount,"剩余次数：", 15 - i)
#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20
# num=20
# fac = 1
# for i in range(1, num + 1):
#     fac = fac * i
# print( num, " 的阶乘是：", fac)