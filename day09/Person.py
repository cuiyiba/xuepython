'''
    人：
        属性：姓名，性别，年龄，身高
        行为：吃，学习，打游戏，睡觉
    1.封装
        1.1 先将属性隐藏
            __属性
        1.2 提供set/Get用于间接赋值和间接取值
'''
import time
class Person:
    __username = ""
    __sex = ""
    __age = 0
    __high = 0.0


    def setHigh(self,high):
        if high > 2.72  or high  < 0:
            print("身高非法！ 别瞎弄！")
        else:
            self.__high = high

    def getHigh(self):
        return self.__high

    def setSex(self,sex):
        if sex != "男" and sex != "女":
            print("你是泰国来的吗？")
        else:
            self.__sex = sex

    def getSex(self):
        return self.__sex



    def setAge(self,age):
        if age > 120  or age < 0:
            print("年龄非法，禁止输入！")
        else:
            self.__age  = age

    def getAge(self):
        return  self.__age

    def setUsername(self,username):
        if username == "":
            print("姓名不能为空！别瞎弄！")
        else:
            self.__username = username

    def getUsername(self):
        return self.__username



    def eat(self,eatName):
        print(self.__username ,"正在吃",eatName)

    def learn(self,subject,hour):
        print(self.__username,"正在学习",subject,",已经学了",hour,"小时！")

    def playGame(self,gameName,hour):
        print(self.__username,"正在玩【",gameName,"】")
        for i in range(2):
            print(".",end="")
            time.sleep(1)
        print("[timi-光子工作室]")
        print("游戏已经玩了",hour,"小时！")

    def sleep(self,hour):
        print(self.__username,"正在睡觉，已经睡了",hour,"小时！")

    def showMe(self):
        print("我叫",self.__username,"，今年",self.__age,",身高",self.__high,"，我是",self.__sex,"性")

p = Person()

# p.username = "刘备"
p.setUsername("刘备")
# p.age = -56
p.setAge(-56)
# p.high = 1.76
p.setHigh(1.76)
# p.sex = "男"
p.setSex("男")


p.eat("小汉堡")
p.learn("匡扶汉室",2)
p.playGame("三国志",10)
p.sleep(10)

p.showMe()


























