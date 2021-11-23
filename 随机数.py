'''
随机数
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，猜小了
起始金额  5000 才对一次给300 猜错扣除100 猜错15次结束
'''

import random
print("猜数字：请输入0~100的正整数")
print("起始金额5000 猜对一次给300 猜错扣除100 猜错15次结束")
#次数
i=0
# 初始金额
amount = 5000
#循环
while i<15:
    i=i+1#次数加一
    # 随机数
    Ran = random.randint(1, 100)
    num=input("开始：")
    num=int(num)
    if num < Ran:
        print("小了")
        amount=amount-100
    elif num > Ran:
        print("大了")
        amount=amount-100
    elif num == Ran:
        print("对了")
        amount=amount + 300
    else:
        print("您输入的数字不合法")
        break
    print("剩余金额：", amount)
    print("剩余次数：", 15 - i)

