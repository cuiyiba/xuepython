'''
生成一个指定长度的验证码，验证码由英文字大小写和数字组成。
双色球选号：
1、双色球由7个两位数组成 前六个范围是1-33，第七个是1-15
(2)后一个比第一个数字大，第七个数字随机
2、键盘输入一个数字，就打印几个几组号码
打印杨辉三角形
'''
from random import randrange, randint, sample
import random

# 成一个指定长度的验证码，验证码由英文字大小写和数字组成。
# def generate_code(code_len):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#     	index = random.randint(0, last_pos)
#     	code += all_chars[index]
#     return code
#
# if __name__=='__main__':
# 	print(generate_code(5))
# 双色球
# 生成6个不重复的红色球号码
# 制作一个号码池，里面有33个数
numbers = []
number = 1
while number < 34:
    numbers.append(number)
    number += 1

#从号码池中取出6个不重复的数字
computer_redballs = []
count = 1
while count <= 6:
    index = random.randint(0, len(numbers) - 1)
    number = numbers[index]
computer_redballs.append(number)
del numbers[index]
count += 1

# 在显示的时候，按照升序进行显示：computer_redballs.sort()
print("红色球号码为：{}".format(computer_redballs))

#生成1个蓝色球号码
computer_blueball = random.randint(1, 16)
print("蓝色球号码为：{}".format(computer_blueball))

#显示计算机生成的双色球号码
print("双色球号码为：{}+".format(computer_redballs), end="")
print("[{}]".format(computer_blueball))

#用户输入一注双色球号码
user_redballs = []
user_blueball = 0
count = 1
while True:
    if len(user_redballs) == 6:
        break
    user_number = input("请输入第{}个红色号码：".format(count))
    if not user_number.isdigit():
        print("你输入的不是数字，请重新输入！")
        continue
    user_number = int(user_number)
    if user_number < 1 or user_number > 33:
        print("你输入的数字超出范围，请重新输入！")
        continue
    if user_number in user_redballs:
        print("该数字已经存在，请重新输入！")
        continue
user_redballs.append(user_number)
count += 1
user_redballs.sort()

while True:
    if user_blueball != 0:
        break
    user_number = input("请输入蓝色球号码：")
    if not user_number.isdigit():
        print("你输入的不是数字，请重新输入！")
        continue
    user_number = int(user_number)
    if user_number < 1 or user_number > 16:
        print("你输入的数字超出范围，请重新输入！")
    continue
user_blueball = user_number
print("用户输入的双色球号码是：{}+[{}]".format(user_redballs, user_blueball))

#判断用户中了几等奖
count = 0
for number in user_redballs:
    if number in computer_redballs:
        count += 1
if count == 6 and user_blueball == computer_blueball:
    print("一等奖")
elif count == 6:
    print("二等奖")
elif count == 5 and user_blueball == computer_blueball:
    print("三等奖")
elif count == 5 or count == 4 and user_blueball == computer_blueball:
    print("四等奖")
elif count == 4 or count == 3 and user_blueball == computer_blueball:
    print("五等奖")
elif user_blueball == computer_blueball:
    print("六等奖")
else:
    print("没中奖，欢迎下次光临！")

print("程序结束")

# 杨辉三角
# num=input('请输入行数：')
# num =int(num)
#
# list1 =[] #list 用来保存杨辉三角
# for n in range(num):
#   row =[1] #保存行
#   list1.append(row)
#
#   if n ==0:
#     print(row)
#     continue
#   for m in range(1,n):
#     row.append(list1[n - 1][m - 1] + list1[n - 1][m])
#   row.append(1)
#
#   print(row)
