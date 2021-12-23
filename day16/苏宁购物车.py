'''

苏宁商城选择商品加入购物车

'''
import time

from selenium import webdriver

driver = webdriver.Chrome ()
try:
    # 创建链接
    driver.get ("https://www.suning.com/")
    # 放大窗口
    driver.maximize_window ()
    # xpatl定位并点击
    driver.find_element_by_xpath ('/html/body/div[6]/div[1]/div/div/ul/li[1]/a[1]').click ()
    # 获取窗口数
    ck = driver.window_handles
    # 跳转到指定页面
    driver.switch_to.window (ck[-1])
    # xpath定位到商品并点击
    driver.find_element_by_xpath ('/html/body/div[6]/div[2]/ul/li[1]/a/img').click ()
    time.sleep (2)
    # 获取窗口数
    ck = driver.window_handles
    # 跳转到指定页面
    driver.switch_to.window (ck[-1])
    time.sleep (2)
    # id定位点击添加到购物车
    driver.find_element_by_id ('addCart').click ()
    time.sleep (2)
    # 在弹出的页面点击去购物车结算
    # driver.switch_to.alert.accept()
    driver.find_element_by_xpath ('/html/body/div[38]/div/div[2]/div/div[1]/a').click ()
    # 获取窗口数
    ck = driver.window_handles
    # 跳转到指定页面
    driver.switch_to.window (ck[-1])
    # 点击去去结算按钮
    driver.find_element_by_xpath ('//*[@id="cart-wrapper"]/div[3]/div/div/div[2]/div[2]/a').click ()
except:
    print("别瞎报错，这没错")
else:print(".........")
finally:print("真的吗，我不信")
time.sleep (3)
driver.quit ()
