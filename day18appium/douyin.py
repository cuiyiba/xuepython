'''

 "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme/.splash.SplashActivity"

'''

from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

url = "127.0.0.1:4723/wd/hub"

param = {
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}

driver = webdriver.Remote (url, param)  #
sleep (3)
el1 = driver.find_element_by_id ("com.ss.android.ugc.aweme:id/bdb")
el1.click ()
sleep (3)
el2 = driver.find_element_by_id ("com.android.packageinstaller:id/permission_deny_button")
el2.click ()
sleep (1)
el3 = driver.find_element_by_id ("com.android.packageinstaller:id/permission_deny_button")
el3.click ()
sleep (1)
while True:
    TouchAction (driver).long_press (x=452, y=1000).move_to (x=500, y=200).release ().perform ()
    sleep (10)


