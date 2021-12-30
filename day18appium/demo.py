
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

url = "127.0.0.1:4723/wd/hub"

param = {
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.coolapk.market",
    "appActivity": "com.coolapk.market.view.main.MainActivity"
}

driver = webdriver.Remote (url, param)  #

time.sleep (2)
TouchAction (driver).tap (x=188, y=1484).perform ()
TouchAction (driver).tap (x=446, y=1552).perform ()
time.sleep (1)
TouchAction (driver).tap (x=99, y=170).perform ()
time.sleep (17)
TouchAction (driver).press (x=438, y=1000).move_to (x=438, y=200).release().perform()
time.sleep (15)
driver.quit ()
