'''
当篮子蛋挞已经满了，停个3秒钟每个客户都有30000元,
然后在判断是否已满，没满，扔一个到篮
同时抢蛋挞分钟
蛋挞篮子：最多500
'''
from threading import Thread
import time

# 蛋挞篮子
egg = 1
count = 0
wage = 0


# 厨师
class cook (Thread):
    username = ""

    # 重写run方法

    def run(self) -> None:
        global egg
        while True:
            if egg <= 500:
                egg = egg + 1
                print (self.username,
                       "做了一个蛋挞\n",
                       "篮子里现在有",
                       egg, "个蛋挞")
            # 篮子满了停3秒
            else:
                time.sleep (3)
                print ("篮子满了停3秒")
                break


# 消费者
class consumers (Thread):
    username = ""
    money = 30000

    # 重写run方法
    def run(self) -> None:
        global egg
        global count
        global wage
        while self.money >= 3:
            if egg > 0:
                self.money = self.money - 3
                print (self.username, "买了", egg, "个蛋挞,\n净收入", self.money, "元钱")
            else:
                print ("没钱买什么蛋挞？")
            count = count + 3
            wage = wage + 1.5
            break


# 收银员
class cashier ():
    global count
    global wage
    global egg
    while egg:
        print ("共收入", count,
               "元\n", "要发工资",
               wage, "元\n", "剩余",
               count - wage, "元")
        break

c = cook ()
c1 = cook ()
c2 = cook ()
c.username = "张富贵"
c1.username = "王富贵"
c2.username = "李富贵"
c.start ()
c1.start ()
c2.start ()
o = consumers ()
o1 = consumers ()
o2 = consumers ()
o3 = consumers ()
o4 = consumers ()
o5 = consumers ()
o.username = "王富贵1"
o1.username = "王富贵2"
o2.username = "王富贵3"
o3.username = "王富贵4"
o4.username = "王富贵5"
o5.username = "王富贵6"
o.start ()
o1.start ()
o2.start ()
o3.start ()
o4.start ()
o5.start ()
