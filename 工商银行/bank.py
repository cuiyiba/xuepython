'''
银行类
'''
import random
from DBUtils import update
from DBUtils import select

bank_name = "中国工商银行昌平支行"
# 账号
def getRandom(self):
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range (8):
        string = string + li[int (random.random () * len (li))]
    return string


class bank:

    # 开户的方法
    def adduser(self, username, password, country, province, street, door, money):
        # 查询是否已满
        sql = "select count(*) from user"  # (5)
        param = []
        data = select (sql, param)
        if len (data) >= 100:
            return 3

        # 查询是否存在
        sql1 = "select * from user where getRandom = %s"
        param1 = [getRandom (self)]
        data1 = select (sql1, param1)
        if len (data1) > 0:
            return 2

        # 插入数据
        else:
            sql2 = " insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param2 = [getRandom (self), username, password, country, province, street, door, money, '2021-12-07', bank_name]
            update (sql2, param2)
        return 1

    # 存钱
    def chunqian(self,account,money):
        sql = "select * from user where getRandom = %s"
        param = [account]
        data = select (sql, param)
        if len (data) > 0:
            sql1 = "update user set money = money + %s where getRandom = %s  "
            param1 = [money, account]
            update (sql1, param1)
            return True
        else:
            return False

    # 取钱
    def quqian(self,account,password,money):
        sql = "select * from user where getRandom = %s"
        param = [account]
        data = select (sql, param)
        if len (data) > 0:
            sql1 = "select * from user where password = %s and getRandom = %s "
            param1 = [password, account]
            data1 = select (sql1, param1)
            if len (data1) > 0:
                sql2 = "select * from user where money > %s and getRandom = %s"
                param2 = [money, account]
                data2 = select (sql2, param2)
                if len (data2) > 0:
                    sql3 = "update user  set money = money - %s  where getRandom = %s"
                    param3 = [money, account]
                    update (sql3, param3)
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1

    # 转账
    def zz(self,outputaccount,inputaccount,outputpassword,outputmoney):
        sql = "select * from user where getRandom = %s "
        param = [outputaccount]
        data = select (sql, param)
        if len (data) > 0:
            sql1 = "select * from user where getRandom = %s "
            param1 = [inputaccount]
            data1 = select (sql1, param1)
            if len (data1) > 0:
                sql2 = "select * from user where password = %s and getRandom = %s "
                param2 = [outputpassword, outputaccount]
                data2 = select (sql2, param2)
                if len (data2) > 0:
                    sql3 = "select * from user where money > %s and getRandom = %s"
                    param3 = [outputmoney, outputaccount]
                    data3 = select (sql3, param3)
                    if len (data3) > 0:
                        sql4 = "update user set money = money - %s where getRandom = %s"
                        param4 = [outputmoney, outputaccount]
                        sql5 = "update user set money = money + %s where getRandom = %s"
                        param5 = [outputmoney, inputaccount]
                        update (sql5, param5)
                        update (sql4, param4)
                        return 5
                    else:
                        return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 1

    # 查询
    def selectUser(self, account, password):
        sql = "select * from user where getRandom = %s "
        param = [account]
        data1 = select (sql, param)
        if len (data1) > 0:
            sql1 = "select * from user where password = %s "
            param1 = [password]
            data = select (sql1, param1)
            if len (data) > 0:
                for i in data1[0]:
                    print ("\t\t", i)
            else:
                print ("用户密码错误！")
        else:
            print ("该用户不存在！")
