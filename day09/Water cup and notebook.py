'''


分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体

'''


class Waterglass:
    # 高度
    high = 0
    # 容积
    capacity = 0.0
    # 颜色
    color = ""
    # 材质
    material = ""

    # 功能
    # 存放液体
    def store(self, ):
        print ("一个材质为：", self.material,
               "高度为：", self.high, "厘米",
               "颜色为：", self.color, "的杯子，",
               "存放了", self.capacity, "l的水。"

               )


# 给杯子的属性赋值
# 把类赋值给变量w
w = Waterglass ()
# 调用类的变量进行赋值
w.high = 13
w.color = "黄色"
w.capacity = 0.77
w.material = "304不锈钢"
w.store ()


# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
class notebook:
    # 定义笔记本属性
    __screen = 0.0
    __price = 0
    __model = ""
    __standby = 0

    def setScreen(self, screen):
        if screen < 0:
            print ("?????")
        else:
            self.__screen = screen

    def getScreen(self):
        return self.__screen

    def setPrice(self, price):
        if price < 0:
            print ("?????")
        else:
            self.__price = price

    def getPrice(self):
        return self.__price

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        self.__model

    def setStandby(self, standby):
        if standby <= 0:
            print ("???????????????????????????????")
        else:
            self.__standby = standby

    def getStandby(self):
        return self.__standby

    # 行为（打字，打游戏，看视频
    def typing(self):
        print ("这一款大小为：", self.__screen, "英寸的电脑", "可以打", self.__standby, "小时的字")

    def playGame(self):
        print ("这一款cpu型号为：", self.__model, "的电脑", "可以打各种大型游戏")

    def video(self):
        print ("这一款价格为：", self.__price, "的电脑", "可以看", self.__standby, "小时的视频")


n = notebook ()
n.setScreen (15.6)
n.setModel ("i9-12980xe")
n.setPrice (9999)
n.setStandby (6)
n.playGame ()
n.typing ()
n.video ()
# n.screen=15.6
# n.price=8999
# n.model="i9-12900K"
# n.memory=1000
# n.standby=3
# n.playGame()
# n.typing()
# n.video()
