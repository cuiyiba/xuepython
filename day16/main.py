'''

操作页面


'''
from selenium import webdriver
import time
from  selenium.webdriver.common.action_chains import ActionChains
driver= webdriver.Chrome()


#滑动验证
#创建连接
# driver.get(r"F:\汉科软\自动化\练习的html\滑动验证\mousedrag.html")
# #打包滑块赋值给hd
# hd=driver.find_element_by_xpath('//*[@id="box"]/div[3]')
# #把driver交给事件链执行
# hdl=ActionChains(driver)
# #hdl驱动鼠标，点住滑块包  从300滑倒0             立即执行
# hdl.click_and_hold(hd).move_by_offset(300,0).perform()#立即执行




#上传文件和下拉列表
# #创建链接
# driver.get(r"F:\汉科软\自动化\练习的html\上传文件和下拉列表\autotest.html")
# #根据ID定位下拉框并点击
# driver.find_element_by_id("areaID").click()
# #定位下拉框内选项并点击
# driver.find_element_by_xpath('//*[@id="areaID"]/option[2]').click()
# #再次点击下拉框以收回下拉状态
# driver.find_element_by_id("areaID").click()
# #id定位选项框并点击
# driver.find_element_by_id("sexID2").click()
# #xpath定位选项框并点击
# driver.find_element_by_xpath('/html/body/form/table/tbody/tr[5]/td/input[4]').click()
# #选择文件赋给file
# file=driver.find_element_by_name("file")
# #选择要上穿的文件路径
# file.send_keys(r"F:\汉科软\自动化\练习的html\上传文件和下拉列表\autotest.html")
# #查看文件是否上传的了内存
# print(file.get_attribute('value'))  # check value
# #点击提交按钮
# driver.find_element_by_id('buttonID').click()














#弹框验证
# #创建链接
# driver.get(r"F:\汉科软\自动化\练习的html\弹框的验证\dialogs.html")
# #坐标定位点击
# driver.find_element_by_id("alert").click()
# #在弹出的弹框页面点击确定
# driver.switch_to.alert.accept()
# #间隔两秒
# time.sleep(2)
# #ID定位坐标。点击
# driver.find_element_by_id("confirm").click()
# #在弹出的弹框页面点击取消
# driver.switch_to.alert.dismiss()
#









#窗口跳转验证
# #创建链接
# driver.get(r"F:\汉科软\自动化\练习的html\跳转页面\pop.html")
# #根据ID定位点击
# driver.find_element_by_id("goo").click()
# #获取窗口数量
# w=driver.window_handles
# #定位指定窗口
# driver.switch_to.window(w[-1])
#
# #跳转到的页面根据ID定位输入框，键入值
# driver.find_element_by_id("kw").send_keys("python")
# #点击。
# driver.find_element_by_id("su").click()


















#输入框输入
#文件地址或网页
# driver.get(r"F:\汉科软\自动化\练习的html\main.html")
#在iframe标签内部的用ID找不到需要用到。switch_to.frame方法
# driver.switch_to.frame("frame")
#根据ID进行定位，模拟键入
# driver.find_element_by_id("input1").send_keys("阿达达")

time.sleep(3)
driver.quit()

