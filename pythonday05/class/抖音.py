from appium import webdriver
import time


server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',          # 需替换成你的driverName
    'platformVersion': '7.1.2',
    'appPackage': 'com.ss.android.ugc.aweme',
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity'
}
driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
time.sleep(8)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb").click()
num = 0
while True:
    time.sleep(5)
    start_x = 500
    start_y = 1300
    distance = 1000
    driver.swipe(start_x, start_y, start_x, start_y - distance)
    num = num+1

    if num == 3:
        break
driver.quit()


