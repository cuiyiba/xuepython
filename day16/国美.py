'''


国美商城添加购物车

加鼠标悬停需求

'''
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
#加载驱动
driver=webdriver.Chrome()
#创建链接
driver.get("https://www.gome.com.cn/")
#放大窗口
driver.maximize_window()
#时停
time.sleep(2)
#定位元素
xt=driver.find_element_by_xpath('//*[@id="lisnav"]/li[5]/h3/a[2]')
# 添加悬停事件        鼠标悬停               立即执行
ActionChains(driver).move_to_element(xt).perform()
time.sleep(2)
#定位元素
driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/div/div[5]/div[1]/div[2]/div[1]/ul/div[2]/a[2]').click()
#获取新页面
ck=driver.window_handles
#跳转到指定窗口
driver.switch_to.window(ck[-1])
#定位元素
driver.find_element_by_xpath('//*[@id="gm-9140329384-1131093392"]/div/div/p[1]/a/img').click()
#获取新页面
ak=driver.window_handles
#跳转到指定窗口
driver.switch_to.window(ak[-1])
time.sleep(2)
#定位元素
driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[7]/a[4]').click()
time.sleep(1)
#再次点击
driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[7]/a[4]').click()

#获取新页面
bk=driver.window_handles
#跳转到指定窗口
driver.switch_to.window(bk[-1])
time.sleep(2)
#定位元素
driver.find_element_by_xpath('//*[@id="item-info-body"]/div/div[3]/a[2]').click()
time.sleep (3)
driver.quit ()


