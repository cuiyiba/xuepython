'''


注册的类
'''
import time

from selenium import webdriver


class zhuce :

    def TestZhuce(uname, pwd, mail, phone):
        # 创建链接
        driver = webdriver.Chrome ()
        # 进入指定页面
        driver.get ("http://localhost:8080/HKR")
        # 全屏
        driver.maximize_window ()
        # 找到注册链接，并点击
        driver.find_element_by_xpath ('/html/body/div/div/div[1]/div[2]/a[1]').click ()
        # 模拟输入姓名
        driver.find_element_by_xpath ('//*[@id="loginname"]').send_keys (uname)
        # 模拟输入真实姓名
        driver.find_element_by_xpath ('//*[@id="msform"]/fieldset[1]/input[2]').send_keys (uname)
        # 模拟输入密码
        driver.find_element_by_xpath ('//*[@id="pwd"]').send_keys (pwd)
        # 确认密码
        driver.find_element_by_xpath ('//*[@id="msform"]/fieldset[1]/input[4]').send_keys (pwd)
        # 点击提交
        driver.find_element_by_xpath ('//*[@id="msform"]/fieldset[1]/input[5]').click ()
        time.sleep (2)
        # 下一步
        driver.find_element_by_xpath ('//*[@id="msform"]/fieldset[2]/input[3]').click ()
        # 填写邮箱
        driver.find_element_by_xpath ('//*[@id="reg_mail"]').send_keys (mail)
        # 填写电话号
        driver.find_element_by_xpath ('//*[@id="reg_phone"]').send_keys (phone)
        # 点击注册
        driver.find_element_by_xpath ('//*[@id="btn_reg"]').click ()
        time.sleep (15)
        # 关闭程序
        driver.quit ()
