'''
请编程
i.人：年龄，性别，姓名。

ii.现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。

iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。

'''


class people:
    __name = ""
    __age = 0
    __sex = ''

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setSex(self, sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex
class worker(people):

    def work(self):
        print(self.getName(),
              "是一位",self.getSex(),
              "士.\n他今年",self.getAge(),"他正在搬砖")
class student(people):
    def xuexi(self):
        print(self.getName(),
              "是一位",self.getSex(),
              "士.\n他今年",self.getAge(),"他正在xuexi")
class ss(worker,student):
    w=worker()
    s=student()
    w.setName("asa")
    w.setAge(55)
    w.setSex('男')
    w.work()
    s.setName ("a")
    s.setAge (5)
    s.setSex ('男')
    s.xuexi()

