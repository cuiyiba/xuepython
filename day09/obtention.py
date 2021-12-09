'''
    面向过程：
        C,C++
    面向对象：
        oak --> java
    自然界：
        模型，图纸    ->    车
        车：
            属性: 车轮胎数，车身颜色，品牌，
            行为(方法)：跑，拉货
        python描述一辆车：
            class类：


'''
# 车类图纸
class Car:
    num = 0
    color = ""
    brand = ""

    def run(self):
        print(self.brand,"品牌的车在跑！")

# 造车
c = Car()

# 给属性赋值
c.num = 5
c.color = "绿色"
c.brand = "柯尼塞格" #

c.run()




























