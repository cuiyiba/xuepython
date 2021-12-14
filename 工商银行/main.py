from bank import bank
from DBUtils import update
from DBUtils import select

bank = bank ()


# 输入帮助方法：chose是打印选项
def inputHelp(chose, datatype="str"):
    while True:
        print ("请输入", chose, ":")
        i = input (">>>:")
        if len (i) == 0:
            print ("该项不能为空！请重新输入！")
            continue
        if datatype != "str":
            return int (i)
        else:
            return i


while True:

    print ("#######中国工商银行账户管理系统######")
    print ("#        1.添加用户                #")
    print ("#        2.存钱                    #")
    print ("#        3.取钱                    #")
    print ("#        4.转账                    #")
    print ("#        5.查询用户                #")
    print ("#        6.退出                    #")
    print ("###################################")
    su = inputHelp ("请输入数字选择对应业务：")
    su = int (su)
    # 判断键入的数字
    if su == 1:
        print ("****添加用户****")
        username = inputHelp ("用户名")
        password = inputHelp ("密码")
        country = inputHelp ("居住地址：1.国家：")
        province = inputHelp ("省份")
        street = inputHelp ("街道")
        door = inputHelp ("门牌号")
        money = inputHelp ("银行卡余额", "int")
        # 调用银行的开户方法完成开户操作  返回 1 2 3
        status = bank.adduser (username, password, country, province, street, door, money)
        # 判断1   2   3
        if status == 1:
            sql16 = "select * from user where username= %s"
            param16 = username
            data = select (sql16, param16)
            for i in data[0]:
                print (i)
            print ("恭喜开户成功！以上是您的开户信息：")
        elif status == 2:
            print ("该用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
        elif status == 3:
            print ("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")

    elif su == 2:
        print ("****存钱****")
        account = inputHelp ("账号")
        money = inputHelp ("存入的金额", "int")

        flag = bank.chunqian (account, money)

        if flag:
            print ("存储成功!您的个人信息为：")
            sql = "select * from user where getRandom= %s"
            param = account
            data = select (sql, param)
            for i in data[0]:
                print ("\t\t", i)
        else:
            print ("对不起，您的个人信息不存在！请先开户后再次操作！")
    elif su == 3:
        print ("****取钱****")
        account = inputHelp ("账户")
        password = inputHelp ("密码")
        tmoney = inputHelp ("取出金额", "int")

        f = bank.quqian (account, password, tmoney)

        if f == 1:
            print ("该用户不存在！")
        elif f == 2:
            print ("密码错误！")
        elif f == 3:
            print ("取款金额不足！")
        elif f == 0:
            print ("取款成功！")
            bank.selectUser (account, password)
    elif su == 4:
        print ("****转账****")
        output = inputHelp ("转出的账号")
        input = inputHelp ("转入的账号")
        outputpass = inputHelp ("转出的密码")
        outputmoney = inputHelp ("要转出的金额", "int")

        f = bank.zz (output, input, outputpass, outputmoney)

        if f == 1:
            print ("转出或转入的账号不存在！")
        elif f == 2:
            print ("输入密码错误！")
        elif f == 3:
            print ("转账金额不足！")
        else:
            print ("转账成功！")
            print ("您的个人信息：")
            bank.selectUser (output, outputpass)
    elif su == 5:
        account = inputHelp ("账号")
        password = inputHelp ("密码")
        bank.selectUser (account, password)
    elif su == 6:
        print ("退出")
        quit ()
    else:
        print ("您输入的数字不对，请重新输入")
        continue
