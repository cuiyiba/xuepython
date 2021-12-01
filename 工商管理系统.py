from random import randint  # abc

# 定义一个字典用来放用户信息
yhxi = {
    1: {
        "账号": 1,
        "姓名": "cuierba",
        "密码": "mm",
        "国家": "gj",
        "省份": "sf",
        "街道": "jd",
        "余额": 100,
        "开户行": "昌平沙河"
    }
}
while True:
    print ("#######中国工商银行账户管理系统######")
    print ("#        1.添加用户                #")
    print ("#        2.存钱                    #")
    print ("#        3.取钱                    #")
    print ("#        4.转账                    #")
    print ("#        5.查询用户                #")
    print ("#        6.退出                    #")
    print ("###################################")
    su = input ("请输入数字选择对应业务：")
    su = int (su)


    # 添加用户
    def adduser():
        Ran = randint (10000000, 99999999)
        xm = input ("请输入您的姓名：")
        mm = input ("请输入您的密码")
        gj = input ("请输入您的国家：")
        sf = input ("\t请输入您的省份：")
        jd = input ("\t\t请输入您的街道")
        ck = input ("请输入预存金额：")
        ck = int (ck)
        kh = "昌平沙河分行"
        dc = yhxiadd (Ran, xm, mm, gj, sf, jd, ck, kh)
        if dc == 1:
            print ("用户信息添加成功,以下为您的信息")
            for i, y in yhxi[Ran].items ():
                print ("\t\t", i, ":", y)
        elif dc == 2:
            print ("请使用其他用户")
        elif dc == 3:
            print ("数据库已满")


    # 把信息存到字典里
    def yhxiadd(Ran, xm, mm, gj, sf, jd, ck, kh):
        if Ran in yhxi:
            return 2
        elif len (yhxi) >= 100:
            return 3
        yhxi[Ran] = {
            "账号": Ran,
            "姓名": xm,
            "密码": mm,
            "国家": gj,
            "省份": sf,
            "街道": jd,
            "余额": ck,
            "开户行": kh
        }
        return 1


    # 存钱
    def chunqian():
        cq = input ("请输入您的账号：")
        cq = int (cq)
        print (yhxi)
        if cq in yhxi:
            for i, y in yhxi[cq].items ():
                print (i, ":", y)
            je = input ("请输入存款金额：")
            je = int (je)
            je = yhxi[cq]["余额"] + je
        yhxi[cq].update ({"余额": je})
        print ("存款成功，您的信息已变更")
        for i, y in yhxi[cq].items ():
            print (i, ":", y)


    # 取钱
    def quqian():
        qq = input ("请输入您的账号：")
        qq = int (qq)
        print (yhxi)
        if qq in yhxi:
            for i, y in yhxi[qq].items ():
                print (i, ":", y)
            je = input ("请输入取款金额：")
            je = int (je)
            je = yhxi[qq]["余额"] - je
        yhxi[qq].update ({"余额": je})
        print ("取款成功，您的信息已变更")
        for i, y in yhxi[qq].items ():
            print (i, ":", y)


    # 转账
    def zz():
        hk = input ("请输入您的账号：")
        hk=int(hk)#改成int类型
        if hk in yhxi:  # 打印用户信息
            for i, y in yhxi[hk].items ():
                print (i, ":", y)
        sq = input ("请输入收款人账号")
        sq = int (sq)
        if sq in yhxi and sq != hk:
            sqzh = input ("请输入转账数额：")
            sqzh = int (sqzh)
            if sqzh <= yhxi[hk]["余额"]:  # 判断转账的金额是否大于余额
                a = yhxi[hk]["余额"] - sqzh  # 转账后的剩余金额
                yhxi[hk].update ({"余额": a})  # 更改进字典
                b = yhxi[sq]["余额"] + sqzh  # 收款账号余额增加
                yhxi[sq].update ({"余额": b})  # 更改进字典
                for i, y in yhxi[hk].items ():  # 遍历汇款人信息
                    print (i, ":", y)
                print ("汇款成功",yhxi[sq]["余额"])  # 打印收款人余额
            else:
                print ("余额不足")
        elif sq in yhxi and sq == hk:
            print ("玩呢？")
        else:
            print ("查无此人！！！")


    # 判断键入的数字
    if su == 1:
        print ("****添加用户****")
        adduser ()
    elif su == 2:
        print ("****存钱****")
        chunqian ()
    elif su == 3:
        print ("****取钱****")
        quqian ()
    elif su == 4:
        print ("****转账****")
        zz()
    elif su == 5:
        print ("****查询用户****")
        cx = input ("请输入您的账号")
        if cx in yhxi:
            for i, y in yhxi[cx].items ():
                print (i, ":", y)
        else:
            print ("用户不存在")
    elif su == 6:
        print ("退出")
        quit()
    else:
        print ("您输入的数字不对，请重新输入")
        continue
