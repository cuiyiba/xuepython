'''

计算器类（包含加减乘除）

'''

#加
def add(x,y):
    return x+y
#减
def subtract(x,y):
    return x-y
#乘
def multiply(x,y):
    return x*y
#除
def divide(x,y):
    return x/y

while True:
    # 用户输入
    print ("选择运算：")
    print ("1、相加")
    print ("2、相减")
    print ("3、相乘")
    print ("4、相除")
    print ("5、退出")

    choice = input ("输入你的选择(1/2/3/4):")
    choice=int(choice)
    if choice==5:
        print("退出")
        quit()
    num1 = int (input ("输入第一个数字: "))
    num2 = int (input ("输入第二个数字: "))
    if choice==1:
        print(num1,"加",num2,"=",add(num1,num2))
    elif choice==2:
        print (num1, "减", num2, "=", subtract (num1, num2))
    elif choice==3:
        print (num1, "乘", num2, "=", multiply (num1, num2))
    elif choice==4:
        print (num1, "除", num2, "=", divide (num1, num2))
    else:
        print("数字不合法，请重新输入")
        continue












