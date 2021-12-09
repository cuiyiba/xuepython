'''

定义一个空调类和对应的测试类
要求：
1、空调有品牌和价格两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
2、提供一个无返回值的无参数的开机的方法，内容打印一句话：“空调开机了...”；
3、提供一个无返回值的带1个int类型参数的定时关机的方法,(int类型的参数表示设定的分钟数)，
    内容打印一句话：“空调将在xxx分钟后自动关闭...”；
4、在测试类中创建出空调对象，并给空调的品牌和价格赋任意值；
5、使用空调对象获取空调的品牌和价格并打印到控制台上；
6、使用空调对象调用开机方法；
7、使用空调对象调用定时关机方法，并传递具体数据值，在控制台上可以看到的效果为：空调将在xxx分钟后自动关闭...
其中语句中的“xxx”是调用方法时传递的具体数据值；
'''

import time
class conditioner:
    # 品牌
    __brand = ""
    # 价格
    __price = 0

    # 私有属性的方法
    def setBrand(self, brand):
        if brand != False:
            self.__brand = brand
        else:
            print ("????????????")

    def getBrand(self):
        return self.__brand

    def setPrice(self, price):
        if price >= 0:
            self.__price = price
        else:
            print ("????")

    def getPrice(self):
        return self.__price

    # 提供一个无返回值的无参数的开机的方法，内容打印一句话：“空调开机了...”；
    def boot(self):
        print (self.__brand, "品牌的空调开机了...\n它的售价为", self.__price, "元")

    # 提供一个无返回值的带1个int类型参数的定时关机的方法, (int类型的参数表示设定的分钟数)，
    # 内容打印一句话：“空调将在xxx分钟后自动关闭...
    def off(int, fen):
        print ("空调将在", fen, "分钟后自动关闭")
        for i in range(fen):
            print(".",end="")
            time.sleep(60)

# 在测试类中创建出空调对象，并给空调的品牌和价格赋任意值；
c = conditioner()
c.setBrand ("格力")
c.setPrice (5626)
# 使用空调对象获取空调的品牌和价格并打印到控制台上
c.boot ()
# 使用空调对象调用定时关机方法，并传递具体数据值，
# 在控制台上可以看到的效果为：空调将在xxx分钟后自动关闭...
# 其中语句中的“xxx”是调用方法时传递的具体数据值；
c.off(3)